import tempfile
import subprocess
import os

TMP_PDF_PATH = "../../tmp_pdf"

def create_pdf(tex_path):
    with tempfile.TemporaryDirectory() as tmp_dir:
        subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode",\
            f"-aux-directory={tmp_dir}", f"-output-directory={TMP_PDF_PATH}"])