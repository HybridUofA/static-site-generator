from delimiter import split_nodes_delimiter
from textnode import TextType, TextNode
import unittest

class TestDelimiter(unittest.TestCase):
    def test_split_basic(self):
        node = TextNode("Hello `code` world!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(len(nodes), 3)
        for i, pnode in enumerate(nodes):
            if i % 2 == 0:
                self.assertEqual(pnode.text_type, TextType.TEXT)
                if i == 0:
                    self.assertEqual(pnode.text, "Hello ")
                elif i == 2:
                    self.assertEqual(pnode.text, " world!")
            else:
                self.assertEqual(pnode.text_type, TextType.CODE)
                self.assertEqual(pnode.text, "code")

    def test_split_multiple(self):
        node = TextNode("Hello `code` world `code2`!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " world ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "code2")
        self.assertEqual(nodes[3].text_type, TextType.CODE)
        self.assertEqual(nodes[4].text, "!")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

def test_split_invalid(self):
    node = TextNode("Hello `code world!", TextType.TEXT)
    with self.assertRaises(ValueError):
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)

def test_non_normal_node(self):
    node = TextNode("Hello `code`", TextType.BOLD)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(nodes), 1)
    self.assertEqual(nodes[0].text, "Hello `code`")
    self.assertEqual(nodes[0].text_type, TextType.BOLD)

def test_empty_input(self):
    nodes = split_nodes_delimiter([], "`", TextType.CODE)
    self.assertEqual(len(nodes), 0)

def test_bold_delimiter(self):
    node = TextNode("Hello **bold** world!", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    
    self.assertEqual(len(nodes), 3)
    self.assertEqual(nodes[0].text, "Hello ")
    self.assertEqual(nodes[0].text_type, TextType.TEXT)
    self.assertEqual(nodes[1].text, "bold")
    self.assertEqual(nodes[1].text_type, TextType.BOLD)
    self.assertEqual(nodes[2].text, " world!")
    self.assertEqual(nodes[2].text_type, TextType.TEXT)
    

    
def test_empty_delimiters(self):
    node = TextNode("Hello `` world!", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(nodes), 3)
    self.assertEqual(nodes[0].text, "Hello ")
    self.assertEqual(nodes[1].text, "")  # Empty text between delimiters
    self.assertEqual(nodes[2].text, " world!")

def test_multiple_nodes(self):
    node1 = TextNode("Hello `code`", TextType.TEXT)
    node2 = TextNode("World!", TextType.BOLD)
    node3 = TextNode("More `code` here", TextType.TEXT)
    nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
    
    self.assertEqual(len(nodes), 6)
    self.assertEqual(nodes[0].text, "Hello ")
    self.assertEqual(nodes[0].text_type, TextType.TEXT)
    self.assertEqual(nodes[1].text, "code")
    self.assertEqual(nodes[1].text_type, TextType.CODE)
    self.assertEqual(nodes[2].text, "World!")
    self.assertEqual(nodes[2].text_type, TextType.BOLD)
    self.assertEqual(nodes[3].text, "More ")
    self.assertEqual(nodes[3].text_type, TextType.TEXT)
    self.assertEqual(nodes[4].text, "code")
    self.assertEqual(nodes[4].text_type, TextType.CODE)
    self.assertEqual(nodes[5].text, " here")
    self.assertEqual(nodes[5].text_type, TextType.TEXT)
