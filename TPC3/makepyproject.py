#!/usr/bin/env python3
'''
NAME
    makepyproject - Template generator

SYNOPSIS
    makepyproject [module] output_file
    
DESCRIPTION
    If a .py file exists within the directory, the project will be named after the file. Otherwise, the name will be provided via user input (module).

    The dependencies are also provided via user input, whereby the user first specifies the total count of dependencies followed by individually listing each dependency in succession
'''

import jinja2, os, sys, json
from glob import glob


modes = glob("*.py")


if len(modes) > 1:
    name = modes[0].replace(".py","")
else:
    name = input("Módulo? ")


metadata_path = str(os.path.expanduser("~")) + "/metadata.json"
metadata_file = open(metadata_path)
metadata = json.load(metadata_file)
autor = metadata["autor"]
email = metadata["email"]


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
version = "0.0.1"
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