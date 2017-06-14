from PIL import Image
from PIL import ImageFilter

#load cat image
catImg = Image.open("dog.jpg")

#Blur cat image
blurCatImg = catImg.filter(ImageFilter.GaussianBlur(radius=5))

#load mask image
maskImg = Image.open("mask.png")

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

       
        
