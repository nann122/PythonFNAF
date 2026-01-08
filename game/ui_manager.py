import pygame
from config import *


class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

        # Button rectangles
        self.left_door_button = pygame.Rect(50, 600, 100, 50)
        self.left_light_button = pygame.Rect(160, 600, 100, 50)
        self.camera_button = pygame.Rect(540, 600, 100, 50)
        self.right_light_button = pygame.Rect(920, 600, 100, 50)
        self.right_door_button = pygame.Rect(1030, 600, 100, 50)

        # Camera selection buttons
        self.camera_buttons = {}
        x_start, y_start = 50, 200
        for i, location in enumerate(CAMERA_LOCATIONS.keys()):
            x = x_start + (i % 4) * 120
            y = y_start + (i // 4) * 40
            self.camera_buttons[location] = pygame.Rect(x, y, 110, 30)

    def render_power_display(self, power_system):
        """Render power indicator"""
        power_percentage = power_system.get_power_percentage()

        # Power bar background
        power_bg = pygame.Rect(50, 50, 300, 30)
        pygame.draw.rect(self.screen, BLACK, power_bg)
        pygame.draw.rect(self.screen, WHITE, power_bg, 2)

        # Power bar fill
        fill_width = int((power_percentage / 100) * 296)
        power_fill = pygame.Rect(52, 52, fill_width, 26)
        color = power_system.get_power_bar_color()
        pygame.draw.rect(self.screen, color, power_fill)

        # Power text
        power_text = self.font_medium.render(f"POWER: {power_percentage:.1f}%", True, WHITE)
        self.screen.blit(power_text, (360, 50))

    def render_time_display(self, current_hour):
        """Render current time"""
        hour_display = current_hour if current_hour > 0 else 12
        am_pm = "AM"
        time_text = self.font_medium.render(f"TIME: {hour_display}:00 {am_pm}", True, WHITE)
        self.screen.blit(time_text, (SCREEN_WIDTH - 200, 50))

    def render_control_buttons(self, left_door_closed, right_door_closed,
                               left_light_on, right_light_on, camera_active):
        """Render control interface buttons"""

        # Left door button
        color = RED if left_door_closed else GREEN
        pygame.draw.rect(self.screen, color, self.left_door_button)
        pygame.draw.rect(self.screen, WHITE, self.left_door_button, 2)
        text = self.font_small.render("L DOOR", True, WHITE)
        text_rect = text.get_rect(center=self.left_door_button.center)
        self.screen.blit(text, text_rect)

        # Left light button
        color = YELLOW if left_light_on else DARK_GRAY
        pygame.draw.rect(self.screen, color, self.left_light_button)
        pygame.draw.rect(self.screen, WHITE, self.left_light_button, 2)
        text = self.font_small.render("L LIGHT", True, WHITE)
        text_rect = text.get_rect(center=self.left_light_button.center)
        self.screen.blit(text, text_rect)

        # Camera button
        color = BLUE if camera_active else DARK_GRAY
        pygame.draw.rect(self.screen, color, self.camera_button)
        pygame.draw.rect(self.screen, WHITE, self.camera_button, 2)
        text = self.font_small.render("CAMERA", True, WHITE)
        text_rect = text.get_rect(center=self.camera_button.center)
        self.screen.blit(text, text_rect)

        # Right light button
        color = YELLOW if right_light_on else DARK_GRAY
        pygame.draw.rect(self.screen, color, self.right_light_button)
        pygame.draw.rect(self.screen, WHITE, self.right_light_button, 2)
        text = self.font_small.render("R LIGHT", True, WHITE)
        text_rect = text.get_rect(center=self.right_light_button.center)
        self.screen.blit(text, text_rect)

        # Right door button
        color = RED if right_door_closed else GREEN
        pygame.draw.rect(self.screen, color, self.right_door_button)
        pygame.draw.rect(self.screen, WHITE, self.right_door_button, 2)
        text = self.font_small.render("R DOOR", True, WHITE)
        text_rect = text.get_rect(center=self.right_door_button.center)
        self.screen.blit(text, text_rect)

    def render_camera_selection(self, camera_system):
        """Render camera selection interface"""
        if not camera_system.is_camera_up:
            return

        # Camera selection panel
        panel_rect = pygame.Rect(30, 180, 500, 200)
        pygame.draw.rect(self.screen, DARK_GRAY, panel_rect)
        pygame.draw.rect(self.screen, WHITE, panel_rect, 2)

        title = self.font_medium.render("SELECT CAMERA", True, WHITE)
        self.screen.blit(title, (panel_rect.x + 10, panel_rect.y + 10))

        # Camera buttons
        for location, button_rect in self.camera_buttons.items():
            if location == camera_system.current_camera:
                pygame.draw.rect(self.screen, BLUE, button_rect)
            else:
                pygame.draw.rect(self.screen, DARK_GRAY, button_rect)
            pygame.draw.rect(self.screen, WHITE, button_rect, 1)

            text = self.font_small.render(location.upper(), True, WHITE)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)

    def render_jumpscare(self, animatronic_name):
        """Render jumpscare screen"""
        # Fill screen with red
        jumpscare_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        jumpscare_surface.fill(RED)
        jumpscare_surface.set_alpha(200)
        self.screen.blit(jumpscare_surface, (0, 0))

        # Jumpscare text
        jumpscare_text = self.font_large.render(f"{animatronic_name.upper()}", True, WHITE)
        text_rect = jumpscare_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(jumpscare_text, text_rect)

        # Game over text
        game_over_text = self.font_medium.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(game_over_text, text_rect)

    def render_victory_screen(self, night_number):
        """Render victory screen"""
        victory_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        victory_surface.fill(GREEN)
        victory_surface.set_alpha(150)
        self.screen.blit(victory_surface, (0, 0))

        victory_text = self.font_large.render(f"NIGHT {night_number} COMPLETE!", True, WHITE)
        text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(victory_text, text_rect)

        continue_text = self.font_medium.render("Press SPACE to continue", True, WHITE)
        text_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(continue_text, text_rect)

    def handle_click(self, pos, camera_system):
        """Handle mouse clicks on UI elements"""
        clicked_element = None

        if self.left_door_button.collidepoint(pos):
            clicked_element = "left_door"
        elif self.left_light_button.collidepoint(pos):
            clicked_element = "left_light"
        elif self.camera_button.collidepoint(pos):
            clicked_element = "camera"
        elif self.right_light_button.collidepoint(pos):
            clicked_element = "right_light"
        elif self.right_door_button.collidepoint(pos):
            clicked_element = "right_door"

        # Camera selection
        if camera_system.is_camera_up:
            for location, button_rect in self.camera_buttons.items():
                if button_rect.collidepoint(pos):
                    camera_system.switch_camera(location)

        return clicked_element
