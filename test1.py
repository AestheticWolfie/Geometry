import tkinter as tk
import math
import time


def polar_to_cartesian(distance, theta, origin_coords: tuple) -> tuple:
    x = distance * math.cos(theta) + origin_coords[0]
    y = distance * math.sin(theta) + origin_coords[1]

    return x, y


class Seed:
    origin_coords = (400, 400)

    def __init__(self, radius, distance, width, theta, colour):
        self.radius = radius
        self.distance = distance
        self.width = width
        self.theta = theta
        self.colour = colour

    def draw_ball(self, parent: tk.Canvas, colour):
        cart_coord = polar_to_cartesian(self.distance, self.theta, self.origin_coords)

        parent.create_oval(cart_coord[0] - self.radius, cart_coord[1] - self.radius,
                           cart_coord[0] + self.radius, cart_coord[1] + self.radius,
                           fill=colour, width=self.width)


# Vars
frame_rate = 60
counter = 0

window = tk.Tk()

window.title = "Phyllotaxis"
window.geometry("800x800")

canvas = tk.Canvas(window, width=800, height=800, background="dark gray")
canvas.pack()

# Creating Ball
ball = Seed(1, 0, 0, 0, "#5fad00")
ball2 = Seed(1, 0, 0, 0, "#5f9aca")

while True:

    ball.theta += 0.01
    ball2.theta -= 0.01

    ball.distance = ball.theta
    ball2.distance = ball2.theta * 1.1
    if not counter % 3:
        ball.draw_ball(canvas, "#5fad00")
    else:
        ball.draw_ball(canvas, "#b69aca")
    if counter % 7:
        ball2.draw_ball(canvas, "#5f9aca")
    else:
        ball2.draw_ball(canvas, "blue")

    window.update()

    counter += 1

    # time.sleep(1/frame_rate)
window.mainloop()
