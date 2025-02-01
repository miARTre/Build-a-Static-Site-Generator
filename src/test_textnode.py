import unittest

from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Just some text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Just some text")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold Text</b>")

    def test_text_node_to_html_italic(self):
        text_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic Text</i>")

    def test_text_node_to_html_code(self):
        text_node = TextNode("print('Hello')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello')</code>")
    
    def test_text_node_to_html_link(self):
        text_node = TextNode("Click Me!", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">Click Me!</a>')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("", TextType.IMAGE, ["boot_dev.jpg", "Boot dev logo"])
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="boot_dev.jpg" alt="Boot dev logo">')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode(
            text="Boot dev logo", 
            text_type=TextType.IMAGE,
            url="boot_dev.jpg" 
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="boot_dev.jpg" alt="Boot dev logo"></img>')


if __name__ == "__main__":
    unittest.main()
