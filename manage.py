import argparse
import tempfile
import os

from components.select_layout import select_layout
from components.create_tex import create_tex, download_tex
from components.create_pdf import create_pdf

def main(n, b):

    ids = list(range(1, int(args.n) + 1))
    layouts = list(map(select_layout, ids))
    texs = list(map(create_tex, layouts))

    ORIGINAL_PATH = os.getcwd()
    TMP_TEX = "\\tmp_tex"
    TMP_TEX_PATH = f"{ORIGINAL_PATH}{TMP_TEX}"
    TEMPLATE_PATH = "\\data\\template_src\\acm"

    iterations = n//b
    os.chdir(TMP_TEX_PATH)
    for iteration in range(iterations):     
        tex_names = list(map( \
            download_tex, \
            ids[iteration*b : iteration*b + b], \
            texs[iteration*b : iteration*b + b] \
            ))
        
        tex_paths = list(map( \
            lambda tex_name : f"{TMP_TEX_PATH}\\{tex_name}", tex_names \
            ))
        
        os.chdir(f"{ORIGINAL_PATH}{TEMPLATE_PATH}")
        list(map(create_pdf, tex_paths))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", type = int, default = 10, \
        required = False, action = "store", \
        help = "Number of pdfs to create.")
    parser.add_argument("--b", type = int, default = 5, \
        required = False, action = "store", \
        help = "Batch size (less means slower but also less overhead.")
    
    args = parser.parse_args()

    main(args.n, args.b)
    


        
    