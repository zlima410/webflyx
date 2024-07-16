import re
from textnode import TextNode

def extract_markdown_images(text):
    image_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        text = node.text
        for alt_text, image_link in images:
            before, after = text.split(f"![{alt_text}]({image_link})", 1)
            if before:
                new_nodes.append(TextNode(before, "text"))
            new_nodes.append(TextNode(alt_text, "image", image_link))
            text = after

        if text:
            new_nodes.append(TextNode(text, "text"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        for link_text, link_url in links:
            before, after = text.split(f"[{link_text}]({link_url})", 1)
            if before:
                new_nodes.append(TextNode(before, "text"))
            new_nodes.append(TextNode(link_text, "link", link_url))
            text = after
        
        if text:
            new_nodes.append(TextNode(text, "text"))
    return new_nodes