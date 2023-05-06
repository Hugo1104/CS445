import cv2
import matplotlib.pyplot as plt

def get_points(image):
    """
    Allows the user to click on an image and select multiple points.
    Use "Q" to leaving selecting.
    Returns a list of (x, y) tuples representing the coordinates of the selected points.
    """
    points = []

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            points.append((x, y))
            cv2.circle(image, (x, y), 3, (0, 0, 255), -1)

    cv2.namedWindow("Press Q to quit")
    cv2.setMouseCallback("Press Q to quit", mouse_callback)

    while True:
        cv2.imshow("Press Q to quit", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    plt.imshow(image[:, :, [2, 1, 0]])

    return points