

def new_file(filename, content):
    with open(filename, 'w+') as f:
        f.write(content)
    print('Created at', filename)
