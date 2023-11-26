import tkinter as tk
from tkinter import messagebox

import random


class LightsOutGame:
    def __init__(self, master, size):
        self.master = master
        self.size = size
        # 1 for single toggle, 0 for toggle neighbors
        self.toggle_mode = tk.BooleanVar(value=True)
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.game_blocks = [
            [
                tk.Button(
                    self.master,
                    width=3,
                    height=2,
                    command=lambda i=i, j=j: self.toggle_light(i, j),
                )
                for j in range(self.size)
            ]
            for i in range(self.size)
        ]

        for i in range(self.size):
            for j in range(self.size):
                self.game_blocks[i][j].grid(row=i, column=j)

        self.btnToggleMode = tk.Checkbutton(
            self.master,
            text="Toggle Neighbors",
            variable=self.toggle_mode,
            command=self.update_toggle_mode,
        )
        self.btnToggleMode.grid(row=self.size, columnspan=self.size)

        self.btnResetGame = tk.Button(
            self.master, text="Reset", command=self.reset_game
        )
        self.btnResetGame.grid(row=self.size + 1, columnspan=self.size)

    def toggle_light(self, i, j):
        if self.toggle_mode.get():
            # Single toggle mode
            self.board[i][j] = 1 - self.board[i][j]
        else:
            # Toggle neighbors mode
            self.toggle_neighbors(i, j)

        self.update_blocks()
        if all(light == 0 for row in self.board for light in row):
            messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def toggle_neighbors(self, i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.size and 0 <= nj < self.size:
                self.board[ni][nj] = 1 - self.board[ni][nj]
        self.update_blocks()
        if all(light == 0 for row in self.board for light in row):
            messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def update_toggle_mode(self):
        # Update the toggle mode when the checkbox is clicked
        self.toggle_mode.set(True if self.toggle_mode.get() == False else False)

    def update_blocks(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    self.game_blocks[i][j].config(bg="yellow")
                else:
                    self.game_blocks[i][j].config(bg="white")

    def reset_game(self):
        self.board = [
            [random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)
        ]
        self.update_blocks()


def main():
    base = tk.Tk()
    base.title("Lights Out Game")
    size = 5  # You can adjust the size of the grid
    game = LightsOutGame(base, size)
    base.mainloop()


if __name__ == "__main__":
    main()
