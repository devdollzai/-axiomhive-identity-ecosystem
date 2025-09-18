.PHONY: install lint test build

install:
	pip install -r config/requirements.txt

lint:
	flake8 src/

test:
	pytest

build:
	docker build -t axiomhive-identity-ecosystem .
