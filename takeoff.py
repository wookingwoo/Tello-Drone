from djitellopy import Tello
import time

me = Tello()
me.connect()

print(f"battery: {me.get_battery()}%")  # 배터리 잔량 출력
print(f"temperature: {me.get_temperature()}°C")  # 드론 온도 출력

me.takeoff()  # 기체 이륙
time.sleep(1)
me.land()  # 기체 착륙
