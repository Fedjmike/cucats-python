from PIL import Image

print("Opening image...")
img = Image.open("image.jpg")
img = img.convert('RGB')

print("Getting data...")
data = img.load()

pixels = []

print("Getting pixels...")
for y in range(img.size[1]):
	pixels.append([])
	for x in range(img.size[0]):
		pixels[y].append(data[x, y])

## Do stuff with pixels
## Save as outpixels


new = Image.new('RGB', img.size)

print("Placing pixels...")
for y in range(img.size[1]):
	for x in range(img.size[0]):
		new.putpixel((x, y), outpixels[y][x])

print("Saving image...")
new.save(outputImage)
print "Done!", outputImage