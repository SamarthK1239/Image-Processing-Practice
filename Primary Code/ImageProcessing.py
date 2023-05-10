# Create filters for image processing
import tempfile

import numpy as np
import cv2
from PIL import Image


def normalize_image(image):
    normalized_image = np.zeros((image.shape[0], image.shape[1]))
    return cv2.normalize(image, normalized_image, 0, 255, cv2.NORM_MINMAX)


def deskew(image):
    co_ordinates = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(co_ordinates)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        (height, width) = image.shape[:2]
        center = (width // 2, height // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (width, height), flags=cv2.INTER_CUBIC,
                                       borderMode=cv2.BORDER_REPLICATE)
        return rotated_image


def set_image_dpi(image_path):
    image = Image.open(image_path)
    length_x, width_y = image.size
    factor = max(1, int(1000 / length_x))
    size = factor * length_x, factor * width_y
    image_resized = image.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    image_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


def remove_noise_and_smooth(image):
    return cv2.fastNlMeansDenoising(image, None, 10, 10, 7, 15)


def thin_and_skeletonize(image_name):
    image = cv2.imread(image_name, 0)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    return erosion


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
