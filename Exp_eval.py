import cv2
from PIL import Image
from pytesseract import image_to_string
cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 1, 1, 0, 1)
t = 0
k = 0
while True:
    rect, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('sample2.jpg', gray[100:180, 100:500])
    cv2.rectangle(img, (100, 100), (500, 180), (50, 30, 100), 2)
    #img = cv2.flip(img, 1)
    cv2.cv.PutText(cv2.cv.fromarray(img), str(k), (100, 200), font, (2, 10, 255))
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    im = Image.open('sample2.jpg')
    text = image_to_string(im, lang="en")
    l = text
    print(l)
    try:
        k = eval(str(l))
        cv2.cv.PutText(cv2.cv.fromarray(img), str(k), (100, 200), font, (2, 10, 255))
        cv2.imshow('img', img)
        print(str(l))
        print(k)
    except:
        pass







