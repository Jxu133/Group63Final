import pygame

pygame.init()

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value=0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if self.value != 0:
            number_font = pygame.font.SysFont("Arial", 10)
            number_text = number_font.render(f"{self.value}", True, grey)
            self.screen.blit(number_text, (self.row,self.col))


