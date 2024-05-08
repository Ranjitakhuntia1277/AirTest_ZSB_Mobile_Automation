from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
import pytest
from airtest.core.api import connect_device


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_APS_Printer_Discover:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)

""""""""""Printer should be added in Google account-soho.swdvt.01@gmail.com
Password: Swdvt@#123""""""
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49135():
    """Check the printer should be discoverable by APS which are associated with the currectly login account in the mobile app"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Icon_Is_Present()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Verify_Printer_Status_Is_Present()
    aps_notification.Verify_Labels_left_Is_Present()
    aps_notification.Verify_Bluetooth_Address_Is_Present()
    """"Turn Off the Printer"""
    sleep(2)
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Check Printers MAC address matches with what is on the physical printer manually"""""""""
### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49136():
    """Check the UI of the Add printer page in APS"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.click_ON_Three_Dot_ON_Print_Service_Page()
    aps_notification.click_Search_On_The_Menu()
    aps_notification.click_ON_Three_Dot_ON_Print_Service_Page()
    aps_notification.click_Add_Printer()
    aps_notification.Verify_ZSB_Series_App_Login_Page_Is_Displaying()
#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49158():
    """Check the ZSB printer should also be discoverable if the printer in error statues(offline/head open/paper out)"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    """Turn off the printer manually"""
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49160():
    """Check the new added printer can be discovered in APS"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.Verify_Printer_Icon_Is_Present()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Verify_Printer_Status_Is_Present()
    aps_notification.Verify_Labels_left_Is_Present()
##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Printer_Discover_TestcaseID_49162():
    """Check can not discover the ZSB printers if interrupted the network of Android device when sharing the printed files in APS"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.Turn_OFF_Wifi()
    aps_notification.Printer_Is_Not_Displaying()
    aps_notification.TURN_ON_Wifi()
    aps_notification.click_Available_Printer_To_Print()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49164():
    """"Check the printers should not be discoverable when it is not register in the current mobile app login(even though printer is online)"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49171():
    """"Check the non-ZSB printers should not be discoverable in APS"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49172():
    """"Check it can not search out the printer after log out from the mobile app"""
    common_method.tearDown()
    common_method.Stop_The_App()
    Common_Method.Clear_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.click_Turn_ON_ZSB_Series_Printer()
    aps_notification.Verify_Notification_To_Login()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    aps_notification.Verify_Notification_Is_Not_Displaying()
#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49175():
    """"Check it would ask to turn on the WIFI to search for wireless printer when the Android without connecting WIFI"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.Turn_OFF_Wifi()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.Verify_Turn_ON_Wifi_Popup()
    aps_notification.TURN_ON_Wifi()
    aps_notification.click_ZSB_Series()
    # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49177():
    """"Check APS can also search out the associated printers after force quit the mobile app once have logined"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    common_method.Stop_The_App()

#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'

def test_Android_APS_Printer_Discover_TestcaseID_49178():
    """"Check switch login the account in mobile app , new associated printers searched out, can not search the printers associated with the previous account"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.click_ZSB_Series()
    aps_notification.Stop_Android_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()

# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49180():
    """Update printer name to a long name ,click refresh, check printer name display correct in APS available devices list"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings tab"""""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.clear_First_Name()
    """Rename the Printer Name with a long text (more than 30 characters)"""
    app_settings_page.Rename_PrinterName_With30_Characters()
    app_settings_page.click_Back_Icon()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Verify_Longer_Printer_Name__Is_Present()
#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49183():
    """Check no printer fetched by APS if user never install ZSB APP"""
    common_method.tearDown()
    common_method.Stop_The_App()
    common_method.uninstall_app()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.Verify_Printer_Is_Not_Displaying()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.Verify_Printer_Is_Not_Displaying()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49726():
    """User A log in ZSB and log out then login with user B, check printers in user B displayed in APS available devices list"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49783():
    """Check only associated ZSB printers is displayed in APS available devices list via share file to ZSB flow"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Printer_Discover_TestcaseID_49785():
    """User login in then log out, check printers associated user can NOT be fetched in APS available devices list"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    common_method.Clear_App()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Printer_Is_Not_Displaying()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()

    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def test_Android_APS_Printer_Discover_TestcaseID_49787():
    """Check ZSB series print service is turned on default and printers is fetched out from ZSB workspace"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_50030():
    """Check ZSB printers can be fetched out in ZSB APS after keep ZSB APP idle for more than 1h"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    sleep(30)
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_50205():
    """Check the printers in APS can be fetched out after log out and log in again in mobile app"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    common_method.Clear_App()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Printer_Is_Not_Displaying()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_50206():
    """Check the printers can be updated to the new account B added after switch logging from account A which its printer selected before in APS printing preview page"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Printer_Discover_TestcaseID_50268():
    """User A logs-in ZSB app and logs out then login with user B, check printers in user B displayed in APS available devices list"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_Printer_Name_Is_Present()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_50508():
    """Put the Media low cartridge to the printer, check the status would be media low in APS"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    """Turn off the printer manually"""
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out manually """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    """"Make the status as media low manually """
    aps_notification.Verify_Printer_Status_AS_Media_LOW()

def test_Android_APS_Printer_Discover_TestcaseID_50514():
    """	Check the printer status correct after turn off and then turn on APS"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    """Turn off the printer manually"""
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49179():
    """Check the printer can not be discovered after deleting the printer in the ZSB mobile app"""
    # common_method.tearDown()
    # common_method.Stop_The_App()
    # aps_notification.Stop_Android_App()
    # aps_notification.click_Mobile_SearchBar()
    # aps_notification.click_On_Searchbar2()
    # aps_notification.Enter_Settings_Text_On_SearchBar()
    # aps_notification.click_Settings()
    # aps_notification.click_Connected_Devices()
    # aps_notification.click_Connection_Preferences()
    # aps_notification.click_Printing_Tab()
    # aps_notification.click_ZSB_Series()
    # aps_notification.Verify_Printer_Name_Is_Present()
    # aps_notification.Stop_Android_App()
    # common_method.Start_The_App()
    # app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    # app_settings_page.click_Delete_Printer_Button()
    # app_settings_page.click_Yes_Delete_Button()
    # common_method.Stop_The_App()
    # aps_notification.Stop_Android_App()
    # aps_notification.click_Mobile_SearchBar()
    # aps_notification.click_On_Searchbar2()
    # aps_notification.Enter_Settings_Text_On_SearchBar()
    # aps_notification.click_Settings()
    # aps_notification.click_Connected_Devices()
    # aps_notification.click_Connection_Preferences()
    # aps_notification.click_Printing_Tab()
    # aps_notification.Verify_Printer_Is_Not_Displaying()
    # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49181():
    """"Check no printer fetched by APS login in ZSB account with no printer added"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.Verify_Printer_Is_Not_Displaying()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Printer_Discover_TestcaseID_49182():
    """	Check no printer fetched by APS if user never logged in ZSB APP"""
    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.Verify_Printer_Is_Not_Displaying()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.Verify_Printer_Is_Not_Displaying()
    # ##""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""