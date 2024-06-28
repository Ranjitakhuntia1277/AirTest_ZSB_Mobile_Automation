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


def test_Others_TestcaseID_45803(self):
    pass

    common_method.tearDown()

    common_method.wait_for_element_appearance_namematches("Open navigation menu")

    """Has bugs SMBM 1801 ,and 997"""
    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is in offline or other state turn it on")

    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    others.click_Printer_Settings()

    """pass the printer name"""
    others.select_first_printer()
    sleep(2)

    others.click_test_print()
    login_page.click_Menu_HamburgerICN()

    common_method.show_message("Remove the cartridge and close the printer")

    others.click_home_button()
    sleep(2)
    res = others.check_printer_online_status()

    if res == "Paper out":
        print("ok")
    else:
        raise Exception("Paper out should be shown but not shown")

    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    others.click_Printer_Settings()

    """pass the printer name"""
    others.select_first_printer()
    sleep(2)

    others.click_test_print()

    common_method.show_message("Insert the cartridge back and close the printer")
    sleep(30)

    login_page.click_Menu_HamburgerICN()

    others.click_home_button()

    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is in offline state turn it on")

def test_Others_TestcaseID_45804(self):
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")

    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    """Has bugs SMBM 1801 ,and 997"""
    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is not in Online state")

    others.select_first_label_from_home()
    others.click_print_button()
    sleep(3)
    others.check_error_print_preview()

    others.click_print_button()
    sleep(4)

    others.click_left_arrow()

    common_method.show_message("Long press the printer power button to turn off the printer.")

    res = others.check_printer_online_status()
    if res == "Offline":
        print("ok")
    else:
        raise Exception("Printer is not in Offline state")

    others.select_first_label_from_home()
    others.click_print_button()
    sleep(3)
    others.check_error_print_preview()

    others.click_print_button()
    sleep(4)

    common_method.wait_for_element_appearance_namematches("Printer currently offline",30)

    others.click_left_arrow()

    common_method.show_message("Turn on Printer ")
    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is not in Online state")


def test_Others_TestcaseID_45805(self):
    pass
    """Has bugs SMBM 1801 ,and 997"""
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")

    common_method.wait_for_element_appearance_namematches("Open navigation menu")

    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is not in Online state")

    others.select_first_label_from_home()
    others.click_print_button()
    sleep(3)
    others.check_error_print_preview()

    others.click_print_button()
    sleep(4)
    others.click_left_arrow()

    common_method.show_message("Open the Printer Cover")
    res = others.check_printer_online_status()
    if res == "Cover Open":
        print("ok")
    else:
        raise Exception("Printer is not in Cover Open state")


    others.select_first_label_from_home()
    others.click_print_button()
    sleep(3)
    others.check_error_print_preview()

    others.click_print_button()
    sleep(4)

    common_method.wait_for_element_appearance_namematches('Printer has cover open',30)

    others.click_left_arrow()

    common_method.show_message("Close the Printer Cover")

    res = others.check_printer_online_status()
    if res == "Online":
        print("ok")
    else:
        raise Exception("Printer is not in Online state")



