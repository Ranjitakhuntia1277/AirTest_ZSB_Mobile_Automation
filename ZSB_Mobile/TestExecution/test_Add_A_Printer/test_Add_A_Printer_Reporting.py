from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
import pytest
from airtest.core.api import connect_device

from ...PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
from ...TestSuite.api_call import insert_step, insert_case_results
from ...TestSuite.api_call import *


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Add_A_Printer_Android:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
pdf_printing_android = PDF_Printing_Screen(poco)

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
execID = 0
leftId = {"0": "7"}


def test_Addprinter_TestcaseID_45656():
    """"Adding the moneybadger while the mobile devices bluetooth is disabled"""

    """"1.Open the app and login the account to go to the overview page."""""
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
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"Disable the Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(4)
    """"click on Allow button on Bluetooth disable & enable popup"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """"can not verify all these steps as these all are coming behind the popup"""
    ### """Check it would go to the page "Let's set up your printer"""
    ### add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    #### """""Check the moneybadger picture would appears at that page."""
    #### add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    #### """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
    add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
    """"click on Cancel button"""
    add_a_printer_screen.click_On_Cancel_Btn()
    """Check the "Let's set up your printer" page will dismiss, and it will back to the slide left page"""
    add_a_printer_screen.Verify_Slideleft_Page_Is_Present()
    """"click the button 'Add a Printer' button again"""
    add_a_printer_screen.click_Add_A_Printer()
    """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
    add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
    """"click on Cancel button"""
    add_a_printer_screen.click_On_Cancel_Btn()
    """"Turn on the Bluetooth"""
    app_settings_page.Enable_Bluetooth()
    sleep(4)
    """"click on Allow button on Bluetooth disable & enable popup"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """"click the button 'Add a Printer' button again"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"Disable the Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(4)
    """"click on Allow button on Bluetooth disable & enable popup"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """click start button"""
    add_a_printer_screen.click_Start_Button()
    """"Accept the popup"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""click on next button"""
    add_a_printer_screen.Click_Next_Button()
    """Unable to find printer(s)" page"""
    add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
    """"Turn on the Bluetooth"""
    add_a_printer_screen.enable_bluetooth()
    sleep(4)
    """click on allow for enable bluetooth"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """Unable to find printer(s)" page"""
    add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
    """"click search again button"""
    add_a_printer_screen.click_Search_Again_Button()
    """""Verify Searching Your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text_For_Add_Printer()
    """""Select the Target Printer"""
    add_a_printer_screen.Select_Printer()
    """"Select button"""
    add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(15)
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """"Turn off Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(5)
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """Verify Unable to connect to printer popup is displaying"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """"Turn on Bluetooth"""
    app_settings_page.Enable_Bluetooth()
    sleep(5)
    """click on Allow button"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """"click on try again"""
    add_a_printer_screen.click_Try_Again()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()
    """""""""done"""""""""""""""""""""""""""


# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
