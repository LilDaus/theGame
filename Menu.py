import os
import pygame
import pygame_menu

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((600, 400))



def start_the_game():

    print('Do the job here !')


menu = pygame_menu.Menu(height=300,
                        width=400,
                        theme=pygame_menu.themes.THEME_BLUE,
                        title='Welcome')

menu.add_text_input('Quang')
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
