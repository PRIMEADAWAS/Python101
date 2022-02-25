import cv2
import numpy as np
from PIL import ImageGrab
import time
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADAWAS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


count = 0
while (True):
    printscreen = np.array(ImageGrab.grab(bbox=(20, 40, 950, 1000)))
    img = printscreen
    count = count + 1
    # print(count)
    if(count):
        hImg, wimg, c = img.shape
        texts = tess.image_to_data(img)
        for x, text in enumerate(texts.splitlines()):
            if x:
                text = text.split()
                if len(text) == 12:
                    x, y, w, h = int(text[6]), int(
                        text[7]), int(text[8]), int(text[9])
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    cv2.putText(img, text[11], (x, y),
                                cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 255, 0), 1)

    cv2.imshow("Screeen Text detection", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
