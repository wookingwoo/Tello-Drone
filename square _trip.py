from djitellopy import Tello

tello = Tello()

tello.connect()
print(f"battery: {tello.get_battery()}%")  # 배터리 잔량 확인

tello.takeoff()

SHORT_DISTANCE = 150
LONG_DISTANCE = 400

for i in range(2):
    print(f"{SHORT_DISTANCE}cm 전진")
    tello.move_forward(SHORT_DISTANCE)
    print("우측으로 90도 회전")
    tello.rotate_clockwise(90)
    print(f"{LONG_DISTANCE}cm 전진")
    tello.move_forward(LONG_DISTANCE)
    print("우측으로 90도 회전")
    tello.rotate_clockwise(90)

tello.land()
