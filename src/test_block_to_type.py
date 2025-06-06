from blocktype import block_to_block_type, BlockType
from block_builder import markdown_to_blocks
import unittest

class TestBlockToBlock(unittest.TestCase):
    def test_varying_headers(self):
        headers = {
            "# Header 1": BlockType.HEADING,
            "## Header 2": BlockType.HEADING,
            "### Header 3": BlockType.HEADING,
            "#### Header 4": BlockType.HEADING,
            "##### Header 5": BlockType.HEADING,
            "###### Header 6": BlockType.HEADING
        }
        for header_text, expected_type in headers.items():
            blocks = markdown_to_blocks(header_text)
            self.assertEqual(block_to_block_type(blocks[0]), expected_type)
    def test_multi_line_code(self):
        text = "```This is a \nCode block with\nMultiple lines of code```"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.CODE)
    def test_multi_line_quote(self):
        text = "> This is a \n> Multiline\n> Quote that continues\n> onto multiple lines"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.QUOTE)
    def test_unordered_list_dashes(self):
        text = "- This is an item in an unordered list\n- This is another"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.UNORDERED)
    def test_unordered_list_asterisks(self):
        text = "* This is an item in an unordered asterisk list\n* This is another"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.UNORDERED)
    def test_ordered_list(self):
        text = "1. This is an ordered list item.\n2. This is the second item.\n3. This is the third item"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.ORDERED)

    def test_paragraph(self):
        text = "This is a paragraph, no special markdown."
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)

    def test_invalid_ordered_list(self):
        text = "2. This is out of order.\n1. This is too"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)

    def test_empty_code_block(self):
        text = "``````"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.CODE)

    def test_too_many_hashes(self):
        text = "####### This is an invalid header"
        blocks = markdown_to_blocks(text)
        self.assertEqual(block_to_block_type(blocks[0]), BlockType.PARAGRAPH)
