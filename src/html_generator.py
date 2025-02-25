from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from blocktype import BlockType, block_to_block_type
from block_builder import markdown_to_blocks
from helper_functions import text_to_children, count_header_level

def markdown_to_html_node(markdown):
    parent = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type is BlockType.PARAGRAPH:
            node = ParentNode("p", text_to_children(block))
            parent.children.append(node)

        elif block_type is BlockType.HEADING:
            level = count_header_level(block)
            content = block.lstrip('#').lstrip()
            node = ParentNode(f"h{count_header_level(block)}", text_to_children(content))
            parent.children.append(node)

        elif block_type is BlockType.QUOTE:
            lines = block.split('\n')
            clean_lines = [line.lstrip('> ') for line in lines]
            content = '\n'.join(clean_lines)
            node = ParentNode("blockquote", text_to_children(content))
            parent.children.append(node)

        elif block_type is BlockType.CODE:
            lines = block.split('\n')
            code_content = '\n'.join(lines[1:-1])
            code_node = LeafNode("code", code_content)
            pre_node = ParentNode("pre", [code_node])
            parent.children.append(pre_node)

        elif block_type is BlockType.UNORDERED:
            lines = block.split('\n')
            list_node = ParentNode("ul", [])
            for line in lines:
                clean_line = line.removeprefix('- ').removeprefix('* ')
                line_node = ParentNode("li", text_to_children(clean_line))
                list_node.children.append(line_node)
            parent.children.append(list_node)

        elif block_type is BlockType.ORDERED:
            lines = block.split('\n')
            list_node = ParentNode("ol", [])
            for line in lines:
                clean_line = line.lstrip('0123456789').lstrip('.').lstrip()
                line_node = ParentNode("li", text_to_children(clean_line))
                list_node.children.append(line_node)
            parent.children.append(list_node)
    return parent
