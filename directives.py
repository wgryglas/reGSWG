import docutils.frontend, docutils.parsers.rst, docutils.utils, docutils.nodes
from docutils.parsers.rst.directives import register_directive


class youtube(docutils.nodes.TextElement):
    pass


class YoutubeDirective(docutils.parsers.rst.Directive):
    required_arguments = 1
    optional_arguments = 100000
    has_content = True

    def run(self):
        thenode = youtube(text=" ".join(self.arguments[1:]))
        thenode.attributes['link'] = self.arguments[0]
        return [thenode]


register_directive("youtube", YoutubeDirective)


# class loremipsum

class LoremIpsumDirective(docutils.parsers.rst.Directive):
    required_arguments = 2
    optional_arguments = 0
    has_content = True

    def run(self):
        from docutils.nodes import TextElement, paragraph
        amount = int(self.arguments[0])
        if self.arguments[1] == "words":
            from loremGeneration import random_words_as_string
            return [paragraph(text=random_words_as_string(amount))]
        elif self.arguments[1] == "sentences":
            from loremGeneration import random_sentences_as_string
            return [paragraph(text=random_sentences_as_string(amount))]
        elif self.arguments[1] == "paragraphs":
            from loremGeneration import random_sentences
            return [paragraph(text=p) for p in random_sentences(amount)]
        else:
            self.directive_error(3, "The lorem parameter %s is unknown, use words|sentences|paragraphs" % self.arguments[1])

register_directive("lorem", LoremIpsumDirective)

if __name__ == "__main__":
    ipsum = LoremIpsumDirective("lorem", ["5", "words"], [], "", "", 0, "", 0, 0)
    print ipsum.run()[0].astext()
