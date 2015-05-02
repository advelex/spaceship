import math
import pygame
import pdb
import time
import pathlib


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_angle(self):
        return math.degrees(math.atan2(self.x, self.y))

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        m_img_path = pathlib.Path('ship_m.png').resolve()
        s_img_path = pathlib.Path('ship_s.png').resolve()
        self.image_original_m = pygame.image.load(str(m_img_path)).convert()
        self.image_original_m.set_colorkey(Gui.BLACK)
        self.image_original_s = pygame.image.load(str(s_img_path)).convert()
        self.image_original_s.set_colorkey(Gui.BLACK)
        self.image = self.image_original_s
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = 300
        self.s = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.v = pygame.math.Vector2(0, 0)
        self.a = pygame.math.Vector2(0, 0)
        self.up = pygame.math.Vector2(0, -1)        # Direction vector

        self.last_time = time.perf_counter()

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
            self.image = self.rot_center(self.image_original_m, self.v.angle_to(self.up))
        else:
            self.image = self.rot_center(self.image_original_s, self.v.angle_to(self.up))

        current_time = time.perf_counter()
        delta_time = (current_time-self.last_time) * 100
        self.last_time = current_time
        

        self.v += self.a*delta_time
        self.s += self.v*delta_time

        if self.s.x > Gui.WINDOW_SIZE[0]:
            self.s.x = -1
        if self.s.x < -1:
            self.s.x = Gui.WINDOW_SIZE[0]
        if self.s.y > Gui.WINDOW_SIZE[1]:
            self.s.y = -1
        if self.s.y < -1:
            self.s.y = Gui.WINDOW_SIZE[1]

        self.rect.x = self.s.x
        self.rect.y = self.s.y



class Gui:

    WINDOW_SIZE = [800, 600]

    # Colors
    BLACK = (0, 0 ,0)
    WHITE = (255, 255, 255)
    RED   = (255, 0 ,0)

    
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption('Spaceship Simulation')

        self.ship = Player()
        self.a = 0.1
        self.fps = 60
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)
        self.clock = pygame.time.Clock()
        self.gui_running = True

        # acceleration vectors
        self.up    = pygame.math.Vector2(0, -self.a)
        self.down  = pygame.math.Vector2(0, self.a)
        self.left  = pygame.math.Vector2(-self.a, 0)
        self.right = pygame.math.Vector2(self.a, 0)
        self.zero  = pygame.math.Vector2(0, 0)

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.a = self.up
                if event.key == pygame.K_DOWN:
                    self.ship.a = self.down
                if event.key == pygame.K_LEFT:
                    self.ship.a = self.left
                if event.key == pygame.K_RIGHT:
                    self.ship.a = self.right

                if event.key == pygame.K_q:
                    return False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.a = self.zero
                if event.key == pygame.K_DOWN:
                    self.ship.a = self.zero
                if event.key == pygame.K_LEFT:
                    self.ship.a = self.zero
                if event.key == pygame.K_RIGHT:
                    self.ship.a = self.zero
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

        
