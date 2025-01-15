import pygame
import games.ludo_king.main as ludo_king


curr_GAME = '' # some govnocode

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
    'ludo_king_icon': pygame.image.load('img/ludo_king_icon.png'),
}

click_REGISTOR = {}

def get_current_game(game):
    games = dict(
        ludo_king=ludo_king,
    )
    return games[game]


def get_elm(game, pos, event):
    for name, elm in game.click_REGISTOR.items():
        if elm.collidepoint(pos):
            if GAMES[game.NAME][event][name] == 'CONTROL':
                GAMES['CONTROL'][name]()
                break

            print(GAMES[game.NAME][event][name](name))
            break


def game_loop():
    running = True
    global curr_GAME
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and not curr_GAME:
                
                if click_REGISTOR['ludo_king_icon'].collidepoint(event.pos):
                    curr_GAME = get_current_game('ludo_king')
                    curr_GAME.draw_board(game_display)
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN and curr_GAME:        
                get_elm(curr_GAME, event.pos, 'MOUSEBUTTONDOWN')
            
        pygame.display.update()


def draw_start_screen():
    global curr_GAME
    curr_GAME = ''
    
    pygame.display.set_caption(SETTINGS['caption'])
    clock = pygame.time.Clock()
    
    game_display.fill(COLORS['black'])
    game_display.blit(ATTR['ludo_king_icon'], (365, 236))
    click_REGISTOR['ludo_king_icon'] = ATTR['ludo_king_icon'].get_rect(topleft = (365, 236))
    

GAMES = {
    'ludo_king': ludo_king.EVENTS,
    
    'CONTROL': {
        'back_btn'  : draw_start_screen,
    }
}


if __name__ == '__main__':
    pygame.init()
    
    game_display = pygame.display.set_mode((
        SETTINGS['display_size']['width'],
        SETTINGS['display_size']['height']
    ))

    draw_start_screen()

    game_loop()
    
    pygame.quit()
    quit()