from textwrap import dedent

MILLION = 7


def create_tex(template):

    layout = ""
    layout += dedent(template.create_documentclass("title"))
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