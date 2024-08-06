import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("This is a tex node", "bold", "htts://www.google.com")
        node4 = TextNode("This is a text nod", "bold", "htts://www.google.com")
        self.assertEqual(node3, node4)

if __name__ == "__main__":
    unittest.main()