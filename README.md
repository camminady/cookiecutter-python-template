# dspkg-cookiecutter-python-template
[![Build Status](https://github.com/WahooFitness/dspkg-cookiecutter-python-template/workflows/test/badge.svg?branch=main&event=push)](https://github.com/WahooFitness/dspkg-cookiecutter-python-template/actions)


## Install requirements
You need to
```
pip install cookiecutter  
pip install jinja2_git
pip install lice
pip install markupsafe==2.0.1
pip install poetry 
```
Alternatively, use `pip3` instead of `pip`.

## Create new project
Run
```cookiecutter https://github.com/WahooFitness/dspkg-cookiecutter-python-template```

## Adding packages 
If your environment needs to use packages like `numpy`, just run
```
poetry add numpy
```
## Typing
We are using `mypy` which enforces rather strict typing.
