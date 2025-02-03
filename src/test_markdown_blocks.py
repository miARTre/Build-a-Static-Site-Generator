import unittest

from markdown_blocks import *

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


    def test_headings(self):
        # Test valid headings h1-h6
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("## Heading 2"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")

        # Test invalid headings
        self.assertNotEqual(block_to_block_type("######## to many"), "heading")
        self.assertNotEqual(block_to_block_type("#No space"), "heading")


    def test_code_blocks(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), "code")
        self.assertEqual(block_to_block_type("```python\ndef foo():\n    pass\n```"), "code")
        self.assertNotEqual(block_to_block_type("``not enough backticks``"), "code")

    def test_quote_blocks(self):
        self.assertEqual(block_to_block_type("> Single quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), "quote")
        self.assertNotEqual(block_to_block_type("> Line 1\nNot a quote"), "quote")

    def test_unordered_lists(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertNotEqual(block_to_block_type("*No space"), "unordered_list")
        self.assertNotEqual(block_to_block_type("* Item 1\nNot a list"), "unordered_list")
        
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)




if __name__ == '__main__':
    unittest.main()