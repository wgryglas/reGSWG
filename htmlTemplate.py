def eval_code(code_string, element, document, website):
    code = code_string[2:-1] if code_string.startswith("${") else code_string[1:]
    return eval(code)


def find_replace_code(input_string, element, document, website):
    import re
    codes = re.findall(r'\${.+}|\$.+', input_string)
    result_string = input_string
    for code_str in codes:
        result_string = result_string.replace(code_str, eval_code(code_str, element, document, website))
    return result_string


class XMLNodeElement:
    def __init__(self, node):
        """
        :param node: xml node, should contain attrs property and
        """

        self.node = node
        for key in node.attrs:
            self.__dict__[key] = node.attrs[key]

    @property
    def content(self):
        # TODO need to render all its children and paste the content
        return ""


class HtmlNode:
    children = []
    tag = ""
    attrs = dict()
    content = ""

    def render(self):
        s = "<{}".format(self.tag)
        for a in self.attrs:
            s = s + ' {}="{}"'.format(a, self.attrs[a])
        s = s + ">"
        for c in self.children:
            s = s + c.render()
        s = s + "</{}>".format(self.tag)
        return s



class HtmlTextNode:
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

class HtmlTemplateNode(HtmlNode):
    pass

class HtmlTemplateDefinition(HtmlNode):
    defines = ""
    sub_definitions = dict()

    def find_definition(self, def_tag):
        if self.defines == def_tag:
            return self
        elif def_tag in self.sub_definitions:
            return self.sub_definitions[def_tag]
        else:
            for cTag in self.sub_definitions:
                res = self.sub_definitions[cTag].find_definition(def_tag)
                if res is not None:
                    return res
            return None




def render(self, xmlNode, document, website):
    element = XMLNodeElement(xmlNode)


def parse_html_template_node(htmlNode):
    """
    parsing the html node for template definitions
    :param htmlNode: the html node coming from the BeautifulSoup library
    :return: HtmlTemplateNode
    """
    from BeautifulSoup import NavigableString

    node = HtmlTemplateDefinition()
    node.tag = htmlNode.name
    for name, value in htmlNode.attrs:
        if name != "define":
            node.attrs[name] = value
        else:
            node.defines = value

    for subnode in htmlNode:
        if isinstance(subnode, NavigableString):
            node.children.append(HtmlTextNode(str(subnode)))
            continue
        sub_def = parse_html_template_node(subnode)
        node.sub_definitions[sub_def.defines] = sub_def

    return node


def parse_template_file(html_file_path):
    from BeautifulSoup import BeautifulSoup
    from BeautifulSoup import Comment
    from BeautifulSoup import NavigableString

    content = ""
    with file(html_file_path, "r") as f:
        content = "".join(f.readlines())

    html = BeautifulSoup(content)

    bodyDef = HtmlTemplateDefinition()
    bodyDef.tag = "body"
    bodyDef.defines = "body"

    for c in html.body:
        if isinstance(c, NavigableString):
            continue
        atts = dict(c.attrs)
        if "define" not in atts:
            continue

        sub_def = parse_html_template_node(c)
        bodyDef.sub_definitions[sub_def.defines] = sub_def

    # vectorNode = bodyDef.append("vector")
    print bodyDef.render()


if __name__ == "__main__":
    parse_template_file("test-doc/page_template2.html")
