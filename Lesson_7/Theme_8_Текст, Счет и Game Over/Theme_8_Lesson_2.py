import pygame  # импортируем библиотеку pygame
import random  # подгружаем рандом
import time

pygame.init()  # используется для мультимедиа контента


# ----------------->SNAKE CLASS<------------------------#
class Snake:  # создаем еще раз класс змейка
    def __init__(self, x, y, color, speed, size):  # создаём конструктор класса (вызывается при вызове класса)
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0  # -1 0 1 возможные значения
        self.dir_y = 0
        self.count = 10  # кол-во голов
        self.heads = []  # список голов
        self.add_head()

    # метод добавления головы
    def add_head(self):
        self.heads.append(Snake_head(self.x, self.y, self.color, self.speed, self.size))

    # метод удаления головы
    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)

    # метод отрисовки головы
    def draw(self, screen):
        for head in self.heads:  # перебираем все головы в списке голов и для каждой головы в списке
            head.draw(screen)  # отрисовываем голову

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed  # движение влево
        if self.dir_x == -1:
            self.x -= self.speed  # движение влево
        if self.dir_y == -1:
            self.y -= self.speed  # движение вверх
        if self.dir_y == 1:
            self.y += self.speed  # движение вниз
        self.add_head()
        self.remove_head()

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

    # функция проверки столкновения со стенами
    def check_walls(self):
        if self.x <= 0 or self.y <= 0 or self.y >= HEIGHT or self.x >= WIDTH:  # упрощаем код через оператор or
            return False # при столкновении со стеной возвращаем False, для is_game_active, чтобы завершить игру
        return True

# ----------------->SNAKE HEAD CLASS<------------------------#
class Snake_head:  # рефактирим класс змейка в класс голова_змейки
    def __init__(self, x, y, color, speed, size):  # создаём конструктор класса (вызывается при вызове класса)
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0  # -1 0 1 возможные значения
        self.dir_y = 0

    # функция отрисовки
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    # функция проверки еды
    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            return True
        return False


# ----------------->VARIABLES<------------------------#
WIDTH = 720  # ширина экрана
HEIGHT = 480  # высота экрана

# создаем цвета палитры RGB или можем использовать встроенные названия цветов в "Pink", "Yellow", etc.
Black = (0, 0, 0)
Red = (255, 0, 0)

image = pygame.image.load("../../images/snake1.png")  # загружаем изображение в папку проекта - обязательно
pygame.display.set_icon(image)  # устанавливаем иконку

speed = 15  # скорость змейки должна быть равна размеру, чтобы мы могли съедать еду
size = speed

food_x = 150  # начальные координаты еды
food_y = 150

fps = 10  # frames per second
clock = pygame.time.Clock()  # создаём таймер и часы - будет тормозить нашу игру, чтобы достичь кол-ва кадров в секунду

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # set_mode(size=00, flags=0, depth=0, display=0, vsync=0)
pygame.display.set_caption("SNAKE GAME")  # указываем название игрового окна

# создаем булевые переменные, которые будут отображать какую клавишу мы нажали
is_key_right = False
is_key_left = False
is_key_down = False
is_key_top = False

is_eat = True  # если is_draw = False, то мы съели кубик-еду
is_game_active = True  # активна ли игра (запущена)

# ----------------->SNAKE OBJECT<------------------------#
snake = Snake(3 * speed, 3 * speed, "White", speed, size)  # создаем объект в переменной змейка

# ----------------->GAME OVER TEXT<------------------------#
font1 = pygame.font.Font('../../Fonts/ARCADECLASSIC.TTF', 72)
game_over_text = font1.render("GAME    OVER!", True, "Pink")

# ----------------->GAME LOOP<------------------------#
while is_game_active:
    # для того, чтобы создать иллюзию перемещения, нужно заливать экран заново
    screen.fill(Black)

    # ----------------->EVENTS<------------------------#   создаем структуру стандартных событий для любой игры #
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

    # ----------------->MOVING<------------------------#
    # привязываем к значениям переменных условия
    if is_key_right:
        snake.move_right()  # заменяем на методы класса
    if is_key_left:
        snake.move_left()
    if is_key_top:
        snake.move_up()
    if is_key_down:
        snake.move_down()

    # ----------------->CALL FUNCTIONS<------------------------#
    is_game_active = snake.check_walls()  # ОБРАБАТЫВАЕМ КОЛЛИЗИЮ
    snake.move()  # непрерывное движение змейки
    snake.draw(screen)  # отрисовка змейки

    # временно закоментируем # is_eat = snake.check_food(food_x, food_y)   # проверяем еду
    # ----------------->CHECK EAT<------------------------#
    if is_eat:  # если еда съедена (кубик подобран)
        # выбираем рандомные координаты появления еды
        food_x = (random.randint(size, WIDTH) * speed % WIDTH)
        food_y = (random.randint(size, HEIGHT) * speed % HEIGHT)
    # print(food_x, food_y)

    # ----------------->FOOD DRAWING<------------------------#
    # pygame.draw.rect(screen, "Yellow", (food_x, food_y, size, size))  # создаем новый кубик (еда)

    pygame.display.update()
    clock.tick(fps)  # игра должна обрабатываться не чаще 30 кадров в сек.

# ----------------->GAME OVER TEXT DRAWING<------------------------#
screen.blit(game_over_text, (160, 200))  # отрисовываем текст
pygame.display.update()  # обновили экран
time.sleep(3)

# ----------------->COMMENTS<------------------------#


