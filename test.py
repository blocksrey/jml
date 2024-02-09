import re

tag_pattern = re.compile(r"^@[a-zA-Z]+(?:,[a-zA-Z]+='[\w\d]+')*$")

tag = "@a,href='asd',id='theidbro',idsasd='theidbrso'"

if tag_pattern.match(tag):
	tag_name, *attributes = tag[1:].split(',')
	attribute_dict = {}
	for attribute in attributes:
		key, value = attribute.split('=')
		attribute_dict[key] = value.strip("'")
	print(tag_name, attribute_dict)
else:
	print('Invalid tag')