from images import Image
def blackAndWhite(image):
    blackPixel = (0, 0, 0)
    whitePixel = (225,255,255)
    for y in range (image.getHeight()):
        for x in range (image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            average = (r + g + b) // 3
            if average < 128 :
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def main(filename = "test.gif"): # give file to be make b & w
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    blackAndWhite(image)
    print("Close the image window to quit")
    image.draw()
    image.save("blackAndWhite.gif") #give your file name
if __name__ == "__main__":
    main()
    