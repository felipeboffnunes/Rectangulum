from abc import ABCMeta, abstractmethod
import random

class TexTemplate(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
       
    def get_random(self):
        return random

    @abstractmethod
    def create_documentclass(self, category) -> str:
        pass

    @abstractmethod
    def create_begin_document(self) -> str:
        pass

    @abstractmethod
    def create_maketitle(self) -> str:
        pass

    @abstractmethod
    def create_title(self) -> str:
        pass

    @abstractmethod
    def create_end_document(self) -> str:
        pass

    