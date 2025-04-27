import pygame

pygame.init()
black = (0, 0, 0)
gray = (105,105,105)
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
            number_font = pygame.font.SysFont("Arial", 40)
            number_text = number_font.render(f"{self.value}", True, black)
            self.screen.blit(number_text, ((self.col) * 78 +30,(self.row) * 78 + 20))
        elif self.sketched_value != 0:
            number_font = pygame.font.SysFont("Arial", 20)
            number_text = number_font.render(f"{self.value}", True, gray)
            self.screen.blit(number_text, ((self.col) * 78 + 5, (self.row) * 78 + 3))


