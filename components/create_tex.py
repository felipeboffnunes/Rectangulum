from textwrap import dedent
from random import randint
MILLION = 7


def create_all_tex(template) -> list:
    style = template.styles[randint(0,len(template.styles)-1)]
    parameter = template.parameters[randint(0,len(template.parameters)-1)]
    
    # First create_tex is the original tex, without categories
    all_tex = [[create_tex(template, style, parameter, "blank", 0), "original", 1]]
    for category, n_box in template.CATEGORIES:
        # if n_box == "n":
        #    n_box = template.randint(1, 5)
        all_tex.append([create_tex(template, style, parameter, category, n_box), category, n_box])
        # Rethink this
        #cls = True
        #for category_key in template.CLS:
        #    if n_box == "n":
        #       n_box = template.randint(1, 5)
        #    if category == category_key:
        #       all_tex.append([create_tex(template, style, parameter, category, n_box), template.CLS[category], n_box])
        #       cls = False
        #       break
        #   if not cls:
        #       category_path = template.CLS[blank]
        #       all_tex.append([create_tex(template, style, parameter, category, n_box), category_path, n_box])
        #       cls = True
    return all_tex

def create_tex(template, style, parameter, category_path, n_box) -> str:
    if "title-section" in category_path :
        ts_box = "cfboxa"
        p_box = "tfboxa"
        a_box = "tfboxa"
    elif "text" in category_path:
        ts_box = "tfboxa"
        p_box = "cfboxa"
        a_box = "tfboxa"
    elif "abstract" in category_path:
        ts_box = "tfboxa"
        p_box = "tfboxa"
        a_box = "cfboxa"
    else:
        ts_box = "tfboxa"
        p_box = "tfboxa"
        a_box = "tfboxa"

    # Needs dynamic logic
    layout = ""
    if category_path == None:
        layout += dedent(template.create_documentclass(style, parameter))
    else:
        layout += dedent(template.create_documentclass(style, parameter, category_path))
    
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

    layout += dedent(template.create_begin_section(ts_box))
    layout += dedent(template.create_paragraph(p_box))

    layout += dedent(template.print_references())

    layout += dedent(template.create_end_document())
    return layout

def download_tex(idx, tex, category, n_box): 
    zeros = "0" * (MILLION - len(str(idx)))
    name = f"{zeros}{idx}_{category}_{n_box}.tex"
    with open(name, "w") as f:
        f.write(tex)
        return name