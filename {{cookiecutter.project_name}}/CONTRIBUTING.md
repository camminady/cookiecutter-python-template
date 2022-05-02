# How to contribute


## Dependencies

We use [poetry](https://github.com/python-poetry/poetry) to manage the dependencies.

To install them you would need to run `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.


## One magic command

Run `make test` to run everything we have!


## Tests

We use `pytest` and `black` for quality control.

To run all tests:

```bash
pytest
```

## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
mypy {{ cookiecutter.project_name.lower().replace('-', '_') }} tests/**/*.py
```

This step is mandatory during the CI.

## Poetry
If you haven't, install [Poetry](https://python-poetry.org/docs/cli/):
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# you might also have to run
# echo "$HOME/.poetry/bin" >> $GITHUB_PATH
```


## Getting the repo
```
git clone git@github.com:{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
make install
```


## Installing and updating dependencies 
If you have to install more packages, you can do so via:
```bash
poetry add somepackage
poetry lock
```

If you want to use and develop this package, it might be handy to install it _editable_:
```bash
pip install -e .
```
