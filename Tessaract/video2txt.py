import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADAWAS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


webcam = cv2.VideoCapture(0)

while (True):
    result, img = webcam.read()

    hImg, wimg, c = img.shape

# texts = tess.image_to_data(img)
    for x, text in enumerate(texts.splitlines()):
        if x:
            text = text.split()
            if len(text) == 12:
                x, y, w, h = int(text[6]), int(
                    text[7]), int(text[8]), int(text[9])
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.putText(img, text[11], (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 255, 0), 1)

# text with position x,y,w,h
    # texts = tess.image_to_boxes(img)
    # # print(texts)
    # for text in texts.splitlines():
    #     text = text.split(' ')
    #     x, y, x2, y2 = int(text[1]), int(text[2]), int(text[3]), int(text[4])
    #     # print(text[0], x, y, w, h)
    #     cv2.rectangle(img, (x, hImg-y), (x2, hImg-y2), (0, 255, 0), 1)
    #     cv2.putText(img, text[0], (x, hImg-y+10),
    #                 cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 255, 0), 1)

    cv2.imshow("Text detection", img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

webcam.release()
cv2.destroyAllWindows()
