import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats

# from alien import Alien
import game_functions as gf


def run_game():
    # initialize game and creating a screen object
    #

    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()

    #     alien = Alien(ai_settings, screen)

    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop for the game
    while True:
        # look for key and mouse inputs

        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
