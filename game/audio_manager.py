import pygame

class AudioManager:
    def __init__(self, asset_loader):
        self.sounds = asset_loader.sounds
        self.ambient_channel = None

    def play_sound(self, filename, volume=1.0):
        sound = self.sounds.get(filename)
        if sound:
            sound.set_volume(volume)
            sound.play()
        else:
            print(f"⚠️ Sound not found: {filename}")

    def play_generated(self, filename, volume=1.0):
        self.play_sound(filename, volume)

    def play_ambient(self, filename, volume=0.3):
        sound = self.sounds.get(filename)
        if sound:
            if self.ambient_channel:
                self.ambient_channel.stop()
            self.ambient_channel = sound.play(-1)
            self.ambient_channel.set_volume(volume)

    def stop_ambient(self):
        if self.ambient_channel:
            self.ambient_channel.stop()

    def play_jumpscare(self):
        self.play_sound("generated_jumpscare.wav", 1.0)
