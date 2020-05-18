from textwrap import dedent
from random import randint
MILLION = 7


def create_all_tex(template):
    style = template.styles[randint(0,len(template.styles)-1)]
    parameter = template.parameters[randint(0,len(template.parameters)-1)]
    
    # First create_tex is the original tex, without categories
    all_tex = [[create_tex(template, style, parameter), "original"]]
    for category in template.CATEGORIES:
        all_tex.append([create_tex(template, style, parameter, category), category])
    return all_tex

def create_tex(template, style, parameter, category=None):
    # Needs dinamic logic
    layout = ""
    if category == None:
        layout += dedent(template.create_documentclass(style, parameter))
    else:
        layout += dedent(template.create_documentclass(style, parameter, category))
    layout += dedent(template.create_begin_document())
    layout += dedent(template.create_title())
    layout += dedent(template.create_maketitle())
    layout += dedent(template.create_end_document())
    return layout

def download_tex(idx, tex, category): 
    zeros = "0" * (MILLION - len(str(idx)))
    name = f"{zeros}{idx}_{category}.tex"
    with open(name, "w") as f:
        f.write(tex)
        return name