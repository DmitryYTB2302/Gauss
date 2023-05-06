import math
import numpy as np

# исходная система
sourceMatrix = np.array([[1.53, 1.61, 1.43, -5.13],
                        [2.35, 2.31, 2.07, -3.69],
                        [3.83, 3.73, 3.45, -5.98]])

# левая часть системы
sourceMatrixA = np.array([[1.53, 1.61, 1.43],
                          [2.35, 2.31, 2.07],
                          [3.83, 3.73, 3.45]])

# правая часть системы
sourceMatrixB = np.array([[-5.13],
                          [-3.69],
                          [-5.98]])

def gauss(a):
    n = len(a)
    for i in range (0, n):
       m = i
       for k in range (i + 1, n):
           if (math.fabs(a[k, i]) > math.fabs(a[m, i])):
               m = k
       for j in range(i, n + 1):
           z = a[i, j]
           a[i, j] = a[m, j]
           a[m, j] = z
       c = a[i, i]
       for j in range(i, n + 1):
           a[i, j] = (a[i, j]) / c
       for k in range(i + 1, n):
           b = a[k, i]
           for l in range(i, n + 1):
               a[k, l] = a[k, l] - b * a[i, l]
    c = a[n - 1, n - 1]
    for j in range(n - 1, n):
        a[n - 1, j] = a[n - 1, j] / c
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = a[n - 1, n] / a[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + a[k,j] * x[j]
        x[k] = a[k, n] - s
        k = k - 1
    return x

def straightGauss(a):
    n = len(a)
    for i in range (0, n):
       m = i
       for k in range (i + 1, n):
           if (math.fabs(a[k, i]) > math.fabs(a[m, i])):
               m = k
       for j in range(i, n + 1):
           z = a[i, j]
           a[i, j] = a[m, j]
           a[m, j] = z
       c = a[i, i]
       for j in range(i, n + 1):
           a[i, j] = (a[i, j]) / c
       for k in range(i + 1, n):
           b = a[k, i]
           for l in range(i, n + 1):
               a[k, l] = a[k, l] - b * a[i, l]
    c = a[n - 1, n - 1]
    for j in range(n - 1, n):
        a[n - 1, j] = a[n - 1, j] / c
    return a

def info():
    a = gauss(sourceMatrix)
    b = straightGauss(sourceMatrix)
    x = np.zeros(3)
    x[2] = np.round(b[2][3], 3) # -8.33
    x[1] = np.round(b[1][3], 3) - np.round(b[1][2], 3)*x[2] # -19.253
    x[0] = np.round(b[0][3], 3) - np.round(b[0][2], 3) * x[1] - np.round(b[0][1], 3) * x[2] # 23.861
    x = np.round(a, 2) - np.round(x, 2)
    res = np.round(np.sqrt((sum(x ** 2))) / 3, 3)
    return res

print("Невязка посчитанная в ручную: ", info())