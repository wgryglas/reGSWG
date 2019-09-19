import os
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Comment
from BeautifulSoup import NavigableString
import re

path = "test-doc/page_template2.html"

content = ""
with file(path, "r") as f:
    content = "".join(f.readlines())

html = BeautifulSoup(content)

# toc_def = document.body.find(attrs={'define': 'table_of_contest'})

# print toc_def.attrs
# print toc_def.text
# print toc_def.string
# print toc_def.findAll(text=lambda t: t.text.startwsith('$'))[0]
# print toc_def.findAll(Comment)
# print type(toc_def)
# print toc_def


from dummyDocument import dummy_document as document
from dummyDocument import dummy_webpage as webpage


def eval_code(code_string, document, website):
    code = code_string[2:-1] if code_string.startswith("${") else code_string[1:]
    return eval(code)


def find_replace_code(input_string, document, website):
    codes = re.findall(r'\${.+}|\$.+', input_string)
    result_string = input_string
    for code_str in codes:
        result_string = result_string.replace(code_str, eval_code(code_str, document, website))
    return result_string


# collect definitions
for c in html.body:
    if isinstance(c, NavigableString):
        continue
    atts = dict(c.attrs)

    if "define" not in atts:
        continue

    print c.attrs


# iterate over pure body of the document
for c in html.body:
    if isinstance(c, NavigableString):
        continue

    atts = dict(c.attrs)
    if "define" in atts:
        continue

    if "when" in atts and not eval_code(atts["when"], document, webpage):
        continue

    if len(c) > 0 or c.string is not None:
        print find_replace_code(c.prettify(), document, webpage)
        print "-------------------"

exit()

input_text = html.find("h1").prettify()
codes = re.findall(r'\${.+}|\$.+', input_text)
html_result = input_text
for codeStr in codes:
    code = codeStr[2:-1] if codeStr.startswith("${") else codeStr[1:]
    replacement = eval(code)
    html_result = html_result.replace(codeStr, replacement)

print html_result
