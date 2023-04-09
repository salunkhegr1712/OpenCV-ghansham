import pytesseract
import cv2
from PIL import Image

im=Image.open("./file.png")

print(im)
# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=839x299 at 0x7FBB8BACFEE0>
print(im.size)
im.show()