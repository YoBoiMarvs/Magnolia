import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import time
import sys

pygame.mixer.init()
pygame.mixer.music.load("magnolia.mp3")
pygame.mixer_music.play()
print()

lyrics = {
    "Wrecking balls and million stones": [1, 0.1, 0.3, 0.1, 0.1],
    "Will never take away": [0.5, 0, 0.5, 0.3],
    "My strongest will to say": [1.5, 0.1, 0.1, 0.5, 0],
    "The words you long to hear": [1.5, 0.1, 0.1, 0.1, 0.3, 0],
    "":[0],
    "The city's falling down and down": [2, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1],
    "This very old long way": [0.5, 0.1, 0.1, 0.5, 0.1],
    "I don't need to say more": [1.5, 0.1, 0.1, 0.1, 0.5, 0.1],
    "The words you long to hear ": [1.5, 0.1, 0.1, 0.1, 0.3, 0],
    "end": [67]
}



def type_line(line, delays, char_delay):
    words = line.split()
    for i, word in enumerate(words):
        if i < len(delays):
            time.sleep(delays[i])
        for char in word:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write(" ")          
        sys.stdout.flush()
    print()


for key, value in lyrics.items():
    type_line(key, value,0.075)

print()
