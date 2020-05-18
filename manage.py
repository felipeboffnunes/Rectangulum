import argparse
from components.select_layout import select_layout

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("n", help="Number of pdfs to create")

    args = parser.parse_args()

    ids = list(range(int(args.n)))
    layouts = list(map(select_layout, ids))