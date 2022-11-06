def dot_product(u, v):
    func = lambda u,v : u*v
    iters_by_func =list(map(func, u, v))
    return sum(iters_by_func)
    

print(dot_product([1, 2], [1, 4]))

print(dot_product([1, 2, 1], [1, 4, 3]))