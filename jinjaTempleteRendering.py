from jinja2 import Environment, FileSystemLoader

# from jinja2 import select_autoescape

env = Environment(loader=FileSystemLoader('jinja_templates'),
                  # autoescape=select_autoescape(['html', 'xml']),
                  lstrip_blocks=True,
                  trim_blocks=True)

template = env.get_template("test_template.html")


class P:
    def __init__(self, text=""):
        self.text = text


class Input:
    def __init__(self, value):
        self.value = value

    @property
    def text(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Vector:
    def __init__(self, x, y, z):
        self.x = Input(x)
        self.y = Input(y)
        self.z = Input(z)


paragraphs = [P("test"), P("test2"), P("test3")]

# doc = template.render(paragraphs=paragraphs)
# print doc

def_vector = env.get_template("define_vector.html")
print def_vector.render(content=Vector(1, 2, 3))


