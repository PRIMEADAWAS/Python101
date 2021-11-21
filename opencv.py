import cv2
img = cv2.imread('image/wow.jpg')

# read img
print(img.ndim)
print(type(img.ndim))
print(img)

# img resize
imgresize = cv2.resize(img, (600, 600))

# show img
cv2.imshow('TITLE', imgresize)
cv2.waitKey(delay=2000)
cv2.destroyAllwindow()
