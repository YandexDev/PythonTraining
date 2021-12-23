# x = 5
# y = x
# print(x, y)
# x += 1
# print(x, y)

# T = (1, 2, 3, 4, 5)
# print(T[0])
# a, b, *C = T
# print(a, b, C, sep=' : ')
# print(type(C))
# print(T)
# print(*T)
# print(*T, sep=' : ', end='!\n')

# id_user_777 = 'Andrei', 'Pervyi'
# id_user_888 = 'Janna', 'Novikova'


# def hello(name, surname):
#     print('Hello,', name, surname, end='!!!\n')


# hello('Andrei', 'Pervyi')
# hello(*id_user_777)
# hello(*id_user_888)

# A = range(1, 10)
# print(*A)

# B = [('Andrei', 'Pervyi'), ('Zina', 'Golikova'), ('Maksim', 'Udalov')]
# for name, surname in B:
#     print(name, surname)

City = {"Moscow": 34567, "Dolgoprudny": 12345, "Piter": 67890}
City["Rostov"] = 45345
for key in City:
    print(key, City[key])

print(City)
print(City["Moscow"])
