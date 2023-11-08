import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread("resource/cloudy.jpg")

# 명암 연산으로 변환
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

h=cv.calcHist([gray],[0],None,[256],[0,256])
plt.plot(h,color='g',linewidth=2)
plt.show()

# 히스토그램 평활화
equal=cv.equalizeHist(gray)
plt.imshow(equal,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

h=cv.calcHist([equal],[0],None,[256],[0,256])
plt.plot(h,color='b',linewidth=2)
plt.show()