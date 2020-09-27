from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata
import re

url = "https://bulletin.miamioh.edu/courses-instruction/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
course_code_list = []
for link in soup.find_all('a'):
    course_code = re.findall(r'[A-Z]{3}', str(link))
    course_code_list.extend(course_code)
# There was one exception of PDF in the list, so I have to omit it
course_code_list = course_code_list[0:len(course_code_list)-1]

for course in course_code_list:
    course_url = "https://bulletin.miamioh.edu/courses-instruction/" + course.casefold() + "/"
    course_page = urlopen(course_url)
    html = course_page.read().decode("utf-8")
    course_soup = BeautifulSoup(html, "html.parser")
    new_str = unicodedata.normalize("NFKD", course_soup.get_text())
    text = "\n".join([ll.rstrip() for ll in new_str.splitlines() if ll.strip()])
print(course_code_list)




