from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Others import Others
from airtest.cli.parser import cli_setup
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen


class Android_APS_Printing:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(2.0)
# stop_app("com.zebra.soho_app")
# sleep(2.0)

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

""""""""""Fresh build installation is required,app should be loggedin"""""""""""""""
"""""Setup:
1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
2. The target printers are connected with the target mobile app login account
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_APS_Printing_TestcaseID_49166():
    """check printing around 50 pages and click cancel, the print job is paused"""

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
    # aps_notification.Verify_Print_job_IS_IN_Progress_Message()
    # aps_notification.click_Cancel_Button_On_The_Printing_InProgress_Notification()
    # """"""""""Check Manually that the printer would pause the printing and the print job have been cancelled"""""""""""
    ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49170():
    """Check it can not print when the printer offline"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """Turn off the Printer Manually"""""""""
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    """"Turn on the Printer manually & check the label printed out"""""
    # # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49186():
    """Check APS queue job will be cleared when go to ZSB app to Clear Print Queue"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """Open the head or remove the media Manually"""
    aps_notification.click_Print_Icon_Option()
    """""""Check Manually that the file would not be printed"""
    common_method.Start_The_App()
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    aps_notification.click_On_Clear_Print_Queue()
    aps_notification.click_Clear_Queue_Button()
    common_method.Stop_The_App()
    aps_notification.Expand_StatusBar()
    aps_notification.Verify_Cancelling_Driver_Job_Is_Displaying()
    aps_notification.Collapse_StatusBar()
    """"Close the Printer head manually"""

    # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49187():
    """Check there is a dialog "Use ZSB series" pop up when printing for the first time on APS and click OK will print success"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """""It will only display on The Android device has not printed via ZSB printer in APS yet"""""
    aps_notification.Verify_Use_ZSB_Series_Popup_Is_Displaying()
    aps_notification.click_On_OK_Button_On_The_Popup()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49188():
    """Check dialog "Use ZSB series" would not pop up when printing for NOT the first time on APS"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49189():
    """Check it would not print when click Cancel on the dialog "Use ZSB series"""

    """"Setup:
    The Android device has not printed via ZSB printer in APS yet"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """""It will only display on The Android device has not printed via ZSB printer in APS yet"""""
    aps_notification.Verify_Use_ZSB_Series_Popup_Is_Displaying()
    aps_notification.Verify_Cancel_Button_Is_Displaying()
    aps_notification.Verify_OK_Button_Is_Displaying()
    # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49190():
    """Check "Use ZSB series" dialog would pop up when cancel first time then print via APS again"""
    """"Setup:
    The Android device has not printed via ZSB printer in APS yet"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    """""It will only display on The Android device has not printed via ZSB printer in APS yet"""""
    aps_notification.Verify_Use_ZSB_Series_Popup_Is_Displaying()
    aps_notification.click_On_OK_Button_On_The_Popup()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49204():
    """Check APS can be turn on before selecting printer if it is turn off"""
    """"Setup:
    The Android device has not printed via ZSB printer in APS yet"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
    aps_notification.Verify_And_Turn_OFF_APS()
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
    """""""""""""""""""""need to execute"""""""""""""""
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

#     # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#

def test_APS_Printing_TestcaseID_49778():
    """Check print service shall support all printable forms and can print out success from Google Drive (image,pdf)"""
    """"Setup:
    Pre-condtion:
    Install ZSB app and user has logged in with at least added a printer
    2. ZSB Series in APS settings is ON"""""""""""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    app_settings_page.click_Keyboard_back_Icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PNG_Image_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_51380():
    """Check print PDF once then cancel it when the second time print it with the same online printer"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
    2. 1 target printer is connected with the target mobile app login account and login in the Android device"""""""""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    app_settings_page.click_Keyboard_back_Icon()
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
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.click_Expand_Icon()
    aps_notification.click_And_Enter_50_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    # aps_notification.click_On_Cancel_Btn_On_The_Popup()
    # aps_notification.Verify_Job_Is_Cancelled()

    ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_51383():
    """Check cancel different print jobs (image/pdf/txt) when printer is media out/cover open"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device (Reference path : Settings -> Connection & sharing -> print)
    2. 1 target printer is connected with the target mobile app login account and login in the Android device
    3. The target printer is cover open/ paper out"""""""""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_51384():
    """	Check cancel same print job at least two times when printer status is cover open"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device(Reference path : Settings -> Connection & sharing -> print)
    2. 1 target printer is connected with the target mobile app login account and login in the Android device
    3. The target printer is cover open/ paper out"""""""""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.click_On_OK_Button_On_The_Popup()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.click_Print_Icon_Option()
    # aps_notification.click_On_Cancel_Btn_On_The_Popup()
    # aps_notification.Verify_Job_Is_Cancelled()
    # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_51618():
    """Verify forcing quit app will not affect the printing job"""
    """Pre-condition:
    Setup:
    1. The APS has been ready and turn on in the Android device (Reference path : Settings -> Connection & sharing -> print)
    2. The target printers are connected with the target mobile app login account, printer is online status"""""

    """""SMBM-2447 is blocking"""

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
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Expand_Icon()
    aps_notification.click_And_Enter_50_Copies_Number_Field()
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    common_method.Start_The_App()
    common_method.Stop_The_App()
    """"Verify manually that quiting app will not affect the printing job"""


# ###""""""""""""""""""""""""""""""""END"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def test_APS_Printing_TestcaseID_49144():
    """Check all supported formats files or information can be printed by the printer service"""

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
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_JPG_Image_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Printing_TestcaseID_49157():
    """Check printer print queue can be opened and cancel/delete the print jobs"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    app_settings_page.click_Keyboard_back_Icon()
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
    aps_notification.click_Expand_Icon()
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # aps_notification.Verify_Print_job_IS_IN_Progress_Message()
    # aps_notification.click_Cancel_Button_On_The_Printing_InProgress_Notification()
    ###"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ##""""""""""""""""""""""""""""""""""""""""""END""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# #""""""""""""""""""Google drive""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_49779():
    """Check print service shall support all printable forms and can print out success from One Drive (image,pdf)"""
    """"Setup:
    Pre-condition:
    Install ZSB app and user has logged in with at least added a printer
    2. ZSB Series in APS settings is ON"""""

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
    aps_notification.click_Mobile_back_icon()
    aps_notification.click_Google_Drive_SearchBar2()
    aps_notification.click_PDF_File_From_The_Google_DriveList()
    aps_notification.click_Suggestion_PDF_File_From_Drive()
    aps_notification.click_ON_Three_Dot_To_Print()
    poco.scroll()
    aps_notification.click_Google_Drive_Print_Option()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.click_Available_Printer_To_Print()
    aps_notification.click_Print_Icon_Option()
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
    aps_notification.Verify_Print_job_sent_successfully_Message()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Printing_TestcaseID_49163():
    """Check it can not perform the printing in the preview page when disconnect the Android or the selected ZSB printers"""

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
    """"Check manually that the printer would not print the label"""""
    """Recover the network with the same WIFI network with the Android device"""""
    """"""""""need to execute"""""
    aps_notification.Turn_OFF_Wifi()
    aps_notification.TURN_ON_Wifi()
    """"Check manually that the printer will work once network is back"""""
    aps_notification.click_Print_Icon_Option()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    #
    #
    # # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###""""""""""""""""""""""""""""""""""""""""""END""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
