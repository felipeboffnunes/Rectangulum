from textwrap import dedent

MILLION = 7


def create_all_tex(template):
    all_tex = []
    for category in template.CATEGORIES:
        all_tex.append(create_tex(template, category))
    return all_tex

def create_tex(template, category):
    # Needs dinamic logic
    layout = ""
    layout += dedent(template.create_documentclass(category))
    layout += dedent(template.create_begin_document())
    layout += dedent(template.create_title())
    layout += dedent(template.create_maketitle())
    layout += dedent(template.create_end_document())
    return layout

def download_tex(idx, tex):
    zeros = "0" * (MILLION - len(str(idx)))
    name = f"{zeros}{idx}.tex"
    with open(name, "w") as f:
        f.write(tex)
        return name