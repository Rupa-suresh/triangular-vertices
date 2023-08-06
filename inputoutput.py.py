import sys
def row_col(point):
    row_no = 1
    head = 1
    while point >= head + row_no:
        head += row_no
        row_no += 1
    col_no=point-head
    return row_no, col_no

def result(points,is_valid):
    length = len(points)
    if is_valid:
        if length == 3:
           return " ".join(list(map(str,points)))+" are the vertices of triangle"
        elif length == 4:
           return " ".join(list(map(str,points)))+" are the vertices of parallelogram"
        elif length == 6:
           return  " ".join(list(map(str,points)))+" are the vertices of hexagon"
    else:
        return " ".join(list(map(str,points)))+" are not vertices of any acceptable figure"         

points = [sys.argv[i] for i in range(1,len(sys.argv))]
points = list(map(int, points))
points.sort()
is_valid = len(points) == 3 and triangle(points) or len(points) == 4 and parallelogram(points) or len(points) == 6 and hexagon(points)
print(result(points,is_valid))
