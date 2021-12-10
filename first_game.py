# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1024, 768])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((100, 125, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.draw.polygon(screen, (150, 0, 255), [(250, 250), (250, 350), (250, 100), (350, 350)])
    pygame.draw.rect(screen, (150, 100, 255), pygame.Rect(30, 30, 60, 60))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()