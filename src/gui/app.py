from src.gui.main_window import MainWindow
import customtkinter as ctk
from src.gui.styles import apply_theme
def main():
    apply_theme()
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()