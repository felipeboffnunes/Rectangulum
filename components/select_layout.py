from components.templates.acmart import ACMART
from components.create_table import create_table
from faker import Faker

def select_layout(idx):
    template = ACMART()
    layout = {}
    for category, n in template.CATEGORIES:
        if category != "all":
            if n == "n":
                n = template.randint(1, 5)
            layout[category] = n
            if category == "tables":
                layout[category] = [create_table()] * n
            elif category == "section-title":
                layout[category] = [create_section_title()] * n
        else:
            layout[category] = "n"

    return (template, layout)

def create_section_title():
    fake = Faker()
    section_title = fake.name()
    text = fake.text()
    content = [section_title, text]
    return content
   
    
    
