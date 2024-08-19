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
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
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
registration_page = Registration_Screen(poco)

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""





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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
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
    """"Stop the App"""
    common_method.Stop_The_App()
# #####################""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Registration_TestcaseID_46303():
    """""""""To test the ZSB Wi-Fi performance Setup"""""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()

    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.Click_Next_Button()
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 30)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """Store the time till wi-fi turn green."""
    time_taken = registration_page.timeTillWiFiGreen()
    print(time_taken)
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()


"""Add printer"""
def test_Registration_TestcaseID_46307():
    """""""""To verify that user is able to continue with the printer after login with the different register login"""""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.Verify_ALL_Allow_Popups()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.Verify_ALL_Allow_Popups()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.Click_Next_Button()
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """wait till wi-fi turn green."""
    registration_page.timeTillWiFiGreen()
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()
# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

