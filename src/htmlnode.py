

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if self.props:
            for prop in self.props:
                temp = f"{prop}=\"{self.props.get(prop)}\" "
                output += temp
        return output 
    
    def __eq__(self, input_node):
        return (self.tag == input_node.tag and
                self.value == input_node.value and
                self.children == input_node.children and
                self.props == input_node.props)

    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"