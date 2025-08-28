import os
import shutil
import sys

from copy_files import copy_files
from gen_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("copying static files to docs directory...")
    copy_files(dir_path_static, dir_path_docs)

    basepath = sys.argv[1] or "/"

    print("generating all pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


main()
