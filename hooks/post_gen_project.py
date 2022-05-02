# -*- coding: utf-8 -*-

"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os


# Get the root project directory:
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# We need these values to generate correct license:
ORGANIZATION = "{{ cookiecutter.organization }}"


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    message = f"""
    Your project {PROJECT_NAME} is created.
    Now you can start working on it:

        cd {PROJECT_NAME}
    
    Useful steps that might follow:
    
        git  init 
        poetry install
        poetry shell
        
    If you have created an empty repository at git@github.com:{ORGANIZATION}/{PROJECT_NAME}.git you can run:
    
        make gitsetup
        make gitfirst
        
    This adds all files and pushes to the repository.
    
    Good luck hacking! 
    """
    print(message)  # noqa: WPS421


print_futher_instuctions()
