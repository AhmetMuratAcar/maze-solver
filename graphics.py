from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")

        self.canvas = Canvas(master=self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        
        self.is_window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Redraws the window"""
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_window_running = True
        while self.is_window_running:
            self.redraw()

        print("Window Closed")

    def close(self):
        self.is_window_running = False

    def draw_line(self, line):
        line.draw(canvas=self.canvas)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill="black",
            width=2
        )