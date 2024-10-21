from airtest.core.api import auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
import inspect
from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ...PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from ...PageObject.Robofinger import test_robo_finger
import os
import time
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

ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()

start_execution_loop(execID)


def preconditions(bluetooth=None):
    add_a_printer_page_ios.delete_printer()
    add_a_printer_page_ios.unpair_printer()
    # login_screen_ios.logout()
    # app_settings_iOS_page_ios.Scroll_till_Delete_Account()
    # app_settings_iOS_page_ios.click_Logout_Btn()
    if bluetooth == "bt_disable":
        add_a_printer_page_ios.disable_bluetooth()
    else:
        add_a_printer_page_ios.enable_bluetooth()


def pair_printer(test_case_id, pair):
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])
    login_screen_ios.login("Google")
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
    if pair == "pair":
        add_a_printer_page_ios.click_pair_button()
    else:
        add_a_printer_page_ios.click_cancel_pair()


def register_printer():
    login_screen_ios.login("Google")
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


def test_add_printer_testcase_id_45656():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    test_steps = {
        1: [1, 'Open the app and login the account to go to the overview page.'],
        2: [2, 'Click the menu button at the left corner\nCheck the slide left page appears.'],
        3: [3,
            'Click the button "Add a Printer"\nCheck it goes to the page "Set up your printer"\nCheck the moneybadger picture appears on that page.\nCheck the dialog with prompt message "Turn on Bluetooth to Allow "ZSB Printer App" to Connect", click on the Cancel button.\nCheck the "Set up your printer" page dismisses and returns to the slide left page.'],
        4: [4,
            'Click the "Add a Printer" button again\nCheck it pops up the dialog with prompt message "Turn on Bluetooth to Allow "ZSB Printer App" to Connect", click on the Settings button, go to settings and enable Bluetooth, then click the back button on the settings page.\nCheck it returns to the "Set up your printer" page.']
    }
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])
    stepId = 1  # Initialize stepId before the try-except block
    try:
        """Precondition"""
        preconditions("bt_disable")
        """Step 1"""
        start_time = time.time()
        login_screen_ios.login("Google")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        """Step 2"""
        start_time = time.time()
        login_screen_ios.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        """Step 3"""
        start_time = time.time()
        add_a_printer_page_ios.click_Add_A_Printer()
        add_a_printer_page_ios.cancel_bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        """Step 4"""
        start_time = time.time()
        add_a_printer_page_ios.click_Add_A_Printer()
        add_a_printer_page_ios.click_settings()
        add_a_printer_page_ios.enable_bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_add_printer_testcase_id_45657():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Sign in the account and click My Data option'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Google Drive will be opened and let user select file to link'],
        4: [4,
            'Select the file with Special character from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
        5: [5,
            'Select the file with long file name from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
        6: [6, 'Remove these 2 files\nCheck these 2 files are able to remove'],
        7: [7, 'Repeat this test case for OneDrive'],
        8: [8, 'Check Account Settings page should provide user management of Google and OneDrive accounts']
    }
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Sign in the account and click My Data option

        """Check the cancel button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""
        """Precondition"""
        preconditions()
        """Steps"""
        start_time = time.time()
        pair_printer(test_case_id, "cancel")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        add_a_printer_page_ios.check_unable_to_connect_printer()
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_add_printer_testcase_id_45665():
    """FAILED : when we click on cancel in step 4 it does not take us to set up printer page"""
    """Check the 'X' button (left top corner) of setup your printer page"""
    """Precondition"""
    preconditions()
    """Step 1"""
    login_screen_ios.login("Google")
    """Step 2"""
    login_screen_ios.click_Menu_HamburgerICN()
    """Step 3"""
    add_a_printer_page_ios.click_Add_A_Printer()
    """Step 4"""
    add_a_printer_page_ios.check_ui_of_printer_setup()
    add_a_printer_page_ios.click_cross()
    """Step 5"""
    add_a_printer_page_ios.cancel_bluetooth()
    add_a_printer_page_ios.click_cross()
    add_a_printer_page_ios.click_exit_button()
    """Step 6"""
    login_screen_ios.click_Menu_HamburgerICN()


def test_Addprinter_TestcaseID_45667():
    """Check using the phone A to add the unconfigured printer which was paired the bluetooth connection by phone A and not in bluetooth limited mode"""
    """Precondition"""
    preconditions()
    """Steps"""
    pair_printer("pair")
    add_a_printer_page_ios.check_select_wifi()
    add_a_printer_page_ios.enter_network_manually("connect")
    # check = add_a_printer_page_ios.check_for_duplicate_wifi_networks()
    # if check:
    #     pass
    add_a_printer_page_ios.check_wifi_connected_successfully()
    add_a_printer_page_ios.finish_setup()
    login_screen_ios.check_finish_setup()


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
    """FAILED: Facebook login was not possible"""
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


def test_add_printer_test_case_id_53091():
    """Check the UI of Wi-Fi searching screen is same as Figma design"""
    """Pre-condition"""
    add_a_printer_page_ios.delete_printer()
    add_a_printer_page_ios.unpair_printer()
    add_a_printer_page_ios.enable_wi_fi()
    """Step 1"""
    login_screen_ios.login("Google")
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """"Step 2"""
    add_a_printer_page_ios.click_start_setup()
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
    add_a_printer_page_ios.click_next_button()
    add_a_printer_page_ios.click_pair_button()
    """Step 3"""
    add_a_printer_page_ios.check_wifi_search_page_ui()


def test_add_printer_test_case_id_53093():
    """[Wi-Fi Network Connection]- Check able to connect a secure Wi-fi with correct pw and proceed (From Discovered networks)"""
    """Pre-condition"""
    add_a_printer_page_ios.delete_printer()
    add_a_printer_page_ios.unpair_printer()
    add_a_printer_page_ios.enable_wi_fi()
    """Step 1"""
    login_screen_ios.login("Google")
    login_screen_ios.click_Menu_HamburgerICN()
    add_a_printer_page_ios.click_Add_A_Printer()
    """"Step 2"""
    add_a_printer_page_ios.click_start_setup()
    add_a_printer_page_ios.check_connect_to_printer()
    add_a_printer_page_ios.click_the_printer_name_to_select("C664C1")
    add_a_printer_page_ios.click_next_button()
    add_a_printer_page_ios.click_pair_button()
    """Step 3"""
    sleep(10)
    add_a_printer_page_ios.choose_closed_wifi_network_correct_password("Tauqeer’s iPhone")
    add_a_printer_page_ios.check_wifi_connected_successfully()
# except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
#         raise Exception(str(e))
# finally:
#         common_method.stop_adb_log_capture()
#         upload_case_files(execID, os.path.dirname(ADB_LOG), test_run_start_time)
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
#         end_execution_loop(execID)
#         end_execution(execID)
