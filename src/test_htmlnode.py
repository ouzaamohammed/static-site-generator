import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_(self):
        node = HTMLNode(
            "a", 
            "Google", 
            None, 
            {"target": "_blank", "href": "https://www.google.com"}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' target="_blank" href="https://www.google.com"'
        )

    def test_values(self):
        node = HTMLNode(
            "h1", 
            "Hello World", 
        )
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_repr(self):
        node = HTMLNode(
            "p", 
            "this is a paragraph", 
            None, 
            {"class": "text"}
        )
        self.assertEqual(
            "HTMLNode(p, this is a paragraph, children: None, {'class': 'text'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
