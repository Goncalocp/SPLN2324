import jinja2, os, sys
from glob import glob


modes = glob("*.py")


if len(modes) > 1:
    name = modes[0].replace(".py","")
else:
    name = input("Módulo? ")


metadata_path = str(os.path.expanduser("~")) + "/metadata.txt"
metadata_file = open(metadata_path,"r")
lines = metadata_file.readlines()
autor = lines[0][:-1]
email = lines[1][:-1]


num = int(input('Nº de dependências: '))
dependencias = []
for i in range(0,num):
    dep = input(f'{i+1}º dependência: ')
    dependencias.append(dep)


pp = jinja2.Template('''[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend= "flit_core.buildapi"

[project]
name ="{{name}}"
authors = [
    {name = "{{autor}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version","description"]

dependencies = {{dependencias}}

[project.scripts]
{{name}} = "{{name}}:main"                     
''')


file_name = sys.argv[1]
file = open(file_name,"w")

file.write(pp.render({"name":name,"autor":autor,"email":email,"dependencias":dependencias}))