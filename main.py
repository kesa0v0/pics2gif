from unit import *

if __name__ == "__main__":
    obj0 = Moveable_object(picture="data/picture/unnamed.png")
    obj0.speed_x = 10
    obj0.speed_y = -10
    obj0.acceleration_x = 5
    obj0.acceleration_y = -5

    screen = Screen((1920, 1080), "ext60", fps=50)
    screen.add_object(obj0)
    for i in range(0, 60):
        screen.render()  # 이미지 생성
        screen.update()  # 물체 업데이트

    screen.extract()