.PHONY: install go

install:
	./install.sh

go:
	python -m flask --app main run
