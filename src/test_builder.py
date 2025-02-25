from block_builder import markdown_to_blocks
import unittest

class TestBlockBuilder(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# This is a heading")
        self.assertEqual(blocks[1], "This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        self.assertEqual(blocks[2], "* This is the first list item in a list block\n* This is another list item")

    def test_extra_blank_lines(self):
        markdown = "# Heading\n\n\nParagraph\n\n\nList"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "Paragraph")
        self.assertEqual(blocks[2], "List")

    def test_whitespace_blocks(self):
        markdown = "   # Heading   \n\n   \n\n   Paragraph   "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "Paragraph")

    def test_empty_input(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 0)
