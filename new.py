import pygame

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("သံကျမှ လှုပ်မယ်")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

# Load and play music
pygame.mixer.music.load("music.mp3")  # သင့် music file နာမည်ကို ထည့်ပါ
pygame.mixer.music.play(-1)  # Loop forever

# Player setup
player_pos = pygame.Rect(375, 275, 50, 50)
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Only allow movement while music is playing
    if pygame.mixer.music.get_busy():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos.x -= speed
        if keys[pygame.K_RIGHT]:
            player_pos.x += speed
        if keys[pygame.K_UP]:
            player_pos.y -= speed
        if keys[pygame.K_DOWN]:
            player_pos.y += speed

    # Draw player
    pygame.draw.rect(screen, BLUE, player_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
