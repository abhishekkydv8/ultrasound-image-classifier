import pydicom
import numpy as np
import cv2

def load_dicom_image(file_path):
    ds = pydicom.dcmread(file_path)
    image = ds.pixel_array.astype(np.float32)
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_GRAY2BGR)
