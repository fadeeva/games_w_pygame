import pygame

SETTINGS = {
        'board': 'games/ludo_king/img/board.svg',
        'bg_clr': (201, 184, 167),
        'caption': 'Ludo King'
}


def draw_board(game_display):
    board_img = SETTINGS['board']
    
    board = pygame.image.load(board_img)

    pygame.display.set_caption(SETTINGS['caption'])
    game_display.fill(SETTINGS['bg_clr'])
    game_display.blit(board, (218, 60))