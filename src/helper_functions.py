from text_to_textnode import text_to_textnodes
from textnode import TextType, TextNode
from htmlnode import text_node_to_html_node
import os, shutil

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]

def count_header_level(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break

    return level

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            print(f"Copying file: {item_path}")
            shutil.copy(item_path, dest_dir)
        else:
            dir_path = os.path.join(source_dir, item)
            copy_path = os.path.join(dest_dir, item)
            print(f"Creating directory: {copy_path}")
            os.mkdir(copy_path)
            copy_static(dir_path, copy_path)
