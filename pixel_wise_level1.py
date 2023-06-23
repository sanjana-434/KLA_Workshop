import cv2
import numpy as np
from PIL import Image
import csv

image_shape = (800,600)  # Example image shape (width, height)


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


def checkDefectByRGB(image_path):
    images = []
    for i in range(0,len(image_path)):
        images.append(Image.open(image_path[i]))

    image_pixels = []
    for i in range(0,len(image_path)):
        image_pixels.append(np.array(images[i]))
    print(image_pixels[0].shape)

    gradient_images = np.array(image_pixels)
    gradient_images = gradient_images.reshape((5,600,800,3))
    print(gradient_images.shape)
    result = []
    for i in range(0,gradient_images.shape[1]):
        for j in range(0,gradient_images.shape[2]):
            value_count = {}
            for k in range(0,gradient_images.shape[0]):
                r = gradient_images[k][i][j][0]
                b = gradient_images[k][i][j][1]
                g = gradient_images[k][i][j][2]
                rgb = str(r)+str(b)+str(g)
                if (rgb not in value_count):
                    value_count[rgb] = []
                value_count[rgb].append(k)
            for k in value_count.keys():
                if (len(value_count[k]) == 1):
                    result.append([value_count[k][0]+1,i,gradient_images.shape[2]-j-1])
                if (len(value_count[k]) == 2):
                    result.append([value_count[k][0]+1,i,gradient_images.shape[2]-j-1])
    print('Number of Defects : ',len(result))
    return (result)



def checkDefectByLaplace(images):
    gradient_images = []
    for i in range(0,len(image_path)):
        gradient_images.append(cv2.Laplacian(images[i], cv2.CV_64F))

    gradient_images = np.array(gradient_images)
    gradient_images = gradient_images.reshape((5,600,800))
    print(gradient_images.shape)
    result = []
    print('1 : ',gradient_images[0][0][30])
    print('2 : ',gradient_images[1][0][30])
    print('3 : ',gradient_images[2][0][30])
    print('4 : ',gradient_images[3][0][30])
    print('5 : ',gradient_images[4][0][30])
    for i in range(0,gradient_images.shape[1]):
        for j in range(0,gradient_images.shape[2]):
            value_count = {}
            for k in range(0,gradient_images.shape[0]):
                if (gradient_images[k][i][j] not in value_count):
                    value_count[gradient_images[k][i][j]] = []
                value_count[gradient_images[k][i][j]].append(k)
            for k in value_count.keys():
                if (len(value_count[k]) == 1):
                    result.append([value_count[k][0],i,j])
    #print('Number of Defects : ',len(result))
    return (result)

def checkDefectByGrayscale(gradient_images):
    results = []
    for i in range(0,len(gradient_images)):
        results.append([])
    print('1 : ',gradient_images[0][0][30])
    print('2 : ',gradient_images[1][0][30])
    print('3 : ',gradient_images[2][0][30])
    print('4 : ',gradient_images[3][0][30])
    print('5 : ',gradient_images[4][0][30])
    for i in range(0,gradient_images.shape[1]):
        for j in range(0,gradient_images.shape[2]):
            value_count = {}
            for k in range(0,gradient_images.shape[0]):
                if (gradient_images[k][i][j] not in value_count):
                    value_count[gradient_images[k][i][j]] = []
                value_count[gradient_images[k][i][j]].append(k)
            for k in value_count.keys():
                if (len(value_count[k]) == 1):
                    results[value_count[k][0]].append([value_count[k][0]+1,j,gradient_images.shape[1]-i-1])
                    print([value_count[k][0]+1,j,gradient_images.shape[1]-i-1])
                '''
                if (len(value_count[k]) == 2):
                    results[value_count[k][1]].append([value_count[k][1]+1,j,gradient_images.shape[1]-i-1])
                '''
    result = results[0]
    for i in range(1,len(results)):
        result.extend(results[i])
    print((result))
    return result

def checkDefectBybinarization(gradient_images):
    results = []
    for i in range(0,len(gradient_images)):
        results.append([])
    print('1 : ',gradient_images[0][0][30])
    print('2 : ',gradient_images[1][0][30])
    print('3 : ',gradient_images[2][0][30])
    print('4 : ',gradient_images[3][0][30])
    print('5 : ',gradient_images[4][0][30])
    for i in range(0,len(gradient_images)):
        gradient_images[i] = gradient_images[i] > 128
    for i in range(0,gradient_images.shape[1]):
        for j in range(0,gradient_images.shape[2]):
            value_count = {0:[],1:[]}
            for k in range(0,gradient_images.shape[0]):
                value_count[gradient_images[k][i][j]].append(k)
            #print(value_count)
            for k in [0,1]:
                if (len(value_count[k]) == 1):
                    results[value_count[k][0]].append([value_count[k][0]+1,i,gradient_images.shape[1]-j-1])
                    print(value_count[k][0]+1,i,j)
    print((results))
    result = result[0]
    for i in range(1,len(results)):
        result.extend(results)
    return result


def convertImage(image_path):
    images = []
    for i in range(0,len(image_path)):
        images.append(cv2.imread(image_path[i], cv2.IMREAD_GRAYSCALE))

    image_pixels = []

    for i in range(0,len(image_path)):
        image_pixels.append(convert_image_to_pixels(image_path[i],1))
    
    gradient_images = image_pixels
    '''
    gradient_images = []
    for i in range(0,len(image_path)):
        gradient_images.append(cv2.Laplacian(images[i], cv2.CV_64F))
    '''
    
    gradient_images = np.array(gradient_images)
    gradient_images = gradient_images.reshape((5,600,800))
    print(gradient_images.shape)
    

    return checkDefectByGrayscale(gradient_images)
    #checkDefectByLaplace(images)
    #return checkDefectByRGB(image_path)
    #return checkDefectBybinarization(gradient_images)



image1_path = 'wafer_image_1_.png'
image2_path = 'wafer_image_2_.png'
image3_path = 'wafer_image_3_.png'
image4_path = 'wafer_image_4_.png'
image5_path = 'wafer_image_5_.png'

image_path = list([image1_path,image2_path,image3_path,image4_path,image5_path])

result = convertImage(image_path)
#print(result)

filename = "result.csv"
    
# writing to csv file 
with open(filename, 'w',newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)         
    csvwriter.writerows(result)
