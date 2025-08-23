import os
import shutil

from textnode import TextNode, TextType
from htmlnode import HTMLNode

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)

def copy_files(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
         os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)

main()
