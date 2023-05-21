import pygame
from modules.classes import MainMenu, NewGameScreen, LoadGame, Player

class Main:
    def __init__(self):
        pygame.init()

        # Set up the game window
        win_width = 1280
        win_height = 720
        self.win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Yoda Stories")

        # Initialize game objects
        self.main_menu = MainMenu(self.win)
        self.new_game_screen = NewGameScreen(self.win, self.main_menu.menu_music)
        self.load_game = LoadGame()

    def run(self):
        # Play the menu music on a loop
        self.main_menu.menu_music.play(loops=-1)

        # Create the game loop
        game_running = True
        frame_index = 0
        while pygame.get_init() and game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu.button_newgame_rect.collidepoint(event.pos):
                        self.new_game_screen.start()

                    elif self.main_menu.button_loadgame_rect.collidepoint(event.pos):
                        self.load_game.select_save_file()

                    elif self.main_menu.button_options_rect.collidepoint(event.pos):
                        print("Options clicked!")

                    elif self.main_menu.button_quit_rect.collidepoint(event.pos):
                        game_running = False

            if pygame.get_init():
                # Draw the background
                self.win.blit(self.main_menu.background_frames[frame_index], (0, 0))
                frame_index = (frame_index + 1) % len(self.main_menu.background_frames)

                # Draw the logo image onto the screen
                self.win.blit(self.main_menu.logo_img, (self.win.get_width() // 2 - self.main_menu.logo_img.get_width() // 2, 0))

                # Draw the menu buttons onto the screen
                self.win.blit(self.main_menu.button_newgame_img, self.main_menu.button_newgame_rect)
                self.win.blit(self.main_menu.button_loadgame_img, self.main_menu.button_loadgame_rect)
                self.win.blit(self.main_menu.button_options_img, self.main_menu.button_options_rect)
                self.win.blit(self.main_menu.button_quit_img, self.main_menu.button_quit_rect)

                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()

                # Check if the mouse is hovering over any menu option
                if self.main_menu.button_newgame_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.win, (255, 255, 0), self.main_menu.button_newgame_rect, 3)
                elif self.main_menu.button_loadgame_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.win, (255, 255, 0), self.main_menu.button_loadgame_rect, 3)
                elif self.main_menu.button_options_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.win, (255, 255, 0), self.main_menu.button_options_rect, 3)
                elif self.main_menu.button_quit_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.win, (255, 255, 0), self.main_menu.button_quit_rect, 3)

                # Update the screen
                pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    print("Yoda Stories - Powered by PyYoda")
    print("Version 0.0.1 - 5/21/2023")
    print("Copyright (c) 2023 - Lucasfilm Ltd. and The Walt Disney Company")
    print("This is free software, and you are welcome to redistribute it under certain conditions.")
    print("See the LICENSE file for details.")

    game = Main()
    game.run()