import pygame

class Input(object):

    def __init__(self):
        self.quit = False

    def update(self):
        #Stores all input events(Keybord, mouse, etc.) into the event var and iterates through it
        for event in pygame.event.get():
            #If the user presses the [x]/close window button, set quit to true, which closes application
            if event.type == pygame.QUIT:
                self.quit = True