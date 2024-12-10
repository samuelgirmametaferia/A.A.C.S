import pygame
import pyttsx3

pygame.init()

engine = pyttsx3.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    text_input = input("Enter text to convert to sound: ")
    engine.say(text_input)
    engine.runAndWait()

pygame.quit()