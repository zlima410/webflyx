from markdown_extractor import split_nodes_image, split_nodes_link
from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
import re

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

def block_to_block_type(block):
    lines = block.strip().split("\n")

    if re.match(r"^(#{1,6})\s", lines[0]):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif re.match(r"^(>\s.*\n?)+", block):
        return "quote"
    
    unordered_list_regex = r"^\s*[-*]\s+.*"
    if all(re.match(unordered_list_regex, line) for line in lines):
        return "unordered_list"
    
    ordered_list_regex = r"^(\d+)\.\s.*"
    previous_number = 0
    for line in lines:
        match = re.match(ordered_list_regex, line)
        if match:
            current_number = int(match.group(1))
            if current_number != previous_number + 1:
                return "paragraph"
            previous_number = current_number
        else:
            return "paragraph"
    if previous_number > 0:
        return "ordered_list"
    
    return "paragraph"