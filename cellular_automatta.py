import pygame
from sys import exit
# import numpy as np

width = 600
height = 600
pygame.init()

#screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cellular Automatta System') 

# used to limit the frame rate
clock = pygame.time.Clock()

# surface = pygame.image.load('./background.jpg')
surface = pygame.Surface((600, 600))
surface.fill("White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

    # draw elements
    screen.blit(surface, (0,0))
    

    # update things
    pygame.display.update()
    # limits fps
    clock.tick(60)














































# # Simulation parameters
# width, height = 500, 500
# n_iterations = 100
# cell_size = 5
# size = (width, height)
# # Initialize the grid
# grid = np.zeros((width // cell_size, height // cell_size), dtype=np.int8)

# def game_of_life_rule(grid, x, y):
#     # Count the number of living neighbors
#     n_neighbors = np.sum(grid[x-1:x+2, y-1:y+2]) - grid[x, y]
#     # Apply the Game of Life rule
#     if grid[x, y] == 1 and n_neighbors in [2, 3]:
#         return 1
#     elif grid[x, y] == 0 and n_neighbors == 3:
#         return 1
#     else:
#         return 0

# # Run the simulation
# pygame.init()
# screen = pygame.display.set_mode(size)
# for i in range(n_iterations):
#     # Update the grid
#     new_grid = np.zeros_like(grid)
#     for x in range(1, grid.shape[0]-1):
#         for y in range(1, grid.shape[1]-1):
#             new_grid[x, y] = game_of_life_rule(grid, x, y)
#     grid = new_grid
#     # Draw the grid
#     screen.fill((255, 255, 255))
#     for x in range(grid.shape[0]):
#         for y in range(grid.shape[1]):
#             if grid[x, y] == 1:
#                 pygame.draw.rect(screen, (0, 0, 0),
#                                  (x*cell_size, y*cell_size, cell_size, cell_size))
#     pygame.display.flip()
#     # Wait for a short time to slow down the simulation
#     pygame.time.wait(50)
# pygame.quit()
