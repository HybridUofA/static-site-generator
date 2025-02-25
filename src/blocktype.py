from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def is_quote_block(block):
    lines = block.split('\n')
    return all(line.startswith('> ') for line in lines)

def is_ordered_list(block):
    lines = block.split('\n')
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            return False
    return True

def is_unordered_list(block):
    lines = block.split('\n')
    return all(line.startswith('- ') or line.startswith('* ') for line in lines)

def block_to_block_type(block):
    if re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.UNORDERED
    if is_ordered_list(block):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH
