#Course Of Instruction Web Scrapping

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url = "https://bulletin.miamioh.edu/courses-instruction/cpb"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
course_code_list = []
for link in soup.find_all('a'):
    course_code = re.findall(r'[A-Z]{3}', str(link))
    course_code_list.extend(course_code)
# There was one exception of PDF in the list, so I have to omit it
course_code_list = course_code_list[0:len(course_code_list)-1]
print(course_code_list)



