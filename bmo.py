import pygame
import random
import glob

WIDTH  = 800
HEIGHT = 600

class MainWindow:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.faces = glob.glob('assets/faces/*.jpg')
        pygame.display.set_caption('BMO ♥')
		
    def _setRandomFace(self):
        face = self.faces[random.randint(0, len(self.faces) - 1)]
        self.display.blit(pygame.image.load(face), (0,0))
		
    def run(self):
        self._setRandomFace()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

if __name__ == '__main__':
    mw = MainWindow()
    mw.run()
    pygame.quit()
    quit()
