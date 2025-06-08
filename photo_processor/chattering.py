import numpy as np
import cv2

class MosaicFilters:
    
    @staticmethod
    def mosaic_1(input_image, number_of_parts = 150):
        image_list = MosaicFilters._image_cutter(input_image, number_of_parts=number_of_parts)
        output_image = MosaicFilters._image_merger(image_list)
        
        return output_image
    
    @staticmethod
    def _image_cutter(source_image, number_of_parts = 140):
        source_image = np.array(source_image)
        output_list = []
        _, width, _ = source_image.shape
        
        tick = False
        for step in range(1, number_of_parts+1):
            image_part = source_image[:, (step-1)*(int(width/number_of_parts)): step*(int(width/number_of_parts))]
            if tick:
                output_list.append(cv2.rotate(image_part, cv2.ROTATE_90_COUNTERCLOCKWISE))
            else:
                output_list.append(cv2.rotate(image_part, cv2.ROTATE_90_CLOCKWISE))
            
        return output_list

    @staticmethod
    def _image_merger(image_list):
        left = 0
        right = len(image_list) - 1
        toggle = 0 
        
        to_vstack = []
        while left < right:
            if toggle:
                to_vstack.append(image_list[left])
                left += 1
            else:
                to_vstack.append(image_list[right])
                right -= 1
            toggle = not toggle
            
        return np.vstack(to_vstack)