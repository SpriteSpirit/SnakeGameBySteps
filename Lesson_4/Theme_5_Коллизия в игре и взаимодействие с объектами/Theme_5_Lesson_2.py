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
sr = pygame.display.set_mode((WIDTH, HEIGHT)) # set_mode(size=00, flags=0, depth=0, display=0, vsync=0)
pygame.display.set_caption("SNAKE GAME") # указываем название игрового окна

fps = 30 # frames per second
clock = pygame.time.Clock() # создаём таймер и часы - будет тормозить нашу игру, чтобы достичь кол-ва кадров в секунду

position_x = 20 # позиция кубика по х
position_y = 20 # позиция кубика по у

# создаем булевые переменные, которые будут отображать какую клавишу мы нажали
is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

speed = 5 # скорость кубика

# указываем размеры героя - змейки
width_hero = 15
height_hero = 15

# игровой цикл (происходят постонные события)
while True:
    # для того, чтобы создать иллюзию перемещения, нужно заливать экран заново
    sr.fill(Black)
    # создаем структуру стандартных событий для любой игры
    for event in pygame.event.get(): # получаем событие из всех событий, происходящий в игре, чтобы обработать

        if event.type == pygame.QUIT: # если тип события - ВЫХОД (нажатие на крестик окна), то
            quit() # закрываем игру

        if event.type == pygame.KEYDOWN:  # ПРОВЕРЯЕМ: если событие == клавиша зажата
            if event.key == pygame.K_RIGHT:  # если клавиша == стрелка вправо
                is_key_right = True
            if event.key == pygame.K_LEFT: # если клавиша == стрелка влево
                is_key_left = True
            if event.key == pygame.K_UP: # если клавиша == стрелка вверх
                is_key_top = True
            if event.key == pygame.K_DOWN: # если клавиша == стрелка вниз
                is_key_down = True

        if event.type == pygame.KEYUP:  # ПРОВЕРЯЕМ: если событие == клавиша отжата
            if event.key == pygame.K_RIGHT:  # если клавиша == стрелка вправо
                is_key_right = False
            if event.key == pygame.K_LEFT: # если клавиша == стрелка влево
                is_key_left = False
            if event.key == pygame.K_UP: # если клавиша == стрелка вверх
                is_key_top = False
            if event.key == pygame.K_DOWN: # если клавиша == стрелка вниз
                is_key_down = False
                
    # привязываем к значениям переменных условия
    if is_key_right:
        position_x += speed  # смещаем позицию кубика на +5
    if is_key_left:
        position_x -= speed  # смещаем позицию кубика на -5
    if is_key_top:
        position_y -= speed # вверх с минусом, вниз - с плюсом
    if is_key_down:
        position_y += speed

    # ОБРАБАТЫВАЕМ КОЛЛИЗИЮ: если мы пересекаем границу стен, то кубик отталкивается
    if position_x <= 0: # отталкиваемся от левой границы
        position_x += speed
    if position_y <= 0: # отталкиваемся от верхней границы
        position_y += speed
    # добавляем условие для проверки коллизии правой границы и нижней
    if position_y + height_hero >= HEIGHT: # учитываем размер кубика + 15
        position_y -= speed
    if position_x + width_hero >= WIDTH: # учитываем размер кубика + 15
        position_x -= speed

    # на экране получаем загрузочную полоску
    pygame.draw.rect(sr, "Green", (position_x, position_y, 15, 15)) #  (20=x, 20=y + i * 25 (расстояние), 15 - ширина, 15 - высота))

    pygame.display.update() # отрисовываем то, что наложили на поверхность
    clock.tick(fps) # игра должна обрабатываться не чаще 30 кадров в сек.

# ------------------------------------------------------
#
# ------------------------------------------------------