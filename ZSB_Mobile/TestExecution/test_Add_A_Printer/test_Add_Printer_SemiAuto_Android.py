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


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)


# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


####Archived
# # ###Steps are not correct
# def test_Addprinter_TestcaseID_47714_SemiAuto():
#     """"Add printer BT pair Timeout : check when printer not in pair mode, check pair time"""
#
#     """"1.Open the app and login the account to go to the overview page."""""
#     common_method.tearDown()
#     common_method.Start_The_App()
#     login_page.click_LoginAllow_Popup()
#     login_page.click_Allow_ZSB_Series_Popup()
#     """2. Click the menu button at the left corner"""
#     login_page.click_Menu_HamburgerICN()
#     """3.Check the slide left page appear"""""
#     add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#     """"3. click the button 'Add a Printer'"""
#     add_a_printer_screen.click_Add_A_Printer()
#     """Check it would go to the page "Let's set up your printer"""
#     add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#     """""Check the moneybadger picture would appears at that page."""
#     add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#     """Click on Start setup button"""
#     add_a_printer_screen.click_Start_Button()
#     """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#     add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#     """""click on Next Button"""""
#     add_a_printer_screen.click_Next_Button()
#     """"Verify Searching For your Printer Text"""
#     add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#     """"Verify Select your Printer Text"""
#     add_a_printer_screen.Verify_Select_your_printer_Text()
#     """Select the Printer"""
#     add_a_printer_screen.Click_The_Printer_Name_To_Select()
#     """"Click on Next Button"""
#     add_a_printer_screen.click_Next_Button()
#     """"""""""Start the timer on your device after clicking on next button"""""
#     common_method.Show_popup_To_Start_The_Timer_On_Your_Device_Manually()
#     """""Check the printer can be paired successfully"""
#     add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#     add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#     add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#     add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#     sleep(5)
#     """""Verify Connecting to printer Text"""
#     add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#     """"Verify Unable to pair your printer"""""
#     add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#     """"Stop the Timer Manually"""
#     common_method.Show_popup_To_Stop_The_Timer_On_Your_Device_Manually()
#     """"Verify Unable to pair your printer"""""
#     add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#     """"Check it would take less then 45 seconds to pair printer Manually"""
#     common_method.Show_popup_To_Verify_It_Should_Take_less_than_45_Seconds_to_pair_printer_Manually()
#     """"Stop the App"""
#     common_method.Stop_The_App()
#
# #     ######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ###Archived
"""Add printer"""
# def test_Registration_TestcaseID_46307():
#     """""""""To verify that user is able to continue with the printer after login with the different register login"""""
#
#     """"1.Open the app and login the account to go to the overview page."""""
#     common_method.tearDown()
#     common_method.Start_The_App()
#     login_page.Verify_ALL_Allow_Popups()
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_screen.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_screen.click_Start_Button()
#     login_page.Verify_ALL_Allow_Popups()
#     add_a_printer_screen.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_screen.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_screen.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_screen.Click_Next_Button()
#     add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
#     common_method.wait_for_element_appearance("Discovered networks", 30)
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """wait till wi-fi turn green."""
#     registration_page.timeTillWiFiGreen()
#     """"click on finish setup button"""
#     common_method.wait_for_element_appearance("Printer registration was successful", 30)
#     add_a_printer_screen.click_Finish_Setup_Button()
#     common_method.Stop_The_App()
# # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# ###Moved to registration
# def test_Addprinter_TestcaseID_53072():
#     """"[Login-Splash Screen]:'Install the ZSB series app (.apk file) and check the Login Screen UI and Contents"""
#
#     """1. Install the ZSB series app on android and iOS"""
#     common_method.tearDown()
#     common_method.Clear_App()
#     """"2. Launch the app and check it can be opened and displays the login splash screen."""
#     common_method.Start_The_App()
#     login_page.click_LoginAllow_Popup()
#     login_page.click_Allow_ZSB_Series_Popup()
#     """"3. Check the contents of the login splash screen."""
#     """"-> Zebra logo and name will be displayed on the login screen."""
#     add_a_printer_screen.Verify_Zebra_Logo_Is_Present_On_Login_Screen()
#     add_a_printer_screen.Verify_Zebra_Text_Is_Present_On_Login_Screen()
#     """"-> ZSB Printer Text and ZSB printer image will be located at the centre of the page."""
#     add_a_printer_screen.Verify_ZSB_Printer_Image_Is_Present()
#     add_a_printer_screen.Verify_ZSB_Printer_Text_Is_Present()
#     """-> "Sign in" button will be available below the printer image."""
#     login_page.Verify_SignIn_Button_Is_Present()
#     """"4. Click on "Sign in" and check that it should navigate the user to login options."""
#     login_page.click_loginBtn()
#     """""5. Sign in using any one of the signing options and check the user can login successfully without any issues."""
#     login_page.click_Loginwith_Google()
#     login_page.Loginwith_Added_Email_Id()
#     """""6. Logout from the mobile app and check the login splash screen is displayed as mentioned in the step 3."""
#     common_method.Clear_App()
#     login_page.Verify_SignIn_Button_Is_Present()
#     """"Stop the App"""
#     common_method.Stop_The_App()
# #####################""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
