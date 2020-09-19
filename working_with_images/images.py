from PIL import Image

def activity1():

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
    box_image.show()

    img.paste(im = box_image, box=(100,100))
    img.paste(im = box_image, box=(400,320))

    img.show()

    reimg = img.resize((400,400))
    print("Width ",img.width,"height",img.height)
    reimg.show()


def activity2():

    img = Image.open("word_matrix.png")
    rotimg = img.rotate(90)
    rotimg.putalpha(128)
    rotimg.show()
    rotimg.save("somenew_image.png")



def activity3():

    # Solution to Image Exercise
    mask_img = Image.open("mask.png")
    word_img = Image.open("word_matrix.png")

    print("Word",word_img.width, word_img.height)
    print("Mask",mask_img.width, mask_img.height)

    reimg_mask = mask_img.resize((word_img.width,word_img.height))
    reimg_mask.putalpha(100)
    word_img.paste(im=reimg_mask,box=(0,0),mask=reimg_mask)

    #word_img.show()
    word_img.save("message_solution.png")
    img = Image.open("message_solution.png")
    img.show()

#activity1()
#activity2()
activity3()
