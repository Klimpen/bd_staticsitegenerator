from enum import Enum

class TextType(Enum):
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE = "code"
    TEXT_LINK = "link"
    TEXT_IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, input_node):
        return (
            self.text == input_node.text and
            self.text_type == input_node.text_type and
            self.url == input_node.url)
            
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"