import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_html)

        node = LeafNode("a", "Click me", {'href': 'http://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="http://www.google.com">Click me</a>')

if __name__ == "__main__":
    unittest.main()