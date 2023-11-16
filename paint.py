import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application")

        # Create a frame for the options
        options_frame = tk.Frame(root)
        options_frame.pack(side=tk.TOP, fill=tk.X)

        # Create buttons for options
        pen_button = tk.Button(options_frame, text="Pen", command=lambda: self.set_tool("pen"))
        pen_button.pack(side=tk.LEFT, padx=5)

        brush_button = tk.Button(options_frame, text="Brush", command=lambda: self.set_tool("brush"))
        brush_button.pack(side=tk.LEFT, padx=5)

        color_button = tk.Button(options_frame, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5)

        eraser_button = tk.Button(options_frame, text="Eraser", command=lambda: self.set_tool("eraser"))
        eraser_button.pack(side=tk.LEFT, padx=5)

        # Create a label for the size control
        size_label = tk.Label(options_frame, text="Size:")
        size_label.pack(side=tk.LEFT, padx=5)

        # Create a scrollbar for the size
        self.size_var = tk.DoubleVar()
        size_scrollbar = tk.Scale(options_frame, from_=1, to=20, orient=tk.HORIZONTAL, variable=self.size_var,
                                  command=self.update_size)
        size_scrollbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Set the default size
        size_scrollbar.set(2)

        # Display the current size
        self.size_display = tk.Label(options_frame, text="2")
        self.size_display.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Initialize drawing variables
        self.old_x = None
        self.old_y = None
        self.tool = "pen"  # Default tool is pen
        self.color = "black"
        self.size = 2

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x, y = event.x, event.y

        if self.old_x and self.old_y:
            if self.tool == "pen":
                self.canvas.create_line(self.old_x, self.old_y, x, y, width=self.size, fill=self.color,
                                        capstyle=tk.ROUND, smooth=tk.TRUE)
            elif self.tool == "brush":
                self.canvas.create_oval(x - self.size, y - self.size, x + self.size, y + self.size,
                                         fill=self.color, outline=self.color)
            elif self.tool == "eraser":
                self.canvas.create_rectangle(x - self.size, y - self.size, x + self.size, y + self.size,
                                             fill="white", outline="white")

        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def update_size(self, size):
        self.size = int(float(size))
        self.size_display.config(text=str(self.size))

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
