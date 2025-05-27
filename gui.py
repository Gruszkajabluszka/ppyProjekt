import tkinter as tk
from tkinter import ttk
from game import GameOfLife

class GameGUI:
    def __init__(self, root, settings):
        self.root = root
        self.settings = settings
        self.game = GameOfLife(settings)
        self.running = False

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.cell_width = self.canvas.winfo_reqwidth() // settings.cols
        self.cell_height = self.canvas.winfo_reqheight() // settings.rows

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.draw_grid()

        self.root.after(settings.speed, self.update_game)

    def on_canvas_click(self, event):
        col = event.x // self.cell_width
        row = event.y // self.cell_height
        self.game.toggle_cell(row, col)
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for r in range(self.settings.rows):
            for c in range(self.settings.cols):
                color = "black" if self.game.grid[r][c] else "white"
                x1 = c * self.cell_width
                y1 = r * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def update_game(self):
        if self.running:
            self.game.update()
            self.draw_grid()
        self.root.after(self.settings.speed, self.update_game)

    def toggle_run(self):
        self.running = not self.running
