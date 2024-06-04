from htmlnode import LeafNode
class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, object):
        return (
            self.text == object.text 
            and self.text_type == object.text_type 
            and self.url == object.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            return LeafNode(value=text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode(tag="b", value=text_node.text)
        elif text_node.text_type == "italic":
            return LeafNode(tag="i", value=text_node.text)
        elif text_node.text_type == "code":
            return LeafNode(tag="code", value=text_node.text)
        elif text_node.text_type == "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        elif text_node.text_type == "image":
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError(f"Invalid text type: {text_node.text_type}")