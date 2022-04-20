from .helper import make_sound


class Animal:
    def __init__(self, name: str, sound: str):
        self.name: str = name
        self.sound: str = sound

    def speak(self) -> str:
        return make_sound(self.name, self.sound)
