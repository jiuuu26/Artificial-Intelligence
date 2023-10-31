import cv2 as cv
import sys

img=cv.imread("resource/son.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.imshow("original",img)
# 좌측 위
cv.imshow("Upper left half",img[0:img.shape[0]//2,0:img.shape[1]//2,:])
# 가운데
cv.imshow("Center half",img[img.shape[0]//4:img.shape[0]*3//4,img.shape[1]//4:img.shape[1]*3//4,:])

cv.imshow("R channel",img[:,:,2])   # 빨간 부분이 밝음
cv.imshow("G channel",img[:,:,1])   # 초록 부분이 밝음
cv.imshow("B channel",img[:,:,0])   # 파란 부분이 밝음


cv.waitKey()
cv.destroyAllWindows()
