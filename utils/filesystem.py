import os
from config import DATA_DIRECTORY
from utils.naming import get_image_name

def get_data_directory():
    if not os.path.exists(DATA_DIRECTORY):
        print("Data directory doesn't exist. Creating it.")
        os.mkdir(DATA_DIRECTORY)
    else:
        print("Data directory exists. No need to create it.")
    return DATA_DIRECTORY

def get_image_path():
    return os.path.join(get_data_directory(), get_image_name())