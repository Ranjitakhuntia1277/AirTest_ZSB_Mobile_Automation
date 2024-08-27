from airtest.core.api import auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
import time
# from self import self

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device


# Specify the device's platform (Android or iOS) and other details

class Add_A_PrinterScreen:
    pass


uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)
auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")

login_screen_ios = Login_Screen_iOS(poco)
app_settings_iOS_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)


# def test_Addprinter_TestcaseID_45658():
#     """SEMI-AUTOMATED"""
#     """Check pairing bluetooth when the printer changes to offline"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """Step 3"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 4"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     """Step 5"""
#     common_method.show_message("Please Turn off the Printer")
#     """Step 6"""
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 7"""
#     common_method.show_message("Please Turn on the Printer and make it enter into the pairing mode")
#     add_a_printer_page_ios.click_try_again()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 8"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()


# def test_Addprinter_TestcaseID_45660():
#     """SEMI-AUTOMATED"""
#     """ Check searching the ess-ids works when the printer is offline"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 3"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 4"""
#     add_a_printer_page_ios.check_select_wifi()
#     common_method.show_message("Please Turn off the Printer")
#     """Step 5"""
#     add_a_printer_page_ios.enter_network_manually("connect")
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 6"""
#     common_method.show_message("Please Turn on the Printer")
#     add_a_printer_page_ios.click_try_again()
#     """Step 7"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()


# def test_Addprinter_TestcaseID_45662():
#     """SMI-AUTOMATED"""
#     """set printer open Ess-id when the printer change to offline, and retry"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_select_wifi()
#     common_method.show_message("Please Turn off the Printer")
#     add_a_printer_page_ios.choose_open_wifi_network()
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 4"""
#     add_a_printer_page_ios.click_try_again()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 5"""
#     common_method.show_message("Please Turn on the Printer")
#     add_a_printer_page_ios.choose_open_wifi_network()
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45666():
#     """SEMI-AUTOMATED"""
#     """CURRENTLY WE ARE NOT AUTOMATING 2 DEVICES TESTCASES"""
#     """Check using phone B to add the unconfigured printer which was paired the bluetooth connection by phone A and not in bluetooth limited mode"""
#     """Precondition Phone A"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()
#     """Precondition on Phone B"""
#     common_method.show_message("Please login wih a stage user on Phone B")
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     common_method.show_message("Use phone B to slide the left slide page to click the button 'Add a Printer"
#                                "do the same steps till select printer page and select the same printer as Phone A, "
#                                "check it must show connection failed'""")


# def test_Addprinter_TestcaseID_45668():
#     """SEMI-AUTOMATED"""
#     """CURRENTLY WE ARE NOT AUTOMATING 2 DEVICES TESTCASES"""
#     """Check using phone B to add the unconfigured printer which was paired the bluetooth connection by phone A and in bluetooth limited mode"""
#     """Precondition Phone A"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()
#     """Precondition on Phone B"""
#     common_method.show_message("Please login wih a stage user on Phone B")
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     """Step 5"""
#     common_method.show_message("Make the printer go into pairing mode")
#     """Step 6"""
#     common_method.show_message(
#         "Use phone B to slide the left slide page to click the button 'Add a Printer', then click Start button")
#     """Step 7"""
#     common_method.show_message(
#         "Check the snipping 'Searching for Wifi network' page shows up, then the 'Select your Wi-Fi network' page pops up")
#     """Step 8"""
#     common_method.show_message(
#         "Select an essid and input correct pw, then click submit button Check the 'Connecting to Wi-Fi network' will be snipping, then the 'Wifi connected' page pops up")
#     """Step 9"""
#     common_method.show_message(
#         "Check it would go to 'Need the Printer Driver?' page automatically Check the notification 'register', 'Printer online' appears.")


# def test_Addprinter_TestcaseID_45669():
#     """SEMI-AUTOMATED"""
#     """Check using phone A to add the unconfigured printer which was paired the bluetooth connection by phone A and in bluetooth limited mode"""
#     """Precondition Phone A"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     """Step 5"""
#     common_method.show_message("Make the printer go into pairing mode")
#     """Step 6"""
#     # login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     """Step 7"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     # add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 8"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     """Step 9"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45670():
#     """SEMI-AUTOMATED"""
#     """CURRENTLY WE ARE NOT AUTOMATING 2 DEVICES TESTCASES"""
#     """Check using the phone B to pair the bluetooth Moneybadger, and don't quit the adding printer process wizard, then using the phone A to discover"""
#     """Precondition Phone A"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()
#     """Precondition on Phone B"""
#     common_method.show_message("Please login wih a stage user on Phone B")
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     common_method.show_message(
#         "Use phone B to slide the left slide page to click the button 'Add a Printer', click Start button Check the 'Printer Discovery' page is spinning Check the the target printer is not displayed on the 'Select your printer' page")


# def test_Addprinter_TestcaseID_45671():
#     """SEMI-AUTOMATED"""
#     """CURRENTLY WE ARE NOT AUTOMATING 2 DEVICES TESTCASES"""
#     """Check using phone B to pair the bluetooth Moneybadger, and don't quit the adding printer process wizard, and make it into bluetooth limited mode, then using phone A to discover"""
#     """Precondition Phone A"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()
#     """Precondition on Phone B"""
#     common_method.show_message("Please login wih a stage user on Phone B")
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     common_method.show_message("Make the printer go into pairing mode")
#     """Step 5"""
#     common_method.show_message(
#         "Use phone B to slide the left slide page to click the button 'Add a Printer', then click Start Check the 'Printer Discovery' page is spinning Check the the target printer is not displayed on the 'Select your printer' page")


# def test_Addprinter_TestcaseID_45675():
#     """SEMI-AUTOMATED"""
#     """To check printer can be connected when it's status is media out"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     common_method.show_message("Make sure the moneybadger's status is media out")
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 3"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     """Step 10"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45676():
#     """SEMI-AUTOMATED"""
#     """To check printer can be connected when it's status is head open"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     common_method.show_message("Make sure the moneybadger's status is head open")
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 3"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     """Step 7"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     """Step 8"""
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45678():
#     """SEMI-AUTOMATED"""
#     """To check Bluetooth search page works when no any moneybadger in your area"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     common_method.show_message("Make sure their is no moneybadger turned on in your area")
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """Step 3"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 4"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     """Step 5"""
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 6"""
#     common_method.show_message("Turn on the Money Badger")
#     add_a_printer_page_ios.click_try_again()
#     """Step 7"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     """Step 8"""
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 9"""
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 10"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45683():
#     """SEMI-AUTOMATED"""
#     """To check ZSB can add multiple printers(>2) to the portal with same network"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     common_method.show_message("Check there is only 1 essid in your room")
#     common_method.show_message("Make sure there are 6 moneybadgers in your room")
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     for i in range(5):
#         login_screen_ios.click_Menu_HamburgerICN()
#         add_a_printer_page_ios.click_Add_A_Printer()
#         add_a_printer_page_ios.click_start_button()
#         add_a_printer_page_ios.check_connect_to_printer()
#         add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#         add_a_printer_page_ios.click_next_button()
#         add_a_printer_page_ios.click_pair_button()
#         add_a_printer_page_ios.check_select_wifi()
#         add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#         add_a_printer_page_ios.check_wifi_connected_successfully()
#         add_a_printer_page_ios.finish_setup()
#         login_screen_ios.check_finish_setup()
#         add_a_printer_page_ios.check_printer_online()
#     CHECK FOR 6 MONEY BADGERS


# def test_Addprinter_TestcaseID_45684():
#     """SEMI-AUTOMATED"""
#     """To check ZSB can connect more than 1 printer to the portal with different network"""
#     """Precondition"""
#     if login_screen_ios.check_finish_setup():
#         pass
#     else:
#         login_screen_ios.click_Menu_HamburgerICN()
#         add_a_printer_page_ios.click_Add_A_Printer()
#         add_a_printer_page_ios.click_start_button()
#         add_a_printer_page_ios.check_connect_to_printer()
#         add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#         add_a_printer_page_ios.click_next_button()
#         add_a_printer_page_ios.click_pair_button()
#         add_a_printer_page_ios.check_select_wifi()
#         add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#         add_a_printer_page_ios.check_wifi_connected_successfully()
#         add_a_printer_page_ios.finish_setup()
#         login_screen_ios.check_finish_setup()
#     common_method.show_message("Make sure there are more than 1 ess-id in your room")
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45685():
#     """SEMI-AUTOMATED"""
#     """To check the printer can be re-added after decommissioning by another account"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     common_method.show_message("Make sure there are more than one account in the phone")
#     login_screen_ios.login()  # Account A
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     """Step 2"""
#     common_method.show_message("Perform decommission on the printer")
#     add_a_printer_page_ios.check_printer_offline()
#     """Step 3"""
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()  # Account B
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()  # Account A
#     login_screen_ios.check_finish_setup()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()  # Account B
#     """Step 4"""
#     common_method.show_message("Perform decommission on the printer")
#     add_a_printer_page_ios.check_printer_offline()
#     """Step 5"""
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()  # Account A
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     login_screen_ios.login()  # Account B
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45686():
#     """SEMI-AUTOMATED"""
#     """To check the printer can be re-added after decommissioning"""
#     """Pre-condition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     """Step 1"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     add_a_printer_page_ios.check_printer_online()
#     """Step 2"""
#     common_method.show_message("Perform decommission on the printer")
#     add_a_printer_page_ios.check_printer_offline()
#     """Step 3"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("NESTWIFI")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     """Step 4"""
#     add_a_printer_page_ios.finish_setup()
#     add_a_printer_page_ios.check_printer_online()
#     """Step 5"""
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_46304():
#     """CANNOT BE AUTOMATED as we connot move the printer, not the device in automation"""
#     """To verify the ZSB Bluetooth intro probability test"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.login()
#     """Step 3"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     """Step 4"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     common_method.show_message("Move 10m apart and then come back and see weather the pairing process is resumed")


# def test_Addprinter_TestcaseID_46305():
#     """SEMI_AUTOMATED"""
#     """To verify the ZSB Bluetooth intro probability test will get an error when far away from printer"""
#     """Pre-condition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.login()
#     """Step 3"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     """Step 5"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     common_method.show_message("While BT pairing is going on, go out of range and stay there")
#     common_method.show_message("BT process should interrupt and error message should display")
def test_add_printer_test_case_id_53087():
    """Verify the "Unable to find Printer(s)" screen is displayed, if the printers are not discovered during the Bluetooth search."""
    """Pre-Condition"""
    add_a_printer_page_ios.delete_printer()
    add_a_printer_page_ios.unpair_printer()
    common_method.show_message("Make sure there is no printer turned on nearby")
    """Step 1"""
    login_screen_ios.login("Google")
    add_a_printer_page_ios.click_Add_A_Printer()
    add_a_printer_page_ios.click_start_setup()
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.check_unable_to_connect_printer()
    # GO home and write


