from images import Image
from functools import reduce
def blur(image):
    def trippleSum(a,b):
        (r1,g1,b1) = a
        (r2,g2,b2) = b
        return (r1+r2, g1+g2, b1+b2)
    newImage=image.clone()
    for y in range (1,image.getHeight()-1):
        for x in range (1,image.getWidth()-1):
            oldPixel = image.getPixel(x,y)
            leftPixel = image.getPixel(x-1,y)
            rightPixel = image.getPixel(x+1,y)
            topPixel = image.getPixel(x,y-1)
            bottomPixel = image.getPixel(x,y+1)
            newPixel = reduce(trippleSum, [oldPixel, leftPixel, rightPixel, topPixel, bottomPixel])
            newPixel = tuple(map(lambda x: x//5, newPixel))
            newImage.setPixel(x,y,newPixel)
    return newImage
def main(filename = "timtest.gif"):
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    newImage = blur(image)
    print("Close the image window to quit")
    newImage.draw()
    newImage.save("blur_img.gif")
if __name__ == "__main__":
    main()