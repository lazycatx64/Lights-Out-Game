
import tkinter as tk
from tkinter import messagebox

import random

TITLE = 'Lights Out Game' 
ROW_SIZE = 5    
COL_SIZE = 5    

class LightsOutGame:
    
    row_size = ROW_SIZE
    col_size = COL_SIZE
    
    def __init__( self, master ):
        self.master = master
        
        self.toggle_mode = tk.BooleanVar( value=False )
        
        self.do_create_size_input()
        self.do_create_control()
        self.do_create_gameblocks()
        self.do_reset_game()



    def do_create_size_input( self ):
        
        # Frame for checkboxes and buttons
        self.frame_size = tk.Frame( self.master, padx=10, pady=10, borderwidth=2, relief="ridge" )
        self.frame_size.grid( row=0, column=0, columnspan=ROW_SIZE+3 )
        
        # Entry for rows
        self.rows_label = tk.Label( self.frame_size, text="Rows:" )
        self.rows_label.grid( row=0, column=0 )
        self.rows_input = tk.Entry( self.frame_size, width=5 )
        self.rows_input.grid( row=0, column=1 )
        self.rows_input.insert( 0, ROW_SIZE )

        # Entry for columns
        self.cols_label = tk.Label( self.frame_size, text="Cols:" )
        self.cols_label.grid( row=0, column=2 )
        self.cols_input = tk.Entry( self.frame_size, width=5 )
        self.cols_input.grid( row=0, column=3 )
        self.cols_input.insert( 0, COL_SIZE )

        
        
    def do_create_control( self ):
        
        # Frame for checkboxes and buttons
        self.frame_control = tk.Frame( self.master, padx=10, pady=10, borderwidth=2, relief="ridge" )
        self.frame_control.grid( row=1, column=0, columnspan=self.row_size+3 )
        
        # Toggle Mode checkbox
        self.button_toggle_mode = tk.Checkbutton(
                self.frame_control,
                text="Flip Single",
                variable=self.toggle_mode,
                command=self.do_update_mode,
            )
        self.button_toggle_mode.grid( row=1, column=0 )

        # Reset Button
        self.button_reset_game = tk.Button(
                self.frame_control, text="Reset", command=self.do_reset_game
            )
        self.button_reset_game.grid( row=1, column=1 )

        
        
    def do_create_gameblocks( self ):
        
        # Frame for game blocks
        self.frame_gameblocks = tk.Frame( self.master, padx=10, pady=10, borderwidth=2, relief="ridge" )
        self.frame_gameblocks.grid( row=2, column=0, columnspan=self.row_size+1 )
        
        # Game Blocks
        self.button_gameblocks = [
            [
                tk.Button(
                    self.frame_gameblocks,
                    width=4,
                    height=2,
                    command=lambda i=i, j=j: self.do_toggle_light( i, j ),
                )
                for j in range( self.col_size )
            ]
            for i in range( self.row_size )
        ]
        for i in range( self.row_size ):
            for j in range( self.col_size ):
                self.button_gameblocks[i][j].grid( row=i, column=j )



    def do_toggle_light( self, i, j ):
        
        # Toggle clicked block
        self.board[i][j] = 1 - self.board[i][j]
        
        # Also toggle neighbors
        if self.toggle_mode.get() == False:
            self.do_toggle_neighbors( i, j )

        self.do_update_blocks()
        
        if all( light == 0 for row in self.board for light in row ):
            messagebox.showinfo( 'Congratulations!', 'You solved the puzzle!' )



    def do_toggle_neighbors( self, i, j ):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.row_size and 0 <= nj < self.col_size:
                self.board[ni][nj] = 1 - self.board[ni][nj]



    def do_update_mode( self ):
        # Update the toggle mode when the checkbox is clicked
        self.toggle_mode.set( True if self.toggle_mode.get() == False else False )
        self.button_toggle_mode.toggle()



    def do_update_blocks( self ):
        for i in range( self.row_size ):
            for j in range( self.col_size ):
                if self.board[i][j] == 1:
                    self.button_gameblocks[i][j].config( bg="black" )
                else:
                    self.button_gameblocks[i][j].config( bg="white" )



    def do_reset_game( self ):
        self.row_size = int(self.rows_input.get())
        self.col_size = int(self.cols_input.get())
        self.frame_gameblocks.destroy()
        self.do_create_gameblocks()
        self.board = [ [random.choice([0, 1]) for _ in range(self.col_size)] for _ in range(self.row_size) ]
        self.do_update_blocks()



def main():
    master = tk.Tk()
    master.title( TITLE )
    game = LightsOutGame( master )
    master.mainloop()
    


if __name__ == "__main__":
    main()
