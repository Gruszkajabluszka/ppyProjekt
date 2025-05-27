import tkinter as tk
from gui import GameGUI
from settings import GameSettings

def main():
    root = tk.Tk()
    root.title("Gra w Życie - Conway")
    settings = GameSettings(rows=30, cols=30, speed=200)
    gui = GameGUI(root, settings)

    control_frame = tk.Frame(root)
    control_frame.pack()

    start_btn = tk.Button(control_frame, text="Start / Stop", command=gui.toggle_run)
    start_btn.pack(side=tk.LEFT)

    clear_btn = tk.Button(control_frame, text="Wyczyść", command=lambda: [gui.game.__init__(settings), gui.draw_grid()])
    clear_btn.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
