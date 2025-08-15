import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Colors
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# Ball properties
ball_radius = 30
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_color = random_color()
ball_speed_x = 5
ball_speed_y = 4

# Clock
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
        ball_color = random_color()
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_color = random_color()

    # Draw
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()