import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# png 파일로 한다면 채널 3을 유지해야하기 때문에 IMREAD_UNCHANGED 필요
#img=cv.imread("resource/son_sig.png",cv.IMREAD_UNCHANGED)
img=cv.imread("resource/son.jpg")

# 오츄 이진화를 이용하여 컬러 영상을 이진 영상으로 만들어줌
t,bin_img=cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(bin_img,cmap='gray')     #cmap='gray'로 명암 영상으로 출력
plt.xticks([])
plt.yticks([])
plt.show()

b=bin_img[bin_img.shape[0]//4:bin_img.shape[0]*3//4,bin_img.shape[1]//4:bin_img.shape[1]*3//4]     #영상의 가운데 부분만 자르기
plt.imshow(b,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 구조 요소
se=np.uint8([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])

# 팽창
b_dilation=cv.dilate(b,se,iterations=1)
plt.imshow(b_dilation,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 침식
b_erosion=cv.erode(b,se,iterations=1)
plt.imshow(b_erosion,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 팽창 후 침식 (닫기)
b_closing=cv.erode(cv.dilate(b,se,iterations=1),se,iterations=1)
plt.imshow(b_closing,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 침식 후 팽창 (열기)
b_opening=cv.dilate(cv.erode(b,se,iterations=1),se,iterations=1)
plt.imshow(b_opening,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()