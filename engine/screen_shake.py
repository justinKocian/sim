import random

class ScreenShake:
    def __init__(self):
        self.duration = 0
        self.max_intensity = 0
        self.elapsed = 0

    def trigger(self, duration=0.5, intensity=5):
        self.duration = duration
        self.max_intensity = intensity
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt

    def get_offset(self):
        if self.elapsed < self.duration:
            t = self.elapsed / self.duration
            falloff = 1 - t  # linear fade
            intensity = int(self.max_intensity * falloff)
            return (
                random.randint(-intensity, intensity),
                random.randint(-intensity, intensity)
            )
        return (0, 0)
