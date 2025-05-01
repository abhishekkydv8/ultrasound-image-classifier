import os

def is_dicom(file_path):
    return file_path.lower().endswith('.dcm')

def get_image_files(folder):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.dcm']
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in valid_extensions]
