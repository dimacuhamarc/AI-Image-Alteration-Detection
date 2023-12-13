import cv2
import os

IMAGE_NAME = 'image1'

def GetImage(image_name, type):
  image_path = os.path.join(os.getcwd(),type + '/' + image_name + '.jpg')
  image = cv2.imread(image_path)
  return image

def DisplayImage(image, window_name):
  cv2.imshow(window_name, image)
  
def __main__():
  DisplayImage(GetImage(IMAGE_NAME, 'altered'), 'Altered Image')
  DisplayImage(GetImage(IMAGE_NAME, 'raw'), 'Original Image')
  
  DetectAlteredImage(GetImage(IMAGE_NAME, 'altered'), GetImage(IMAGE_NAME, 'raw'))

  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
__main__()