import cv2

class PhotoProcessor:
    def __init__(self):
        #TODO: BLOCK CHANGE OF THE LOADED IMAGE ADD GETTER SETTER
        self.loaded_image: cv2.Mat = None
        self.worked_image: cv2.Mat = None
        self.history: list = []

    def load_image(self, image_path: str):
        self.loaded_image: cv2.Mat = cv2.imread(image_path) #TODO: explore flags
        
    def save_image(self, image_path: str):
        result = cv2.imwrite(image_path, self.worked_image) #TODO: explore params, what to do from result
        
    def apply_edit(self, edit_func, **kwargs):
        if self.worked_image is None:
            self.worked_image = self.loaded_image
        
        self.history.append(self.worked_image)
        self.worked_image = edit_func(self.worked_image, **kwargs)
        
        """
        editor = ImageEditor("input.jpg")

# Use the Adjustments module
editor.apply_edit(editor.adjustments.brightness, beta=30)
editor.apply_edit(editor.adjustments.contrast, alpha=1.2)

# Use the Filters module
editor.apply_edit(editor.filters.blur, kernel_size=5)

# Undo the last edit
editor.undo()

editor.save("output.jpg")
        """