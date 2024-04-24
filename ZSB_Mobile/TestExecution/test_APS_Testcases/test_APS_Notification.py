from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ZSB_Mobile.PageObject.Others import Others


class Android_APS_Notification:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
stop_app("com.zebra.soho_app")
sleep(2.0)

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
others = Others
aps_notification = APS_Notification(poco)

""""""""""Fresh build installation is required, without login"""""""""""""""
"""""Setup:
1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
2. The target printer is connected with the target mobile app login account and login in the Android device"""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_APS_Notification_TestcaseID_49155():
#     """Check user shall be notified if user has not logged in at least once"""
#
#
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# app_settings_page.Scroll_till_Delete_Account()
# app_settings_page.click_Logout_Btn()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# common_method.Start_The_App()
# login_page.click_loginBtn()
# login_page.click_LoginAllow_Popup()
# login_page.click_Loginwith_Google()
# common_method.Stop_The_App()
# aps_notification.Verify_Notification_Is_Not_Displaying()
#
#
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_APS_Notification_TestcaseID_49167():
#     """Check the paper size in Android device to the user when printer is on the error statues(wrong media/head is open/no media)"""
#
# """""Setup:
# 1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
# 2. The target printer is connected with the target mobile app login account and login in the Android device"""""""""""
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Print_Review_Page()
# aps_notification.click_Save_AS_PDF()
# aps_notification.click_All_Printers()
# """""Open the printer's head Manually- & make printer offline manually """"""""
# aps_notification.Verify_Printer_Status_AS_Offline()
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_APS_Notification_TestcaseID_49168():
#     """ Check it can restart the print job in the Android notifications Message list if the error is cleared"""
#
#
# """"""""""Setup:
# 1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
# 2. The target printer is connected with the target mobile app login account and login in the Android device"""""""""""""""
#
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Print_Review_Page()
# aps_notification.click_Save_AS_PDF()
# aps_notification.click_All_Printers()
# aps_notification.click_Available_Printer_To_Print()
# """"""""""need to add & EXECUTE"""""""""
# """"4. Open the printer's head/ paper out/ turn off the printer manually""""""
# """" click on print button"""
# aps_notification.click_Print_Icon_Option()
# aps_notification.Verify_Print_job_sent_successfully_Message()
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_APS_Notification_TestcaseID_49169():
#     """ Check the error messages can be cleared in real time if the error status in printer is fixed"""
#
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Print_Review_Page()
# aps_notification.click_Save_AS_PDF()
# aps_notification.click_All_Printers()
# aps_notification.click_Available_Printer_To_Print()
# """"4. Open the printer's head/ paper out/ turn off the printer manually""""""
# """" click on print button"""
# aps_notification.click_Print_Icon_Option()
# aps_notification.Verify_Print_job_sent_successfully_Message()
# """"5.Recover printer
# Check the labels will be printed out successfully manually"""
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_APS_Notification_TestcaseID_50267():
#     """ Check user will get notification when user is logged out from the ZSB app and tried to use APS"""
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Print_Review_Page()
# aps_notification.click_Save_AS_PDF()
# aps_notification.click_All_Printers()
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# app_settings_page.Scroll_till_Delete_Account()
# app_settings_page.click_Logout_Btn()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Settings_Text_On_SearchBar()
# aps_notification.click_Settings()
# aps_notification.click_Connected_Devices()
# aps_notification.click_Connection_Preferences()
# aps_notification.click_Printing_Tab()
# aps_notification.click_ZSB_Series()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()

# # # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_APS_Notification_TestcaseID_50498():
#     """ Check it will notify user need login when share a file on APS if user not login ZSB series"""
#
#
# """"""""""Fresh build installation is required, without login"""""""""""""""
# """""""""""ZSB Series in APS settings is off"""""""""
#
# common_method.Start_The_App()
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
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_ZSB_Series()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_APS_Notification_TestcaseID_50499():
#     """ Check user can receive the notification also even previously had received once, if the user is not logged into the ZSB series when sharing a file to print in APS"""
#
# common_method.Start_The_App()
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
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_ZSB_Series()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_APS_Notification_TestcaseID_50500():
#     """ Check it will notify user need login to search printers when share another file via APS if user not login ZSB series and a print preview has been opened"""
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_JPG_Image_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_On_Share_Option()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# def test_APS_Notification_TestcaseID_50501():
#     """  Check user would not receive the login notifications if the user remains logged in to the ZSB series during the operation in APS"""
#
#
# common_method.Start_The_App()
# common_method.Stop_The_App()
# common_method.Start_The_App()
# login_page.click_loginBtn()
# login_page.click_LoginAllow_Popup()
# login_page.click_Loginwith_Google()
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
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_Is_Not_Displaying()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_ZSB_Series()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_Is_Not_Displaying()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_Is_Not_Displaying()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_APS_Notification_TestcaseID_50502():
#     """Check the notification will dismiss when user click on the login notification and login successful"""
#
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_pen_Icon_near_UserName()
# app_settings_page.Scroll_till_Delete_Account()
# app_settings_page.click_Logout_Btn()
# common_method.Stop_The_App()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# common_method.Start_The_App()
# login_page.click_loginBtn()
# login_page.click_LoginAllow_Popup()
# login_page.click_Loginwith_Google()
# common_method.Stop_The_App()
# aps_notification.Verify_Notification_Is_Not_Displaying()

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_APS_Notification_TestcaseID_50503():
#     """Check that the notification would not be dismissed after force quit the ZSB printer service or the print preview via APS"""
#
# common_method.Start_The_App()
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
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.click_Mobile_back_icon()
# aps_notification.click_ZSB_Series()
# aps_notification.click_Turn_ON_ZSB_Series_Printer()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# aps_notification.click_Mobile_SearchBar()
# aps_notification.click_On_Searchbar2()
# aps_notification.Enter_Files_Text_On_SearchBar()
# aps_notification.click_Files_Folder()
# aps_notification.click_Drive_Searchbar()
# aps_notification.click_Drive_Searchbar2()
# aps_notification.click_PDF_File_From_The_List()
# aps_notification.click_Suggestion_PDF_File()
# aps_notification.click_PDF_ON_Result()
# aps_notification.click_ON_Three_Dot()
# aps_notification.click_Print_Option()
# aps_notification.Verify_Notification_To_Login()
# aps_notification.Stop_Android_App()
# common_method.Stop_The_App()
# #""""""""""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""