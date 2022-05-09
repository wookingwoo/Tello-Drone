from djitellopy import Tello

me = Tello()
me.connect_to_wifi("SSID", "PW")
print(me.get_battery())  # 배터리 잔량 확인
