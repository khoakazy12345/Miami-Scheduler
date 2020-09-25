import re
text_file = open("Sample_Data.txt")
text = text_file.readlines()
for line in text:
    line = line.split()
    line = " ".join(line[1:])
    origin = re.sub(r"[,;]", " and ", line)
    origin = origin.split()
    origin_copy = list(origin)
    # Remove any unnecessary strings
    for string in origin_copy:
        if (re.search(r"^.?and.?$|^.?or.?$|[A-Z]{3}|[0-9]{3}", string) is None):
            origin.remove(string)
    origin_copy = list(origin)
    # get rid of graduate courses
    for order in range(len(origin_copy)-1, -1, -1):
        if re.search(r"[5-9]{1}[0-9]{2}", origin_copy[order]) is not None:
            origin.pop(order)
    # get rid of / symbol and trimming down course code + course number
    for order in range(len(origin)):
        origin[order] = re.sub(r"\(|\)", "", origin[order])
        if re.search(r"/", origin[order]) is not None:
            origin[order] = origin[order][:3]
    # trimming down excess "and" and "or" terms
    i = 0
    while i < len(origin):
        if (origin[i-1] == "or" or origin[i-1] == "and") and (re.search(r"[0-9]{3}", origin[i]) is not None):
            origin.insert(i, "CPB")
            i = i + 1
            continue
        if re.search(r"[A-Z]{3}|[0-9]{3}", origin[i]) is not None:
            i = i + 1
        elif ((origin[i] == "or" or origin[i] == "and") and i == len(origin)-1):
            origin.pop(i)
        elif origin[i] == "or" and re.search(r"[A-Z]{3}|[0-9]{3}", origin[i+1]) is None:
            origin.pop(i)
        elif origin[i] == "and" and re.search(r"[A-Z]{3}|[0-9]{3}", origin[i+1]) is None:
            origin.pop(i)
        else:
            i = i + 1
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
    print(fin_list)
