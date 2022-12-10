# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Insert number of week day:')
a = int(input())
if (a==6 or a==7):
    print("This is a weekend")
else: 
    print("This is a working day")

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

print('Define X is True or False')
x = input()
print('Define Y is True or False')
y = input()
print('Define Z is True or False')
z = input()

def verifyStatement(x,y,z):
    if (not (x or y or z)) == (not x and not y and not z):
        print ('True')

verifyStatement(x,y,z)

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("insert x coordinate:")
x = int(input())
print("insert y coordinate:")
y = int(input())

def findCoordinates(x, y):
    quarter = 1
    if x > 0 and y < 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    elif x < 0 and y > 0:
        quarter = 4
    print(quarter)

findCoordinates(x,y)

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print("insert number of quarter:")
quarter = int(input())

def findQuarter(quarter):
    if quarter == 1:
        print("range is x > 0, y > 0 for 1 quarter")
    elif quarter == 2:
        print("range is x > 0 and y < 0 for 2 quarter")
    elif quarter == 3:
        print("range is x < 0 and y < 0 for 3 quarter")
    else:
        print("range is x < 0 and y > 0 for 4 quarter") 

findQuarter(quarter)

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def setCoordinates():
    coordinates = []
    for i in range(2):
        try:
            print("set coordinate")
            number = int(input())
            coordinates.append(number)
        except ValueError:
            print("Try to insert an integer")
    return coordinates

def findDistance(a, b):
    distance = round(((b[0] - a[0]) **2 + (b[1] - a[1]) ** 2) ** 0.5, 2)
    return distance

print("insert coordinates of A")
pointA = setCoordinates()
print("insert coordinates of B")
pointB = setCoordinates()

print ('distance is: {}' .format(findDistance(pointA, pointB)))


