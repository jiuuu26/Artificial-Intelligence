'''
마우스를 통한 상호작용
''' 

import cv2 as cv
import sys

img=cv.imread("resource/son.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

img = cv.resize(img, dsize=(0,0),fx=1.5,fy=1.5)

def draw(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+200,y+200),(0,255,0),2)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),2)

    cv.imshow("Drawing",img)

cv.namedWindow("What is this")
cv.imshow("Drawing",img)

cv.setMouseCallback("Drawing", draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break