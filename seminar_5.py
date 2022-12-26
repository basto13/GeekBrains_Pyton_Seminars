
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""abc"".

# text = ('History about abc. A and B are included in abc')
# print('Initial text: {}'. format(text))

# # 11111111111 1st colution 

# lst = [i for i in text.split() if 'abc' not in i]
# result = ' '.join(str(x) for x in lst)
# print('Resulted text: {}'. format(result))

# # !!!!!!!! 2d solution

# result = text.split()
# result = filter(lambda x: 'abc' not in x, result)
# print(*result)



# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 100 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

# P2P

# sweets_amount = 100
# turn = random.randint(1, 2)
# print("The player {} turn". format(turn))
# player1 = 1
# player2 = 2

# def moveInfo(turn, quantity, sweets_amount):
#     print('turn', turn)
#     print("Player {} made a move, he took {}. {} sweets is left.".format(turn, quantity, sweets_amount))

# def changeTurn(turn, player1, player2):
#     if turn == player1:
#         turn = player2
#     else:
#         turn = player1 
#     print("now it's player's {} move".format(turn))
#     return turn  

# while sweets_amount > 28:
#     quantity = int(input('Player {} Insert the quantity of sweets you want to take: '.format(turn)))
#     sweets_amount -= quantity
#     moveInfo(turn, quantity, sweets_amount)
#     turn = changeTurn(turn, player1, player2)
#     if sweets_amount < 28:
#         if turn == 1:
#             print("First player won")
#         else:
#             print("Second player won")

# a) Добавьте игру против бота
# P2Computer

# sweets_amount = 100
# turn = random.randint(1, 2)
# print("The player {} turn". format(turn))
# human = 1
# bot = 2

# def moveInfo(turn, quantity, sweets_amount):
#     if turn == 1:
#         print("Human made a move, he took {}. {} sweets is left.".format(quantity, sweets_amount))
#     else: 
#         print("Bot made a move, he took {}. {} sweets is left.".format(quantity, sweets_amount))

# def changeTurn(turn, human, bot):
#     if turn == human:
#         turn = bot
#     else:
#         turn = human 
#     print("now it's player's {} move".format(turn))
#     return turn  

# while sweets_amount > 28:
#     if turn == human:
#         quantity = int(input('Human Insert the quantity of sweets you want to take: '))
#     else:
#         quantity = random.randint(1, 28)
#         move = ('Bot takes {} sweets'.format(quantity))
#     sweets_amount -= quantity
#     moveInfo(turn, quantity, sweets_amount)
#     turn = changeTurn(turn, human, bot)
#     if sweets_amount < 28:
#         if turn == 1:
#             print("Human won")
#         else:
#             print("Bot won")


# b) Подумайте как наделить бота ""интеллектом""


# 3. Создайте программу для игры в ""Крестики-нолики"".



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def encode(string):
#     encoding = ""
#     i = 0
#     while i < len(string):
#         count = 1
#         while i + 1 < len(string) and string[i] == string[i + 1]:
#             count = count + 1
#             i = i + 1
#         encoding += str(count) + string[i]
#         i = i + 1
#     return encoding

# print(encode('AAAAABBCDDD'))