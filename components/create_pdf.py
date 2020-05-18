import subprocess
import os

def create_pdf(tex):
    os.chdir("../data/template_src/acm")
    subprocess.run(["pdflatex", tex, "-interaction=nonstopmode"])