import cv2

image = cv2.imread("image.jpg")

sizes = [(100, 100), (300, 300), (500, 500)]

for i, size in enumerate(sizes, 1):
    resized = cv2.resize(image, size)
    cv2.imshow(f"Resized {i}", resized)
    cv2.imwrite(f"resized_{i}.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()