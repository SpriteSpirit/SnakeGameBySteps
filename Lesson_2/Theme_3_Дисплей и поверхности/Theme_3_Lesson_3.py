import pygame # импортируем библиотеку pygame

WIDTH = 720 # ширина экрана
HEIGHT = 480 # высота экрана

# создаем цвета палитры RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Lime = (0, 255, 0)
Blue = (0, 0, 255)

# загружаем изображение в папку проекта - обязательно
image = pygame.image.load("../../images/snake1.png")
pygame.display.set_icon(image) # устанавливаем иконку

# создали переменнную, в которой зраним параметры экрана
sr = pygame.display.set_mode((WIDTH, HEIGHT)) # set_mode(size=00, flags=0, depth=0, display=0, vsync=0) - какие параметры принимает функция (мы указали только размер экрана)
pygame.display.set_caption("SNAKE GAME") # указываем название игрового окна

# игровой цикл (происходят постонные события)
# используем пока что бесконечный цикл
while True:
    # создаем структуру стандартных событий для любой игры
    for event in pygame.event.get(): # получаем событие из всех событий, происходящий в игре, чтобы обработать
        if event.type == pygame.QUIT: # если тип события - ВЫХОД (нажатие на крестик окна), то
            quit() # закрываем игру

    for i in range(15):
        pygame.draw.rect(sr, "Green", (20, 20 + i * 25, 15, 15)) #  (20=x, 20=y + i * 25 (расстояние), 15 - ширина, 15 - высота))
        pygame.draw.rect(sr, "Green", (20 + i * 25, 20, 15, 15))  # (20=x + i * 25 (расстояние), 20=y , 15 - ширина, 15 - высота))

    pygame.display.update() # отрисовываем то, что наложили на поверхность
# ------------------------------------------------------
# Отрисовка примитивов:
# pygame.draw.rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) - прямоугольник
# pygame.draw.polygon(surface, color, points, width=0)  # points (tuple(coordinate) or list(coordinate)) - a sequence of 3 or more (x, y) coordinates that make up the vertices of the polygon, each coordinate in the sequence must be a tuple/list/pygame.math.Vector2 of 2 ints/floats, e.g. [(x1, y1), (x2, y2), (x3, y3)]
# pygame.draw.circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) - круг
# pygame.draw.ellipse(surface, color, rect, width=0) - эллипс
# pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1) - дуга
# pygame.draw.line(surface, color, start_pos, end_pos, width=1) - ломаная линия
# pygame.draw.lines(surface, color, closed, points, width=1) - ломаные линии
# pygame.draw.aaline(surface, color, start_pos, end_pos, blend=1) - сглаженная линия
# pygame.draw.aalines(surface, color, closed, points, blend=1) - сглаженные линии
#
#  EXAMPLES:
# pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
# pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
# pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)
# pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
# pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
# pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
# pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,border_bottom_right_radius=15)
# pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
# pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
# pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
# pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
# pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
# pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
# pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
# pygame.draw.circle(screen, BLUE, [60, 250], 40)
# pygame.draw.circle(screen, BLUE, [250, 250], 40, 0, draw_top_right=True)
# pygame.draw.circle(screen, RED, [250, 250], 40, 30, draw_top_left=True)
# pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
# pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)
# ------------------------------------------------------