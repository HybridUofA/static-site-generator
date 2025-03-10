
import unittest



from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):
        def test_normal_node(self):
                node = HTMLNode("h1", "Test Header", None, {"href": "https://www.google.com", "target": "_blank",})
                html_string = ' href="https://www.google.com" target="_blank"'
                self.assertEqual(node.props_to_html(), html_string)

        def test_no_props(self):
                node = HTMLNode("h1", "Test Header")
                html_string = ""
                self.assertEqual(node.props_to_html(), html_string)

        def test_one_prop(self):
                node = HTMLNode("h1", "Test Header", None, {"href": "https://www.google.com",})
                html_string = ' href="https://www.google.com"'
                self.assertEqual(node.props_to_html(), html_string)

        def test_leaf_node_initialization(self):
                node = LeafNode("p", "Hello, world!", {"class": "text"})
                self.assertEqual(node.tag, "p")
                self.assertEqual(node.value, "Hello, world!")
                self.assertEqual(node.props, {"class": "text"})
                self.assertEqual(node.children, None)

        def test_to_html_with_tag(self):
                node = LeafNode("a", "Click here", {"href": "https://boot.dev",})
                self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click here</a>')

        def test_to_html_without_props(self):
                node = LeafNode("p", "Just a paragraph.")
                self.assertEqual(node.to_html(), "<p>Just a paragraph.</p>")

        def test_to_html_without_tag(self):
                node = LeafNode(None, "Plain text with no tag")
                self.assertEqual(node.to_html(), "Plain text with no tag")

        def test_to_html_no_value(self):
                node = LeafNode("p", None)
                try:
                        node.to_html()
                        assert False
                except ValueError as e:
                        self.assertEqual(str(e), "LeafNode must have a value.")

        def test_parent_node_with_children(self):
                node = ParentNode(
                        "div",
                        [
                                LeafNode("p", "Paragraph 1"),
                                LeafNode("p", "Paragraph 2"),
                        ]
                )
                self.assertEqual(node.to_html(), "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>")

        def test_nested_nodes(self):
                node = ParentNode(
                        "div",
                        [
                                ParentNode(
                                        "section",
                                        [LeafNode("p", "Nested paragraph")]
                                ),
                                LeafNode("span", "Text in a span"),
                        ]
                )
                self.assertEqual(node.to_html(), "<div><section><p>Nested paragraph</p></section><span>Text in a span</span></div>")

        def test_empty_children(self):
                node = ParentNode("div", [])
                self.assertEqual(node.to_html(), "<div></div>")

        def test_error_handling_parents(self):
                try:
                        node = ParentNode(None, [LeafNode("p", "Should fail")])
                        node.to_html()
                        assert False
                except ValueError as e:
                        self.assertEqual(str(e), "ParentNode must have a tag.")

        def test_normal_text_to_html(self):
                normal_node = TextNode("plain text", TextType.TEXT)
                normal_html = text_node_to_html_node(normal_node)
                self.assertEqual(normal_html.to_html(), "plain text")

        def test_bold_text_to_html(self):
                bold_node = TextNode("bold text", TextType.BOLD)
                bold_html = text_node_to_html_node(bold_node)
                self.assertEqual(bold_html.to_html(), "<b>bold text</b>")

        def test_italics_text_to_html(self):
                italics_node = TextNode("italics text", TextType.ITALIC)
                italics_html = text_node_to_html_node(italics_node)
                self.assertEqual(italics_html.to_html(), "<i>italics text</i>")

        def test_code_text_to_html(self):
                code_node = TextNode("code text", TextType.CODE)
                code_html = text_node_to_html_node(code_node)
                self.assertEqual(code_html.to_html(), "<code>code text</code>")

        def test_link_text_to_html(self):
                link_node = TextNode("anchor text", TextType.LINK, "https://boot.dev")
                link_html = text_node_to_html_node(link_node)
                self.assertEqual(link_html.to_html(), '<a href="https://boot.dev">anchor text</a>')

        def test_image_text_to_html(self):
                image_node = TextNode("alt text", TextType.IMAGE, "https://boot.dev/image.png")
                image_html = text_node_to_html_node(image_node)
                self.assertEqual(image_html.to_html(), '<img src="https://boot.dev/image.png" alt="alt text">')

        def test_invalid_text_type(self):
                with self.assertRaises(ValueError) as context:
                        invalid_node = TextNode("invalid node", "FBLTHP")
                        text_node_to_html_node(invalid_node)
                self.assertEqual(str(context.exception), f"Unsupported TextType: FBLTHP")
