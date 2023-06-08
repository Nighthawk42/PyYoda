# menu.py

import pygame
from pytmx.util_pygame import load_pygame
import tkinter as tk
from tkinter import filedialog

class MainMenu:
    def __init__(self, win):
        self.win = win
        self.logo_img = pygame.image.load("data/images/logo.png")
        self.button_newgame_img = pygame.image.load("data/images/button_newgame.png")
        self.button_loadgame_img = pygame.image.load("data/images/button_loadgame.png")
        self.button_options_img = pygame.image.load("data/images/button_options.png")
        self.button_quit_img = pygame.image.load("data/images/button_quit.png")
        self.button_x = self.win.get_width() // 2 - self.button_newgame_img.get_width() // 2
        self.button_y = self.logo_img.get_height() + 50
        self.button_spacing = 5
        self.button_width = self.button_newgame_img.get_width()
        self.button_height = self.button_newgame_img.get_height()
        self.button_newgame_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        self.button_loadgame_rect = pygame.Rect(self.button_x, self.button_y + self.button_height + self.button_spacing, self.button_width, self.button_height)
        self.button_options_rect = pygame.Rect(self.button_x, self.button_y + 2 * (self.button_height + self.button_spacing), self.button_width, self.button_height)
        self.button_quit_rect = pygame.Rect(self.button_x, self.button_y + 3 * (self.button_height + self.button_spacing), self.button_width, self.button_height)
        self.menu_music = pygame.mixer.Sound("data/sounds/theme.ogg")
        self.menu_music.set_volume(0.5)
        self.background_frames = []

        # Load the background gif frames
        for i in range(108):
            filename = f"data/images/starfield/frame_{i}.png"
            frame = pygame.image.load(filename)
            frame_scaled = pygame.transform.scale(frame, self.win.get_size())
            self.background_frames.append(frame_scaled)

        self.button_rects = [
            self.button_newgame_rect,
            self.button_loadgame_rect,
            self.button_options_rect,
            self.button_quit_rect
        ]

class NewGame:
    def __init__(self, win, menu_music, settings):
        self.win = win
        self.menu_music = menu_music
        self.settings = settings
        self.screen_width = self.settings.window_width
        self.screen_height = self.settings.window_height

    def start(self):
        pass

    def draw_game(self):
        # Clear the screen
        self.win.fill((0, 0, 0))

        # Draw game elements
        # ...

        # Draw other game objects, characters, UI, etc.

        # Add any additional drawing logic specific to Dagobah
    
class LoadGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main tkinter window

    def select_save_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Save Files", "*.sav")])
        if file_path:
            print("Selected save file:", file_path)
            # Perform further actions with the selected save file
        else:
            print("No save file selected.")
