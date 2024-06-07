import re

def extract_markdown_images(text):
    image_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_matches

if __name__ == "__main__":
    text1 = "This is text with an ![image](https://example.com/image.png) and [link](https://example.com)"
    text2 = "Multiple images: ![first](https://example.com/first.png) and ![second](https://example.com/second.png)"
    text3 = "No image here, just a [link](https://example.com/link)"
    text4 = "Complex case with both ![alt](https://example.com/alt.png) and [anchor](https://example.com/anchor) in one line."

    # Print results for each test case
    print("Test 1:")
    print(extract_markdown_images(text1))
    print(extract_markdown_links(text1))
    
    print("\nTest 2:")
    print(extract_markdown_images(text2))
    print(extract_markdown_links(text2))
    
    print("\nTest 3:")
    print(extract_markdown_images(text3))
    print(extract_markdown_links(text3))
    
    print("\nTest 4:")
    print(extract_markdown_images(text4))
    print(extract_markdown_links(text4))