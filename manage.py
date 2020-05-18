import argparse
from components.select_layout import select_layout
from components.create_tex import create_tex, download_tex

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n",  type = int, default = 10, \
        required = False, action = "store", \
        help = "Number of pdfs to create.")
    
    args = parser.parse_args()

    ids = list(range(int(args.n)))
    layouts = list(map(select_layout, ids))
    texs = list(map(create_tex, layouts))
    list(map(download_tex, ids, texs))
    