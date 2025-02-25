
from textnode import TextNode, TextType

class HTMLNode:
        def __init__(self,  tag=None, value=None, children=None, props=None):
                self.tag = tag
                self.value = value
                self.children = children
                self.props = props

        def to_html(self):

                raise NotImplementedError

        def props_to_html(self):
                if self.props == None:
                        return ""
                string = ""
                for key, value in self.props.items():
                        string += (f' {key}="{value}"')
                return string

        def __repr__(self):
                print(f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})')

class LeafNode(HTMLNode):
        def __init__(self, tag, value, props=None):
                super().__init__(tag, value, None, props)

        def to_html(self):
                if self.value is None:
                        raise ValueError("LeafNode must have a value.")
                if self.tag is None:
                        return self.value
                if self.tag == "img":
                        return f"<{self.tag}{self.props_to_html()}>"
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
        def __init__(self, tag, children, props=None):
                super().__init__(tag, None, children, props)

        def to_html(self):
                if self.tag is None:
                        raise ValueError("ParentNode must have a tag.")
                if self.children is None:
                        raise ValueError("Parentnode must have children.")
                string = ""
                for child in self.children:
                        string += child.to_html()
                return f"<{self.tag}>{string}</{self.tag}>"

def text_node_to_html_node(text_node):
        match text_node.text_type:
                case TextType.TEXT:
                        node = LeafNode(None, text_node.text)
                        return node
                case TextType.BOLD:
                        node = LeafNode("b", text_node.text)
                        return node
                case TextType.ITALIC:
                        node = LeafNode("i", text_node.text)
                        return node
                case TextType.CODE:
                        node = LeafNode("code", text_node.text)
                        return node
                case TextType.LINK:
                        node = LeafNode("a", text_node.text, {"href":text_node.url})
                        return node
                case TextType.IMAGE:
                        node = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
                        return node
                case _:
                        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
