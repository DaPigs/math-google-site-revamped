import json
from flask import Flask, request

f = open("urls.json", "r")
urls = json.load(f)
f.close()

def get_dic(dictionary, items):
    if(items == [""]):
        return dictionary
    if(len(items) == 1):
        return dictionary[items[0]]
    return get_dic(dictionary[items[0]], items[1:])

def new_dict_to_html(dictionary, current_route=""):
    html = "<ul>"
    for key, value in dictionary.items():
        html += "<li>"
        route = f"{current_route}/{key}" if current_route else key
        if isinstance(value, dict):
            html += f"<a href='{request.host_url}/{route}'>{key}</a>"
            if current_route.startswith(route):
                html += new_dict_to_html(value, current_route)
        else:
            html += f"<a target='_blank' href='{value}'>{key}</a>"
        html += "</li>"
    html += "</ul>"
    return html

def dict_to_html(dictionary, current_route=""):
    html = "<ul>"
    for key, value in dictionary.items():
        html += "<li>"
        if isinstance(value, dict):
            html += f"<a href='{current_route}/{key}'>{key}</a>" if current_route else f"<a href='{key}'>{key}</a>"
            html += dict_to_html(value, f"{current_route}/{key}")
        else:
            html += f"<a target='_blank' href='{value}'>{key}</a>"
        html += "</li>"
    html += "</ul>"
    return html

app = Flask(__name__)

@app.route('/favicon.ico/')
def useless():
    return ""

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if(path.endswith("/")):
        path = path[:-1]
    path1 = path.split("/")
    update = "" if path else "<h1>Updated 26th July 2023</h1><br><br>"
    return update + new_dict_to_html(get_dic(urls, path1), "/"+path) + "<br><br>" +  dict_to_html(get_dic(urls, path1), path)
app.run()