# Python Standard Libraries
import argparse
import tempfile
import os
# Libraries
from pdf2image import convert_from_path
# Components
from components.select_layout import select_layout
from components.create_tex import create_all_tex, download_tex
from components.create_pdf import create_pdf
from components.detect_shapes import detect_shapes

def main(n, b):

    ids = list(range(1, int(args.n) + 1))
    layouts = list(map(select_layout, ids))
    texs = list(map(create_all_tex, layouts))

    ORIGINAL_PATH = os.getcwd()
    TMP_TEX_PATH = f"{ORIGINAL_PATH}\\data\\tmp_tex"
    TMP_PDF_PATH = f"{ORIGINAL_PATH}\\data\\tmp_pdf"
    TEMPLATE_PATH = f"{ORIGINAL_PATH}\\data\\template_src\\acm"
    TEX_PATH = f"{ORIGINAL_PATH}\\results\\tex"
    PDF_PATH = f"{ORIGINAL_PATH}\\results\\pdf"

    # Batch iteration
    iterations = n//b
    for iteration in range(iterations):
        batch_begin = iteration * b
        batch_end = batch_begin + b
        batch_ids = ids[batch_begin:batch_end]
        batch_texs = texs[batch_begin:batch_end]
        # Each tex has several categories
        # Title, Subtitle, Tables...
        # To receive the separate coordinates
        # we need to create each pdf with only
        # category with black boxes
        for idx, tex_categories in zip(batch_ids, batch_texs):
            # tex_categories = [tex, category]

            # NEEDS TO CHANGE TMP DIRS TO REAL TMP DIRS!
            # with tempfile.TemporaryDirectory() as path:

            # Go to /data/tmp_tex and create texs
            os.chdir(TMP_TEX_PATH)
            tex_names = list(map( \
                lambda tex_category : download_tex(idx, tex_category[0], tex_category[1]), tex_categories \
                ))
            
            tex_paths = list(map( \
                lambda tex_name : f"{TMP_TEX_PATH}\\{tex_name}", tex_names \
                ))
        
            # Go to /data/template_src/{template}/ and create PDFs
            os.chdir(TEMPLATE_PATH)
            list(map(create_pdf, tex_paths))

            
            # Move the original tex to /results/tex folder
            try:
                os.rename(tex_paths[0], f"{TEX_PATH}\\{tex_names[0]}".replace("_original", ""))
            except:
                pass
            for tex_path in tex_paths[1:]:
                os.remove(tex_path)

            # Split PDFs into individual pages
            with os.scandir(TMP_PDF_PATH) as pdfs:
                for pdf in pdfs:
                    if "_original" in pdf.name:
                        # Move the original pdf to /results/pdf folder
                        try:
                            os.rename(pdf.path, f"{PDF_PATH}\\{pdf.name}".replace("_original", ""))
                        except:
                            pass
                    else:
                        with tempfile.TemporaryDirectory() as path:
                            pages = convert_from_path(pdf.path, output_folder=path)
                            list(map(detect_shapes, pages))


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
    


        
    