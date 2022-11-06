def scalar_m(s, v):
    func = lambda num : num * s
    v_by_func = map(func, v)
    return list(v_by_func)

print(scalar_m(2,[2,1,-1]))