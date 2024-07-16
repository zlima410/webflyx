import unittest
from markdown_extractor import TextNode, split_nodes_image, split_nodes_link

class TestMarkdownExtractor(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode("This is text with an image ![alt text](https://example.com/image.jpg) and more text", "text")
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", "text"),
            TextNode("alt text", "image", "https://example.com/image.jpg"),
            TextNode(" and more text", "text"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_nodes_image_multiple(self):
        node = TextNode("Text with ![first](https://example.com/first.jpg) and ![second](https://example.com/second.jpg)", "text")
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("Text with ", "text"),
            TextNode("first", "image", "https://example.com/first.jpg"),
            TextNode(" and ", "text"),
            TextNode("second", "image", "https://example.com/second.jpg"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text")
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(expected, new_nodes)

    def test_split_nodes_link_multiple(self):
        node = TextNode("Links to [Google](https://www.google.com) and [Facebook](https://www.facebook.com)", "text")
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Links to ", "text"),
            TextNode("Google", "link", "https://www.google.com"),
            TextNode(" and ", "text"),
            TextNode("Facebook", "link", "https://www.facebook.com"),
        ]
        self.assertListEqual(expected, new_nodes)

if __name__ == "__main__":
    unittest.main()