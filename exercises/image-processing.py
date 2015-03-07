# Hello. Welcome to image processing! :)

# This is a fully functional Python program, annotated with comments to explain
# what's going on. You can click "raw" at the top right of the file in GitHub
# to download the file to your computer.

# First we're going to import two modules which will be useful later in the
# program. These two modules are both part of the "standard library", which
# means that they come by default with every Python installation. Standard
# library imports are conventionally put right at the top of scripts.
import itertools
import math

# We're also going to be using PIL - the Python imaging library. This doesn't
# come with Python by default, so you'll probably have to install it using pip
# before you can run this code. PIL for Python 3 comes in a package called
# Pillow. From the command line, try:
# (Windows:)    python -3 -m pip install Pillow
# (Mac/Linux:)  pip3 install Pillow
# Once PIL is installed (and you've got the cucats logo image file -- see
# below), you should try running this script (the one you're reading) to check
# everything's working.
from PIL import Image
# We've imported the Image module from PIL. You can view its documentation at:
# http://effbot.org/imagingbook/image.htm

# The following function takes a PIL Image object, and inverts its left half.
# Note that the function doesn't "return" anything. It doesn't need to, because
# it modifies the image in-place. (That is, it doesn't make a copy.)
# *Exercise*: Explain how the function works.
def invert_left_half(image):
    pixel_rgba_values = image.load()
    width, height = image.size

    extent = itertools.product(
        range(0, math.floor(width/2)), range(0, height))

    for i, j in extent:
        (r, g, b, a) = pixel_rgba_values[i, j]
        pixel_rgba_values[i, j] = (255-r, 255-g, 255-b, a)

# We're going to read an image file and make an instance of the Image class
# provided my the Image module of PIL. We're going to use the CUCaTS logo
# as our input file. (Download it from cucats.org/r/logo and save it in the
# same folder as this script.) Note that we use the "with" syntax mentioned
# in the presentation.
with Image.open("cucats-logo.png") as image:
    invert_left_half(image)
    image.save("cucats-logo-half-inverted.png")

# Exercises
# =========
# 1) Crop the CUCaTS logo, to get rid of the text. (The PIL documentation will
#    probably be helpful!)
# 2) Try using a different input image. Something will go wrong if you
#    don't use a png with transparency. What goes wrong and how can you
#    fix it?
# 3) Try blurring an image.
