from abc import ABCMeta, abstractmethod
import random

CATEGORIES = [["title", 1], ["subtitle", 1], ["abstract", 1], ["aux-info", "n"], \
            ["section-title", "n"], ["text", "n"], ["images", "n"], ["tables", "n"], \
            ["author-name", "n"], ["references", "n"], ["images-desc", "n"], ["tables-desc", "n"], \
            ["all", "n"], ["blank", 0]]

class TexTemplate(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass
       
    def get_random(self):
        return random

    def get_categories(self):
        return CATEGORIES

    @abstractmethod
    def create_documentclass(self, style, parameter, category) -> str:
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

    