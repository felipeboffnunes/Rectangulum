from components.tex_template import TexTemplate

class ACMART(TexTemplate):

    def __init__(self, master=TexTemplate):
        self.styles = ["manuscript", "acmsmall", "acmlarge", "acmtog", \
            "acmconf", "sigchi", "sigplan"]
        
        self.parameters = ["anonymous", "review", \
            "authorversion", "screen", "authordraft"]

        self.CATEGORIES = master.get_categories(master)
        # Here you can edit the categories
        #
        # Add categories specific from this template
        # self.CATEGORIES.append(["ccs", 1])
        # self.CATEGORIES.append(["ccs-title", 1])
        #
        # Delete default categories this template does not support
        # self.CATEGORIES.remove(["images", "n"])
        # self.CATEGORIES.remove(["images-dec", "n"])
        

    def create_documentclass(self, style, parameter, category=None) -> str:
        if category == None:
            content = f"""
            \\documentclass[{style}, {parameter}]{{acmart}}
            """
        else:
            content = f"""
            \\documentclass[{style}, {parameter}]{{acmart_{category}}}
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
