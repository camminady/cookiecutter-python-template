from .helper import make_sound
import logging

logger = logging.getLogger(__name__)


class Being:
    """This is a class representing something that has a name."""

    def __init__(self, name):
        logger.debug("Being with name %s initialized", name)
        self.name = name

    def __str__(self):
        return self.name


class Animal(Being):
    def __init__(self, name: str, sound: str):
        logger.debug("Animal with name %s and sound initialized", name, sound)
        super.__init__(name)
        self.sound: str = sound

    def speak(self) -> str:
        logger.error("Animal %s makes a sound!", self.name, self.sound)
        return make_sound(self.name, self.sound)
