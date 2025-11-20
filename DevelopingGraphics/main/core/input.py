import pygame

class Input(object):

    def __init__(self):
        self.quit = False
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []

    def update(self):
        self.keyDownList = []
        self.keyUpList = []

        #Stores all input events(Keybord, mouse, etc.) into the event var and iterates through it
        for event in pygame.event.get():

            #If the user presses the [x]/close window button, set quit to true, which closes application
            if event.type == pygame.QUIT:
                self.quit = True
            
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name( event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)
        
    
    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList
    def isKeyPressed(self, keyCode):
        return keyCode in self.keyPressedList
    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList