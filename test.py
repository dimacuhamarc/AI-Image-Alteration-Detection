import cv2
import numpy as np
import os

#detects if an image has been altered using histogram
def DetectAlteredImage(image, altered_image):
  #converts image to grayscale
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  altered_image = cv2.cvtColor(altered_image, cv2.COLOR_BGR2GRAY)
  
  #creates histogram for both images
  image_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
  altered_image_hist = cv2.calcHist([altered_image], [0], None, [256], [0, 256])
  
  #compares histograms
  if np.sum(image_hist) == np.sum(altered_image_hist):
    print("No alteration detected.")
  else:
    print("Image alteration detected!")
    
def DisplayImage(image, window_name):
  cv2.imshow(window_name, image)


def usingSobel():
  image_path = os.path.join(os.getcwd(), 'rabbit.png')
  original_image = cv2.imread(image_path)
  altered = cv2.imread(image_path)
  
  sobel_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=5)
  sobel_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=5)
  
  sobel_x_altered = cv2.Sobel(altered, cv2.CV_64F, 1, 0, ksize=5)
  sobel_y_altered = cv2.Sobel(altered, cv2.CV_64F, 0, 1, ksize=5)
  
  magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
  
  magnitude_altered = np.sqrt(sobel_x_altered**2 + sobel_y_altered**2)
  
  threshold = 100
  
  edge_mask = (magnitude > threshold).astype(np.uint8) * 255
  
  edge_mask_altered = (magnitude_altered > threshold).astype(np.uint8) * 255


  DisplayImage(original_image, 'Original Image')
  DisplayImage(edge_mask, 'Edge Image')

  if np.sum(edge_mask) == np.sum(edge_mask_altered):
      print("No alteration detected.")
  else:
      print("Image alteration detected!" + str(np.sum(edge_mask)))
  