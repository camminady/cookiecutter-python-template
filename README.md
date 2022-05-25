# cookiecutter-python-template


## Installation requirements
You need to
```shell
pip3 install cookiecutter  
pip3 install jinja2_git
pip3 install lice
pip3 install markupsafe==2.0.1
pip3 install poetry 
```
Alternatively, use `pip` instead of `pip3`.

## Creating a new project
Run
```shell
cookiecutter git@github.com:camminady/cookiecutter-python-template
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
