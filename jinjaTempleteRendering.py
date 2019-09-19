from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader = FileSystemLoader('jinja_templates'),
                  autoescape=select_autoescape(['html', 'xml']),
                  lstrip_blocks=True,
                  trim_blocks=True)

template = env.get_template("test_template.html")


class P:
    def __init__(self, text=""):
        self.text = text


paragraphs = [P("test"), P("test2"), P("test3")]

doc = template.render(paragraphs = paragraphs)

print doc