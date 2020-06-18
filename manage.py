# Python Standard Libraries
from multiprocessing import Pool, cpu_count
from functools import partial
import argparse
import tempfile
import json
import os
import re
# Libraries
from pdf2image import convert_from_path
# Components
from components.select_layout import select_layout
from components.create_tex import create_all_tex, download_tex
from components.create_pdf import create_pdf
from components.detect_shapes import detect_shapes

MILLION = 7

def main(n, b):

    ids = list(range(1, int(args.n) + 1))
    templates, layouts = zip(*map(select_layout, ids))
    texs = list(map(create_all_tex, templates, layouts))

    ORIGINAL_PATH = os.getcwd()
    TEMPLATE_PATH = f"{ORIGINAL_PATH}\\data\\template_src\\acm"
    TEX_PATH = f"{ORIGINAL_PATH}\\results\\tex"
    PDF_PATH = f"{ORIGINAL_PATH}\\results\\pdf"
    JSON_PATH = f"{ORIGINAL_PATH}\\results\\json"

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
        # one category with black boxes
        # tex_categories = [tex, category, category_path, n]
        for idx, tex_categories in zip(batch_ids, batch_texs):
            # Format idx (1 becomes 0000001)
            zeros = "0" * (MILLION - len(str(idx)))
            idx = f"{zeros}{idx}"
            
            with tempfile.TemporaryDirectory() as path:
                # Write category tex files and get paths
                os.chdir(path)
                tex_names = list(map( \
                    lambda tex_category : download_tex(idx, tex_category[0], tex_category[1], \
                        tex_category[3]), tex_categories \
                    ))
                
                tex_paths = list(map( \
                    lambda tex_name : f"{path}\\{tex_name}", tex_names \
                ))
                
                # Go to /data/template_src/{template}/ and create PDFs
                os.chdir(TEMPLATE_PATH)
                cpu = cpu_count() - 1
                create = partial(create_pdf, path=path, orpath=TEMPLATE_PATH)
                with Pool(cpu) as p:
                    p.map(create, tex_paths)
                
                #for tpath in tex_paths:
                #    create_pdf(tpath, path=path, orpath=TEMPLATE_PATH)
                
                # Move the original tex to /results/tex folder
                try:
                    os.rename(tex_paths[0], f"{TEX_PATH}\\{tex_names[0]}".replace("_blank_0", ""))
                except:
                    os.remove(tex_paths[0])

                json_coordinates = {}
                # Split PDFs into individual pages
                with os.scandir(path) as files:
                    for f in files:                    
                        if "_blank_0.pdf" in f.name:
                            # Move the original pdf to /results/pdf folder
                            try:
                                os.rename(f.path, f"{PDF_PATH}\\{f.name}".replace("_blank_0", ""))
                            except:
                                os.remove(f.path)
                        elif "_all_n.pdf" in f.name:
                            # Move the all boxed pdf to /results/pdf folder
                                try:
                                    os.rename(f.path, f"{PDF_PATH}\\{f.name}".replace("_all_n", "_box"))
                                except:
                                    os.remove(f.path)       
                        elif ".pdf" in f.name:
                            # Tranforms PDFs in separate pages as PIL Images
                            pages = convert_from_path(f.path, output_folder=path)

                            n_box = re.search("_(\d*n*?)\.pdf$", f.name).group(1) 
                            category = re.search("_(.*?)_\d*n*\.pdf$", f.name).group(1)

                            # Use detect_shapes(page, visual=True)
                            # to see the bounding boxes found
                            coordinates = list(map(lambda page : detect_shapes(page, visual=False), pages))

                            # Delete the smallest boxes
                            bigger = []
                            for z, page in enumerate(coordinates):
                                for i, coordinate in enumerate(page):
                                    x, y, w, h = coordinate
                                    if w < 4 or h < 4:
                                        continue
                                    area = w * h
                                    bigger.append([area, z, i])
                            bigger.sort(reverse=True)
                            if n_box != "n":
                                bigger = bigger[:int(n_box)]
                            filtered_coordinates = []
                            for box in bigger:
                                filtered_coordinates.append(coordinates[box[1]][box[2]])

                            # Get coordinates
                            if idx in json_coordinates:
                                json_coordinates[idx][category] = filtered_coordinates 
                            else:
                                json_coordinates[idx] = {category : filtered_coordinates}
                            
                            # Uncomment to see all pdfs created
                            #os.rename(f.path, f"{PDF_PATH}\\{f.name}")

                # Write coordinates to json
                os.chdir(JSON_PATH)
                with open(f"{idx}.json", "w") as j:
                    j.write(json.dumps(json_coordinates))
                           
                            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", type = int, default = 10, \
        required = False, action = "store", \
        help = "Number of pdfs to create.")
    parser.add_argument("--b", type = int, default = 1, \
        required = False, action = "store", \
        help = "Batch size (less means slower but also less overhead).")
    
    args = parser.parse_args()

    main(args.n, args.b)
    


        
    