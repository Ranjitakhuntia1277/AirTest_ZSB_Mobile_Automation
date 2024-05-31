from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen

import pytest


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
delete_account_page = Delete_Account_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
device_network_page = Device_Networks_Android(poco)


def test_Delete_Account_TestcaseID_45760():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Close Delete Account pop up dialog"""
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    registration_page.click_log_out_button()
    data_sources_page.checkIfInLoginPage()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45761():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """9. Click X button to close the Delete account dialog - no X button."""
    data_sources_page.clickCancel()
    """Check if user is in settings page after closing Delete Account dialog"""
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    while not poco("Log Out").exists():
        poco.scroll()
    registration_page.click_log_out_button()
    common_method.wait_for_element_appearance("Sign In")
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception(
            "Delete account dialog popped up after canceling delete account and re-loging into the same account.")
    except Exception as e:
        pass


def test_Delete_Account_TestcaseID_45762():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Close Delete Account pop up dialog"""
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    registration_page.click_log_out_button()
    common_method.wait_for_element_appearance("Sign In")
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Home", 20)
    except:
        raise Exception("Did not reach home page after login - login unsuccessful.")


def test_Delete_Account_TestcaseID_45763():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """9. Click X button to close the Delete account dialog - no X button."""
    data_sources_page.clickCancel()
    """Check if user is in settings page after closing Delete Account dialog"""
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    while not poco("Log Out").exists():
        poco.scroll()
    registration_page.click_log_out_button()
    common_method.wait_for_element_appearance("Sign In")
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception(
            "Delete account dialog popped up after canceling delete account and re-loging into the same account.")
    except Exception as e:
        pass


def test_Delete_Account_TestcaseID_45764():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_App()


# def test_Delete_Account_TestcaseID_45766():
#     """Add a printer to this account before executing
#     username - deletezsb@gmail.com
#     password - deletezsb@1234"""
#     common_method.tearDown()
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     registration_page.clickSignIn()
#     registration_page.click_Google_Icon()
#     help_page.chooseAcc("deletezsb@gmail.com")
#     data_sources_page.checkIfOnHomePage()
#     """Verify that there is 1 offline printer in the account"""
#     delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     while not poco("Log Out").exists():
#         poco.scroll()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """Check Delete Account page show up"""
#     try:
#         common_method.wait_for_element_appearance(
#             "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#             20)
#     except:
#         raise Exception("Delete account page did not show up.")
#     """Check continue disabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#         x = 1 / 0
#     except ZeroDivisionError:
#         raise Exception("Continue enabled without checking the three check boxes")
#     except Exception as e:
#         pass
#     """check there are 3 items need acknowledge """
#     try:
#         common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "All data in your workspace will be removed.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Your account will be de-identified, meaning it will not be associated with you.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Ensure your printer is ON to factory reset your ZSB printer.")
#     except:
#         raise Exception("Three checkboxes not present to acknowledge.")
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#     except:
#         raise Exception("Continue disabled even after checking the three check boxes")
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:"""
#     delete_account_page.verifyImportantMessageOnSignInPage()
#     registration_page.clickSignIn()
#     registration_page.click_Google_Icon()
#     help_page.chooseAcc("deletezsb@gmail.com")
#     data_sources_page.checkIfOnHomePage()
#     """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     try:
#         common_method.wait_for_element_appearance(
#             "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
#             20)
#     except:
#         raise Exception(
#             "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
#     """CLick delete in final confirmation pop up"""
#     delete_account_page.clickDelete()
#     """Verify Account Deleted dialog pop up"""
#     delete_account_page.checkAccountDeletedDialog()
#     """CLick Ok"""
#     delete_account_page.clickOk()
#     """Check if logged out automatically after clicking Ok"""
#     data_sources_page.checkIfInLoginPage()
#     """Login Again"""
#     registration_page.clickSignIn()
#     registration_page.click_Google_Icon()
#     help_page.chooseAcc("deletezsb@gmail.com")
#     data_sources_page.checkIfOnHomePage()
#     registration_page.verify_if_on_EULA_page()
#     """Accept EULA for future execution"""
#     registration_page.click_accept()
#     registration_page.clickClose()
#     registration_page.clickExit()
#     data_sources_page.checkIfOnHomePage()
#     delete_account_page.verifyNoPrinterInAccount()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"check the target printers in available printer list"""
#     delete_account_page.checkTargetPrintersAvailable()
#     common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45767():
    """Add a printer to this facebook account before executing and log out of facebook
    # username - deletezsbfacebook@gmail.com
    # password - Zebra#123456789"""
    common_method.tearDown()
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("Zebra#123456789", "deletezsbfacebook@gmail.com")
    data_sources_page.checkIfOnHomePage()
    """Verify that there is 1 online printer in the account"""
    delete_account_page.checkIfThereIs1PrinterWithOnlineStatus()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:"""
    delete_account_page.verifyImportantMessageOnSignInPage()
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    delete_account_page.clickContinueAsInFacebookLogin()
    data_sources_page.checkIfOnHomePage()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    delete_account_page.clickContinueAsInFacebookLogin()
    data_sources_page.checkIfOnHomePage()
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccount()
    """13. click add printer, check the target printers in available printer list-pending"""
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45769():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccount()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    delete_account_page.verifyMyDataEmpty()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    delete_account_page.verifyMyDesignsEmpty()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45780():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    data_sources_page.lock_phone()
    sleep(3600)
    wake()
    delete_account_page.verifyImportantMessageOnSignInPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Home", 20)
    except:
        raise Exception("Did not reach home page after login")
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45781():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    sleep(3600)
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zsbswdvt@gmail.com", "zsbswdvt@1234", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Click Log Out"""
    registration_page.click_log_out_button()
    delete_account_page.verifyImportantMessageOnSignInPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Home", 20)
    except:
        raise Exception("Did not reach home page after login")
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45782():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    """Force quit the app"""
    common_method.Stop_The_App()
    """Wait for 1 hour"""
    sleep(3600)
    """Open the app"""
    common_method.Start_The_App()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    try:
        common_method.wait_for_element_appearance(
            "Home", 20)
    except:
        raise Exception("Did not reach home page after login")
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()


def test_Delete_Account_TestcaseID_45783():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    common_method.tearDown()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    common_method.Stop_The_App()
    """Wait for 1 hour"""
    common_method.Start_The_App()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    common_method.Start_The_App()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    common_method.wait_for_element_appearance("Home", 20)
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    common_method.Stop_The_App()
    common_method.Start_The_App()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    common_method.Start_The_App()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()


def test_Delete_Account_TestcaseID_45786():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    """Scroll till log out button"""
    registration_page.scrollTillLogOutAppears()
    """Disconnect mobile device network"""
    template_management_page.turn_off_wifi()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    delete_account_page.verifyServiceUnavailableErrorPopUp()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45787():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Sign in with email and password"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    if poco("com.android.chrome:id/coordinator").exists():
        poco("com.android.chrome:id/coordinator").click()
    keyevent("back")
    poco.scroll()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")
    """Enter the User Email"""
    registration_page.enter_user_email_for_registering("zsbswdvt@gmail.com")
    registration_page.click_on_next()
    """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
    """Verify Account already exists page title"""
    registration_page.check_email_already_exists_page_title()
    """Verify Account already exists page message"""
    registration_page.check_email_already_Exists_page_message()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45788():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Sign in with email and password"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    if poco("com.android.chrome:id/coordinator").exists():
        poco("com.android.chrome:id/coordinator").click()
    keyevent("back")
    poco.scroll()
    registration_page.click_on_reset_password()
    registration_page.check_if_in_password_recovery_page()
    registration_page.Enter_Username_password_recovery_page("deletezsb@gmail.com")
    registration_page.click_SUBMIT()
    registration_page.wait_for_element_appearance_text("Success!", 10)
    registration_page.check_message_on_success_page()
    registration_page.checkClickHerePresent()
    registration_page.click_on_Click_here()
    registration_page.check_if_on_Reset_Password_page()
    """Enter otp manually"""
    sleep(30)
    registration_page.fillNewPassword("Zebra#123456789")
    registration_page.fillConfirmPassword("Zebra#123456789")
    registration_page.click_SUBMIT()
    registration_page.check_successful_password_reset_page_message()
    registration_page.click_on_Click_here()
    try:
        registration_page.wait_for_element_appearance_text("Sign In With", 10)
    except:
        raise Exception("Did not reach Sign in page")
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()

def test_Delete_Account_TestcaseID_45770():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    poco("com.android.chrome:id/new_tab_view_button").click()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    sleep(2)
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    delete_account_page.verifyIfOnEULAPageWeb()
    delete_account_page.AcceptEULAWeb()
    data_sources_page.clickGotItWeb()
    registration_page.wait_for_element_appearance_text("Home", 10)
    delete_account_page.verifyNoPrinterInAccountWeb()
    poco.scroll()
    data_sources_page.lock_phone()
    wake()
    delete_account_page.VerifyIfNoRecentlyPrintedDesignsPresent()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    data_sources_page.click_My_Data()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    delete_account_page.verifyMyDataEmpty()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    data_sources_page.clickMyDesigns()
    data_sources_page.click_Menu_HamburgerICNWeb()
    delete_account_page.verifyMyDesignsEmptyWeb()
    common_method.Stop_The_App()



def test_Delete_Account_TestcaseID_53205():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    """Check the EULA would be display with the new fonts and styles. pending"""
    registration_page.click_accept()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45774():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """Force quit the app"""
    common_method.Stop_The_App()
    """Wait for 1 hour"""
    sleep(3600)
    """Open the app"""
    common_method.Start_The_App()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45775():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance(
            "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
            20)
    except:
        raise Exception(
            "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """Switch to different app"""
    delete_account_page.switch_to_different_app()
    sleep(60)
    """Switch back to the app"""
    delete_account_page.switch_to_different_app()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()


def test_Delete_Account_TestcaseID_45776():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    data_sources_page.lock_phone()
    "wait for 50 min"
    sleep(3000)
    wake()
    delete_account_page.verifyImportantMessageOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()


def test_Delete_Account_TestcaseID_45777():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    "wait for 50 min"
    sleep(3000)
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zsbswdvt@gmail.com", "zsbswdvt@1234", 1, 0)
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    registration_page.click_log_out_button()
    delete_account_page.verifyImportantMessageOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45778():
    pass
    common_method.tearDown()
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.verifyImportantMessageOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.verifyDeleteAccountDialogPopUp()
    data_sources_page.lock_phone()
    "wait for 65 min"
    sleep(3900)
    wake()
    delete_account_page.verifyDeleteAccountDialogPopUp()
    """Click delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    "check"
    delete_account_page.checkDeleteErrorDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if on settings after clicking Ok"""
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45784():
    pass
    common_method.tearDown()
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Verify that there is 1 offline printer in the account"""
    delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    try:
        common_method.wait_for_element_appearance(
            "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
            20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                  "Ensure your printer is ON to factory reset your ZSB printer.")
    except:
        raise Exception("Three checkboxes not present to acknowledge.")
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
    except:
        raise Exception("Continue disabled even after checking the three check boxes")
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:"""
    delete_account_page.verifyImportantMessageOnSignInPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance(
            "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
            20)
    except:
        raise Exception(
            "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    poco("com.android.chrome:id/new_tab_view_button").click()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    sleep(2)
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    delete_account_page.verifyIfOnEULAPageWeb()
    delete_account_page.AcceptEULAWeb()
    data_sources_page.clickGotItWeb()
    registration_page.wait_for_element_appearance_text("Home", 10)
    delete_account_page.verifyNoPrinterInAccountWeb()
    stop_app("com.android.chrome")
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("deletezsb@gmail.com", "Zebra#123456789", 1, 0)
    data_sources_page.checkIfOnHomePage()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"check the target printers in available printer list"""
    delete_account_page.checkTargetPrintersAvailable()
    common_method.Stop_The_App()
