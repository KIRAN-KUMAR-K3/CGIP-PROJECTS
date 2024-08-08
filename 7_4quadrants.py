import cv2

# Load the image
image = cv2.imread('test.jpg')

# Get image height and width
height, width = image.shape[:2]

# Split the image into four quadrants
top_left = image[0:height//2, 0:width//2]
top_right = image[0:height//2, width//2:width]
bottom_left = image[height//2:height, 0:width//2]
bottom_right = image[height//2:height, width//2:width]

# Display the original image and the quadrants
cv2.imshow('Original Image', image)
cv2.imshow('Top Left Quadrant', top_left)
cv2.imshow('Top Right Quadrant', top_right)
cv2.imshow('Bottom Left Quadrant', bottom_left)
cv2.imshow('Bottom Right Quadrant', bottom_right)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
