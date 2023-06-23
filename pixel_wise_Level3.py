import cv2
import numpy as np
from PIL import Image
import csv
import os

image_shape = (1500,2000) 

def convert_pixels_to_image(pixels, image_shape):
    # Reshape the pixel array to match the image shape
    pixel_array = np.reshape(pixels, image_shape)

    # Convert the pixel array to image
    image = np.uint8(pixel_array)

    return image

def convert_image_to_pixels(image_path, pixel_length):
    image = Image.open(image_path)
    image = image.convert("L")  # Convert to grayscale
    width, height = image.size
    pixel_count = (width // pixel_length) * (height // pixel_length)
    pixels = []

    for y in range(0, height, pixel_length):
        for x in range(0, width, pixel_length):
            pixel_value = image.getpixel((x, y))
            pixels.append(pixel_value)

    return pixels

def checkDefectByGrayscale(gradient_images):
    careAreas = [[[8,1368],[836,616]],[[224,356],[904,88]],[[1336,1280],[1872,672]],[[1076,576],[1560],84]]

    results = []
    for i in range(0,len(gradient_images)):
        results.append([])
    for l in range(0,len(careAreas)):
        c = careAreas[l]
        for i in range(1000-1-c[0][1],1000-c[1][1]):
            for j in range(c[0][0],c[1][0]+1):
                value_count = {}
                for k in range(0,gradient_images.shape[0]):
                    if (gradient_images[k][i][j] == -1):
                        continue
                    if (gradient_images[k][i][j] not in value_count):
                        value_count[gradient_images[k][i][j]] = []
                    value_count[gradient_images[k][i][j]].append(k)
                for k in value_count.keys():
                    if (len(value_count[k]) == 1):
                        results[value_count[k][0]].append([value_count[k][0]+1,j,gradient_images.shape[1]-i-1])
                        #print([value_count[k][0]+1,j,gradient_images.shape[1]-i-1])
                '''
                if (len(value_count[k]) == 2):
                    results[value_count[k][1]].append([value_count[k][1]+1,j,gradient_images.shape[1]-i-1])
                '''
    result = results[0]
    for i in range(1,len(results)):
        result.extend(results[i])
    print((result))
    return result


def convertImage(image_path):
    images = []
    for i in range(0,len(image_path)):
        images.append(cv2.imread(image_path[i], cv2.IMREAD_GRAYSCALE))

    image_pixels = []
    exclusiveZones = [[[368,1112],[560,892]] , [[1548,1084],[1720,897]] , [[268,320],[468,208]],[[1312,528],[1464,248]]]
    for i in range(0,len(image_path)):
        image_pixels.append(np.array(convert_image_to_pixels(image_path[i],1)))
    gradient_images = image_pixels
    
    gradient_images = np.array(gradient_images)
    print(gradient_images.shape)
    gradient_images = gradient_images.reshape((15,1000,1200))
    print(gradient_images.shape)
    for i in range(0,len(gradient_images)):
        for j in range(0,len(exclusiveZones)):
            e = exclusiveZones[j]
            gradient_images[i][(1000-1-e[0][1]):(1000-e[1][1]),e[0][0]:e[1][0]] = -1
    

    return checkDefectByGrayscale(gradient_images)



#files_images = (os.listdir('D:/Lab_Main/KLA_Workshop/level3_input'))
file_images = []
for i in range(1,241):
    file_images.append('D:/Lab_Main/KLA_Workshop/level3_input/wafer_image_'+str(i)+'.png')
print(file_images)

exclusiveZones = [[[368,1112],[560,892]] , [[1548,1084],[1720,897]] , [[268,320],[468,208]],[[1312,528],[1464,248]]]
careAreas = [[[8,1368],[836,616]],[[224,356],[904,88]],[[1336,1280],[1872,672]],[[1076,576],[1560],84]]


image_path = list(file_images)

#{"top_left": {"x": 762, "y": 826}, "bottom_right": {"x": 1092, "y": 490}}]
result = convertImage(image_path)
#print(result)

filename = "result_level3.csv"
    
# writing to csv file 
with open(filename, 'w',newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)         
    csvwriter.writerows(result)