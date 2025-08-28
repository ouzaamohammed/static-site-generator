import os
import shutil
import sys

from copy_files import copy_files
from gen_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)

    print("generating all pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
