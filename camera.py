'''
    Self Timer Camera
    By : Ashutosh Maheshwari
'''
import pygame.camera
import pygame.image
import time
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
print("SELF TIMER\nEnter the time duration in seconds: ");
num = int(input())
cam.start()
while num > 0:
    if num <= 3:
        print(str(num)+" seconds left\n")
    if num==1:
        print("Say CHEESE\n")
    time.sleep(1)
    num -= 1
time.sleep(3)
img = cam.get_image()
pygame.image.save(img, "self_timer.jpg")
pygame.camera.quit()
