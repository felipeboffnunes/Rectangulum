# Python Standard Libraries
import argparse
import tempfile
import os
import re
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
            # tex_categories = [tex, category, n_box]

            with tempfile.TemporaryDirectory() as path:
                os.chdir(path)
                tex_names = list(map( \
                    lambda tex_category : download_tex(idx, tex_category[0], tex_category[1], tex_category[2]), tex_categories \
                    ))

                tex_paths = list(map( \
                    lambda tex_name : f"{path}\\{tex_name}", tex_names \
                    ))
            
                # Go to /data/template_src/{template}/ and create PDFs
                os.chdir(TEMPLATE_PATH)
                list(map(lambda tex_path: create_pdf(tex_path, path), tex_paths))
                os.chdir(path)
                
                # Move the original tex to /results/tex folder
                try:
                    os.rename(tex_paths[0], f"{path}\\{tex_names[0]}".replace("_original", ""))
                except:
                    pass

                json = {}
                # Split PDFs into individual pages
                with os.scandir(path) as files:
                    for f in files:
                        if "_original.pdf" in f.name:
                            # Move the original pdf to /results/pdf folder
                            try:
                                os.rename(f.path, f"{PDF_PATH}\\{f.name}".replace("_original", ""))
                            except:
                                pass
                        elif ".pdf" in f.name:
                            pages = convert_from_path(f.path, output_folder=path)
                            category = re.search("_(.*?)_\d*\.pdf$", f.name).group(1)
                            n_box = re.search("_(\d*?).pdf$", f.name).group(1)     
                            idx = re.search("^\d*", f.name).group(0)

                            # Little hack
                            # I don't know why, but I can't use the map(detect_shapes)
                            # inside the temporary directory
                            os.chdir(ORIGINAL_PATH)
                            coordinates = list(map(lambda page : detect_shapes(page, visual=True), pages))

                            # Delete the smallest boxes
                            bigger = []
                            for i, coordinate in enumerate(coordinates[0]):
                                x, y, w, h = coordinate
                                area = w * h
                                bigger.append([area, i])
                            bigger.sort(reverse=True)
                            bigger = bigger[:int(n_box)]
                            filtered_coordinates = []
                            for box in bigger:
                                filtered_coordinates.append(coordinates[0][box[1]])

                            json.update({idx : {category : filtered_coordinates}})
                            for i in json:
                                print(i, json[i])
                            input()


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
    


        
    