from components.tex_template import TexTemplate

SRC_PATH = "./data/template_src/acm/"
ACM_FILE = "acmart_"

# Write here all categories that use a CLS file.
AS_CLS = ["title", "subtitle", "abstract", "author-name", "author-affiliation", \
    "aux-info", "ccs", "doi", "keywords", "acm-ref", "acm-ref-title", "blank", "all"]

class ACMART(TexTemplate):

    def __init__(self, master=TexTemplate):
        # Template tools for generating content
        self.randint = self.get_random()
        #self.gen = self.get_generator()

        # The latex articles generally have different styles
        # and parameters, most of the times they are explicitly
        # cited in the tex default file, but can also be found
        # on the cls file.
        #
        # Only use styles that are for A4 templates, comment the
        # templates not used on the side.
        self.styles = ["manuscript", "acmsmall", "acmlarge", "acmtog", \
            "acmconf", "sigchi", "sigplan"] #sigchi-a not suited
        
        self.parameters = ["anonymous", "review", \
            "authorversion", "screen", "authordraft"]

        self.CATEGORIES = self.get_categories()
        # Here you can edit the categories
        #
        # Add categories specific from this template
        # self.CATEGORIES.append(["ccs", 1])
        # self.CATEGORIES.append(["ccs-title", 1])
        #
        # Delete default categories this template does not support
        # self.CATEGORIES.remove(["images", "n"])
        # self.CATEGORIES.remove(["images-desc", "n"])
        self.CATEGORIES.append(["acm-ref-title", 1])
        self.CATEGORIES.append(["acm-ref", 1])
        self.CATEGORIES.append(["author-affiliation", "n"])
        self.CATEGORIES.append(["keywords", 1])
        self.CATEGORIES.append(["ccs", 1])
        self.CATEGORIES.append(["doi", 1])
        
        self.CLS = {}
        list(map(lambda c : self.CLS.update({c : f"{SRC_PATH}{ACM_FILE}{c}"}), AS_CLS))

    def __repr__(self):
        return "ACMART"

    def create_documentclass(self, style, parameter, category=None) -> str:
        if category == None:
            content = f"""
            \\documentclass[{style}, natbib=false, {parameter}]{{acmart}}
            """ 
        else:
            content = f"""
            \\documentclass[{style}, natbib=false, {parameter}]{{acmart_{category}}}
            """
        return content

    def create_usepackage(self) -> str:
        content = f"""
        \\usepackage{{tikz}}
        \\usetikzlibrary{{tikzmark}}
        \\usetikzlibrary{{calc}}
        \\usepackage[style=ieee,sorting=nty]{{biblatex}}
        \\usepackage{{varwidth}}
        """
        return content

    def setup_boxes(self) -> str:
        content = f"""
        \\newcommand{{\\cfboxa}}[1]{{%
            {{\\setlength\\fboxsep{{0pt}}\\fbox{{%
                \\begin{{varwidth}}{{\\dimexpr\\columnwidth-2}}
                    \\begingroup
                    \\leavevmode\\color{{black}}#1
                    \\endgroup
                \\end{{varwidth}}
                }} 
            }} 
        }}
        \\newcommand{{\\tfboxa}}[1]{{%
            {{\\setlength\\fboxsep{{0pt}}\\fbox{{
                \\begin{{varwidth}}{{\\dimexpr\\columnwidth-2}}
                    \\begingroup
                    \\leavevmode\\color{{black}}#1
                    \\endgroup
                \\end{{varwidth}}
                }}
            }}%
        }}
        """
        return content

    def setup_references(self) -> str:
        content = f"""
        \\addbibresource{{bib.bib}}
        \\newbibmacro*{{infoboxnote}}{{\\printfield[infoboxnote]{{\\notefield}}}}
        \\renewbibmacro*{{finentry}}{{\\finentry\\tikzmark{{\\thefield{{entrykey}}end}}}}
        \\newcommand{{\\highlight}}[1]{{%
        \\begin{{tikzpicture}}[remember picture, overlay]
        \\coordinate (begin) at ($ (pic cs:#1beg) + (-.5ex,2ex) $);
        \\coordinate (end) at ($ (pic cs:#1end) + (0,-.8ex) $);
        \\coordinate (penult) at ($ (begin |-  end) + (0,-.5ex) $);
        \\coordinate (right) at ($ (begin) + (\\linewidth+1ex,0) $);
        \\draw[draw=black] (begin) -- (right |- begin) -- (right |- end) -- ( begin |- end) -- cycle;
        \\end{{tikzpicture}}}}

        \\AtEveryBibitem{{%
            {{\\highlight{{\\thefield{{entrykey}}}}\\tikzmark{{\\thefield{{entrykey}}beg}}\\usebibmacro{{infoboxnote}}\\bibitemstyle}}%
            {{}}}}
        \\setlength\\bibitemsep{{0.2\\baselineskip}}
        """
        return content

    def create_acm_setup(self) -> str:
        content = f"""
        \\setcopyright{{none}}
        \\copyrightyear{{2018}}
        \\acmYear{{2018}}
        \\acmDOI{{10.1145/1122445.1122456}}
        \\acmConference[Woodstock '18]{{Woodstock '18: ACM Symposium on Neural
        Gaze Detection}}{{June 03--05, 2018}}{{Woodstock, NY}}
        \\acmBooktitle{{Woodstock '18: ACM Symposium on Neural Gaze Detection,
        June 03--05, 2018, Woodstock, NY}}
        \\acmPrice{{15.00}}
        \\acmISBN{{978-1-4503-XXXX-X/18/06}}
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

    def create_author(self) -> str:
        content = f"""
        \\author{{Ben Trovato}}
        \\authornote{{Both authors contributed equally to this research.}}
        \\email{{trovato@corporation.com}}
        \\orcid{{1234-5678-9012}}
        \\author{{G.K.M. Tobin}}
        \\authornotemark[1]
        \\email{{webmaster@marysville-ohio.com}}
        \\affiliation{{%
        \\institution{{Institute for Clarity in Documentation}}
        \\streetaddress{{P.O. Box 1212}}
        \\city{{Dublin}}
        \\state{{Ohio}}
        \\postcode{{43017-6221}}
        }}
        """
        return content

    def create_abstract(self) -> str:
        content = f"""
        \\begin{{abstract}}
        A clear and well-documented \LaTeX\ document is presented as an
        article formatted for publication by ACM in a conference proceedings
        or journal publication. Based on the ``acmart'' document class, this
        article presents and explains many of the common variations, as well
        as many of the formatting elements an author may use in the
        preparation of the documentation of their work.
        \\end{{abstract}}"""
        return content

    def create_ccs(self) -> str:
        content = f"""
        \\begin{{CCSXML}}
        <ccs2012>
        <concept>
        <concept_id>10010520.10010553.10010562</concept_id>
        <concept_desc>Computer systems organization~Embedded systems</concept_desc>
        <concept_significance>500</concept_significance>
        </concept>
        <concept>
        <concept_id>10010520.10010575.10010755</concept_id>
        <concept_desc>Computer systems organization~Redundancy</concept_desc>
        <concept_significance>300</concept_significance>
        </concept>
        <concept>
        <concept_id>10010520.10010553.10010554</concept_id>
        <concept_desc>Computer systems organization~Robotics</concept_desc>
        <concept_significance>100</concept_significance>
        </concept>
        <concept>
        <concept_id>10003033.10003083.10003095</concept_id>
        <concept_desc>Networks~Network reliability</concept_desc>
        <concept_significance>100</concept_significance>
        </concept>
        </ccs2012>
        \\end{{CCSXML}}
        \\ccsdesc[500]{{Computer systems organization~Embedded systems}}
        \\ccsdesc[300]{{Computer systems organization~Redundancy}}
        \\ccsdesc{{Computer systems organization~Robotics}}
        \\ccsdesc[100]{{Networks~Network reliability}}

        """
        return content

    def create_keywords(self) -> str:
        content = f"""
        \\keywords{{datasets, neural networks, gaze detection, text tagging}}
        """
        return content

    def create_tfbox(self) -> str:
        content = f"""
        \\cfboxa{{
        """
        return content
    
    def end_tfbox(self) -> str:
        content = f"""
        }}
        """
        return content
    
    def create_begin_section(self, title, box) -> str:
        content = f"""
        \\{box}{{
        \\section{{{title}}}
        }}
        """
        return content
    
    def create_begin_subsection(self, box) -> str:
        content = f"""
        \\{box}{{
        \\subsection{{sub Introduction}}
        }}
        """
        return content

    def create_paragraph(self, text, box) -> str:
        content = f"""
        \\{box}{{
        {text}
        }}
        """
        return content
    
    def create_table(self, table, box) -> str:
        rows = []
        for row in table:
            row_string = f""""""
            for column in row:
                row_string += f"""{column}& """
            row_string = row_string[:-2]
            rows.append(row_string)
            
        content = f"""
        \\{box}{{
            \\begin{{table}}[H]   
            \\caption{{Frequency of Special Characters}}  
            \\label{{tab:freq}}
            \\{box}{{
                \\begin{{tabular}}{{ccl}}
                    \\toprule
                    {rows[0]}\\\\
                    \\midrule
        """
        for row in rows:
            content += f"""{row}\\\\\n"""
        content = content[:-2]
        content += f"""
                    \\bottomrule
                \\end{{tabular}}
            }}
            \\end{{table}}
        }}"""
        return content

    def print_references(self) -> str:
        content = f"""
        \\printbibliography
        """
        return content

    def create_end_document(self) -> str:
        content = f"""
        \\end{{document}}
        \\endinput
        """
        return content
