import tkinter as tk


class Window(tk.Tk):

    def __init__(self, **kwargs):
        super().__init__()

        # Window Construction

        self.title_name: str = kwargs.get('title', "Geometry")
        self.x_geometry = kwargs.get('x_geometry', 400)
        self.y_geometry = kwargs.get('y_geometry', 400)

        self.title(self.title_name)
        self.geometry(f"{self.x_geometry}x{self.y_geometry}")

        # Canvas Construction

        self.background = kwargs.get('background', '#ffffff')

        self.canvas = tk.Canvas(self, background=self.background)
        self.canvas.pack(fill="both", expand=True)



