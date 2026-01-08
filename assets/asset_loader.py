import os
import pygame

class AssetLoader:
    def __init__(self):
        self.sounds = {}
        self.base_sound_path = "assets/sounds"
        self.generated_path = "assets/generated"

    def load_all_assets(self):
        pygame.mixer.init()
        self._load_sounds_from_folder(self.base_sound_path)
        self._load_sounds_from_folder(self.generated_path)

    def _load_sounds_from_folder(self, folder):
        if not os.path.exists(folder):
            return

        for file in os.listdir(folder):
            if file.endswith(".wav"):
                path = os.path.join(folder, file)
                self.sounds[file] = pygame.mixer.Sound(path)

    def load_generated_sound(self, path):
        filename = os.path.basename(path)
        self.sounds[filename] = pygame.mixer.Sound(path)
