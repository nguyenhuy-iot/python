import cv2
cam=cv2.VideoCapture(0)
while True:
    ret,f=cam.read()
    pic=cv2.cvtColor(f,1)
    cv2.imshow('frame',pic)

    k=cv2.waitKey(1)
    if(k==113):
        break
cam.release()
cv2.destroyAllWindows()