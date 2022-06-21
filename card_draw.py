import random
from PIL import Image

suits = ['C', 'D', 'H', 'S']

suit = random.choice(suits)
number = random.randint(1, 14)

card = suit+str(number)

print(card)

img = Image.open("images/"+card+".png")
img.show()
