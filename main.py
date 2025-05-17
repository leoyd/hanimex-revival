import cv2
from utils.filesystem import get_image_path

def capture_image():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Erreur : Impossible d’ouvrir la caméra.")
        return

    result, image = camera.read()
    if result:
        cv2.imshow('preview', image)
        cv2.imwrite(get_image_path(), image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Erreur : aucune image capturée.")

    camera.release()

if __name__ == "__main__":
    capture_image()