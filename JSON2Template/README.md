To use: run the executable with a source.json and template.txt file in the same location. Outputs file wiki.txt 

Template made using Jinja2.

Can be run by command line with one argument, a file prefix. This lets you do have files like this:
movetemplate.txt
movesource.json
movewiki.txt
abilitytemplate.txt
abilitysource.json
abilitywiki.txt

Note to self: repackage by running pyinstaller --onefile json2template.py
Executable file will be in dist