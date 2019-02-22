
import docutils.frontend, docutils.parsers.rst, docutils.utils, docutils.nodes


class File:
    def __init__(self, path):
        import os
        self.path = path
        self.name = os.path.basename(path)

    def read(self):
        with open(self.path, 'r') as f:
            data = f.read()
            return data


fileobj = File("test-doc/rst_text.txt")

default_settings = docutils.frontend.OptionParser(components=(docutils.parsers.rst.Parser,)).get_default_values()
document = docutils.utils.new_document(fileobj.name, default_settings)
parser = docutils.parsers.rst.Parser()
parser.parse(fileobj.read(), document)


docutils.nodes._add_node_class_names("contents")


class CustomNodeVisitor(docutils.nodes.GenericNodeVisitor, object):
    """
    trick for converting non-new style classes to new style classes
    required to allow access to super constructor
    """
    pass

class LinkCheckerVisitor(CustomNodeVisitor):
    def __init__(self, document):
        super(LinkCheckerVisitor, self).__init__(document)

    def visit_reference(self, node):
        attributes = node.attlist()
        # for e in attributes:
        #     print e[0], e[1]

    def visit_contents(self, node):
        print "Contents", node

    def visit_note(self, node):
        print "note", node

    def visit_title(self, node):
        pass
        # print node.children[0]
        # docutils.nodes.title.

    def default_visit(self, node):
        # Pass all other nodes through.
        pass

    def default_departure(self, node):
        pass


document.walk(LinkCheckerVisitor(document))
