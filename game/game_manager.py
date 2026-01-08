import pygame
import random
from .power_system import PowerSystem
from .animatronics import AIDirector
from .camera_system import CameraSystem
from .audio_manager import AudioManager
from .ui_manager import UIManager
from config import *


class GameManager:
    def __init__(self, screen):
        self.screen = screen

        # Game systems
        self.power_system = PowerSystem()
        self.ai_director = AIDirector()
        self.camera_system = CameraSystem()
        self.audio_manager = AudioManager()
        self.ui_manager = UIManager(screen)

        # Game state
        self.current_night = 1
        self.current_hour = 0  # 0 = 12 AM, 5 = 6 AM
        self.hour_timer = 0
        self.game_state = "playing"  # playing, game_over, victory, power_out
        self.should_quit = False

        # Control states
        self.left_door_closed = False
        self.right_door_closed = False
        self.left_light_on = False
        self.right_light_on = False
        self.light_timer = 0
        self.max_light_duration = 3.0

        # Jumpscare
        self.jumpscare_timer = 0
        self.jumpscare_duration = 3.0
        self.jumpscare_animatronic = None

        # Power outage
        self.power_out_timer = 0
        self.power_out_duration = 5.0

    def handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.game_state == "victory":
                self.start_next_night()
            elif event.key == pygame.K_r and self.game_state == "game_over":
                self.restart_night()
            elif event.key == pygame.K_ESCAPE:
                self.should_quit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                clicked = self.ui_manager.handle_click(event.pos, self.camera_system)
                self.handle_control_input(clicked)

    def handle_control_input(self, control):
        """Handle control inputs"""
        if self.game_state != "playing":
            return

        if control == "left_door":
            self.left_door_closed = not self.left_door_closed
            self.audio_manager.play_sound('door_close', 0.5)

        elif control == "right_door":
            self.right_door_closed = not self.right_door_
