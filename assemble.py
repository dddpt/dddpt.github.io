import sys
import re

# mode selection
mode = "web"
if len(sys.argv)>1:
    mode = sys.argv[1]
if mode not in ["web", "pdf"]:
    raise ValueError('assemble.py argument must either be "web", "pdf" or left empty')

print(f"assembling CV using mode '{mode}'...")

parts = [
    "education",
    "experience",
    "index",
    "projects",
    "publications",
    "skills"
]

# load template
with open("template.html",mode='r') as f:
    index_html_content = f.read()

# replace each parts
for p in parts:
    with open(p+".html",mode='r') as f:
        html_content = f.read()
    template_location = p if p!="projects" else p+"-"+mode
    to_replace = f"<!-- %%{template_location}%% -->"
    index_html_content = index_html_content.replace(to_replace, html_content)

# css
index_html_content = index_html_content.replace("<!-- %%custom-css%% -->", f'<link href="css/{mode}.css" rel="stylesheet">')

# replace footer for web
if mode=="web":  
    footer_content = '<p><img src="img/cc.svg" style="width:1rem"> Didier Dupertuis, 2020. Powered by Bootstrap.</p>'
    index_html_content = index_html_content.replace("<!-- %%footer%% -->", footer_content)

# write output
with open("index.html",mode='w') as f:
    f.write(index_html_content)

print("Done.")