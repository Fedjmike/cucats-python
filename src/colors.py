from PIL import Image

print("Opening image...")
img = Image.open(args.image)
img = img.convert('RGBA')

print("Getting data...")
data = img.load()
new = Image.new('RGBA', img.size)

pixels = []

print("Getting pixels...")
for y in range(img.size[1]):
	pixels.append([])
	for x in range(img.size[0]):
		pixels[y].append(data[x, y])

## Do stuff with pixels

print("Placing pixels...")
for y in range(img.size[1]):
	for x in range(img.size[0]):
		new.putpixel((x, y), sortedPixels[y][x])

print("Saving image...")
new.save(outputImage)
print "Done!", outputImage