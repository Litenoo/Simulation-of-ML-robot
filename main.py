from env.environment import Environment
from world.grid_loader import World
import argparse
import time

def main(headless=False):
    world = World.load_png("./world/grid1.png")

    if headless:
        pass
    else:
        from render.pygame_view import PygameView
        view = PygameView(world)

    running = True
    while running:
        if not headless:
            running = view.update(world)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()

    main(headless=args.headless)