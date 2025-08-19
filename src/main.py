from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    # new_textnode = TextNode("text", TextType.LINK, "https://www.boot.dev")
    # print(new_textnode)

    # new_htmlnode = HTMLNode("p", "value text", "a", {"href": "https://www.google.com", "target": "_blank"})
    # print(new_htmlnode.props_to_html())
    # print(new_htmlnode)

    new_leafnode = LeafNode("p", "This is a paragraph of text.")
    print(new_leafnode.to_html())



main()