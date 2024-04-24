from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method

from ZSB_Mobile.PageObject.Login_Screen import Login_Screen


class Feed_on_HeadClose:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Open_navigation_menu = "Open navigation menu"
        self.Printer_Settings_Btn = "Printer Settings"
        self.ZSB_DP14 = "ZSB-DP14\nTab 2 of 2"
        self.ZSB_DP12 = "ZSB-DP12\nTab 2 of 2"
        # self.icon = "android.widget.Switch"
        self.android_widget_button = "android.widget.Button"
        self.feed_on_close_text = Template(r"tpl1704697508294.png", record_pos=(0.009, -0.125), resolution=(1080, 2340))
        self.Label_alignment_demo = "Label Alignment Demo"
        self.Label_alignment_video = Template(r"tpl1704698058775.png", record_pos=(-0.002, -0.025),resolution=(1080, 2340))
        self.touch_to_cancel = Template(r"tpl1704705761537.png", record_pos=(0.212, 0.548), resolution=(1080, 2340))

    def click_navigation_menu(self):
        navigate_menu = self.poco(self.Open_navigation_menu)
        navigate_menu.click()

    def click_Printer_Settings(self):
        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def click_selected_printer(self):
        zsb_printer = self.poco(self.ZSB_DP12)
        zsb_printer.click()

    def click_icon(self):
        icon = self.poco(self.android_widget_button)
        icon.click()

    def verify_text(self):

        temp=assert_exists(self.feed_on_close_text, "ok")
        temp = "ok"
        if temp == "ok":
            return "success"
        else:
            return "failed"


    def click_demo_video(self):
        alignment_demo = self.poco(self.Label_alignment_demo)
        alignment_demo.click()

    def verify_demo_video(self):
        temp = assert_exists(self.Label_alignment_video, "ok")

        if temp == "ok":
            return "passed"
        else:
            return "failed"

    def click_to_exit_demo_video(self):

        touch(self.touch_to_cancel)



