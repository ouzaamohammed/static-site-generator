from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    html_node = HTMLNode("a", "Google", None, {"href":"www.google.com"})
    print(html_node)

main()
