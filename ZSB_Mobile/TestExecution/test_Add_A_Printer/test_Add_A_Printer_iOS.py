from airtest.core.api import auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
import time

from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ...PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from ...PageObject.Robofinger import test_robo_finger
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


def register_printer():
    sleep(10)
    e_check = poco(nameMatches="(?s).*ZSB-DP12.*")
    if e_check.exists():
        return
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    add_a_printer_page_ios.click_start_setup()
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
    add_a_printer_page_ios.click_next_button()
    add_a_printer_page_ios.click_pair_button()
    """Step 6"""
    add_a_printer_page_ios.check_select_wifi()
    """Step 7"""
    add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
    """Step 8"""
    add_a_printer_page_ios.check_wifi_connected_successfully()
    add_a_printer_page_ios.finish_setup()


# def test_Addprinter_TestcaseID_45656():
#     """"Adding the moneybadger while the mobile devices bluetooth is disabled"""
#     """ FAILED : Because we sometimes after switching from settings to ZSB app, it is showing the setting option"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.logout()
#     app_settings_iOS_page_ios.Scroll_till_Delete_Account()
#     app_settings_iOS_page_ios.click_Logout_Btn()
#     add_a_printer_page_ios.disable_bluetooth()
#     """Step 1"""
#     login_screen_ios.login()
#     """Step 2"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     """Step 3"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.cancel_bluetooth()
#     """Step 4"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_settings()
#     add_a_printer_page_ios.enable_bluetooth()
#     """Step 5"""
#     sleep(2)
#     add_a_printer_page_ios.disable_bluetooth()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_unable_to_find()
#     """Step 6"""
#     add_a_printer_page_ios.enable_bluetooth()
#     add_a_printer_page_ios.click_search_again()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     """Step 7"""
#     add_a_printer_page_ios.disable_bluetooth()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 8"""
#     add_a_printer_page_ios.enable_bluetooth()
#     add_a_printer_page_ios.click_try_again()
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     """Step 9"""
#     add_a_printer_page_ios.finish_setup()


# def test_Addprinter_TestcaseID_45657():
#     """Check the cancel button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""
#     """FAILED :The Pair popup is not popping for the second time"""
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
#     """Step 5"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_cancel_pair()
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     add_a_printer_page_ios.unpair_printer()
#     """Step 6"""
#     add_a_printer_page_ios.click_try_again()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 7"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()


# def test_Addprinter_TestcaseID_45663():
#     """INVALID TESTCASE because there is no option for help in latest version of app"""
#     """set printer wpa psk Ess-id manually when the printer change to offline, and go to Help"""
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
#     """Step 5"""
#     add_a_printer_page_ios.enter_network_manually("connect")
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """----------INVALID TESTCASE----------"""


# def test_Addprinter_TestcaseID_45665():
#     """FAILED : when we click on cancel in step 4 it does not take us to set up printer page"""
#     """Check the left top corner button of each page work during adding a moneybadger"""
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
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.cancel_bluetooth()
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     """Step 6"""
#     login_screen_ios.click_Menu_HamburgerICN()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     """Step 7"""
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 8"""
#     add_a_printer_page_ios.click_start_button()
#     """Step 9"""
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 10"""
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     """INVALID TEST CASE"""

# def test_Addprinter_TestcaseID_45667():
#     """Check using the phone A to add the unconfigured printer which was paired the bluetooth connection by phone A and not in bluetooth limited mode"""
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
#     add_a_printer_page_ios.click_Add_A_Printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     """Step 6"""
#     add_a_printer_page_ios.check_select_wifi()
#     check = add_a_printer_page_ios.check_for_duplicate_wifi_networks()
#     if check:
#         pass
#     """Step 7"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     """Step 8"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()

# def test_Addprinter_TestcaseID_45672():
#     """connect printer by using the 'Add a Printer' button at the overview page and check information card"""
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
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     add_a_printer_page_ios.check_select_wifi()
#     check = add_a_printer_page_ios.check_for_duplicate_wifi_networks()
#     if check:
#         pass
#     """Step 6"""
#     add_a_printer_page_ios.choose_open_wifi_network()
#     """Step 10"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()


# def test_Addprinter_TestcaseID_45679():
#     """FAILED: In step 8 after clicking the cross button it is directly taking to home page, instead of Wifi-setup page"""
#     """To check Cancel and re-enter correct password for PSK WPA Essid works"""
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
#     check = add_a_printer_page_ios.check_for_duplicate_wifi_networks()
#     if check:
#         pass
#     """Step 7"""
#     add_a_printer_page_ios.choose_closed_wifi_network_incorrect_password()
#     add_a_printer_page_ios.check_unable_to_connect_printer()
#     """Step 8"""
#     add_a_printer_page_ios.click_cross()
#     add_a_printer_page_ios.click_exit_button()
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 9"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     """Step 10"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     add_a_printer_page_ios.finish_setup()
#     login_screen_ios.check_finish_setup()

# def test_Addprinter_TestcaseID_45682():
#     """To check the Cancel button in "Enter Network Info" dialog"""
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
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 5"""
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 7"""
#     add_a_printer_page_ios.enter_network_manually("cancel")
#     add_a_printer_page_ios.check_select_wifi()

# def test_Addprinter_TestcaseID_46303():
#     """To test the ZSB Wi-Fi performance"""
#     """Precondition"""
#     add_a_printer_page_ios.delete_printer()
#     add_a_printer_page_ios.unpair_printer()
#     login_screen_ios.login()
#     add_a_printer_page_ios.enable_bluetooth()
#     """Step 1"""
#     add_a_printer_page_ios.click_Add_A_Printer()
#     """Step 2"""
#     add_a_printer_page_ios.click_start_button()
#     add_a_printer_page_ios.check_connect_to_printer()
#     add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
#     add_a_printer_page_ios.click_next_button()
#     add_a_printer_page_ios.click_pair_button()
#     """Step 3"""
#     add_a_printer_page_ios.check_select_wifi()
#     """Step 4"""
#     add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
#     start_time = time.time()
#     """Step 5"""
#     add_a_printer_page_ios.check_wifi_connected_successfully()
#     end_time = time.time()
#     time_taken = start_time-end_time
#     assert time_taken <= 60, f"Error: Step 4 and Step 5 took too long ({time_taken} seconds), exceeding the 1-minute limit."

def test_add_printer_test_case_id_53067():
    """Printer Setup Screen-Check the UI of Printer Setup screen"""
    """Step 1"""
    login_screen_ios.login("Google")
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """Step 2"""
    add_a_printer_page_ios.check_ui_of_printer_setup()


def test_add_printer_test_case_id_53068():
    """Printer Setup Screen-Check the UI of Exit Printer Setup dialog"""
    """Step 1"""
    login_screen_ios.login("Google")
    """Step 2"""
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    add_a_printer_page_ios.click_cross()
    add_a_printer_page_ios.click_exit_button()


def test_add_printer_test_case_id_53070():
    """Printer Setup Screen-Verify the functionality, when the user clicks on "Start setup" option in "Setup your printer page"""
    """Step 1"""
    login_screen_ios.login("Google")
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    add_a_printer_page_ios.click_start_setup()


def test_add_printer_test_case_id_53071():
    """Verify the "Set up your printer" page is displayed the same for all the social login accounts"""
    social_logins = ["Google", "Apple", "Facebook"]
    for login in social_logins:
        # Step 1 & Step 2
        login_screen_ios.login(login)
        login_screen_ios.click_Menu_HamburgerICN()
        add_a_printer_page_ios.click_Add_A_Printer()
        add_a_printer_page_ios.check_ui_of_printer_setup()
        add_a_printer_page_ios.click_cross()
        add_a_printer_page_ios.click_exit_button()
        login_screen_ios.logout()
        app_settings_iOS_page_ios.Scroll_till_Delete_Account()
        app_settings_iOS_page_ios.click_Logout_Btn()


def test_add_printer_test_case_id_53073():
    """Install the lower version of the ZSB series app and upgrade to the latest version (.apk file) and check the Login Screen UI and Contents"""
    add_a_printer_page_ios.downgrade_app_version()
    login_screen_ios.check_login_ui()
    add_a_printer_page_ios.upgrading_app_version()
    login_screen_ios.check_login_ui()
    login_screen_ios.login("Google")
    login_screen_ios.logout()
    login_screen_ios.check_login_ui()


def test_add_printer_test_case_id_53086():
    """Verify the contents of "Search your printer" page and its animations are as per the figma design."""
    """Step 1"""
    login_screen_ios.login("Google")
    """Step 2"""
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """Step 3 & STep 4"""
    add_a_printer_page_ios.check_ui_of_printer_setup()
    """Step 5 & Step 6"""
    add_a_printer_page_ios.click_start_setup()
    """Step 7"""
    add_a_printer_page_ios.check_connect_to_printer()


def test_add_printer_test_case_id_53088():
    """Verify the behavior by selecting the printer from the list which is already registered with the same account."""
    """Pre-Condition"""
    add_a_printer_page_ios.delete_printer()
    add_a_printer_page_ios.unpair_printer()
    login_screen_ios.login("Google")
    """Step 1"""
    add_a_printer_page_ios.click_Add_A_Printer()
    """Step 2,3,4,5,6"""
    add_a_printer_page_ios.click_start_setup()
    """Step 7"""
    add_a_printer_page_ios.check_connect_to_printer()
    """Step 8 & Step 9"""
    add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
    """"Step 10"""
    add_a_printer_page_ios.click_next_button()
    # PENDING


def test_add_printer_test_case_id_53089():
    """Verify "Select Your Printer screen" screen UI, contents and buttons are proper as per the Figma design."""
    """Step 1"""
    login_screen_ios.login("Google")
    """Step 2"""
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """Step 3"""
    add_a_printer_page_ios.click_start_setup()
    """Step 4"""
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.click_find_my_printer_bluetooth_id()


def test_add_printer_test_case_id_53090():
    """Verify the behavior by selecting the printer from the list which is already registered with the same account."""
    """Pre-condition"""
    login_screen_ios.login("Google")
    register_printer()
    """Step 1"""
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """"Step 2 & 3"""
    add_a_printer_page_ios.click_start_setup()
    """Step 4"""
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
    add_a_printer_page_ios.click_next_button()
    add_a_printer_page_ios.click_pair_button()
    add_a_printer_page_ios.check_select_wifi()

