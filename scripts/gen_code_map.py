#!/usr/bin/env python3
"""Generate a Markdown code map for the repository.

This script scans the docs/, include/, and src/ directories to produce an
overview of the project structure.  The output includes:
    * a file tree
    * a brief responsibility summary for each file
    * cross-references via `#include "..."`
    * a list of TODO/FIXME notes

The result is written to stdout so it can be redirected to docs/code_map.md.
"""
import os, re, sys, subprocess
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPO_SLUG = "ProgrammingWithYagle/Zombie-Survival-2.0"

def file_last_sha(rel_path: str) -> str:
    """Get the last commit SHA that touched this file."""
    return subprocess.check_output(
        ["git", "log", "-n", "1", "--format=%H", "--", rel_path],
        cwd=ROOT
    ).decode().strip()

def permalink(sha, rel_path, start, end=None):
    quoted = quote(rel_path, safe="/")  # encode spaces, parentheses, etc.
    anchor = f"#L{start}" if end is None or end == start else f"#L{start}-L{end}"
    return f"https://github.com/{REPO_SLUG}/blob/{sha}/{quoted}{anchor}"

SCAN_DIRS = ["docs", "include", "src"]
CODE_EXTS = {".c",".cc",".cpp",".h",".hpp",".hh",".ipp",".inl",".mm",".m",".rs",".py",".java",".js",".ts",".tsx",".cs",".go",".lua"}
COMMENT_PREFIXES = ("//", "#")

def read_text(p: Path):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""

def first_comment_block(p: Path, text: str):
    # For code: capture leading // or /* */. For md/txt: first nonempty line.
    if p.suffix in CODE_EXTS:
        lines = text.splitlines()
        block, start, end = [], None, None
        i = 0
        # line comments
        while i < len(lines) and (lines[i].strip().startswith("//") or lines[i].strip().startswith("#")):
            if start is None: start = i+1
            block.append(lines[i].strip().lstrip("/#").strip())
            end = i+1
            i += 1
        # block comment
        if start is None and i < len(lines) and "/*" in lines[i]:
            start = i+1
            block.append(lines[i].strip())
            i += 1
            while i < len(lines):
                block.append(lines[i].strip())
                if "*/" in lines[i]:
                    end = i+1
                    break
                i += 1
        if start and end:
            summary = " ".join(" ".join(block).split())
            return summary[:200], start, end
    # markdown/plain docs
    for idx, line in enumerate(text.splitlines(), start=1):
        if line.strip():
            return line.strip()[:200], idx, idx
    return None, None, None

def derive_summary_from_path(p: Path):
    if "UI (Interface)" in p.parts:
        return "UI spec / screen outline.", None, None
    if p.suffix == ".md":
        return "Documentation.", None, None
    if p.suffix in {".h",".hpp"}:
        return "Header declarations.", None, None
    if p.suffix in {".c",".cc",".cpp"}:
        return "Source implementation.", None, None
    return "File (needs description).", None, None

include_re = re.compile(r'^\s*#include\s+"([^"]+)"')
todo_re = re.compile(r'\b(TODO|FIXME)\b', re.IGNORECASE)

def collect():
    files = []
    for d in SCAN_DIRS:
        base = ROOT / d
        if not base.exists(): continue
        for p in sorted(base.rglob("*")):
            if p.is_file():
                rel = p.relative_to(ROOT).as_posix()
                files.append((p, rel))
    return files

def build_tree(files):
    # simple textual tree
    lines = []
    by_dir = {}
    for _, rel in files:
        parts = rel.split("/")
        by_dir.setdefault(parts[0], []).append(parts[1:])
    def walk(prefix, entries, depth=0):
        dirs, leafs = {}, []
        for parts in entries:
            if len(parts) == 1:
                leafs.append(parts[0])
            else:
                dirs.setdefault(parts[0], []).append(parts[1:])
        indent = "  " * depth
        if depth == 0:
            for k in sorted(dirs): lines.append(f"{k}/")
            for f in sorted(leafs): lines.append(f"{f}")
        else:
            for k in sorted(dirs): lines.append(f"{indent}{k}/")
            for f in sorted(leafs): lines.append(f"{indent}{f}")
        for k in sorted(dirs):
            walk(prefix+[k], dirs[k], depth+1)
    flat = [(p, rel) for p, rel in files]
    walk([], [rel.split("/") for _, rel in flat], 0)
    return lines

def main():
    files = collect()
    print("# Code Map (auto-generated)\n")
    print("**Do not edit by hand. Run `make codemap` to regenerate.**\n")
    print("## File tree (docs / include / src)\n```")
    for line in build_tree(files):
        print(line)
    print("```\n")

    print("## Responsibilities\n")
    for p, rel in files:
        text = read_text(p)
        summary, s, e = first_comment_block(p, text)
        if not summary:
            summary, s, e = derive_summary_from_path(p)
        print(f"### `{rel}`")
        print(f"{summary}")
        if s:
            link = permalink(file_last_sha(rel), rel, s, e)
            # quote the first line of the block
            block_first = text.splitlines()[s-1].strip()
            print(f"> `{block_first}`  \n> {link}")
        print()

    print("## Cross-references (`#include \"...\"`)\n")
    for p, rel in files:
        if p.suffix not in CODE_EXTS: continue
        lines = read_text(p).splitlines()
        for i, line in enumerate(lines, start=1):
            m = include_re.match(line)
            if m:
                target = m.group(1)
                link = permalink(file_last_sha(rel), rel, i)
                print(f"- `{rel}` ➜ `{target}`  \n  > `{line.strip()}`  \n  > {link}")
    print()

    print("## TODO / FIXME\n")
    any_todo = False
    for p, rel in files:
        text = read_text(p)
        for i, line in enumerate(text.splitlines(), start=1):
            if todo_re.search(line):
                any_todo = True
                link = permalink(file_last_sha(rel), rel, i)
                print(f"- `{rel}:{i}`  \n  > `{line.strip()}`  \n  > {link}")
    if not any_todo:
        print("_No TODO/FIXME found._")

if __name__ == "__main__":
    sys.exit(main())
