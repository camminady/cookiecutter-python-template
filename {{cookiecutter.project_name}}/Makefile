SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy {{ cookiecutter.project_name.lower().replace('-', '_') }} tests/*.py
	poetry run black .
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run pytest --ignore=dev/

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit


.PHONY: clean
clean: 
	rm -rf tests/__pycache__ .pytest_cache .mypy_cache {{ cookiecutter.project_name.lower().replace('-', '_') }}/__pycache__ .coverage dev/__pycache__ dev/notebooks/__pycache__


.PHONY: install
install:
	poetry config virtualenvs.in-project true
	poetry install




.PHONY: gitsetup
gitsetup:
	git config --global init.defaultBranch main
	git init
	git remote add origin git@github.com:{{ cookiecutter.organization }}/{{ cookiecutter.project_name.lower()}}.git
	git branch -M main

.PHONY: gitfirst
gitfirst:
	git add .
	git add .editorconfig .gitignore .readthedocs.yml .github
	git commit -am "Initial commit, adding all files."
	git push -u origin main
	

.PHONY: all
all:
	poetry config --local virtualenvs.in-project true
	poetry install
	make gitsetup
	make gitfirst

