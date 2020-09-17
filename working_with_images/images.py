from PIL import Image


print("Pillow - Working with Images")

img = Image.open("example.jpg")
#img.show()  # Opens default image viewer
print(img.filename)
print(img.size)
print(img.format_description)
print("Width ",img.width,"height",img.height)

# crop returns a rectangular region from this image.
# The box is a 4-tuple defining the left, right and lower pixel

xs = 860
ys = 840

cropwidth = 300
cropheight = 417

box = (xs,ys,min(xs+cropwidth,img.width),min(ys+cropheight,img.height))
print(box)
box_image = img.crop(box)
#box_image.show()

img.paste(im = box_image, box=(100,100))
img.paste(im = box_image, box=(400,320))

img.show()
