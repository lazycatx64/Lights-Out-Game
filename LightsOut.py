import tkinter as tk
from tkinter import messagebox

import random


class LightsOutGame:
    
    def __init__( self, master, size ):
        self.master = master
        self.size = size
        
        self.toggle_mode = tk.BooleanVar( value=False )
        
        self.do_create_widgets()
        self.do_reset_game()


    def do_create_widgets( self ):
        
        # Frame for checkboxes and buttons
        self.frame_control = tk.Frame( self.master, padx=10, pady=10, borderwidth=2, relief="ridge" )
        self.frame_control.grid( row=0, column=0, columnspan=self.size+1 )
        
        # Toggle Mode checkbox
        self.button_toggle_mode = tk.Checkbutton(
                self.frame_control,
                text="Flip Single",
                variable=self.toggle_mode,
                command=self.do_update_mode,
            )
        self.button_toggle_mode.grid( row=0, column=0, columnspan=self.size )


        # Reset Button
        self.button_reset_game = tk.Button(
                self.frame_control, text="Reset", command=self.do_reset_game
            )
        self.button_reset_game.grid( row=0, column=self.size+1 )


        # Frame for game blocks
        self.frame_gameblocks = tk.Frame( self.master, padx=10, pady=10, borderwidth=2, relief="ridge" )
        self.frame_gameblocks.grid( row=1, column=0, columnspan=self.size+1 )
        


        # Game Blocks
        self.button_gameblocks = [
            [
                tk.Button(
                    self.frame_gameblocks,
                    width=4,
                    height=2,
                    command=lambda i=i, j=j: self.do_toggle_light( i, j ),
                )
                for j in range( self.size )
            ]
            for i in range( self.size )
        ]
        for i in range( self.size ):
            for j in range( self.size ):
                self.button_gameblocks[i][j].grid( row=i, column=j )



    def do_toggle_light( self, i, j ):
        if self.toggle_mode.get():
            # Single toggle mode
            self.board[i][j] = 1 - self.board[i][j]
        else:
            # Toggle neighbors mode
            self.do_toggle_neighbors( i, j )

        self.do_update_blocks()
        
        if all( light == 0 for row in self.board for light in row ):
            messagebox.showinfo( 'Congratulations!', 'You solved the puzzle!' )


    def do_toggle_neighbors( self, i, j ):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.size and 0 <= nj < self.size:
                self.board[ni][nj] = 1 - self.board[ni][nj]


    def do_update_mode( self ):
        # Update the toggle mode when the checkbox is clicked
        self.toggle_mode.set( True if self.toggle_mode.get() == False else False )
        self.button_toggle_mode.toggle()


    def do_update_blocks( self ):
        for i in range( self.size ):
            for j in range( self.size ):
                if self.board[i][j] == 1:
                    self.button_gameblocks[i][j].config( bg="black" )
                else:
                    self.button_gameblocks[i][j].config( bg="white" )


    def do_reset_game( self ):
        self.board = [
            [random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)
        ]
        self.do_update_blocks()


def main():
    base = tk.Tk()
    base.title( 'Lights Out Game' )
    size = 5  # You can adjust the size of the grid
    game = LightsOutGame( base, size )
    base.mainloop()


if __name__ == "__main__":
    main()
