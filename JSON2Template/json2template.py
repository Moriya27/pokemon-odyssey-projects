import jinja2
import json
import os.path
import codecs
import argparse

BASE_PATH = os.path.join(os.path.dirname(__file__), "")

parser = argparse.ArgumentParser(description='Fill a Jinja2 template based on json.')

parser.add_argument('prefix', metavar='p', type=str, nargs='?',
                    help='prefix of the file names', default="")

args = parser.parse_args()

templateLoader = jinja2.FileSystemLoader(searchpath=BASE_PATH)
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = args.prefix + "template.txt"
template = templateEnv.get_template(TEMPLATE_FILE)
    
with codecs.open(BASE_PATH + args.prefix + 'source.json', 'r', 'utf-8-sig') as move_file:
    sourcejson = json.load(move_file)

string = template.render(list=sourcejson)

f = open("./" + args.prefix + "wiki.txt", "wb+")
f.write(string.encode('utf-8'))
f.close()

