def main():
    x, y = 500, 600
    width, height = 300, 400
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Нарисовать домик широной width и высотой height, с опорной точки x и y,
    которая находитс в нижней точке фундамента
    x, y: координаты опорной точки, середины домика
    width, height: полная ширина и высота домика
    return: None
    """
    print('Рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, (y - walls_height - foundation_height),
                    width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Рисует основание домика
    """
    print('Рисую основание домика...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    """
    Рисует стены домика
    """
    print('Рисую стены домика...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """
    Рисует крышу домика
    """
    print('Рисую крышу домика...', x, y, width, height)
    pass


main()
