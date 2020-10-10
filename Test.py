count = 1
points = [[0,6],[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[2,8]]
#points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[0,6],[3,9],[2,8]]
if points is None:
    print (0)
check = [points[0]]
for i in range (1, len(points)):
    for a in range (len(check)):
        start1 = points[i][0]
        end1 = points[i][1]
        start2 = check[a][0]
        end2 = check[a][1]
        start = max(start1, start2)
        end = min(end1, end2)
        if end >= start:
            check[a] = [start, end]
            break
        if (a == len(check)-1):
            check.append(points[i])
            count = count + 1


print(check)
print(count)