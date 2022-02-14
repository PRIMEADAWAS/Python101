import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADAWAS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


img = cv2.imread('wow.jpg')
# img = cv2.cvtColor(img, cv2.COLORE_BGR2RGB)
# print(img.shape)
hImg, wimg, c = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'

# all text
txtAll = tess.image_to_string(img)
# print(txtAll)


# text with position x,y,w,h
# texts = tess.image_to_boxes(img, config=conf)
# # print(texts)
# for text in texts.splitlines():
#     text = text.split(' ')
#     x, y, x2, y2 = int(text[1]), int(text[2]), int(text[3]), int(text[4])
#     # print(text[0], x, y, w, h)
#     cv2.rectangle(img, (x, hImg-y), (x2, hImg-y2), (0, 255, 0), 1)
#     cv2.putText(img, text[0], (x, hImg-y+10),
#                 cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 255, 0), 1)


# group word x,y,w,h
texts = tess.image_to_data(img)
# print(texts)
for x, text in enumerate(texts.splitlines()):
    if x:
        text = text.split()
        # print(text)
        if len(text) == 12:
            # print(text)
            x, y, w, h = int(text[6]), int(
                text[7]), int(text[8]), int(text[9])
            # print(text[0], x, y, w, h)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv2.putText(img, text[11], (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 255, 0), 1)


imgresize = cv2.resize(img, (1280, 720))
cv2.imshow("tesserect", imgresize)
cv2.waitKey(0)
