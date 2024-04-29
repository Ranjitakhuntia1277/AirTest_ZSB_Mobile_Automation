from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen

class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# wake()
# start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
delete_account_page = Delete_Account_Screen(poco)


def test_Delete_Account_TestcaseID_45760():
    """Login Pending"""
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
        common_method.wait_for_element_appearance("For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.", 20)
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
        common_method.wait_for_element_appearance("For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.", 20)
    except:
        raise Exception("Delete account page did not show up.")
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    try:
        common_method.wait_for_element_appearance("Settings")
    except:
        raise Exception("Did not return to settings page.")
    registration_page.click_log_out_button()
    common_method.Stop_The_App()


def test_Delete_Account_TestcaseID_45761():
    """Login Pending"""
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
        common_method.wait_for_element_appearance("For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.", 20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x=1/0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "Ensure your printer is ON to factory reset your ZSB printer.")
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
    """check mobile app will auto logout and show login screeen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance("Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.", 20)
    except:
        raise Exception("Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "deletezsb@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance("Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.", 20)
    except:
        raise Exception("User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
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
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "deletezsb@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    try:
        common_method.wait_for_element_appearance("Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.", 20)
        x=1/0
    except ZeroDivisionError:
        raise Exception("Delete account dialog popped up after canceling delete account and re-loging into the same account.")
    except Exception as e:
        pass


def test_Delete_Account_TestcaseID_45762():
    """Login Pending"""
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
        common_method.wait_for_element_appearance("For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.", 20)
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
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "deletezsb@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    try:
        common_method.wait_for_element_appearance(
            "Home",20)
    except:
        raise Exception("Did not reach home page after login - login unsuccessful.")


def test_Delete_Account_TestcaseID_45763():
    """Login Pending"""
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
        common_method.wait_for_element_appearance("For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.", 20)
    except:
        raise Exception("Delete account page did not show up.")
    """Check continue disabled"""
    try:
        template_management_page.wait_for_appearance_enabled("Continue")
        x=1/0
    except ZeroDivisionError:
        raise Exception("Continue enabled without checking the three check boxes")
    except Exception as e:
        pass
    """check there are 3 items need acknowledge """
    try:
        common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "All data in your workspace will be removed.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "Your account will be de-identified, meaning it will not be associated with you.")
        delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox", "Ensure your printer is ON to factory reset your ZSB printer.")
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
    """check mobile app will auto logout and show login screeen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    try:
        common_method.wait_for_element_appearance("Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.", 20)
    except:
        raise Exception("Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "deletezsb@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    try:
        common_method.wait_for_element_appearance("Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.", 20)
    except:
        raise Exception("User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
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
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "deletezsb@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    try:
        common_method.wait_for_element_appearance("Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.", 20)
        x=1/0
    except ZeroDivisionError:
        raise Exception("Delete account dialog popped up after canceling delete account and re-loging into the same account.")
    except Exception as e:
        pass
