from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Login_Screen import *
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import pytest


class Android_App_Printer_Management:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

common_method = Common_Method(poco)
# login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
registration_page = Registration_Screen(poco)
login_page = Login_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
aps_notification = APS_Notification(poco)

def test_PrinterManagement_TestcaseID_47920():
    pass
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("sohozsb@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Swipe up"""
    scroll_view = poco("android.widget.ScrollView")
    """Set the maximum number of swipes to avoid an infinite loop"""
    poco.scroll()
    """Open Printer settings"""
    app_settings_page.click_Printer_Settings()

    """Select printer"""
    printer_management_page.clickPrinter1InPinterSettings()
    printer_2_name = printer_management_page.getPrinter2NameInPrinterSettings()
    print(printer_2_name)
    """Rename printer1 to printer2 name"""
    printer_management_page.setPrinterName(printer_2_name)
    keyevent("Enter")
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Printer Update Failed")
        x=1/0
    except ZeroDivisionError:
        raise Exception("Error pop up if 2 printers have same name.")
    except Exception as e:
        pass
    """Verify is '(1)' is appended to the duplicate name"""
    """Unable to verify due to BUG"""
    printer_management_page.verifyPrinterNameAfterRenaming(printer_2_name)
    common_method.Stop_The_App()


def test_PrinterManagement_TestcaseID_47785():
    pass
    """clear app data"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Click three dot menu of target printer"""
    deletingPrinterName = printer_management_page.clickThreeDotMenu()
    """Click on delete printer"""
    printer_management_page.clickDelete()
    """Verify first Delete dialog pop up window"""
    printer_management_page.checkDeletePopUp(1)
    """Choose delete option"""
    printer_management_page.clickDelete()
    """Verify second Delete dialog pop up window"""
    printer_management_page.checkDeletePopUp(2)
    """Click Yes Delete option"""
    printer_management_page.clickYesDelete()
    """Verify Message box prompt appears "Unpair Bluetooth From Printer" along printer MAC address"""
    printer_management_page.checkUnpairBluetoothPopUp()
    """Message box Does not contain MAC address"""
    """Click Drop Down option"""
    printer_management_page.clickDropDownMenuIcon()
    """Check if Done option is greyed out"""
    printer_management_page.checkElementIsGreyedOut("Done")
    """Unpair device in bluetooth settings"""
    printer_management_page.unpair_bluetooth_device()
    """Click Done"""
    printer_management_page.clickDoneOption()
    common_method.wait_for_element_appearance("Home", 15)
    """Check if printer is decommissioned"""
    printer_management_page.checkIfPrinterIsDecommissioned(deletingPrinterName)
    common_method.Stop_The_App()


def test_PrinterManagement_TestcaseID_47882():
    pass
    common_method.tearDown()
    """Click three dot menu of target printer"""
    printer_management_page.clickThreeDotMenu()
    sleep(5)
    """Click on delete printer"""
    printer_management_page.clickDelete()
    sleep(2)
    """Verify first Delete dialog pop up window"""
    printer_management_page.checkDeletePopUp(1)
    sleep(2)
    """Choose delete option"""
    printer_management_page.clickDelete()
    sleep(2)
    """Verify second Delete dialog pop up window"""
    printer_management_page.checkDeletePopUp(2)
    sleep(2)
    """Click Yes Delete option"""
    printer_management_page.clickYesDelete()
    sleep(2)
    """Verify if there is a pop up: Unpair Printer From Bluetooth"""
    printer_management_page.checkUnpairBluetoothPopUp()
    sleep(2)
    """Verify if the pop up has Drop Down option"""
    printer_management_page.checkDropDownMenuIconIsPresent()
    sleep(2)
    """Click Drop Down option"""
    printer_management_page.clickDropDownMenuIcon()
    sleep(2)
    """Verify if the info in the Drop Down matches with the expected info"""
    printer_management_page.checkDropDownMenuInfo()
    sleep(2)
    """Close the pop up"""
    common_method.Stop_The_App()

# ####"""""""""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45888():
    """	Check user can delete a printer from Mobile App"""

    common_method.tearDown()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    sleep(5)
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on three dot on added printer on home page"""
    app_settings_page.Verify_Printer_Text()
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    """""click on delete printer button"""
    app_settings_page.click_Delete_Printer_Button()
    """verify delete printer page"""
    app_settings_page.Verify_Delete_Printer_Page()
    app_settings_page.Click_Cancel_On_Delete_Printer_Page()
    app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
    """"click delete printer button"""
    app_settings_page.click_Delete_Printer_Button()
    """"click yes delete button"""
    app_settings_page.click_Yes_Delete_Button()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify UI of unpair bluetooth dropdown list """
    app_settings_page.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
    """click on unpair bluetooth dropdown list"""""
    app_settings_page.Verify_And_click_Unpair_Bluetooth_dropdown_list()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Settings_Text_On_SearchBar()
    aps_notification.click_Settings()
    aps_notification.click_Connected_Devices()
    app_settings_page.click_Unpair_Icon()
    app_settings_page.click_On_Unpair()
    app_settings_page.click_Confirm_Delete_Popup()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    app_settings_page.click_Done_Btn()
    app_settings_page.Verify_Printer_Is_Not_Displaying()
    """stop the app"""
    common_method.Stop_The_App()
    """"10. Check printer is also being deleted in web portal and printer tool Manually"""
# # ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
