import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
pre_rel_path = r"\Prereq\\" + "MTH" + ".txt"
pre_file_path = script_dir + pre_rel_path
pre_file = open(pre_file_path, "r", encoding="utf8")
text = pre_file.readlines()
for line in text:
    line = line.split()
    line = " ".join(line[1:])
    origin = re.sub(r"[,;]", " and ", line)
    origin = origin.split()
    origin_copy = list(origin)
    print(" ".join(origin))
    # Remove any unnecessary strings
    for string in origin_copy:
        if (re.search(r"^.?and.?$|^.?or.?$|[A-Z]{3}|[0-9]{3}", string) is None
                or re.search(r"SAT|ACT", string) is not None):
            origin.remove(string)
    # get rid of graduate courses
    origin_copy = list(origin)
    for order in range(len(origin_copy)-1, -1, -1):
        if re.search(r"[5-9]{1}[0-9]{2}", origin_copy[order]) is not None:
            origin.pop(order)
    # get rid of / symbol and trimming down course code + course number
    for order in range(len(origin)):
        origin[order] = re.sub(r"\(|\)", "", origin[order])
        if re.search(r"/", origin[order]) is not None:
            origin[order] = origin[order][:3]
    # trim down stupid strings in the beginning
    for string in origin:
        if (re.match(r"^[A-Z]{3}", string)) is None:
            origin = origin[1:]
        else:
            break
    # trim down stupid things at the end
    origin_copy = list(origin)
    for order in range(len(origin_copy)-1, -1, -1):
        if re.search(r"[0-9]{3}", origin[order]) is None:
            origin.pop()
        else:
            break
    # trimming down excess "and" and "or" terms
    i = 0
    while i < len(origin):
        # Remember the course code
        if re.search(r"[A-Z]{3}", origin[i]) is not None:
            code = origin[i]
        if ((re.search(r"[0-9]{3}", origin[i]) is not None) and (re.search(r"[A-Z]{3}", origin[i-1]) is None)):
            origin.insert(i, code)
            i = i + 1
        elif re.search(r"[A-Z]{3}|[0-9]{3}", origin[i]) is not None:
            i = i + 1
        elif ((origin[i] == "or" or origin[i] == "and") and i == len(origin)-1):
            origin.pop(i)
        elif origin[i] == "or" and re.search(r"[A-Z]{3}|[0-9]{3}", origin[i+1]) is None:
            origin.pop(i)
        elif origin[i] == "and" and re.search(r"[A-Z]{3}|[0-9]{3}", origin[i+1]) is None:
            origin.pop(i)
        else:
            i = i + 1
    print(origin)
    fin_list = [[]]
    i = 0
    while len(origin) > 0:
        if re.search(r"[A-Z]{3}", origin[0]) is not None:
            fin_list[i].append(" ". join(origin[0:2]))
            origin.pop(0)
            origin.pop(0)
        elif origin[0] == "or":
            origin.pop(0)
        elif origin[0] == "and":
            origin.pop(0)
            fin_list.append([])
            i = i + 1
