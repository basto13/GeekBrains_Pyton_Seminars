# # 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst

# line = 'C:\WINDOWS\System32\drivers\etc\\nst'
# print(line)
# print(r'C:\WINDOWS\System32\drivers\etc\nst')


# # 2. a = [4, 3, -10, 1, 7, 12] 
# a = [4, 3, -10, 1, 7, 12]
# b = a.sort(key = lambda x: x % 2)
# print(a)

# 3)На вход программы поступает список наименований рек, записанных в одну строчку через пробел. 
# Необходимо отсортировать этот список в порядке убывания длин названий. 
# Результат вывести в одну строчку через пробел.

# rivers_string = 'Volga Neva Oka Lena'
# rivers_list = rivers_string.split(' ')
# print(rivers_list)
# rivers_list.sort(key = lambda x: len(x))
# print(rivers_list)


# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

result = sum(map(lambda x: x ** 2, filter(lambda x: not x % 9, range(0, 100))))
print(result)

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)