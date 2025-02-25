from markdown_parser import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text == "":
            continue
        if len(links) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for link in links:
                full_link = f"[{link[0]}]({link[1]})"
                parts = remaining_text.split(full_link, 1)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                remaining_text = parts[1]
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text == "":
            continue
        if len(images) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for image in images:
                full_image = f"![{image[0]}]({image[1]})"
                parts = remaining_text.split(full_image, 1)
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                remaining_text = parts[1]
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
