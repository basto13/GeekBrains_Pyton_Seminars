# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23

# lst = [- 8, 11, 0, -23, 140, 1]
# print(type(lst[0]))

# resultedList = list(filter(lambda x: 9 < x < 100 or -100 < x < -9, lst))
# result = ' '.join(map(str, resultedList))
# print(result)

# 2. Дан список, вывести отдельно буквы и цифры.

# a = ( "a", 'b', '2', '3' ,'c')
# # b = ( 'a' , 'b' , 'c')
# # c = ( '2', '3')

# example = 'b'
# ex2 = '3'

# b = ' '.join(str(x) for x in a if x.isdigit())
# print('numbers ', b)
# c = ' '.join(str(x) for x in a if not x.isdigit())
# print('letters', c)


# 3. Преобразовать набора списков users = ['user1','user2','user3','user4','user5'] ids = [4, 5, 9, 14, 7] salary = [111,222,333] в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]

# users = ['user1','user2','user3','user4','user5'] 
# ids = [4, 5, 9, 14, 7] 
# salary = [111,222,333]

# # 1st solution

# all_data = list(zip(users, ids, salary))
# print('1st solution', all_data)
# for element in all_data:
#     el = list(element)
#     print(el)

# # 2d solution

# result = list(map(list, zip(users, ids, salary)))
# print('2d solution', result)
# for e in result:
#     print(e)


# # 3.1 и потом вернуть в исходное состояние

# reversedList = []
# a = []
# b = []
# c = []
# for i in all_data:
#     a.append(i[0])
#     b.append(i[1])
#     c.append(i[2])
# reversedList.append(list(a))
# reversedList.append(list(b))
# reversedList.append(list(c))
# print('reversed list is ', reversedList)

# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]
