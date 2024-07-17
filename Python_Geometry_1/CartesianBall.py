import tkinter as tk


class CartesianBall:
    """Cartesian Ball uses the standard (x,y) system we know and love. Remember we draw instance then we update
    coords to move x,y to their new x,y. After that we then just call on draw_move and the canvas handles it"""

    def __init__(self, start_x: float,
                 start_y: float,
                 parent: tk.Canvas,
                 **kwargs):
        self.x_prev: float = start_x
        self.y_prev: float = start_y

        self.x: float = start_x
        self.y: float = start_y

        self.x_velocity = kwargs.get('x_velocity', 0)
        self.y_velocity = kwargs.get('y_velocity', 0)

        self.x_collision: bool = False
        self.y_collision: bool = False

        self.radius: float = kwargs.get('ball_radius', 1)

        self.colour: str = kwargs.get('colour', '#ffffff')
        self.border_width: int = kwargs.get('border_width', 0)

        self.parent = parent
        self.canvas_object: (int, None) = None

    def draw_instance(self):
        self.canvas_object = self.parent.create_oval(self.x - self.radius, self.y - self.radius,
                                                     self.x + self.radius, self.y + self.radius,
                                                     fill=self.colour, width=self.border_width)

    def draw_move(self):
        """Canvas.move() method takes in the change in x and y and moves based on that."""

        delta_x = self.x - self.x_prev
        delta_y = self.y - self.y_prev

        self.parent.move(self.canvas_object, delta_x, delta_y)
        self.draw_line()

        self.x_prev = self.x
        self.y_prev = self.y

        self.parent.update()

    def draw_line(self):

        self.parent.create_line((self.x_prev, self.y_prev),(self.x,self.y),
                                width=2, fill="black")

