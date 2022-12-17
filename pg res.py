import pygame

# Initialize pygame
pygame.init()

# Get display information
display_info = pygame.display.Info()

# Get the resolution of the display
display_width = display_info.current_w
display_height = display_info.current_h

# Print the resolution to the console
print(f"Resolution: {display_width}x{display_height}")
