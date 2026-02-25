import pygame
import pge


class Square(pge.Object):
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = 200

    def handle_event(self, event, dt):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("K_SPACE")

    def handle_keys(self, keys, dt):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:   dx -= 1
        if keys[pygame.K_RIGHT]:  dx += 1
        if keys[pygame.K_UP]:     dy -= 1
        if keys[pygame.K_DOWN]:   dy += 1

        self.rect.x += dx * self.speed * dt
        self.rect.y += dy * self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


scene = pge.Scene()
square = Square(400, 300, 50, pygame.Color('red'))
scene.regist_object(square)

game = pge.Game().regist_scene(scene)
game.run()