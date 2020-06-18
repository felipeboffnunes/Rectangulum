from textwrap import dedent
from random import randint, shuffle
from components.create_table import create_table

def create_all_tex(template, layout) -> list:
    style = template.styles[randint(0,len(template.styles)-1)]
    parameter = template.parameters[randint(0,len(template.parameters)-1)]
    
    all_tex = [[create_tex(template, style, parameter, "blank", layout), "blank", template.CLS["blank"], 0]]
    for category, _ in template.CATEGORIES:
        n = layout[category]
        cls = False
        for category_key in template.CLS:
            if category == category_key:
               category_path = template.CLS[category_key]
               all_tex.append([create_tex(template, style, parameter, category, layout), category, category_path, n])
               cls = True
               break
        if not cls and category != "blank":
           category_path = template.CLS["blank"]
           all_tex.append([create_tex(template, style, parameter, "blank", layout), category, category_path, n])
           cls = False
        
    return all_tex

def create_tex(template, style, parameter, category, layout_aux) -> str:

    if repr(template) == "ACMART":
        layout = create_tex_ACMART(template, style, parameter, category, layout_aux)
    
    return layout

def create_tex_ACMART(template, style, parameter, category, layout_aux):
    layout = ""
    if category == None:
        layout += dedent(template.create_documentclass(style, parameter))
    else:
        layout += dedent(template.create_documentclass(style, parameter, category))
    
    layout += dedent(template.create_usepackage())
    layout += dedent(template.setup_references())
    layout += dedent(template.create_acm_setup())
    layout += dedent(template.setup_boxes())

    layout += dedent(template.create_begin_document())
    
    layout += dedent(template.create_title())
    layout += dedent(template.create_author())
    layout += dedent(template.create_abstract())
    layout += dedent(template.create_ccs())
    layout += dedent(template.create_keywords())
    layout += dedent(template.create_maketitle())

    # Dynamic part
    random_parts = []
    for title, text in layout_aux["section-title"]:
        part = ""
        part += dedent(template.create_tfbox())
        part += dedent(template.create_begin_section(title, "cfboxa" if category == "section-title" or category == "all" else "tfboxa"))
        part += dedent(template.create_paragraph(text, "cfboxa" if category == "text" or category == "all" else "tfboxa"))
        part += dedent(template.end_tfbox())
        random_parts.append(part)

    for table in layout_aux["tables"]:
        part = ""
        part += dedent(template.create_table(table, "cfboxa" if category == "tables" or category == "all" else "tfboxa"))
        random_parts.append(part)
        
    shuffle(random_parts)
    for part in random_parts:
        layout += part
    
    layout += dedent(template.print_references())

    layout += dedent(template.create_end_document())
    return layout

def download_tex(idx, tex, category, n_box): 
    name = f"{idx}_{category}_{n_box}.tex"
    with open(name, "w") as f:
        f.write(tex)
    return name