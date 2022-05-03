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
    
    
                    
    
    ##############################################################################
    #                                                                            #
    #                 __          __     _    _  ____   ____                     #
    #                 \ \        / /\   | |  | |/ __ \ / __ \                    #
    #                  \ \  /\  / /  \  | |__| | |  | | |  | |                   #
    #                   \ \/  \/ / /\ \ |  __  | |  | | |  | |                   #
    #                    \  /\  / ____ \| |  | | |__| | |__| |                   #
    #                     \/  \/_/    \_\_|  |_|\____/ \____/                    #
    ##############################################################################                                                                                                                                                        
    #
    #   Your project {PROJECT_NAME} is created.                                          
    #   Create an empty repository at:                                                   
    #   git@github.com:{ORGANIZATION}/{PROJECT_NAME}.git                                 
    #                                                                                     
    #   To install all packages, initializes git, add all files, and push,               
    #   just run:                                                                                                                                                          
                      
     cd {PROJECT_NAME}
     git  init 
     poetry install
     make gitsetup
     make gitfirst
    

    """
    print(message)  # noqa: WPS421


print_futher_instuctions()
