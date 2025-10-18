import cv2
import numpy as np

# Load the image
image = cv2.imread("safal.jpg")
original = image.copy()

# Convert to grayscale and create a mask using thresholding
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

# Optional: improve mask with morphological operations
kernel = np.ones((5, 5), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=3)
mask = cv2.GaussianBlur(mask, (21, 21), 0)

# Invert mask for the background
inv_mask = cv2.bitwise_not(mask)

# Blur the original image
blurred = cv2.GaussianBlur(original, (21, 21), 0)

# Extract foreground (sharp) and background (blurred)
foreground = cv2.bitwise_and(original, original, mask=inv_mask)
background = cv2.bitwise_and(blurred, blurred, mask=mask)

# Combine the foreground and blurred background
final = cv2.add(foreground, background)

# Show and save the result
cv2.imshow("Blurred Background", final)
cv2.imwrite("blurred_background.jpg", final)
cv2.waitKey(0)
cv2.destroyAllWindows()