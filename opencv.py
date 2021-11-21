import cv2

img = cv2.imread('image/wow.jpg', 1)
# 1 color, 0 grayscale

# read img
print(img.ndim)
print(type(img.ndim))
print(img)

# img resize
imgresize = cv2.resize(img, (900, 600))

# img write
cv2.imwrite('imwrite.jpg', imgresize)

# show img
cv2.imshow('TITLE', imgresize)
cv2.waitKey(delay=2000)
cv2.destroyAllwindow()
