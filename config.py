import pygame

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (128, 128, 128)

# Game settings
TOTAL_POWER = 100
POWER_DRAIN_BASE = 0.1  # per second
POWER_DRAIN_CAMERA = 0.2
POWER_DRAIN_DOOR = 0.5
POWER_DRAIN_LIGHT = 0.3

HOUR_DURATION = 85  # seconds per in-game hour
TOTAL_HOURS = 6  # 12 AM to 6 AM

# Camera locations
CAMERA_LOCATIONS = {
    'show_stage': (100, 100),
    'dining_area': (300, 150),
    'pirate_cove': (500, 120),
    'supply_closet': (200, 300),
    'backstage': (400, 280),
    'kitchen': (600, 200),
    'west_hall': (150, 450),
    'east_hall': (550, 450)
}

# Animatronic spawn points
ANIMATRONIC_SPAWNS = {
    'freddy': 'show_stage',
    'bonnie': 'show_stage',
    'chica': 'show_stage',
    'foxy': 'pirate_cove'
}
