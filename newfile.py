import pygame
from time import sleep
from random import randint

# Initialize Pygame
pygame.init()

# Set the window size
hi="Snakes and Ladders"
screen = pygame.display.set_mode((400, 300))

# Run the game loop
background_image=pygame.image.load("image.jpg")
font = pygame.font.Font(None, 36)
image=pygame.transform.scale(background_image,[720,720])
running = True
#text_surface1= font.render(hi, True, (0, 0, 0))
#text_surface2 = font.render(hi, True, (0, 0, 0))
a=243
b=50
roll=0
ra = None
button_color = (0, 255 ,0)  # Blue
button_x, button_y = 500, 1000 # Position
button_width, button_height = 150, 150  # Size
while running:
    sleep(0.05)
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 100))
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    text_surface1 = font.render(hi, True, (0, 0, 0))
    text_surface2 = font.render("ROLL", True, (100, 0, 100))
    screen.blit(text_surface1,(a,b))
    screen.blit(text_surface2,(543,1060))
    if ra!=None:
        text_surface3 = font.render(str(ra), True, (100, 0, 100))
        screen.blit(text_surface3,(243,1060))
        pygame.display.flip()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        """elif True or event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):
            	print("hi")
            	ra=randint(1,6)"""
    # Update game state
    
    
    # Draw the screen
        #while True:
# Clean up
pygame.quit()
