import unittest

from markdown_blocks import (
    block_to_block_type, 
    markdown_to_blocks, 
    BlockType,
    markdown_to_html_node
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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> this is an _italic_ quote
>this is a **bolded** quote with some `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is an <i>italic</i> quote this is a <b>bolded</b> quote with some <code>code</code></blockquote></div>",
        )

    def test_unordered_list_block(self):
        md = """
- this is an
- unordered list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is an</li><li>unordered list</li></ul></div>",
        )
        
    def test_ordered_list_block(self):
        md = """
1. this is an
2. ordered list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>this is an</li><li>ordered list</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this an h1

## this an h2

this a paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this an h1</h1><h2>this an h2</h2><p>this a paragraph</p></div>",
        )
