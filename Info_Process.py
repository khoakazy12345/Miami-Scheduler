import re
text_file = open("Sample_Data.txt")
text = text_file.readlines()
for line in text:
    line = line.split()
    line = " ".join(line[1:])
    origin = re.sub(r"[,;]"," and ",line)
    origin = origin.split()
    origin_copy = list(origin)
    for string in origin_copy:
        if (re.search(r"^.?and.?$|^.?or.?$|[A-Z]{3}|[0-9]{3}", string) is None):
            origin.remove(string)
    reverse_origin = origin[::-1]
    for string in reverse_origin:
        if (re.search(r"and|or", string)) is not None:
            origin = origin[:-1]
        else:
            break
    origin_copy = list(origin)
    for order in range(len(origin_copy)-1,-1,-1):
        if re.search(r"[5-9]{1}[0-9]{2}", origin_copy[order]) is not None:
            origin.pop(order)
    for order in range (len(origin)):
        origin[order] = re.sub(r"\(|\)", "", origin[order])
        if re.search(r"/", origin[order]) is not None:
            origin[order] = origin[order][:3]
    print(origin)
    print(origin)
