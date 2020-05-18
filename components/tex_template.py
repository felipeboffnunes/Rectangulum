import abc
import random

class TexTemplate(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        pass
       
    def get_random(self):
        return random

    @abc.abstractmethod
    def create_documentclass(self) -> str:
        pass

    @abc.abstractmethod
    def create_title(self) -> str:
        return

    