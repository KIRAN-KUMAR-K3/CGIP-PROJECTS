import cv2

# Load the image
image = cv2.imread('test.jpg')

# Apply Gaussian blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Apply median blur
median_blur = cv2.medianBlur(image, 15)

# Apply bilateral filter
bilateral_blur = cv2.bilateralFilter(image, 15, 75, 75)

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Blur', bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
