import argparse
import tempfile
import os

from components.select_layout import select_layout
from components.create_tex import create_tex, download_tex
from components.create_pdf import create_pdf

def main(n):

    ids = list(range(1, int(args.n) + 1))
    layouts = list(map(select_layout, ids))
    texs = list(map(create_tex, layouts))

    ORIGINAL_PATH = os.getcwd()
    TMP_TEX = "\\tmp_tex"
    TMP_TEX_PATH = f"{ORIGINAL_PATH}{TMP_TEX}"
    os.chdir(TMP_TEX_PATH)  
    tex_names = list(map(download_tex ,ids, texs))
    
    tex_paths = list(map( \
        lambda tex_name : f"{TMP_TEX_PATH}\\{tex_name}", tex_names \
        ))

    TEMPLATE_PATH = "\\data\\template_src\\acm"
    os.chdir(f"{ORIGINAL_PATH}{TEMPLATE_PATH}")
    list(map(create_pdf, tex_paths))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", type = int, default = 10, \
        required = False, action = "store", \
        help = "Number of pdfs to create.")
    
    args = parser.parse_args()

    main(args.n)
    


        
    