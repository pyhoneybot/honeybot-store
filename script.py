

from storeapi.jinja2 import render
from storeapi.files import new_file

from plugins_info import get_plugins_info

context = {}

infos = get_plugins_info()
context['infos'] = infos
context['NUM_PLUGINS'] = len(infos)
# context['message'] = 'abcd'
text = render('index/index.html', **context)

# print(text)

new_file('docs/index.html', text)



