import cv2
import numpy as np
import matplotlib.pyplot as plt

def pick_points(image):
    """
    Allows the user to click on an image and select multiple points.
    Use "Q" to leaving selecting.
    Returns a list of (x, y) tuples representing the coordinates of the selected points.
    """
    points = []
    image_display = image.copy()
    W, H, _ = image_display.shape

    image_guide = cv2.imread("utils/facial_landmarks_68markup.jpg")
    dim = (H, W)
    image_guide = cv2.resize(image_guide, dim)

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            points.append((x, y))
            cv2.circle(image_display, (x, y), 3, (0, 0, 255), -1)

    cv2.namedWindow("picker")
    cv2.setMouseCallback("picker", mouse_callback)
    cv2.setWindowTitle("picker", "Use the reference to select points, press Q to quit")
    cv2.setWindowProperty("picker", cv2.WND_PROP_TOPMOST, 1)

    while True:
        image_picker = np.concatenate((image_display, image_guide), axis=1)
        cv2.imshow("picker", image_picker)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()

    plt.figure()
    plt.imshow(image_display[:, :, [2, 1, 0]])

    return points