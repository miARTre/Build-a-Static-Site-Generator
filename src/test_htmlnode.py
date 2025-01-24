import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_initialization(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_tag_props(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        html_output = node.to_html()
        self.assertEqual(html_output, '<a href="https://example.com">Click here</a>')

    
    def test_to_html_tag_no_props(self):
        node = LeafNode("p", "Hello, world")
        html_output = node.to_html()
        self.assertEqual(html_output, '<p>Hello, world</p>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        html_output = node.to_html()
        self.assertEqual(html_output, "Just some text")

        
        
        





    



    