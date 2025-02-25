from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    parts = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Unclosed {delimiter} in node!")
            for i, part in enumerate(parts):
                if len(part) > 0:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
    return new_nodes
