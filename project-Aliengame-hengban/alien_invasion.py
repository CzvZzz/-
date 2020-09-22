import sys
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(screen,ai_settings)
    bullets = Group()
    pygame.display.set_caption("aliengame")

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(bullets, ship)

        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()