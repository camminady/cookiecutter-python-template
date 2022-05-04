# We want to expose the animal class, but not the being
# This allows using the Animal class as: from {{cookiecutter.project_name}} import Animal
# If users still want to use the being, they can import {{cookiecutter.project_name}}.animal.Being
from .Animal import Animal

# Setup Logging such that by default, no log messages are printed
# The user of this module can subscribe to the logger and print messages if desired
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
