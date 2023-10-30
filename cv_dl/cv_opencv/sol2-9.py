import cv2 as cv
import sys

img=cv.imread("resource/son.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

Brushsiz=5
LColor, RColor = (255,0,0),(0,0,255)

def painting(event, x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:   # 좌클릭 시
        cv.circle(img,(x,y),Brushsiz,LColor,-1)
    elif event == cv.EVENT_RBUTTONDOWN: # 우클릭 시
        cv.circle(img,(x,y),Brushsiz,RColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:    #좌 클릭한 상태로 이동시
        cv.circle(img,(x,y),Brushsiz,LColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:    #우 클릭한 상태로 이동시
        cv.circle(img,(x,y),Brushsiz,RColor,-1)

    # 수정된 영상을 윈도우에 다시 디스플레이
    cv.imshow("Painting",img)


cv.namedWindow("Painting")
cv.imshow("Painting",img)

cv.setMouseCallback("Painting", painting)

# 아래의 무한루프가 없다면 콜백 함수 등록 후 프로그램이 종료됨
while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows
        break