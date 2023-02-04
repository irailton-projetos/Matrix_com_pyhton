
# CRIAR MATRIX
# -----------------------------

import random

def matrix1(*args):
    matrix = []
    for valor in range(0,3):
        linha = []
        for valor1 in range(0,4):
            linha.append(random.randint(1,9))
        matrix.append(linha)
    
    for l in range(len(matrix)):
        for c in range(len(matrix)):
            print([matrix[l][c]],end='')
        print()
    n = len(matrix)
    assert n == len(matrix)
    print(sum(matrix[i][i] for i in range(n)))

matrix1()

