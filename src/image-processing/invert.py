import itertools
import math

# View documentation for the Image module at:
# http://effbot.org/imagingbook/image.htm
from PIL import Image


def invert_left_half(image):
    pixel_rgba_values = image.load()
    width, height = image.size

    extent = itertools.product(
        range(0, math.floor(width/2)), range(0, height))

    for i, j in extent:
        (r, g, b, a) = pixel_rgba_values[i, j]
        pixel_rgba_values[i, j] = (255-r, 255-g, 255-b, a)


with Image.open("img/cucats-logo.png") as image:
    invert_left_half(image)
    image.save("img/cucats-logo-half-inverted.png")


# Exercises
# ---------
#
# 1) Crop the CUCaTS logo, to get rid of the text.
#
# 2) Try using a different input image. Something will go wrong if you
#    don't use a png with transparency. What goes wrong and how can you
#    fix it?
#
# 3) Try blurring an image.
