import pytest

from {{ cookiecutter.project_name.lower().replace('-', '_') }}.Animal import Animal


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ("tiger", "roooaaar", "roooaaar"),  # Tiger makes roooaaar.
        ("cow", "mooooo", "mooooo"),  # Cow makes mooooo.
    ],
)
def test_some_function(first, second, expected) -> None:
    """Example test with parametrization."""
    animal: Animal = Animal(first, second)
    assert animal.speak() == f"The {first} says {second}."
