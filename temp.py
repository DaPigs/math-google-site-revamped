import modules
modules.make_application("main.py")

# import modules
# urls = []
# html = modules.HTML(modules.read_file("dropdown.html"))
# for i in html.find_elements_by_xpath(modules.xpath.tag("li")):
#     for a in i.find_elements_by_xpath(modules.xpath.tag("a")):
#         url = a.get_attribute("href")
#         display = True
#         for x in ["home", "videos"]:
#             if(x in url):
#                 display = False
#                 break
#         if(display):
#             print(url)
#             urls.append(url)
# print(urls)