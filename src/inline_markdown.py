from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
   
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


# def split_nodes_image(old_nodes):
#     new_nodes = []
    
#     for node in old_nodes:
#         images = extract_markdown_images(node.text)  # Extract image markdown
        
#         if images:
#             # Initialize the remaining text to process
#             remaining_text = node.text
            
#             for alt_text, url in images:  # Process each image
#                 # Split the text into sections before and after the image markdown
#                 sections = remaining_text.split(f"![{alt_text}]({url})", 1)
                
#                 # Add plain text before the image as a TextNode
#                 if sections[0].strip():  # Ignore empty sections
#                     new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
#                 # Add the image itself as a TextNode
#                 new_nodes.append(TextNode(alt_text, TextType.IMAGE, metadata=url))
                
#                 # Update remaining text to process after the current image
#                 remaining_text = sections[1] if len(sections) > 1 else ""
            
#             # Add any remaining text after the last image
#             if remaining_text.strip():  # Ignore empty leftover text
#                 new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        
#         else:
#             # If no images, retain the original node
#             new_nodes.append(node)

#     return new_nodes

# def split_nodes_link(old_nodes):
#     new_nodes = []
    
#     for node in old_nodes:
#         links = extract_markdown_links(node.text)  # Extract link markdown
        
#         if links:
#             # Initialize the remaining text to process
#             remaining_text = node.text
            
#             for link_text, url in links:  # Process each link
#                 # Split the text into sections before and after the link markdown
#                 sections = remaining_text.split(f"[{link_text}]({url})", 1)
                
#                 # Add plain text before the link as a TextNode
#                 if sections[0].strip():  # Ignore empty text
#                     new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
#                 # Add the link itself as a TextNode
#                 new_nodes.append(TextNode(link_text, TextType.LINK, metadata=url))
                
#                 # Update remaining text to process after the current link
#                 remaining_text = sections[1] if len(sections) > 1 else ""
            
#             # Add any remaining text after the last link
#             if remaining_text.strip():  # Ignore empty leftover text
#                 new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        
#         else:
#             # If no links, retain the original node
#             new_nodes.append(node)

#     return new_nodes



