import pygame

# Initialize Pygame
pygame.init()

# Set the window size and create the screen buffer
screen = pygame.display.set_mode((400, 300))

# Create the button surface
button_surface = pygame.Surface((100, 50))
button_surface.fill((0, 255, 0))

# Create the button rect
button_rect = pygame.Rect(150, 120, 100, 50)

# Create the font object
font = pygame.font.Font(None, 86)

# Create the message surface
message_surface = font.render("Button was clicked!", True, (0, 0, 0))

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is hovering over the button
            if button_rect.collidepoint(event.pos):
                button_surface.fill((255, 0, 0))
                screen.blit(message_surface, (300, 400))
        #    else:
             #   button_surface.fill((0, 255, 0))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            if button_rect.collidepoint(event.pos) or True:
                # Draw the message
                screen.blit(message_surface, (300, 400))
                # Draw the button
        screen.fill((255, 255, 255))
        screen.blit(button_surface, button_rect)
       # screen.blit(message_surface, (300, 400))
    
    
    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
