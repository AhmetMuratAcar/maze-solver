from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")

        self.canvas = Canvas(master=self.root, bg="white", height=height, width=width)
        self.canvas.pack()
        
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

        print("Window Closed)

    def close(self):
        self.is_window_running = False

    def draw_line(self, line, fill_color):
        line.draw(canvas=self.canvas, fill_color=fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color,
            width=2
        )


def main():
    win = Window(800, 600)
    p1 = Point(50, 100)
    p2 = Point(0, 0)
    l1 = Line(p1, p2)
    win.draw_line(line=l1, fill_color="black")

    p3 = Point(400, 300)
    p4 = Point(800, 600)
    l2 = Line(p3, p4)
    win.draw_line(line=l2, fill_color="red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
