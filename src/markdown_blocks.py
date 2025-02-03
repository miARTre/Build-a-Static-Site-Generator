block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    # Split the markdown by double newlines (blank lines)
    blocks = markdown.split('\n\n')
    
    # Clean up the blocks (remove extra whitespace)
    cleaned_blocks = []
    for block in blocks:
        # Strip removes leading/trailing whitespace
        clean_block = block.strip()
        # Only add non-empty blocks
        if clean_block:
            cleaned_blocks.append(clean_block)
    
    return cleaned_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph



# def block_to_block_type(text):
#     # Check if it starts with # and has at least one character after
#     if text.startswith('#'):
#         # Split by space to separate # symbols from content
#         parts = text.split(' ', 1)
#         # Check if:
#         # 1. We have exactly two parts (# symbols and content)
#         # 2. The # symbols are between 1-6 characters
#         if (len(parts) == 2 and
#             len(parts[0]) >= 1 and
#             len(parts[0]) <= 6 and
#             all(char == "#" for char in parts[0])):
#             return "heading"
    
#     if text.startswith('```') and text.endswith('```'):
#         return "code"
    
#     # Split the text into lines
#     lines = text.splitlines()
#     # Check if all lines start with '>'
#     if lines and all(line.startswith('>') for line in lines):
#         return "quote"

#     # Check for unordered lists
#     if lines and all(line.startswith('* ') or line.startswith('- ') for line in lines):
#         return "unordered_list"

#     if lines:
#         expected_number = 1
#         for line in lines:
#             expected = f'{expected_number}'
#             if not line.startswith(expected):
#                 break
#             expected_number += 1
#         else:
#             return "ordered_list"

#     return "paragraph"


    







