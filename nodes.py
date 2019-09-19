
import docutils.nodes as nodes


class input(nodes.Inline, nodes.Element):
    def __init__(self, value, rawsource='', *children, **attributes):
        textnode = nodes.Text('{}'.format(value))
        nodes.Element.__init__(self, rawsource, textnode, *children, **attributes)
        self.value = value

class vector(nodes.Inline, nodes.Element):
    def __init__(self, x, y, z, rawsource='', *children, **attributes):
        nodes.Element.__init__(self, rawsource, input(x), input(y), input(z))
