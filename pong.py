import pygame

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 100

BALL_WIDTH = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() * 0.9, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() * 0.1 - PLAYER_WIDTH, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "red", (*player_pos, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, "blue", (*player2_pos, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.circle(screen, "white", (*ball_pos, BALL_WIDTH, BALL_WIDTH))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    
    if player_pos.y > screen.get_height() -PLAYER_HEIGHT:
        player_pos.y = screen.get_height() - PLAYER_HEIGHT
    elif player_pos.y < 0:
        player_pos.y = 0

  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += 300 * dt
    
    if player2_pos.y > screen.get_height() -PLAYER_HEIGHT:
        player2_pos.y = screen.get_height() - PLAYER_HEIGHT
    elif player2_pos.y < 0:
        player2_pos.y = 0


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()