import pygame
import json
import os
from PIL import Image


class AssetLoader:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.data = {}

    def load_all_assets(self):
        """Load all game assets"""
        self.load_images()
        self.load_sounds()
        self.load_fonts()
        self.load_data()
        print("🎮 All assets loaded successfully!")

    def load_images(self):
        """Load all image assets"""
        image_paths = [
            'images/backgrounds/security_room.png',
            'images/ui/static_overlay.png'
        ]

        # Load animatronic sprites
        animatronics = ['freddy', 'bonnie', 'chica', 'foxy']
        for name in animatronics:
            image_paths.extend([
                f'images/animatronics/{name}.png',
                f'images/animatronics/{name}_jumpscare.png'
            ])

        # Load camera backgrounds
        cameras = ['show_stage', 'dining_area', 'pirate_cove', 'supply_closet',
                   'backstage', 'kitchen', 'west_hall', 'east_hall']
        for location in cameras:
            image_paths.append(f'images/cameras/{location}.png')

        # Load UI elements
        ui_elements = ['button_off', 'button_on', 'button_active', 'button_danger']
        for element in ui_elements:
            image_paths.append(f'images/ui/{element}.png')

        for path in image_paths:
            if os.path.exists(path):
                try:
                    self.images[os.path.basename(path)] = pygame.image.load(path)
                except pygame.error as e:
                    print(f"⚠️  Could not load image {path}: {e}")
            else:
                print(f"⚠️  Image file not found: {path}")

    def load_sounds(self):
        """Load all sound assets"""
        sound_paths = [
            'sounds/sfx/jumpscare.wav',
            'sounds/sfx/door_close.wav',
            'sounds/sfx/light_switch.wav',
            'sounds/sfx/camera_static.wav',
            'sounds/ambient/electrical_hum.wav',
            'sounds/ambient/air_conditioning.wav',
            'sounds/music/music_box.wav'
        ]

        # Add footstep sounds
        for i in range(1, 6):
            sound_paths.append(f'sounds/sfx/footstep_{i}.wav')

        # Add animatronic sounds
        animatronics = ['freddy', 'bonnie', 'chica', 'foxy']
        for name in animatronics:
            sound_paths.append(f'sounds/sfx/{name}_movement.wav')

        for path in sound_paths:
            if os.path.exists(path):
                try:
                    self.sounds[os.path.basename(path)] = pygame.mixer.Sound(path)
                except pygame.error as e:
                    print(f"⚠️  Could not load sound {path}: {e}")
            else:
                print(f"⚠️  Sound file not found: {path}")

    def load_fonts(self):
        """Load font assets"""

