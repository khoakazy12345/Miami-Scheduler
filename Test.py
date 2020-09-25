fin_list = [[]]
 i = 0
  while len(origin) > 0:
       if re.search(r"[A-Z]{3}", origin[i]) is not None:
            fin_list[i].append(" ". join(origin[0:2]))
            origin.pop(0)
            origin.pop(0)
        elif origin[i] == "or":
            origin.pop(0)
        elif origin[i] == "and":
            origin.pop(0)
            fin_list.append([])
            i = i + 1
    #print(fin_list)
