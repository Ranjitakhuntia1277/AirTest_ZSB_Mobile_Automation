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
delete_account_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
delete_account_page = Delete_Account_Screen(poco)
template_management_page = Template_Management_Screen(poco)
help_page = Help_Screen(poco)


# def test_Delete_Account_TestcaseID_45765():
#     """Add 2 printer to this account before executing
#     username - zebra05.swdvt@gmail.com
#     password - Zebra#123456789"""
#     pass
#     common_method.show_message(
#         "Add 2 printer to this account before executing\nusername - zebra05.swdvt@gmail.com\npassword - Zebra#123456789, make sure one is oline and other is offline")
#     """clear app data"""
#     common_method.tearDown_iOS()
#     """clear app data"""
#     data_sources_page.log_out_for_current_execution_ios()
#     """Sign in"""
#     data_sources_page.checkIfInLoginPage()
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
#     data_sources_page.checkIfOnHomePage()
#     "In home page 2 printer show in printer list , one is online and one is offline, click pen icon go to user setting page-pending"
#     """Verify that there is 1 offline printer in the account"""
#     delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
#     delete_account_page.checkIfThereIs1PrinterWithOnlineStatus()
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     registration_page.scroll_till_log_out()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """Check Delete Account page show up"""
#     delete_account_page.check_if_on_delete_account_page()
#     """Check continue disabled"""
#     delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
#     """check there are 3 items need acknowledge """
#     delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:"""
#     delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     delete_account_page.check_final_delete_account_pop_up()
#     """CLick delete in final confirmation pop up"""
#     delete_account_page.clickDelete()
#     """Verify Account Deleted dialog pop up"""
#     delete_account_page.checkAccountDeletedDialog()
#     """CLick Ok"""
#     delete_account_page.clickOk()
#     """Check if logged out automatically after clicking Ok"""
#     data_sources_page.checkIfInLoginPage()
#     common_method.show_message("Turn on the printer that is offline")
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     data_sources_page.checkIfOnHomePage()
#     registration_page.verify_if_on_EULA_page()
#     """Accept EULA for future execution"""
#     registration_page.click_accept()
#     registration_page.clickClose()
#     registration_page.clickExit()
#     data_sources_page.checkIfOnHomePage()
#     delete_account_page.verifyNoPrinterInAccount()
#     """"click on Add printer tab"""""
#     delete_account_page.click_Add_A_Printer()
#     """"click on the start button"""
#     delete_account_page.click_Start_Button()
#     delete_account_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     delete_account_page.Verify_Searching_for_your_printer_Text()
#     """"check the target printers in available printer list"""
#     common_method.show_message(
#         "check the 2 printers are available printer list, select one printer, check printer can be added again")
#     common_method.Stop_The_iOSApp()
#
#
# def test_Delete_Account_TestcaseID_45771():
#     pass
#     """clear app data"""
#     common_method.tearDown_iOS()
#     """clear app data"""
#     data_sources_page.log_out_for_current_execution_ios()
#     """Sign in"""
#     data_sources_page.checkIfInLoginPage()
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
#     data_sources_page.checkIfOnHomePage()
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     registration_page.scroll_till_log_out()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     """Check Delete Account page show up"""
#     delete_account_page.check_if_on_delete_account_page()
#     """Check continue disabled"""
#     delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
#     """check there are 3 items need acknowledge """
#     delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:
#     Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     delete_account_page.check_notice_information_on_login_page_after_choosing_delete_account()
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
#     """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     delete_account_page.check_final_delete_account_pop_up()
#     """Click delete in final confirmation pop up"""
#     delete_account_page.clickDelete()
#     """Verify Account Deleted dialog pop up"""
#     delete_account_page.checkAccountDeletedDialog()
#     """CLick Ok"""
#     delete_account_page.clickOk()
#     """Check if logged out automatically after clicking Ok"""
#     data_sources_page.checkIfInLoginPage()
#     """Cannot automate
#     11. Open Printer Tools click sign button check Login page show up, input the deleted user name and password click Sign in, check user can login printer tools successfully and no printer show in printer list.
#     has to be executed manually"""
#     common_method.show_message(
#         "11. Open Printer Tools click sign button check Login page show up, input the deleted user name and password click Sign in, check user can login printer tools successfully and no printer show in printer list.\nAccount info - username - zebra05.swdvt@gmail.com password- Zebra#123456789")
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     registration_page.verify_if_on_EULA_page()
#     """Accept EULA for future execution"""
#     """Check the EULA would be display with the new fonts and styles. pending"""
#     registration_page.click_accept()
#     registration_page.clickClose()
#     registration_page.clickExit()
#     common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45785():
    pass
    # """clear app data"""
    # common_method.tearDown_iOS()
    # """clear app data"""
    # data_sources_page.log_out_for_current_execution_ios()
    # """Sign in"""
    # data_sources_page.checkIfInLoginPage()
    # registration_page.clickSignIn()
    # data_sources_page.signInWithEmail()
    # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    # data_sources_page.checkIfOnHomePage()
    # """Click Hamburger Icon"""
    # login_page.click_Menu_HamburgerICN()
    # """Click on edit profile"""
    # registration_page.click_on_profile_edit()
    """""click on upload photo"""
    delete_account_page.click_User_upload_photo()
    """click on camera option"""
    delete_account_page.click_Mobile_Camera()
    """""click allow if it is present"""
    delete_account_page.allow_camera_access_pop_up()
    """"click on click picture icon"""
    delete_account_page.capture_the_image_button()
    delete_account_page.use_photo()
    """"Verify photo uploaded message"""""
    delete_account_page.Verify_Photo_Uploaded_Message()
    """Change first name"""
    delete_account_page.change_first_name()
    """Change last name"""
    delete_account_page.change_last_name()
    """Change unit of measurement"""
    delete_account_page.change_unit_of_measurement()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    delete_account_page.click_Three_Dot_On_Workspace()
    delete_account_page.click_Edit_Txt()
    delete_account_page.click_User_upload_photo()
    sleep(2)
    """""click on the 1st image"""
    delete_account_page.selectProfileImage()
    """Change workspace name"""
    delete_account_page.change_workspace_name()
    """click on the save & exit"""
    delete_account_page.click_Save_Exit_Btn()
    sleep(2)
    delete_account_page.click_Three_Dot_On_Workspace()
    """Click change theme"""
    delete_account_page.click_Change_Theme()
    """Change default theme to any other theme"""
    delete_account_page.check_Change_Electic_Theme()
    """click on the save & exit"""
    delete_account_page.click_Save_Exit_Btn()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    delete_account_page.click_Printer_Settings()
    """"change the darkness level"""
    delete_account_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    delete_account_page.Verify_Darkness_Updated_Message()
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
    """CLick delete in final confirmation pop up"""
    delete_account_page.clickDelete()
    """Verify Account Deleted dialog pop up"""
    delete_account_page.checkAccountDeletedDialog()
    """CLick Ok"""
    delete_account_page.clickOk()
    """Check if logged out automatically after clicking Ok"""
    data_sources_page.checkIfInLoginPage()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789")
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    """Check the EULA would be display with the new fonts and styles. pending"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    delete_account_page.verifyDefaultSettings()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    delete_account_page.click_Three_Dot_On_Workspace()
    delete_account_page.click_Edit_Txt()
    """Verify if workspace settings are back to default"""
    delete_account_page.verifyDefaultWorkspaceSettings()
    data_sources_page.clickBackArrow()
    delete_account_page.click_Three_Dot_On_Workspace()
    """Click change theme"""
    delete_account_page.click_Change_Theme()
    """Verify if theme is back to default"""
    delete_account_page.verifyDefaultTheme()
    data_sources_page.clickBackArrow()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    delete_account_page.click_Printer_Settings()
    delete_account_page.verifyIfSeekBarIsDefault()
    """Step 20 pending due to web inconsistency"""
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45766():
    pass
    """Add a printer to this account before executing
    username - zebra05.swdvt@gmail.com
    password - Zebra#123456789"""
    common_method.show_message(
        "Add printer to account - zebra05.swdvt@gmail.com-Zebra#123456789 with google login and get the printer to offline state")
    """clear app data"""
    common_method.tearDown_iOS()
    """clear app data"""
    data_sources_page.log_out_for_current_execution_ios()
    """Sign in"""
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    help_page.chooseAcc("zebra05.swdvt@gmail.com")
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
    registration_page.click_Google_Icon()
    help_page.chooseAcc("zebra05.swdvt@gmail.com")
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
    registration_page.click_Google_Icon()
    help_page.chooseAcc("zebra05.swdvt@gmail.com")
    data_sources_page.checkIfOnHomePage()
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    delete_account_page.verifyNoPrinterInAccount()
    """"click on Add printer tab"""""
    delete_account_page.click_Add_A_Printer()
    """"click on the start button"""
    delete_account_page.click_Start_Button()
    delete_account_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    delete_account_page.Verify_Searching_for_your_printer_Text()
    """"check the target printers in available printer list"""
    delete_account_page.checkTargetPrintersAvailable()
    common_method.Stop_The_iOSApp()


def test_Delete_Account_TestcaseID_45788():
    pass
    """clear app data"""
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
    """Sign in with email and password"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.click_on_reset_password()
    registration_page.check_if_in_password_recovery_page()
    registration_page.Enter_Username_password_recovery_page("zebra05.swdvt@gmail.com")
    registration_page.wait_for_element_appearance("Success!", 15)
    registration_page.check_message_on_success_page()
    registration_page.checkClickHerePresent()
    registration_page.click_on_Click_here()
    registration_page.check_if_on_Reset_Password_page()
    """Enter otp manually"""
    common_method.show_message(
        "Enter the otp received on gmail account - zebra05.swdvt@gmail.com - Zebra#123456789 in the 'Temporary Password' field. Click Ok in the dialog after its done.")
    registration_page.fillNewPassword("Zebra#1234567819")
    registration_page.fillConfirmPassword("Zebra#1234567819")
    registration_page.click_SUBMIT()
    registration_page.check_successful_password_reset_page_message()
    registration_page.click_on_Click_here()
    data_sources_page.checkIfInLoginPage()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    registration_page.verify_if_on_EULA_page()
    """Accept EULA for future execution"""
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    common_method.Stop_The_iOSApp()
    common_method.show_message("Change password of zebra05.swdvt@gmail.com in zebra login back to Zebra#123456789")


