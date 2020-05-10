from PIL import Image
from os import path, mkdir


class gif:
    def __init__(self, name, pictures=[], fps=15, optimize=False, loop=0):
        self.name = name

        self.pictures = pictures
        self.frame_len = 0
        self.fps = fps
        self.optimize = optimize
        self.loop = loop

    def add_picture(self, picture):
        if type(picture) == list():
            self.pictures += picture
        else:
            # TODO: check picture is image
            self.pictures.append(picture)

        self.frame_len = len(self.pictures)

    def extract(self):
        if self.frame_len <= 1:
            raise Exception("frame length is less than 2.")
        if not path.isdir('./data/ext'):
            mkdir('./data/ext')

        self.pictures[0].save(f'data/ext/{self.name}.gif',
                              save_all=True, append_images=self.pictures[1:], optimize=self.optimize,
                              duration=1000/self.fps, loop=self.loop)
