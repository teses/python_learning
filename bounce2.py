import sys, pygame, time

pygame.init()

size = width, height = 800, 480
velocity_x = 0.1
velocity_y = 0
gravity = 0.0005
x = 20
y = 0
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

while 1:
    #time.sleep(0.01)

    # Fenster schliessen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # velocity
    x += velocity_x
    y += velocity_y

    # gravitation
    velocity_y += gravity

    #if x < 0 or x > width:
    #    dx = -dx

    if y < 0 or y > height:
        velocity_y = -velocity_y

    screen.fill(black)
    pygame.draw.circle(screen, white, (x, y), 10)
    pygame.display.flip()
