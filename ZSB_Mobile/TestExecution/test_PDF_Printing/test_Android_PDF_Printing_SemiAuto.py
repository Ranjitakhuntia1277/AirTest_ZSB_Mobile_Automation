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
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    pdf_printing.Verify_No_Warning_Popup()
    """""""Turn Off the Printer manually"""""""""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""""Turn ON the printer manually"""""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """ADD the Cartridge without the paper manually"""
    common_method.Show_popup_To_Add_The_Cartridge_Without_Paper_Manually()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_PaperOut()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Is_Out_Of_Paper()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Put the media back into the printer manually"""
    common_method.Show_popup_To_Put_The_Media_Back_Into_The_printer_Manually()
    """""""Turn ON the printer manually"""""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Open the printer cover manually"""
    common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_CoverOpen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Cover_Open()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Close the printer cover manually"""
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """Remove the Cartridge manually"""
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
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
    common_method.Show_popup_To_Verify_the_view_of_pdf_screens_for_1stone_and_for_rest_it_will_be_different_Manually()
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
    common_method.Show_popup_To_Verify_the_view_of_pdf_screens_for_1stone_and_for_rest_it_will_be_different_Manually()
    poco.scroll()
    pdf_printing.click_Right_Arrow_of_PDF_On_Preview_Screen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()


#     ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    pdf_printing.Verify_Cover_Open_Notification()
    pdf_printing.Verify_Cover_Open_Is_Displaying_In_The_Printer_List()
    """""Take away the printer cartridge, and close the printer head manually"""
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
    pdf_printing.Verify_PaperOUT_Notification()
    pdf_printing.Verify_PaperOUT_Is_Displaying_In_The_Printer_List()
    """"open the printer head, take away the cartridge and install another type cartridge manually and close the printer cover manually"""
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
    common_method.Show_popup_To_Insert_Different_Cartridge_Manually()
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
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
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    """""""Turn ON the printer manually"""""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    """"4. Check print preview show with default printer media size-----this step has to be removed from testcase"""
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
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """ADD the Cartridge without the paper manually"""
    common_method.Show_popup_To_Add_The_Cartridge_Without_Paper_Manually()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_PaperOut()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Is_Out_Of_Paper()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Put the media back into the printer manually"""
    common_method.Show_popup_To_Put_The_Media_Back_Into_The_printer_Manually()
    """""""Turn ON the printer manually"""""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    """""Open the printer cover manually"""
    common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_CoverOpen()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_Cover_Open()
    pdf_printing.Verify_Print_Complete_Popup_IS_Not_Displaying()
    """""Close the printer cover manually"""
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
    pdf_printing.Verify_The_Printer_As_Online()
    pdf_printing.Select_The_Online_Printer()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Print_Complete_Popup()
    # #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    pdf_printing.Verify_Status_Of_The_Printer_As_Offline()
    pdf_printing.click_Print_Option_On_PDF_Printing()
    pdf_printing.Verify_Warnning_Popup_For_Printer_IS_Offline()
    pdf_printing.click_On_OK_Button_On_PrinterOffline_Popup()
    """""Turn On the Printer manually"""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    common_method.Show_popup_To_Verify_Printout_Manually()
#     #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

