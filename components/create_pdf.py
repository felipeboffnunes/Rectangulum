import tempfile
import subprocess
import os

def create_pdf(tex_path, path, orpath):
    with tempfile.TemporaryDirectory() as tmp_dir:
        subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode",\
            f"-aux-directory={path}", f"-output-directory={tmp_dir}"])
        os.chdir(path)
        subprocess.run(["bibtex", os.path.basename(tex_path)[:-4]])
        os.chdir(orpath)
        #subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode",\
        #    "-quiet", f"-aux-directory={tmp_dir}", f"-output-directory={path}"])
        subprocess.run(["pdflatex", tex_path, "-interaction=nonstopmode", \
            f"-aux-directory={tmp_dir}", f"-output-directory={path}"])

     
     