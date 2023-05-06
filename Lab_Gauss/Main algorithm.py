import math
import numpy as np
import solve
import matplotlib.pyplot as plt

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

# обратный ход
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

def gauss(a):
    # указываем точность решения
    eps = 1e-16
    # создаем 2 копии массива, они нам понадобятся дальше
    matrix1 = np.array(a)
    matrix2 = np.array(a)
    # len1 - хранит в себе количество строк, len 2 - количество столбцов
    len1 = len(a[:, 0])
    len2 = len(a[0, :])
    # запускаем глобальный цикл проходящийся по строкам для вычисления системы
    for i in range(len1):
        # max - переменная хранящая максимальный элемент столбца
        max = abs(a[i][i])
        firstIndex = i
        secondIndex = i
        # цикл поиска максимального элемента в столбце
        while secondIndex < len1:
            if abs(a[secondIndex][i]) > max:
                # в max - лежит наибольший элемент
                max = abs(a[secondIndex][i])
                firstIndex = secondIndex
            secondIndex += 1
        # коэффициент перед текущим x на диагонали
        coeff = float(a[i][i])
        z = i
        # делим всю строку на коэффициент x, x становиться равный 1
        while z < len2:
            a[i][z] = a[i][z] / coeff
            z += 1
        j = i + 1
        # отнимаем строку, умноженую на коэффициент от следующей,
        # в результате получаем столбец нулей.
        # глобальный цикл выполняется до тех пор пока не получим матрицу прямого хода
        while j < len1:
            b = a[j][i]
            z = i
            while z < len2:
                a[j][z] = a[j][z] - a[i][z] * b
                z += 1
            j += 1
    # массив хранящий в себе матрицу прямого хода
    matrix = backTrace(a, len1)
    return [a, matrix]

def info1():
    print("Исходная система: \n", sourceMatrix)
    print("Левая часть системы: \n", sourceMatrixA)
    print("Правая часть системы: \n", sourceMatrixB)
    print("Система прямого хода: \n", gauss(sourceMatrix)[0])
    print("Решение системы своим методом: \n", gauss(sourceMatrix)[1])
    print("Решение системы встроенным методом: \n", np.linalg.solve(sourceMatrixA, sourceMatrixB))

info1()

