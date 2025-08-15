import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bouncing Balls Animation")

# Clock
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, radius=30):
        self.radius = radius
        self.x = random.randint(radius, WIDTH - radius)
        self.y = random.randint(radius, HEIGHT - radius)
        self.color = self.random_color()
        self.speed_x = random.choice([4, 5, 6])
        self.speed_y = random.choice([4, 5, 6])

    def random_color(self):
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def move(self, screen_width, screen_height):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x = -self.speed_x
            self.color = self.random_color()
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y
            self.color = self.random_color()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


# Create multiple balls
balls = [Ball() for _ in range(5)]  # 5 balls; increase for more fun

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # Move and draw balls
    screen.fill((0, 0, 0))  # Clear screen
    for ball in balls:
        ball.move(WIDTH, HEIGHT)
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
