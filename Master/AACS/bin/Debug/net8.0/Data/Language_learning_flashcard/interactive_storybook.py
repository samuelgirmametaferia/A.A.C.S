import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Player character
player_x = 50
player_y = 50
player_size = 20

# Story world map (example)
map = [
    ["wall", "wall", "wall", "wall", "wall"],
    ["wall", "empty", "empty", "empty", "wall"],
    ["wall", "empty", "player", "empty", "wall"],
    ["wall", "empty", "empty", "empty", "wall"],
    ["wall", "wall", "wall", "wall", "wall"]
]

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# A* pathfinding algorithm (simplified)
def find_path(start, goal):
  # ... (implementation for A* pathfinding)

# Game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Handle player movement
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    player_y += UP[1]
  if keys[pygame.K_DOWN]:
    player_y += DOWN[1]
  if keys[pygame.K_LEFT]:
    player_x += LEFT[0]
  if keys[pygame.K_RIGHT]:
    player_x += RIGHT[0]

  # Keep player within map bounds
  player_x = max(0, min(player_x, width - player_size))
  player_y = max(0, min(player_y, height - player_size))

  # Draw the game world
  screen.fill((0, 0, 0))  # Clear the screen
  for row in map:
    for col in row:
      if col == "wall":
        pygame.draw.rect(screen, (255, 255, 255), (col * 50, row * 50, 50, 50))
      elif col == "player":
        pygame.draw.circle(screen, (0, 255, 0), (player_x, player_y), player_size)

  pygame.display.flip()

pygame.quit()