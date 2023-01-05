# Урок 3. Данные, функции и модули в Python
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

a = [2, 3, 5, 9, 3]
# sum = 0
# for idx, x in enumerate(a):
#     if idx % 2:
#         sum += x
# print(sum)

print(sum([i for i in a if i % 2 == 0]))


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# b = [2, 3, 4, 5, 6]
# sumList = []
# i = 0
# length = len(b)
# while i < round(length / 2 + 0.5):
#     sumList.append(b[i] * b[length - 1 - i])
#     i += 1
# print(sumList)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# numbers = list(map(float, input("Insert the numbers separated by spaces:\n").split()))
# resultedList = [round(i%1,2) for i in numbers if i%1 != 0]
# print(max(resultedList) - min(resultedList))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input())
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# positiveFibList = []
# def fib(n, is_positive):
#     if n in {0, 1}:
#         return n
#     if is_positive:
#         return fib(n - 2, is_positive) + fib(n - 1, is_positive)
#     else:
#         return fib(n - 2, is_positive) - fib(n - 1, is_positive)

# positiveFibList = [fib(n, True) for n in range(10)]
# print('positive list ', positiveFibList)
# negativeFibList = [fib(n, False) for n in range(10)]
# print('negative list ', negativeFibList)

# negativeFibList.pop(0)
# negativeFibList.reverse()
# negativeFibList.extend(positiveFibList)
# print('result is ', negativeFibList)
