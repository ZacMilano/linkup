.PHONY: install dev serve start

install:
	./install.sh

dev:
	python -m flask --app main run -p 8080
serve:
	make dev
start:
	make dev
