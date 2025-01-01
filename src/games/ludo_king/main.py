import pygame


COLORS = {
    'beige': (201, 184, 167),
    'light beige': (229, 219, 207),
    'dark beige': (160, 146, 135),
    'black': (35, 31, 32)
}

SETTINGS = {
        'bg_clr': COLORS['beige'],
        'caption': 'Ludo King',
}

ATTR = {
    'board': 'games/ludo_king/img/board.svg',
    'circle': 'games/ludo_king/img/circle.svg',
    'dice': 'games/ludo_king/img/dice.svg',
}


def draw_board(game_display):
    pygame.display.set_caption(SETTINGS['caption'])
    game_display.fill(SETTINGS['bg_clr'])
    
    board = pygame.image.load(ATTR['board'])
    game_display.blit(board, (218, 60))
    
    circle = pygame.image.load(ATTR['circle'])
    game_display.blit(circle, (63, 125))
    game_display.blit(circle, (841, 483))
    
    dice = pygame.image.load(ATTR['dice'])
    game_display.blit(dice, (80, 141))
    game_display.blit(dice, (858, 497))
    
    