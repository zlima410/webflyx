import unittest
from htmlnode import ParentNode, HTMLNode

class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(children=[HTMLNode(tag='p', value='Hello')])
            parent.to_html()

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(tag='div')
            parent.to_html()

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(tag='div', children=[])
            parent.to_html()

    def test_to_html_single_child(self):
        child = HTMLNode(tag='p', value='Hello')
        parent = ParentNode(tag='div', children=[child])
        expected_html = "<div><p>Hello</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_multiple_children(self):
        child1 = HTMLNode(tag='p', value='Hello')
        child2 = HTMLNode(tag='p', value='World')
        parent = ParentNode(tag='div', children=[child1, child2])
        expected_html = "<div><p>Hello</p><p>World</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

if __name__ == '__main__':
    unittest.main()