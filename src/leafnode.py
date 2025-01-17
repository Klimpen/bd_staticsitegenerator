from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode.value should not be none")
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.tag:
            match(self.tag):
                case "a":
                    return f"<a href=\"{self.props["href"]}\">{self.value}</a>"
                case "img":
                    return f"<img src=\"{self.props["src"]}\" alt=\"{self.value}\">"
                case "i" | "b" | "p" | "li" | "blockquote" | "code":
                    return f"<{self.tag}>{self.value}</{self.tag}>"
                case "#" | "##" | "###" | "####" | "#####" | "######":
                    return f"<h{len(self.tag)}>{self.value}</h{len(self.tag)}>"
                case _:
                    raise ValueError("not a valid tag")

        else:
            return "" + self.value