import numpy as np
import math
import solve
import matplotlib.pyplot as plt

size = range(50, 100)

V = []
V2 = []
V3 = []


def M_Gauss(n):
    A = np.random.uniform(0, 10, (n, n))
    b = np.random.uniform(0, 10, (n, 1))
    M = np.hstack((A, b))
    xx = solve(A, b)
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = (M[i, j]) / c
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = M[k, l] - b * M[i, l]
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = M[n - 1, j] / c
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = M[n - 1, n] / M[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + M[k, j] * x[j]
        x[k] = M[k, n] - s
        k = k - 1
    i = 1
    b1 = xx
    b2 = x
    d1 = 0
    for i in range(0, n - 1):
        d1 = d1 + (b1[i] - b2[i]) ** 2
    d = (1 / n) * math.sqrt(d1)
    V.append(d)
    e1 = 6
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e1)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e1)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e1)
    x3 = []
    for i in range(0, n):
        x3.append(0)
    x3[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]), e1)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x3[j])
        x3[k] = round((M[k, n] - s), e1)
        k = k - 1
    i = 1
    b31 = xx
    b32 = x3
    d31 = 0
    for i in range(0, n - 1):
        d31 = d31 + (b31[i] - b32[i]) ** 2
    d3 = (1 / n) * math.sqrt(d31)
    V3.append(d3)
    e = 3
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e)
    x2 = []
    for i in range(0, n):
        x2.append(0)
    x2[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]), e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x2[j])
        x2[k] = round((M[k, n] - s), e)
        k = k - 1
    i = 1
    b21 = xx
    b22 = x2
    d21 = 0
    for i in range(0, n - 1):
        d21 = d21 + (b21[i] - b22[i]) ** 2
    d2 = (1 / n) * math.sqrt(d21)
    V2.append(d2)


for n in size:
    M_Gauss(n)

# отображение результатов
fig, ax = plt.subplots()
plt.plot(size, V, 'r-', label='без округления')
plt.plot(size, V2, 'b-', label='округление до 3')
plt.plot(size, V3, linestyle='-', color='lime', label='округление до 6')
ax.legend()
plt.yscale('log')
plt.grid()
plt.show()