# x = 11
# while x > 0:
#     x -= 1
#     print(x)
#     if x == 5:
#         break
#         # exit()
# else:
#     print('wtf')
# print('End')

# for i in 2, 5, 3, 7:
#     i -= 1
#     print(i, end=' ')

# a = range(10)
# print(a[1])


def multy_summ(x: int, y: "int > 0") -> int:
    "складывает два параметра"
    """можно вот так
    переносить строки
    и писать документ строку"""
    # вверху это документ строка
    # :int и -> int: это аннотация типов
    z = x + y
    print(z)
    return z - 1


print(multy_summ(1, 4))
