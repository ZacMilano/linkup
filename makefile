.PHONY: install dev serve start clean

install:
	./install.sh

dev:
	python -m flask --app main --debug run -p 8080
serve:
	make dev
start:
	make dev

clean:
	find . | grep -E "__pycache__" | xargs rm -rf
