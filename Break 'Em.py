import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10
PADDLE_SPEED = 10
BALL_SPEED = [5, 5]
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
BRICK_ROWS = 4
BRICK_COLS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RAINBOW_COLORS = [
    (255, 0, 0),     # Red
    (255, 127, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (75, 0, 130),    # Indigo
    (148, 0, 211)    # Violet
]

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rainbow Breakout')

# Initialize paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initialize ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Initialize ball direction
ball_dx, ball_dy = BALL_SPEED

# Create bricks arranged in a triangle shape
bricks = []
start_x = (WIDTH - BRICK_WIDTH * BRICK_COLS) // 2  # Center the triangle horizontally

for row in range(BRICK_ROWS):
    num_bricks = BRICK_COLS - row  # Decrease the number of bricks each row
    row_start_x = start_x + (BRICK_WIDTH // 2) * row  # Shift each row inward to center the triangle

    for col in range(num_bricks):
        brick = pygame.Rect(row_start_x + col * BRICK_WIDTH, 50 + row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.left += PADDLE_SPEED

    # Update ball position
    ball.x += ball_dx
    ball.y += ball_dy

    # Check for collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Check for collision with paddle
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Check for collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_dy = -ball_dy
            bricks.remove(brick)

    # Check if ball missed the paddle
    if ball.bottom > HEIGHT:
        running = False  # Game over

    # Clear the screen
    screen.fill(BLACK)

    # Draw bricks with rainbow colors
    for i, brick in enumerate(bricks):
        color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        pygame.draw.rect(screen, color, brick)

    # Draw paddle and ball
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    pygame.time.delay(30)

# Quit the game
pygame.quit()
