import modules
urls = []
html = modules.HTML(modules.read_file("dropdown.html"))
for i in html.find_elements_by_xpath(modules.xpath.tag("li")):
    for a in i.find_elements_by_xpath(modules.xpath.tag("a")):
        url = a.get_attribute("href")
        display = True
        for x in ["home", "videos"]:
            if(x in url):
                display = False
                break
        if(display):
            print(url)
            urls.append(url)

import json, time
driver = modules.Driver()
driver.get("https://sites.google.com/hci.edu.sg/22-23-h2-math/")
#remember to switch to mobile view and refresh
input("Ready?")

def write_dic(dictionary, items, data):
    if(len(items) == 1):
        dictionary[items[0]] = data
        return dictionary
    elif(items[0] not in dictionary):
        dictionary[items[0]] = write_dic({}, items[1:], data)
        return dictionary
    elif(items[0] in dictionary):
        dictionary[items[0]] = write_dic(dictionary[items[0]], items[1:], data)
        return dictionary
S = modules.read_file("html.html")
f = open("urls.json", "r")
dic = json.load(f)
f.close()
dic = {}
for i in urls:
    driver.get("https://sites.google.com"+i)
    time.sleep(2)
    dics = i.replace("?authuser=1", "").replace("/hci.edu.sg/22-23-h2-math/", "").split("/")
    if(len(dics) == 1):
        continue
    html = modules.HTML(driver.page_source)
    for i in html.find_elements_by_xpath(modules.xpath.tag("iframe")):
        name, url = i.get_attribute("aria-label").replace("Drive, ", ""), i.get_attribute("src").replace("/preview?authuser=1", "")
        print(name, url)
        dic = write_dic(dic, dics+[name], url)
f = open("urls.json", "w")
json.dump(dic, f)
f.close()