import pygame
class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.image_rect.bottom = (self.screen_rect.bottom)*0.5

        self.bottom = float(self.image_rect.bottom)
        
        self.moving_up = False
        self.moving_down = False

    def blitem(self):
       self.screen.blit(self.image, self.image_rect)
    def update(self):
        if self.moving_up and self.image_rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed

        self.image_rect.bottom = self.bottom