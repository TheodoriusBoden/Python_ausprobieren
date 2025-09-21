import random
import time

GREEN = "\033[92m"

# Einmal kurz die Farbe einstellen
print(GREEN + "Du bist ein Hacker!")

while True:
    r = random.randint(0, 1)
    print(r, end="")