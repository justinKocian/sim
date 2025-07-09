# audio.py
import pygame

class AudioController:
    def __init__(self):
        pygame.mixer.init()
        self.music_volume = 0.5
        self.sfx_volume = 0.7
        self.current_track = None

    def play_music(self, filepath, loop=True):
        if self.current_track != filepath:
            pygame.mixer.music.load(filepath)
            self.current_track = filepath
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def set_music_volume(self, volume):
        self.music_volume = max(0.0, min(volume, 1.0))
        pygame.mixer.music.set_volume(self.music_volume)

    def play_sound(self, filepath):
        sound = pygame.mixer.Sound(filepath)
        sound.set_volume(self.sfx_volume)
        sound.play()

    def set_sfx_volume(self, volume):
        self.sfx_volume = max(0.0, min(volume, 1.0))
