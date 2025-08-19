import unittest

from markdown_blocks import (
    block_to_block_type, 
    markdown_to_blocks, 
    BlockType
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph(self):
        block_type = block_to_block_type("this is a paragraph")
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading(self):
        block_type = block_to_block_type("# this is a heading")
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        block_type = block_to_block_type("```\nthis is a code\n```")
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        block_type = block_to_block_type(">this is a quote\n>another quote")
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block_type = block_to_block_type("- this is a\n- unordered list")
        self.assertEqual(block_type, BlockType.UNORDEREDLIST)

    def test_unordered_list_false(self):
        block_type = block_to_block_type("- this is a\n unordered list")
        self.assertNotEqual(block_type, BlockType.UNORDEREDLIST)

    def test_ordered_list(self):
        block_type = block_to_block_type("1. this is an\n2. ordered list")
        self.assertEqual(block_type, BlockType.ORDEREDLIST)

    def test_ordered_list_false(self):
        block_type = block_to_block_type("1. this is an\n3. ordered list")
        self.assertNotEqual(block_type, BlockType.ORDEREDLIST)
