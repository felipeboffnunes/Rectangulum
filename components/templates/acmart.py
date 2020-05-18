from components.tex_template import TexTemplate

class ACMART(TexTemplate):

    def __init__(self, master=TexTemplate):
        self.styles = ['acmsmall', 'acmlarge', 'acmtog', \
            'acmconf', 'sigchi', 'sigchi-a', 'sigplan']
        
        self.parameters = ['anonymous', 'review', \
            'authorversion', 'screen', 'authordraft']

        self.random = master.get_random(master)

    def create_documentclass(self) -> str:
        style = self.styles[self.random.randint(0,len(self.styles)-1)]
        parameter = self.parameters[self.random.randint(0,len(self.parameters)-1)]
        content = f"""
        \\documentclass[{style}]{{{parameter}}}
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