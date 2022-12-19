print("hello world")

a = [1, 2, 3, 5, 8, 15, 23, 38]

#  result = [(2, 4), (8, 64), (38, 1444)]

mult = lambda x: x**2

result = [(i, mult(i)) for i in a if i % 2 == 0] 
print(result)