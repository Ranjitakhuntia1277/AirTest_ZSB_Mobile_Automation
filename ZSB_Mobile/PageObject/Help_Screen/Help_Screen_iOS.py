# LoginFunction.py
from platform import platform

# import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
# from pipes import Template
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.assertions import assert_exists, assert_equal
from airtest.core.api import *
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from airtest.core.api import device as current_device
from ZSB_Mobile.Common_Method import *


common_method = Common_Method(poco)


class Help_Screen:
    pass


    def __init__(self, poco):
        self.poco = poco

    def chooseAcc(self, Acc_Name="zebra03.swdvt@gmail.com"):
        sleep(7)
        account = self.poco(Acc_Name)
        count = 0
        while not account.exists() and count <= 2:
            sleep(2)
            start_point = (0.57, 0.47)
            vector = (0.297, 0.211)
            count += 1
            swipe(start_point, vector)
            sleep(2)
            count += 1
        account.click()
        sleep(4)

    def checkIfOnSignInPage(self):
        try:
            self.poco("Sign In").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach \"Sign In\" page.")

