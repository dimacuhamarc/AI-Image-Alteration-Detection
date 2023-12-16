import cv2
import numpy as np
import os

def DisplayImage(image, window_name):
  cv2.imshow(window_name, image)

#using sobel
def DetectUsingSobel(image, altered_image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  altered_image = cv2.cvtColor(altered_image, cv2.COLOR_BGR2GRAY)
  
  #applies sobel
  sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
  sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
  
  sobel_x_altered = cv2.Sobel(altered_image, cv2.CV_64F, 1, 0, ksize=5)
  sobel_y_altered = cv2.Sobel(altered_image, cv2.CV_64F, 0, 1, ksize=5)
  
  magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
  
  magnitude_altered = np.sqrt(sobel_x_altered**2 + sobel_y_altered**2)
  
  threshold = 100
  
  edge_mask = (magnitude > threshold).astype(np.uint8) * 255
  
  edge_mask_altered = (magnitude_altered > threshold).astype(np.uint8) * 255
  
  DisplayImage(edge_mask, 'Edge Image')
  DisplayImage(edge_mask_altered, 'Edge Image Altered')
  
  if np.sum(edge_mask) == np.sum(edge_mask_altered):
    print("No alteration detected.")
  else:
    print("Image alteration detected!")


def DetectUsingPixelValue(image1, image2, threshold=30):

    # Check if the images have the same dimensions
    if image1.shape != image2.shape:
        raise ValueError("The images must have the same dimensions.")

    # Compute the absolute difference between the two images
    diff = cv2.absdiff(image1, image2)

    # Create a mask based on the threshold
    mask = np.all(diff > threshold, axis=-1)

    # Initialize an output image with zeros
    result = np.zeros_like(image1)
    
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    coordinates = np.column_stack(np.where(gray > threshold))

    # Set the altered pixels to red in the output image
    result[mask] = [0, 0, 255]  # Red color for altered pixels
      
    
    DisplayImage(result, 'Pixel Value Visualizer')
    
    if coordinates.size == 0:
      print("No alteration detected.")
    else:
      print("Differing pixel coordinates:")
      for coord in coordinates:
          print(f"Pixel at ({coord[1]}, {coord[0]}) is different.")


