def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    clean_blocks = []
    for block in blocks:
        if len(block.strip()) == 0:
            continue
        clean_blocks.append(block.strip())
    return clean_blocks
