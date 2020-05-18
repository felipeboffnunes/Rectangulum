import subprocess
import os

def create_pdf(tex_path):
    subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode"])