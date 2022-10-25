from test import test


def turn_clockwise(compass_points):
    l =['N', 'E', 'S', 'W']
    for i in l:
        index = l.index(i)
        if str(compass_points).upper() == i:
            return l[index+1]
        else:
            return 'N'
        


#print(turn_clockwise('w'))
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)