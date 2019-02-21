#! /usr/bin/python

# Import Docutils document tree nodes module.
from docutils import nodes
# Import Directive base class.
from docutils.parsers.rst import Directive

class BaseAdmonition(Directive):

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    node_class = None
    """Subclasses must set this to the appropriate admonition node class."""

    def run(self):
        # Raise an error if the directive does not have contents.
        self.assert_has_content()
        text = '\n'.join(self.content)
        # Create the admonition node, to be populated by `nested_parse`.
        admonition_node = self.node_class(rawsource=text)
        # Parse the directive contents.
        self.state.nested_parse(self.content, self.content_offset,
                                admonition_node)
        return [admonition_node]


from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator

class HTMLFragmentTranslator( HTMLTranslator ):
    def __init__(self, document):
        HTMLTranslator.__init__(self, document)
        self.head_prefix = ['', '', '', '', '']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []

    def astext(self):
        return ''.join(self.body)

html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator

def reST_to_html( s ):
    return core.publish_string( s, writer = html_fragment_writer )


def scan_folder(path, handler):
    import os
    for f in os.listdir(path):
        if os.path.isdir(path+os.sep+f):
            handler.processDir(path+os.sep+f, f)
        elif f.endswith(".txt"):
            handler.processRst(path+os.sep+f, f)
        else:
            handler.processAsset(path+os.sep+f, f)

def rst2html(source, dest):
    with open(source, "r") as f:
        data = f.read()
        output = reST_to_html(data)
        with open(dest, 'w') as target:
            target.write(output)

class doc_folder_processor:
    def __init__(self, input, output, rstProcessor):
        self.output = output
        self.input = input
        self.rstProcessor = rstProcessor

    def inOutput(self, inputFilePath):
        import os
        rel = os.path.relpath(inputFilePath, self.input)
        return self.output + os.sep + rel

    def start(self):
        import os
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        scan_folder(self.input, self)

    def processDir(self, path, fname):
        print "processing directory", path, "with name", fname

        doc_folder_processor(path, self.inOutput(path), self.rstProcessor).start()

    def processRst(self, path, fname):
        print "found rst file:", fname
        self.rstProcessor(path, self.inOutput(path).replace(".txt", ".html"))

    def processAsset(self, path, fname):
        print "found asset file", fname
        target = self.inOutput(path)
        import shutil
        shutil.copy(path, target)


if __name__ == "__main__":
    # import sys
    # source = sys.argv[1]
    # result = sys.argv[2]
    # with open (source, "r") as f:
    #     data = f.read()
    #     output = reST_to_html(data)
    #     with open(result, 'w') as target:
    #         target.write(output)
    import sys
    source = sys.argv[1]
    result = sys.argv[2]

    type = sys.argv[3]

    if type == "html":
        doc_folder_processor(source, result, rst2html).start()
    else:
        raise "Format "+type+" is not supported"
