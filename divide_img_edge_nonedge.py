import cv2

def detect_edges(image_path):
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
    cv2.imwrite('EdgeImage2.png', edge_image)
    cv2.imwrite('Non-EdgeImage2.png', non_edge_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'wafer_image_1.png'
detect_edges(image_path)
