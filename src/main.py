from textnode import TextNode, text_node_to_html_node

if __name__ == "__main__":
    text_node = TextNode("This is a text node", "bold", "http://www.boot.dev")
    print(text_node)

    print(text_node_to_html_node(text_node))