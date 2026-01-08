import pygame
import sys
from game.game_manager import GameManager
from config import *


class PizzaNights:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pizza Nights - Horror Survival")
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize game manager
        self.game_manager = GameManager(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.game_manager.handle_event(event)

    def update(self, dt):
        self.game_manager.update(dt)

    def render(self):
        self.screen.fill(BLACK)
        self.game_manager.render()
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds

            self.handle_events()
            self.update(dt)
            self.render()

            if self.game_manager.should_quit:
                self.running = False

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = PizzaNights()
    game.run()
