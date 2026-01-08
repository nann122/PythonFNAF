import pygame
import random


class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_playing = False
        self.ambient_channel = None

        # Load sounds (placeholder - replace with actual sound files)
        try:
            # self.sounds['footsteps'] = pygame.mixer.Sound('assets/sounds/footsteps.wav')
            # self.sounds['door_close'] = pygame.mixer.Sound('assets/sounds/door.wav')
            # self.sounds['jumpscare'] = pygame.mixer.Sound('assets/sounds/jumpscare.wav')
            pass  # Placeholder for actual sound loading
        except:
            print("Warning: Sound files not found. Running in silent mode.")

    def play_sound(self, sound_name, volume=1.0):
        """Play a sound effect"""
        if sound_name in self.sounds:
            sound = self.sounds[sound_name]
            sound.set_volume(volume)
            sound.play()

    def play_ambient(self, sound_name, volume=0.3, loop=-1):
        """Play ambient background sound"""
        if sound_name in self.sounds:
            if self.ambient_channel:
                self.ambient_channel.stop()
            self.ambient_channel = self.sounds[sound_name].play(loop)
            self.ambient_channel.set_volume(volume)

    def stop_ambient(self):
        """Stop ambient sounds"""
        if self.ambient_channel:
            self.ambient_channel.stop()

    def play_music(self, music_file, volume=0.5, loop=-1):
        """Play background music"""
        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop)
            self.music_playing = True
        except:
            print(f"Warning: Could not load music file: {music_file}")

    def stop_music(self):
        """Stop background music"""
        pygame.mixer.music.stop()
        self.music_playing = False

    def play_power_out_sequence(self):
        """Play the power outage sequence audio"""
        self.stop_ambient()
        # Play Toreador March or similar ominous tune
        # self.play_music('assets/sounds/toreador_march.mp3', volume=0.7, loop=0)

    def play_jumpscare_sound(self, animatronic_name):
        """Play jumpscare sound for specific animatronic"""
        self.play_sound('jumpscare', volume=1.0)
