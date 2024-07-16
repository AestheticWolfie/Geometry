import math
import tkinter as tk


def polar_to_cartesian(distance, theta, origin_coords: tuple) -> tuple:
    x = distance * math.cos(theta) + origin_coords[0]
    y = distance * math.sin(theta) + origin_coords[1]

    return x, y


class Seed:

    def __init__(self, radius, **kwargs):
        self.radius: int = radius

        # Only use either polar or cartesian

        self.distance: int = kwargs.get('polar_distance', None)
        self.theta: int = kwargs.get('polar_theta', None)  # Radians

        self.x = kwargs.get('cartesian_x', None)
        self.y = kwargs.get('cartesian_y', None)
        self.x_velocity = kwargs.get('cartesian_x_velocity', None)
        self.y_velocity = kwargs.get('cartesian_y_velocity', None)

        self.colour: str = kwargs.get('colour', '#ffffff')
        self.border_width: int = kwargs.get('border_width', 0)

        self.origin_coords: tuple = kwargs.get('origin_coords', (400, 400))

        self.canvas_object = None

    def draw_ball_polar(self, parent: tk.Canvas):
        cart_coord = polar_to_cartesian(self.distance, self.theta, self.origin_coords)

        self.canvas_object = parent.create_oval(cart_coord[0] - self.radius, cart_coord[1] - self.radius,
                                                cart_coord[0] + self.radius, cart_coord[1] + self.radius,
                                                fill=self.colour, width=self.border_width)

    def draw_ball_cart(self, parent: tk.Canvas):
        self.canvas_object = parent.create_oval(self.x - self.radius, self.y - self.radius,
                                                self.x + self.radius, self.y + self.radius,
                                                fill=self.colour, width=self.border_width)

    def move_ball_linear_cartestian(self, parent: tk.Canvas, m, speed, delta_time):
        delta_x = 1*delta_time * speed
        delta_y = m*delta_time * speed

        parent.move(self.canvas_object, delta_x, delta_y)

    def move_ball_parabola(self, parent: tk.Canvas, a, b, speed, delta_time, elapsed_time):

        delta_x = 1 * delta_time * speed
        delta_y = (2 * a * elapsed_time + b) * delta_time * speed

        parent.move(self.canvas_object, delta_x, delta_y)
        
