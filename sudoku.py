import pygame, sys
from sudoku_generator import generate_sudoku
from Board import Board
from Cell import Cell

pygame.init()


def main():
    #variable declarations:
    window_width = 700
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

    #starting board rects
    easy_rect = pygame.Rect(window_width//2 - 100, 300, 200, 60)
    medium_rect = pygame.Rect(window_width//2 - 100, 400, 200, 60)
    hard_rect = pygame.Rect(window_width//2 - 100, 500, 200, 60)

    #game board rects
    reset_rect = pygame.Rect(50, window_width + 30, 150, 50)
    restart_rect = pygame.Rect(250, window_width + 30, 200, 50)
    quit_rect = pygame.Rect(525, window_width +30 , 150, 50)

    #end screen rect
    end_rect = pygame.Rect(window_width//2 - 100, 500, 200, 60)

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

            elif current_screen == game_screen:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rect.collidepoint(event.pos):
                        board.reset_to_original()
                    elif restart_rect.collidepoint(event.pos):
                        current_screen = start_screen
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    else:
                        position = board.click(*event.pos)
                        if position:
                            board.select(*position)

            elif current_screen == win_screen:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hard_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            elif current_screen == lose_screen:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hard_rect.collidepoint(event.pos):
                        current_screen = start_screen

        #renders start screen
        screen.fill(white)
        if current_screen == start_screen:
            #renders background image
            image = pygame.image.load('images/sudoku_bg.jpg').convert()
            screen.blit(image, (0, 0))


            #renders title text
            title = Title_font.render("UF SUDOKU!", True, black)
            screen.blit(title, (window_width // 2 - title.get_width() // 2, 150))


            #easy button
            pygame.draw.rect(screen, black, easy_rect, 0)
            pygame.draw.rect(screen, green, easy_rect, 2)
            easy_option_text = font.render("EASY", True, green)
            screen.blit(easy_option_text, (easy_rect.centerx - easy_option_text.get_width() // 2,
                                           easy_rect.centery - easy_option_text.get_height() // 2))

            #medium button
            pygame.draw.rect(screen,black,medium_rect, 0)
            pygame.draw.rect(screen, yellow, medium_rect, 2)
            medium_option_text = font.render("MEDIUM", True, yellow)
            screen.blit(medium_option_text, (medium_rect.centerx - medium_option_text.get_width() // 2,
                                             medium_rect.centery - medium_option_text.get_height() // 2))

            #hard
            pygame.draw.rect(screen,black,hard_rect,0)
            pygame.draw.rect(screen, red, hard_rect, 2)
            hard_option_text = font.render("HARD", True, red)
            screen.blit(hard_option_text, (hard_rect.centerx - hard_option_text.get_width() // 2,
                                           hard_rect.centery - hard_option_text.get_height() // 2))

        elif current_screen == game_screen:
            board.draw()

            pygame.draw.rect(screen, yellow, reset_rect)
            reset_text = font.render("RESET", True, black)
            screen.blit(reset_text,(reset_rect.centerx - reset_text.get_width()//2, reset_rect.centery
                                    - reset_text.get_height()//2))

            pygame.draw.rect(screen, green, restart_rect)
            restart_text = font.render("RESTART", True, black)
            screen.blit(restart_text, (restart_rect.centerx -restart_text.get_width()//2, restart_rect.centery -
                        restart_text.get_height()//2))

            pygame.draw.rect(screen, red, quit_rect)
            quit_text = font.render("QUIT", True, black)
            screen.blit(quit_text,(quit_rect.centerx - quit_text.get_width()//2, quit_rect.centery -
                                   quit_text.get_height()//2))

        elif current_screen == win_screen:
            # renders background image
            image = pygame.image.load('images/victory.jpg').convert()
            screen.blit(image, (0, 0))

            #renders win text
            win_text = Title_font.render("Victory! good job :3", True, black)
            screen.blit(win_text, (window_width // 2 - win_text.get_width() // 2, 150))

            #exit button
            pygame.draw.rect(screen, black, end_rect, 3)
            exit_text = font.render("EXIT", True, black)
            screen.blit(exit_text, (end_rect.centerx - exit_text.get_width() // 2,
                                             end_rect.centery - exit_text.get_height() // 2))

        elif current_screen == lose_screen:
            # renders background image
            image = pygame.image.load('images/loss.jpg').convert()
            screen.blit(image, (0, 0))

            # renders loss text
            loss_text = Title_font.render("Game over (╥ ω ╥)", True, black)
            screen.blit(loss_text, (window_width // 2 - loss_text.get_width() // 2, 150))

            # restart button
            pygame.draw.rect(screen, black, end_rect, 3)
            restart_text = font.render("RESTART", True, black)
            screen.blit(restart_text, (end_rect.centerx - restart_text.get_width    () // 2,
                                    end_rect.centery - restart_text.get_height() // 2))



        pygame.display.update()


if __name__ == "__main__":
    main()