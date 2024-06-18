from platform import platform

import pytest
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from airtest.core.api import device as current_device
import os


def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates", a)


class Others:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.capture_image_button = "PhotoCapture"


    def capture_the_image_button(self):
        take_img_btn = self.poco(self.capture_image_button)
        take_img_btn.click()
