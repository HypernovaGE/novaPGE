import pygame

pygame.init()

class Object:
    def __init__(self):
        pass

    def update(self, event, deltatime):
        pass

    def draw(self, screen: pygame.Surface):
        pass

class Scene:
    def __init__(self):
        self.color: pygame.Color = pygame.Color(113, 199, 245)
        self.objects: list[Object] = []

    def update(self, events, deltatime):
        for gameobject in self.objects:
            for event in events:
                gameobject.update(event, deltatime)

    def draw(self, screen: pygame.Surface):
        screen.fill(self.color)
        for gameobject in self.objects:
            gameobject.draw(screen)
    
    def regist_object(self, gameobject: Object):
        self.objects.append(gameobject)

        return self

class Game:
    def __init__(self):
        self.screen_size: tuple = (960, 640)
        self.is_running: bool = True

        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_size)
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.scenes: list[Scene] = []

    def run(self):
        while self.is_running:
            dt = self.clock.tick(100) / 1000
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            for scene in self.scenes:
                scene.update(events, dt)
            for scene in self.scenes:
                scene.draw(self.screen)
                        
            pygame.display.update()
    
    def regist_scene(self, scene: Scene):
        self.scenes.append(scene)

        return self