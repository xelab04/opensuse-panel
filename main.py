import json
from jinja2 import Template

def get_json(filepath="./opensuse.json"):
    with open(filepath) as f:
        d = json.load(f)
    return d


def main():
    myjson = get_json()

    with open("template.html", 'r') as template_file:
        template = Template(template_file.read())

        # print(myjson["data"])

        output = template.render(data=myjson["data"])

        with open("index.html", 'w+') as outfile:
            outfile.write(output)

main()
