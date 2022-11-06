def add_vectors(u, v):
    return list(map(sum,zip(u,v)))
    
print(add_vectors([1, 1], [1, 1]))
print(add_vectors([1, 2], [1, 4]))
print(add_vectors([1, 2, 1], [1, 4, 3]))
