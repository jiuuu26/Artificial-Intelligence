import cv2 as cv
import sys

img=cv.imread("resource/son.jpg")

t,bin_img=cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print("오츄 알고리즘의 최적 임계값 ",t)

cv.imshow("original",img)
cv.imshow("otsu",bin_img)

cv.imwrite("resource/otsu.jpg",bin_img)

cv.waitKey()
cv.destroyAllWindows()
