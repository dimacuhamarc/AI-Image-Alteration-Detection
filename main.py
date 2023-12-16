##  Module Imports
import cv2
import os
from detector import DetectUsingPixelValue

##  Change this to the name of the image you want to test
IMAGE_NAME = 'image18'

##  Function Definitions
# Get Image Function
def GetImage(image_name, type, resize = True):
  image_path = os.path.join(os.getcwd(),type + '/' + image_name + '.jpg')
  image = cv2.imread(image_path)
  
  if image.shape[0] > image.shape[1]:
    resize = False
    
  if resize:
    resized_image = cv2.resize(image, (1000, 500),interpolation = cv2.INTER_LANCZOS4)
  return image if not resize else resized_image

# Image Display Function
def DisplayImage(image, window_name):
  cv2.imshow(window_name, image)

##  Main Script
def __main__():
  DisplayImage(GetImage(IMAGE_NAME, 'altered'), 'Altered Image')
  DisplayImage(GetImage(IMAGE_NAME, 'raw'), 'Original Image')
  
  # Detecting the altered pixels using the pixel value method
  DetectUsingPixelValue(GetImage(IMAGE_NAME, 'raw'), GetImage(IMAGE_NAME, 'altered'))
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
__main__()
