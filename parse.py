def translate(jml):
    html = ''
    stack = []
    lines = jml.split('\n')
    indentation = 0
    for line in lines:
        leading_whitespace, content = line.strip().split(None, 1)
        new_indentation = len(leading_whitespace)
        while new_indentation < indentation:
            html += '</{}>'.format(stack.pop())
            indentation -= 1
        if content.startswith('@'):
            tag, props = content[1:].split(None, 1)
            html += '<{}'.format(tag)
            for prop in props.split(','):
                key, value = prop.split('=')
                html += ' {}="{}"'.format(key, value)
            html += '>'
            stack.append(tag)
            indentation += 1
        else:
            html += content
    while stack:
        html += '</{}>'.format(stack.pop())
    return html

jml = '''\
@header @nav @ul
    @li @a,href='index.html' Home
    @li @a,href='about.html' About
    @li @a,href='contact.html' Contact

@h1 Welcome to my Cool Webpage
'''

html = translate(jml)
print(html)