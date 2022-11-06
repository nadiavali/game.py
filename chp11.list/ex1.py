list(range(0, 10, -2))

def rule(start, stop, step):
    if start < stop and step < 0:
        return 'it is not working'
    else:
        return list(range(start, stop, step))

print(rule(0, 10, 2))