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


def test_Addprinter_TestcaseID_45656():
    """"Adding the moneybadger while the mobile devices bluetooth is disabled"""

    """"1.Open the app and login the account to go to the overview page."""""
    # common_method.tearDown()
    # common_method.Clear_App()
    # common_method.Start_The_App()
    # login_page.click_LoginAllow_Popup()
    # login_page.click_Allow_ZSB_Series_Popup()
    # login_page.click_loginBtn()
    # login_page.click_LoginAllow_Popup()
    # login_page.click_Allow_ZSB_Series_Popup()
    # login_page.click_Loginwith_Google()
    # login_page.Loginwith_Added_Email_Id()
    # """2. Click the menu button at the left corner"""
    # login_page.click_Menu_HamburgerICN()
    # """3.Check the slide left page appear"""""
    # add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"Disable the Bluetooth"""
    add_a_printer_screen.disable_bluetooth()
    sleep(4)
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
    add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
    """"click on Cancel button"""
    add_a_printer_screen.click_On_Cancel_Btn()
    """Check the "Let's set up your printer" page will dismiss, and it will back to the slide left page"""
    add_a_printer_screen.Verify_Slideleft_Page_Is_Present()
    """"click the button 'Add a Printer' button again"""
    add_a_printer_screen.click_Add_A_Printer()
    """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
    """""""""Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message"""""""""""
    add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
    """"Turn on the Bluetooth"""
    add_a_printer_screen.enable_bluetooth()
    sleep(4)
    """""Verify Let's setup your printer page"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"Disable the Bluetooth"""
    add_a_printer_screen.disable_bluetooth()
    sleep(4)
    """"Let's setup your printer" page, click on Start button, close BT dialog again if it pops up"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Click on start setup button"""
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
    """Unable to find printer(s)" page"""
    add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
    """"click search again button"""
    add_a_printer_screen.click_Search_Again_Button()
    """""Verify Searching Your printer text"""
    add_a_printer_screen.Verify_Searching_Your_Printer_Text()
    """"Verify Select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""Select the Target Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Select button"""
    add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
    """""Check the printer can be paired successfully"""




