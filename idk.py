import pygame
from time import sleep
from random import randint
import os
os.chdir(r"Python")
os.chdir("snl")
pygame.init()
hi="Snakes and Ladders"
screen = pygame.display.set_mode((720,1400))
t1=0#randint(0,1)
background_image=pygame.image.load("image.jpg")
player1=pygame.image.load("player_1.png")
player2=pygame.image.load("player_2.png")
font = pygame.font.Font(None, 36)
image=pygame.transform.scale(background_image,[720,720])
p1=pygame.transform.scale(player1,[25,40])
p2=pygame.transform.scale(player2,[70,70])
running = True
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
p1x=20
p1y=770
#def exi():
ho=None
	
def pre(t1):
	if t1==0:
		ra=player()
		return ra#,hj
#		t1=1
"""	elif t1==1:
		computer()
		t1=0"""
def player():
	mouse_x,mouse_y=pygame.mouse.get_pos()
	con= (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height)
	if ho: #event.type == pygame.MOUSEBUTTONDOWN :
		if con:
			button_rect.collidepoint(mouse_x,mouse_y)
			ra=randint(1,6)
			print(ra)
		#	hj=0
			return ra#,hj
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         	running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
         	ho=True
    sleep(1)
    screen.fill((255, 240, 230))
    screen.blit(image, (0, 100))
    button_rect=pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    text_surface1 = font.render(hi, True, (0, 0, 0))
    text_surface2 = font.render("ROLL", True, (100, 0, 100))
    screen.blit(text_surface1,(243,50))
    screen.blit(text_surface2,(543,1060))
    screen.blit(p1,(p1x,p1y))
    ra=pre(t1)
    ho=False
    """if hj==0:
    	ho==False"""
    if True or ra!=None:
        text_surface3 = font.render(str(ra), True, (100, 0, 100))
        screen.blit(text_surface3,(243,1060))
    pygame.display.flip()
pygame.quit()