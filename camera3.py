import cv2
import time

cam = cv2.VideoCapture(2)

cv2.namedWindow("test")

img_counter = 0

flag=True
while flag:
    time.sleep(3)
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    time.sleep(3)
    if not ret:
        break
    #k = cv2.waitKey(1)

#    if k%256 == 27:
        # ESC pressed
 #       print("Escape hit, closing...")
  #      break
   # elif k%256 == 32:
        # SPACE pressed
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    flag=False

cam.release()
