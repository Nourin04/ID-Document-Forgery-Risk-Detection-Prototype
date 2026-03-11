import cv2


def check_blur(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    if laplacian_var < 100:
        return True, laplacian_var   # blurry
    return False, laplacian_var      # clear


def check_resolution(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    if width < 500 or height < 300:
        return "Low"
    return "Good"


def detect_edges(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    edge_count = edges.sum()

    return edge_count