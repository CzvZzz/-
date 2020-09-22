import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):

        super().__init__()
        self.screen = screen

        self.bullet_rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.bullet_rect.centery = ship.image_rect.centery
        self.bullet_rect.centerx = ship.image_rect.centerx

        self.x = float(self.bullet_rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.bullet_rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)