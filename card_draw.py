import random
from PIL import Image
from os import listdir

suits = ['C', 'D', 'H', 'S']

suit = random.choice(suits)
number = random.randrange(1, 14)

card = suit+str(number)

print(card)

img = Image.open("images/"+card+".png")
img.show()
