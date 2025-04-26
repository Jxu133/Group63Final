# import pygame
# from Cell import cell
# from sudoku_generator import sudoku_maker

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell= None
    #Draws Sudoku grid outline with bold lines to differentiate 3x3 boxes. Draws every cell on board
    def draw(self):
        pass

    #marks cell at row, col in board as selected cell. Once a cell has been selected, user can edit its value or
    #sketched value
    def select(self, row ,col):
        pass

    #If a tuple of (x,y) coordinates is within the displayed board,
    #this function returns a tuple of the (row, col) of the cell which was clicked.
    #Otherwise, this function returns None.
    def click(self,x,y):
        pass

    #Clears cell value. NOTE: Users can only remove cell/sketched values made THEMSELVES
    def clear(self):
        pass

    #Sets the sketched value of the current selected cell equal to the user entered value.
    #It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        pass

    #Sets the value of the current selected cell equal to the user entered value.
    #Called when the user presses the Enter key.
    def place_number(self, value):
        pass

    #Resets all cells in the board to their original values
    #(0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        pass

    #Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        pass

    #Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        pass

    #Finds an empty cell and returns its row and col as a tuple (x,y).
    def find_empty(self):
        pass

    #Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass
