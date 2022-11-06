import numpy
def cross_product(u, v):
    return numpy.cross(u, v)

print(cross_product([1, 2, 1], [1, 4, 3]))


#or

def cross_prod(a, b):
    result = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

    return result

