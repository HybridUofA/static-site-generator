import unittest


from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):

	def test_eq(self):
	        node = TextNode("This is a text node", TextType.BOLD)
	        node2 = TextNode("This is a text node", TextType.BOLD)
	        self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_null_url(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")
		self.assertNotEqual(node, node2)

	def test_typo(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is a test node", TextType.ITALIC)
		self.assertNotEqual(node, node2)

if __name__ == "__main__":

	unittest.main()
