import cv2

img=cv2.imread("solar-system.jpg")

cv2.imshow('displayImage',img)

cv2.waitKey(0)
print(img)