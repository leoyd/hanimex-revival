import cv2
from pynput import keyboard
from utils.filesystem import get_image_path

# To avoid multiple captures if key is held down
pressed_keys = set()

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

def on_press(key):
    if key in pressed_keys:
        return None

    pressed_keys.add(key)

    try:
        if hasattr(key, 'char') and key.char == 'q':
            print("Exiting the program.")
            return False  # Stop listener
    except Exception:
        pass

    if key == keyboard.Key.space:
        capture_image()
        return None
    return None


def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
