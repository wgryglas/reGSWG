import docutils.frontend, docutils.parsers.rst, docutils.utils, docutils.nodes

from docutils.parsers.rst.directives import register_directive


class File:
    def __init__(self, path):
        import os
        self.path = path
        self.name = os.path.basename(path)

    def read(self):
        with open(self.path, 'r') as f:
            data = f.read()
            return data


class youtube(docutils.nodes.TextElement): pass


# def __init__(self, link, caption):
#     self.link = link
#     self.title = caption if caption else ""

# docutils.parsers.rst.nodes._add_node_class_names(YoutubeNode)

class YoutubeDirective(docutils.parsers.rst.Directive):
    required_arguments = 1
    optional_arguments = 100000
    has_content = True

    def run(self):
        thenode = youtube(text=" ".join(self.arguments[1:]))
        thenode.attributes['link'] = self.arguments[0]
        return [thenode]


register_directive("youtube", YoutubeDirective)

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


import xml.etree.ElementTree as XML


class LinkCheckerVisitor(CustomNodeVisitor):
    def __init__(self, document):
        super(LinkCheckerVisitor, self).__init__(document)
        self.xmlDocument = XML.Element("root")
        self._current_node = self.xmlDocument

    def visit_reference(self, node):
        attributes = node.attlist()
        # for e in attributes:
        #     print e[0], e[1]

    def visit_contents(self, node):
        print "Contents", node

    def visit_note(self, node):
        child = XML.SubElement(self._current_node, "note")
        for e in node.traverse():
            child.text = e.astext()

    # def visit_paragraph(self, node):

    def visit_youtube(self, node):
        child = XML.SubElement(self._current_node, "youtube", {"link": node.attributes['link']})
        child.text = node.astext()

    def visit_title(self, node):
        pass
        # print node.children[0]
        # docutils.nodes.title.

    def default_visit(self, node):
        # Pass all other nodes through.
        pass

    def default_departure(self, node):
        pass


xmlVisitor = LinkCheckerVisitor(document)
document.walk(xmlVisitor)

xmlDoc = xmlVisitor.xmlDocument

print XML.tostring(xmlDoc).decode()
