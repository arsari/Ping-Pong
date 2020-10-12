import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# window setup
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 193, 7)
RED = (244, 67, 54)
GREEN = (76, 175, 80)
TEAL = (0, 150, 136)
size = (1000, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
scoreA = 0
scoreB = 0
message = "Press X for exit"

# paddles player A
paddleA = Paddle(RED, 10, 75)
paddleA.rect.x = 20
paddleA.rect.y = 150

# paddles player B
paddleB = Paddle(GREEN, 10, 75)
paddleB.rect.x = 970
paddleB.rect.y = 450

# ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 500
ball.rect.y = 325

# sprites list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# main loop
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    # key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    # ball bouncing
    if ball.rect.x >= 990:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 640:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    # game court setup
    screen.fill(BLACK)
    pygame.draw.line(screen, TEAL, [500, 0], [500, 630], 5)
    all_sprites_list.draw(screen)

    # score setup
    font = pygame.font.Font(None, 75)
    text = font.render(str(scoreA), 1, YELLOW)
    screen.blit(text, (400, 10))
    text = font.render(str(scoreB), 1, YELLOW)
    screen.blit(text, (565, 10))

    # bottom message setup
    footer = pygame.font.Font(None, 20)
    text = footer.render(str(message), 1, YELLOW)
    screen.blit(text, (450, 635))

    # draw screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
