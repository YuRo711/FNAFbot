from pynput import keyboard, mouse
import pyautogui
import time
from AnimatronicEyes import *


CAM_PANEL = (792, 857)
LEFT = [(373, 651), (375, 555), (512, 532)]
RIGHT = [(1528, 652), (1532, 530), (1388, 543)]
CAMERAS = {
    "1A": (1309, 546),
    "1B": (1275, 608),
    "1C": (1257, 677),
    "2A": (1294, 797),
    "2B": (1306, 837),
    "4A": (1397, 801),
    "4B": (1405, 836),
    "7": (1527, 622)
}


class Animatronic:
    def __init__(self):
        self.freddy_count = 0
        self.freddy_room = "1A"
        self.bonnie_room = "1A"
        self.chika_room = "1A"
        self.room = "1A"
        self.cameras = False
        self.door = LEFT
        self.sleep = 0.7
        self.eyes = AnimatronicEyes()
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        my_mouse = mouse.Listener(on_click=self.coordinates)
        # my_mouse.start()

    def coordinates(self, x, y, button, pressed):
        if self.eyes.see_danger(self.door[2]):
            self.door_alarm()

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.door_alarm()
        elif key == keyboard.Key.ctrl:
            self.cam_alarm()
        elif key == keyboard.Key.enter:
            self.freddy_hear()
        elif key == keyboard.Key.shift:
            self.cameras_routine()
        elif key == keyboard.Key.left:
            self.check_door(LEFT)
        elif key == keyboard.Key.right:
            self.check_door(RIGHT)

    def cameras_routine(self):
        pyautogui.click(CAM_PANEL)
        self.cameras = True
        if self.freddy_room != "6":
            self.check_camera(self.freddy_room)
            time.sleep(self.sleep)
        self.check_camera("1C")
        time.sleep(self.sleep)
        self.check_camera("2A")
        time.sleep(self.sleep)
        self.check_camera("4A")
        time.sleep(self.sleep)
        pyautogui.click(CAM_PANEL)
        self.cameras = False
        pyautogui.click(810, 540)

    def check_camera(self, cam):
        if self.room != cam:
            self.room = cam
            pyautogui.click(CAMERAS[cam])

    def cam_alarm(self):
        if self.room == self.freddy_room or self.room == "1C":
            pyautogui.click(CAM_PANEL)
            self.cameras = False

    def door_alarm(self):
        pyautogui.click(self.door[1])

    def freddy_hear(self):
        self.freddy_count += 1
        if self.freddy_count == 1:
            self.freddy_room = "1B"
        elif self.freddy_count == 2:
            self.freddy_room = "7"
        elif self.freddy_count == 3:
            self.freddy_room = "6"
        elif self.freddy_count == 4:
            self.freddy_room = "4B"

    def check_door(self, door):
        pyautogui.click(door[0])
        if self.eyes.see_danger(self.door[2]):
            self.door_alarm()
        time.sleep(0.2)
        pyautogui.click(door[0])


ani = Animatronic()
while True:
    pass
