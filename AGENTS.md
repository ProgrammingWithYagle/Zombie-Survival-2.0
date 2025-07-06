# AGENTS Guidelines

This document provides basic project conventions for all contributors.

## Folder Layout
- `src/` - C++ source files (`.cpp`).
- `include/` - Header files (`.h`).
- `assets/` - Images, audio, and other game assets.
- `docs/` - Long-form documentation and design notes.
- `tests/` - Automated tests and test data.
- `build/` - CMake build directory (should remain untracked).

## C++ Guidelines
- Separate headers and implementations.
- Use `snake_case` for variable and function names.
- Use `PascalCase` for class names.
- Prefer modern C++17 features and include `#pragma once` in headers.
- Indent with four spaces and keep lines under 100 characters when possible.
- Comment complex logic and keep functions focused on a single task.

## Contribution Process
1. Add new `.cpp` files to `src/` and corresponding headers to `include/`.
2. Place new images or audio under `assets/`.
3. Document significant changes in `docs/`.
4. Add tests under `tests/` when introducing new features.
5. Build using CMake:
   ```bash
   cmake -S . -B build
   cmake --build build
   ```
6. Run tests after building:
   ```bash
   ctest --test-dir build
   ```
7. Ensure all tests pass before submitting a pull request.

These guidelines apply to both AI and human contributions.
