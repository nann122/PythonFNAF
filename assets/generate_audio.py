import numpy as np
import scipy.io.wavfile as wav
import os
from scipy import signal
import random

# Create directories
os.makedirs('sounds/sfx', exist_ok=True)
os.makedirs('sounds/ambient', exist_ok=True)
os.makedirs('sounds/music', exist_ok=True)


class AudioGenerator:
    def __init__(self):
        self.sample_rate = 44100

    def generate_sine_wave(self, frequency, duration, amplitude=0.5):
        """Generate a sine wave"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        return wave

    def generate_noise(self, duration, color='white'):
        """Generate colored noise"""
        samples = int(self.sample_rate * duration)

        if color == 'white':
            noise = np.random.normal(0, 1, samples)
        elif color == 'pink':
            # Simple pink noise approximation
            white_noise = np.random.normal(0, 1, samples)
            noise = signal.lfilter([1], [1, 0.5], white_noise)

        return noise * 0.1

    def apply_envelope(self, wave, attack=0.1, decay=0.1, sustain=0.7, release=0.2):
        """Apply ADSR envelope to wave"""
        length = len(wave)
        envelope = np.ones(length)

        # Attack
        attack_samples = int(attack * length)
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

        # Decay
        decay_samples = int(decay * length)
        decay_end = attack_samples + decay_samples
        envelope[attack_samples:decay_end] = np.linspace(1, sustain, decay_samples)

        # Release
        release_samples = int(release * length)
        envelope[-release_samples:] = np.linspace(sustain, 0, release_samples)

        return wave * envelope

    def create_jumpscare_sound(self):
        """Create jumpscare sound effect"""
        duration = 1.0

        # Combine multiple frequencies for harsh sound
        wave1 = self.generate_sine_wave(440, duration, 0.3)  # A4
        wave2 = self.generate_sine_wave(550, duration, 0.3)  # C#5
        wave3 = self.generate_sine_wave(660, duration, 0.2)  # E5

        # Add noise for harshness
        noise = self.generate_noise(duration) * 0.5

        combined = wave1 + wave2 + wave3 + noise

        # Sharp attack, quick decay
        combined = self.apply_envelope(combined, 0.01, 0.1, 0.8, 0.3)

        # Normalize
        combined = combined / np.max(np.abs(combined))

        wav.write('sounds/sfx/jumpscare.wav', self.sample_rate,
                  (combined * 32767).astype(np.int16))
        print("✅ Jumpscare sound created")

    def create_footsteps(self):
        """Create footstep sound effects"""
        for i in range(5):  # Create 5 different footstep sounds
            duration = 0.3

            # Low frequency thump with noise
            wave = self.generate_sine_wave(80 + random.randint(-10, 10), duration, 0.6)
            noise = self.generate_noise(duration) * 0.3

            combined = wave + noise
            combined = self.apply_envelope(combined, 0.01, 0.05, 0.3, 0.1)

            # Normalize
            combined = combined / np.max(np.abs(combined))

            wav.write(f'sounds/sfx/footstep_{i + 1}.wav', self.sample_rate,
                      (combined * 32767).astype(np.int16))

        print("✅ Footstep sounds created")

    def create_door_sound(self):
        """Create door closing sound"""
        duration = 1.5

        # Mechanical door sound - descending frequency sweep
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        frequency = 200 * np.exp(-t * 2)  # Exponential decay

        wave = 0.3 * np.sin(2 * np.pi * frequency * t)

        # Add mechanical noise
        noise = self.generate_noise(duration) * 0.2

        combined = wave + noise
        combined = self.apply_envelope(combined, 0.1, 0.2, 0.8, 0.5)

        # Normalize
        combined = combined / np.max(np.abs(combined))

        wav.write('sounds/sfx/door_close.wav', self.sample_rate,
                  (combined * 32767).astype(np.int16))
        print("✅ Door sound created")

    def create_electrical_sounds(self):
        """Create electrical/static sounds"""
        # Light switch sound
        duration = 0.2
        wave = self.generate_sine_wave(1000, duration, 0.4)
        noise = self.generate_noise(duration) * 0.6
        combined = (wave + noise) * 0.5
        combined = self.apply_envelope(combined, 0.01, 0.05, 0.5, 0.1)
        combined = combined / np.max(np.abs(combined))

        wav.write('sounds/sfx/light_switch.wav', self.sample_rate,
                  (combined * 32767).astype(np.int16))

        # Camera static
        duration = 2.0
        static = self.generate_noise(duration, 'pink') * 0.3
        static = self.apply_envelope(static, 0.1, 0, 1.0, 0.1)
        static = static / np.max(np.abs(static))

        wav.write('sounds/sfx/camera_static.wav', self.sample_rate,
                  (static * 32767).astype(np.int16))

        print("✅ Electrical sounds created")

    def create_ambient_sounds(self):
        """Create ambient background sounds"""
        # Electrical hum
        duration = 10.0
        hum1 = self.generate_sine_wave(60, duration, 0.1)  # 60Hz hum
        hum2 = self.generate_sine_wave(120, duration, 0.05)  # Harmonic

        combined = hum1 + hum2

        # Add some variation
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        variation = 0.02 * np.sin(2 * np.pi * 0.1 * t)  # Slow variation
        combined = combined * (1 + variation)

        combined = combined / np.max(np.abs(combined))

        wav.write('sounds/ambient/electrical_hum.wav', self.sample_rate,
                  (combined * 32767).astype(np.int16))

        # Air conditioning
        duration = 8.0
        noise = self.generate_noise(duration, 'pink') * 0.15

        # Add periodic variations (compressor cycling)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        cycle = 0.5 * (1 + 0.3 * np.sin(2 * np.pi * 0.2 * t))

        ac_sound = noise * cycle
        ac_sound = ac_sound / np.max(np.abs(ac_sound))

        wav.write('sounds/ambient/air_conditioning.wav', self.sample_rate,
                  (ac_sound * 32767).astype(np.int16))

        print("✅ Ambient sounds created")

    def create_animatronic_sounds(self):
        """Create animatronic-specific sounds"""
        animatronics = ['freddy', 'bonnie', 'chica', 'foxy']

        for i, name in enumerate(animatronics):
            # Each animatronic gets a different base frequency
            base_freq = 200 + i * 100
            duration = 2.0

            # Mechanical servo sounds
            wave = self.generate_sine_wave(base_freq, duration, 0.3)

            # Add harmonics for more robotic sound
            wave += self.generate_sine_wave(base_freq * 1.5, duration, 0.2)
            wave += self.generate_sine_wave(base_freq * 2, duration, 0.1)

            # Add mechanical noise
            noise = self.generate_noise(duration) * 0.2

            combined = wave + noise
            combined = self.apply_envelope(combined, 0.2, 0.3, 0.6, 0.4)
            combined = combined / np.max(np.abs(combined))

            wav.write(f'sounds/sfx/{name}_movement.wav', self.sample_rate,
                      (combined * 32767).astype(np.int16))

        print("✅ Animatronic sounds created")

    def create_music_box(self):
        """Create simple music box melody (placeholder for Toreador March)"""
        # Simple melody approximation
        notes = [440, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99]  # A-G
        melody = [0, 2, 4, 2, 0, 0, 2, 4, 2, 0]  # Simple pattern

        duration_per_note = 0.5
        total_duration = len(melody) * duration_per_note

        music = np.array([])

        for note_index in melody:
            if note_index < len(notes):
                freq = notes[note_index]
                note_wave = self.generate_sine_wave(freq, duration_per_note, 0.3)

                # Music box timbre - add harmonics
                note_wave += 0.2 * self.generate_sine_wave(freq * 2, duration_per_note, 0.3)
                note_wave += 0.1 * self.generate_sine_wave(freq * 3, duration_per_note, 0.3)

                note_wave = self.apply_envelope(note_wave, 0.01, 0.1, 0.7, 0.2)
                music = np.concatenate([music, note_wave])

        music = music / np.max(np.abs(music))

        wav.write('sounds/music/music_box.wav', self.sample_rate,
                  (music * 32767).astype(np.int16))
        print("✅ Music box melody created")


if __name__ == "__main__":
    generator = AudioGenerator()
    generator.create_jumpscare_sound()
    generator.create_footsteps()
    generator.create_door_sound()
    generator.create_electrical_sounds()
    generator.create_ambient_sounds()
    generator.create_animatronic_sounds()
    generator.create_music_box()
    print("🔊 All audio assets generated successfully!")
