import cv2
import numpy as np

# Text Properties
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = (0, 255, 255)
thickness = 1

# Image Display Function
def DisplayImage(image, window_name):
  cv2.imshow(window_name, image)

# Pixel Value Detector
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
    
    # Convert the mask to a 3-channel image so we can easily overlay it on the original
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Find the coordinates of all pixels above the threshold
    coordinates = np.column_stack(np.where(gray > threshold))
    
    # Set the altered pixels to red in the output image
    result[mask] = [0, 0, 255]  # Red color for altered pixels
    
    # Prints the result based on the coordinates of the altered pixels
    if coordinates.size == 0:
      print("No alteration detected.")
    else:
      print("Differing pixel coordinates:")
      for coord in coordinates:
          print(f"Pixel at ({coord[1]}, {coord[0]}) is different.")
          
      # Add a yellow bounding box (outline only) around the altered area
      min_x, min_y = np.min(coordinates, axis=0)
      max_x, max_y = np.max(coordinates, axis=0)
      
      # Yellow outline and Text
      result = cv2.rectangle(result, (min_y - 5, min_x - 5), (max_y + 5, max_x + 5), (0, 255, 255), 2)  # Yellow outline
      result = cv2.putText(result, "Area of Alteration", (min_y, min_x - 10), font, fontScale, color, thickness, cv2.LINE_AA)
      
      print("The Image is altered")
      
    # Display the result
    DisplayImage(result, 'Pixel Value Visualizer')
