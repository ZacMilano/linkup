.PHONY: install dev serve start

install:
	./install.sh

dev:
	python -m flask --app main run
serve:
	make dev
start:
	make dev
