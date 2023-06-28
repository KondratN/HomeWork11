# 12.5(б) Дан двумерный массив. Вывести на экран:
# все элементы s-го столбца массива.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def someElement(matrix, num):
#     for i in range(len(matrix)):
#         print(matrix[i][num], end='\n')
#     print()
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# num3 = int(input("Введите номер столбца для вывода: "))
# someElement(someMatrix, num3 - 1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.6(б) Дан двумерный массив. Вывести на экран:
# все элементы m-й строки массива.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def someElement(matrix, num):
#     for i in range(len(matrix)):
#         print(matrix[num][i], end=' ')
#     print()
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# num3 = int(input("Введите номер строки для вывода: "))
# someElement(someMatrix, num3 - 1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.16(а) Составить программу:
# расчета разности двух любых элементов двумерного массива.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def diferenceElement(matrix):
#     someMatr = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             someMatr.append(matrix[i][j])
#     firstNum = someMatr[random.randint(0, len(someMatr) - 1)]
#     secondNum = someMatr[random.randint(0, len(someMatr) - 1)]
#     print('Первое случайное число:', firstNum)
#     print('Второе случайное число:', secondNum)
#     print('Разность = ', firstNum - secondNum)
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# diferenceElement(someMatrix)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.33(а) Дан двумерный массив. Вывести на экран:
# все элементы пятого столбца массива, начиная с последнего элемента этого столбца.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def someElement(matrix):
#     index = len(matrix) - 1
#     while index >= 0:
#         print(matrix[index][len(matrix[index]) - 1], end='\n')
#         index -= 1
#     print()
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# someElement(someMatrix)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.62(а) Дан двумерный массив. Найти:
# сумму элементов каждой строки.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def someElementSum(matrix):
#     summa = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             summa += matrix[i][j]
#         print(f'Сумма {i+1} строки =',summa, end='\n')
#         summa = 0
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# someElementSum(someMatrix)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.90(а) Дан двумерный массив. В каждой его строке найти:
# максимальный элемент.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def maxElement(matrix):
#     someMatr = []
#     for i in range(len(matrix)):
#         someMatr.append(max(matrix[i]))
#     print(someMatr)
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# maxElement(someMatrix)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 12.90(б) Дан двумерный массив. В каждой его строке найти:
# минимальный элемент.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random
#
#
# def minElement(matrix):
#     someMatr = []
#     for i in range(len(matrix)):
#         someMatr.append(min(matrix[i]))
#     print(someMatr)
#
#
# def normalView(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
#
#
# num1 = int(input("Введите количество строк: "))
# num2 = int(input("Введите количество столбцов: "))
# someMatrix = [[]] * num1
# for i in range(num1):
#     someMatrix[i] = [0] * num2
# for i in range(num1):
#     for j in range(num2):
#         someMatrix[i][j] = random.randint(0, 100)
#
# normalView(someMatrix)
# minElement(someMatrix)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
