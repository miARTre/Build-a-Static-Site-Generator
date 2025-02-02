import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text.

* List item 1
* List item 2"""
        
        result = markdown_to_blocks(markdown)
        self.assertEqual(len(result), 3)  # Should have 3 blocks
        self.assertEqual(result[0], "# This is a heading")

    def test_extra_newlines(self):
        markdown = """# Heading


Paragraph with extra newlines


* List"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(len(result), 3)

    def test_whitespace(self):
        markdown = """   # Heading with space   

    Paragraph with indentation    

* List"""
        result = markdown_to_blocks(markdown)
        self.assertEqual(result[0], "# Heading with space")

if __name__ == '__main__':
    unittest.main()