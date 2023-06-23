import cv2
import numpy as np
from PIL import Image

image_shape = (600,800)  # Example image shape (width, height)


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

def checkDefect(gradient_images):
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
    print(len(result))
    #print(result)   




def convertToLaplace(image_path):
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


    checkDefect(gradient_images)




image1_path = 'wafer_image_1.png'
image2_path = 'wafer_image_2.png'
image3_path = 'wafer_image_3.png'
image4_path = 'wafer_image_4.png'
image5_path = 'wafer_image_5.png'

image_path = list([image1_path,image2_path,image3_path,image4_path,image5_path])

result = convertToLaplace(image_path)
