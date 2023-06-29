import modules, json, time
driver = modules.Driver()
driver.get("https://sites.google.com/hci.edu.sg/22-23-h2-math/")
input("Ready?")
urls = ['/hci.edu.sg/22-23-h2-math/chapter-resources?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/pure-math?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/statistics?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/h2-foundation-mathematics?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/pure-math?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/statistics?authuser=1', '/hci.edu.sg/22-23-h2-math/chapter-resources/h2-foundation-mathematics?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-bt-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-promo-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-dec-holidays-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-revision-package-1?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-revision-package-2?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-tpe-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-bt-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-promo-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2022-c1-dec-holidays-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-revision-package-1?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-revision-package-2?authuser=1', '/hci.edu.sg/22-23-h2-math/revision-packages/2023-c2-tpe-revision-package?authuser=1', '/hci.edu.sg/22-23-h2-math/tests-exams?authuser=1', '/hci.edu.sg/22-23-h2-math/tests-exams/c2-tests-exams?authuser=1', '/hci.edu.sg/22-23-h2-math/tests-exams/c1-tests-exams?authuser=1', '/hci.edu.sg/22-23-h2-math/tests-exams/c2-tests-exams?authuser=1', '/hci.edu.sg/22-23-h2-math/tests-exams/c1-tests-exams?authuser=1', '/hci.edu.sg/22-23-h2-math/study-sessions?authuser=1', '/hci.edu.sg/22-23-h2-math/study-sessions/2023-term-1-2-mss?authuser=1', '/hci.edu.sg/22-23-h2-math/study-sessions/2022-term-3-4-mss?authuser=1', '/hci.edu.sg/22-23-h2-math/study-sessions/2023-term-1-2-mss?authuser=1', '/hci.edu.sg/22-23-h2-math/study-sessions/2022-term-3-4-mss?authuser=1']

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