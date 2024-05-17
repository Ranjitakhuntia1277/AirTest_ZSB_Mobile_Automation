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
    """Turn off the printer manually"""
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
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
    """Turn off the printer manually"""
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out manually """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    """"Make the status as media low manually """
    aps_notification.Verify_Printer_Status_AS_Media_LOW()
    """Check Printers MAC address matches with what is on the physical printer manually"""""""""
    """""""""Insert the cartridge which is different from the 4' x 6' label (eg. LC2) into the target printer""""""""""""
    """"Check the preview page and the label would be re-sized in the preview page"""""""
# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_51379():
    """Check the first-time print PDF, then second time print it by another printer and cancel the print job"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
    2. Two target printer are connected with the target mobile app login account and login in the Android device
    3. Printer A is Online, Printer B is cover open/paper out"""""""""

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
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_On_OK_Button_On_The_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    """""need to execute"""
    """"Add a new printer and Cover Open on the printer B manually"""
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_On_Cancel_Btn_On_The_Popup()
    aps_notification.Verify_Job_Is_Cancelled()
    """"""""""Check Manually all the below steps"""""""""""""""""""""""""""""""""
    """""1.that the printer would pause the printing and the print job have been cancelled
    6. Select another PDF or image, select to the same printer to print via printer 2
    Check the job is shown in Printer Spooler, waiting to sent
    7. Cancel the job sending to printer 1
    Check the job can be cancelled successfully
    Check the job for printer 2 will be send successfully
    8. Check printer 2 will print out the correct label"""""""""""""""""""""""""""""
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
    aps_notification.Verify_Printer_Status_AS_Offline()
    """Head open on the printer manually """
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """"Make the status as paper out """
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
##### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""