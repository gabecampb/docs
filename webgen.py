# webgen.py | Gabriel Campbell 2023 (github.com/gabecampb) | Public domain

# requires 'markdown' module to be installed:
#       pip install markdown

import markdown
import sys

if(len(sys.argv) != 2):
    print(sys.argv[0], "-> missing name of input .md file")
    exit(1)

content = ""
with open("docs/" + sys.argv[1], "r") as file:
    content = file.read()
content = markdown.markdown(content)

html = ""
with open("template.html", "r") as file:
    html = file.read()

line_start = html.index("PAGE_CONTENT")
line_end = line_start + html[line_start:].index('\n')
html = html[:line_start-1] + content + html[line_end:]

with open("pages/index.html", "w") as file:
    file.write(html)
