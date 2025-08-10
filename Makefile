.PHONY: codemap
codemap:
	python scripts/gen_code_map.py > docs/code_map.md
	@echo "Updated docs/code_map.md"
