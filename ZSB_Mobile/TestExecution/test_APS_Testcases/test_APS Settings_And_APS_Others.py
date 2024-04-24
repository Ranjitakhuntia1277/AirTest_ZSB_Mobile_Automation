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


class Android_APS_Settings_And_APS_Others:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")

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


def test_APS_Settings_And_APS_Others_TestcaseID_49138():
    """Check the APS can be turn on/off"""

common_method.tearDown()
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
aps_notification.click_Mobile_SearchBar()
aps_notification.click_On_Searchbar2()
aps_notification.Enter_Settings_Text_On_SearchBar()
aps_notification.click_Settings()
aps_notification.click_Connected_Devices()
aps_notification.click_Connection_Preferences()
aps_notification.click_Printing_Tab()
aps_notification.click_ZSB_Series()
aps_notification.click_Turn_ON_ZSB_Series_Printer()
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
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_APS_Settings_And_APS_Others_TestcaseID_49143():
    """Check the UI of the darkness setting in APS settings page"""

common_method.tearDown()
aps_notification.Stop_Android_App()