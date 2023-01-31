import pygame  # импортируем библиотеку pygame
import random  # подгружаем рандом


class Snake:  # создаём класс змейка
    def __init__(self, x, y, color, speed, size):  # создаём конструктор класса (вызывается при вызове класса)
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0  # -1 0 1 возможные значения
        self.dir_y = 0

    # перерабатываем управление на непрерывное движение змейки
    def move(self):
        if self.dir_x == 1:
            self.x += self.speed  # движение влево
        if self.dir_x == -1:
            self.x -= self.speed  # движение влево
        if self.dir_y == -1:
            self.y -= self.speed  # движение вверх
        if self.dir_y == 1:
            self.y += self.speed  # движение вниз

    # функция движения вправо
    def move_right(self):
        self.dir_x = 1
        self.dir_y = 0

    # функция движения влево
    def move_left(self):
        self.dir_x = -1
        self.dir_y = 0

    # функция движения вниз
    def move_down(self):
        self.dir_x = 0
        self.dir_y = 1

    # функция движения вверх
    def move_up(self):
        self.dir_x = 0
        self.dir_y = -1

    # функция отрисовки
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    # функция проверки столкновения со стенами
    def check_walls(self):
        if self.x <= 0:  # отталкиваемся от левой границы
            self.move_right()  # position_x += speed заменяем на методы класса
        if self.y <= 0:  # отталкиваемся от верхней границы
            self.move_down()
            # добавляем условие для проверки коллизии правой границы и нижней
        if self.y >= HEIGHT:  # уже не учитываем размер кубика + 15
            snake.move_up()
        if self.x >= WIDTH:  # уже не учитываем размер кубика + 15
            self.move_left()

    # функция проверки еды
    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            return True
        return False


WIDTH = 720  # ширина экрана
HEIGHT = 480  # высота экрана

# создаем цвета палитры RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Lime = (0, 255, 0)
Blue = (0, 0, 255)

# загружаем изображение в папку проекта - обязательно
image = pygame.image.load("../../images/snake1.png")
pygame.display.set_icon(image)  # устанавливаем иконку

speed = 15  # скорость змейки должна быть равна размеру, чтобы мы могли съедать еду
size = speed

food_x = 150  # начальные координаты еды
food_y = 150

fps = 10  # frames per second
clock = pygame.time.Clock()  # создаём таймер и часы - будет тормозить нашу игру, чтобы достичь кол-ва кадров в секунду

# создали переменнную, в которой храним параметры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set_mode(size=00, flags=0, depth=0, display=0, vsync=0)
pygame.display.set_caption("SNAKE GAME")  # указываем название игрового окна

# создаем булевые переменные, которые будут отображать какую клавишу мы нажали
is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

# добавим булевую переменную для отрисовки по условию
is_eat = True  # если is_draw = False, то мы съели кубик-еду

snake = Snake(3 * speed, 3 * speed, "White", speed, size)  # создаем объект в переменной змейка

# игровой цикл (происходят постонные события)
while True:
    # для того, чтобы создать иллюзию перемещения, нужно заливать экран заново
    screen.fill(Black)

    # создаем структуру стандартных событий для любой игры
    for event in pygame.event.get():  # получаем событие из всех событий, происходящий в игре, чтобы обработать

        if event.type == pygame.QUIT:  # если тип события - ВЫХОД (нажатие на крестик окна), то
            quit()  # закрываем игру

        if event.type == pygame.KEYDOWN:  # ПРОВЕРЯЕМ: если событие == клавиша зажата
            if event.key == pygame.K_RIGHT:  # если клавиша == стрелка вправо
                is_key_right = True
            if event.key == pygame.K_LEFT:  # если клавиша == стрелка влево
                is_key_left = True
            if event.key == pygame.K_UP:  # если клавиша == стрелка вверх
                is_key_top = True
            if event.key == pygame.K_DOWN:  # если клавиша == стрелка вниз
                is_key_down = True

        if event.type == pygame.KEYUP:  # ПРОВЕРЯЕМ: если событие == клавиша отжата
            if event.key == pygame.K_RIGHT:  # если клавиша == стрелка вправо
                is_key_right = False
            if event.key == pygame.K_LEFT:  # если клавиша == стрелка влево
                is_key_left = False
            if event.key == pygame.K_UP:  # если клавиша == стрелка вверх
                is_key_top = False
            if event.key == pygame.K_DOWN:  # если клавиша == стрелка вниз
                is_key_down = False

    # привязываем к значениям переменных условия
    if is_key_right:
        snake.move_right()  # заменяем на методы класса
    if is_key_left:
        snake.move_left()
    if is_key_top:
        snake.move_up()
    if is_key_down:
        snake.move_down()

    snake.check_walls()  # ОБРАБАТЫВАЕМ КОЛЛИЗИЮ
    snake.move() # непрерывное движение змейки
    snake.draw(screen)  # отрисовка змейки

    # проверяем еду
    is_eat = snake.check_food(food_x, food_y)

    if is_eat:  # если еда съедена (кубик подобран)
        # выбираем рандомные координаты появления еды
        food_x = (random.randint(size, WIDTH) * speed % WIDTH)
        food_y = (random.randint(size, HEIGHT) * speed % HEIGHT)
        print(food_x, food_y)

    pygame.draw.rect(screen, "Yellow", (food_x, food_y, size, size))  # создаем новый кубик (еда)

    pygame.display.update()  # отрисовываем то, что наложили на поверхность
    clock.tick(fps)  # игра должна обрабатываться не чаще 30 кадров в сек.

# ------------------------------------------------------
# для проверки всех позиций еды можно поставить fps = 2000, закомментировать screen.fill(Black) в цикле
# и перенести  food_x = random.randint(1, 20) * speed и food_y = random.randint(1, 20) * speed за пределы условия
# ------------------------------------------------------
