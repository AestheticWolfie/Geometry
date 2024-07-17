import time
import math

from CartesianBall import *
from CustomWindow import Window

window = Window(title="Geometry", x_geometry=400, y_geometry=400)

#  Ball Construction and placement

ball = CartesianBall(start_x=window.x_geometry / 2,
                     start_y=window.y_geometry / 2,
                     parent=window.canvas,
                     colour="green",
                     border_width=1,
                     ball_radius=5)

ball.draw_instance()


#  Update Func

def linear_update(ball_object: CartesianBall,
                  delta_time: float):

    ball_object.x = ball_object.x_prev + ball.x_velocity*delta_time
    ball_object.y = ball_object.y_prev + ball.y_velocity*delta_time

    if 0 >= ball_object.x or ball_object.x >= window.x_geometry and not ball_object.x_collision:
        ball_object.x_velocity *= -1
        ball_object.x_collision = True

    if 0 >= ball_object.y or ball_object.y >= window.y_geometry and not ball_object.y_collision:

        x_border = (window.y_geometry - ball_object.y_prev)\
                   *(ball_object.x - ball_object.x_prev)/(ball_object.y - ball_object.y_prev)
        x_border += ball_object.x_prev

        ball_object.x = x_border
        ball_object.y = 1

        ball_object.y_velocity *= -1
        ball_object.y_collision = True

    if 0 < ball_object.x < window.x_geometry and ball_object.x_collision:
        ball_object.x_collision = False

    if 0 < ball_object.y < window.y_geometry and ball_object.y_collision:
        ball_object.y_collision = False


#  Simulation

last_update_time = time.time()

ball.x_velocity = 100
ball.y_velocity = -200

while True:
    time.sleep(1/120)

    delta_time = time.time() - last_update_time
    print(delta_time)

    linear_update(ball, delta_time=delta_time)

    ball.draw_move()


    last_update_time += delta_time

window.mainloop()
