import re
text_file = open("Sample_Data.txt")
text = text_file.readlines()
for line in text:
    line = line.split()
    line = " ".join(line[1:])
    origin = re.sub(r"[,;]"," and ",line)
    origin = origin.split()
    origin_copy = list(origin)
    for i in list(origin):
        if (re.search(r"^.?and.?$|^.?or.?$|[A-Z]{3}|[0-9]{3}", i) is None):
            origin.remove(i)
    print(" ".join(origin))