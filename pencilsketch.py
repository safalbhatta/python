import cv2
#loading the image
image=cv2.imread('/Users/safalbhatta/pythonProject/Rashmi.jpeg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert_image=255-gray_image
blurred=cv2.GaussianBlur(invert_image,(21,21),0)
inverted_blurred=255-blurred
sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
cv2.imwrite('pencil_sketch.jpg',sketch)
cv2.imshow('Pencil Sketch',sketch)
cv2.waitKey(0)  