from components.templates.acmart import ACMART
from components.create_table import create_table
from faker import Faker
from random import randint, shuffle
import os

ORIGINAL_PATH = os.getcwd()
IMG_PATH = f"{ORIGINAL_PATH}\\data\\images"

def select_layout(idx):
    template = ACMART()
    layout = {}
    layout_order_n = 0
    for category, n in template.CATEGORIES:
        if category != "all":
            if n == "n":
                n = template.randint(1, 5)
            layout[category] = n
            if category == "tables":
                layout[category] = [create_table()] * n
                layout_order_n += n
            elif category == "section-title":
                layout[category] = [create_section_title()] * n
                layout_order_n += n
            elif category == "keywords":
                layout[category] = [create_keywords(n)]
            elif category == "abstract":
                layout[category] = [create_abstract()]
            elif category == "title":
                layout[category] = [create_title()]
            elif category == "author-name":
                layout[category] = [create_author()] * n
            elif category == "ccs":
                layout[category] = [create_ccs()]
            elif category == "images":
                layout[category] = create_image(n)
                layout_order_n += n
            else: layout[category] = []
        else:
            layout[category] = ["n"]
    layout_order_n = list(range(layout_order_n))
    shuffle(layout_order_n)
    layout["layout_order"] = layout_order_n
    return (template, layout)

def create_section_title():
    fake = Faker()
    section_title = fake.name()
    text = fake.text()
    content = [section_title, text]
    return content
   
def create_keywords(n):
    fake = Faker()
    content = ""
    for _ in range(n):
        content += f"{fake.name()}, "
    return content[:-2]

def create_abstract():
    fake = Faker()
    content = fake.text()
    return content
    
def create_title():
    fake = Faker()
    content = fake.name()
    return content

def create_author():
    fake = Faker()
    author = {}
    author["name"] = fake.name()
    author["affiliation"] = fake.name()
    return author
    
def create_ccs():
    return f"""
    	\\begin{{CCSXML}}
        <ccs2012>
        <concept>
        <concept_id>10010520.10010553.10010562</concept_id>
        <concept_desc>Computer systems organization~Embedded systems</concept_desc>
        <concept_significance>500</concept_significance>
        </concept>
        <concept>
        <concept_id>10010520.10010575.10010755</concept_id>
        <concept_desc>Computer systems organization~Redundancy</concept_desc>
        <concept_significance>300</concept_significance>
        </concept>
        <concept>
        <concept_id>10010520.10010553.10010554</concept_id>
        <concept_desc>Computer systems organization~Robotics</concept_desc>
        <concept_significance>100</concept_significance>
        </concept>
        <concept>
        <concept_id>10003033.10003083.10003095</concept_id>
        <concept_desc>Networks~Network reliability</concept_desc>
        <concept_significance>100</concept_significance>
        </concept>
        </ccs2012>
        \\end{{CCSXML}}
        \\ccsdesc[500]{{Computer systems organization~Embedded systems}}
        \\ccsdesc[300]{{Computer systems organization~Redundancy}}
        \\ccsdesc{{Computer systems organization~Robotics}}
        \\ccsdesc[100]{{Networks~Network reliability}}
        """
        
def create_image(n):
    faker = Faker()
    paths = []
    for i in range(n):
        zeros = "0" * (5 - len(str(n)))
        paths.append([f"{zeros}{i+1}.png", faker.name()])
    return paths