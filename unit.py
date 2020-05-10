from PIL import Image
import animate


class Object:
    def __init__(self, x=0, y=0, picture=None):
        self.x = x
        self.y = y

        try:
            self.picture = Image.open(picture)  # 사진 지정
        except:
            print(f"ERROR: Cannot open image file : {picture}")
            self.picture = None

    def update(self):
        pass


class Moveable_object(Object):
    def __init__(self, x=0, y=0, picture=None):
        super().__init__(x, y, picture)
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        super().update()
        self.x += self.speed_x
        self.y -= self.speed_y
        self.speed_x += self.acceleration_x
        self.speed_y += self.acceleration_y


class Screen:
    def __init__(self, resolution, name, fps=15, optimize=False, loop=0):
        self.resolution = resolution
        self.components = []
        if fps > 50:
            fps = 50
        self.gif = animate.gif(name, [], fps, optimize, loop)  # gif 클래스 만들기

    def update(self):  # 물체 업데이트
        for component in self.components:
            component.update()

    def add_object(self, obj):
        self.components.append(obj)

    def render(self):
        # TODO: rendering picture
        self.frame = Image.new("RGBA", self.resolution, (255, 255, 255, 0))  # 한 프레임 바탕 만들기

        for component in self.components:  # 사진 붙여넣기
            self.frame.paste(component.picture,
                             (component.x, component.y,
                              component.picture.size[0] + component.x,
                              component.picture.size[1] + component.y))

        # self.frame.show()

        self.gif.add_picture(self.frame)   #gif에 프레임 추가

    def extract(self):
        self.gif.extract()