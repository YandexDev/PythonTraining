username = input('Как тебя зовут? ')
userage = int(input(f'Сколько тебе лет, {username}? '))
print(f'Привет, {username}. Тебе {userage} ', end='')
if userage % 10 == 1 and userage != 11:
    print('год!')
elif userage >= 5 and userage <= 20:
    print('лет!')
elif userage % 10 >= 2 and userage % 10 <= 4:
    print('года!')
else:
    print('лет!')

# x = 10
# while True:
#     x -= 1
#     if x < 0:
#         break
#     print(x)

# while x >= 0:
#     print(x)
#     x -= 1

# for i in range(1, 5):
#     print(i)


# print(14/3)
# print(14//3)
# print(14 % 3)
# print(2**10)

# print(len(str(10000)))

# x = 10.5
# y = 20
# z = 'goal'
# print(x, y, z, sep=':', end=' and ')
# print(x, y, z, sep='|')
# print(f'{x}:{y}:{z}')

# x = (5 != 3)
# print(x)

# help(print)
