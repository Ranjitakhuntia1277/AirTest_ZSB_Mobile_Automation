import datetime
import time
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class Delete_Account_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.deleteAccount = poco("Delete Account")
        self.logOut = poco("Log Out")

    def checkIfDeleteAccountIsNextToLogOut(self):
        if self.logOut.parent().child()[0].get_name() == "Delete Account":
            pass
        else:
            raise Exception("Delete Account is not next to Log Out")

    def clickDeleteAccount(self):
        self.deleteAccount.click()

    def wait_for_element_appearance_name_type(self, element_type, element_name, time_out=15):
        self.poco(type=element_type, name=element_name).wait_for_appearance(timeout=time_out)

    def checkThreeCheckboxesInDeleteAccountPage(self):
        self.poco("All data in your workspace will be removed.").click()
        self.poco("Your account will be de-identified, meaning it will not be associated with you.").click()
        self.poco("Ensure your printer is ON to factory reset your ZSB printer.").click()

    def clickCloseButtonInDeleteAccountPage(self):
        self.poco("Delete Account").parent().child()[0].click()