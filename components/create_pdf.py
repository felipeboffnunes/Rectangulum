import tempfile
import subprocess
import os

WORK_DIR = "../../work_dir"

def create_pdf(tex_path):
    with tempfile.TemporaryDirectory() as tmp_dir:
        subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode",\
            f"-aux-directory={tmp_dir}", f"-output-directory={WORK_DIR}"])