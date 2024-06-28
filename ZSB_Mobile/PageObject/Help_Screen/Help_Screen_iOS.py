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

    def chooseAcc(self, Acc_Name="zsbswdvt@gmail.com"):
        account = self.poco(Acc_Name)
        account.click()

