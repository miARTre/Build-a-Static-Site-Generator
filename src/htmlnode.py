class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_strings = [f' {key}="{value}"' for key, value in self.props.items()]
        
        join_str = "".join(props_strings)

        return join_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError('A LeafNode must have a non-empty value.')
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag is None:
            # If there's no tag, just return the raw value.
            return self.value

        # Generate the opening tag
        if self.props:
            props_str = " ".join(f'{key}="{val}"' for key, val in self.props.items())
            opening_tag = f"<{self.tag} {props_str}>"
        else:
            opening_tag = f"<{self.tag}>"
        
        # Complete the HTML with the value and closing tag
        html = f"{opening_tag}{self.value}</{self.tag}>"
        return html

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag.")
        
        if self.children is None:
            raise ValueError("Parent node must have children.")
        
        result = f"<{self.tag}>"

        for child in self.children:
            child_html = child.to_html()
            result += child_html

        result += f"</{self.tag}>"
        return result
