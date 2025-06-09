import tkinter as tk
from gui import GameGUI, SettingsWindow
from settings import GameSettings

def main():
    root = tk.Tk()
    root.title("Gra w Życie - Conway")
    settings = GameSettings(rows=30, cols=30, speed=200)
    gui = GameGUI(root, settings)

    def on_closing():
        gui.save_on_exit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    control_frame = tk.Frame(root)
    control_frame.pack()

    start_btn = tk.Button(control_frame, text="Start / Stop", command=gui.toggle_run)
    start_btn.pack(side=tk.LEFT)

    clear_btn = tk.Button(control_frame, text="Wyczyść", command=lambda: [gui.game.__init__(settings), gui.draw_grid()])
    clear_btn.pack(side=tk.LEFT)

    save_btn = tk.Button(control_frame, text="Zapisz", command=gui.save_grid)
    save_btn.pack(side=tk.LEFT)

    load_btn = tk.Button(control_frame, text="Wczytaj", command=gui.load_grid)
    load_btn.pack(side=tk.LEFT)

    def open_settings_window():
        def apply_new_settings(new_settings):
            nonlocal settings, gui
            settings = new_settings

            gui.canvas.destroy()


            gui = GameGUI(root, settings)


            start_btn.config(command=gui.toggle_run)
            clear_btn.config(command=lambda: [gui.game.__init__(settings), gui.draw_grid()])
            save_btn.config(command=gui.save_grid)
            load_btn.config(command=gui.load_grid)

        SettingsWindow(root, settings, apply_new_settings)

    settings_btn = tk.Button(control_frame, text="Ustawienia", command=open_settings_window)
    settings_btn.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
