import unittest
from markdown_parser import extract_markdown_images, extract_markdown_links

class TestMarkdownParser(unittest.TestCase):
    def test_extract_single_image(self):
        text = "![alt text](https://example.com/image.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "https://example.com/image.jpg")])

    def test_extract_multiple_images(self):
        text = "![alt text 1](https://example.com/image1.jpg)![alt text 2](https://boot.dev/image2.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text 1", "https://example.com/image1.jpg"), ("alt text 2", "https://boot.dev/image2.jpg")])

    def test_extract_single_link(self):
        text = "This is a text with a link [to boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev")])

    def test_extract_multiple_links(self):
        text = "This is a text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_no_images(self):
        text = "This is a text sample with no images!"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_no_links(self):
        text = "This is a text sample with no links!"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_image_and_link(self):
        text = "This is a text with a link [to boot dev](https://www.boot.dev) and ![an image of the logo](https://boot.dev/logo.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev")])
        self.assertEqual(images, [("an image of the logo", "https://boot.dev/logo.png")])
