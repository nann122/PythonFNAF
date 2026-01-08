import pygame
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

# Create directories
os.makedirs('images/backgrounds', exist_ok=True)
os.makedirs('images/animatronics', exist_ok=True)
os.makedirs('images/ui', exist_ok=True)
os.makedirs('images/cameras', exist_ok=True)


class ImageGenerator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.Surface((1280, 720))

    def create_security_room_background(self):
        """Create security room background"""
        img = Image.new('RGB', (1280, 720), (20, 20, 30))
        draw = ImageDraw.Draw(img)

        # Draw desk
        draw.rectangle([0, 500, 1280, 720], fill=(40, 30, 20))

        # Draw monitor bezels
        draw.rectangle([200, 100, 1000, 450], fill=(10, 10, 10))
        draw.rectangle([210, 110, 990, 440], fill=(0, 0, 0))

        # Control panel
        draw.rectangle([50, 580, 1230, 680], fill=(60, 60, 70))

        # Buttons
        buttons = [(100, 620), (200, 620), (580, 620), (960, 620), (1080, 620)]
        for x, y in buttons:
            draw.rectangle([x - 40, y - 20, x + 40, y + 20], fill=(100, 100, 100))

        img.save('images/backgrounds/security_room.png')
        print("✅ Security room background created")

    def create_animatronic_sprites(self):
        """Create simple animatronic sprites"""
        animatronics = {
            'freddy': (139, 69, 19),  # Brown
            'bonnie': (88, 41, 156),  # Purple
            'chica': (255, 255, 0),  # Yellow
            'foxy': (200, 50, 50)  # Red
        }

        for name, color in animatronics.items():
            # Normal sprite
            img = Image.new('RGBA', (200, 300), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Body
            draw.ellipse([50, 50, 150, 200], fill=color)
            # Head
            draw.ellipse([60, 20, 140, 100], fill=color)
            # Eyes (glowing white dots)
            draw.ellipse([75, 40, 90, 55], fill=(255, 255, 255))
            draw.ellipse([110, 40, 125, 55], fill=(255, 255, 255))
            # Eye pupils (black)
            draw.ellipse([80, 45, 85, 50], fill=(0, 0, 0))
            draw.ellipse([115, 45, 120, 50], fill=(0, 0, 0))

            img.save(f'images/animatronics/{name}.png')

            # Jumpscare sprite (larger, distorted)
            jumpscare_img = img.resize((400, 600))
            jumpscare_img = jumpscare_img.filter(ImageFilter.BLUR)
            jumpscare_img.save(f'images/animatronics/{name}_jumpscare.png')

        print("✅ Animatronic sprites created")

    def create_camera_feeds(self):
        """Create camera feed backgrounds"""
        locations = {
            'show_stage': (100, 50, 150),
            'dining_area': (80, 80, 60),
            'pirate_cove': (60, 30, 30),
            'supply_closet': (40, 40, 40),
            'backstage': (50, 50, 30),
            'kitchen': (90, 70, 40),
            'west_hall': (30, 30, 50),
            'east_hall': (50, 30, 30)
        }

        for location, color in locations.items():
            img = Image.new('RGB', (800, 450), color)
            draw = ImageDraw.Draw(img)

            # Add some basic shapes for atmosphere
            if location == 'show_stage':
                # Stage curtains
                draw.rectangle([100, 50, 200, 400], fill=(150, 0, 0))
                draw.rectangle([600, 50, 700, 400], fill=(150, 0, 0))
                # Stage
                draw.rectangle([200, 350, 600, 400], fill=(139, 69, 19))

            elif location == 'dining_area':
                # Tables
                for i in range(3):
                    for j in range(2):
                        x, y = 150 + i * 200, 200 + j * 100
                        draw.ellipse([x, y, x + 80, y + 80], fill=(100, 70, 40))

            elif location == 'pirate_cove':
                # Curtain
                draw.rectangle([300, 0, 500, 450], fill=(100, 0, 100))

            # Add static grain effect
            for _ in range(100):
                x, y = np.random.randint(0, 800), np.random.randint(0, 450)
                brightness = np.random.randint(0, 50)
                color_with_grain = tuple(max(0, min(255, c + brightness)) for c in color)
                draw.rectangle([x, y, x + 2, y + 2], fill=color_with_grain)

            img.save(f'images/cameras/{location}.png')

        print("✅ Camera feed backgrounds created")

    def create_ui_elements(self):
        """Create UI elements"""
        # Power bar segments
        for i in range(10):
            img = Image.new('RGBA', (30, 20), (0, 255, 0, 255))
            img.save(f'images/ui/power_segment_{i}.png')

        # Button states
        button_states = {
            'button_off': (100, 100, 100),
            'button_on': (0, 255, 0),
            'button_active': (255, 255, 0),
            'button_danger': (255, 0, 0)
        }

        for state, color in button_states.items():
            img = Image.new('RGB', (100, 50), color)
            draw = ImageDraw.Draw(img)
            draw.rectangle([5, 5, 95, 45], outline=(255, 255, 255), width=2)
            img.save(f'images/ui/{state}.png')

        # Static overlay
        static_img = Image.new('RGBA', (800, 450), (0, 0, 0, 0))
        draw = ImageDraw.Draw(static_img)

        for _ in range(1000):
            x, y = np.random.randint(0, 800), np.random.randint(0, 450)
            alpha = np.random.randint(50, 200)
            color = np.random.choice([(255, 255, 255), (0, 0, 0)])
            draw.rectangle([x, y, x + 1, y + 1], fill=color + (alpha,))

        static_img.save('images/ui/static_overlay.png')

        print("✅ UI elements created")


if __name__ == "__main__":
    generator = ImageGenerator()
    generator.create_security_room_background()
    generator.create_animatronic_sprites()
    generator.create_camera_feeds()
    generator.create_ui_elements()
    print("🎨 All image assets generated successfully!")
