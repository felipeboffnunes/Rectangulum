from components.tex_template import TexTemplate

class ACMART(TexTemplate):

    def __init__(self, master=TexTemplate):
        self.styles = ['acmsmall', 'acmlarge', 'acmtog', \
            'acmconf', 'sigchi', 'sigchi-a', 'sigplan']
        
        self.parameters = ['anonymous', 'review', \
            'authorversion', 'screen', 'authordraft']

        self.random = master.get_random(master)



    def create_documentclass(self) -> str:
        content = f"""
        \\documentclass[
            {self.styles[self.random.randint(0,len(self.styles))]}
        ]{{
            {self.parameters[self.random.randint(0,len(self.parameters))]}
        }}
        """
        return content

    def create_title(self) -> str:
        content = f"""
        Example Title
        """
        return content

