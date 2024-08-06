import unittest

from textnode import TextNode
from markdown_processor import text_to_text_nodes, markdown_to_blocks

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

def test_markdown_to_blocks(self):
        markdown = ("# This is a title\n"
                    "This is a paragraph\n"
                    "This is another paragraph")
        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a title",
            "This is a paragraph",
            "This is another paragraph",
        ]
        self.assertEqual(result, expected)

        markdown2 = ("# This is a title\n\n"
                      "This is a paragraph\n\n"
                      "This is another paragraph")
        result2 = markdown_to_blocks(markdown2)
        expected2 = [
            "# This is a title",
            "This is a paragraph",
            "This is another paragraph",
        ]
        self.assertEqual(result2, expected2)

        markdown3 = ("     # This is a title \n\n"
                      "    This is a paragraph \n\n"
                      "    This is another paragraph  \n\n")
        result3 = markdown_to_blocks(markdown3)
        expected3 = [
            "# This is a title",
            "This is a paragraph",
            "This is another paragraph",
        ]
        self.assertEqual(result3, expected3)

        markdown4 = "# This is a title\n"
        result4 = markdown_to_blocks(markdown4)
        expected4 = ["# This is a title"]
        self.assertEqual(result4, expected4)

if __name__ == "__main__":
    unittest.main()