import math
import pygame
import pdb


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_angle(self):
        return math.degrees(math.atan2(self.x, self.y))

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image_original_m = pygame.image.load("ship_m.png").convert()
        self.image_original_m.set_colorkey(Gui.BLACK)
        self.image_original_s = pygame.image.load("ship_s.png").convert()
        self.image_original_s.set_colorkey(Gui.BLACK)
        self.image = self.image_original_s
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = 300
        self.v = Vector(0, 0)
        self.a = Vector(0, 0)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
        

    def update(self):
        if self.a.x != 0 or self.a.y != 0:
            self.image = self.rot_center(self.image_original_m, self.v.get_angle()+180)
        else:
            self.image = self.rot_center(self.image_original_s, self.v.get_angle()+180)

        self.v.x += self.a.x
        self.v.y += self.a.y
        self.rect.x += self.v.x
        self.rect.y += self.v.y

        if self.rect.x > Gui.WINDOW_SIZE[0]:
            self.rect.x = -1
        if self.rect.x < -1:
            self.rect.x = Gui.WINDOW_SIZE[0]
        if self.rect.y > Gui.WINDOW_SIZE[1]:
            self.rect.y = -1
        if self.rect.y < -1:
            self.rect.y = Gui.WINDOW_SIZE[1]



class Gui:

    WINDOW_SIZE = [800, 600]

    # Colors
    BLACK = (0, 0 ,0)
    WHITE = (255, 255, 255)
    RED = (255, 0 ,0)
    
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption('Spaceship Simulation')

        self.ship = Player()
        self.a = 0.2
        self.fps = 60
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)
        self.clock = pygame.time.Clock()
        self.gui_running = True

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.a.y = -self.a
                if event.key == pygame.K_DOWN:
                    self.ship.a.y = self.a
                if event.key == pygame.K_LEFT:
                    self.ship.a.x = -self.a
                if event.key == pygame.K_RIGHT:
                    self.ship.a.x = self.a

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.a.y = 0
                if event.key == pygame.K_DOWN:
                    self.ship.a.y = 0
                if event.key == pygame.K_LEFT:
                    self.ship.a.x = 0
                if event.key == pygame.K_RIGHT:
                    self.ship.a.x = 0
        return True

    def update_logic(self):
        self.ship.update()

    def update_grafics(self):
        self.screen.fill(self.BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


    def loop(self):

        while self.gui_running:
            
            self.gui_running = self.event_manager()
            self.update_logic()
            self.update_grafics()
            self.clock.tick(self.fps)

        pygame.quit()



def main():
    # pdb.set_trace()
    game = Gui()
    game.loop()

if __name__ == '__main__':
    main()

        
