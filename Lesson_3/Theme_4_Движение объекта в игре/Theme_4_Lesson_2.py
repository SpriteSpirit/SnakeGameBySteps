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

position_x = 20 # позиция кубика

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
                position_x += 5 # смещаем позицию кубика на +5
            if event.key == pygame.K_LEFT: # если клавиша == стрелка влево
                position_x -= 5 # смещаем позицию кубика на -5


    # на экране получаем загрузочную полоску
    pygame.draw.rect(sr, "Green", (position_x, 250, 15, 15)) #  (20=x, 20=y + i * 25 (расстояние), 15 - ширина, 15 - высота))

    pygame.display.update() # отрисовываем то, что наложили на поверхность
    clock.tick(fps) # игра должна обрабатываться не чаще 30 кадров в сек.

# ------------------------------------------------------
# События  - EVENTS (https://pg1.readthedocs.io/en/latest/ref/event.html)
# QUIT              none
# ACTIVEEVENT       gain, state
# KEYDOWN           key, mod, unicode, scancode
# KEYUP             key, mod, unicode, scancode
# MOUSEMOTION       pos, rel, buttons, touch
# MOUSEBUTTONUP     pos, button, touch
# MOUSEBUTTONDOWN   pos, button, touch
# JOYAXISMOTION     joy (deprecated), instance_id, axis, value
# JOYBALLMOTION     joy (deprecated), instance_id, ball, rel
# JOYHATMOTION      joy (deprecated), instance_id, hat, value
# JOYBUTTONUP       joy (deprecated), instance_id, button
# JOYBUTTONDOWN     joy (deprecated), instance_id, button
# VIDEORESIZE       size, w, h
# VIDEOEXPOSE       none
# USEREVENT         code
# ------------------------------------------------------