from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self, image):
        self.image = image
        self.original = None
        self.changed = []
    def open(self):
        try:
            self.original = Image.open(self.image)
        except:
            print("Image not found, 404")
        self.original.show()
    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        temp_image = self.image.split(".")
        new_image = temp_image[0]+str(len(self.changed))+".jpg"
        rotated.save(new_image)
    def crop(self):
        box = (40, 10, 60, 40)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        temp_image = self.image.split(".")
        new_image = temp_image[0]+str(len(self.changed))+".jpg"
        cropped.save(new_image)

MyImage = ImageEditor("originalo.jpg")
MyImage.open()
MyImage.do_left()
MyImage.crop()

for im in MyImage.changed():
    im.show()