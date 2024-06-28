from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Login_Screen import *

from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen import Login_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Others.Others import Others
import pytest


class Android_App_Printer_Management:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

common_method = Common_Method(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
registration_page = Registration_Screen(poco)
others = Others(poco)


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

def test_Others_TestcaseID_47955():
    pass
    common_method.tearDown()
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    names, id = others.get_printer_names()
    print(names, id)
    others.select_printer_1(id[1])
    others.rename_printer(id[1], names[2])
    sleep(1)
    keyevent("enter")
    res = others.verify_text_update_printer_name_fail()
    print(res)
    if not res:
        raise Exception("printer update failed not raised")


def test_Others_TestcaseID_47946():
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Home")
    except:
        pass
    """take the previous number of cartridges"""
    previous = others.get_no_of_left_cartridge()

    """click on navigation option"""
    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    others.click_Printer_Settings()
    others.select_first_printer()
    sleep(2)
    n = 2

    """test the printer to print the label"""
    for i in range(n):
        others.click_test_print()
        others.wait_for_appearance_all("Print complete")
        sleep(2)
    sleep(5)
    """Go to the Home Page"""
    login_page.click_Menu_HamburgerICN()
    others.click_home_button()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = others.get_no_of_left_cartridge()

    """Check wheather the cartridges are updated"""
    res = others.check_auto_update_cartridge(previous, after, n)
    if not res:
        raise Exception("number of cartridge count not updated")

def test_Others_TestcaseID_47945(self):
    pass

    """Has bug id: SMBM-2247"""
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Home")
    except:
        pass
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()

    names, id = others.get_printer_names()
    others.select_printer_1(id[1])

    others.rename_printer(id[1],"")
    others.click_enter()

    res = others.get_null_name_error_and_space_for_printer_name()
    if res:
        print("ok")
    else:
        raise Exception("proper error msg not displayed for null value")

    others.rename_printer(id[1],"    ")
    others.click_enter()

    if res:
        print("ok")
    else:
        raise Exception("Space  accepted")
def test_Others_TestcaseID_49203():
    pass

    common_method.tearDown()
    try:
        common_method.wait_for_element_appearance_namematches("Home")
    except:
        pass
    """Click On the Three dots of the Home page Printer"""
    others.click_three_dots()

    """Click on the Delete Button"""
    others.click_delete_button()

    """Verify the text image (Currently The text cannot be extracted so verifying using the name)"""
    try:
        others.verify_delete_printer_text()
    except:
        raise Exception("step 2-2 fails, which does not match the wordings")

    """Check cancel and delete button exists"""
    others.check_cancel_and_delete_button()

    """cancel the delete printer dialogue"""
    others.click_cancel_delete_printer()


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
