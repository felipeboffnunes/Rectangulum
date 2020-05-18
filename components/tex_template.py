from abc import ABCMeta, abstractmethod
import random

class TexTemplate(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.CATEGORIES = ["title", "subtitle", "aux_text", \
            "section_title", "text", "images", "tables", \
            "authors", "references", "images_desc", "tables_desc"]
       
    def get_random(self):
        return random

    def get_categories(self):
        return self.CATEGORIES

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

    