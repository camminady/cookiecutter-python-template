# cookiecutter-python-package-template

[![Build Status](https://github.com/camminady/cookiecutter-python-package-template/workflows/test/badge.svg?branch=main&event=push)](https://github.com/camminady/cookiecutter-python-package-template/actions)
[![codecov](https://codecov.io/gh/camminady/cookiecutter-python-package-template/branch/main/graph/badge.svg)](https://codecov.io/gh/camminady/cookiecutter-python-package-template)
[![Python Version](https://img.shields.io/pypi/pyversions/cookiecutter-python-package-template.svg)](https://pypi.org/project/cookiecutter-python-package-template/)

A cookiecutter template for Python packages.





## Installation

```bash
pip install git+https://github.com/camminady/cookiecutter-python-package-template.git
```


## Example

```python
from cookiecutter_python_package_template.Animal import Animal

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

[License](https://github.com/camminady/cookiecutter-python-package-template/blob/main/LICENSE)

[Documentation](https://htmlpreview.github.io/?https://github.com/camminady/cookiecutter-python-package-template/blob/main/docs/_build/html/index.html)

