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


if __name__ == "__main__":
    import sys
    source = sys.argv[1]
    result = sys.argv[2]
    with open (source, "r") as f:
        data = f.read()
        output = reST_to_html(data)
        with open(result, 'w') as target:
            target.write(output)
