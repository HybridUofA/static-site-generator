from text_to_textnode import text_to_textnodes
from textnode import TextType, TextNode
from htmlnode import text_node_to_html_node

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
