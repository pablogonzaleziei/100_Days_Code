import pygame
import random

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle System")

# Define the Particle class
class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)
        self.life = random.randint(20, 50)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        if self.life <= 0:
            particles.remove(self)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Set up the clock and run the game loop
clock = pygame.time.Clock()
particles = []
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn new particles when the mouse is clicked
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        for i in range(10):
            particles.append(Particle(x, y, random.randint(5, 20)))

    # Update and draw the particles
    for particle in particles:
        particle.update()
        particle.draw(screen)

    # Update the display
    pygame.display.update()

# Quit Pygame when the game loop ends
pygame.quit()
