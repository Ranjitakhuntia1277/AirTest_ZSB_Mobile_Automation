from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout

from ZSB_Mobile.Common_Method import Common_Method
import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\\templates",
                            a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)

common_method = Common_Method(poco)


class Delete_Account_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.logOut = "Log Out"
        self.deleteAccount = "Delete Account"
        self.delete = "Delete"
        self.continue_disabled = Template(Basic_path(r"continue_disabled.png"), record_pos=(0.332, 0.883), resolution=(1170, 2532))
        self.continue_enabled = Template(Basic_path(r"continue_enabled.png"), record_pos=(0.332, 0.883), resolution=(1170, 2532))
        self.assistive_touch = Template(Basic_path(r"assistive_touch.png"), record_pos=(0.397, -0.01), resolution=(1170, 2532))
        self.lock_phone = Template(Basic_path(r"lock_screen.png"), record_pos=(0.23, -0.038), resolution=(1170, 2532))

    def checkIfDeleteAccountIsNextToLogOut(self):
        sleep(2)
        if self.poco(self.logOut).parent().child("Delete Account").exists():
            pass
        else:
            raise Exception("Delete Account is not next to Log Out")
        sleep(2)

    def clickDeleteAccount(self):
        sleep(2)
        self.poco(self.deleteAccount).click()

    def clickDelete(self):
        sleep(4)
        self.poco(self.delete).click()

    def check_if_on_delete_account_page(self):
        try:
            self.poco(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.").wait_for_appearance(
                timeout=20)
        except:
            raise Exception("Delete account page did not show up.")

    def check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page(self):
        sleep(2)
        try:
            assert_exists(self.continue_disabled)
            pass
        except:
            raise Exception("Continue enabled without checking the three check boxes.")

    def acknowledge_three_checkboxes_in_delete_account_page(self):
        try:
            self.poco("Please acknowledge the following to continue:").wait_for_appearance(timeout=20)
            self.poco(name="All data in your workspace will be removed.").wait_for_appearance(timeout=20)
            self.poco(
                name="Your account will be de-identified, meaning it will not be associated with you.").wait_for_appearance(
                timeout=20)
            self.poco(name="Ensure your printer is ON to factory reset your ZSB printer.").wait_for_appearance(
                timeout=20)
        except:
            raise Exception("Three checkboxes not present to acknowledge.")

    def checkThreeCheckboxesInDeleteAccountPage(self):
        self.poco("All data in your workspace will be removed.").click()
        self.poco("Your account will be de-identified, meaning it will not be associated with you.").click()
        self.poco("Ensure your printer is ON to factory reset your ZSB printer.").click()

    def check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page(self):
        sleep(2)
        try:
            assert_exists(self.continue_enabled)
            pass
        except:
            raise Exception("Continue disabled even after checking the three check boxes.")

    def clickCloseButtonInDeleteAccountPage(self):
        self.poco("Delete Account").parent().child("Button").click()

    def check_if_back_to_settings_page(self):
        try:
            self.poco("Settings").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not return to settings page.")

    def check_notice_information_on_login_page_after_choosing_delete_account(self):
        try:
            self.poco("Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.").wait_for_appearance(timeout=20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")

    def check_final_delete_account_pop_up(self):
        sleep(10)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        try:
            self.poco("To complete the ZSB account deletion process, select Delete.").wait_for_appearance(timeout=20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")

    def check_if_delete_account_pop_up_displayed_even_after_clicking_cancel(self):
        try:
            self.poco("To complete the ZSB account deletion process, select Delete.").wait_for_appearance(timeout=20)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception(
                "Delete account dialog popped up after canceling delete account and re-loging into the same account.")
        except Exception as e:
            pass

    def checkAccountDeletedDialog(self):
        try:
            self.poco("Your account has been successfully deleted.").wait_for_appearance(timeout=20)
        except:
            raise Exception("Account Deleted dialog did not appear.")

    def clickOk(self):
        sleep(3)
        self.poco("Ok").click()

    def verifyNoPrinterInAccount(self):
        try:
            self.poco(
                nameMatches="(?s).*Add a printer to get started. We’ll help you set things up.*").wait_for_appearance(
                timeout=20)
        except:
            raise Exception("Printers are already added in this account.")

    def verifyMyDataEmpty(self):
        try:
            self.poco("You don’t have any files").wait_for_appearance(timeout=20)
        except:
            raise Exception("My Data is not empty.")

    def verifyMyDesignsEmpty(self):
        try:
            self.poco(
                "There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.").wait_for_appearance(
                timeout=20)
        except:
            raise Exception("My Designs is not empty.")

    def verifyNoImportantMessageOnSignInPage(self):
        try:
            self.poco(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.").wait_for_appearance(
                timeout=20)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" displayed without deleting the account.")
        except Exception as e:
            pass

    def click_Cancel_Btn(self):
        sleep(10)
        self.poco(name="Cancel").click()
        sleep(2)

    def verifyServiceUnavailableErrorPopUp(self):
        try:
            self.poco("The service is currently unavailable.").wait_for_appearance(timeout=20)
        except:
            raise Exception("Pop up with message \"Error\nThe service is currently unavailable.\"  is not displayed.")

    def enable_Wi_Fi(self):
        sleep(2)
        start_app("com.apple.Preferences")
        sleep(2)
        self.poco("Wi-Fi").click()
        sleep(2)
        Wi_Fi_toggle = self.poco(type="Switch", name="Wi‑Fi")
        switch_value = Wi_Fi_toggle.attr("value")
        if switch_value == "0":
            Wi_Fi_toggle.click()
        stop_app("com.apple.Preferences")

    def disable_Wi_Fi(self):
        sleep(2)
        start_app("com.apple.Preferences")
        sleep(2)
        self.poco("Wi-Fi").click()
        sleep(2)
        Wi_Fi_toggle = self.poco(type="Switch", name="Wi‑Fi")
        switch_value = Wi_Fi_toggle.attr("value")
        if switch_value == "1":
            Wi_Fi_toggle.click()
        stop_app("com.apple.Preferences")

    def lock_device(self):
        sleep(2)
        touch(self.assistive_touch)
        sleep(2)
        touch(self.lock_phone)

    def unlock_device(self):
        sleep(2)
        keyevent("HOME")
        sleep(2)
        keyevent("HOME")
        sleep(3)

    def open_zsb_app(self):
        keyevent("HOME")
        sleep(3)
        self.poco("Search").click()
        sleep(2)
        if self.poco("Clear text").exists():
            self.poco("Clear text").click()
            sleep(2)
        text("ZSB Series")
        sleep(2)
        self.poco("ZSB Series").click()

    def switch_to_different_app(self):
        sleep(2)
        start_app("com.apple.AppStore")
        sleep(2)

    def open_zsb_portal_web(self):
        self.poco("kToolbarNewTabButtonIdentifier").click()
        sleep(2)
        self.poco("Search or type URL").click()
        sleep(2)
        text("https://zsbportal.zebra.com/")
        sleep(5)
        if self.poco("Home").exists():
            self.poco("Zebra Small Office Home Office").child("Other").child("Link").click()
            sleep(2)
            touch(Template(r"tpl1725248704554.png", record_pos=(0.05, -0.571), resolution=(1170, 2532)))
            sleep(2)
            self.poco("Zebra Small Office Home Office").child("Other").child("Link").click()
            sleep(2)
            self.poco("Log Out").click()
            sleep(3)
            self.poco("Back").swipe([0.0059, 0.0])
            sleep(5)
        self.poco("Sign In With").wait_for_appearance(timeout=20)

    def checkDeleteErrorDialog(self):
        try:
            self.poco("Your account was unable to be deleted.").wait_for_appearance(timeout=20)
        except:
            raise Exception("Account Deleted dialog did not appear.")

    def verifyIfOnEULAPageWeb(self):
        try:
            self.poco("End User License Agreement").wait_for_appearance(timeout=15)
        except:
            raise Exception("Did not reach EULA page")

    def accept_EULA_web(self):
        sleep(4)
        count = 0
        while count <= 100:
            sleep(2)
            start_point = (0.57, 0.47)
            vector = (0.297, 0.211)
            count += 1
            swipe(start_point, vector)
            sleep(2)
            if self.poco("\"ZSB Printing Services\" means applications, functionality, application\nprogramming interfaces, communications, features, and other services\nprovided by Zebra over a network to cause a ZSB Printer to print.").exists():
                self.poco(name="Accept", type="Button").click()
                break
        self.poco("Button").click()

    def verifyNoPrinterInAccountWeb(self):
        sleep(5)
        self.poco("Learn how to add a printer to get started. We’ll help you set things up.").exists()

    def verifyMyDesignsEmptyWeb(self):
        sleep(3)
        try:
            self.poco("You don’t have any designs").wait_for_appearance(timeout=20)
        except:
            raise Exception("My Designs is not empty.")

    def checkIfThereIs1PrinterWithOfflineStatus(self):
        sleep(3)
        if self.poco(nameMatches="(?s).*prints left.*").exists():
            if not self.poco(nameMatches="(?s).*Offline.*").exists():
                raise Exception("The printer is not offline")
        else:
            raise Exception("There is no printer in the account.")

    def VerifyIfNoRecentlyPrintedDesignsPresent(self):
        sleep(3)
        if not self.poco("To Print a Label").exists():
            raise Exception("There are recently printed designs present.")

    def click_Add_A_Printer(self):
        sleep(3)
        self.poco("Add A Printer").click()

    def click_Start_Button(self):
        if self.poco(nameMatches="(?s).*While Using App.*").exists():
            self.poco(nameMatches="(?s).*While Using App.*").click()
            sleep(3)
        self.poco("Start Setup").click()
        sleep(3)


    def Click_Next_Button(self):
        sleep(3)
        self.poco("Next").click()

    def checkTargetPrintersAvailable(self):
        try:
            self.poco("Select your printer").wait_for_appearance(timeout=20)
        except:
            raise Exception("target printers not shown in printer list.")

    def Verify_Searching_for_your_printer_Text(self):
        try:
            self.poco("Searching for your printer").wait_for_appearance(timeout=20)
        except:
            raise Exception("Searching for your printer not displayed.")

    def checkIfThereIs1PrinterWithOnlineStatus(self):
        sleep(3)
        if self.poco(nameMatches="(?s).*prints left.*").exists():
            if not self.poco(nameMatches="(?s).*Online.*").exists():
                raise Exception("The printer is not online")
        else:
            raise Exception("There is no printer in the account.")

    def click_User_upload_photo(self):
        sleep(3)
        try:
            self.poco("Upload photo").click()
        except:
            self.poco("Upload Photo").click()

    def click_Mobile_Camera(self):
        sleep(3)
        self.poco("Camera").click()

    def allow_camera_access_pop_up(self):
        sleep(3)
        if self.poco("OK").exists():
            self.poco("OK").click()

    def capture_the_image_button(self):
        sleep(3)
        self.poco("PhotoCapture").click()

    def use_photo(self):
        sleep(3)
        self.poco("Use Photo").click()

    def Verify_Photo_Uploaded_Message(self):
        sleep(3)
        self.poco("Avatar changed successfully").wait_for_appearance(timeout=20)

    def change_first_name(self):
        sleep(3)
        self.poco("TextField").click()
        sleep(3)
        text("Changed")
        sleep(4)

    def change_last_name(self):
        sleep(3)
        self.poco("TextField")[-1].click()
        sleep(3)
        text("Name")
        sleep(4)

    def change_unit_of_measurement(self):
        sleep(3)
        start_point = (0.57, 0.47)
        vector = (0.297, 0.211)
        swipe(start_point, vector)
        sleep(2)
        self.poco(nameMatches="(?s).*Units of Measurement.*").click()
        sleep(2)
        self.poco("Millimetres").click()

    def click_Three_Dot_On_Workspace(self):
        sleep(2)
        self.poco("Button")[1].click()

    def click_Edit_Txt(self):
        sleep(3)
        self.poco("Edit").click()

    def click_Printer_Settings(self):
        sleep(3)
        self.poco("Printer Settings").click()

    def Change_Darkness_Level_Bar(self):
        seekbar = self.poco("Graphic Options").parent().child("Other")
        newvalue = 50
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage
        seekbar.click([click_x, seekbar_size[1] / 2])

    def Verify_Darkness_Updated_Message(self):
        sleep(3)
        self.poco("Graphic Options updated successfully").wait_for_appearance(timeout=20)

    def change_workspace_name(self):
        sleep(3)
        self.poco("TextField").click()
        sleep(2)
        text("New workspace name.")

    def click_Save_Exit_Btn(self):
        sleep(3)
        self.poco("Save & Exit").click()

    def click_Change_Theme(self):
        sleep(3)
        self.poco("Change Theme").click()

    def check_Change_Electic_Theme(self):
        sleep(3)
        self.poco("Eclectic").parent().child("Button").click()

    def verifyDefaultWorkspaceSettings(self):
        try:
            assert_exists(
                Template(Basic_path(r"default_workspace.png"), record_pos=(-0.356, -0.585), resolution=(1170, 2532)),
                "Please fill in the test point.")
        except:
            raise Exception("Workspace photo is not default")
        workspace_name = self.poco("TextField").attr("value")
        if workspace_name == "My First Workspace":
            pass
        else:
            raise Exception("Default workspace name is not \"My First Workspace\".")

    def verifyDefaultTheme(self):
        modern_theme = self.poco("Modern").parent().child("Button")
        check_value = modern_theme.attr("value")
        if check_value == "1":
            pass
        else:
            raise Exception("Theme is not in default setting.")

    def verifyIfSeekBarIsDefault(self):
        seek_bar = self.poco("Graphic Options").parent().child("Other")
        seek_bar_value = seek_bar.attr("value")
        if seek_bar_value == "100%":
            pass
        else:
            raise Exception("Seekbar is not in default setting.")

    def selectProfileImage(self, image_name="DP.PNG"):
        sleep(3)
        self.poco("Search").wait_for_appearance(timeout=15)
        sleep(2)
        self.poco(image_name).parent().parent().child().child("Image").click()
        sleep(3)

    def verifyDefaultSettings(self, avatar="DZ", first_name="Delete", last_name="Zsb", email="zebra05.swdvt@gmail.com", unit_of_measurement="Inches"):
        sleep(3)
        if not self.poco(nameMatches=f"(?s).*{avatar}.*").exists():
            raise Exception("Avatar is not back to default after changing avatar and then deleting account.")
        if not self.poco("TextField").attr("value") == first_name:
            raise Exception("First name not back to default after modifying it and then deleting the account.")
        if not self.poco("TextField")[-1].attr("value") == last_name:
            raise Exception("Last name not back to default after modifying it and then deleting the account.")
        if not self.poco("TextField").parent().child("Other").attr("value") == email:
            raise Exception("Email is not the expected one.")
        sleep(3)
        start_point = (0.57, 0.47)
        vector = (0.297, 0.211)
        swipe(start_point, vector)
        sleep(2)
        if not self.poco(nameMatches=f"(?s).*{unit_of_measurement}.*").exists():
            raise Exception("Inches is not default unit of measurement.")




