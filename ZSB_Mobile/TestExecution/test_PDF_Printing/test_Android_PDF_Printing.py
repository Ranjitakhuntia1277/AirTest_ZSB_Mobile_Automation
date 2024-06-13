import logging

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
# from ZSB_Mobile.PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen


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
pdf_printing = PDF_Printing_Screen(poco)
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
    pdf_printing.click_Send_Copy_For_Google_Drive_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45806():
    """Error Handling-Check sharing pdf to ZSB app when the printer is in error status(offline, media out, paper out)will show waring toast"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
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
    pdf_printing.Select_The_Online_Printer()
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
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Open the printer cover manually"""
    pdf_printing.Verify_Status_Of_The_Printer_As_CoverOpen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Cover_Open()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Close the printer cover manually"""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
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

##### bug id-SMBM-2727
def test_Android_PDF_Printing_TestcaseID_45809():
    """Share template PDF files to ZSB Series and print out (ZSB series in different pages)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Click_On_PDF_Print_Review_BackIcon()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()


# ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45810():
    """the printing preview page can be rotated on tablet"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_Label_Print_Range_Is_Selected_AS_All()
    pdf_printing.Verify_Current_Label_Print_Option_IS_Displaying()
    pdf_printing.Verify_Custom_Label_Print_Option_IS_Displaying()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_To_Current()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()


# #######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45811():
    """the end digit should be bigger than the begin digit when choosing Custom radio box"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.Verify_Label_Print_Range_Is_Selected_AS_All()
    pdf_printing.Verify_Current_Label_Print_Option_IS_Displaying()
    pdf_printing.Verify_Custom_Label_Print_Option_IS_Displaying()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.click_Start_Range_Filed()
    pdf_printing.click_Change_Start_Range()
    pdf_printing.click_End_Range_Filed()
    pdf_printing.Verify_There_IS_NO_1_Option_Is_Available()
    pdf_printing.click_End_Range_Filed()
    pdf_printing.click_Change_Start_Range()
    pdf_printing.click_Start_Range_Filed()


#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45812():
    """Check can share a big size file to ZSB Serial and display with out any issue"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Edit_Option()
    pdf_printing.click_OK_Button_On_Popup()
    pdf_printing.Select_Text_Area_To_Edit()
    pdf_printing.click_Done_Btn()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'

# ##bug id- SMBM-2808
def test_Android_PDF_Printing_TestcaseID_45813():
    """Check can share a big size file to ZSB Serial and display with out any issue"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Edit_Option()
    pdf_printing.click_OK_Button_On_Popup()
    pdf_printing.Select_Text_Area_To_Edit()
    pdf_printing.click_Done_Btn()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Select_2nd_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.click_OK_Button_On_Popup_If_Printer_Is_Offline()


# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45814():
    """Check can share PDF to ZSB serial and login with social media account success"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    common_method.Clear_App()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    sleep(2)
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    sleep(4)
    """""after the issue is fixed, need to delete the below function"""
    # pdf_printing.Switch_To_Different_App()
    # pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page_For_Printer_Online_And_Not_Added()


# #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#### bug id-SMBM-922
def test_Android_PDF_Printing_TestcaseID_45815():
    """change cropper window direction for the pdf file has more than 1 label (apply to current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.Verify_Current_Label_Range_Option_Is_Selected()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45816():
    """change cropper window direction for the pdf file has more than 1 label (apply to all)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.Verify_Current_Label_Range_Option_Is_Selected()
    pdf_printing.click_All_Label_Range_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


# #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45817():
    """	change cropper window chosen area for the pdf file has more than 1 label (apply to current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45818():
    """	change cropper window chosen area for the pdf file has more than 1 label (apply to all)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_All_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id-SMBM-1767
def test_Android_PDF_Printing_TestcaseID_45819():
    """change cropper window direction and chosen area for the pdf file has more than 1 label (apply to current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    """Verify Manually the view of pdf screens for 1st one it will be different and for rest it will be different"""
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45820():
    """change cropper window direction and chosen area for the pdf file has more than 1 label (apply to all)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_All_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    """Verify the view of pdf screens for 1st one it will be different and for rest it will be different"""
    poco.scroll()
    pdf_printing.click_Right_Arrow_of_PDF_On_Preview_Screen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45821():
    """check cancle button on the Edit page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.Verify_Done_Button_Is_Present()
    pdf_printing.Verify_Cancel_Button_Is_Present()
    pdf_printing.click_Cancel_Button()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Right_Arrow_of_PDF_On_Preview_Screen()
    pdf_printing.click_Left_Arrow_of_PDF_On_Preview_Screen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    #     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45822():
    """	change cropper window direction for the pdf file only has 1 label (apply to all/Current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    #     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45823():
    """	change cropper window chosen area for the pdf file only has 1 label (apply to all/Current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45824():
    """	change cropper window direction and chosen area for the pdf file only has 1 label (apply to all/Current)"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45825():
    """	Check printing preview page can update info when changing printer status and cartridge"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    """"""""""""" open the printer head manually"""""""""
    pdf_printing.Verify_Cover_Open_Notification()
    pdf_printing.Verify_Cover_Open_Is_Displaying_In_The_Printer_List()
    """""Take away the printer cartridge, and close the printer head manually"""
    pdf_printing.Verify_PaperOUT_Notification()
    pdf_printing.Verify_PaperOUT_Is_Displaying_In_The_Printer_List()
    """"open the printer head, take away the cartridge and install another type cartridge manually"""
    pdf_printing.Verify_Cover_Closed_Notification()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.Click_On_PDF_Print_Review_BackIcon()
    sleep(10)
    pdf_printing.Verify_Printer_Status_AS_Online_On_Homepage()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Test_Print_Button()


#     ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ####Bug id- SMBM-2371
def test_Android_PDF_Printing_TestcaseID_45826():
    """Mulit-page PDF share to ZSB Serial, select all pages, check all pages can print out success"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.Verify_Label_Print_Range_Is_Selected_AS_All()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Verify_Print_Complete_Popup_Should_Not_present_Again()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45827():
    """Mulit-page PDF share to ZSB Serial, select current page, check current page can print out success"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Move_To_Page_No_3()
    pdf_printing.click_And_Enter_Copies_Number_Field()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Move_To_Page_No_3()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###Bug id- SMBM-1936
def test_Android_PDF_Printing_TestcaseID_45828():
    """Mulit-page PDF share to ZSB Serial, select Custom and select a range, check selected pages can print out success"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Range_1_Is_Displaying()
    pdf_printing.click_Start_Range_Filed()
    pdf_printing.click_Change_Start_Range_To_3()
    pdf_printing.click_Default_End_Range_Filed()
    pdf_printing.click_Change_End_Range_To_6()
    pdf_printing.click_Print_Option_On_PDF_Printing()


#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45829():
    """	about 500-pages PDF share to ZSB Serial, select Custom and select a range, check page number show correnct can select a valid range"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Range_1_Is_Displaying()
    pdf_printing.click_Start_Range_Filed()
    pdf_printing.click_Default_End_Range_Filed()
    pdf_printing.click_Change_End_Range_To_6()
    pdf_printing.click_Print_Option_On_PDF_Printing()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45830():
    """	One Page PDF share to ZSB Serial,select Custom and select a range, check range show 1 to 1 and not able to change"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Range_1_Is_Displaying()
    pdf_printing.click_Start_Range_Filed()
    pdf_printing.click_Default_End_Range_Filed()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45831():
    """	With no printer added, share pdf to ZSB serial, check printer preview display"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Printer_Not_Found_Popup()
    pdf_printing.click_Continue_Button()
    pdf_printing.Verify_Print_Is_GreyedOut()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45832():
    """	With one printer added Share PDF to ZSB Serial, check printer default selected, printer status will displayed"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    """""""Turn Off the Printer manually"""""""""
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45833():
    """	With multi printers added, share PDF to ZSB Serial, check user can select different printer to print"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45834():
    """	With ZSB mobile app installed,open Third Party App click Share button, check "ZSB Serial" in app list"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45835():
    """	Opened and login in Mobile App, From Third App open PDF share to ZSB Serial will open ZSB Serial and show print preview page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45836():
    """	Not login Mobile App, from Third App open PDF file share to ZSB Mobile App , ZSB Mobile app will open login page after login success will show print Preview page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    sleep(2)
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    sleep(4)
    pdf_printing.Verify_Print_Preview_page_For_Printer_Online_And_Not_Added()
    # ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45837():
    """	ZSB Serial login but not run on back ground, from Third App open PDF file share to ZSB Mobile App , ZSB Mobile app will open login page after login success will show print Preview page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#
def test_Android_PDF_Printing_TestcaseID_45838():
    """	ZSB Serial login but not run on back ground, from Third App open PDF """""

    """Blocked due to SMBM-640 SMBM-681 SMBM-792 & SMBM-2808"""


def test_Android_PDF_Printing_TestcaseID_45840():
    """	Open PDF file with Adobe Reader share to ZSB Serial, print Preview and print out then Open another PDF file in Adobe reader Share to ZSB Serail"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ####iOS Bug-SMBM-2874
def test_Android_PDF_Printing_TestcaseID_45841():
    """Open PDF file with Adobe Reader share to ZSB Serial, print Preview and print out then Open another PDF file from Files/Google Drive/ One Drive Share to ZSB Serial"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_Copy_For_Google_Drive_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45842():
    """Open Landscape view PDF file and share to ZSB Serial, check preview page show correct"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45843():
    """Open PDF file contains both portait and landscpage pages, check preivew page show correct"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    """"4. Check print preview show with default printer media size-----this step has to be removed"""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    """""""""5.user can crop any area in pdf file----cropping is not possible as there is no element for the object"""""
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_2nd_Page_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_1st_Page_Option()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45844():
    """Share a 4''x6 '' size pdf to ZSB Serial and print out with 4"x6" media,check the print out label content is as expected"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45846():
    """Printer in Error status, Share a PDF to ZSB serial and click edit label will pop up error dialog"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    """""""Turn Off the Printer manually"""""""""
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """ADD the Cartridge without the paper manually"""
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_PaperOut()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Is_Out_Of_Paper()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Put the media back into the printer manually"""
    """""""Turn ON the printer manually"""""""""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Open the printer cover manually"""
    pdf_printing.Verify_Status_Of_The_Printer_As_CoverOpen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Cover_Open()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Close the printer cover manually"""
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45847():
    """Share a PDF to ZSB serial, check the default print copies value is 1, and can update copies to a valid value print out correct copies"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_Default_Copies_Values_Is_1()
    pdf_printing.Update_Copies_Value()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45848():
    """Share a PDF to ZSB serial, check in print preview page, user input invalid value it will auto change to valid value"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_Default_Copies_Values_Is_1()
    pdf_printing.Update_Copies_Value_To_Special_Characters()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Default_Copies_Values_Is_1()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45849():
    """After updated print Copies in print preview page, the total labels would print out would auto update"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    pdf_printing.click_Send_File_For_Files()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_Default_Copies_Values_Is_1()
    pdf_printing.Update_Copies_Value()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Total_Labels()
    pdf_printing.Update_Copies_Value_To_10()
    pdf_printing.click_Custom_Label_Range_Option()
    pdf_printing.Verify_Total_Labels()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'


def test_Android_PDF_Printing_TestcaseID_45850():
    """"Preview Feature" popup as a dismissible text box"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Edit_Option()
    pdf_printing.click_OK_Button_On_Popup()
    pdf_printing.click_Rotation_Option()
    """""Close icon is not displaying on the popup"""


# ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45851():
    """click back button on the printing preview page would navigate to the Redirect calling App"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Click_On_PDF_Print_Review_BackIcon()
    app_settings_page.Home_text_is_present_on_homepage()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_45852():
    """image file cannot share to ZSB serial"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    aps_notification.click_PNG_Image_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    pdf_printing.Verify_ZSB_APP_Option_Is_Not_There()
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###need to select invalid pdf
def test_Android_PDF_Printing_TestcaseID_45853():
    """Check invalid PDF would fail share to ZSB serial"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45854():
    """the cropper window is resized after switching to a printer with a different cartridge size"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_To_Current()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    """"There is no option the check the media size as it is not displaying on the screen, testcase needs to be modified"""
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_45873():
    """PDF Print: Print a small size design then share a PDF to ZSB serial print out"""

    """""Insert media size is 2.25*4 or 4*3 or 4*6 Manually and verify the printout manually"""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    pdf_printing.click_Common_Design()
    pdf_printing.click_First_Image_ON_The_List()
    pdf_printing.click_firstimage_on_firstone()
    pdf_printing.click_print_Button()
    pdf_printing.click_Print2_button()
    """verify the printout manually"""""
    pdf_printing.click_Back_Icon()
    pdf_printing.click_Back_Icon()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """verify the printout manually"""""
    # ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_47938():
    """Colored logos Printing"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Verify the colored logo on the PDF  Manually on the printout"""


#     ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_47939():
    """User is able to resize the PDF and other images before printing"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_To_Current()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'


def test_Android_PDF_Printing_TestcaseID_47940():
    """User is not able to enter non-number to the Copies field in the print page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_And_Enter_Invalid_Number_In_Copies_Number_Field()
    pdf_printing.Verify_Print_Is_GreyedOut()


# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_47949():
    """To verify the updation on Print Preview Page/ Notification on change in Printer State"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_Print_Preview_page()
    """""""Turn Off the Printer manually"""""""""
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()


# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_PDF_Printing_TestcaseID_47950():
    """To verify the timing behaviour on giving Multiple prints"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_And_Enter_Copies_Number_Field()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.click_And_Enter_2Copies_Number_Field()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    # ###########"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_PDF_Printing_TestcaseID_47951():
    """To verify the selection box on selecting a PDF File"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""#

def test_Android_PDF_Printing_TestcaseID_47952():
    """To verify the pdf settings would change to the original when waking up the screen"""
    #
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_To_Current()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    common_method.Turn_Off_The_Phone()
    sleep(2)
    common_method.Turn_ON_The_Phone()
    poco.scroll()
    pdf_printing.Verify_Print_Preview_page()

#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ####bug id----SMBM-811
def test_Android_PDF_Printing_TestcaseID_47953():
    """To verify the print post Edit Label on Print Preview"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Current_Label_Range_Option()
    pdf_printing.click_Drag_And_Drop_The_Cropper()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """"Verify the proper size, area & content in the printout manually"""
#     #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



# ###bug id---SMBM-829(enhancement)
def test_Android_PDF_Printing_TestcaseID_47954():
    """To verify the scalability for rotated and unrotated PDF Pages"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    pdf_printing.click_Adobe_From_The_List()
    pdf_printing.click_Adobe_Folder()
    pdf_printing.click_Search_Icon_On_Adobe()
    pdf_printing.click_PDF_From_The_Adobe_List()
    pdf_printing.click_ON_Three_Dot_On_Adobe_PDF()
    pdf_printing.click_Share_On_Adobe()
    pdf_printing.click_Send_A_Copy_On_Adobe()
    pdf_printing.Select_ZSB_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""after the issue is fixed, need to delete the below function"""
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Switch_To_Different_App()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_To_Current()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()
    pdf_printing.click_Edit_Label()
    pdf_printing.click_Rotation_Option()
    pdf_printing.click_Done_Btn()
    pdf_printing.Verify_Print_Preview_page()

#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

