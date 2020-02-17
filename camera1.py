import cv2
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


counter=25
while counter:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break	
    if counter==1:
    	img_name = "d_{}.png".format(img_counter)
    	cv2.imwrite(img_name, frame)
    	print("{} written!".format(img_name))
    	img_counter += 1
    counter=counter-1

cam.release()
