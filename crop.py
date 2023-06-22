'''import cv2


img = cv2.imread("wafer_image_1.png")
crop_img = img[0,800:1:600]
cv2.imwrite("out1.png", crop_img)
cv2.waitKey(0)
'''

from PIL import Image 
 
  
img = Image.open(r"wafer_image_1.png") 
 
'''
left = 0
top = 0
right = 80
bottom = 30
 
  
img_res = img.crop((left, top, right, bottom)) 
img_res.show() 
'''
left = 0
top = 0
right = 800
bottom = 600
 
  
img_res = img.crop((left, top, right, bottom)) 
 
 
img_res.show() 

'''
import cv2
image = cv2.imread(r"wafer_image_1.png")
 
y=0
x=0
h=20
w=60
crop_image = image[x:w, y:h]
cv2.imwrite("out1.png", crop_image)
cv2.waitKey(0)
'''