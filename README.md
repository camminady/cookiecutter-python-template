# cookiecutter_python_package_template
[![Build Status](https://github.com/WahooFitness/cookiecutter_python_package_template/workflows/test/badge.svg?branch=main&event=push)](https://github.com/WahooFitness/cookiecutter_python_package_template/actions)


## Install requirements
You need to
```
pip install cookiecutter 
pip install jinja2_git
pip install lice
```

## Create new project
```cookiecutter https://github.com/WahooFitness/cookiecutter_python_package_template```


## How to include other private repos
When using `zsh`, run

```poetry add git+ssh://git@github.com/WahooFitness/ds-pathfinder.git\#main```
With `fish`, run

```poetry add git+ssh://git@github.com/WahooFitness/ds-pathfinder.git#main```
