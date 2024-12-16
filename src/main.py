import pygame


display_width  = 1000
display_height = 700

black  = (3, 3, 15)

ludo_king_icon = 'img/ludo_king_icon.png'

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                ludo_king_rect = ludo_king.get_rect(topleft = (365, 236))
                if ludo_king_rect.collidepoint(event.pos):
                    print('show ludo king board')
            
        pygame.display.update()

            
if __name__ == '__main__':
    pygame.init()
    
    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('GAME W/ PYGAME')
    clock = pygame.time.Clock()

    ludo_king = pygame.image.load(ludo_king_icon).convert_alpha()
    
    game_display.fill(black)
    game_display.blit(ludo_king, (365, 236))
    
    game_loop()
    
    pygame.quit()
    quit()