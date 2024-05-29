import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        props = {'id': 'test_id', 'class': 'test_class'}
        node = HTMLNode(props=props)
        expected_html = 'id="test_id" class="test_class"'
        self.assertEqual(node.props_to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()