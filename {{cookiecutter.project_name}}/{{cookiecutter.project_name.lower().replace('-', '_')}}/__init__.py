# We want to expose the animal class, but not the being
# This allows using the Animal class as: from {{cookiecutter.project_name}} import Animal
# If users still want to use the being, they can import {{cookiecutter.project_name}}.animal.Being
from .Animal import Animal
