import cv2
import numpy as np

def detect_alteration(image_path):
    # Read the image
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=5)

    # Compute the magnitude of the gradient
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Define a threshold for edge detection
    threshold = 100

    # Create a binary mask based on the threshold
    edge_mask = (magnitude > threshold).astype(np.uint8) * 255

    # Display the original and edge-detected images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Edge Detection', edge_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Check if alteration is detected based on the edge information
    if np.sum(edge_mask) > 0:
        print("Image alteration detected!")
    else:
        print("No alteration detected.")

# Specify the path to the image you want to analyze
image_path = 'path/to/your/image.jpg'

# Call the function to detect alteration
detect_alteration(image_path)
