from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen


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


def test_AppSettings_TestcaseID_47913():
 """""""""""""""Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""""""

# try:

# """start the app"""
# common_method.tearDown()
# #test_robo_finger()
# sleep(6)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on Add printer tab"""""
# add_a_printer_screen.click_Add_A_Printer()
# """"click on the start button"""
# add_a_printer_screen.click_Start_Button()
# login_page.click_Allow_ZSB_Series_Popup()
# add_a_printer_screen.Verify_Lets_Make_Sure_Text()
# add_a_printer_screen.Click_Next_Button()
# """"Verify searching for your printer text"""
# add_a_printer_screen.Verify_Searching_for_your_printer_Text()
# """"verify select your printer text"""
# add_a_printer_screen.Verify_Select_your_printer_Text()
# """"select 2nd printer which you want to add"""
# add_a_printer_screen.click_2nd_Printer_Details_To_Add()
# """""click on select button"""
# add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
# """"verify pairing your printer text"""
# add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# """"verify pairing your printer text"""
# add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# """Verify Connect Wi-fi Network Text"""
# add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
# """"click on connect button on connect wifi network screen"""
# add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
# add_a_printer_screen.click_Password_Field_On_Join_Network()
# add_a_printer_screen.click_Submit_Button_ON_Join_Network()
# """"verify need the printer driver text"""
# add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
# """""verify registering your printer text"""
# add_a_printer_screen.Verify_Registering_your_Printer_Text()
# """"Turn OFF the WIFI & Turn on again after some time (approx. 2 min)"""
# aps_notification.disable_wifi()
# aps_notification.enable_wifi()
# sleep(7)
# """"click on finish setup button"""
# add_a_printer_screen.click_Finish_Setup_Button()
# # common_method.savePassResult(errors, "47913")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47924():
     """Verify Should not allow same printer name in all the clients.."""
#
# """"Account should be having 2 printers"""
#
# # # try:
# """start the app"""
# common_method.tearDown()
# test_robo_finger()
# sleep(6)
# """"verify home text is displaying on the home screen"""
# app_settings_page.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on Add printer tab"""""
# add_a_printer_screen.click_Add_A_Printer()
# """"click on the start button"""
# add_a_printer_screen.click_Start_Button()
# login_page.click_Allow_ZSB_Series_Popup()
# add_a_printer_screen.Verify_Lets_Make_Sure_Text()
# add_a_printer_screen.Click_Next_Button()
# """"Verify searching for your printer text"""
# add_a_printer_screen.Verify_Searching_for_your_printer_Text()
# """"verify select your printer text"""
# add_a_printer_screen.Verify_Select_your_printer_Text()
# """"select 2nd printer which you want to add"""
# add_a_printer_screen.click_2nd_Printer_Details_To_Add()
# """""click on select button"""
# add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
# """"verify pairing your printer text"""
# add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# """"verify pairing your printer text"""
# add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# """Verify Connect Wi-fi Network Text"""
# add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
# """"click on connect button on connect wifi network screen"""
# add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
# add_a_printer_screen.click_Password_Field_On_Join_Network()
# add_a_printer_screen.click_Submit_Button_ON_Join_Network()
# """"verify need the printer driver text"""
# add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
# """""verify registering your printer text"""
# add_a_printer_screen.Verify_Registering_your_Printer_Text()
# """"click on finish setup button"""
# add_a_printer_screen.click_Finish_Setup_Button()
# """click on hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# """click on printer settings tab"""
# app_settings_page.click_Printer_Settings()
# """"scroll till the 3rd printer"""
# app_settings_page.Scroll_Till_Notification_Settings_Tab()
# """click on printer name on the printer settings page"""""
# app_settings_page.click_PrinterName2_On_Printersettings()
# """click on printr name"""
# app_settings_page.click_Printer_Name_Text_Field()
# """click on printer name text field"""
# app_settings_page.clear_First_Name()
# """Rename the Printer Name with a long text (more than 30 characters)"""
# app_settings_page.Rename_PrinterName_With_Same_Name()
# """"click on back icon"""
# app_settings_page.click_Back_Icon()
# """verify printer name update failed message"""
# app_settings_page.Verify_Printer_Name_Update_Failed_Message()
# """click continue button"""""
# app_settings_page.click_Continue_Button_On_Printer_Update_Failed_Popup()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Printer_Settings()
# """"verify previous printer name is displaying"""
# app_settings_page.click_PrinterName2_On_Printersettings()
# # # common_method.savePassResult(errors, "47924")
# # # except Exception as e:
# # # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_49709():
    """Manage network- Check able to manage network with long name"""

#
# """"printer should be online & wifi should be connected"""
#
#
# # try:
# """start the app"""
# common_method.tearDown()
# """click on hamburger menu icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on printer settings"""
# app_settings_page.click_Printer_Settings()
# """"click on printer name on  printer settings"""
# app_settings_page.click_PrinterName_On_Printersettings()
# """click on wifi tab"""
# app_settings_page.click_wifi_tab()
# app_settings_page.click_Manage_Networks_Btn()
# """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
# app_settings_page.accept_Continue_popup()
# login_page.click_Allow_ZSB_Series_Popup()
# """"""""""verify the continue button and click on that"""""
# app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
# sleep(5)
# """"""""""Verify the Add Network text & button & click on that"""""""""""
# app_settings_page.click_Add_Network()
# sleep(3)
# """""""""""""Verify Add network page is opening and verify the text"""""""
# app_settings_page.get_text_Add_Network()
# app_settings_page.click_Enter_Network_Manually()
# app_settings_page.click_Long_Network_UserName()
# app_settings_page.click_Join_Btn_On_Other_Network_Popup()
# app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
# app_settings_page.Verify_Long_Network_UserName()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Printer_Settings()
# """"click on the red icon to delete the added network name"""
# app_settings_page.click_Red_Icon_to_remove_network()
# # common_method.savePassResult(errors, "49709")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_49711():
    """Manage networks- Check there is a prompt message when applying to the network which can't resolve Zebra host"""


# # try:
# """start the app"""
# common_method.tearDown()
# """click on hamburger menu icon"""
# login_page.click_Menu_HamburgerICN()
# """"click on printer settings"""
# app_settings_page.click_Printer_Settings()
# """"click on printer name on  printer settings"""
# app_settings_page.click_PrinterName_On_Printersettings()
# """click on wifi tab"""
# app_settings_page.click_wifi_tab()
# app_settings_page.click_Manage_Networks_Btn()
# """"verify bluetooth connection required text"""
# app_settings_page.get_text_Bluetooth_connection_required_Txt()
# app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
# app_settings_page.click_Allow_Btn()
# app_settings_page.click_Add_Network()
# app_settings_page.click_Enter_Network_Manually()
# app_settings_page.click_Long_Network_UserName()
# app_settings_page.click_Join_Btn_On_Other_Network_Popup()
# app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
# app_settings_page.Verify_Long_Network_UserName()
# app_settings_page.click_Apply_Chnages_Button()
# """""Currently there is no error message displaying so Couldnot automate, it is blocked due to SMBM-2163"""""""""""
# app_settings_page.Verify_The_Invalid_Network_Error_Message()
# # common_method.savePassResult(errors, "49711")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50326():
    """Manage Network- Check able to add/delete/sort network when printer bt paired/unpaired in device""""""

""""App should be in logged in condition & printer should be added """"
""""""connect with Another wifi Network except NESTWIFI"""


#
# # try:
# """"start the app"""
# common_method.tearDown()
# """"click on the hamburger icon"""
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# app_settings_page.click_wifi_tab()
# app_settings_page.click_Manage_Networks_Btn()
# app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
# app_settings_page.click_Add_Network()
# app_settings_page.click_ZEBRA_Network()
# app_settings_page.click_Network_Password_Field()
# app_settings_page.click_Network_Submit_Btn()
# app_settings_page.Verify_NestWIFI_Network_Name_In_Network_List()
# app_settings_page.click_Red_Icon_to_remove_network()
# app_settings_page.Verify_NestWIFI_In_Network_List()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Home_Tab()
# app_settings_page.Verify_Printer_is_already_added()
# # common_method.savePassResult(errors, "50326")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50325():
    """Manage Network-Check able to add/delete/sort network when printer bt paired/unpaired in device"""


""""App should be in logged in condition & printer should be added """


# # try:
# """"start the app"""
# common_method.tearDown()
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# app_settings_page.click_wifi_tab()
# app_settings_page.click_Manage_Networks_Btn()
# app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
# app_settings_page.click_Add_Network()
# app_settings_page.click_Enter_Network_Manually()
# app_settings_page.click_Network_UserName()
# app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
# app_settings_page.click_Enter_Network_Manually()
# app_settings_page.click_Network_UserName()
# app_settings_page.click_Security_Open()
# app_settings_page.click_WPA_PSK()
# app_settings_page.click_Keyboard_back_Icon()
# app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
# app_settings_page.click_Enter_Network_Manually()
# app_settings_page.click_Network_UserName()
# app_settings_page.click_Join_Btn_On_Other_Network_Popup()
# app_settings_page.Verify_Added_Network()
# # common_method.savePassResult(errors, "50325")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47910():
    """""Verify pull-down screen twice then the prints left value can refresh success in home page."""""

# # try:
# #     """start the app"""
# common_method.tearDown()
# sleep(3)
# # add_a_printer_screen.click_Add_A_Printer()
# app_settings_page.Verify_Printer_is_already_added()
# """take the prvious number of cartridges"""
# previous = app_settings_page.Check_no_of_left_cartridge()
# print(previous)
#
# """click on navigation option"""
# login_page.click_Menu_HamburgerICN()
#
# """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
# app_settings_page.click_Printer_Settings()
# app_settings_page.click_PrinterName_On_Printersettings()
# sleep(2)
# n=2
#
# """test the printer to print the label"""
# for i in range(n):
#     app_settings_page.click_Test_Print_Button()
#     sleep(2)
#
# sleep(1)
# """Go to the Home Page"""
# login_page.click_Menu_HamburgerICN()
# app_settings_page.click_Home_Tab()
# sleep(2)
#
# """After printing Get the number of cartridges"""
# after = app_settings_page.Check_no_of_left_cartridge()
# print(after)
#
# """Check wheather the cartridges are updated or not"""
# res = app_settings_page.check_update_cartridge(previous,after,n)
# if res:
#     print("success")
# else:
#     print("Failed")
# # common_method.savePassResult(errors, "47910")
# # except Exception as e:
# # common_method.saveError(errors, e)
# """stop the app"""
# common_method.Stop_The_App()


### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

