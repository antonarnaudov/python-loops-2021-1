from math import sqrt
from random import randint
from time import sleep, time
from tkinter import *

HEIGHT = 500
WIDTH = 800

window = Tk()
window.title('Puk')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

# drawing submarine
ship = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_hit_area = c.create_oval(0, 0, 30, 30, outline='yellow')
SHIP_R = 15

MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

c.move(ship, MID_X, MID_Y)
c.move(ship_hit_area, MID_X, MID_Y)

# move a submarine
SHIP_SPD = 10


def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship, 0, -SHIP_SPD)
        c.move(ship_hit_area, 0, -SHIP_SPD)

    elif event.keysym == 'Down':
        c.move(ship, 0, SHIP_SPD)
        c.move(ship_hit_area, 0, SHIP_SPD)

    elif event.keysym == 'Left':
        c.move(ship, -SHIP_SPD, 0)
        c.move(ship_hit_area, -SHIP_SPD, 0)

    elif event.keysym == 'Right':
        c.move(ship, SHIP_SPD, 0)
        c.move(ship_hit_area, SHIP_SPD, 0)


c.bind_all('<Key>', move_ship)

# create a bubble
bub_id = []
bub_r = []
bub_speed = []

MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10

GAP = 100


def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    bubble = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(bubble)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


# move bubbles
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


# get coordinates
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2

    return x, y


# delete bubble
def del_bubble(i):
    bub_r.pop(i)
    bub_speed.pop(i)
    c.delete(bub_id[i])
    bub_id.pop(i)


# clean bubbles
def clean_up_bubs():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)


# calculate the distance
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# pop the bubbles
def collision():
    points = 0
    for bub_i in range(len(bub_id) - 1, -1, -1):
        if distance(ship_hit_area, bub_id[bub_i]) < (SHIP_R + bub_r[bub_i]):
            points += (bub_r[bub_i] + bub_speed[bub_i])
            del_bubble(bub_i)
    return points


c.create_text(50, 30, text='TIME', fill='white')
c.create_text(150, 30, text='SCORE', fill='white')
time_text = c.create_text(50, 30, text='TIME', fill='white')
score_text = c.create_text(150, 30, text='SCORE', fill='white')


def show_score(score):
    c.itemconfig(score_text, text=str(score))


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

# main game loop
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

c.create_text(MID_X, MID_Y, text='GAME OVER', fill='white', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 30, text=f'Score: {str(score)}', fill='white')
c.create_text(MID_X, MID_Y + 45, text=f'Bonus time: {str(bonus * TIME_LIMIT)}', fill='white')
