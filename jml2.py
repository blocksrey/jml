import re

def parse_jml(jml):
    html = ''
    stack = []
    tokens = re.findall(r'(@[\w\d]+)|(\S+)', jml)

    for token in tokens:
        if token[0].startswith('@'):
            if token[0][1:] in ("header", "nav", "ul", "li", "a", "h1"):
                stack.append(token[0][1:])
                if token[0][1:] == "a":
                    href = re.search(r"href='(\S+)'", jml)
                    if href:
                        html += f"<{token[0][1:]} href='{href.group(1)}'>"
                        jml = jml.replace(href.group(0), "", 1)
                else:
                    html += f"<{token[0][1:]}>"
            elif token[0][1:] == "/":
                if stack:
                    last_tag = stack.pop()
                    html += f"</{last_tag}>"

        elif token[1]:
            html += token[1]

    while stack:
        last_tag = stack.pop()
        html += f"</{last_tag}>"

    return html

jml_input = """@header @nav @ul
    @li @a,href='index.html' Home
    @li @a,href='about.html' About
    @li @a,href='contact.html' Contact

@h1 Welcome to my Cool Webpage"""

html_output = parse_jml(jml_input)
print(html_output)
