import cv2
import numpy as np

# Load the image
image = cv2.imread('test.jpg')

# Define rotation angle (in degrees)
angle = 45

# Define scaling factors
scale_x = 1.5
scale_y = 1.5

# Define translation offsets
tx = 50
ty = 50

# Get image dimensions
height, width = image.shape[:2]

# Define rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

# Apply rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Apply scaling
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)

# Apply translation
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Translated Image', translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
