import cv2 
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np 

def display(im_path):
    
    dpi = 80
    im_data = plt.imread(im_path)

    # for color image , .shape function gives three Attribute
    if(len(im_data.shape)==3):
        height, width, depth = im_data.shape # difference
    else:
        height, width= im_data.shape  #difference

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

def invertedImage(img):
    # now taking and reading the page1 file 
    invertedImage=cv2.bitwise_not(img)

    # now save the image using imwrite function of the CV2
    cv2.imwrite("numberplates/1.jpg",invertedImage)

# function to convert image to grayScaleImage
def toGrayScale(img):
    gsImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # now also show converted grayScaleImage 
    cv2.imwrite("numberplates/car9-grayScale.png",gsImage)
    # display("numberplates/bikeGrayScaleImage.jpg")
    return gsImage


# now lets write function to convert a image into black and white
def toBWImage(img):
    thresh,BWimage=cv2.threshold(img,120,200,cv2.THRESH_BINARY)
    cv2.imwrite("numberplates/Cars9-output.png",BWimage)
    return BWimage

# noise removal function
def noiseRemoval(image):
    # first in noise removal we have to use erosion, dilation and morphology in order to 
    # remove the noise around character 

    # first create a kernal for dilation 
    kernal=np.ones((1,1),np.uint8)
    # do dilation
    image=cv2.dilate(image,kernel=kernal,iterations=1)
    
    # create another kernal for the erosion
    kernal=np.ones((1,1),np.uint8)
    # do erossion 
    image=cv2.erode(image,kernel=kernal,iterations=1)

    # now we are going to apply morphology and median blur
    image=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel=kernal)
    image=cv2.medianBlur(image,3)
    
    cv2.imwrite("numberplates/NRcar9.png",image)
    # now return the output 
    return image

def main():
    # the cv2 will convert image into a numpy array
    image=cv2.imread("numberplates/Cars9.png")
    gsImage=toGrayScale(image)
    # display
    # display("numberplates/Cars0.png")
    # convert np array into image  using pil 
    m=toBWImage(gsImage)
    ns=noiseRemoval(m)
    # img

    # showing image from the numpy array as image using plt 
    # plt.imshow(image)

    # we have some problem with show  

main()