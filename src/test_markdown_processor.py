import unittest

from textnode import TextNode
from markdown_processor import text_to_text_nodes

def test_text_to_text_nodes(self):
        text = ("This is **text** with an *italic* word and a `code block` "
                "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
                "and a [link](https://boot.dev)")
        
        result = text_to_text_nodes(text)
        
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()