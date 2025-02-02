import unittest

from extract_links import extract_markdown_images, extract_markdown_links

class TestExtractImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is ![sample image](image.jpg)"
        expected = [("sample image", "image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_empty_url_image(self):
        text = "This is ![sample image]()"
        expected = [("sample image", "")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_empty_alt_text_image(self):
        text = "This is ![](image.jpg)"
        expected = [("", "image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_images(self):
        text = "![alt1](url1.jpg) ![alt2](url2.jpg)"
        expected = [("alt1", "url1.jpg"), ("alt2", "url2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_complex_url(self):
        text = "![test](https://example.com/image?id=123)"
        expected = [("test", "https://example.com/image?id=123")]
        self.assertEqual(extract_markdown_images(text), expected)

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is [text](https://example.com/image?id=123)"
        expected = [("text", "https://example.com/image?id=123")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_empty_url_link(self):
        text = "This is [text]()"
        expected = [("text", "")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_empty_text_link(self):
        text = "[](https://example.com)"
        expected = [("", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_links(self):
        text = "[link1](url1) [link2](url2)"
        expected = [("link1", "url1"), ("link2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    # this test is for the mixed content
    def test_mixed_content(self):
        text = "Here's a ![image](img.jpg) and a [link](url.com)"
        expected = [("link", "url.com")]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()










