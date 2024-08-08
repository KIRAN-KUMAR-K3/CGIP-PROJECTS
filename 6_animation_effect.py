import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Effects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

num_objects = 10
objects = []

for _ in range(num_objects):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 30)
    color = random.choice([RED, GREEN, BLUE])
    speed_x = random.randint(-5, 5)
    speed_y = random.randint(-5, 5)
    objects.append({"x": x, "y": y, "radius": radius, "color": color, "speed_x": speed_x, "speed_y": speed_y})

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for obj in objects:
        obj["x"] += obj["speed_x"]
        obj["y"] += obj["speed_y"]

        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > screen_width:
            obj["speed_x"] = -obj["speed_x"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > screen_height:
            obj["speed_y"] = -obj["speed_y"]

        pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["radius"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
