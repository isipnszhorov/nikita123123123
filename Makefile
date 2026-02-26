.PHONY: install run build package-install clean

install:
	uv sync

run:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

clean:
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf src/*/__pycache__/

lint:
	uv run ruff check src/vd_games

