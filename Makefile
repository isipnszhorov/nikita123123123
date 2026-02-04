# Makefile для проекта VD-games

.PHONY: install run build package-install clean

# Установка зависимостей проекта
install:
	uv sync

# Запуск приложения через uv
run:
	uv run VD-games

# Сборка пакета
build:
	uv build

# Установка собранного пакета в систему
package-install:
	uv tool install dist/*.whl

# Очистка
clean:
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf src/*/__pycache__/
