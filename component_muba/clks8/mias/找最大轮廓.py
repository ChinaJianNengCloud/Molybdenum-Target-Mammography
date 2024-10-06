import cv2
import numpy as np

def retain_largest_contour(image_path):

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("无法加载图像")

    mask = np.zeros_like(img)

    mask[30:-30, 30:-30] = 255  # 设置中间区域为白色，其余为黑色
    img_masked = cv2.bitwise_and(img, mask)
    gray = cv2.cvtColor(img_masked, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=8)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return img


    largest_contour = max(contours, key=cv2.contourArea)

    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    result = cv2.bitwise_and(img, mask)

    return result

output_image = retain_largest_contour(r'largest_contour_image.jpg')

cv2.imwrite('largest_contour_image.jpg', output_image)
