import os
import urllib.request
from urllib.request import *
import shutil
import json

BASE_PATH = os.path.join(os.path.dirname(__file__), "./")

if not os.path.exists('images'):
    os.makedirs('images')
    
def get_image(number, filename=None):
    if filename is None:
        filename = number
        
    if not os.path.isfile(BASE_PATH + "/images/" + filename +".png"):
        url = "http://assets.pokemon.com/assets/cms2/img/pokedex/full/"+number+".png"
        with urllib.request.urlopen(Request(url, headers={'User-Agent': 'Mozilla'})) as response, open(BASE_PATH + "/images/" + filename +".png", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

with open(BASE_PATH + 'pokemon numbers.json', encoding='utf-8') as data_file:
    data = json.load(data_file)
    for number in range(1, data["number"]+1):
        get_image(str(number).zfill(3))
    
    for number in data["alternate forms"].keys():
        get_image(data["alternate forms"][number], number)
    
