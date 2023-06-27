import pyautogui
from PIL import Image


DOORWAY_LEFT = (512, 532)
DOORWAY_RIGHT = (1388, 543)


class AnimatronicEyes:
    def see_danger(self, door):
        screenshot = pyautogui.screenshot()
        screenshot.save('1.png')
        self.analyze('1.png', door)

    @staticmethod
    def analyze(image, door):
        im = Image.open(image)
        pix = im.load()
        if pix[door] != (0, 0, 0) and pix[door] != (33, 11, 11) and pix[door] != (0, 5, 6):
            print(pix[door])
            return True
        return False
