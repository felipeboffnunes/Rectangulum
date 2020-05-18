from components.tex_template import TexTemplate

class ACMART(TexTemplate):

    def __init__(self, master=TexTemplate):
        self.styles = ['acmsmall', 'acmlarge', 'acmtog', \
            'acmconf', 'sigchi', 'sigchi-a', 'sigplan']
        
        self.parameters = ['anonymous', 'review', \
            'authorversion', 'screen', 'authordraft']

        self.random = master.get_random(master)
        self.CATEGORIES = master.get_categories(master)
        # Here you can edit the categories
        #
        # Add categories specific from this template
        # self.CATEGORIES.append("ccs")
        #
        # Delete default categories this template does not support
        # self.CATEGORIES.remove("subtitle")
        

    def create_documentclass(self, category) -> str:
        style = self.styles[self.random.randint(0,len(self.styles)-1)]
        parameter = self.parameters[self.random.randint(0,len(self.parameters)-1)]
        content = f"""
        \\documentclass[{style, parameter}]{{acmart_{category}}}
        """
        return content

    def create_begin_document(self) -> str:
        content = f"""
        \\begin{{document}}
        """
        return content

    def create_maketitle(self) -> str:
        content = f"""
        \\maketitle
        """
        return content

    def create_title(self) -> str:
        content = f"""
        \\title{{Example Title}}
        """
        return content

    def create_end_document(self) -> str:
        content = f"""
        \\end{{document}}
        \\endinput
        """
        return content
