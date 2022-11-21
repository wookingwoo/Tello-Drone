from djitellopy import Tello

tello = Tello()

tello.connect()
print(f"battery: {tello.get_battery()}%")  # 배터리 잔량 출력
print(f"temperature: {tello.get_temperature()}°C")  # 드론 온도 출력

tello.takeoff()

SHORT_DISTANCE = 140
LONG_DISTANCE = 400

for i in range(2):
    print(f"{SHORT_DISTANCE}cm 전진")
    tello.move_forward(SHORT_DISTANCE)
    tello.flip_right()  # 우측으로 플립
    print("우측으로 90도 회전")
    tello.rotate_clockwise(90)
    print(f"{LONG_DISTANCE}cm 전진")
    tello.move_forward(LONG_DISTANCE)
    tello.flip_right()  # 우측으로 플립
    print("우측으로 90도 회전")
    tello.rotate_clockwise(90)

tello.move_back(17)
tello.rotate_clockwise(360)
tello.flip_forward()  # 전방으로 플립
tello.move_left(3)

tello.land()
