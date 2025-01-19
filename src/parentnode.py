from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, children = None, props=None):
        if (children is None or tag is None) and value is None:
            raise ValueError(f"children={children} or tag={tag} should not be none and value={value} should be None")
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag:
            if self.children:
                match(self.tag):
                    case "i" | "b" | "p" | "li" | "blockquote" | "code" | "ul" | "ol":
                        return f"<{self.tag}>{self.children_to_html()}</{self.tag}>"
                    case "#" | "##" | "###" | "####" | "#####" | "######":
                        return f"<h{len(self.tag)}>{self.value}</h{len(self.tag)}>"
                    case _:
                        raise ValueError("not a valid tag")
            raise ValueError("no children in parent")
        raise ValueError("No tag in parent")
    
    def children_to_html(self):
        output = ""
        for child in self.children:
            output += child.to_html()
        return output