import pygame
from time import sleep
from random import randint
"""import os
os..chdir("")"""

# Initialize Pygame
pygame.init()

# Set the window size
hi="Snakes and Ladders"
screen = pygame.display.set_mode((720,1400))
t1=randint(0,1)
# Run the game loop
background_image=pygame.image.load("image.jpg")
font = pygame.font.Font(None, 36)
image=pygame.transform.scale(background_image,[720,720])
running = True
#text_surface1= font.render(hi, True, (0, 0, 0))
#text_surface2 = font.render(hi, True, (0, 0, 0))
roll=0
ra = None
button_color = (0, 255 ,0) 
button_x, button_y = 500, 1000 
button_width, button_height = 150, 150  # Size
"""def move():
		for x in range(ra):
			sleep(0.300)
		tif p.no%10==0:
			some_plsyer = y=y +10
		elif p.no <100 or p.no <80 or p.no<60 or p.no < 40 or p.no <20 :
			x=x+1"""
#def exi():
	
def pre():
	if t1==0:
		player()
		t1=1
	elif t1==1:
		computer()
		t1=0
def player():
	mouse_x,mouse_y=pygame.mouse.get_pos()
	con= (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height)
	if event.type == pygame.MOUSEBUTTONDOWN :
		button_rect.collidepoint(mouse_pos)
		ra=(1,6)
		print(ra)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         	running=False
    sleep(0.05)
    screen.fill((255, 240, 230))
    screen.blit(image, (0, 100))
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    text_surface1 = font.render(hi, True, (0, 0, 0))
    text_surface2 = font.render("ROLL", True, (100, 0, 100))
    screen.blit(text_surface1,(243,50))
    screen.blit(text_surface2,(543,1060))
        
    if ra!=None:
        text_surface3 = font.render(str(ra), True, (100, 0, 100))
        screen.blit(text_surface3,(243,1060))
    pygame.display.flip()
    
    #	exi()
    # Handle events
  """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif True or event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if   (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):          	if t1 ==1:
            		ra=randint(1,6)
            	move()
            	rc=randint(1,6)"""
        #while True:
# Clean up
pygame.quit()
