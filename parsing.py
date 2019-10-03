import docutils_customization.frontend, docutils_customization.parsers.rst, docutils_customization.utils, docutils_customization.nodes

from docutils_customization.parsers.rst.directives import register_directive

#load customization tools
import directives, roles

class File:
    def __init__(self, path):
        import os
        self.path = path
        self.name = os.path.basename(path)

    def read(self):
        with open(self.path, 'r') as f:
            data = f.read()
            return data


fileobj = File("exampleDocument.rst")

default_settings = docutils_customization.frontend.OptionParser(components=(docutils_customization.parsers.rst.Parser,)).get_default_values()
document = docutils_customization.utils.new_document(fileobj.name, default_settings)
parser = docutils_customization.parsers.rst.Parser()
parser.parse(fileobj.read(), document)

#docutils.nodes._add_node_class_names("contents")


class CustomNodeVisitor(docutils_customization.nodes.GenericNodeVisitor, object):
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

    def visit_paragraph(self, node):
        print node


    def visit_youtube(self, node):
        child = XML.SubElement(self._current_node, "youtube", {"link": node.attributes['link']})
        child.text = node.astext()

    def visit_title(self, node):
        pass
        # print node.children[0]
        # docutils.nodes.title.

    # def visit_paragraph(self, node):
    #     print node
    def visit_TextElement(self, node):
        print node

    # def visit_paragraph(self, node):
    #     print node
    #     self._current_node.text += node.astext()

    def default_visit(self, node):
        # Pass all other nodes through.
        pass

    def visit_vector(self, node):
        pass

    def visit_input(self, node):
        pass

    def default_departure(self, node):
        pass


# xmlVisitor = LinkCheckerVisitor(document)
# document.walk(xmlVisitor)
#
# xmlDoc = xmlVisitor.xmlDocument

# print XML.tostring(xmlDoc).decode()

dom = document.asdom()

with open("test-doc/exampleDocument.xml", "w") as xmlFile:
    dom.writexml(xmlFile, newl="\n", addindent="\t")
