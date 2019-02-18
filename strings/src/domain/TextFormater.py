import abc


class TextFormater(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def format(self, text: str, length: int, justified: bool):
        pass
