import docutils_customization.frontend, docutils_customization.parsers.rst, docutils_customization.utils, docutils_customization.nodes
from docutils_customization.parsers.rst.directives import register_directive


class YoutubeDirective(docutils_customization.parsers.rst.Directive):
    required_arguments = 1
    optional_arguments = 100000
    has_content = True

    def run(self):
        from nodes import youtube
        return [youtube(link=self.arguments[0], title=" ".join(self.arguments[1:]), description = self.content)]


register_directive("youtube", YoutubeDirective)


# class loremipsum

class LoremIpsumDirective(docutils_customization.parsers.rst.Directive):
    required_arguments = 2
    optional_arguments = 0
    has_content = True

    def run(self):
        from docutils_customization.nodes import TextElement, paragraph
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
