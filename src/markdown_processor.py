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

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        new_block = block.strip()
        if len(new_block) > 0:
            new_blocks.append(new_block)
    return new_blocks