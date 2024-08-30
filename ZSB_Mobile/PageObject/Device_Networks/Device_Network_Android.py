from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ...Common_Method import Common_Method
from airtest.core.api import device as current_device
import os


import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\TestExecution\\test_Smoke_Test", a)
else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)
class Device_Networks_Android:
    pass

    def __init__(self, poco):
        self.poco = poco

    def wait_till_the_networks_list(self):
        self.poco(name="android.widget.ImageView").child("android.view.View").wait_for_appearance(timeout=30)

    def click_network_by_name(self,name):
        count=0
        while not self.poco(nameMatches=".*"+name+".*").exists() and count<10:
            self.poco.scroll()
            count+=1
        self.poco(nameMatches=".*"+name+".*").click()

    def check_the_wordings_in_connect_to_network(self):
        a = self.poco(nameMatches=".*Please enter the password.*"+".*the printer to this network.*").exists()
        b = self.poco(nameMatches=".*Connect to Network.*").exists()

        return a and b

    def click_on_cancel_button(self):
        try:
            self.poco("Cancel").click()
        except:
            self.poco("cancel").click()

    def enter_the_password(self,password):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(password)
        keyevent("enter")

    def click_on_connect(self):
        self.poco("Connect").click()

    def get_the_network_name_and_status(self):
        try:
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a,b
        except:
            self.poco.swipe([0.5,0.4],[0.5,0.9])
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a, b

    def swap_two_networks(self,netw1,netw2):
        temp2 = self.poco(nameMatches=".*" + ". " + netw2 + ".*").get_name()

        temp1 = self.poco(nameMatches=".*" + ". " + netw1 + ".*").get_name()

        temp2 = self.poco(temp2)
        temp1 = self.poco(temp1)

        temp2.drag_to(temp1)

    def check_add_network_button_enabled(self):
        while not self.poco("Add Network").exists():
            self.poco.scroll()
        a = self.poco("Add Network",enabled=True).exists()
        return a


    def get_network_names(self):
        temp = []
        for i in self.poco(type="android.widget.Button", nameMatches="[0-9]. .*"):
            temp.append(i.get_name())
        res=[]
        for i in temp:
            res.append(i[3:])
        return res

    def delete_the_network(self,name):
        pos = self.poco(type="android.widget.Button",nameMatches=".*"+name+".*").attr("pos")
        size = self.poco(type="android.widget.Button",nameMatches=".*"+name+".*").attr("size")

        right_middle_x = pos[0] + size[0] * 0.48

        right_middle_y = pos[1] - size[1] * 0.0

        self.poco.click([right_middle_x, right_middle_y])

    def wait_for_the_printer_to_connect_network(self,name):
        self.poco("Current Network").parent().child(name).wait_for_appearance(timeout=60)

    def turn_off_wifi(self):
        cmd = "adb shell svc wifi disable"
        self.run_the_command(cmd)

    def turn_on_cellular_data(self):
        cmd = "adb shell svc data enable"
        self.run_the_command(cmd)

    def turn_off_cellular_data(self):
        cmd = "adb shell svc data disable"
        self.run_the_command(cmd)

    def run_the_command(self, command):
        cmd = command

        # Using os.system() method
        a = os.system(cmd)
        return a

    def check_internet_disconnect_error(self):
        a = self.poco("Error\nThe service is currently unavailable.").exists()
        return a

    def check_sudden_network_off_error(self):
        a = self.poco("Error\nAn Unknown Error has Occured.").exists()
        b = self.check_internet_disconnect_error()
        return a or b

    def check_failed_to_connect_network_error(self):
        a = self.poco(nameMatches="(?s).*Printer failed to connect to Wifi Network. This could be caused by incorrect password, router rejecting the connection, or wifi network being out of range. Do you want to continue or cancel the changes?.*")

    def click_on_continue_in_network_disconnect_error(self):
        self.poco("Continue").click()

    def refresh_home_page(self):
        self.poco.swipe([0.5, 0.25], [0.5, 0.7], duration=0.5)
        sleep(2)

    def allow_nearby_devices_permission(self,allow=1):

        cmd = "adb shell am start -a android.settings.SETTINGS"
        self.run_the_command(cmd)
        sleep(2)
        try:
            try:
                try:
                    self.poco(text="Search settings").click()
                except:
                    self.poco(textMatches="Search").click()
                self.poco(type="android.widget.EditText").set_text("zsb")
                keyevent("enter")
                sleep(1)

                self.poco(textMatches=".*ZSB.*").click()
            except:
                pass

            self.poco(text="ZSB Series").click()
            self.poco(text="Permissions").click()
            self.poco(text="Nearby devices").click()
        except:
            pass

        if allow:
            self.poco(nameMatches=".*allow.*").click()
        else:
            self.poco(nameMatches=".*deny.*").click()

    def check_failed_network(self):
        a = self.poco(nameMatches="(?s).*Failed to Connect to Wifi Network.*").exists()
        return a

    def check_the_my_designs_internet_lost_error(self):
        a = self.poco("An error occurred when loading your designs. Please tap to try again").exists()

        return a















