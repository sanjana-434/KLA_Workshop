import cv2
import numpy as np
from PIL import Image

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


def calculate_absolute_difference(ref_image_path, to_be_detected_image_path):
    # Read the reference and to-be-detected images
    ref_image = cv2.imread(ref_image_path, cv2.IMREAD_GRAYSCALE)
    to_be_detected_image = cv2.imread(to_be_detected_image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the absolute difference between the images
    pixel_values_ref_image = convert_image_to_pixels(ref_image_path,1)
    pixel_values_to_be_detected_image = convert_image_to_pixels(to_be_detected_image_path,1)
    print(len(pixel_values_ref_image))
    print(len(pixel_values_to_be_detected_image))
    pixel_values_ref_image = np.array(pixel_values_ref_image)
    pixel_values_to_be_detected_image = np.array(pixel_values_to_be_detected_image)

    abs_diff = cv2.absdiff(pixel_values_ref_image, pixel_values_to_be_detected_image)
    print("Abs : ",abs_diff)
    
    image_shape = ref_image.shape  # Example image shape (width, height)
    abs_image = convert_pixels_to_image(pixel_values_ref_image, image_shape)
    print("Dim : ",abs_image.shape)
    ref_image = convert_pixels_to_image(pixel_values_ref_image, image_shape)
    to_be_detected_image = convert_pixels_to_image(pixel_values_to_be_detected_image, image_shape)
    # Display the absolute difference image
    cv2.imwrite('AbsoluteDifference4.png', abs_image)




def detect_edges(image_path,i):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE = 0
    cv2.imwrite('grayScale.png', image)

    # Apply Canny edge detection
    edges = cv2.Canny(image, 100, 200)  # Adjust the threshold values as needed

    # Create a mask for the edges
    edge_mask = edges > 0

    # Create a non-edge mask
    non_edge_mask = ~edge_mask

    # Apply the masks to the original image
    edge_image = image.copy()
    edge_image[non_edge_mask] = 0

    non_edge_image = image.copy()
    non_edge_image[edge_mask] = 0

    # Display the edge and non-edge images
    cv2.imwrite('EdgeImage'+str(i)+'.png', edge_image)
    cv2.imwrite('Non-EdgeImage'+str(i)+'.png', non_edge_image)



detect_edges('wafer_image_1.png',1)
detect_edges('wafer_image_2.png',2)

# Example usage
ref_image_path = 'Non-EdgeImage1.png'
to_be_detected_image_path = 'Non-EdgeImage2.png'
calculate_absolute_difference(ref_image_path, to_be_detected_image_path)
