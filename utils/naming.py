import datetime
from config import *


def get_image_name_date_part():
    datetime_now = datetime.datetime.now()
    date_part = datetime_now.strftime("%d%m%Y")
    time_part = datetime_now.strftime("%H%M%S")
    return date_part + time_part

def get_image_name():
    return get_image_name_date_part() + "_" + CAMERA_NAME + EXTENSION