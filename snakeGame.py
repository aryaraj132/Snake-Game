import pygame as pg
import time
import random
import os
pg.init()

width = 800
height = 600

screen = pg.display.set_mode((width, height))
pg.display.set_caption("By - Aryan")

icon = pg.image.load(os.path.dirname(os.path.realpath(__file__)) + '/snake.png')
pg.display.set_icon(icon)
clock = pg.time.Clock()
font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("comicsansms", 35)
def message(msg,color):
    info = font_style.render(msg, True, color)
    screen.blit(info, [10, height/2])

snakeSize = 10
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, (255,255,0))
    screen.blit(value, [0, 0])
def snake(snakeSize, List):
    for x in List:
        pg.draw.rect(screen,(255,0,0),[x[0],x[1],snakeSize, snakeSize])

def loop():
    running = True
    lost = False
    x_cod = width/2
    y_cod = height/2

    x_change = 0
    y_change = 0

    List = []
    Length = 1

    food_x = round(random.randrange(0, width - snakeSize)/10.0) * 10.0
    food_y = round(random.randrange(0, height - snakeSize)/10.0) * 10.0

    while running:
        while lost:
            screen.fill((0,0,0))
            message("You Lost! Press Q-Quit or C-Play Again", (255,0,0))
            Your_score(Length - 1)
            pg.display.update()
            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_q:
                        running = False
                        lost = False
                    if event.key==pg.K_c:
                        loop()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                screen.fill((0,0,0))
                message("Sorry! But you will have to finish what you started", (255,0,0))
                Your_score(Length - 1)
                pg.display.update()
                time.sleep(3)
                loop()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -snakeSize
                    y_change = 0
                elif event.key == pg.K_RIGHT:
                    x_change = snakeSize
                    y_change = 0
                elif event.key == pg.K_UP:
                    x_change = 0
                    y_change = -snakeSize
                elif event.key == pg.K_DOWN:
                    x_change = 0
                    y_change = snakeSize
                elif event.key == pg.K_q:
                    running = False
        if x_cod >= width or x_cod < 0 or y_cod >= height or y_cod<0:
            lost = True
        x_cod += x_change
        y_cod += y_change
        screen.fill((120,120,120))
        pg.draw.rect(screen,(255,255,0),[food_x,food_y,snakeSize,snakeSize])
        Head = []
        Head.append(x_cod)
        Head.append(y_cod)
        List.append(Head)
        if len(List) > Length:
            del List[0]
        for x in List[:-1]:
            if x == Head:
                lost = True
        snake(snakeSize, List)
        Your_score(Length - 1)
        pg.display.update()
        if x_cod == food_x and y_cod == food_y:
            food_x = round(random.randrange(0, width - snakeSize)/10.0) * 10.0
            food_y = round(random.randrange(0, height - snakeSize)/10.0) * 10.0
            Length += 1
        clock.tick(15)

    pg.quit()
    quit()
loop()