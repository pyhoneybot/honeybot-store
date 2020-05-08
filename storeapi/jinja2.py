from jinja2 import Environment, FileSystemLoader


def render(file_name, templates='templates', **kwargs):
    file_loader = FileSystemLoader(templates)
    env = Environment(loader=file_loader)
    template = env.get_template(file_name)
    output = template.render(kwargs)
    return output