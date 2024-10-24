from airtest.core.api import auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
# from self import self

from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ...PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
# from poco import poco
# from ...conftest import Conftest
from ...PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device


class iOS_App_Settings:
    pass


uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)
auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
# start_app("com.zebra.soho")
# sleep(5)

# conftest = Conftest(poco)
# conftest.test_conftest()
login_screen_ios = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)


# def test_AppSettings_TestcaseID_47918():
#     """	Verify ZSB app permission works fine."""
#     """""Freshly Install the latest  stage/production app on the phone & printer should be added"""""""""
#
#     """start the app"""
#     common_method.Start_The_iOSApp()
#     login_screen_ios.click_loginBtn()
#     """"""" Allow pop up before login for the fresh installation"""""""
#     login_screen_ios.Verify_LoginAllow_Popup_IS_Displaying()
#     """""for the first installation click on the zsb series popup"""
#     login_screen_ios.click_Allow_Login_Popup()
#     """""Relaunch the app"""
#     common_method.relaunch_iOSapp()
#     """"""" Allow pop up before login for the fresh installation"""""""
#     login_screen_ios.click_Continue_Btn_To_Login()
#     """""for the first installation click on the zsb series popup"""
#     login_screen_ios.click_Allow_Login_Popup()
#     """""Relaunch the app"""
#     common_method.relaunch_iOSapp()
#     """Permission is not displaying due to SMBM-1242"""
#     login_screen_ios.Verify_LoginAllow_Popup_IS_Not_Displaying()
#     # ""'stop the app'
#     common_method.Stop_The_iOSApp()

# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45688():
    """""""""Verify Wifi Settings"""""
    """""Install the latest production app on the phone & printer should be added and it should be connected to wifi"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    common_method.tearDown_iOS()
    """" Allow pop up before login for the fresh installation"""""
    login_screen_ios.click_Allow_Login_Popup()
    """""for the first installation click on the zsb series popup"""
    login_screen_ios.click_Allow_Login_Popup()
    """""""""click on the login button"""""""""""
    login_screen_ios.click_loginBtn()
    sleep(2)
    login_screen_ios.click_Allow_Login_Popup()
    """""""select the login with google option"""""""""
    login_screen_ios.click_Loginwith_Google()
    login_screen_ios.click_GooglemailId()
    login_screen_ios.Enter_Google_UserID()
    app_settings_page_ios.click_Keyboard_back_Icon()
    login_screen_ios.click_Emailid_Nextbtn()
    sleep(2)
    login_screen_ios.click_Password_Nextbtn()
    sleep(9)
    """""""click on the left hamburger menu on the home page"""""""""
    login_screen_ios.click_Menu_HamburgerICN()
    """""click on the printer settings tab"""
    app_settings_page_ios.click_Printer_Settings()
    """""click on the printer tab"""
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    app_settings_page_ios.click_General_Tab()
    """"Verify the Test print button text & tab"""
    app_settings_page_ios.Test_Print_button_is_present_on_printer_settings_page()
    """""""""" click on the wifi tab option"""""""""""
    app_settings_page_ios.click_wifi_tab()
    """""""""validate the Current network text"""""
    app_settings_page_ios.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
    """""""Validate the Network status text is present on the printer settings screen"""""""
    app_settings_page_ios.test_Network_Status_Txt_is_present_on_printer_settings_page()
    """"validate network status result text on the printer settings screen"""
    app_settings_page_ios.get_text_Network_Status_Result_Txt()
    """"""""" Verify IP address text is present on the printer settings screen"""""""""
    app_settings_page_ios.get_text_IPAddress_Txt()
    """""""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
    app_settings_page_ios.IS_Present_Save_Network_Message_Txt()
    """""""verify manage networks text is present & clickable"""""""
    app_settings_page_ios.click_Manage_Networks_Btn()
    """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
    app_settings_page_ios.accept_Continue_popup()
    login_screen_ios.click_Allow_Login_Popup()
    """""""""Verify the Cancel button on the Bluetooth_Connection_Failed_Popup"""""
    app_settings_page_ios.Cancel_is_present_on_Bluetooth_Connection_Failed_Popup()
    """"""""""verify the continue button and click on that"""""
    app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    """"""""""Verify the red remove icon next to the network name"""""
    app_settings_page_ios.click_Red_Icon_to_remove_network()
    sleep(5)
    """"""""""Verify the Add Network text & button & click on that"""""""""""
    app_settings_page_ios.click_Add_Network()
    sleep(3)
    """""""""""""Verify Add network page is opening and verify the text"""""""
    app_settings_page_ios.get_text_Add_Network()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Network_UserName()
    app_settings_page_ios.click_Join_Btn_On_Other_Network_Popup()
    """""test case 7 to 10 need to check on Web portal manually"""
    # """stop the app"""
    common_method.Stop_The_iOSApp()

# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_AppSettings_TestcaseID_45689():
#     """""""""Check Change Theme Function Works"""""
#
#     """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
#     """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#     """""Check whether App is installed or not"""
#
#     """""""""start the app"""""""""""
#     common_method.tearDown_iOS()
#     """""""click hamburger menu"""""""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click three dot on workspace"""""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """""""verify edit text"""""""
#     app_settings_page_ios.get_text_Edit_Txt()
#     """"click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """""verify change theme page pop ups by verifying the change theme header"""
#     app_settings_page_ios.get_text_Change_Theme_Header()
#     sleep(1)
#     """""""change 5 theme and check it should get saved and then need to tap on exit"""""""
#     app_settings_page_ios.check_Change_Electic_Theme()
#     sleep(3)
#     """""click save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     """""""SMBM-986 is still present""""
#     """"After applying the theme check whether it is navigating back to home page not verifying the background image as there is no element present"""
#     sleep(3)
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """""click on hamburger icon on home page"""""
#     login_screen_ios.click_Menu_HamburgerICN()
#     sleep(4)
#     """"click on three dot icon on workspace"""""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """"click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """""check Bohemian theme"""
#     sleep(3)
#     app_settings_page_ios.check_Change_Bohemian_Theme()
#     sleep(3)
#     """""click save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """""click on hamburger icon on home page"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     sleep(2)
#     """"click on three dot icon on workspace"""""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """"click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """""check Professional theme"""
#     sleep(3)
#     app_settings_page_ios.check_Change_Professional_Theme()
#     sleep(3)
#     """""click save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """""click on hamburger icon on home page"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     sleep(4)
#     """"click on three dot icon on workspace"""""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """"click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """""check Maker theme"""
#     sleep(3)
#     app_settings_page_ios.check_Change_Maker_Theme()
#     sleep(3)
#     """""click save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """""click on hamburger icon on home page"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     sleep(4)
#     """"click on three dot icon on workspace"""""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """"click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """""check Modern theme"""
#     sleep(3)
#     app_settings_page_ios.check_Change_Modern_Theme()
#     sleep(3)
#     # """""click save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_45690():
#     """""""""Update Unit of Measure in Mobile App, check it will sync to Web Portal and Printer Tools"""""
#
#     """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
#     """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#     """""Check whether App is installed or not"""
#
#
#     """""start the app"""
#     common_method.tearDown_iOS()
#     """""click hamburger menu"""""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on the pen icon near the user name"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     sleep(1)
#     poco.scroll()
#     """"""""""verify units of measurement text is present or not"""""""""
#     app_settings_page_ios.check_If_Units_of_Measurements_Is_Present()
#     """""""verify  Inches is the by default value is displaying"""""""
#     app_settings_page_ios.click_Units_of_Measurements()
#     sleep(2)
#     """"Verify all the available values"""""
#     app_settings_page_ios.verify_Milimetres_Is_Present()
#     app_settings_page_ios.verify_Centimetres_Is_Present()
#     app_settings_page_ios.verify_Inches_Is_Present()
#     sleep(2)
#     """"click on Centimeters option"""
#     app_settings_page_ios.click_Centimeters()
#     sleep(1)
#     """""""""verify the updated message popup"""""
#     app_settings_page_ios.verify_updated_msg()
#     """""""Click on the hamburger icon"""""""
#     sleep(2)
#     login_screen_ios.click_Menu_HamburgerICN()
#     """""click on the home tab"""
#     app_settings_page_ios.click_Home_Tab()
#     sleep(2)
#     """""""""verify printer details, everything should display in centimeters"""""
#     app_settings_page_ios.verify_printer_details_in_Centimeters()
#     sleep(2)
#     login_screen_ios.click_Menu_HamburgerICN()
#     """""click on my design tab"""
#     app_settings_page_ios.click_My_Design()
#     sleep(4)
#     """""verify the design size under my design"""
#     app_settings_page_ios.verify_My_Details_Design_in_Centimeters()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     sleep(1)
#     poco.scroll()
#     app_settings_page_ios.click_Units_of_Measurements()
#     sleep(2)
#     app_settings_page_ios.click_Inches()
#     sleep(2)
#     """Syncing to web portal is not working properly so need to verify manually"""
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# # # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_45691():
#     """""""""Edit Workspace - upload and remove image"""""
#
#
#     """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
#     """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#     """""Check whether App is installed or not"""
#
#     """"start the app"""""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     sleep(2)
#     """""verify the Edit workspace text"""
#     app_settings_page_ios.get_text_Edit_Workspace()
#     """""""click upload photo"""""""
#     app_settings_page_ios.click_upload_photo()
#     sleep(2)
#     """""click on the 1st image"""
#     app_settings_page_ios.click_On_First_Image_SearchBar()
#     app_settings_page_ios.click_First_Image()
#     app_settings_page_ios.click_JPG_ON_Result()
#     """click on the save & exit"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(2)
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     app_settings_page_ios.click_Remove_Image()
#     app_settings_page_ios.click_Save_Exit_Btn()
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     app_settings_page_ios.Is_Present_Profile_Avatar_Letter()
#     sleep(2)
#     app_settings_page_ios.click_upload_photo()
#     app_settings_page_ios.click_Back_Icon()
#     sleep(2)
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_45692():
#     """""""""Edit Workspace - Update workspace name"""""
#
#     """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
#     """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#     """""Check whether App is installed or not"""
#
#
#     """"start the app"""""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     sleep(2)
#     """""verify the Edit workspace text"""
#     app_settings_page_ios.get_text_Edit_Workspace()
#     """"Verify Workspace Name Text"""
#     sleep(2)
#     app_settings_page_ios.Is_Present_Workspace_Name_Text()
#     """""""click on workspace name"""""""""
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     # """""clear workspace name text field"""
#     app_settings_page_ios.Clear_Workspace_Name()
#     sleep(2)
#     """"Click on keyboard back icon"""
#     app_settings_page_ios.click_Keyboard_back_Icon()
#     """""""""""Verify save & exit option is not there"""""""""
#     app_settings_page_ios.Verify_SaveExit_Option_Is_Not_There()
#     """""click on back icon on edit workspace"""
#     app_settings_page_ios.click_back_Icon_On_Edit_Workspace()
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     sleep(2)
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     app_settings_page_ios.Clear_Workspace_Name()
#     """"verify the workspace field by giving space """
#     app_settings_page_ios.Update_Workspace_Name_With_Space()
#     app_settings_page_ios.click_Save_Exit_Btn()
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     app_settings_page_ios.Clear_Workspace_Name()
#     sleep(2)
#     """"Click on keyboard back icon"""
#     app_settings_page_ios.click_Keyboard_back_Icon()
#     sleep(1)
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     """"verify the workspace field by special characters with more than 30 characters """
#     app_settings_page_ios.Update_Workspace_Name_With_Special_Characters_with_30_characters()
#     sleep(3)
#     """""click on save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     app_settings_page_ios.click_Edit_Txt()
#     """"""""""Verify the workspace updated name"""""""""""""""
#     app_settings_page_ios.Verify_Updated_Name()
#     sleep(3)
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     app_settings_page_ios.Clear_Workspace_Name()
#     sleep(2)
#     """"Click on keyboard back icon"""
#     app_settings_page_ios.click_Keyboard_back_Icon()
#     app_settings_page_ios.click_Workspace_Name_Text_Field()
#     app_settings_page_ios.Update_Workspace_Name_with_Original_Name()
#     """""click on save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     sleep(3)
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# # # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_45705():
#     """""""""Verify account profile update for non-Zebra user"""""
#
#
#     """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
#     """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
#     """""Check whether App is installed or not"""
#
#
#     """""""start the app"""""""
#     common_method.tearDown_iOS()
#     """""click hamburger menu"""""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on the pen icon near the user name"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """""""verify First name text is present"""""""
#     app_settings_page_ios.Is_Present_First_Name_Text()
#     """""""verify last name text is present"""""""
#     app_settings_page_ios.Is_Present_Last_Name_Text()
#     """""click first name text field"""
#     app_settings_page_ios.click_First_Name_Text_Field()
#     """"clear first name field"""
#     app_settings_page_ios.clear_First_Name()
#     """""Update first name with special characters with 30 characters"""
#     app_settings_page_ios.Update_First_Name_With_Special_Characters_with_30_characters()
#     sleep(3)
#     """""click last name text field"""
#     app_settings_page_ios.click_Last_Name_Text_Field()
#     """"clear Last name field"""
#     app_settings_page_ios.clear_Last_Name()
#     """""Update last name with special characters with 30 characters"""
#     app_settings_page_ios.Update_Last_Name_With_Special_Characters_with_30_characters()
#     sleep(3)
#     """"verify the updated names message"""
#     app_settings_page_ios.verify_Your_changes_have_been_saved_Message()
#     sleep(3)
#     """""click last name text field"""
#     app_settings_page_ios.click_Last_Name_Text_Field()
#     """"clear Last name field"""
#     app_settings_page_ios.clear_Last_Name()
#     """Update the default Last name"""
#     app_settings_page_ios.Update_Default_Last_Name()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """""click First name text field"""
#     app_settings_page_ios.click_First_Name_Text_Field()
#     """"clear First name field"""
#     app_settings_page_ios.clear_First_Name()
#     """Update the default First name"""
#     app_settings_page_ios.Update_Default_First_Name()
#     """""""change password link is not opening the correct page---SMBM-1098, due to this bug could not automate"""""
#     """""""change email is not yet implemented so could not automate this"""""""""
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47810():
#     """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
#     """"Install the latest production app on the phone & printer should be added with logged in condition Create the object for Login page & Common_Method page to reuse the methods"""
#     """""Check whether App is installed or not"""""
#
#     """""start the app"""""
#     common_method.tearDown_iOS()
#     """"Click on hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on  home tab"""
#     app_settings_page_ios.click_Home_Tab()
#     sleep(2)
#     """""verify printer is already added or not"""
#     app_settings_page_ios.Verify_Printer_is_already_added()
#     sleep(1)
#     """""""verify recently printed labels is present"""""""
#     app_settings_page_ios.Is_Present_Recently_Printed_Labels_Text()
#     """click on the first recently present label"""
#     app_settings_page_ios.click_Firstone_In_Recently_Prtinted_Label()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47820():
#     """"Verify ZSB app home page (overview page) should scroll to the bottom of the list in Recently Printed Labels"""""
#
#     """"Precondition:
#     1. Install the latest production app on the tablet
#     2. Prepare a production with printer added and sign in
#     3. There are 6 Recently Printed Lables present in account"""""
# #
#
#     """""""start the app"""""""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on  home tab"""
#     app_settings_page_ios.click_Home_Tab()
#     sleep(2)
#     """""verify printer is already added or not"""
#     app_settings_page_ios.Verify_Printer_is_already_added()
#     sleep(1)
#     """""""verify recently printed labels is present"""""""
#     app_settings_page_ios.Is_Present_Recently_Printed_Labels_Text()
#     """""""verify first recent lebel is present"""""""
#     app_settings_page_ios.Is_Present_Firstone_In_Recently_Printed_Label()
#     poco.scroll()
#     """"Verify buy more labels is present"""
#     app_settings_page_ios.Is_Present_Buy_More_Labels()
#     sleep(3)
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47825():
#     """""Verify ZSB app doesn't shows error as "Logout failed. Please try logging out again"."""""
#
#     #
#     """Precondition:
#     1. Registered a production user
#     2. Install production Mobile App into test device"""
# #
#
#     """""""start the app"""""""
#     common_method.tearDown_iOS()
#     sleep(3)
#     """""click on hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """""click on the pen icon near to user name"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """Verify User settings text is present"""
#     app_settings_page_ios.Is_Present_User_Settings_Text()
#     """"Scroll till the delete button"""
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     """"Verify Logout button"""
#     app_settings_page_ios.Is_Present_Logout_Btn()
#     """"click on the delete account button"""
#     app_settings_page_ios.click_Delete_Account_Btn()
#     """"Verify Delete account text is present"""
#     app_settings_page_ios.verify_Delete_Account_Text()
#     """verify Please Acknowledge text is present"""""
#     app_settings_page_ios.verify_Please_Acknowledge_Text()
#     """""verify & click on first checkbox """
#     app_settings_page_ios.click_First_Checkbox()
#     """""verify & click on second checkbox """
#     app_settings_page_ios.click_Second_Checkbox()
#     """""verify & click on third checkbox """
#     app_settings_page_ios.click_Third_Checkbox()
#     """verify security message text is present"""""
#     app_settings_page_ios.verify_Security_Message_Text()
#     """click on cancel button"""
#     app_settings_page_ios.click_Cancel_Btn()
#     """verify setting text is present"""
#     app_settings_page_ios.Is_Present_User_Settings_Text()
#     """"verify & click on delete account button"""
#     app_settings_page_ios.click_Delete_Account_Btn()
#     """""verify & click on first checkbox """
#     app_settings_page_ios.click_First_Checkbox()
#     """""verify & click on second checkbox """
#     app_settings_page_ios.click_Second_Checkbox()
#     app_settings_page_ios.click_Third_Checkbox()
#     """"click on the confirm button to delete the account"""
#     app_settings_page_ios.click_Confirm_Btn_To_DeleteAccount()
#     """"verify zebra logo is present"""
#     app_settings_page_ios.Is_Present_Zebra_Logo()
#     """verify ZSB printer image is displaying"""""
#     app_settings_page_ios.Is_Present_ZSB_Printer_Icon()
#     """""Verify login page Important messsage text"""
#     app_settings_page_ios.Verify_Login_Page_Important_Message_Text()
#     """click on login button"""
#     login_screen_ios.click_loginBtn()
#     login_screen_ios.click_Allow_Login_Popup()
#     """""""select the login with google option"""""""""
#     login_screen_ios.click_Loginwith_Google()
#     login_screen_ios.click_GooglemailId()
#     login_screen_ios.Enter_Google_UserID()
#     app_settings_page_ios.click_Keyboard_back_Icon()
#     login_screen_ios.click_Emailid_Nextbtn()
#     sleep(2)
#     login_screen_ios.click_Password_Nextbtn()
#     sleep(9)
#     """"verify delete account pop up message"""
#     app_settings_page_ios.Is_Present_Delete_Account_Popup()
#     """"click on cancel button on the pop up"""
#     app_settings_page_ios.click_Cancel_on_Delete_Account_Popup()
#     """"verify settings text is displaying"""
#     app_settings_page_ios.Is_Present_User_Settings_Text()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47879():
#     """""Verify typo and guide message is correct on Searching For your printer page."""""
#
#
#     """Precondition:
#     1. Registered a production user
#     2. Install production Mobile App into test device"""""
#
#
#     """""""start the app"""""""
#     common_method.tearDown_iOS()
#     """"click on hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """""click on Add a printer"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     app_settings_page_ios.click_ZSB_Series_Popup()
#     """""click on start Button"""
#     add_a_printer_page_ios.click_Start_Button()
#     login_screen_ios.click_Allow_Login_Popup()
#     add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
#     add_a_printer_page_ios.click_LED_Guide_Button()
#     """"verify printer led not flashing text"""
#     add_a_printer_page_ios.Verify_Blue_Left_LED_Text_And_Expand()
#     add_a_printer_page_ios.Verify_Red_Right_LED_Text_And_Expand()
#     """click on the printer led guide done button"""
#     add_a_printer_page_ios.click_Printer_LED_Guide_Done_Btn()
#     add_a_printer_page_ios.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47880():
#     """""Verify "Done" Button and text "LED light Behavior Support" position is correct in Printer LED Guide dialog."""""
# #
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"click on hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """""click on Add a printer"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     app_settings_page_ios.click_ZSB_Series_Popup()
#     """""click on start Button"""
#     add_a_printer_page_ios.click_Start_Button()
#     add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
#     add_a_printer_page_ios.click_LED_Guide_Button()
#     """click on the printer led guide done button"""
#     add_a_printer_page_ios.click_Printer_LED_Guide_Done_Btn()
#     add_a_printer_page_ios.Click_Next_Button()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_47911():
#     """ Verify auto Label Feed On Printer Cover Close value doesn't retrieve in progress after changing darkness level."""
#
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"verify printer is already added"""
#     app_settings_page_ios.Verify_Printer_is_already_added()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on Printer settings tab"""
#     app_settings_page_ios.click_Printer_Settings()
#     """"click on printer name on the printer settings page"""
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     """verify general tab text"""
#     app_settings_page_ios.Verify_General_Tab_Text()
#     """"verify printer name text"""
#     app_settings_page_ios.Verify_Printer_Name_Text()
#     """verify darkness level bar is present & change the darkness level"""
#     app_settings_page_ios.Verify_Darkness_Level_Bar()
#     """"change the darkness level"""
#     app_settings_page_ios.Change_Darkness_Level_Bar()
#     """verify the darkness updated message"""
#     app_settings_page_ios.Verify_Darkness_Updated_Message()
#     """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
#     app_settings_page_ios.Check_toggle_button()
#     """click on the toggle button"""
#     app_settings_page_ios.click_toggle_button()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47914():
#     """Android Only-Verify there is no unknown printer appeared in the Bluetooth list."""
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on add a printer"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     app_settings_page_ios.click_ZSB_Series_Popup()
#     """""click on start Button"""
#     add_a_printer_page_ios.click_Start_Button()
#     add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
#     add_a_printer_page_ios.Click_Next_Button()
#     """"verify searching for your printer text"""
#     add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page_ios.Verify_Select_your_printer_Text()
#     add_a_printer_page_ios.Verify_Discovered_Devices_Text()
#     add_a_printer_page_ios.Verify_same_ZSB_image_for_all_items()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47915():
#     """""Printer Bluetooth List displays printers which have already been added even if "Show All Printers" is not selected."""
#
#
#
#     """start the app"""""
#     common_method.tearDown_iOS()
#     """"verify home text is displaying on the home screen"""
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     app_settings_page_ios.click_ZSB_Series_Popup()
#     """"click on the start button"""
#     add_a_printer_page_ios.click_Start_Button()
#     login_screen_ios.click_Allow_Login_Popup()
#     add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
#     add_a_printer_page_ios.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page_ios.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     # add_a_printer_screen.click_2nd_Printer_Details_To_Add()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_47917():
#     """Verify Printer’s name is too long which should not causes app get stuck and style error at Printer Settings page."""
#
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on printer settings tab"""""
#     app_settings_page_ios.click_Printer_Settings()
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     app_settings_page_ios.click_Printer_Name_Text_Field()
#     app_settings_page_ios.clear_Printer_Name()
#     """Rename the Printer Name with a long text (more than 30 characters)"""
#     app_settings_page_ios.Rename_PrinterName_With30_Characters()
#     app_settings_page_ios.click_Back_Icon()
#     app_settings_page_ios.Verify_Exceeding_Characters_Message()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_Printer_Settings()
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     app_settings_page_ios.click_Printer_Name_Text_Field()
#     app_settings_page_ios.clear_Printer_Name()
#     app_settings_page_ios.Update_PrinterName()
#     app_settings_page_ios.click_Back_Icon()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_47923():
#     """Verify changing password should log out all clients."""
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     app_settings_page_ios.click_Logout_Btn()
#     login_screen_ios.click_loginBtn()
#     login_screen_ios.click_Allow_Login_Popup()
#     login_screen_ios.click_Login_With_Email_Tab()
#     login_screen_ios.click_Password_TextField()
#     login_screen_ios.Enter_Zebra_Password()
#     login_screen_ios.click_SignIn_Button()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     app_settings_page_ios.click_Change_Password_Btn()
#     app_settings_page_ios.click_Cookies_Close_Icon()
#     app_settings_page_ios.Verify_Password_Recovery_Text_Is_Displaying()
#     """After changing the password, it should logged out. this needs to be validated Manually"""""
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# ### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_47956():
#     """Upload avatar via "Photo Gallery" using the default interface of Onedrive"""
#
#     #
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on pen icon"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """"Verify User settings text in user settings page"""
#     app_settings_page_ios.Is_Present_User_Settings_Text()
#     """""click on upload photo"""
#     app_settings_page_ios.click_User_upload_photo()
#     """click on camera option"""
#     app_settings_page_ios.click_Mobile_Camera()
#     """""click allow if it is present"""
#     app_settings_page_ios.Click_Allow_popup()
#     """"click on click picture icon"""
#     app_settings_page_ios.click_picture()
#     app_settings_page_ios.click_Use_Photo()
#     """"Verify photo uploaded message"""""
#     app_settings_page_ios.Verify_Photo_Uploaded_Message()
#     """"click user photo remove image"""
#     app_settings_page_ios.click_User_Photo_Remove_Image()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_49665():
#     """Manage network- Check Bluetooth Connection failed dialog will pop up after BT Paring Request dialog disappeared"""
#     """"WIFI should not be connected in wifi section under printer name"""
#
#     #
#     """start the app"""
#     common_method.tearDown_iOS()
#     """click on hamburger menu"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click printer settings tab"""
#     app_settings_page_ios.click_Printer_Settings()
#     """click on printer name"""
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     """"click wifi tab"""
#     app_settings_page_ios.click_wifi_tab()
#     """"click manage network buttons"""
#     app_settings_page_ios.click_Manage_Networks_Btn()
#     """"verify bluetooth connection required text"""
#     app_settings_page_ios.get_text_Bluetooth_connection_required_Txt()
#     """""click continue button on bluetooth connection required"""
#     app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
#     """"verify bluetooth_connection failed popup"""
#     app_settings_page_ios.Verify_Bluetooth_Connection_Failed_Popup()
#     """""click continue button on connection failed popup"""
#     app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
#     """"click on manage networks button"""
#     app_settings_page_ios.click_Manage_Networks_Btn()
#     app_settings_page_ios.click_Back_Icon()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# # ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_49960():
#     """Check click change password in user profile page: it added callback url, responsce_type, client_id and redirect_url parameters"""
#
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     app_settings_page_ios.click_Logout_Btn()
#     login_screen_ios.click_loginBtn()
#     login_screen_ios.click_Allow_Login_Popup()
#     login_screen_ios.click_Login_With_Email_Tab()
#     login_screen_ios.click_Password_TextField()
#     login_screen_ios.Enter_Zebra_Password()
#     login_screen_ios.click_SignIn_Button()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     app_settings_page_ios.click_Change_Password_Btn()
#     app_settings_page_ios.click_Cookies_Close_Icon()
#     app_settings_page_ios.Verify_Password_Recovery_Text_Is_Displaying()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_49961():
#     """Check after change password, click return to login will navigate to login page and user able to login with new password success"""
#
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     login_screen_ios.click_Menu_HamburgerICN()
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     app_settings_page_ios.click_Change_Password_Btn()
#     app_settings_page_ios.click_Cookies_Close_Icon()
#     app_settings_page_ios.Verify_Change_Password_PageURL_Is_Displaying()
#     app_settings_page_ios.Verify_Password_Recovery_Text_Is_Displaying()
#     app_settings_page_ios.click_Password_Recovery_Email_TextField()
#     app_settings_page_ios.click_Submit_On_Password_Recovery_Screen()
#     """"other steps are blocked due to SMBM-2234 & SMBM-1098"""
#     """"After changing the password, login screen and login should be verified manually"""
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_50031():
#     """Check the error message prompted when print test page and printer head open or offline"""
#
#
#     """printer should be online"""
#     """start the app"""
#     common_method.tearDown_iOS()
#     sleep(3)
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on printer settings tab"""""
#     app_settings_page_ios.click_Printer_Settings()
#     """"click on printer name on printer settings page"""
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     """verify printer name text"""
#     app_settings_page_ios.Verify_Printer_Name_Text()
#     """click test print button"""
#     app_settings_page_ios.click_Test_Print_Button()
#     """"Verify Printed successfully text"""
#     app_settings_page_ios.Verify_Printed_Successfully_Text()
#     """click test print button"""
#     app_settings_page_ios.click_Test_Print_Button()
#     """"Turn off the Printer manually"""
#     """""verify error message of cover open"""
#     app_settings_page_ios.Verify_ErrorMessage_Text()
#     """""Cover close on the printer manually"""""
#     """"click on test print"""
#     app_settings_page_ios.click_Test_Print_Button()
#     """"Verify Printed successfully text"""
#     app_settings_page_ios.Verify_Printed_Successfully_Text()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ## """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_50333():
#     """Android only- Check it will back to manage network after clicking device’s back button"""""
#     """""App should be in logged in condition & printer should be added"""""
# #
#
#     """"start the app"""
#     common_method.tearDown_iOS()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on the printer settings tab"""
#     app_settings_page_ios.click_Printer_Settings()
#     """click on the printer name"""
#     app_settings_page_ios.click_PrinterName_On_Printersettings()
#     """"click on the wifi tab"""
#     app_settings_page_ios.click_wifi_tab()
#     """click on the Manage network button"""
#     app_settings_page_ios.click_Manage_Networks_Btn()
#     """"verify bluetooth connection required text"""
#     app_settings_page_ios.get_text_Bluetooth_connection_required_Txt()
#     app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
#     """""Due to bug id SMBM-2243, step 5 is blocked"""
#     """Turn off printer Manually"""
#     """"verify bluetooth connection failed pop up"""
#     app_settings_page_ios.Verify_Bluetooth_Connection_Failed_Popup()
#     app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_51702():
#     """Check the UI of toggle buttons on Notification Settings""""""
#     """"App should be in logged in condition & printer should be added"""
#     #
#     #
#     """"start the app"""
#     common_method.tearDown_iOS()
#     """click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on Notifications Tab"""
#     app_settings_page_ios.click_Notifications_Tab()
#     """"Scroll till Notification Settings Tab"""
#     app_settings_page_ios.Scroll_Till_Next_Tab()
#     """click on notification settings tab"""
#     app_settings_page_ios.click_Notification_Settings_Tab()
#     """"verify notification settings toggle buttons and text"""
#     app_settings_page_ios.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
#     """"scroll till messages tab"""
#     app_settings_page_ios.Scroll_Till_Messages_Tab()
#     """""click Messages tab"""
#     app_settings_page_ios.click_Mesages_Tab()
#     """verify messages text and toggle button"""
#     app_settings_page_ios.Verify_Messages_Text_And_Toggle_Buttons()
#     """"click on hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """click on three dot icon"""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """""click change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """"click on electic theme to change the theme"""
#     app_settings_page_ios.check_Change_Electic_Theme()
#     """click on save & exit"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     """verify notifications text is displaying"""
#     app_settings_page_ios.Verify_Notifications_Text_IS_Displaying()
#     """"verify updated messages tab color"""
#     app_settings_page_ios.Verify_Updated_MessagesTab_Color()
#     """scroll right till Notification settings"""
#     app_settings_page_ios.Scroll_Right()
#     """click on Notification Settings tab"""
#     app_settings_page_ios.click_Notification_Settings_Tab()
#     """verify updtaed Notification settings messages"""
#     app_settings_page_ios.Verify_Updated_Notifications_SettingsTab_Messages_Color()
#     """click on hamburger menu"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """click on three dot icon"""
#     app_settings_page_ios.click_Three_Dot_On_Workspace()
#     """click on change theme"""
#     app_settings_page_ios.click_Change_Theme()
#     """"click on change modern theme"""
#     app_settings_page_ios.check_Change_Modern_Theme()
#     """click on save & exit button"""
#     app_settings_page_ios.click_Save_Exit_Btn()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_AppSettings_TestcaseID_51705():
#     """Check clicking the photo taken by camera will not affect uploading photo as user avatar""""""
#     """"""""App should be in logged in condition & printer should be added"""""
# #
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     """"click on the hamburger icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """"click on pen icon"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """"Verify User settings text in user settings page"""
#     app_settings_page_ios.Is_Present_User_Settings_Text()
#     """""click on upload photo"""
#     app_settings_page_ios.click_User_upload_photo()
#     """click on camera option"""
#     app_settings_page_ios.click_Mobile_Camera()
#     """""click allow if it is present"""
#     app_settings_page_ios.Click_Allow_popup()
#     """"click on click picture icon"""
#     app_settings_page_ios.click_picture()
#     app_settings_page_ios.click_Use_Photo()
#     """"Verify photo uploaded message"""""
#     app_settings_page_ios.Verify_Photo_Uploaded_Message()
#     """"click user photo remove image"""
#     app_settings_page_ios.click_User_Photo_Remove_Image()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_51788():
#     """""Sign in with existing Non-Zebra User Account, then sign out"""
#     """"App should be in logged in condition & printer should be added"""""
#
#
#     """"start the app"""
#     common_method.tearDown_iOS()
#     """"click on the hamburger menu icon"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """click on the pen icon"""
#     app_settings_page_ios.click_pen_Icon_near_UserName()
#     """"scroll till delete account """
#     app_settings_page_ios.Scroll_till_Delete_Account()
#     """click on logout """
#     app_settings_page_ios.click_Logout_Btn()
#     """"click on login page"""
#     login_screen_ios.click_loginBtn()
#     login_screen_ios.click_Allow_Login_Popup()
#     """""""select the login with google option"""""""""
#     login_screen_ios.click_Loginwith_Google()
#     login_screen_ios.click_GooglemailId()
#     login_screen_ios.Enter_Google_UserID()
#     app_settings_page_ios.click_Keyboard_back_Icon()
#     login_screen_ios.click_Emailid_Nextbtn()
#     sleep(2)
#     login_screen_ios.click_Password_Nextbtn()
#     sleep(9)
#     """verify home text is present on home page"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
#
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_47881():
#     """""Verify "How to Unpair Bluetooth" dropdown list should expend with small size screen device."""""
#
# #
#     """"Precondition:
#     1. Registered a production user
#     2. Install production Mobile App into test device
#     3. Login Mobile App with user already added printer"""""
#
#     """start the app"""
#     common_method.tearDown_iOS()
#     sleep(3)
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on three dot on added printer on home page"""
#     app_settings_page_ios.click_Three_Dot_On_Added_Printer_On_HomePage()
#     """""click on delete printer button"""
#     app_settings_page_ios.click_Delete_Printer_Button()
#     """verify delete printer page"""
#     app_settings_page_ios.Verify_Delete_Printer_Page()
#     """"click delete printer button"""
#     app_settings_page_ios.click_Delete_Printer_Button()
#     """"click yes delete button"""
#     app_settings_page_ios.click_Yes_Delete_Button()
#     """click on unpair bluetooth dropdown list"""""
#     app_settings_page_ios.Verify_And_click_Unpair_Bluetooth_dropdown_list()
#     """"verify UI of unpair bluetooth dropdown list """
#     app_settings_page_ios.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
#
# ### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
# def test_AppSettings_TestcaseID_47928():
#     """UI warning and confirmation verification when printer is deleted before decommissioned(Android)"""
#     """"Account should be having 2 printers"""
#
#     #
#     common_method.tearDown_iOS()
#     """"verify home text is displaying on the home screen"""
#     app_settings_page_ios.Home_text_is_present_on_homepage()
#     """click on three dot on added printer on home page"""
#     app_settings_page_ios.Verify_Printer_Text()
#     app_settings_page_ios.click_Three_Dot_On_Added_Printer_On_HomePage()
#     """""click on delete printer button"""
#     app_settings_page_ios.click_Delete_Printer_Button()
#     """verify delete printer page"""
#     app_settings_page_ios.Verify_Delete_Printer_Page()
#     app_settings_page_ios.Click_Cancel_On_Delete_Printer_Page()
#     app_settings_page_ios.click_Three_Dot_On_Added_Printer_On_HomePage()
#     """"click delete printer button"""
#     app_settings_page_ios.click_Delete_Printer_Button()
#     """"click yes delete button"""
#     app_settings_page_ios.click_Yes_Delete_Button()
#     """"verify UI of unpair bluetooth dropdown list """
#     app_settings_page_ios.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
#     """click on unpair bluetooth dropdown list"""""
#     app_settings_page_ios.Verify_And_click_Unpair_Bluetooth_dropdown_list()
#     common_method.Stop_The_iOSApp()
#     app_settings_page_ios.Stop_iOS_App()
#     app_settings_page_ios.click_Mobile_SearchBar()
#     app_settings_page_ios.click_On_Searchbar2()
#     app_settings_page_ios.Enter_Settings_Text_On_SearchBar()
#     app_settings_page_ios.click_Settings()
#     app_settings_page_ios.click_Bluetooth()
#     app_settings_page_ios.click_Unpair_Icon()
#     app_settings_page_ios.click_On_Unpair()
#     common_method.Start_The_iOSApp()
#     app_settings_page_ios.click_Done_Btn()
#     app_settings_page_ios.Verify_Printer_Is_Not_Displaying()
#     """stop the app"""
#     common_method.Stop_The_iOSApp()
# ###""""""""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""""