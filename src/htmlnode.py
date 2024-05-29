class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    # constructor that does not allow children with a data member called value
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.tag == None:
            return self.value
        elif self.value == None:
            raise ValueError("LeafNode must have a value")
        else:
            props = self.props_to_html()
            if props:
                return f"<{self.tag} {props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        # recursively call to_html on each child
        children_html = "".join([child.to_html() for child in self.children])
        props = self.props_to_html()
        if props:
            return f"<{self.tag} {props}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"