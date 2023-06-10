# menu.py

import pygame
from modules.settings import Settings
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
        
        button_width, button_height = self.button_newgame_img.get_size()
        button_x = self.win.get_width() // 2 - button_width // 2
        button_y = self.logo_img.get_height() + 50
        button_spacing = 5
        
        self.button_newgame_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        self.button_loadgame_rect = pygame.Rect(button_x, button_y + button_height + button_spacing, button_width, button_height)
        self.button_options_rect = pygame.Rect(button_x, button_y + 2 * (button_height + button_spacing), button_width, button_height)
        self.button_quit_rect = pygame.Rect(button_x, button_y + 3 * (button_height + button_spacing), button_width, button_height)
        
        self.button_rects = [
            self.button_newgame_rect,
            self.button_loadgame_rect,
            self.button_options_rect,
            self.button_quit_rect
        ]
        
        self.menu_music = pygame.mixer.Sound("data/sounds/theme.ogg")
        self.menu_music.set_volume(0.5)
        
        self.background_frames = [
            pygame.transform.scale(
                pygame.image.load(f"data/images/starfield/frame_{i}.png"), 
                self.win.get_size()
            ) for i in range(108)
        ]

class NewGame:
    def __init__(self, win, menu_music, settings):
        pass
    def print():
        print("New Game Selected!")
    
class LoadGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0, '-topmost', True)
        self.root.overrideredirect(True)
        self.root.withdraw()

    def select_save_file(self):
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Save Files", "*.sav")])
        if file_path:
            print(f"Selected save file: {file_path}")
            # Perform further actions with the selected save file
        else:
            print("No save file selected.")
