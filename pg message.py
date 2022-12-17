import pygame

# Initialize pygame
pygame.init()

# Set up the game window and display surface
window_size = (720,1600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Game")

# Set up the font
font = pygame.font.Font(None, 36)

# Render the text to a surface
text_surface = font.render("Hello, World!", True, (0, 0, 0))

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the text to the display surface
window.fill((255, 255, 255))
window.blit(text_surface, (50, 50))
    
    # Update the display
pygame.display.update()

# Quit pygame
pygame.quit()
