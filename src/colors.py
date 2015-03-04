import itertools

from PIL import Image


image = Image.open("image.png")
pixels = image.load()

for (i, j) in itertools.product(range(10, 20), range(10, 20)):
    pixels[i, j] = (128, 128, 128)

image.save("output.png")
