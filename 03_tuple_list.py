# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)
# b = []
# b = a
# b[0] = 2
# print(b)

# x = int('AB', base=16)
# print(x)

# A = list('Hello')
# print(A)

# B = [1, 2, 3]
# B.append(4)
# print(B)

A = list(range(1, 101, 1))
print(A)
# B = []
# for x in A:
#     if x % 7 == 0:
#         B.append(x)
# print(B)

B = [x for x in A if x % 7 == 0]
print(B)

help(list)
