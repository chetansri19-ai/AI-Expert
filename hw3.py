import cv2
import numpy as np

image = cv2.imread("image.jpg")

height, width = image.shape[:2]

matrix = cv2.getRotationMatrix2D((width // 2, height // 2), 45, 1)
rotated = cv2.warpAffine(image, matrix, (width, height))

cropped = image[50:250, 50:250]

bright = cv2.convertScaleAbs(image, alpha=1, beta=50)

cv2.imshow("Original", image)
cv2.imshow("Rotated", rotated)
cv2.imshow("Cropped", cropped)
cv2.imshow("Brightened", bright)

cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("brightened.jpg", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()