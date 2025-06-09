import tkinter as tk
from tkinter import filedialog, messagebox
from game import GameOfLife
from settings import GameSettings


class GameGUI:
    def __init__(self, root, settings):
        self.root = root
        self.settings = settings
        self.game = GameOfLife(settings)
        self.running = False

        self.canvas = tk.Canvas(root, width=900, height=900, bg="white")
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

    def save_on_exit(self):
        filename = "autosave.txt"
        with open(filename, 'w') as f:
            for row in self.game.grid:
                f.write(''.join(str(cell) for cell in row) + '\n')

    def save_grid(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if filename:
            with open(filename, 'w') as f:
                for row in self.game.grid:
                    f.write(''.join(str(cell) for cell in row) + '\n')

    def load_grid(self):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if filename:
            with open(filename, 'r') as f:
                lines = f.readlines()
                self.game.grid = [
                    [int(char) for char in line.strip()]
                    for line in lines
                ]
            self.draw_grid()


class SettingsWindow:
    def __init__(self, master, current_settings, on_apply):
        self.top = tk.Toplevel(master)
        self.top.title("Ustawienia gry")
        self.on_apply = on_apply

        tk.Label(self.top, text="Wiersze:").grid(row=0, column=0)
        tk.Label(self.top, text="Kolumny:").grid(row=1, column=0)
        tk.Label(self.top, text="Szybkość (ms):").grid(row=2, column=0)

        self.rows_entry = tk.Entry(self.top)
        self.cols_entry = tk.Entry(self.top)
        self.speed_entry = tk.Entry(self.top)

        # Wstępne wartości
        self.rows_entry.insert(0, str(current_settings.rows))
        self.cols_entry.insert(0, str(current_settings.cols))
        self.speed_entry.insert(0, str(current_settings.speed))

        self.rows_entry.grid(row=0, column=1)
        self.cols_entry.grid(row=1, column=1)
        self.speed_entry.grid(row=2, column=1)

        tk.Button(self.top, text="Zastosuj", command=self.apply).grid(row=3, column=0, columnspan=2, pady=10)

    def apply(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            speed = int(self.speed_entry.get())
            self.on_apply(GameSettings(rows, cols, speed))
            self.top.destroy()
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawne liczby całkowite.")