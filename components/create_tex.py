from inspect import cleandoc
from random import randint, shuffle
from components.create_table import create_table

def create_all_tex(template, layout) -> list:
    style = template.styles[randint(0,len(template.styles)-1)]
    parameter = template.parameters[randint(0,len(template.parameters)-1)]
    
    all_tex = [[create_tex(template, style, parameter, "blank", "blank", layout), "blank", template.CLS["blank"], 0]]

    for category, _ in template.CATEGORIES:
        n = len(layout[category])
        cls = False
 
        for category_key in template.CLS:
            if category == category_key:
               category_path = template.CLS[category_key]
               all_tex.append([create_tex(template, style, parameter, category, category, layout), category, category_path, n])
               cls = True
               break
        if not cls and category != "blank":
           category_path = template.CLS["blank"]
           all_tex.append([create_tex(template, style, parameter, "blank" , category, layout), category, category_path, n])
           cls = False
    return all_tex

def create_tex(template, style, parameter, category, category_aux, layout_aux) -> str:

    if repr(template) == "ACMART":
        layout = create_tex_ACMART(template, style, parameter, category, category_aux, layout_aux)
    
    return layout

def create_tex_ACMART(template, style, parameter, category, category_aux, layout_aux):
    layout = ""
    if category == None:
        layout += cleandoc(template.create_documentclass(style, parameter))
    else:
        layout += cleandoc(template.create_documentclass(style, parameter, category))
    
    layout += cleandoc(template.create_usepackage())
    layout += cleandoc(template.setup_references())
    layout += cleandoc(template.create_acm_setup())
    layout += cleandoc(template.setup_boxes())

    layout += cleandoc(template.create_begin_document())
    
    layout += cleandoc(template.create_title(layout_aux["title"]))
    for author in layout_aux["author-name"]:
        layout += cleandoc(template.create_author(author))
    layout += cleandoc(template.create_abstract(layout_aux["abstract"]))
    layout += cleandoc(template.create_ccs(layout_aux["ccs"]))
    layout += cleandoc(template.create_keywords(layout_aux["keywords"]))
    layout += cleandoc(template.create_maketitle())

    # Dynamic part
    random_parts = []
    for title, text in layout_aux["section-title"]:
        part = ""
        part += cleandoc(template.create_tfbox())
        part += cleandoc(template.create_begin_section(title, "cfboxa" if category_aux == "section-title" or category_aux == "all" else "tfboxa"))
        part += cleandoc(template.create_paragraph(text, "cfboxa" if category_aux == "text" or category_aux == "all" else "tfboxa"))
        part += cleandoc(template.end_tfbox())
        random_parts.append(part)

    for table in layout_aux["tables"]:
        part = cleandoc("")
        part += cleandoc(template.create_table(table, "cfboxa" if category_aux == "tables" or category_aux == "all" else "tfboxa"))
        random_parts.append(part)
        
    for image, desc in layout_aux["images"]:
        part = cleandoc("")
        part += cleandoc(template.create_image(image if category_aux == "images" or category_aux == "all" else "white.png",\
            desc, "cfboxa" if category_aux == "images" or category_aux == "all" else "tfboxa",\
            "cfboxa" if category_aux == "images-desc" or category_aux == "all" else "tfboxa"))
        random_parts.append(part)
        
    for n in layout_aux["layout_order"]:
        layout += random_parts[n]
    
    layout += cleandoc(template.print_references())

    layout += cleandoc(template.create_end_document())
    return layout

def download_tex(idx, tex, category, n_box): 
    name = f"{idx}_{category}_{n_box}.tex"
    with open(name, "w") as f:
        f.write(tex)
    return name