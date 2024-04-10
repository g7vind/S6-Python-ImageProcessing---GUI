from images import Image
def grayScale(image):
    for y in range (image.getHeight()):
        for x in range (image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            r=(int(r*0.299))
            g=(int(g*0.587))
            b=(int(b*0.114))
            average = r + g + b
            image.setPixel(x, y, (average, average, average))
def main(filename = "test.gif"):
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    grayScale(image)
    print("Close the image window to quit")
    image.draw()
    image.save("grayScale_img.gif")
if __name__ == "__main__":
    main()