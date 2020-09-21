#Course Of Instruction Web Scrapping

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
    course_file = open(course + ".txt", "w", encoding="utf-8")
    course_file.write(text)




class Course:
    def __init__(self,dept,number,desc,hours):
        self.dept = dept
        self.number = number
        self.desc = desc
        self.hours = hours

    #Set new dept
    def setDept(self,dept):
        self.dept = dept

    #Get the department
    def getDept(self):
        return self.dept

    # Set new dept
    def setNumber(self, number):
        self.number = number

    # Get the department
    def getNumber(self):
        return self.number

    # Set new dept
    def setDesc(self, desc):
        self.desc = desc

    # Get the department
    def getDesc(self):
        return self.desc

    # Set new dept
    def setHours(self, hours):
        self.hours = hours

    # Get the department
    def getHours(self):
        return self.hours