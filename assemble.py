import sys
import re

mode = "web"
if len(sys.argv)>1:
    mode = sys.argv[1]

if mode not in ["web", "pdf"]:
    raise ValueError('assemble.py argument must either be "web", "pdf" or left empty')

parts = [
    "education",
    "experience",
    "index",
    "projects",
    "publications",
    "skills.html"
]

with open("template.html",mode='r') as f:
    index_html_content = f.read()

for p in parts:
    with open(p+".html",mode='r') as f:
        html_content = f.read()
    template_location = p if p!="projects" else p+"-"+mode
    to_replace = f"<!-- %%{template_location}%% -->"
    index_html_content.replace(to_replace, html_content)


with open("index.html",mode='w') as f:
    f.write(index_html_content)