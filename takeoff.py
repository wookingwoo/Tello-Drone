from djitellopy import Tello
import time

me = Tello()
me.connect()
print(me.get_battery())  # 배터리 잔량 확인 가능

me.takeoff()  # 기체 이륙
time.sleep(1)
me.land()  # 기체 착륙
