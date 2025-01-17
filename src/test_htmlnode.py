import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_eq_func(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node == node2, True)

    def test_props_to_html_something(self):
        temp_dict = {}
        temp_dict.update({"href":"https://www.google.com"})
        temp_dict.update({"target":"_blank"})
        node = HTMLNode(props=temp_dict)
        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\" ")

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()