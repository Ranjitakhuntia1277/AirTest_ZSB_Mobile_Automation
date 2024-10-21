from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ...PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)
from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_APS_Testcases.store import execID, leftId
import inspect

class Android_APS_Print_Preview_Options:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)

""""""""""Printer should be added in Google account-:zebra21.dvt@gmail.com
Password: Swdvt@#123""""""
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()
start_execution_loop(execID)

def test_Android_APS_Print_Preview_TestcaseID_49141():
    """Check the print options in the printing page when sharing a file to print and selecting the ZSB printer"""

    common_method.tearDown()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    ##### common_method.show_popup()
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
    aps_notification.click_And_Enter_Copies_Number_Field()
    aps_notification.Verify_PaperSize()
    aps_notification.Verify_Pages_Number()
    aps_notification.Verify_Black_And_White_Text()
    aps_notification.Verify_Orientation_Text()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()


##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49142():
    """Check it works that APS can print 1 copy 1 page of the supported shared file with default settings"""

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
    aps_notification.Verify_Labels_Left_Count()
    aps_notification.Verify_Default_Value_Is_1()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)


#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49146():
    """Check the multiple copies can be printed in APS"""

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
    aps_notification.Verify_Labels_Left_Count()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)
    aps_notification.click_And_Enter_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49147():
    """Check the user can set the printing range in the preview page in APS"""

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
    aps_notification.click_Expand_Icon()


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49148():
    """Check the cropped option works when printing in APS"""

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
    aps_notification.Verify_Default_Value_Is_1()
    aps_notification.Verify_Labels_Left_Count()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49149():
    """Check the Rotation option works when printing in APS"""

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
    aps_notification.Verify_Portrait_Option()
    aps_notification.click_Expand_Icon()
    aps_notification.Verify_Portrait_View_Is_Displaying()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Portrait_Tab()
    aps_notification.click_Landscape_Option()
    aps_notification.click_Expand_Icon()
    aps_notification.Verify_Landscape_View_Is_Displaying()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()


#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49150():
    """Check the Print in Color vs. Print in Black and White printing option"""

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
    aps_notification.Verify_Black_And_White_Text()
    aps_notification.click_Expand_Icon()


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49151():
    """Check the Single or Double Sided printing option"""
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
    aps_notification.Verify_One_Sided_Option()
    aps_notification.click_Expand_Icon()
    # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49152():
    """	Check the Scaling Percentage option disabled in printing for APS"""
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
    aps_notification.Verify_Percentage_Is_Not_Present()
    aps_notification.click_Expand_Icon()


#     ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49153():
    """Check the printer dropdown list works and can change the printer to print"""

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
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer2_To_Print()
    aps_notification.Verify_Labels_Left_Count()
    aps_notification.Verify_Printer_Status()
    aps_notification.Verify_PaperSize()


#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def test_Android_APS_Print_Preview_TestcaseID_49159():
    """Check it works that APS can print 1 copy with multiple pages of the supported shared file with default settings"""

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
    aps_notification.Verify_Labels_Left_Count()
    aps_notification.Verify_Default_Value_Is_1()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)


#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49165():
    """	Check inputting the invalid copies in print option"""

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
    aps_notification.Verify_Default_Value_Is_1()
    aps_notification.click_And_Enter_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49173():
    """	Check it can not print when inputting out of page range in the printing page"""
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
    aps_notification.click_All_Arrow_Mark()
    aps_notification.Select_Range_Of_Option()
    aps_notification.Select_Start_And_End_Page_Number()
    aps_notification.Verify_Cannot_Select_Greater_than_Maximunpage()


#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49174():
    """Check it can print when selecting the custom range in the printing page"""

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
    aps_notification.click_All_Arrow_Mark()
    aps_notification.Select_Range_Of_Option()
    aps_notification.Select_1_to_1_Page()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    aps_notification.click_Expand_Icon()
    aps_notification.click_All_Arrow_Mark()
    aps_notification.Select_Range_Of_Option()
    aps_notification.Select_2_to_4_Page()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    """""Verify Print results manually"""


#     ######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49191():
    """Printer field is displayed the last selected printer name on print preview page when ever selected a printer"""

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
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
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
    aps_notification.click_OK_On_Confirmation_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()


# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Android_APS_Print_Preview_TestcaseID_49725():
    """Verify the Print Preview layout gets updated as per the Orientation set"""

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
    aps_notification.Verify_Portrait_Option()
    aps_notification.click_Expand_Icon()
    aps_notification.Verify_Portrait_View_Is_Displaying()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Portrait_Tab()
    aps_notification.click_Landscape_Option()
    aps_notification.click_Expand_Icon()
    aps_notification.Verify_Landscape_View_Is_Displaying()


#     ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49786():
    """Printer field is displayed "Select a Printer" when have not select a printer ever on print preview page"""
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
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Android_APS_Print_Preview_TestcaseID_49790():
    """Check print failed when turn off APS ZSB series at print preview page"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    poco.scroll()
    aps_notification.click_Google_Drive_Print_Option()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_And_Turn_OFF_APS()
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
    poco.scroll()
    aps_notification.click_Google_Drive_Print_Option()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.Printer_Is_Not_Displaying()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    aps_notification.click_Connection_Preferences()
    aps_notification.click_Printing_Tab()
    aps_notification.click_ZSB_Series()
    aps_notification.Verify_And_Turn_ON_APS()
    aps_notification.Stop_Android_App()

#    #######""""""""""""""""""""END""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
