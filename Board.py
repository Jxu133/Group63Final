import pygame
from Cell import Cell
from sudoku_generator import generate_sudoku
pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell= None
        self.board_size = min(width, height - 200)

        #fills board
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        if self.difficulty == 'easy':
            values = generate_sudoku(9,30)
        elif self.difficulty == 'medium':
            values = generate_sudoku(9,40)
        elif self.difficulty == 'hard':
            values = generate_sudoku(9,50)
        self.board = values
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = Cell(values[row][col], row, col, screen)
    #Draws Sudoku grid outline with bold lines to differentiate 3x3 boxes. Draws every cell on board
    def draw(self):
        gap = 78
        for i in range(10):
            if i % 3 == 0:
                board_line_width = 3
            else:
                board_line_width = 1
            y_pos = i * gap + 1
            x_pos = i * gap
            pygame.draw.line(self.screen, (0, 0, 0), (0, y_pos), (self.board_size, y_pos), board_line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (x_pos, 0), (x_pos, self.board_size), board_line_width)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()


    #marks cell at row, col in board as selected cell. Once a cell has been selected, user can edit its value or
    #sketched value
    def select(self, row ,col):
        self.selected_cell = (row, col)

    #If a tuple of (x,y) coordinates is within the displayed board,
    #this function returns a tuple of the (row, col) of the cell which was clicked.
    #Otherwise, this function returns None.
    def click(self,x,y):
        if 0 <= x < self.width and 0 <= y < self.height:
            gap_x = self.width // 9
            gap_y = self.height //9
            col = x // gap_x
            row = y // gap_y
            return (row, col)
        return None

    #Clears cell value. NOTE: Users can only remove cell/sketched values made THEMSELVES
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.board[row][col] == 0 and self.cells[row][col] is not None:
                self.cells[row][col].set_sketched_value(0)

    #Sets the sketched value of the current selected cell equal to the user entered value.
    #It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.cells[row][col] is not None:
                self.cells[row][col].set_sketched_value(value)

    #Sets the value of the current selected cell equal to the user entered value.
    #Called when the user presses the Enter key.
    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.cells[row][col] is not None:
                self.cells[row][col].set_cell_value(value)
                self.board[row][col] = value

    #Resets all cells in the board to their original values
    #(0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col] is not None:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)
                self.board[row][col] = 0

    #Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

    #Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col] is not None:
                    self.board[row][col] = self.cells[row][col].value

    #Finds an empty cell and returns its row and col as a tuple (x,y).
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    #Check whether the Sudoku board is solved correctly.
    def check_board(self):
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]
                if value == 0:
                    return False
                # Check row
                if self.board[row].count(value) != 1:
                    return False
                # Check column
                col_values = [self.board[r][col] for r in range(9)]
                if col_values.count(value) != 1:
                    return False
                # Check 3x3 box
                box_start_row = (row // 3) * 3
                box_start_col = (col // 3) * 3
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(self.board[box_start_row + r][box_start_col + c])
                if box.count(value) != 1:
                    return False
        return True