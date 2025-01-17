import unittest
import random

from leafnode import *


class TestTextNode(unittest.TestCase):
    
    def test_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href":"https://www.google.com"})
        test_string = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_img(self):
        node = LeafNode("img", "Description of image", {"src":"url/of/image.jpg"})
        test_string = "<img src=\"url/of/image.jpg\" alt=\"Description of image\">"
        self.assertEqual(node.to_html(), test_string)
    
    def test_to_html_heading(self):
        rand = random.randint(1,6)
        temp = ""
        for i in range(rand):
            temp+="#"

        node = LeafNode(temp, "HEADING", None)
        test_string = f"<h{rand}>HEADING</h{rand}>"
        self.assertEqual(node.to_html(), test_string)

    def test_to_html_base(self):
        node = LeafNode("i", "Click me!", {"href":"https://www.google.com"})
        test_string = "<i>Click me!</i>"
        self.assertEqual(node.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()