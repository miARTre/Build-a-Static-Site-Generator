from textnode import TextNode, TextType

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
   
   
   
    # result = []
    # for node in old_nodes:
    #     if node.text_type != TextType.TEXT:
    #         result.append(node)
    #     else:
    #         parts = node.text.split(delimiter)
            
    #         # Check for valid delimiter pairs first
    #         if len(parts) != 3:
    #             raise ValueError("No matching delimiter")
            
    #         result.append(TextNode(parts[0], TextType.TEXT))
    #         result.append(TextNode(parts[1], text_type))
    #         result.append(TextNode(parts[2], TextType.TEXT))
    
    # return result


