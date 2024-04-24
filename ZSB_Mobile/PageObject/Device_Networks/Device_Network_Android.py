from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import device as current_device
import os


def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",a)
class Device_Networks_Android:
    pass

    def __init__(self, poco):
        self.poco = poco

    def wait_till_the_networks_list(self):
        self.poco(name="android.widget.ImageView").child("android.view.View").wait_for_appearance(timeout=20)

    def click_network_by_name(self,name):
        while not self.poco(nameMatches=".*"+name+".*").exists():
            self.poco.scroll()
        self.poco(nameMatches=".*"+name+".*").click()

    def check_the_wordings_in_connect_to_network(self):
        a = self.poco(nameMatches=".*Please enter the password.*"+".*the printer to this network.*").exists()
        b = self.poco(nameMatches=".*Connect to Network.*").exists()

        return a and b

    def click_on_cancel_button(self):
        self.poco("Cancel").click()
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
            res.append(i.split(" ")[1])
        return res

    def delete_the_network(self,name):
        self.poco(nameMatches=".*"+name+".*").focus([0.92, 0.5]).click()














