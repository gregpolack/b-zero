from pygame.time import get_ticks

class Timer:
    def __init__ (self, duration):
        self.duration = duration
        self.is_active = False
        self.start_time = 0
    
    def activate(self):
        self.is_active = True
        self.start_time = get_ticks()

    def deactivate(self):
        self.is_active = False
        self.start_time = 0
    
    def update(self):
        if self.is_active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                self.deactivate()