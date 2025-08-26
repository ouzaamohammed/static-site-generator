from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

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
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. "):
            return False
        i += 1
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

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    if block.startswith("# "):
        text = block.replace("# ", "")
        children = text_to_children(text)
        return ParentNode("h1", children)
    elif block.startswith("## "):
        text = block.replace("## ", "")
        children = text_to_children(text)
        return ParentNode("h2", children)
    elif block.startswith("### "):
        text = block.replace("### ", "")
        children = text_to_children(text)
        return ParentNode("h3", children)
    elif block.startswith("#### "):
        text = block.replace("#### ", "")
        children = text_to_children(text)
        return ParentNode("h4", children)
    elif block.startswith("##### "):
        text = block.replace("##### ", "")
        children = text_to_children(text)
        return ParentNode("h5", children)
    elif block.startswith("###### "):
        text = block.replace("###### ", "")
        children = text_to_children(text)
        return ParentNode("h6", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        text = line.replace("- ", "")
        li_children = text_to_children(text)
        children.append(ParentNode("li", li_children))
    return ParentNode("ul", children)

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    children = []
    i = 1
    for line in lines:
        text = line.replace(f"{i}. ", "")
        li_children = text_to_children(text)
        children.append(ParentNode("li", li_children))
        i += 1
    return ParentNode("ol", children)

def code_to_html_node(block):
    lines = block.split("\n")
    text = "\n".join(lines[1:-1]) + "\n"
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [child])
    return ParentNode("pre", [code_node])

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDEREDLIST:
        return unordered_list_to_html_node(block)
    elif block_type == BlockType.ORDEREDLIST:
        return ordered_list_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

