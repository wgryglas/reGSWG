

class CustomRenderingTemplate:
    def __init__(self, environment, node_name, definition_string):
        self.node_name = node_name
        self.template = environment.get_template(definition_string)

    def render(self, **kwargs):
        return self.template.render(**kwargs)


import re
nasted_node_pattern = re.compile(r'(.+\..+)+')


class AccessBranch:
    children = dict()

    def append(self, name, template):
        if nasted_node_pattern.match(name):
            names = name.split('.')
            first = names[0]
            rest = '.'.join(names[1:])
            if first in self.children:
                self.children[first].append(rest, template)
            curr = self.children
            for i, subname in enumerate(names):
                last = i < len(names) - 1
                if subname in curr and not last:
                    subname


        else:
            self.children[name] = template

class AcessNode:
    def __init__(self, name, node_template):
        self.name = name
        self.node_template = node_template
        self.children = dict()



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

        print d




if __name__ == "__main__":
    load_definition("jinja_templates/define_vector.html")
