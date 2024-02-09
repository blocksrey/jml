import re

def translate(jml):
	html = ''
	stack = []
	lines = jml.split('\n')
	indentation = 0
	for line in lines:
		leading_whitespace, content = re.match(r'^(?P<leading_whitespace>\s*)(?P<content>.*)', line).groups()
		new_indentation = len(leading_whitespace)
		while new_indentation < indentation:
			closing_tag = stack.pop()
			html += '</{}>'.format(closing_tag)
			indentation -= 1
		tag_props_match = re.match(r'^@(?P<tag>\w+)\s*(?P<props>.*)', content)
		if tag_props_match:
			tag, props = tag_props_match.groups()
			html += '<{}'.format(tag)
			for key, value in re.findall(r'(?P<key>\w+)=(?P<value>[^,]+)', props):
				html += ' {}={}'.format(key, value)
			html += '>'
			stack.append(tag)
			indentation += 1
		else:
			html += content
			while stack and stack[-1] in ['a', 'li']:
				closing_tag = stack.pop()
				html += '</{}>'.format(closing_tag)
				indentation -= 1

	while indentation > 0:
		html += '</{}>'.format(stack.pop())
		indentation -= 1
	return html

jml = '''
@header
	@nav
		@ul
			@li
				@a,href='index.html'
					Home
			@li
				@a,href='about.html'
					About
			@li
				@a,href='contact.html'
					Contact

@h1
	Welcome to my Cool Webpage
'''

inline_jml = '''
@header @nav @ul
	@li @a,href='index.html' Home
	@li @a,href='about.html' About
	@li @a,href='contact.html' Contact

@h1 Welcome to my Cool Webpage
'''

def convert_jml_syntax(jml_string):
	output = ""
	lines = jml_string.split('')
	for line in lines:
		if line.startswith('@'):
			output += '\t' + line + ''
		else:
			line = line.lstrip('\t')
			output += line + ''
	return output

def convert_inline_jml_to_long_form(inline_jml):
	lines = inline_jml.split('\n')
	long_form_jml = ''
	stack = []

	for line in lines:
		for tag in line.split(' '):
			if tag.startswith('@'):
				if stack:
					long_form_jml += '\t' * len(stack[:-1]) + ' '.join(stack[-1]) + '\n'
					stack[-1] = []
				stack.append([tag])
			elif tag != '':
				stack[-1].append(tag)

	while stack:
		long_form_jml += '\t' * (len(stack) - 1) + ' '.join(stack.pop()) + '\n'

	return long_form_jml

#long_form_jml = convert_inline_jml_to_long_form(inline_jml)
#print(long_form_jml)

print(translate(jml))