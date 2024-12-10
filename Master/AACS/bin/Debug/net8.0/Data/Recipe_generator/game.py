import pygame
import random

class NPC:
  def __init__(self, name, dialogue):
    self.name = name
    self.dialogue = dialogue
    self.current_line = 0

  def speak(self):
    return self.dialogue[self.current_line]

  def next_line(self):
    self.current_line += 1

player_x = 100
player_y = 100

npc = NPC('Bob', ['Hello there!', 'What brings you here?', 'Let\'s go on an adventure!'])

screen = pygame.display.set_mode((600, 400))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((255, 255, 255))
  pygame.draw.circle(screen, (0, 0, 255), (player_x, player_y), 20)

  text = npc.speak()
  font = pygame.font.Font(None, 36)
  text_surface = font.render(text, True, (0, 0, 0))
  text_rect = text_surface.get_rect(center=(300, 200))
  screen.blit(text_surface, text_rect)

  pygame.display.flip()

pygame.quit()