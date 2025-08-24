import unittest

from gen_content import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# hello

this a markdown
"""

        title = extract_title(md)
        self.assertEqual("hello", title)
