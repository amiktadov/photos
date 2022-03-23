from PIL import Image as Img, ImageFilter

class Image:
    def __init__(self, image) -> None:
        self.image = Img.open(image)
        self.bright = 0
        self.contrast = 0
        self.bw = 0

    def Blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def Contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)

    def Resize(self, x, y):
        self.image.thumbnail((x, y))


