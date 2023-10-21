from requests import get, post
import cv2 as cv
from os import system

res = get("https://hackattic.com/challenges/basic_face_detection/problem?access_token=b53b9d130f72e759").json()
system('wget -O tiles.png ' + res['image_url'] )
img = cv.imread('tiles.png')
w, h = img.shape[:2]
cropped = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(cropped, 1.3, 5)
ans = []
for (x,y,w,h) in faces:
  rx = x // 100
  ry = y // 100
  nx = rx * 100
  ny = ry * 100
  cv.rectangle(cropped,(nx,ny),(nx+100,ny+100),(255,255,0),2)
  ans.append([int(rx), int(ry)])
cv.imwrite("faces.png", cropped)
postRes = post('https://hackattic.com/challenges/basic_face_detection/solve?access_token=b53b9d130f72e759', json={"face_tiles": ans})
print(postRes.json())
