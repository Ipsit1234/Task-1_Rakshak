import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('minions.jpg')   #provide the input path here

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
image1 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

blue_lower = np.array([110,50,50])
blue_upper = np.array([130,255,255])

green_lower = np.array([50,50,50])
green_upper = np.array([70,255,255])

red_lower = np.array([0,50,50])
red_upper = np.array([10,255,255])

mask1 = cv2.inRange(hsv,blue_lower,blue_upper)
mask2 = cv2.inRange(hsv,green_lower,green_upper)
mask3 = cv2.inRange(hsv,red_lower,red_upper)

mask1 = cv2.cvtColor(mask1,cv2.COLOR_GRAY2BGR)
mask2 = cv2.cvtColor(mask2,cv2.COLOR_GRAY2BGR)
mask3 = cv2.cvtColor(mask3,cv2.COLOR_GRAY2BGR)

mask1 = cv2.bitwise_and(image1, mask1)
mask2 = cv2.bitwise_and(image1, mask2)
mask3 = cv2.bitwise_and(image1, mask3)

images = [image1,mask1,mask2,mask3]
titles = ['Original','Blue_only','Green_only','Red_only']
for i in range(4) :
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


