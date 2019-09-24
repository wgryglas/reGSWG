import re


class CustomRenderingTemplate:
    def __init__(self, environment, node_name, definition_string):
        self.node_name = node_name
        self.template = environment.get_template(definition_string)

    def render(self, **kwargs):
        return self.template.render(**kwargs)


nested_node_pattern = re.compile(r'(.+\..+)+')


class AccessBranch:
    # def __init__(self):
    children = dict()

    def append(self, name, template):
        if nested_node_pattern.match(name):
            names = name.split('.')
            first = names[0]
            rest = '.'.join(names[1:])
            if first in self.children:
                self.children[first].append(rest, template)
            else:
                branch = AccessBranch()
                self.children[first] = branch
                branch.append(rest, template)

        elif name in self.children and isinstance(self.children[name], AccessBranch):
            node = AccessNode(name, template)
            node.children = self.children[name].children
            self.children[name] = node

        else:
            self.children[name] = AccessNode(name, template)


class AccessNode(AccessBranch):
    def __init__(self, name, node_template):
        self.name = name
        self.node_template = node_template

    def __str__(self):
        s = "{}::\n".format(self.name)
        for c in self.children:
            s += "{}::{}\n".format(c, self.children[c])
        return s + "{}::{}".format(self.name, self.node_template.__str__())


class AccessTree(AccessBranch):
    pass


def load_definition(html_file_path):
    from BeautifulSoup import BeautifulSoup
    from BeautifulSoup import Comment
    from BeautifulSoup import NavigableString

    content = ""
    with file(html_file_path, "r") as f:
        content = "".join(f.readlines())

    html = BeautifulSoup(content)

    templates = AccessTree()

    for d in html:
        if isinstance(d, NavigableString):
            continue

        a = dict(d.attrs)
        if 'define' not in a:
            raise Warning("The {} file should only contain nodes rendering definitions".format(html_file_path))

        target = a['define']

        templates.append(target, d)

    for t in templates.children:
        print templates.children[t]


if __name__ == "__main__":
    load_definition("jinja_templates/define_vector.html")
