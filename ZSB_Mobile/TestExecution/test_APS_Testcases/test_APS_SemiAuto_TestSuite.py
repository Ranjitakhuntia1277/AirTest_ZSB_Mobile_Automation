from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
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

""""""""""Printer should be added in Google account-zebra21.dvt@gmail.com
Password: Swdvt@#123""""""
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


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
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    """Head open on the printer manually """
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out  Manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Remove_The_Cartridge_And_Close_ThePrinter_Head_Manually()
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    """Turn off the printer manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    aps_notification.Verify_Printer_Status_AS_Offline()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    """Turn oN the printer manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    aps_notification.Verify_Printer_Status_AS_Online()
    """"Make the status as media low manually """
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Change_The_Cartridge_To_Medialow_Manually()
    aps_notification.Verify_Printer_Status_AS_Media_LOW()
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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    """Select the printer manually from the list which has medialow"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Select_The_Printer_Manually()
    aps_notification.Verify_Printer_Status_AS_Media_LOW()

# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_51379():
    """Check the first-time print PDF, then second time print it by another printer and cancel the print job"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
    2. Two target printer are connected with the target mobile app login account and login in the Android device
    3. Printer A is Online, Printer B is cover open/paper out"""""""""
    common_method.Show_popup_To_Add_2_Printer_Manually()
    common_method.Show_popup_To_Turn_ON_PrinterA_And_CoverOpen_And_PaperOut_To_PrinterB_Manually()
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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    common_method.Show_popup_To_Select_Printer_A_Manually()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_On_OK_Button_On_The_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    common_method.Show_popup_To_Verify_Printout_Manually()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    common_method.Show_popup_To_Select_Printer_B_Manually()
    aps_notification.click_Expand_Icon()
    aps_notification.click_And_Enter_5_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()




    aps_notification.click_On_Cancel_Btn_On_The_Popup()
    aps_notification.Verify_Job_Is_Cancelled()
    """"""""""Check Manually all the below steps"""""""""""""""""""""""""""""""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Verify_All_The_Below_Points_Manually()
    """Check printer 2 will print out the correct label"""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out """
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
##### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_49161():
    """Check the paper size is different from the print formats"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """""""""Insert the cartridge which is different from the 4' x 6' label (eg. LC2) into the target printer manually""""""""""""
    """"Check the preview page and the label would be re-sized in the preview page"""""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Insert_Different_Cartridge_Manually()
    aps_notification.click_Print_Icon_Option()
    """Verify the print Manually"""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    # ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_51614():
    """Send multiple jobs but only cancel the first job, check the rest of jobs can be printed out"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
    2. Two target printers are connected with the target mobile app login account and login in the Android device
    3. Prepare  pdf/txt/image files"""""""""


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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Expand_Icon()
    aps_notification.click_And_Enter_50_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    """""""need to execute"""""""
    aps_notification.Verify_Print_job_IS_IN_Progress_Message()
    aps_notification.click_Cancel_Button_On_The_Printing_InProgress_Notification()
    """"""""""Check Manually all the below steps"""""""""""""""""""""""""""""""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Verify_All_The_Below_Points_Manually()
    """""1.that the printer would pause the printing and the print job have been cancelled
    6. Select another PDF or image, select to the same printer to print via printer 2
    Check the job is shown in Printer Spooler, waiting to sent
    7. Cancel the job sending to printer 1
    Check the job can be cancelled successfully
    Check the job for printer 2 will be send successfully
    8. Check printer 2 will print out the correct label"""""""""""""""""""""""""""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    ## """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49154():
    """Check the paper size in print options displayed correctly and can be updated"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.Verify_Labels_Left_Count()
    aps_notification.Verify_Printer_Status()
    aps_notification.Verify_PaperSize()
    """""Open the printer's head manually"""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """""Close the printer's head without any cartridge manually"""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
    aps_notification.Verify_NA_Status()
    """"""""""Open the printer's head and change the cartridge from the printer"""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    common_method.Show_popup_To_Insert_Different_Cartridge_Manually()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_ConfirmationPopup()
    # ######""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
