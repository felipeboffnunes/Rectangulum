from textwrap import dedent

def create_tex(template):
    layout = f""""""

    layout += dedent(template.create_documentclass())
    layout += dedent(template.create_begin_document())
    layout += dedent(template.create_title())
    layout += dedent(template.create_maketitle())
    layout += dedent(template.create_end_document())

    return layout

def download_tex(idx, tex):
    with open(f"{idx}.tex", "w") as f:
        f.write(tex)