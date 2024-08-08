import cv2

# Read the image
image = cv2.imread('sample.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the threshold image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_image = image.copy()

# Draw all contours with green color and thickness 2
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the original image with contours
cv2.imshow("Image with Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
