import os
import sys
import importlib
import ast
from collections import OrderedDict

BASE_DIR = '../honeybot/honeybot/plugins'
import ast

def pyfiles(folder):
    return [f for f in os.listdir(folder) 
                if f.endswith('.py') and not f.startswith('__')]



def strip_square(string):
    return string.strip().strip('[').strip(']')

def last_key(od):
    return next(reversed(od.keys()))

def parse_dstring(docstring):
    section_flag = 0

    docs = docstring.strip()
    all_info = OrderedDict()

    for line in docs.split('\n'):
        if line.strip() == '' and last_key(all_info) != 'commands':
            section_flag = 0

        if line.strip().startswith('['):
            section_flag = 1

            section_name = line.strip().strip('[').strip(']')
            if '.py' in section_name:
                all_info['name'] = [section_name.lower()]
                all_info['description'] = []
            else:
                all_info[section_name.lower()] = []
        else:
            if section_flag:
                all_info[last_key(all_info)].append(line.strip())
        

    return all_info


x = """
[bitcoin.py]
Bitcoin Price Checking Plugin

[Author]
Gabriele Ron

[Website]
https://Macr0Nerd.github.io

[About]
Checks the current price for Bitcoin through the Legacy Coin Market Cap API
TODO: Update API to new Coin Market Cap API

[Commands]
>>> .btc
returns current value of bitcoin

>>> .btf
returns current value of bitcoinf
"""

# print(parse_dstring(x))



BASE_DIR = '../honeybot/honeybot/plugins'

def get_plugins_info():
    plugin_dicts = []

    files = pyfiles(BASE_DIR)
    # print(files)
    
    print(len(files))
    for i, file in enumerate(files):
        print('running on', file)
        with open('{}{}{}'.format(BASE_DIR, os.sep, file)) as f:
            try:
                tree = ast.parse(f.read())
                docstring = ast.get_docstring(tree)
                plugin_dicts.append(parse_dstring(docstring))
            except StopIteration as e:
                print(e)
            except UnicodeDecodeError as e:
                print(e)
            
            #if i == 0:
            #    break
    

    return plugin_dicts




