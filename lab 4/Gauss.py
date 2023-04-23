import math
import numpy as np
import matplotlib.pyplot as plt
import solve

# исходная матрица
matr = np.array([[1.53, 1.61, 1.43, -5.13],
                 [2.35, 2.31, 2.07, -3.69],
                 [3.83, 3.73, 3.45, -5.98]])

# левая матрица
matrA = np.array([[1.53, 1.61, 1.43], [2.35, 2.31, 2.07], [3.83, 3.73, 3.45]])
# правая часть матрицы с коффициетнмаи
matrB = np.array([[-5.13], [-3.69], [-5.98]])

# метод Гаусса
def gauss(a):
    eps = 1e-16
    c = np.array(a)
    a = np.array(a)
    len1 = len(a[:, 0])
    len2 = len(a[0, :])
    for g in range(len1):
        max = abs(a[g][g])
        my = g
        t1 = g
        while t1 < len1:
            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1
        amain = float(a[g][g])
        z = g
        while z < len2:
            a[g][z] = a[g][z] / amain
            z += 1
        j = g + 1
        while j < len1:
            b = a[j][g]
            z = g
            while z < len2:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1
    a = backTrace(a, len1)
    return a

#обратный ход
def backTrace(a, len1):
    a = np.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]

# тестирование своим методом
print(gauss(matr))

# тестирование встроенным методом
print(np.linalg.solve(matrA, matrB))