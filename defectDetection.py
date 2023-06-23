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

def detect_defects(image, reference_image, grayscale_threshold, gradient_threshold):
    # Convert images to grayscale
    
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    pixels_grayscale_image = (convert_image_to_pixels('wafer_image_1.png',1))
    pixels_grayscale_reference = (convert_image_to_pixels('wafer_image_2.png',1))
    
    pixels_grayscale_reference = np.array(pixels_grayscale_reference)
    pixels_grayscale_image = np.array(pixels_grayscale_image)

    print(len(pixels_grayscale_image))
    print(len(pixels_grayscale_reference))
    
    # Compute grayscale difference
    grayscale_diff = cv2.absdiff(pixels_grayscale_image, pixels_grayscale_reference)
    grayscale_image = convert_pixels_to_image(pixels_grayscale_image, image_shape)
    grayscale_reference = convert_pixels_to_image(pixels_grayscale_reference, image_shape)
    cv2.imwrite('grayscale_image.png',grayscale_image)
    cv2.imwrite('grayscale_reference.png',grayscale_reference)
    grayscale_image = cv2.imread('grayscale_image.png')
    grayscale_reference = cv2.imread('grayscale_reference.png')

    # Compute gradient
    gradient_image = cv2.Laplacian(grayscale_image, cv2.CV_64F)

    # Compute gradient difference
    gradient_diff = cv2.absdiff(gradient_image, cv2.Laplacian(grayscale_reference, cv2.CV_64F))
    # Apply thresholding
    grayscale_mask = grayscale_diff > grayscale_threshold
    gradient_mask = gradient_diff > gradient_threshold

    #gradient_mask = gradient_mask.ravel()

    # Combine masks
    defect_mask = np.logical_or(grayscale_mask, gradient_mask)

    # Perform morphological operations to enhance defect regions
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    defect_mask = cv2.morphologyEx(defect_mask.astype(np.uint8), cv2.MORPH_CLOSE, kernel)

    # Find contours of defects
    contours, _ = cv2.findContours(defect_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around defects on the original image
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    return image

# Load the original image and reference image
image = cv2.imread('wafer_image_1.png')
reference_image = cv2.imread('wafer_image_2.png')

# Set the threshold values
grayscale_threshold = 30
gradient_threshold = 50

# Detect defects in the image
result = detect_defects(image, reference_image, grayscale_threshold, gradient_threshold)

# Display the result
cv2.imwrite('Defect Detection Result', result)