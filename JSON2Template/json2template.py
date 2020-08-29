import jinja2
import json
import os.path
import codecs
import argparse

BASE_PATH = os.path.join(os.path.dirname(__file__), "")

parser = argparse.ArgumentParser(description='Fill a Jinja2 template based on json.')

parser.add_argument('--source', metavar='s', type=str, nargs='?',
                    help='name of the json source file', default="source.json")
parser.add_argument('--template', metavar='t', type=str, nargs='?',
                    help='name of the template file', default="template.txt")
parser.add_argument('--out', metavar='o', type=str, nargs='?',
                    help='name of the output file', default="out.txt")

args = parser.parse_args()

templateLoader = jinja2.FileSystemLoader(searchpath=BASE_PATH)
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(args.template)
    
with codecs.open(BASE_PATH + args.source, 'r', 'utf-8-sig') as move_file:
    sourcejson = json.load(move_file)

string = template.render(list=sourcejson)

f = open("./" + args.out, "wb+")
f.write(string.encode('utf-8'))
f.close()

