# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/workflows/test/badge.svg?branch=main&event=push)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions)
[![codecov](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})

{{ cookiecutter.project_description }}


## How to install this package in another `dspkg-package` 
When using `zsh`, run

```poetry add git+ssh://git@github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git\#main```

With `fish`, run

```poetry add git+ssh://git@github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git#main```



## Example

```python
from {{cookiecutter.project_name.lower().replace('-', '_')}}.Animal import Animal

tiger = Animal("Tiger", "roooar")
tiger.speak()
# => 'The Tiger says roooar.'
```



## Contributing

After changing into the repository, run:
```bash
poetry install
poetry shell
```
This will install all required packages and activate the correct environment.
Add packages via 
```
poetry add matplotlib
```

## Links

[Python Coding Guidelines](https://wahooligans.atlassian.net/wiki/spaces/SCIENCE/pages/23586078720/Python+Coding+Guidelines)

[Documentation](https://htmlpreview.github.io/?https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/main/docs/_build/html/index.html)


