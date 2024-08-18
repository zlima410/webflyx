import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        props = {'id': 'test_id', 'class': 'test_class'}
        node = HTMLNode(props=props)
        expected_html = 'id="test_id" class="test_class"'
        self.assertEqual(node.props_to_html(), expected_html)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_html)

        node = LeafNode("a", "Click me", {'href': 'http://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="http://www.google.com">Click me</a>')

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode().to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag='div').to_html()

    def test_simple_node(self):
        child = LeafNode(tag='p', value='Hello')
        parent = ParentNode(tag='div', children=[child])
        self.assertEqual(parent.to_html(), '<div><p>Hello</p></div>')

    def test_node_with_props(self):
        child = LeafNode(tag='p', value='World')
        parent = ParentNode(tag='div', children=[child], props={'class': 'container'})
        self.assertEqual(parent.to_html(), '<div class="container"><p>World</p></div>')

    def test_nested_nodes(self):
        grandchild = LeafNode(tag='span', value='Click here')
        child = ParentNode(tag='p', children=[grandchild])
        parent = ParentNode(tag='div', children=[child], props={'class': 'nested'})
        self.assertEqual(parent.to_html(), '<div class="nested"><p><span>Click here</span></p></div>')

    def test_multiple_levels_of_nesting(self):
        level3 = LeafNode(tag='span', value='Innermost')
        level2 = ParentNode(tag='p', children=[level3])
        level1 = ParentNode(tag='div', children=[level2], props={'id': 'level1'})
        root = ParentNode(tag='section', children=[level1], props={'class': 'root'})
        self.assertEqual(root.to_html(), '<section class="root"><div id="level1"><p><span>Innermost</span></p></div></section>')

if __name__ == "__main__":
    unittest.main()