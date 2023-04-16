import cv2

path = "test.jpg"
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

lists = cascade.detectMultiScale(img_gray, minSize=(100, 100))

if len(lists):
  for (x, y, w, h) in lists:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
  cv2.imshow('img', img)
  cv2.waitKey(0)
else:
  print('Nothing')
  