import random
from PIL import Image
from os import listdir

card = Image.open("images/"+random.choice(listdir("images/")))
card.show()
