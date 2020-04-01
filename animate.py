from PIL import Image


class gif:
    def __init__(self, name, fps, optimize=False, loop=0):
        self.name = name
        
        self.pictures = []
        self.frame = 0
        self.fps = fps
        self.optimize = optimize
        self.loop = loop
    
    def add_picture(self, picture):
        if type(picture) == list():
            self.pictures += picture
        else:
            #TODO: check picture is image
            self.pictures.append(picture)
        
        self.frame = len(self.pictures)
        
    def extract(self):
        if self.frame <= 1:
            raise Exception("frame is less than 2.")
        self.pictures[0].save(f'data/{self.name}.gif',
               save_all=True, append_images=self.pictures[1:], optimize=self.optimize, duration=1000/self.fps, loop=self.loop)