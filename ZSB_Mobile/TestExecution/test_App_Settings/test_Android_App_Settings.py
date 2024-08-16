from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
import pytest
from airtest.core.api import connect_device


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)


# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47918():
    """	Verify ZSB app permission works fine."""
    """Freshly Install the latest stage/production app on the phone & printer should be added"""

    #
    common_method.tearDown()
    common_method.Stop_The_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    """ Allow pop up before login for the fresh installation"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    """for the first installation click on the zsb series popup"""
    login_page.click_Allow_ZSB_Series_Popup()
    """Relaunch the app"""
    common_method.relaunch_app()
    """ Allow pop up before login for the fresh installation"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """for the first installation click on the zsb series popup"""
    login_page.click_Allow_ZSB_Series_Popup()
    """Relaunch the app"""
    common_method.relaunch_app()
    """Permission is not displaying due to SMBM-1242"""
    login_page.Verify_LoginAllow_Popup_IS_Displaying()
    common_method.Stop_The_App()
##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ####bug id----SMBM-2120
def test_AppSettings_TestcaseID_49665():
    """Manage network- Check Bluetooth Connection failed dialog will pop up after BT Paring Request dialog disappeared"""


    """"WIFI should not be connected in wifi section under printer name"""

    #
    common_method.tearDown()
    common_method.Clear_App()
    common_method.Start_The_App()
    """ Allow pop up before login for the fresh installation"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    """for the first installation click on the zsb series popup"""
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    """click on hamburger menu"""
    login_page.click_Menu_HamburgerICN()
    """"click printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """click on printer name"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """"click wifi tab"""
    app_settings_page.click_wifi_tab()
    """"click manage network buttons"""
    app_settings_page.click_Manage_Networks_Btn()
    """"verify bluetooth connection required text"""
    app_settings_page.get_text_Bluetooth_connection_required_Txt()
    """""click continue button on bluetooth connection required"""
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    """"verify bluetooth_connection failed popup"""
    app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()
    """""click continue button on connection failed popup"""
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    """"click on manage networks button"""
    app_settings_page.click_Manage_Networks_Btn()
    """stop the app"""
    common_method.Stop_The_App()
### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def test_AppSettings_TestcaseID_45689():
    """""""""Check Change Theme Function Works"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """""""""start the app"""""""""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""""click hamburger menu"""""""
    login_page.click_Menu_HamburgerICN()
    """"click three dot on workspace"""""
    app_settings_page.click_Three_Dot_On_Workspace()
    """""""verify edit text"""""""
    app_settings_page.get_text_Edit_Txt()
    """"click on change theme"""
    app_settings_page.click_Change_Theme()
    """""verify change theme page pop ups by verifying the change theme header"""
    app_settings_page.get_text_Change_Theme_Header()
    sleep(1)
    """""""change 5 theme and check it should get saved and then need to tap on exit"""""""
    app_settings_page.check_Change_Electic_Theme()
    sleep(3)
    """""click save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    """""""SMBM-986 is still present""""
    """"After applying the theme check whether it is navigating back to home page not verifying the background image as there is no element present"""
    sleep(3)
    app_settings_page.Home_text_is_present_on_homepage()
    """""click on hamburger icon on home page"""""
    login_page.click_Menu_HamburgerICN()
    sleep(4)
    """"click on three dot icon on workspace"""""
    app_settings_page.click_Three_Dot_On_Workspace()
    """"click on change theme"""
    app_settings_page.click_Change_Theme()
    """""check Bohemian theme"""
    sleep(3)
    app_settings_page.check_Change_Bohemian_Theme()
    sleep(3)
    """""click save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.Home_text_is_present_on_homepage()
    """""click on hamburger icon on home page"""
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """"click on three dot icon on workspace"""""
    app_settings_page.click_Three_Dot_On_Workspace()
    """"click on change theme"""
    app_settings_page.click_Change_Theme()
    """""check Professional theme"""
    sleep(3)
    app_settings_page.check_Change_Professional_Theme()
    sleep(3)
    """""click save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.Home_text_is_present_on_homepage()
    """""click on hamburger icon on home page"""
    login_page.click_Menu_HamburgerICN()
    sleep(4)
    """"click on three dot icon on workspace"""""
    app_settings_page.click_Three_Dot_On_Workspace()
    """"click on change theme"""
    app_settings_page.click_Change_Theme()
    """""check Maker theme"""
    sleep(3)
    app_settings_page.check_Change_Maker_Theme()
    sleep(3)
    """""click save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.Home_text_is_present_on_homepage()
    """""click on hamburger icon on home page"""
    login_page.click_Menu_HamburgerICN()
    sleep(4)
    """"click on three dot icon on workspace"""""
    app_settings_page.click_Three_Dot_On_Workspace()
    """"click on change theme"""
    app_settings_page.click_Change_Theme()
    """""check Modern theme"""
    sleep(3)
    app_settings_page.check_Change_Modern_Theme()
    sleep(3)
    """""click save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.Home_text_is_present_on_homepage()
    """stop the app"""
    common_method.Stop_The_App()

# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_45690():
    """""""""Update Unit of Measure in Mobile App, check it will sync to Web Portal and Printer Tools"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""


    """""start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""click hamburger menu"""""
    login_page.click_Menu_HamburgerICN()
    """"click on the pen icon near the user name"""
    app_settings_page.click_pen_Icon_near_UserName()
    sleep(1)
    poco.scroll()
    """"""""""verify units of measurement text is present or not"""""""""
    app_settings_page.check_If_Units_of_Measurements_Is_Present()
    """""""verify  Inches is the by default value is displaying"""""""
    app_settings_page.click_Units_of_Measurements()
    sleep(2)
    """"Verify all the available values"""""
    app_settings_page.verify_Milimetres_Is_Present()
    app_settings_page.verify_Centimetres_Is_Present()
    app_settings_page.verify_Inches_Is_Present()
    sleep(2)
    """"click on Centimeters option"""
    app_settings_page.click_Centimeters()
    sleep(1)
    """""""""verify the updated message popup"""""
    app_settings_page.verify_updated_msg()
    """""""Click on the hamburger icon"""""""
    sleep(2)
    login_page.click_Menu_HamburgerICN()
    """""click on the home tab"""
    app_settings_page.click_Home_Tab()
    sleep(2)
    """""""""verify printer details, everything should display in centimeters"""""
    app_settings_page.verify_printer_details_in_Centimeters()
    sleep(2)
    login_page.click_Menu_HamburgerICN()
    """""click on my design tab"""
    app_settings_page.click_My_Design()
    sleep(4)
    """""verify the design size under my design"""
    app_settings_page.verify_My_Details_Design_in_Centimeters()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    sleep(1)
    poco.scroll()
    app_settings_page.click_Units_of_Measurements()
    sleep(2)
    app_settings_page.click_Inches()
    sleep(2)
    """Syncing to web portal is not working properly so need to verify manually"""
    """stop the app"""
    common_method.Stop_The_App()

# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ####bug id----SMBM-2416

def test_AppSettings_TestcaseID_45691():
    """""""""Edit Workspace - upload and remove image"""""


    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """"start the app"""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    sleep(2)
    """""verify the Edit workspace text"""
    app_settings_page.get_text_Edit_Workspace()
    """""""click upload photo"""""""
    app_settings_page.click_upload_photo()
    sleep(2)
    """""click on the 1st image"""
    app_settings_page.click_On_First_Image_SearchBar()
    app_settings_page.click_First_Image()
    app_settings_page.click_JPG_ON_Result()
    app_settings_page.click_First_Image_ON_The_List()
    """click on the save & exit"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(2)
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    sleep(2)
    app_settings_page.click_Remove_Image()
    app_settings_page.Is_Present_Profile_Avatar_Letter()
    sleep(2)
    app_settings_page.click_upload_photo()
    sleep(1)
    app_settings_page.click_Back_Icon()
    app_settings_page.click_Close_Icon()
    sleep(2)
    app_settings_page.click_Save_Exit_Btn()
    sleep(2)
    """stop the app"""
    common_method.Stop_The_App()
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_45692():
    """""""""Edit Workspace - Update workspace name"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""


    """""""""start the app"""""""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    sleep(2)
    """""verify the Edit workspace text"""
    app_settings_page.get_text_Edit_Workspace()
    """"Verify Workspace Name Text"""
    sleep(2)
    app_settings_page.Is_Present_Workspace_Name_Text()
    """""""click on workspace name"""""""""
    app_settings_page.click_Workspace_Name_Text_Field()
    """""clear workspace name text field"""
    app_settings_page.Clear_Workspace_Name()
    sleep(2)
    """"Click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    """""""""""Verify save & exit option is not there"""""""""
    app_settings_page.Verify_SaveExit_Option_Is_Not_There()
    """""click on back icon on edit workspace"""
    app_settings_page.click_back_Icon_On_Edit_Workspace()
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    sleep(2)
    """""Check the previous Workspace name is displaying"""
    app_settings_page.Is_Present_Workspace_Name()
    app_settings_page.click_Workspace_Name_Text_Field()
    app_settings_page.Clear_Workspace_Name()
    sleep(2)
    app_settings_page.click_Workspace_Name_Text_Field()
    """"verify the workspace field by giving space """
    app_settings_page.Update_Workspace_Name_With_Space()
    sleep(3)
    """"Click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    sleep(3)
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    app_settings_page.click_Workspace_Name_Text_Field()
    app_settings_page.Clear_Workspace_Name()
    sleep(2)
    """"Click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    sleep(1)
    app_settings_page.click_Workspace_Name_Text_Field()
    """"verify the workspace field by special characters with more than 30 characters """
    app_settings_page.Update_Workspace_Name_With_Special_Characters_with_30_characters()
    sleep(3)
    """"Click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    sleep(3)
    """""click on save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    app_settings_page.click_Three_Dot_On_Workspace()
    app_settings_page.click_Edit_Txt()
    """"""""""Verify the workspace updated name"""""""""""""""
    app_settings_page.Verify_Updated_Name()
    sleep(3)
    app_settings_page.click_Workspace_Name_Text_Field()
    app_settings_page.Clear_Workspace_Name()
    sleep(2)
    """"Click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    app_settings_page.click_Workspace_Name_Text_Field()
    app_settings_page.Update_Workspace_Name_with_Original_Name()
    sleep(3)
    app_settings_page.click_Keyboard_back_Icon()
    sleep(3)
    """""click on save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    sleep(3)
    """stop the app"""
    common_method.Stop_The_App()
# # # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_45705():
    """""""""Verify account profile update for non-Zebra user"""""


    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """""""start the app"""""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""click hamburger menu"""""
    login_page.click_Menu_HamburgerICN()
    """"click on the pen icon near the user name"""
    app_settings_page.click_pen_Icon_near_UserName()
    """""""verify First name text is present"""""""
    app_settings_page.Is_Present_First_Name_Text()
    """""""verify last name text is present"""""""
    app_settings_page.Is_Present_Last_Name_Text()
    """""click first name text field"""
    app_settings_page.click_First_Name_Text_Field()
    """"clear first name field"""
    sleep(3)
    app_settings_page.clear_First_Name()
    """""Update first name with special characters with 30 characters"""
    app_settings_page.Update_First_Name_With_Special_Characters_with_30_characters()
    sleep(3)
    poco.scroll()
    """""click last name text field"""
    app_settings_page.click_Last_Name_Text_Field()
    """"clear Last name field"""
    app_settings_page.clear_Last_Name()
    """""Update last name with special characters with 30 characters"""
    app_settings_page.Update_Last_Name_With_Special_Characters_with_30_characters()
    sleep(3)
    """""click keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    """"verify the updated names message"""
    app_settings_page.verify_Your_changes_have_been_saved_Message()
    sleep(3)
    """""click last name text field"""
    app_settings_page.click_Last_Name_Text_Field()
    """"clear Last name field"""
    app_settings_page.clear_Last_Name()
    """Update the default Last name"""
    app_settings_page.Update_Default_Last_Name()
    app_settings_page.click_Keyboard_back_Icon()
    sleep(3)
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    """""click First name text field"""
    app_settings_page.click_First_Name_Text_Field()
    """"clear First name field"""
    app_settings_page.clear_First_Name()
    """Update the default First name"""
    app_settings_page.Update_Default_First_Name()
    app_settings_page.click_Keyboard_back_Icon()
    """""""change password link is not opening the correct page---SMBM-1098, due to this bug could not automate"""""
    """""""change email is not yet implemented so could not automate this"""""""""
    """stop the app"""
    common_method.Stop_The_App()

###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47810():
    """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
    """"Install the latest production app on the phone & printer should be added with logged in condition Create the object for Login page & Common_Method page to reuse the methods"""
    """""Check whether App is installed or not"""""


    """""start the app"""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"Click on hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on  home tab"""
    app_settings_page.click_Home_Tab()
    sleep(2)
    """""verify printer is already added or not"""
    app_settings_page.Verify_Printer_is_already_added()
    sleep(1)
    """""""verify recently printed labels is present"""""""
    app_settings_page.Is_Present_Recently_Printed_Labels_Text()
    """""""verify first recent lebel is present"""""""
    app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
    """click on the first recently present label"""
    app_settings_page.click_Firstone_In_Recently_Prtinted_Label()
    """stop the app"""
    common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47820():
    """"Verify ZSB app home page (overview page) should scroll to the bottom of the list in Recently Printed Labels"""""

    """"Precondition:
    1. Install the latest production app on the tablet
    2. Prepare a production with printer added and sign in
    3. There are 6 Recently Printed Lables present in account"""""
    #

    """""""start the app"""""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    """"click on  home tab"""
    app_settings_page.click_Home_Tab()
    sleep(2)
    """""verify printer is already added or not"""
    app_settings_page.Verify_Printer_is_already_added()
    sleep(1)
    """""""verify recently printed labels is present"""""""
    app_settings_page.Is_Present_Recently_Printed_Labels_Text()
    """""""verify first recent lebel is present"""""""
    app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
    poco.scroll()
    """"Verify buy more labels is present"""
    app_settings_page.Is_Present_Buy_More_Labels()
    sleep(3)
    """stop the app"""
    common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47825():
    """""Verify ZSB app doesn't shows error as "Logout failed. Please try logging out again"."""""

    #
    """Precondition:
    1. Registered a production user
    2. Install production Mobile App into test device"""
    #

    """""""start the app"""""""
    common_method.tearDown()
    sleep(3)
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""click on hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """""click on the pen icon near to user name"""
    app_settings_page.click_pen_Icon_near_UserName()
    """Verify User settings text is present"""
    app_settings_page.Is_Present_User_Settings_Text()
    """"Scroll till the delete button"""
    app_settings_page.Scroll_till_Delete_Account()
    """"Verify Logout button"""
    app_settings_page.Is_Present_Logout_Btn()
    """"click on the delete account button"""
    app_settings_page.click_Delete_Account_Btn()
    """"Verify Delete account text is present"""
    app_settings_page.verify_Delete_Account_Text()
    """verify Please Acknowledge text is present"""""
    app_settings_page.verify_Please_Acknowledge_Text()
    """""verify & click on first checkbox """
    app_settings_page.click_First_Checkbox()
    """""verify & click on second checkbox """
    app_settings_page.click_Second_Checkbox()
    """""verify & click on third checkbox """
    app_settings_page.click_Third_Checkbox()
    """verify security message text is present"""""
    app_settings_page.verify_Security_Message_Text()
    """click on cancel button"""
    app_settings_page.click_Cancel_Btn()
    """verify setting text is present"""
    app_settings_page.Is_Present_User_Settings_Text()
    """"verify & click on delete account button"""
    app_settings_page.click_Delete_Account_Btn()
    """""verify & click on first checkbox """
    app_settings_page.click_First_Checkbox()
    """""verify & click on second checkbox """
    app_settings_page.click_Second_Checkbox()
    app_settings_page.click_Third_Checkbox()
    """"click on the confirm button to delete the account"""
    app_settings_page.click_Confirm_Btn_To_DeleteAccount()
    """"verify zebra logo is present"""
    app_settings_page.Is_Present_Zebra_Logo()
    """verify ZSB printer image is displaying"""""
    app_settings_page.Is_Present_ZSB_Printer_Icon()
    """""Verify login page Important messsage text"""
    app_settings_page.Verify_Login_Page_Important_Message_Text()
    """click on login button"""
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    sleep(3)
    """"verify delete account pop up message"""
    app_settings_page.Is_Present_Delete_Account_Popup()
    """"click on cancel button on the pop up"""
    app_settings_page.click_Cancel_on_Delete_Account_Popup()
    """"verify settings text is displaying"""
    app_settings_page.Is_Present_User_Settings_Text()
    """stop the app"""
    common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47879():
    """""Verify typo and guide message is correct on Searching For your printer page."""""


    """Precondition:
    1. Registered a production user
    2. Install production Mobile App into test device"""""


    """""""start the app"""""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"click on hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """""click on Add a printer"""
    add_a_printer_screen.click_Add_A_Printer()
    """""click on start Button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.click_LED_Guide_Button()
    """"verify printer led not flashing text"""
    add_a_printer_screen.Verify_Blue_Left_LED_Text_And_Expand()
    add_a_printer_screen.Verify_Red_Right_LED_Text_And_Expand()
    """click on the printer led guide done button"""
    add_a_printer_screen.click_Printer_LED_Guide_Done_Btn()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """stop the app"""
    common_method.Stop_The_App()

### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47880():
    """""Verify "Done" Button and text "LED light Behavior Support" position is correct in Printer LED Guide dialog."""""
    #

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"click on hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """""click on Add a printer"""
    add_a_printer_screen.click_Add_A_Printer()
    """""click on start Button"""
    add_a_printer_screen.click_Start_Button()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.click_LED_Guide_Button()
    #### """"verify the position of all the buttons"""
    #### add_a_printer_screen.Verify_the_Position_of_all_the_Buttons()
    """click on the printer led guide done button"""
    add_a_printer_screen.click_Printer_LED_Guide_Done_Btn()
    add_a_printer_screen.Click_Next_Button()
    """stop the app"""
    common_method.Stop_The_App()
###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id-SMBM-1684
def test_AppSettings_TestcaseID_47911():
    """ Verify auto Label Feed On Printer Cover Close value doesn't retrieve in progress after changing darkness level."""



    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.Check_toggle_button()
    """click on the toggle button"""
    app_settings_page.click_toggle_button()
    """stop the app"""
    common_method.Stop_The_App()
###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47914():
    """Android Only-Verify there is no unknown printer appeared in the Bluetooth list."""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on add a printer"""
    add_a_printer_screen.click_Add_A_Printer()
    """""click on start Button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.Click_Next_Button()
    """"verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    add_a_printer_screen.Verify_Discovered_Devices_Text()
    add_a_printer_screen.Verify_same_ZSB_image_for_all_items()
    """stop the app"""
    common_method.Stop_The_App()
###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47915():
    """""Printer Bluetooth List displays printers which have already been added even if "Show All Printers" is not selected."""



    """start the app"""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    ### add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """stop the app"""
    common_method.Stop_The_App()

### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ######bug id---SMBM-2644
def test_AppSettings_TestcaseID_47917():
    """Verify Printer’s name is too long which should not causes app get stuck and style error at Printer Settings page."""



    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings tab"""""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.clear_First_Name()
    """Rename the Printer Name with a long text (more than 30 characters)"""
    app_settings_page.Rename_PrinterName_With30_Characters()
    app_settings_page.click_Back_Icon()
    app_settings_page.Verify_Exceeding_Characters_Message()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.clear_First_Name()
    app_settings_page.Update_PrinterName()
    app_settings_page.click_Back_Icon()
    """stop the app"""
    common_method.Stop_The_App()

## #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ###bug id---SMBM-2243
def test_AppSettings_TestcaseID_50333():
    """Android only- Check it will back to manage network after clicking device’s back button"""""

    """"App should be in logged in condition & printer should be added"""""


    """"start the app"""""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on the printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """click on the printer name"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """"click on the wifi tab"""
    app_settings_page.click_wifi_tab()
    """click on the Manage network button"""
    app_settings_page.click_Manage_Networks_Btn()
    """"verify bluetooth connection required text"""
    app_settings_page.get_text_Bluetooth_connection_required_Txt()
    """click on keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    """""Due to bug id SMBM-2243, step 5 is blocked"""
    """Turn off printer Manually"""
    """"verify bluetooth connection failed pop up"""
    app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()
    """""click keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    """"verify wifi tab & text is present"""
    app_settings_page.Verify_Wifi_Tab_Text()
    """stop the app"""
    common_method.Stop_The_App()
#
### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47923():
    """Verify changing password should log out all clients."""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Logout_Btn()
    login_page.click_loginBtn()
    login_page.Verify_ALL_Allow_Popups()
    login_page.signInWithEmail()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Change_Password_Btn()
    app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
    app_settings_page.click_Close_Icon_On_Password_Recovery_Page()
    """After changing the password, it should logged out. this needs to be validated Manually"""""
    """stop the app"""
    common_method.Stop_The_App()

###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47956():
    """Upload avatar via "Photo Gallery" using the default interface of Onedrive"""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on pen icon"""
    app_settings_page.click_pen_Icon_near_UserName()
    """"Verify User settings text in user settings page"""
    app_settings_page.Is_Present_User_Settings_Text()
    """""click on upload photo"""
    app_settings_page.click_User_upload_photo()
    """click on camera option"""
    app_settings_page.click_Mobile_Camera()
    """""click allow if it is present"""
    app_settings_page.Click_Allow_popup()
    """"click on click picture icon"""
    app_settings_page.click_picture()
    """"Verify photo uploaded message"""""
    app_settings_page.Verify_Photo_Uploaded_Message()
    """"click user photo remove image"""
    app_settings_page.click_User_Photo_Remove_Image()
    """stop the app"""
    common_method.Stop_The_App()
# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50325():
    """Manage Network-Check able to add/delete/sort network when printer bt paired/unpaired in device"""


    """"App should be in logged in condition & printer should be added """



    """"start the app"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page.click_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Security_Open()
    app_settings_page.click_WPA_PSK()
    app_settings_page.click_Keyboard_back_Icon()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page.Verify_Added_Network()
    """stop the app"""
    common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def test_AppSettings_TestcaseID_49960():
    """Check click change password in user profile page: it added callback url, responsce_type, client_id and redirect_url parameters"""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.signInWithEmail()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    app_settings_page.click_Keyboard_back_Icon()
    login_page.click_SignIn_Button()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Change_Password_Btn()
    app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
    """stop the app"""
    common_method.Stop_The_App()

###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ####bug id---SMBM-2234
def test_AppSettings_TestcaseID_49961():
    """Check after change password, click return to login will navigate to login page and user able to login with new password success"""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Change_Password_Btn()
    app_settings_page.Verify_Change_Password_PageURL_Is_Displaying()
    app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
    app_settings_page.click_Password_Recovery_Email_TextField()
    app_settings_page.click_Submit_On_Password_Recovery_Screen()
    """"other steps are blocked due to SMBM-2234 & SMBM-1098"""
    """"After changing the password, login screen and login should be verified manually"""
    """stop the app"""
    common_method.Stop_The_App()

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_51702():
    """Check the UI of toggle buttons on Notification Settings""""""
    """"App should be in logged in condition & printer should be added"""
    #
    #
    #
    """"start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Notifications Tab"""
    app_settings_page.click_Notifications_Tab()
    """"Scroll till Notification Settings Tab"""
    app_settings_page.Scroll_Till_Notification_Settings_Tab()
    """click on notification settings tab"""
    app_settings_page.click_Notification_Settings_Tab()
    """"verify notification settings toggle buttons and text"""
    app_settings_page.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
    """"scroll till messages tab"""
    app_settings_page.Scroll_Till_Messages_Tab()
    """""click Messages tab"""
    app_settings_page.click_Mesages_Tab()
    """verify messages text and toggle button"""
    app_settings_page.Verify_Messages_Text_And_Toggle_Buttons()
    """"click on hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """click on three dot icon"""
    app_settings_page.click_Three_Dot_On_Workspace()
    """""click change theme"""
    app_settings_page.click_Change_Theme()
    """"click on electic theme to change the theme"""
    app_settings_page.check_Change_Electic_Theme()
    """click on save & exit"""
    app_settings_page.click_Save_Exit_Btn()
    """verify notifications text is displaying"""
    app_settings_page.Verify_Notifications_Text_IS_Displaying()
    """"verify updated messages tab color"""
    app_settings_page.Verify_Updated_MessagesTab_Color()
    """scroll right till Notification settings"""
    app_settings_page.Scroll_Right()
    """click on Notification Settings tab"""
    app_settings_page.click_Notification_Settings_Tab()
    """verify updtaed Notification settings messages"""
    app_settings_page.Verify_Updated_Notifications_SettingsTab_Messages_Color()
    """click on hamburger menu"""
    login_page.click_Menu_HamburgerICN()
    """click on three dot icon"""
    app_settings_page.click_Three_Dot_On_Workspace()
    """click on change theme"""
    app_settings_page.click_Change_Theme()
    """"click on change modern theme"""
    app_settings_page.check_Change_Modern_Theme()
    """click on save & exit button"""
    app_settings_page.click_Save_Exit_Btn()
    """stop the app"""
    common_method.Stop_The_App()

### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#
def test_AppSettings_TestcaseID_51788():
    """""Sign in with existing Non-Zebra User Account, then sign out"""

    """"App should be in logged in condition & printer should be added"""""


    """"start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"click on the hamburger menu icon"""
    login_page.click_Menu_HamburgerICN()
    """click on the pen icon"""
    app_settings_page.click_pen_Icon_near_UserName()
    """"scroll till delete account """
    app_settings_page.Scroll_till_Delete_Account()
    """click on logout """
    app_settings_page.click_Logout_Btn()
    """"click on login page"""
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    sleep(2)
    """verify home text is present on home page"""
    app_settings_page.Home_text_is_present_on_homepage()
    """stop the app"""
    common_method.Stop_The_App()
# ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_51705():
    """Check clicking the photo taken by camera will not affect uploading photo as user avatar""""""
    """"""""App should be in logged in condition & printer should be added"""""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on pen icon"""
    app_settings_page.click_pen_Icon_near_UserName()
    """"Verify User settings text in user settings page"""
    app_settings_page.Is_Present_User_Settings_Text()
    """""click on upload photo"""
    app_settings_page.click_User_upload_photo()
    """click on camera option"""
    app_settings_page.click_Mobile_Camera()
    """""click allow if it is present"""
    app_settings_page.Click_Allow_popup()
    """"click on click picture icon"""
    app_settings_page.click_picture()
    """"Verify photo uploaded message"""""
    app_settings_page.Verify_Photo_Uploaded_Message()
    """"click user photo remove image"""
    app_settings_page.click_User_Photo_Remove_Image()
    """stop the app"""
    common_method.Stop_The_App()

###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# #####bug id----SMBM-951
def test_AppSettings_TestcaseID_47924():
    """Verify Should not allow same printer name in all the clients.."""
    #
    """"Account should be having 2 printers"""


    """start the app"""
    common_method.tearDown()
    # ##test_robo_finger()
    ### sleep(6)
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.Click_Next_Button()
    add_a_printer_screen.click_Close_Icon_On_Select_Your_Printer_Screen()
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """click on printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"scroll till the 2nd or 3rd printer"""
    app_settings_page.Scroll_Till_2nd_Printer()
    """click on printer name on the printer settings page"""""
    app_settings_page.click_PrinterName2_On_Printersettings()
    """click on printr name"""
    app_settings_page.click_Printer_Name_Text_Field()
    """click on printer name text field"""
    app_settings_page.clear_First_Name()
    """Rename the Printer Name with a long text (more than 30 characters)"""
    app_settings_page.Rename_PrinterName_With_Same_Name()
    """"click on back icon"""
    app_settings_page.click_Back_Icon()
    """click continue button"""""
    app_settings_page.click_Continue_Button_On_Printer_Update_Failed_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.Scroll_Till_2nd_Printer()
    """"verify previous printer name is displaying"""
    app_settings_page.click_PrinterName2_On_Printersettings()
    """stop the app"""
    common_method.Stop_The_App()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id---SMBM-1937
def test_AppSettings_TestcaseID_47910():
    """""Verify pull-down screen twice then the prints left value can refresh success in home page."""""


    """start the app"""
    common_method.tearDown()
    sleep(3)
    ### add_a_printer_screen.click_Add_A_Printer()
    app_settings_page.Verify_Printer_is_already_added()
    """take the prvious number of cartridges"""
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)

    """click on navigation option"""
    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    sleep(2)
    n=2

    """test the printer to print the label"""
    for i in range(n):
        app_settings_page.click_Test_Print_Button()
        sleep(2)

    sleep(1)
    """Go to the Home Page"""
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)

    """Check wheather the cartridges are updated or not"""
    res = app_settings_page.check_update_cartridge(previous,after,n)
    if res:
        print("success")
    else:
        print("Failed")
    """stop the app"""
    common_method.Stop_The_App()


### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47881():
    """""Verify "How to Unpair Bluetooth" dropdown list should expend with small size screen device."""""



    """"Precondition:
    1. Registered a production user
    2. Install production Mobile App into test device
    3. Login Mobile App with user already added printer"""""


    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on three dot on added printer on home page"""
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    """""click on delete printer button"""
    app_settings_page.click_Delete_Printer_Button()
    """verify delete printer page"""
    app_settings_page.Verify_Delete_Printer_Page()
    """"click Cancel on printer button"""
    app_settings_page.Click_Cancel_On_Delete_Printer_Page()
    """stop the app"""
    common_method.Stop_The_App()

### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47928_Bug1888():
    """UI warning and confirmation verification when printer is deleted before decommissioned(Android)"""
    """"Account should be having 2 printers"""


    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on three dot on added printer on home page"""
    app_settings_page.Verify_Printer_Text()
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    """""click on delete printer button"""
    app_settings_page.click_Delete_Printer_Button()
    """verify delete printer page"""
    app_settings_page.Verify_Delete_Printer_Page()
    app_settings_page.Click_Cancel_On_Delete_Printer_Page()
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    """"click delete printer button"""
    app_settings_page.click_Delete_Printer_Button()
    app_settings_page.click_Delete_Printer_Button()
    """"click yes delete button"""
    app_settings_page.click_Yes_Delete_Button()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify UI of unpair bluetooth dropdown list """
    app_settings_page.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
    """click on unpair bluetooth dropdown list"""""
    app_settings_page.Verify_And_click_Unpair_Bluetooth_dropdown_list()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    app_settings_page.click_Unpair_Icon()
    app_settings_page.click_On_Unpair()
    app_settings_page.click_Confirm_Delete_Popup()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    app_settings_page.click_Done_Btn()
    app_settings_page.Verify_Printer_Is_Not_Displaying()
    """stop the app"""
    common_method.Stop_The_App()
###""""""""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""""