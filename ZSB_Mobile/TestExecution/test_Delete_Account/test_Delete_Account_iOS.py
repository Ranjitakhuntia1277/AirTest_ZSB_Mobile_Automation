from airtest.core.api import *
from poco.drivers.ios import iosPoco
from self import self

from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ...PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from ...PageObject.Data_Source_Screen.Data_Sources_Screen_iOS import Data_Sources_Screen
from ...PageObject.Registration_Screen.Registration_Screen_iOS import Registration_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen_iOS import Printer_Management_Screen
from ...PageObject.Delete_Account.Delete_Account_Screen_iOS import Delete_Account_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK_iOS import Template_Management_Screen
from ...PageObject.Help_Screen.Help_Screen_iOS import Help_Screen
from poco import poco
import pytest
from airtest.core.api import connect_device


class iOS_Delete_Account:
    pass


# uuid= "00008103-000C718814E3401E"
uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)
auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])

login_page = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
delete_account_page = Delete_Account_Screen(poco)
template_management_page = Template_Management_Screen(poco)
help_page = Help_Screen(poco)


def test_Delete_Account_TestcaseID_45760():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    data_sources_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge"""
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Close Delete Account pop up dialog"""
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    delete_account_page.check_if_back_to_settings_page()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    delete_account_page.check_if_back_to_settings_page()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    data_sources_page.checkIfInLoginPage()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45761():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    data_sources_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """9. Click X button to close the Delete account dialog - no X button."""
    data_sources_page.clickCancel()
    """Check if user is in settings page after closing Delete Account dialog"""
    delete_account_page.check_if_back_to_settings_page()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.check_if_delete_account_pop_up_displayed_even_after_clicking_cancel()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45762():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Close Delete Account pop up dialog"""
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    delete_account_page.check_if_back_to_settings_page()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    delete_account_page.clickCloseButtonInDeleteAccountPage()
    delete_account_page.check_if_back_to_settings_page()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45763():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """9. Click X button to close the Delete account dialog - no X button."""
    data_sources_page.clickCancel()
    """Check if user is in settings page after closing Delete Account dialog"""
    delete_account_page.check_if_back_to_settings_page()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    data_sources_page.checkIfInLoginPage()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    delete_account_page.check_if_delete_account_pop_up_displayed_even_after_clicking_cancel()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45764():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45769():
    """Check delete Zebra account success and re login in Mobile app Need accept EULA and all data cleared(My Designs/My Data)"""
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Login Again"""
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
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
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45780():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    delete_account_page.lock_device()
    sleep(30)
    # sleep(3600)
    delete_account_page.unlock_device()
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.click_Cancel_Btn()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45781():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    # sleep(3600)
    sleep(30)
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.click_Cancel_Btn()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Click Log Out"""
    registration_page.click_log_out_button()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45782():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Force quit the app"""
    common_method.Stop_The_iOSApp()
    """Wait for 1 hour"""
    # sleep(3600)
    sleep(30)
    """Open the app"""
    common_method.Start_The_iOSApp()
    """Login Again"""
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.click_Cancel_Btn()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Click Log Out"""
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    delete_account_page.verifyNoImportantMessageOnSignInPage()


def test_Delete_Account_TestcaseID_45783():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    common_method.Stop_The_iOSApp()
    """Wait for 1 hour"""
    sleep(30)
    # sleep(3600)
    common_method.Start_The_iOSApp()
    """Login Again"""
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """---------------------------"""
    """Remove the code below when time is modified to 3600s"""
    delete_account_page.click_Cancel_Btn()
    """---------------------------"""
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user
    delete"""
    delete_account_page.check_final_delete_account_pop_up()
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
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    """Scroll till log out button"""
    registration_page.scroll_till_log_out()
    """Disconnect mobile device network"""
    delete_account_page.disable_Wi_Fi()
    """Click Delete Account"""
    delete_account_page.open_zsb_app()
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    delete_account_page.verifyServiceUnavailableErrorPopUp()
    delete_account_page.enable_Wi_Fi()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45770():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    # delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()
    data_sources_page.open_chrome()
    delete_account_page.open_zsb_portal_web()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.verifyIfOnEULAPageWeb()
    delete_account_page.accept_EULA_web()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccountWeb()
    delete_account_page.VerifyIfNoRecentlyPrintedDesignsPresent()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.click_My_Data()
    data_sources_page.click_Menu_HamburgerICNWeb()
    delete_account_page.verifyMyDataEmpty()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.clickMyDesigns()
    data_sources_page.click_Menu_HamburgerICNWeb()
    delete_account_page.verifyMyDesignsEmptyWeb()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45775():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """Switch to different app"""
    delete_account_page.switch_to_different_app()
    # sleep(3600)
    sleep(10)
    """Switch back to the app"""
    delete_account_page.open_zsb_app()
    sleep(5)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
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
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    sleep(10)
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    delete_account_page.lock_device()
    "wait for 50 min"
    # sleep(3000)
    sleep(20)
    delete_account_page.unlock_device()
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45774():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    sleep(10)
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """Force quit the app"""
    common_method.Stop_The_iOSApp()
    """Wait for 1 hour"""
    # sleep(3600)
    sleep(20)
    """Open the app"""
    common_method.Start_The_iOSApp()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45777():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    sleep(10)
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    "wait for 50 min"
    sleep(3000)
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45778():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    sleep(10)
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    delete_account_page.lock_device()
    "wait for 65 min"
    sleep(3900)
    # sleep(30)
    delete_account_page.unlock_device()
    delete_account_page.check_final_delete_account_pop_up()
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
    common_method.Stop_The_iOSApp()


"""Add printer to account"""


def test_Delete_Account_TestcaseID_45784():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra051.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Verify that there is 1 offline printer in the account"""
    delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:"""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    common_method.Stop_The_iOSApp()
    data_sources_page.open_chrome()
    delete_account_page.open_zsb_portal_web()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    delete_account_page.verifyIfOnEULAPageWeb()
    delete_account_page.accept_EULA_web()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccountWeb()
    data_sources_page.close_chrome()
    delete_account_page.open_zsb_app()
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra051.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """"click on Add printer tab"""""
    delete_account_page.click_Add_A_Printer()
    """"click on the start button"""
    delete_account_page.click_Start_Button()
    delete_account_page.Click_Next_Button()
    """Pending step 13"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"Verify searching for your printer text"""
    delete_account_page.Verify_Searching_for_your_printer_Text()
    """"check the target printers in available printer list"""
    delete_account_page.checkTargetPrintersAvailable()
    common_method.Stop_The_iOSApp()


# #####""""""""""""""""""""""""""""""Fixed""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Existing bug:-
def test_Delete_Account_TestcaseID_45787():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
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
    registration_page.registerEmail()
    registration_page.check_if_on_ZSB_printer_account_registration_page()
    """Enter the User Email"""
    registration_page.enter_user_email_for_registering()
    """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
    """Verify Account already exists page title"""
    registration_page.check_email_already_exists_page_title()
    """Verify Account already exists page message"""
    registration_page.check_email_already_Exists_page_message()
    common_method.Stop_The_iOSApp()


######### Existing bug:-
def test_Delete_Account_TestcaseID_53205():
    pass
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
    """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    """Check the EULA would be display with the new fonts and styles. pending"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    common_method.Stop_The_iOSApp()


# ######"""""""""""""""""""""""""""""""""FIXED""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""Need to do facebook login"""
def test_Delete_Account_TestcaseID_45767():
    """Add a printer to this facebook account before executing and log out of facebook
#     # username - zebra09.swdvt@gmail.com
#     # password - Zebra#123456789"""
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("Zebra#123456789", "zebra09.swdvt@gmail.com")
    data_sources_page.checkIfOnHomePage()
    """Verify that there is 1 online printer in the account"""
    delete_account_page.checkIfThereIs1PrinterWithOnlineStatus()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:"""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    delete_account_page.clickContinueAsInFacebookLogin()
    data_sources_page.checkIfOnHomePage()
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
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


def test_Delete_Account_TestcaseID_45768():
    pass
    """clear app data"""
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")
    """Check if reached home page after login"""
    data_sources_page.checkIfOnHomePage()
    """Verify that there are no printers in the account"""
    delete_account_page.verifyNoPrinterInAccount()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    """Check If Delete Account is beside Logout button"""
    delete_account_page.checkIfDeleteAccountIsNextToLogOut()
    """Click Delete Account"""
    delete_account_page.clickDeleteAccount()
    """Check Delete Account page show up"""
    delete_account_page.check_if_on_delete_account_page()
    """Check continue disabled"""
    delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
    """check there are 3 items need acknowledge """
    delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
    """Click the three checkBoxes"""
    delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
    """Check continue enabled"""
    delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
    """Click continue"""
    data_sources_page.clickContinue()
    """check mobile app will auto logout and show login screen with notice information:
    Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
    delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")
    """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
    delete_account_page.check_final_delete_account_pop_up()
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
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccount()
    common_method.Stop_The_iOSApp()