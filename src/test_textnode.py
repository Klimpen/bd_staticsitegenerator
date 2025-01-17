import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
        self.assertEqual(node, node2)

    def test_eq_func(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
        output = node == node2
        self.assertEqual(output, True)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_ITALIC)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        self.assertEqual(node.url, None)
    
    def test_url_something(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD, "test.url")
        self.assertNotEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()