from components.templates.acmart import ACMART

def select_layout(idx):
    template = ACMART()
    layout = {}
    for category, n in template.CATEGORIES:
        if n == "n":
            n = template.randint(1, 5)
        layout[category] = n

    return (template, layout)

   
    
    
