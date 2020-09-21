import re

text_file = open("CPB.txt", "r")
text = text_file.readlines()
course_dict = {}
pre = {}
co = {}
for line in text:
    if line[0:3] == "CPB":
        course_code = line[0:7]
        name = re.search(r"(?<=\.).*(?=\.)", line).group(0)
        credit = re.search(r"(?<=\().*(?=\))", line).group(0)
        course_dict[course_code] = [name.strip(), credit[0]]
    else:
        line_split = line.split(".")
        for i in line_split:
            prereq = re.search(r"(?i)Prerequisite", i)
            coreq = re.search(r"(?i)Co-requisite",i)
            if prereq is not None and coreq is None:
                pre[course_code] = i.strip()
                continue
            if coreq is not None:
                co[course_code] = i.strip()
for i in pre:
    print(i, pre[i])




