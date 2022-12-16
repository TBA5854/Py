import pygame


pygame.init()


display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
running =True
while running :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False