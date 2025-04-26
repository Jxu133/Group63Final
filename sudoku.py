import pygame, sys
from sudoku_generator import generate_sudoku
from Board import Board
from Cell import Cell

pygame.init()


def main():
    #variable declarations:
    window_width = 900
    window_height = 900
    grid_size = 9
    white = (255, 255, 255)
    green = (0, 255, 0)
    yellow =(255, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    Title_font = pygame.font.SysFont("Times New Roman", 72)
    font = pygame.font.SysFont("Arial", 36)

    #scren settings
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("UF Sudoku!")

    start_screen = 0
    game_screen = 1
    win_screen = 2
    lose_screen = 3
    current_screen = start_screen
    board = None #this will be created when a difficulty is chosen

    easy_rect = pygame.Rect(window_width//2 - 100, 300, 200, 60)
    medium_rect = pygame.Rect(window_width//2 - 100, 400, 200, 60)
    hard_rect = pygame.Rect(window_width//2 - 100, 500, 200, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_screen == start_screen:
                if event.type == pygame.MOUSEBUTTONDOWN: #checks which difficulty is chosen
                    if easy_rect.collidepoint(event.pos):
                        board = Board(window_width,window_height,screen,'easy')
                        current_screen = game_screen
                    elif medium_rect.collidepoint(event.pos):
                        board = Board(window_width, window_height, screen, 'medium')
                        current_screen = game_screen
                    elif hard_rect.collidepoint(event.pos):
                        board =  Board(window_width, window_height, screen, 'hard')
                        current_screen = game_screen


        #renders start screen
        screen.fill(white)
        if current_screen == start_screen:
            #renders title text
            title = Title_font.render("UF SUDOKU!", True, black)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, 150))


            #easy button
            pygame.draw.rect(screen, green, easy_rect, 2)
            easy_option_text = font.render("EASY", True, green)
            screen.blit(easy_option_text, (easy_rect.centerx - easy_option_text.get_width() // 2,
                                           easy_rect.centery - easy_option_text.get_height() // 2))

            #medium button
            pygame.draw.rect(screen, yellow, medium_rect, 2)
            medium_option_text = font.render("MEDIUM", True, yellow)
            screen.blit(medium_option_text, (medium_rect.centerx - medium_option_text.get_width() // 2, medium_rect.centery - medium_option_text.get_height() // 2))

            #hard
            pygame.draw.rect(screen, red, hard_rect, 2)
            hard_option_text = font.render("HARD", True, red)
            screen.blit(hard_option_text, (hard_rect.centerx - hard_option_text.get_width() // 2, hard_rect.centery - hard_option_text.get_height() // 2))

        elif current_screen == game_screen:
            board.draw()

        elif current_screen == win_screen:
            win_text = Title_font.render("Congratulations smarty pants! You Won!!!", True, green)



        pygame.display.update()


if __name__ == "__main__":
    main()