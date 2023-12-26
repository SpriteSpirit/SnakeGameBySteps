import pygame
import time
from random import randint

pygame.init()

font1 = pygame.font.SysFont(None, 72)
game_over_text = font1.render("Game Over", True, "White")


def main_menu():
    menu = True
    selected = "Start"

    while menu:
        screen.fill("Pink")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "Start"
                if event.key == pygame.K_DOWN:
                    selected = "Exit"
                if event.key == pygame.K_RETURN:
                    if selected == "Start":
                        return True
                    else:
                        the_end = True
                        return False

        title = font1.render("Snake Game", True, "Red")
        font3 = pygame.font.SysFont(None, 48)

        if selected == "Start":
            start = font3.render("Start", True, "Black")
        else:
            start = font3.render("Start", True, "White")

        if selected == "Exit":
            exit = font3.render("Exit", True, "Black")
        else:
            exit = font3.render("Exit", True, "White")

        screen.blit(title, (width / 2 - 165, 80))
        screen.blit(start, (width / 2 - 45, 200))
        screen.blit(exit, (width / 2 - 45, 250))

        pygame.display.update()
        clock.tick(fps)


class Snake:
    def __init__(self, x, y, colour, speed):
        self.x = x
        self.y = y
        self.colour = colour
        self.speed = speed
        self.size = 15
        self.dir_x = 0
        self.dir_y = 0
        self.count = 1
        self.heads = []
        self.add_head()
        self.change_colour_snake()

    def add_head(self):
        self.heads.append(Snake_head(self.x, self.y, self.colour, self.speed, self.size))

    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed
        if self.dir_x == -1:
            self.x -= self.speed
        if self.dir_y == -1:
            self.y -= self.speed
        if self.dir_y == 1:
            self.y += self.speed
        self.add_head()
        self.remove_head()

    def move_right(self):
        if self.count == 1:
            self.dir_x = 1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = 1
                self.dir_y = 0

    def move_left(self):
        if self.count == 1:
            self.dir_x = -1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = -1
                self.dir_y = 0

    def move_up(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = -1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = -1

    def move_down(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = 1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = 1

    def draw(self, screen):
        for head in self.heads:
            head.draw(screen)
        # pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size))

    def check_walls(self):
        if self.x <= 0 or self.y <= 0 or self.y >= height - self.size or self.x >= width - self.size:
            return False
        return True

    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.count += 1
            return True
        return False

    def check_snake(self):
        for i in range(len(self.heads)):
            if i != len(self.heads) - 1:
                if self.x == self.heads[i].x and self.y == self.heads[i].y:
                    return False
            return True

    def change_colour_snake(self):
        if self.check_food(food_x, food_y):
            self.colour = colours[randint(0, len(colours) - 1)]


class Snake_head:
    def __init__(self, x, y, colour, speed, size):
        self.x = x
        self.y = y
        self.colour = colour
        self.speed = speed
        self.size = size
        self.dir_x = 0  # -1 0 1 возможные значения
        self.dir_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size))


width = 720
height = 480
fps = 10
clock = pygame.time.Clock()

# image = pygame.image.load("snakeicon.png")
# pygame.display.set_icon(image)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# pygame.draw.rect(screen, "yellow", (60, 70, 15, 30))
# pygame.draw.line(screen, "blue", [60, 70], [120, 480], 10)
# pygame.draw.ellipse(screen, "white", (100,100, 20, 80))


food_x = 150
food_y = 150
size = 15
speed = 15

is_key_right = False
is_key_left = False
is_key_up = False
is_key_down = False

is_eat = True
is_game_active = main_menu()
the_end = main_menu()

snake = Snake(15, 15, "yellow", speed)

colours = ["yellow", "red", "blue", "white", "green"]


def change_food_colour():
    pygame.draw.rect(screen, snake.colour, (food_x, food_y, size, size))


while is_game_active:
    screen.fill("black")
    font2 = pygame.font.SysFont(None, 30)
    score_text = font2.render(str(snake.count - 1), True, "White")
    screen.blit(score_text, (20, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                is_key_up = True
            if event.key == pygame.K_s:
                is_key_down = True
            if event.key == pygame.K_a:
                is_key_left = True
            if event.key == pygame.K_d:
                is_key_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                is_key_up = False
            if event.key == pygame.K_s:
                is_key_down = False
            if event.key == pygame.K_d:
                is_key_right = False
            if event.key == pygame.K_a:
                is_key_left = False

    if is_key_right:
        snake.move_right()
    if is_key_left:
        snake.move_left()
    if is_key_up:
        snake.move_up()
    if is_key_down:
        snake.move_down()

    snake.move()
    snake.change_colour_snake()
    snake.draw(screen)
    is_game_active1 = snake.check_walls()
    is_game_active2 = snake.check_snake()
    is_game_active = is_game_active1 and is_game_active2
    print(is_game_active1, is_game_active2)
    is_eat = snake.check_food(food_x, food_y)

    if is_eat:
        food_x = randint(size, width) * speed % width
        food_y = randint(size, height) * speed % height

    change_food_colour()

    pygame.display.update()
    clock.tick(fps)

if the_end:
    screen.fill("Red")
    screen.blit(game_over_text, (width / 2 - 140, height / 2 - 40))
    pygame.display.update()
    time.sleep(2)
