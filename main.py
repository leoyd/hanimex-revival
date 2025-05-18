import cv2
import keyboard
from utils.filesystem import get_image_path

def capture_image():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        return

    ret, frame = camera.read()
    if ret:
        image_path = get_image_path()
        cv2.imwrite(image_path, frame)
    else:
        print("Error: No image captured.")

    camera.release()

if __name__ == "__main__":
    while True:
        key = keyboard.read_key()
        if key == 'space':
            capture_image()
        elif key == 'q':
            print("Quitte le programme.")
            break
