import pygame
import random


NAME = 'ludo_king'

COLORS = {
    'beige'      : (201, 184, 167),
    'light beige': (229, 219, 207),
    'dark beige' : (160, 146, 135),
    'black'      : (35, 31, 32)
}

SETTINGS = {
        'bg_clr' : COLORS['beige'],
        'caption': 'Ludo King',
}

ATTR = {
    'board'      : pygame.image.load('games/ludo_king/img/board.svg'),
    'circle'     : pygame.image.load('games/ludo_king/img/circle.svg'),
    'dice'       : pygame.image.load('games/ludo_king/img/dice.svg'),
    'yel_chip'   : pygame.image.load('games/ludo_king/img/yellow_chip.svg'),
    'red_chip'   : pygame.image.load('games/ludo_king/img/red_chip.svg'),
    'back_btn'   : pygame.image.load('games/ludo_king/img/btn_arrow_back.svg'),
    'replay_btn' : pygame.image.load('games/ludo_king/img/btn_arrow_replay.svg'),
    'game_icon'  : pygame.image.load('games/ludo_king/img/icon_game.png'),
}

click_REGISTOR = {}


def get_elm_by_click(pos):
    pass


def throw_dice():
    return random.choice(range(1, 7))


def draw_board(game_display):
    pygame.display.set_caption(SETTINGS['caption'])
    game_display.fill(SETTINGS['bg_clr'])
    
    game_display.blit(ATTR['board'], (218, 60))
    
    game_display.blit(ATTR['circle'], (63, 125))
    
    game_display.blit(ATTR['circle'], (841, 483))
    click_REGISTOR['circle'] = ATTR['circle'].get_rect(topleft=(841, 483))
    
    game_display.blit(ATTR['dice'], (80, 141))
    game_display.blit(ATTR['dice'], (858, 497))
    
    game_display.blit(ATTR['yel_chip'], (591, 435))
    click_REGISTOR['yel_chip_1'] = ATTR['yel_chip'].get_rect(topleft=(591, 435))
    game_display.blit(ATTR['yel_chip'], (648, 435))
    click_REGISTOR['yel_chip_2'] = ATTR['yel_chip'].get_rect(topleft=(648, 435))
    game_display.blit(ATTR['yel_chip'], (591, 492))
    click_REGISTOR['yel_chip_3'] = ATTR['yel_chip'].get_rect(topleft=(591, 492))
    game_display.blit(ATTR['yel_chip'], (648, 492))
    click_REGISTOR['yel_chip_4'] = ATTR['yel_chip'].get_rect(topleft=(648, 492))
    
    game_display.blit(ATTR['red_chip'], (321, 165))
    click_REGISTOR['red_chip_1'] = ATTR['red_chip'].get_rect(topleft=(321, 165))
    game_display.blit(ATTR['red_chip'], (378, 165))
    click_REGISTOR['red_chip_2'] = ATTR['red_chip'].get_rect(topleft=(378, 165))
    game_display.blit(ATTR['red_chip'], (321, 222))
    click_REGISTOR['red_chip_3'] = ATTR['red_chip'].get_rect(topleft=(321, 222))
    game_display.blit(ATTR['red_chip'], (378, 222))
    click_REGISTOR['red_chip_4'] = ATTR['red_chip'].get_rect(topleft=(378, 222))
    
    game_display.blit(ATTR['back_btn'], (936, 22))
    click_REGISTOR['back_btn'] = ATTR['back_btn'].get_rect(topleft=(936, 22))
    game_display.blit(ATTR['replay_btn'], (939, 123))
    click_REGISTOR['replay_btn'] = ATTR['replay_btn'].get_rect(topleft=(939, 123))
    
    game_display.blit(ATTR['game_icon'], (910, 48))
    

EVENTS = {
    'MOUSEBUTTONDOWN': {
        'circle': throw_dice,
    }
}