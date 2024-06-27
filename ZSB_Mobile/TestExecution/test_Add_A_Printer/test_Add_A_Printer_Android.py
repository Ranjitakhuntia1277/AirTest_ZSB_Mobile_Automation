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


def test_Addprinter_TestcaseID_45657():
    """"Check the cancle button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """Click on Cancel button on the bluetooth pairing popup"""
    add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """Verify Please try the following before attempting to connect to printer again. Text"""""
    add_a_printer_screen.Verify_Please_Try_The_Following_Before_Attempting_Again_Text()
    """"Check there are ""Try again"", ""Watch Troubleshooting Video"" and ""Get Help"" three options on the page----This has to be removed from testcase"""
    """"open your device's Bluetooth settings and unpair your connection to this printer before trying again."""""
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
    """"click on Try Again button"""
    add_a_printer_screen.click_Try_Again()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Connecting to Cloud Text"""
    add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45658_SemiAuto():
    """"Check pairing bluetooth when the printer changes to offline"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """"5. Turn off the target printer from front panel Manually"""""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    """"6. Check the target printer on "Select your printer" page and click Select"""
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """Verify Please try the following before attempting to connect to printer again. Text"""""
    add_a_printer_screen.Verify_Please_Try_The_Following_Before_Attempting_Again_Text()
    """""""Power on the printer Manually"""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """"click on Try Again button"""
    add_a_printer_screen.click_Try_Again()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Connecting to Cloud Text"""
    add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45660_SemiAuto():
    """"Search the essids when the printer is offline"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""Turn OFF The Printer Manually"""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    """"Select Enter Network Manually Option"""
    add_a_printer_screen.click_Enter_Network_Manually()
    """""Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
    add_a_printer_screen.Enter_Network_ESSID()
    add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """""""Power on the printer Manually"""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """"click on Try Again button"""
    add_a_printer_screen.click_Try_Again()
    """"Select Enter Network Manually Option"""
    add_a_printer_screen.click_Enter_Network_Manually()
    """""Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
    add_a_printer_screen.Enter_Network_ESSID()
    add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Connecting to Cloud Text"""
    add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45662_SemiAuto():
    """"set printer open Essid when the printer change to offline, and retry"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""Turn OFF The Printer Manually"""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """""""Power on the printer Manually"""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """"click on Try Again button"""
    add_a_printer_screen.click_Try_Again()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Connecting to Cloud Text"""
    add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_45663_SemiAuto():
    """"set printer wpa psk Essid manually when the printer change to offline, and go to Help"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""Turn OFF The Printer Manually"""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    """"Select Enter Network Manually Option"""
    add_a_printer_screen.click_Enter_Network_Manually()
    """""Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
    add_a_printer_screen.Enter_Network_ESSID()
    add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """""""Power on the printer Manually"""""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """"click on Try Again button"""
    add_a_printer_screen.click_Try_Again()
    """"Select Enter Network Manually Option"""
    add_a_printer_screen.click_Enter_Network_Manually()
    """""Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
    add_a_printer_screen.Enter_Network_ESSID()
    add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Connecting to Cloud Text"""
    add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45665():
    """"Check the left top corner button of each page work during adding a moneybadger."""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"click on the close icon"""
    add_a_printer_screen.click_Close_Icon()
    """"Verify Exit Printer Setup Popup"""
    add_a_printer_screen.Verify_Exit_Printer_Setup_Popup()
    """"Click on Cancel Button"""
    add_a_printer_screen.click_On_Cancel_Button()
    """"Verify It will stay on Setup Your Printer Screen"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"click on the close icon"""
    add_a_printer_screen.click_Close_Icon()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on start button"""
    add_a_printer_screen.click_Start_Button()
    """"Accept the popup"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""click on Close icon on Select Your Printer page"""""
    add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""click on Close icon on Select Your Printer page"""""
    add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"click on the close icon"""
    add_a_printer_screen.click_Close_Icon()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on start button"""
    add_a_printer_screen.click_Start_Button()
    """"Accept the popup"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""click on Close icon on Select Your Printer page"""""
    add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify there is no close icon"""""
    add_a_printer_screen.Verify_Close_Icon_Is_Not_Present()


# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_45670_SemiAuto():
    """"using the phone B to pair the bluetooth Moneybadger, and don't quit the adding printer process wizard, then using the phone A to discover."""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""Prepare two production users without adding any printer and sign in phone A and B" Manually"""
    common_method.Show_popup_To_SignIn_PhoneA_And_B_Without_Printer_Manually()
    """"Connect to phone A"""
    common_method.Show_popup_To_Connect_To_PhoneA_Manually()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""Use phone B, click the hamburger Icon and click on 'Add a Printer', click Start button Manually"""
    common_method.Show_popup_To_Connect_To_PhoneB_Manually()
    """Navigate till the 'Printer Discovery' page Manually"""""
    common_method.Show_popup_To_Navigate_Till_PrinterDiscovery_Page_Manually()
    """""Check the the target printer is not displayed on the "Select your printer" page"""
    common_method.Show_popup_To_Verify_Target_Printer_Is_Not_Displaying_On_Select_Your_PrinterPage_Manually()
    # #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_45678_SemiAuto():
    """"retrieve moneybadger when no online moenybadgers at your area, then open one, retrieve again"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""2. Verify there is no any moneybadger in your area Manually"""
    common_method.Show_popup_To_Verify_There_Is_No_Moneybadger_In_Your_Area_Manually()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""5. Verify There should be no printer found and app will go to "No printers found" page"""
    add_a_printer_screen.Verify_No_Printers_Found_Text()
    """"Verify "Please make sure your printer is on and Bluetooth Text"""
    add_a_printer_screen.Verify_Your_Printer_is_ON_And_Bluetooth_Is_Enabled_Text()
    """"You can hold the reset button on the back of your printer for 5 seconds to reset the printer. Manually"""""
    common_method.Show_popup_To_Reset_The_Printer_Manually()
    """""Power on a moneybadger printer Manually"""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """ Click on "Try Again" button."""""
    add_a_printer_screen.click_Try_Again()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
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


#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_45679_SemiAuto():
    """"set wrong password of the PSK WPA Essid to printer by choosing it, then click 'Cancel'"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""Verify no duplicated Essids, all Essid is unique and only wpa psk and open securiy Essids in it Manually"""""
    common_method.Show_popup_To_Verify_No_Duplicat_Essids_And_Other_Details_Manually()
    """6. choose the Essid which next to the lock icon."""
    add_a_printer_screen.click_The_ESSID_Next_To_Lock_Icon()
    """"Check it would pop up the dialog "Enter Network Passwords"""""
    add_a_printer_screen.Verify_Enter_Network_Passwords_Text_Is_Displaying()
    """"7. enter the incorrect passwod, and click "Submit"""""
    add_a_printer_screen.Enter_Longe_Wrong_Password_In_Field()
    """"Check the page "Wifi Setup" is spinning."""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """Check wait a few seconds, and the dialog 'Fail to Connect' with incorrect passwod message and 'retry', 'help' button"""""""""""
    add_a_printer_screen.Verify_Unable_To_Connect_Printer_To_Wifi_Popup()
    """""8. Click the 'X' button at left upper corner"""
    add_a_printer_screen.click_Close_Icon()
    """click on Exit on Exit Printer setup popup"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """Check it would go to the page 'Continue printer setup' in Connect to WIfi step"""
    """"9. click Next again and choose the Essid again, and input the correct password for it and submit"""
    """10. check the wifi is connected and the printer is finished setup and added to account successfully."""
    '''''''''''''''''''''''''''It is going to home page so could not automated all the above steps'''''
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on start button"""
    add_a_printer_screen.click_Start_Button()
    """"Accept the popup"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
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


#     ######""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45682():
    """"connect printer with PSK WPA Essid manually, then cancel'"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""""5. Check the page labelled  Connect Wi-Fi network pops up showing the wifi-to which device is connected"""""""
    add_a_printer_screen.Verify_Added_Wifi_which_Is_Connected()
    """"Select a different one and Check it would pop upSearching for Wifi Networks page"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """Click "Enter Network manually"""
    add_a_printer_screen.click_Enter_Network_Manually()
    """""Enter an ESSID password"""""
    add_a_printer_screen.Enter_Network_ESSID()
    """"Enter Password"""
    add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
    """"click on cancel button on connect wifi network screen"""
    add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
    """Verify it would still at the "Select your Wifi Network" page"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_47714_SemiAuto():
    """"Add printer BT pair Timeout : check when printer not in pair mode, check pair time"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """"""""""Start the timer on your device after clicking on next button"""""
    common_method.Show_popup_To_Start_The_Timer_On_Your_Device_Manually()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """"Verify Unable to pair your printer"""""
    add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
    """"Stop the Timer Manually"""
    common_method.Show_popup_To_Stop_The_Timer_On_Your_Device_Manually()
    """"Verify Unable to pair your printer"""""
    add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
    """"Check it would take less then 45 seconds to pair printer Manually"""
    common_method.Show_popup_To_Verify_It_Should_Take_less_than_45_Seconds_to_pair_printer_Manually()


#     ######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_47715_SemiAuto():
    """"Add printer BT pair Timeout : check cancel Bluetooth Pairing request, check pair time"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""4. Press target printer 3-5 second to enter pairing mode(blue light) Manually"""
    common_method.Show_popup_To_Make_The_Printer_To_Pairing_Mode_Manually()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """Check it would popup bluetooth pairing mode and click on cancel button"""
    add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
    add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup_If_Present()
    """"""""""Start the timer on your device after clicking on next button"""""
    common_method.Show_popup_To_Start_The_Timer_On_Your_Device_Manually()
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """"Verify Unable to pair your printer"""""
    add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
    """"Stop the Timer Manually"""
    common_method.Show_popup_To_Stop_The_Timer_On_Your_Device_Manually()
    """"Verify Unable to pair your printer"""""
    add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
    """"Check it would take less then 45 seconds to pair printer Manually"""
    common_method.Show_popup_To_Verify_It_Should_Take_less_than_45_Seconds_to_pair_printer_Manually()


#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_48436():
    """"Verify the Cancel button functionality on "Join Network Page" while connceting to already connected / newly connected network"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """5. In The "Join Network" page, click a password that is incompatible from length point of view"""
    add_a_printer_screen.Enter_Wrong_Password_In_Field()
    """"6. The user should be shown message "Password should contain between 8 and 63 characters"""""
    add_a_printer_screen.Verify_Password_Should_Contain_Between_Message()
    """"click on cancel button on connect wifi network screen"""
    add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
    """"8. The user should be navigated back to previous screen"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """5. In The "Join Network" page, click a password that is incompatible from length point of view"""
    add_a_printer_screen.Enter_Wrong_Password_In_Field()
    """"6. The user should be shown message "Password should contain between 8 and 63 characters"""""
    add_a_printer_screen.Verify_Password_Should_Contain_Between_Message()
    """"click on cancel button on connect wifi network screen"""
    add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
    """"8. The user should be navigated back to previous screen"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """stop the app"""
    common_method.Stop_The_App()


# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_48438():
    """"Verify the timeout scenario when user enters the password and does not Continue"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """""Minimize the app for 3o minutes"""
    common_method.Stop_The_App()
    sleep(1800)
    """""6  Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward"""""
    common_method.Start_The_App()
    add_a_printer_screen.Enter_Password_Field()
    """""Minimize the app for 3o minutes"""
    common_method.Stop_The_App()
    sleep(1800)
    """""6  Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward"""""
    common_method.Start_The_App()
    """"click on the Connect button on Join Network"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


#     ############""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_48693():
    """"Verify the Signal Strength UI for WiFi with Average connectivity"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"Verify the signal Strength UI"""
    add_a_printer_screen.Verify_The_Signal_Strength_UI()
    """"4. Verify the signal Strength UI. The same should be shown in full strength in greyed out 
    This has been removed"""


# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_47702_AemiAuto():
    """"Add printer select network: Check search again to refresh current Wi-Fi list multi times will works fine"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """Verify it is displayed the WIFI network which the mobile phone is connected"""
    add_a_printer_screen.Verify_Known_Network()
    """Verify Discovered Network lists"""
    add_a_printer_screen.Verify_Network_Lists()
    """"click on Search Again"""
    add_a_printer_screen.click_Search_Again_Button()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"Verify Known & Discovered networks are still same"""
    add_a_printer_screen.Verify_Known_Network()
    add_a_printer_screen.Verify_Network_Lists()
    """"6. shut done one network Manually"""
    common_method.Show_popup_To_Shut_Down_One_Network_Manually()
    """"click on Search Again"""
    add_a_printer_screen.click_Search_Again_Button()
    """"Verify the shut down network not show in list Manually"""
    common_method.Show_popup_To_Verify_The_Shut_Down_Network_Not_showing_In_The_List_Manually()
    """""8. Open a new network(eg: personal hotspot) Manually"""""
    common_method.Show_popup_To_Open_A_New_Network_Manually()
    """"9. Click search again, check the network refresh success"""
    add_a_printer_screen.click_Search_Again_Button()
    """check the new added network appear in list Manually"""
    common_method.Show_popup_To_Verify_The_New_Added_Network_Manually()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """select A network to connect"""
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
#     #######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def test_Addprinter_TestcaseID_53209_SemiAuto():
    """"[New Fonts and UI checking]Perform the Add printer process and check all the page/toast font and dialogs and buttons displayed correctly"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Verify the Image & UI with Figma Manually"""
    common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """"Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """select A network to connect"""
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"Verify Printer Setup Complete Font & style Manually"""
    common_method.Show_popup_To_Verify_Printer_Setup_Complete_Font_And_Style_Manually()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()
#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_53210_SemiAuto():
    """"[New Fonts and UI checking]Perform the Add printer process and check error message dialog display correct when adding printer,example Firmware update Error, internet access blocked"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Verify the Image & UI with Figma Manually"""
    common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """"Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """5. Select a Wi-Fi without network, click Connect button"""
    """Check Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Select_A_WIFI_Without_Network_And_Chcek_The_Fonts_And_Style_Manually()
    """"6. Check Printer registration page displayed with new fonts and style Manually"""
    common_method.Show_popup_To_Verify_New_Font_And_Style_Of_Registration_Page_Displayed_Manually()
    """7. Check "internet access blocked" error message would be prompted with new fonts and style"""
    add_a_printer_screen.Verify_Internet_Access_Blocked_Popup()
    """""Verify New Fonts & style Manually for Internet Access Blocked Popup Manually"""
    common_method.Show_popup_To_Verify_NewFonts_And_Style_Of_Internet_Access_Popup_Manually()
    """"" Check "Firmware update Error" error message would be prompted with new fonts and style Manually"""
    common_method.Show_popup_To_Verify_Firmware_Update_Error_With_NewFonts_And_Style_Manually()
# ######""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_53211_SemiAuto():
    """"[New Fonts and UI checking]Perform the Add printer process and check paired failed page display correct"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Verify the Image & UI with Figma Manually"""
    common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify The font & Style of Select your Printer page"""
    common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """"Verify Bluetooth pairing your printer page with new fonts and style"""
    common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
    """Click on Cancel button on the bluetooth pairing popup"""
    add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
    """""Verify "Unable to pair your printer"" page pops up"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """""Verify the Unable To Connect to Printer page fonts & Style"""
    common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def test_Addprinter_TestcaseID_53212_SemiAuto():
    """"[New Fonts and UI checking]Perform the Add printer process and check Unable to connect the printer page display correct when adding a printer searching wifi step with turn off device bluetooth"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Verify the Image & UI with Figma Manually"""
    common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify The font & Style of Select your Printer page"""
    common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """"Verify Bluetooth pairing your printer page with new fonts and style"""
    common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """"Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """5. Select a Wi-Fi without network, click Connect button"""
    """Check Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Select_A_WIFI_Without_Network_And_Chcek_The_Fonts_And_Style_Manually()
    """"Disable the Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(4)
    """"click on Allow button on Bluetooth disable & enable popup"""
    add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """Verify Unable to connect to the printer page displayed correct with the new fonts and styles"""
    add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
    """""Verify the Unable To Connect to Printer page fonts & Style"""
    common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_53213_SemiAuto():
    """"[New Fonts and UI checking]Perform the Add printer process and check Failed to connect page dislay correct when adding a printer with input wrong password"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Verify the Image & UI with Figma Manually"""
    common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify The font & Style of Select your Printer page"""
    common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """"Verify Bluetooth pairing your printer page with new fonts and style"""
    common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """"Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
    common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"Select a wifi network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """"6. Input the invalid password and try to connect"""""""""
    add_a_printer_screen.Enter_Longe_Wrong_Password_In_Field()
    """"Check the page "Wifi Setup" is spinning."""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """""""Check fail to connect the printer page prompted with the new fonts and styles"""""""
    add_a_printer_screen.Verify_Unable_To_Connect_Printer_To_Wifi_Popup()
    """""""Check fail to connect the printer page prompted with the new fonts and styles"""""""
    """"Verify the new fonts and styles"""""
    common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
#   #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_53214_SemiAuto():
    """"[New Fonts and UI checking]Check the permission dialog display correct, remove all the permission and turn off device Bluetooth, then click add printer"""

    """""1.Login with a test account"""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2.Turn off the Bluetooth and location permission on the device Manually"""
    """"Disable the Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(4)
    common_method.Show_popup_To_Disable_Location_Permission_On_The_Device_Manually()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """""Check the permission dialog display correctly with the new fonts and styles"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""""2. Turn on Bluetooth permission on the device"""""""
    app_settings_page.Enable_Bluetooth()
    sleep(4)
    """"Check the Location permission dialog display correctly with the new fonts and styles"""
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """3. Turn on location permission but turn off Bluetooth permission on the device Manually"""
    common_method.Show_popup_To_Enable_Location_Permission_On_The_Device_Manually()
    """"Disable the Bluetooth"""
    app_settings_page.Disable_Bluetooth()
    sleep(4)
    """"Check the Bluetooth permission dialog display correctly with the new fonts and styles Manually"""
    common_method.Show_popup_To_Verify_Bluetooth_Permission_Popup_With_New_Design_On_The_Device_Manually()
    ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_53069():
    """"Printer Setup Screen- Check clicking the exit/cancel button on Exit Printer Setup dialog"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"click on the close icon"""
    add_a_printer_screen.click_Close_Icon()
    """"Verify Exit Printer Setup Popup"""
    add_a_printer_screen.Verify_Exit_Printer_Setup_Popup()
    """"Click on Cancel Button"""
    add_a_printer_screen.click_On_Cancel_Button()
    """"Verify It will stay on Setup Your Printer Screen"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """"click on the close icon"""
    add_a_printer_screen.click_Close_Icon()
    """"Click on Exit Button"""
    add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
    """3.Check the slide left page appear on home page(it will navigate to home page)"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#    #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_53072():
    """"[Login-Splash Screen]:'Install the ZSB series app (.apk file) and check the Login Screen UI and Contents"""

    """1. Install the ZSB series app on android and iOS"""
    common_method.tearDown()
    common_method.Clear_App()
    """"2. Launch the app and check it can be opened and displays the login splash screen."""
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"3. Check the contents of the login splash screen."""
    """"-> Zebra logo and name will be displayed on the login screen."""
    add_a_printer_screen.Verify_Zebra_Logo_Is_Present_On_Login_Screen()
    add_a_printer_screen.Verify_Zebra_Text_Is_Present_On_Login_Screen()
    """"-> ZSB Printer Text and ZSB printer image will be located at the centre of the page."""
    add_a_printer_screen.Verify_ZSB_Printer_Image_Is_Present()
    add_a_printer_screen.Verify_ZSB_Printer_Text_Is_Present()
    """-> "Sign in" button will be available below the printer image."""
    login_page.Verify_SignIn_Button_Is_Present()
    """"4. Click on "Sign in" and check that it should navigate the user to login options."""
    login_page.click_loginBtn()
    """""5. Sign in using any one of the signing options and check the user can login successfully without any issues."""
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    """""6. Logout from the mobile app and check the login splash screen is displayed as mentioned in the step 3."""
    common_method.Clear_App()
    login_page.Verify_SignIn_Button_Is_Present()
# #####################""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""