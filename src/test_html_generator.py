import unittest
from html_generator import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        node = markdown_to_html_node("This is a paragraph")
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_header(self):
        node = markdown_to_html_node("# Header")
        self.assertEqual(node.to_html(), "<div><h1>Header</h1></div>")
                
    def test_quote(self):
        node = markdown_to_html_node("> This is a quote")
        
        self.assertEqual(node.to_html(), "<div><blockquote>This is a quote</blockquote></div>")
                
    def test_code(self):
        markdown = "```\nprint('hello')\n```"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><pre><code>print('hello')</code></pre></div>")
        
    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>")
        
    def test_ordered_list(self):
        markdown = "1. First\n2. Second"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><ol><li>First</li><li>Second</li></ol></div>")
