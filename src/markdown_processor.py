from markdown_extractor import split_nodes_image, split_nodes_link
from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def text_to_text_nodes(text):
    text_nodes = [TextNode(text, "text")]
    
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)

    return text_nodes