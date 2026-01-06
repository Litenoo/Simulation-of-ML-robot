import pygame

class PygameView:
    def __init__(self, world, scale=1, fps=40):
        pygame.init()
        self.world = world
        self.scale = scale
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.screen = pygame.display.set_mode(
            (world.width*scale, world.height*scale),
            pygame.RESIZABLE
        )
        pygame.display.set_caption("Simulation")


    def update(self, world):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(
                    (event.w, event.h),
                    pygame.RESIZABLE
                )

        for y in range(world.height):
            for x in range(world.width):
                color = (16,19,26) if world.grid[y][x] == 0 else (2,2,2)
                pygame.draw.rect(
                    self.screen,
                    color,
                    (x * self.scale, y * self.scale, self.scale, self.scale)
                )

        dt = self.clock.tick(self.fps)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        
        pygame.display.flip()
        return True