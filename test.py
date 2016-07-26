from mako.template import Template
print(Template("hellp ${data}!").render(data="world"))

