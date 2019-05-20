class DimensionError(Exception):
    pass


def add_matrices(a, b):
    if len(a) != len(b):
        raise DimensionError

    for i in range(len(a)):
        if len(a[i]) != len(b[i]): raise DimensionError

    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j] + b[i][j])

    # return c
    return [[el1 + el2 for (el1, el2) in zip(x, y)] for (x, y) in zip(a, b)]


def add_matrices_dim(a,b):
    if type(a) != list:
        return a + b
    else:
        if len(a) != len(b) : raise DimensionError
        return [add_matrices_dim(x,y) for x,y in zip(a,b)]

def sub_matrices_dim(a, b):
    if type(a) != list:
        return a - b
    else:
        if len(a) != len(b): raise DimensionError
        return [sub_matrices_dim(x, y) for x, y in zip(a, b)]
