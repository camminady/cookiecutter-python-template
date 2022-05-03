# dspkg-cookiecutter-python-template
[![Build Status](https://github.com/WahooFitness/dspkg-cookiecutter-python-template/workflows/test/badge.svg?branch=main&event=push)](https://github.com/WahooFitness/dspkg-cookiecutter-python-template/actions)
## Guidelines
Our Python coding guidelines are on [Confluence](https://wahooligans.atlassian.net/wiki/spaces/SCIENCE/pages/23586078720/Python+Coding+Guidelines).


## Installation requirements
You need to
```shell
pip install cookiecutter  
pip install jinja2_git
pip install lice
pip install markupsafe==2.0.1
pip install poetry 
```
Alternatively, use `pip3` instead of `pip`.

## Creating a new project
Run
```shell
cookiecutter https://github.com/WahooFitness/dspkg-cookiecutter-python-template
```
You will then be asked to enter the package name and the organization under which the Github repository will live (`WahooFitness` is the default).
## Adding packages 
If your environment needs to use packages like `numpy`, just run
```shell
poetry add numpy
```

## VS Code
Inside a new repository, there is a `.vscode` folder with an `extensions.json` and a `settings.json` file. If you open VSCode and press `cmd+shift+p`, then type `Show recommended extensions` and hit enter, you can install those extensions that are listed in `extensions.json`. 

## Typing
We are using `mypy` which enforces rather strict typing.
