import sys

from PIL import Image
from PIL import ImageFilter

#load args
args = sys.argv

#load cat image
catImg = Image.open(args[1])

#Blur cat image
blurCatImg = catImg.filter(ImageFilter.GaussianBlur(radius=5))

#load mask image
maskImg = Image.open(args[2])

#gray mask image
grayMaskImg = maskImg.convert('LA')

#result image
resultImg = catImg.copy()

#process images
for y in range(0,500):
    for x in range(0,800):
       grayValue, alpha = grayMaskImg.getpixel((x,y))
       
       if grayValue == 0:
           resultImg.putpixel((x,y), blurCatImg.getpixel((x,y)))
          
           

resultImg.show()

       
        
