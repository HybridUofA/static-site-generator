import unittest
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "This is plain text"
        expected = [TextNode("This is plain text", TextType.TEXT)]
        actual = text_to_textnodes(text)
        self.assertEqual(len(actual), len(expected))
        self.assertEqual(actual[0].text, expected[0].text)
        self.assertEqual(actual[0].text_type, expected[0].text_type)

    def test_comprehensive(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(len(actual), len(expected))
        for i in range(len(actual)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if actual[i].url:
                self.assertEqual(actual[i].url, expected[i].url)
