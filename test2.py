from Seed import *
import tkinter as tk
import math
import time
import random

# Constants
frame_rate = 60


# Polar to Cartestian
def polar_to_cartesian(distance, theta, origin_coords: tuple) -> tuple:
    x = distance * math.cos(theta) + origin_coords[0]
    y = distance * math.sin(theta) + origin_coords[1]

    return x, y


# Window
window = tk.Tk()

window.title = "Phyllotaxis"
window.geometry("800x800")

# Canvas
canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()

# Creating ball
ball_list: list[Seed] = []

for i in range(0, 1500):
    ball = Seed(radius=1, cartesian_x=random.randint(0,100), cartesian_y=random.randint(0, 100), border_width=1)
    ball.draw_ball_cart(canvas)
    ball_list.append(ball)

# Variables
delta_time = 0
elapsed_time = 0

while True:
    previous_time = time.time()

    for index, item in enumerate(ball_list):
        item.move_ball_parabola(canvas, -1
                                , (10 + (index/50))
                                , 5, delta_time, elapsed_time)

    window.update()
    delta_time = time.time() - previous_time
    elapsed_time += delta_time
    if delta_time != 0:
        print(1/delta_time)
    else:
        print(10000)

window.mainloop()
