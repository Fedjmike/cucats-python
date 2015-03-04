import itertools
import math

from PIL import Image


def invert_left_half(image):
    pixel_rgba_values = image.load()
    width, height = image.size

    extent = itertools.product(
        range(0, math.floor(width/2)), range(0, height))

    for i, j in extent:
        (r, g, b, a) = pixel_rgba_values[i, j]
        pixel_rgba_values[i, j] = (255-r, 255-g, 255-b, a)


with Image.open("cucats-logo.png") as image:
    invert_left_half(image)
    image.save("cucats-logo-half-inverted.png")
