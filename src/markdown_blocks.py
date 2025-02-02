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

