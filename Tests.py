import unittest
from AnimatronicEyes import *


class EyeTestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.eyes = AnimatronicEyes()

    def test_bonnie_left_door(self):
        expected = True
        self.assertEqual(self.eyes.analyze('danger.png', DOORWAY_LEFT), expected)
