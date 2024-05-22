import logging

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ZSB_Mobile.PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen
from ZSB_Mobile.PageObject.PDF_Printing.PDF_Printing_Android import *
# from setuptools import logging
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen

# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_PDF_Printing:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
pdf_printing = PDF_Printing_Android(poco)
delete_account = Delete_Account_Screen(poco)
""""""""""Printer should be added in Google account-zebra21.dvt@gmail.com
Password: Swdvt@#123""""""
# delete_account.switch_to_different_app()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45808():
    """PDF Print: User NOT login share a PDF to ZSB serial print out then share an other PDF to ZSB serial and print out"""

    common_method.tearDown()
    common_method.Stop_The_App()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Drive_On_Searchbar()
    aps_notification.click_Drive_Folder()
    aps_notification.click_Mobile_Footer_Back_Icon()
    aps_notification.click_Google_Drive_SearchBar2()
    aps_notification.click_PDF_File_From_The_Google_DriveList()
    aps_notification.click_Suggestion_PDF_File_From_Drive()
    aps_notification.click_ON_Three_Dot_To_Print()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45806():
    """Error Handling-Check sharing pdf to ZSB app when the printer is in error status(offline, media out, paper out)will show waring toast"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Verify_No_Warning_Popup()
    """""""Turn Off the Printer manually"""""""""
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """ADD the Cartridge without the paper manually"""
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_PaperOut()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Is_Out_Of_Paper()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Put the media back into the printer manually"""
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Open the printer cover manually"""
    pdf_printing.Verify_Status_Of_The_Printer_As_CoverOpen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Cover_Open()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Close the printer cover manually"""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """Remove the Cartridge manually"""
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_MediaOut()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Is_Out_Of_MediaOut()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45809():
    """Share template PDF files to ZSB Series and print out (ZSB series in different pages)"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_PDF_From_The_List()
    pdf_printing.click_Suggestion_PDF()
    pdf_printing.click_PDF_From_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Click_On_PDF_Print_Review_BackIcon()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_PDF_From_The_List()
    pdf_printing.click_Suggestion_PDF()
    pdf_printing.click_PDF_From_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Click_On_PDF_Print_Review_BackIcon()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_PDF_From_The_List()
    pdf_printing.click_Suggestion_PDF()
    pdf_printing.click_PDF_From_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.click_Share_Option()
    pdf_printing.Select_ZSB_App()
    pdf_printing.Verify_Print_Preview_page()
# ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45810():
    """the printing preview page can be rotated on tablet"""

    # common_method.tearDown()
    # common_method.Stop_The_App()
    # aps_notification.Stop_Android_App()
    # aps_notification.click_Mobile_SearchBar()
    # aps_notification.click_On_Searchbar2()
    # aps_notification.Enter_Files_Text_On_SearchBar()
    # aps_notification.click_Files_Folder()
    # aps_notification.click_Mobile_back_icon()
    # aps_notification.click_Mobile_back_icon()
    # aps_notification.click_Drive_Searchbar()
    # aps_notification.click_Drive_Searchbar2()
    # pdf_printing.click_Adobe_From_The_List()
    # pdf_printing.click_PDF_From_The_List()
    # pdf_printing.click_Suggestion_PDF()
    # pdf_printing.click_PDF_From_Result()
    # aps_notification.click_ON_Three_Dot()
    # pdf_printing.click_Share_Option()
    # pdf_printing.Select_ZSB_App()
    # pdf_printing.Verify_Print_Preview_page()
    # pdf_printing.Verify_The_Printer_As_Online()
    # pdf_printing.Verify_Label_Print_Range_Is_Selected_AS_All()
    # pdf_printing.Verify_Current_Label_Print_Option_IS_Displaying()
    # pdf_printing.Verify_Custom_Label_Print_Option_IS_Displaying()
    # ###pdf_printing.Rotate_The_Print_Preview_Screen()
    pdf_printing.Verify_Print_Preview_Page_After_Rotation()



def test_Android_PDF_Printing_TestcaseID_45811():
    """the end digit should be bigger than the begin digit when choosing Custom radio box"""

    # common_method.tearDown()
    # common_method.Stop_The_App()
    # aps_notification.Stop_Android_App()
    # aps_notification.click_Mobile_SearchBar()
    # aps_notification.click_On_Searchbar2()
    # aps_notification.Enter_Files_Text_On_SearchBar()
    # aps_notification.click_Files_Folder()
    # aps_notification.click_Mobile_back_icon()
    # aps_notification.click_Mobile_back_icon()
    # aps_notification.click_Drive_Searchbar()
    # aps_notification.click_Drive_Searchbar2()
    # pdf_printing.click_Adobe_From_The_List()
    # pdf_printing.click_PDF_From_The_List()
    # pdf_printing.click_Suggestion_PDF()
    # pdf_printing.click_PDF_From_Result()
    # aps_notification.click_ON_Three_Dot()
    # pdf_printing.click_Share_Option()
    # pdf_printing.Select_ZSB_App()
    # pdf_printing.Verify_Print_Preview_page()
    # pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Verify_Label_Print_Range_Is_Selected_AS_All()
    pdf_printing.Verify_Current_Label_Print_Option_IS_Displaying()
    pdf_printing.Verify_Custom_Label_Print_Option_IS_Displaying()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.click_Start_Range_Filed()
    pdf_printing.click_Chnage_Start_Range()
    pdf_printing.click_End_Range_Filed()
    pdf_printing.click_Chnage_End_Range()



