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
            else: layout[category] = []
        else:
            layout[category] = ["n"]
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