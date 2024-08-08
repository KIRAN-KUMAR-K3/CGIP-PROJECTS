import cv2
import numpy as np

canvas_width = 500
canvas_height = 500

canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)

translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
rotation_matrix = cv2.getRotationMatrix2D((150, 150), 45, 1.0)
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

translated_obj = cv2.transform(np.array([obj_points]), translation_matrix).squeeze().astype(np.int32)
rotated_obj = cv2.transform(np.array([translated_obj]), rotation_matrix).squeeze().astype(np.int32)
scaled_obj = cv2.transform(np.array([rotated_obj]), scaling_matrix).squeeze().astype(np.int32)

cv2.polylines(canvas, [obj_points], isClosed=True, color=(0, 0, 0), thickness=2)
cv2.polylines(canvas, [translated_obj], isClosed=True, color=(0, 255, 0), thickness=2)
cv2.polylines(canvas, [rotated_obj], isClosed=True, color=(255, 0, 0), thickness=2)
cv2.polylines(canvas, [scaled_obj], isClosed=True, color=(0, 0, 255), thickness=2)

cv2.imshow("2D Transformations", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
