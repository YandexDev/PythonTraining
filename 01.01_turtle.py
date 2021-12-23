import turtle as tur


def star():
    tur.color("red", "yellow")
    tur.speed(10)
    tur.begin_fill()
    for step in range(5):
        tur.forward(70)
        tur.left(144)
    tur.end_fill()


for starStep in range(5):
    star()
    tur.forward(100)
    tur.left(360 / 5)

tur.done()
