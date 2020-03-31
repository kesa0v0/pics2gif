from PIL import Image


class gif:
    def __init__(self, fps):
        self.pictures = []
        self.frame = 0
        self.fps = fps
    
    def add_picture(self, picture):
        if type(picture) == list():
            self.pictures += picture
        else:
            #TODO: check picture is image
            self.pictures.append(picture)
        
        self.frame = len(self.pictures)
        
    def extract(self):
        if self.frame <= 0:
            raise Exception("blank frame.")
        
    




if __name__ == "__main__":
    gif = gif(15)
    gif.extract()