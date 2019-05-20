from mathematica.algebra.matrices import add_matrices, add_matrices_dim


def test_add_matrices():
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    b = [[1,1,1],
         [0,0,0],
         [2,2,2]]

    c = [[2,3,4],
         [4,5,6],
         [9,10,11]]

    assert add_matrices(a,b) == c

def test_add_matrices2():
    a = [[1,2,3],
         [4,5,6]]

    b = [[1,1,1],
         [0,0,0]]

    c = [[2,3,4],
         [4,5,6]]

    assert add_matrices(a,b) == c

def test_3_wymiary():
    a = [[[1, 2, 3], [2, 3, 4]], [[2, 2, 2], [3, 3, 3]]]
    b = [[[1, 1, 1], [0, 0, 0]], [[2, 2, 2], [4, 4, 4]]]
    c = [[[2, 3, 4], [2, 3, 4]], [[4, 4, 4], [7, 7, 7]]]

    assert add_matrices_dim(a,b) == c
