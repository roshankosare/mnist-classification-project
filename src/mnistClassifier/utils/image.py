

import numpy as np
from PIL import Image

def preprocess_image(image:Image):
    # Resize the image to 28x28 pixels
    image_resized = image.resize((28, 28))
    # Convert image to grayscale
    image_gray = image_resized.convert('L')
    # Convert image to numpy array
    image_array = np.array(image_gray)
    # Flatten the image array
    image_flat = image_array.flatten()

    return image_flat
