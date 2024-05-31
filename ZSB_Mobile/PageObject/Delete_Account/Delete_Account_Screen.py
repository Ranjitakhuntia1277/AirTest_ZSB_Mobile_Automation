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

from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen import Login_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class Delete_Account_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.deleteAccount = "Delete Account"
        self.logOut = "Log Out"
        self.delete = "Delete"

    def checkIfDeleteAccountIsNextToLogOut(self):
        if self.poco(self.logOut).parent().child()[0].get_name() == "Delete Account":
            pass
        else:
            raise Exception("Delete Account is not next to Log Out")

    def clickDeleteAccount(self):
        self.poco(self.deleteAccount).click()

    def clickDelete(self):
        self.poco(self.delete).click()

    def clickOk(self):
        self.poco("Ok").click()

    def checkAccountDeletedDialog(self):
        try:
            self.poco("Account Deleted\nYour account has been successfully deleted.").wait_for_appearance(timeout=10)
        except:
            raise Exception("Account Deleted dialog did not appear.")

    def checkDeleteErrorDialog(self):
        try:
            self.poco("Delete Account Error\nYour account was unable to be deleted.").wait_for_appearance(timeout=10)
        except:
            raise Exception("Account Deleted dialog did not appear.")

    def wait_for_element_appearance_name_type(self, element_type, element_name, time_out=15):
        self.poco(type=element_type, name=element_name).wait_for_appearance(timeout=time_out)

    def checkThreeCheckboxesInDeleteAccountPage(self):
        self.poco("All data in your workspace will be removed.").click()
        self.poco("Your account will be de-identified, meaning it will not be associated with you.").click()
        self.poco("Ensure your printer is ON to factory reset your ZSB printer.").click()

    def clickCloseButtonInDeleteAccountPage(self):
        self.poco("Delete Account").parent().child()[0].click()

    def verifyImportantMessageOnSignInPage(self):
        try:
            self.poco(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.").wait_for_appearance(timeout=20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")

    def verifyNoImportantMessageOnSignInPage(self):
        try:
            self.poco(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.").wait_for_appearance(timeout=20)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" displayed without deleting the account.")
        except Exception as e:
            pass

    def verifyServiceUnavailableErrorPopUp(self):
        try:
            self.poco("Error\nThe service is currently unavailable.").wait_for_appearance(timeout=15)
        except:
            raise Exception("Pop up with message \"Error\nThe service is currently unavailable.\"  is not displayed.")

    def verifyNoPrinterInAccount(self):
        try:
            self.poco(
                nameMatches="(?s).*Add a printer to get started. We’ll help you set things up.*").wait_for_appearance(
                timeout=15)
        except:
            raise Exception("Printers are already added in this account.")

    def verifyNoPrinterInAccountWeb(self):
        try:
            self.poco(text="No Printers available").wait_for_appearance(timeout=15)
        except:
            raise Exception("Printers are already added in this account.")

    def VerifyIfNoRecentlyPrintedDesignsPresent(self):
        try:
            self.poco(
                text="Get started by printing labels from our common designs or create a new label design. Your recently printed labels will appear here.").wait_for_appearance(
                timeout=15)
        except:
            raise Exception("There are designs in recently printed designs.")

    def verifyIfOnEULAPageWeb(self):
        try:
            self.poco(text="End User License Agreement").wait_for_appearance(timeout=15)
        except:
            raise Exception("Did not reach EULA page")

    def AcceptEULAWeb(self):
        while not self.poco(text="Accept", enabled=True).exists():
            self.poco.scroll()
        self.poco(text="Accept").click()

    def verifyMyDataEmpty(self):
        try:
            self.poco(text="You don’t have any files").wait_for_appearance(timeout=15)
        except:
            try:
                self.poco("You don’t have any files").wait_for_appearance(timeout=15)
            except:
                raise Exception("My Data is not empty.")

    def verifyMyDesignsEmpty(self):
        try:
            self.poco(
                "There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.").wait_for_appearance(
                timeout=15)
        except:
            raise Exception("My Designs is not empty.")

    def verifyMyDesignsEmptyWeb(self):
        try:
            self.poco(text="You don’t have any designs").wait_for_appearance(timeout=15)
        except:
            raise Exception("My Designs is not empty.")

    def switch_to_different_app(self):
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)

    def change_first_name(self, first_name="new_first_name"):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(first_name)
        keyevent("back")
        sleep(4)

    def change_last_name(self, last_name="new_last_name"):
        self.poco("android.widget.EditText")[1].click()
        self.poco("android.widget.EditText")[1].set_text(last_name)
        keyevent("back")
        sleep(4)

    def change_unit_of_measurement(self):
        self.poco.scroll()
        self.poco(nameMatches="(?s).*Units of Measurement.*").click()
        self.poco("Centimetres").click()
        sleep(5)

    def selectFirstImage(self):
        self.poco("androidx.cardview.widget.CardView").click()

    def change_workspace_name(self, workspace_name="new workspace name"):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(workspace_name)
        keyevent("back")
        sleep(2)

    def verifyDefaultSettings(self):
        return_message = False
        try:
            assert_exists(Template(r"tpl1714996894841.png", record_pos=(-0.343, -0.588), resolution=(1080, 2340)),
                          "Please fill in the test point.")
        except:
            raise Exception("Profile photo is not default")
        if self.poco("android.widget.EditText").get_text() == self.first_name:
            if self.poco("android.widget.EditText")[1].get_text() == self.last_name:
                if self.poco(textMatches=".*.com.*").get_text() == "deletezsb@gmail.com":
                    return_message = True
        if not return_message:
            raise Exception("First name, Last name, Email not matching expected values.")
        self.poco.scroll()
        if self.poco(nameMatches="(?s).*Inches.*").exists():
            pass
        else:
            raise Exception("Inches is not default unit of measurement.")

    def verifyDefaultWorkspaceSettings(self):
        try:
            assert_exists(Template(r"tpl1714998188897.png", record_pos=(-0.343, -0.588), resolution=(1080, 2340)),
                          "Please fill in the test point.")
        except:
            raise Exception("Workspace photo is not default")
        if self.poco("android.widget.EditText").get_text() == "My First Workspace":
            pass
        else:
            raise Exception("Default workspace name is not \"My First Workspace\".")

    def verifyDefaultTheme(self):
        if self.poco("Modern").child("android.widget.RadioButton", checked=True).exists():
            pass
        else:
            raise Exception("Theme is not in default setting.")

    def verifyIfSeekBarIsDefault(self):
        if self.poco("100%").exists():
            pass
        else:
            raise Exception("Seekbar is not in default setting.")

    def checkIfThereIs1PrinterWithOnlineStatus(self):
        if self.poco(nameMatches="(?s).*Online.*").exists():
            pass
        else:
            raise Exception("There is no printer with Online status.")

    def checkIfThereIs1PrinterWithOfflineStatus(self):
        if self.poco(nameMatches="(?s).*Offline.*").exists():
            pass
        else:
            raise Exception("There is no printer with Offline status.")

    def clickContinueAsInFacebookLogin(self):
        try:
            self.poco(text="Continue as Zsb").wait_for_appearance(timeout=20)
            self.poco(text="Continue as Zsb").click()
        except:
            pass

    def verifyDeleteAccountDialogPopUp(self):
        try:
            self.poco(
                "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.").wait_for_appearance(timeout=20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")

    def checkTargetPrintersAvailable(self):
        try:
            self.poco("Select your printer").wait_for_appearance(timeout=20)
        except:
            raise Exception("target printers nor shown in printer list.")
