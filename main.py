import modellibrary as lib

# print(__name__)

# lib.foo()

# x = lib.bar(4, 4)
# print(x)

lib.create_objects('Andrei')
lib.create_objects('Vasya')
lib.create_objects('Galya')
lib.print_objects()

for obj in lib.objects:
    if 'Galya' in obj:
        print('Galya is found')

lib.objects.pop()
# Удаляет последний индекс в списке
lib.print_objects()
# help(lib)
# print(dir(lib))
