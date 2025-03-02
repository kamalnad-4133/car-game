import pygame
import random

pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
LANES = [100, 200, 300, 400]

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("hard Car Game")

# Load Car
car = pygame.Rect(WIDTH//2 - CAR_WIDTH//2, HEIGHT - CAR_HEIGHT - 20, CAR_WIDTH, CAR_HEIGHT)
obstacles = []
score = 0
speed = 5
obstacle_speed = 7
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.x > 0:
        car.x -= speed
    if keys[pygame.K_RIGHT] and car.x < WIDTH - CAR_WIDTH:
        car.x += speed
    
    # Spawn obstacles
    if random.randint(1, 50) == 1:
        lane = random.choice(LANES)
        obstacles.append(pygame.Rect(lane, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT))
    
    # Move obstacles
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
    
    # Collision Detection
    for obstacle in obstacles:
        if car.colliderect(obstacle):
            print(f"Game Over! Score: {score}")
            running = False
    
    # Draw objects
    pygame.draw.rect(screen, BLUE, car)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)
    
    # Display Score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
