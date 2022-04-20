# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/workflows/test/badge.svg?branch=main&event=push)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions)
[![codecov](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)

{{ cookiecutter.project_description }}





## Installation

```bash
pip install git+https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}.git
```


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


## Links

[License](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/main/LICENSE)

[Documentation](https://htmlpreview.github.io/?https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/main/docs/_build/html/index.html)

