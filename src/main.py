import pygame
import games.ludo_king.main as ludo_king


COLORS = {
    'black' : (3, 3, 15)
}

SETTINGS = {
        'bg_clr'      : COLORS['black'],
        'caption'     : 'GAME W/ PYGAME',
        'display_size': {
            'width' : 1000,
            'height': 700
        }
}

ATTR = {
    
}

ludo_king_icon = 'img/ludo_king_icon.png'


def get_current_game(game):
    games = dict(
        ludo_king=ludo_king,
    )
    return games[game]


def get_elm(game, pos, event):
    for name, elm in game.click_REGISTOR.items():
        if elm.collidepoint(pos):
            if GAMES[game.NAME][event][name] == 'CONTROL':
                print(GAMES['CONTROL'][name])
                break

            print(GAMES[game.NAME][event][name]())
            break


def game_loop():
    running = True
    curr_GAME = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and not curr_GAME:
                
                if ludo_king_rect.collidepoint(event.pos):
                    curr_GAME = get_current_game('ludo_king')
                    curr_GAME.draw_board(game_display)
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN and curr_GAME:        
                get_elm(curr_GAME, event.pos, 'MOUSEBUTTONDOWN')
            
        pygame.display.update()



GAMES = {
    'ludo_king': ludo_king.EVENTS,
    
    'CONTROL': {
        'back_btn'  : 'must draw start screen',
        'replay_btn': 'start game again'
    }
}

def draw_start_screen():
    pass
        
if __name__ == '__main__':
    pygame.init()
    
    game_display = pygame.display.set_mode((
        SETTINGS['display_size']['width'],
        SETTINGS['display_size']['height']
    ))
    
    ludo_king_main_icon = pygame.image.load(ludo_king_icon).convert_alpha()
    ludo_king_rect = ludo_king_main_icon.get_rect(topleft = (365, 236))
    
    pygame.display.set_caption(SETTINGS['caption'])
    clock = pygame.time.Clock()
    
    
    game_display.fill(COLORS['black'])
    game_display.blit(ludo_king_main_icon, (365, 236))
    
    game_loop()
    
    pygame.quit()
    quit()