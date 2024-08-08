import cv2
import numpy as np

# Load the image
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Apply edge detection using Canny
edges = cv2.Canny(image, 100, 200)

# Apply texture analysis using Laplacian of Gaussian (LoG)
image_blur = cv2.GaussianBlur(image, (3, 3), 0)
image_log = cv2.Laplacian(image_blur, cv2.CV_64F)
image_log = np.uint8(np.absolute(image_log))

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.imshow('Texture (LoG)', image_log)

cv2.waitKey(0)
cv2.destroyAllWindows()
