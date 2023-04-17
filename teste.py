import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ii = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    #conv = cv2.cvtColor(frame, cv2.COLOR_BGR2BGR)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('s'):
        ii += 1
        cv2.imwrite('framecap{}.png'.format(ii),frame)
        img = cv2.imread('framecap{}.png'.format(ii),1)
        cv2.imshow('frame capture',img)

cap.release()
cv2.destroyAllWindows()