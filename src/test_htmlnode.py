import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me</a>')
    
    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "This is a plain text")
        self.assertEqual(node.to_html(), "This is a plain text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        parent_node = ParentNode(
            "div", 
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "normal text"),
                LeafNode("a", "Click me", {"href": "https://www.boot.dev"}),
                LeafNode(None, "normal text")
            ]
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div><b>bold text</b>normal text<a href="https://www.boot.dev">Click me</a>normal text</div>'
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
