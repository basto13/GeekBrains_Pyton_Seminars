# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# a = 0.56
# s = str(a).replace('.', '')
# sum = 0
# for i in s:
#     sum += int(i)
# print('sum is ', sum)

# Improvements of previous homework
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def sum(number, sum):
#     return sum + number

# a = 0.56
# s = str(a).replace('.', '')
# s = list(lambda x: x in s)
# total = 0
# total = map(sum, s)
# print(type(total))
# print('total is ', total)

# c = float(input("Insert a number: "))
# lst = sum(map(int, str(c).replace(".", "").replace("-", "")))
# print(lst)

# print(sum(map(int, (filter(str.isdigit, input("Insert the number: "))))))


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# multList = []
# n = 4
# mult = 1
# for i in range(1, n + 1):
#     mult = mult * i
#     multList.append(mult)
# print(multList)

# # 3. Задайте список из n чисел последовательности (1+\frac 1 n)^n и выведите на экран их сумму.
# # (1+ 1/n)^n
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = 3
# d = {i : ((1+1/i)**i) for i in range(1, n + 1)}
# print("list of results: {}" .format(d))
# values = d.values()
# print(values)
# sum = 1
# for e in values:
#     sum *= e
# print("sum is {}" .format(sum))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# n = 4
# createdNumbers = list(range(-n, n + 1))
# positions = []
# multList = []

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     positions.append(int(line))
# data.close()

# mult = 1
# for element in positions:
#     mult = mult * createdNumbers[element]

# print(createdNumbers)
# print('List is', positions)
# print("Mult", mult)


# # 5. Реализуйте алгоритм перемешивания списка

# import random
# a = ['winter', 'spring', 'summer', 'autumn']
# random.shuffle(a)
# print(a)