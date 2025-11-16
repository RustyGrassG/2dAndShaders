import pygame
import sys

class Base(object):

    def __init__(self, screenSize=[512,512]):
        pygame.init()

        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        #Sets the screen rendering attributes
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE)
        
        #initializes the screen/window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        #sets the window caption
        pygame.display.set_caption("Graphics Window")

        #Determines if main loop is still active
        self.running = True
        #sets clock for time-related events
        self.clock = pygame.time.Clock()

    
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        
        self.initialize()

        #Runs app
        while self.running:

            self.update()

            ##Render##
            #displays image on screen
            pygame.display.flip()

            #Pause, if necessary, to achieve 60 FPS
            self.clock.tick(60)
        
        ##shutdown##
        pygame.quit()
        sys.exit()
