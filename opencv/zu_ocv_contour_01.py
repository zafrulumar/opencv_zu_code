import numpy as np
import cv2

def empty(a):
    pass

img = cv2.imread('Resource\images\oc01.jpg')

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Threshold","TrackBars",0,255,empty)
cv2.createTrackbar("Maxvalue","TrackBars",0,255,empty)
cv2.createTrackbar("blr1","TrackBars",0,255,empty)
cv2.createTrackbar("blr2","TrackBars",0,255,empty)

while True:

    th = cv2.getTrackbarPos("Threshold","TrackBars")
    mv = cv2.getTrackbarPos("Maxvalue", "TrackBars")
    b1 = cv2.getTrackbarPos("blr1", "TrackBars")
    b2 = cv2.getTrackbarPos("blr2", "TrackBars")

    blurred = cv2.pyrMeanShiftFiltering(img, b1, b2)
    imgray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray,  th, mv, 0)
    cv2.imshow('Threshold', thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of contours = " + str(len(contours)))
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)


#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print("Number of contours = " + str(len(contours)))
#print(contours)

#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
#cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

#cv2.imshow('Image', img)
#cv2.imshow('Image GRAY', imgray)
#cv2.waitKey(0)
cv2.destroyAllWindows()