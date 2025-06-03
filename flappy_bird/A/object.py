import pygame
import random

# Bird
class Bird:
    def __init__(self):
        self.bird_list = []
        bird_color = random.choice(["red","blue","yellow"])
        for i in range(1,4):
            img = pygame.image.load(f"Assets/Grumpy/{bird_color}{i}.png")
            self.bird_list.append(img)
        self.reset()

    def update(self):
        self.velocity += 0.3

        if self.velocity >= 8:
            self.velocity = 8

        if self.rect.bottom <= 0.80 * HEIGHT:
            self.rect.y += self.velocity

        if self.alive:
            if pygame.mouse.get_pressed()[0]:
                self.jumped = True
                self.velocity -= 7

            self.image = pygame.tranform.pygame.transform.rotate((self.im_list[self.index]), self.degree)
        else:
            if self.rect.bottom <= 0.80 * SCREEN_HEIGHT:
                self.degree -+ 2
            self.image = pygame.tranform.pygame.transform.rotate((self.im_list[self.index]), self.degree)



    def reset(self):
        self.index = 0
        self.image = self.im_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = SCREEN_HEIGHT // 2
        self.counter = 0
        self.vel = 0
        self.jumped = False
        self.alive = True
        self.degree = 0
        self.mid_position = SCREEN_HEIGHT // 2
        self.flap_position = 0
        self.flap_inc 1