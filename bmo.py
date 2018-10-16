import random
import glob
import pygame

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BMO_COLOR = (128, 230, 209)


class MainWindow:
    def __init__(self):
        self.bmo_face = True
        pygame.init()
        self.display = pygame.display.set_mode(
            (WIDTH, HEIGHT), pygame.RESIZABLE)
        self.faces = glob.glob('assets/faces/*.jpg')
        pygame.display.set_caption('BMO ♥')

    def _set_random_face(self):
        face = self.faces[random.randint(0, len(self.faces) - 1)]
        self.display.blit(pygame.image.load(face), (0, 0))

    def _set_text(self):
        w, h = pygame.display.get_surface().get_size()
        self.font = pygame.font.SysFont("Times New Roman", 100)
        self.text = self.font.render("Hello Finn", False, BLACK)
        text_w, text_h = self.font.size("Hello Finn")
        self.display.fill(BMO_COLOR)
        self.display.blit(self.text, ((w - text_w) / 2, (h - text_h) / 2))

    def _left_mouse_pressed(self):
        return pygame.mouse.get_pressed()[0]

    def _toggle_display(self):
        if self.bmo_face:
            self._set_text()
        else:
            self._set_random_face()
        self.bmo_face = not self.bmo_face

    def run(self):
        self._set_random_face()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if self._left_mouse_pressed():
                    self._toggle_display()
                if event.type == pygame.QUIT:
                    return


if __name__ == '__main__':
    mw = MainWindow()
    mw.run()
    pygame.quit()
    quit()
