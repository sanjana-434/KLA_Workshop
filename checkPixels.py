import cv2

image1_path = 'wafer_image_1.png'
image2_path = 'wafer_image_2.png'
image3_path = 'wafer_image_3.png'
image4_path = 'wafer_image_4.png'
image5_path = 'wafer_image_5.png'

image_path = list([image1_path,image2_path,image3_path,image4_path,image5_path])
images = []
for i in range(0,len(image_path)):
    images.append(cv2.imread(image_path[i], cv2.IMREAD_GRAYSCALE))

#crop_image = image[x:w, y:h]
i1 = cv2.vconcat([images[0][0:1,30:31],images[1][0:1,30:31],images[2][0:1,30:31],images[3][0:1,30:31],images[4][0:1,30:31]])
i2 = cv2.vconcat([images[0][0:1,72:73],images[1][0:1,72:73],images[2][0:1,72:73],images[3][0:1,72:73],images[4][0:1,72:73]])
i3 = cv2.vconcat([images[0][0:1,85:86],images[1][0:1,85:86],images[2][0:1,85:86],images[3][0:1,85:86],images[4][0:1,85:86]])
i4 = cv2.vconcat([images[0][0:1,86:87],images[1][0:1,86:87],images[2][0:1,86:87],images[3][0:1,86:87],images[4][0:1,86:87]])
i5 = cv2.vconcat([images[0][0:1,205:206],images[1][0:1,205:206],images[2][0:1,205:206],images[3][0:1,205:206],images[4][0:1,205:206]])
i6 = cv2.vconcat([images[0][0:1,220:221],images[1][0:1,220:221],images[2][0:1,220:221],images[3][0:1,220:221],images[4][0:1,220:221]])



cv2.imwrite("i1.png", i1)
cv2.imwrite("i2.png", i2)
cv2.imwrite("i3.png", i3)
cv2.imwrite("i4.png", i4)
cv2.imwrite("i5.png", i5)
cv2.imwrite("i6.png", i6)

'''im_v = cv2.vconcat([img1, img1])
1 0 30
2 0 72
1 0 85
3 0 86
3 0 205
2 0 220
5 0 222
1 0 235
3 0 237
3 0 265
1 0 273
3 0 394
3 0 442
3 0 450
5 0 466
2 0 565
3 0 580
5 0 601'''