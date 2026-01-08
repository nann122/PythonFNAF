import pygame
import random
from config import *


class CameraSystem:
    def __init__(self):
        self.current_camera = None
        self.is_camera_up = False
        self.static_timer = 0
        self.static_duration = 0
        self.show_static = False

    def open_camera(self, location=None):
        """Open camera system"""
        self.is_camera_up = True
        if location:
            self.current_camera = location
        else:
            self.current_camera = "show_stage"  # Default camera

    def close_camera(self):
        """Close camera system"""
        self.is_camera_up = False
        self.current_camera = None

    def switch_camera(self, location):
        """Switch to different camera"""
        if self.is_camera_up and location in CAMERA_LOCATIONS:
            self.current_camera = location
            self.trigger_static()

    def trigger_static(self):
        """Add static interference when switching cameras"""
        if random.random() < 0.3:  # 30% chance of static
            self.show_static = True
            self.static_duration = random.uniform(0.5, 2.0)
            self.static_timer = 0

    def update(self, dt):
        """Update camera system"""
        if self.show_static:
            self.static_timer += dt
            if self.static_timer >= self.static_duration:
                self.show_static = False
                self.static_timer = 0

    def render_camera_feed(self, screen, ai_director):
        """Render the current camera view"""
        if not self.is_camera_up or not self.current_camera:
            return

        # Camera background
        camera_rect = pygame.Rect(200, 100, 800, 450)
        pygame.draw.rect(screen, DARK_GRAY, camera_rect)
        pygame.draw.rect(screen, WHITE, camera_rect, 3)

        # Camera label
        font = pygame.font.Font(None, 36)
        label_text = font.render(f"CAM: {self.current_camera.upper()}", True, WHITE)
        screen.blit(label_text, (camera_rect.x + 10, camera_rect.y + 10))

        # Show animatronics at current location
        animatronics = ai_director.get_animatronics_at_location(self.current_camera)

        y_offset = 60
        for animatronic in animatronics:
            animatronic_text = font.render(f"{animatronic.name.upper()} DETECTED", True, RED)
            screen.blit(animatronic_text, (camera_rect.x + 10, camera_rect.y + y_offset))
            y_offset += 40

        # Static overlay
        if self.show_static:
            static_surface = pygame.Surface((camera_rect.width, camera_rect.height))
            static_surface.fill(WHITE)
            static_surface.set_alpha(100)
            screen.blit(static_surface, (camera_rect.x, camera_rect.y))

            # Static noise pattern
            for _ in range(50):
                x = random.randint(camera_rect.x, camera_rect.x + camera_rect.width)
                y = random.randint(camera_rect.y, camera_rect.y + camera_rect.height)
                color = random.choice([BLACK, WHITE, LIGHT_GRAY])
                pygame.draw.circle(screen, color, (x, y), random.randint(1, 3))
