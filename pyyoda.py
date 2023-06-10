import pygame
from modules.menu import MainMenu, NewGame, LoadGame
from modules.settings import Settings

class PyYoda:
    def __init__(self):
        pygame.init()

        # Set up the game window
        game_settings = Settings("settings.json")
        fullscreen = game_settings.settings["fullscreen"]
        screen_info = pygame.display.Info()
        win_width = screen_info.current_w if fullscreen else game_settings.settings["window_width"]
        win_height = screen_info.current_h if fullscreen else game_settings.settings["window_height"]
        self.win = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Yoda Stories - PyYoda")

        # Initialize game objects
        self.main_menu = MainMenu(self.win)
        self.new_game_screen = NewGame(self.win, self.main_menu.menu_music, game_settings)
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
                    self.handle_mouse_click(event.pos)

            if pygame.get_init():
                frame_index = frame_index + 1
                frame_index = frame_index % len(self.main_menu.background_frames)
                self.update_display(frame_index)

        pygame.quit()


    def handle_mouse_click(self, pos):
        buttons = [
            (self.main_menu.button_newgame_rect, NewGame.print),
            (self.main_menu.button_loadgame_rect, self.load_game.select_save_file),
            (self.main_menu.button_options_rect, lambda: print("Options clicked!")),
            (self.main_menu.button_quit_rect, pygame.quit)
        ]
        for button_rect, action in buttons:
            if button_rect.collidepoint(pos):
                action()

    def update_display(self, frame_index):
        # Draw the background
        self.win.blit(self.main_menu.background_frames[frame_index], (0, 0))

        # Draw the logo image onto the screen
        logo_pos_x = self.win.get_width() // 2 - self.main_menu.logo_img.get_width() // 2
        self.win.blit(self.main_menu.logo_img, (logo_pos_x, 0))

        # Draw the menu buttons onto the screen
        menu_buttons = [
            (self.main_menu.button_newgame_img, self.main_menu.button_newgame_rect),
            (self.main_menu.button_loadgame_img, self.main_menu.button_loadgame_rect),
            (self.main_menu.button_options_img, self.main_menu.button_options_rect),
            (self.main_menu.button_quit_img, self.main_menu.button_quit_rect)
        ]
        for button_img, button_rect in menu_buttons:
            self.win.blit(button_img, button_rect)

        # Check if the mouse is hovering over any menu option
        mouse_pos = pygame.mouse.get_pos()
        for button_rect in self.main_menu.button_rects:
            if button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.win, (255, 255, 0), button_rect, 3)

        # Update the screen
        pygame.display.update()

if __name__ == '__main__':
    print("Yoda Stories - Powered by PyYoda")
    print("Version 0.0.1 - 5/21/2023")
    print("Copyright (c) 2023 - Lucasfilm Ltd. and The Walt Disney Company")
    print("This is free software, and you are welcome to redistribute it under certain conditions.")
    print("See the LICENSE file for details.")
    
    game = PyYoda()
    game.run()