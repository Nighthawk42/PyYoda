# classes.py - This contains our Python Classes for the game.

import pygame, sys, os, random, math
import tkinter as tk
from tkinter import filedialog

# Main Menu Classes.
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

class NewGameScreen:
    def __init__(self, win, menu_music):
        self.win = win
        self.screen_width = win.get_width()
        self.screen_height = win.get_height()
        self.menu_music = menu_music

    def start(self):
        pygame.init()  # Initialize Pygame's video system
        self.menu_music.stop()  # Stop the menu music
        self.draw_blank_screen()

        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

            pygame.display.update()

        pygame.quit()  # Quit Pygame

    def draw_blank_screen(self):
        self.win.fill((0, 0, 0))  # Fill the screen with black

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

# Gameplay classes. 
class Player:
    class Player(pygame.sprite.Sprite):
        def __init__(self,pos,groups):
            super().__init__(groups)