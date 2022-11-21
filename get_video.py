from djitellopy import tello
import cv2
from time import sleep

me = tello.Tello()
me.connect()

print(me.get_battery())
me.streamon()

WINDOW_SCALE = 3

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360 * WINDOW_SCALE, 240 * WINDOW_SCALE))
    cv2.imshow("Image", img)
    cv2.waitKey(2)
