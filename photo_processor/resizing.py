import cv2
import numpy as np


class ImageResizing:
    @staticmethod
    def image_multiply(input_image):
        
        image_mirrored = cv2.flip(input_image, 0)
        output_image = np.vstack([input_image, image_mirrored])
        output_image = np.hstack([output_image, cv2.flip(output_image, 1)])
        
        return output_image