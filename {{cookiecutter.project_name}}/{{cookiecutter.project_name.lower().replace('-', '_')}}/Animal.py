from .helper import make_sound


class Being:
    """This is a class representing something that has a name."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal(Being):
    def __init__(self, name: str, sound: str):
        super.__init__(name)
        self.sound: str = sound

    def speak(self) -> str:
        return make_sound(self.name, self.sound)
