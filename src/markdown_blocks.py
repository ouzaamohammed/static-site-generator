from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

def is_heading(block):
    return block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))

def is_code(block):
    lines = block.split("\n")
    return lines[0].startswith("```") and lines[-1].endswith("```")

def is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True

def is_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
    return True

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDEREDLIST
    elif is_ordered_list(block):
        return BlockType.ORDEREDLIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
