import inspect

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Others.Others import Others
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
# from setuptools import logging
from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
others = Others(poco)
device_networks = Device_Networks_Android(poco)

"""""""""""""""""""""""Change Password part needs to be verified manually"""""""""""""""""""""""""""""
ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()

start_execution_loop(execID)


# #### bug id-SMBM-2773
def test_AppSettings_TestcaseID_47913():
    test_steps = {
        1: [1, 'Install the ZSB app and log in with the user ID.'],
        2: [2, 'Click on the "Add Printer" button.'],
        3: [3, 'Once Bluetooth pairing is done, select the available Wi-Fi Access Point (AP).'],
        4: [4,
            'Once the Wi-Fi connection is established and you get the "Registering your printer" message on the mobile display, turn OFF the Wi-Fi AP.'],
        5: [5, 'Turn ON the Wi-Fi AP after approximately 2 minutes.'],
        6: [6,
            'Observe the printer registration process and ensure it resumes from the point where the network connection was dropped.Remove the printer once connected.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()
        """Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""
        common_method.show_message("Have a printer in hand to register in the upcoming steps.")
        common_method.show_message("Have a hotspot/wi-fi in hand which can be turned off when required.")
        common_method.tearDown()
        # test_robo_finger()
        # sleep(6)
        data_sources_page.log_out_of_account()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Add printer tab"""""
        add_a_printer_screen.click_Add_A_Printer()
        login_page.Verify_ALL_Allow_Popups()
        """"click on the start button"""
        add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
        """""Check the moneybadger picture would appears at that page."""
        add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
        """Click on Start setup button"""
        add_a_printer_screen.click_Start_Button()
        login_page.Verify_ALL_Allow_Popups()
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
        common_method.show_message("Select the Printer which you had prepared in the beginning.")
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """Verify Connect Wi-fi Network Text"""
        add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
        """Connect to wifi"""
        network_name = common_method.get_user_input("Enter the name of the wi-fi/hotspot which you prepared in the beginning.")
        network_password = common_method.get_user_input("Enter the password of the wi-fi/hotspot which you prepared in the beginning.")
        device_networks.click_network_by_name(network_name)
        device_networks.enter_the_password(network_password)
        device_networks.click_on_connect()
        app_settings_page.verify_connecting_to_wifi_network_page_is_displayed()
        app_settings_page.verify_printer_successfully_connected_to_wifi_network_page_displayed()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        app_settings_page.verify_registering_printer_to_zsb_account_page_displayed()
        common_method.show_message("Turn off the wi-fi/hotspot which is connected to the printer.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        sleep(120)
        common_method.show_message("Turn on the wi-fi/hotspot which is connected to the printer.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        app_settings_page.verify_registering_printer_to_zsb_account_page_displayed()
        app_settings_page.verify_printer_registration_successful_page_is_displayed()
        app_settings_page.complete_test_printer_steps()
        common_method.show_message("Remove the printer that was added now.")
        common_method.Stop_The_App()

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


###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


####### bug id---SMBM-2778
def test_AppSettings_TestcaseID_50031():
    """Check the error message prompted when print test page and printer head open or offline"""
    test_steps = {
        1: [1, 'Test user login mobile app.'],
        2: [2, 'Click Print Settings > printer tab > General.'],
        3: [3,
            'Click Test Print button. Check test label print out successfully and a toast message shows up: "Test label printed successfully to <Printer name>".'],
        4: [4, 'Open printer header, printer current status is Cover Open.'],
        5: [5, 'Click Test Print Button again.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        """printer should be online"""
        """start the app"""
        common_method.tearDown()
        sleep(3)
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on printer settings tab"""""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """click test print button"""
        app_settings_page.click_Test_Print_Button()
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Verify_Printout_Manually()
        """"Verify Printed successfully text"""
        app_settings_page.Verify_Printed_Successfully_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """"Open the printer cover manually"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Open_The_Printer_Cover_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """click test print button"""
        app_settings_page.click_Test_Print_Button()
        """""verify error message of cover open"""
        app_settings_page.Verify_ErrorMessage_Text()
        """""Cover close on the printer manually"""""
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
        """"click on test print"""
        app_settings_page.click_Test_Print_Button()
        """"Verify Printed successfully text"""
        app_settings_page.Verify_Printed_Successfully_Text()
        """stop the app"""
        common_method.Stop_The_App()

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


## #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id-SMBM-2160
"""Blocked due to bug SMBM-2932"""


def test_AppSettings_TestcaseID_49709():
    pass
    test_steps = {
        1: [1, 'Sign in to the test account with a printer added, go to Printer settings > Printer name > Wi-Fi tab.'],
        2: [2, 'Click Manage Networks option, pair Bluetooth if needed, and click the Add Network option.'],
        3: [3,
            'When the network list is displayed, click the "Enter Network Manually" option. Enter a long network name ("Test-EnterNetwork-Manually-NameDisplay", 38 characters), input password if needed, then submit. Check if the added network is displayed in the list and verify that the delete button is clickable (Some characters may be hidden, which is acceptable).'],
        4: [4,
            'Exit the manage network screen and re-enter it. Check if the added network is still displayed in the list.'],
        5: [5, 'Attempt to sort or delete the network. Verify that all functions work as expected.']
    }
    """Manage network - Check able to manage network with long name"""
    common_method.show_message("Prepare a wi-fi/hotspot network with long name(38-char)")
    """"printer should be online & wifi should be connected"""
    """start the app"""
    common_method.tearDown()
    """click on hamburger menu icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
    common_method.show_message(
        "Check if message'\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.'\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")
    login_page.click_Allow_ZSB_Series_Popup()
    """"""""""verify the continue button and click on that"""""
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    sleep(5)
    """"""""""Verify the Add Network text & button & click on that"""""""""""
    app_settings_page.click_Add_Network()
    sleep(3)
    """""""""""""Verify Add network page is opening and verify the text"""""""
    app_settings_page.get_text_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    long_network_name = common_method.get_user_input("Enter the Name of the long name network in the text field.")
    common_method.show_message("Connect to 'long name network' which you prepared in the beginning.")
    app_settings_page.Verify_Long_Network_UserName(long_network_name)
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    """"click on the red icon to delete the added network name"""

    # """stop the app"""
    # common_method.Stop_The_App()


##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ####bug id-SMBM-2163
"""Update name of network which cannot resolve zebra host"""
def test_AppSettings_TestcaseID_49711():
    """Manage networks- Check there is a prompt message when applying to the network which can't resolve Zebra host"""
    test_steps = {
        1: [1,
            'Sign in to the test account with the printer added and the printer in Online status (connected to a valid network). Go to Printer settings > Printer name > Wi-Fi tab. Check if the current connected Wi-Fi is correct.'],
        2: [2,
            'Click Manage Networks option, pair Bluetooth if needed. Click Add Network option. Check if the available Wi-Fi networks are shown correctly.'],
        3: [3, 'Select the network that cannot resolve the Zebra host. Check if the network can be added to the list.'],
        4: [4,
            'Sort the newly added network to the first priority and apply the changes. Check for a prompt message notifying the user that the network is invalid for the printer. If no prompt appears, verify that it connects to the second priority network within 5 minutes.']
    }
    """start the app"""
    common_method.tearDown()
    """click on hamburger menu icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    """"verify bluetooth connection required text"""
    common_method.handel_bluetooth_connection_required_pop_up()
    app_settings_page.click_Allow_Btn()
    app_settings_page.click_Add_Network()
    device_networks.wait_till_the_networks_list()
    default_network = "NESTWIFI"
    netw1 = "zebra-host"
    netw1pass = "123456789"
    device_networks.click_network_by_name(netw1)
    device_networks.enter_the_password(netw1pass)
    device_networks.click_on_connect()
    device_networks.check_if_network_present_in_saved_networks(netw1)
    app_settings_page.click_Apply_Chnages_Button()
    device_networks.swap_two_networks(default_network, netw1)
    """""Currently there is no error message displaying so Couldnot automate, it is blocked due to SMBM-2163"""""""""""
    """"Verify The error message manually if it is displaying"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.show_message("Check for a prompt message notifying the user that the network is invalid for the printer. If no prompt appears, verify that it connects to the second priority network within 5 minutes.")
    # common_method.Show_popup_For_Error_Message_Manually()
    ### app_settings_page.Verify_The_Invalid_Network_Error_Message()
    """stop the app"""
    common_method.Stop_The_App()


## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50326():
    """Manage Network- Check able to add/delete/sort network when printer bt paired/unpaired in device""""""

    """"App should be in logged in condition & printer should be added """"
    """"""connect with Another wifi Network except NESTWIFI"""
    test_steps = {
        1: [1, 'Sign in to the test account and navigate to Printer settings > Printer name > Wi-Fi tab.'],
        2: [2, 'Click Manage Networks, pair Bluetooth if needed. Check that the "Add Network" option is visible.'],
        3: [3,
            'Click on the "Add Network" button and select a network to add. Verify that the network is added successfully to the network list.'],
        4: [4,
            'Delete one of the added networks. Check that the deleted network is no longer visible in the network list.'],
        5: [5,
            'Sort the network list, exit the Manage Networks page, and return to the home page. Verify that the printer is online and that it is possible to print a test label.'],
        6: [6,
            'Go to the device’s settings and disconnect the printer Bluetooth (or use another device, sign in with the same user, ensuring the printer is not paired).'],
        7: [7,
            'Return to the ZSB Series app and click Manage Networks, pair Bluetooth if needed. Check that the network at the top is the one sorted in step 5.'],
        8: [8, 'Turn on the bluetooth and remove the newly added network.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        """"start the app"""
        common_method.tearDown()
        """"click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_wifi_tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        app_settings_page.click_Manage_Networks_Btn()
        common_method.handel_bluetooth_connection_required_pop_up()
        others.click_on_allow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        netw1 = "EVT_ArubaOpen"
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        sleep(5)
        common_method.wait_for_element_appearance("Connected", 100)
        common_method.wait_for_element_appearance_enabled("Apply Changes")
        device_networks.check_if_network_present_in_saved_networks(netw1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        device_networks.delete_the_network(netw1)
        sleep(5)
        device_networks.check_if_network_not_present_in_saved_networks(netw1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """Add one more network"""
        others.click_add_network_button()
        default_network = "NESTWIFI"
        netw2 = "EL17-Cisco-WPA-WPA2"
        netw2_pass = "Dvttesting@123"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()
        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        sleep(5)
        common_method.wait_for_element_appearance("Connected", 100)
        common_method.wait_for_element_appearance_enabled("Apply Changes")
        device_networks.check_if_network_present_in_saved_networks(netw2)
        device_networks.swap_two_networks(default_network, netw2)
        app_settings_page.click_Apply_Chnages_Button()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Home_Tab()
        others.check_printer_online_status()
        login_page.click_Menu_HamburgerICN()
        """"click on printer settings tab"""""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()
        """click test print button"""
        app_settings_page.click_Test_Print_Button()
        """"Verify Printed successfully text"""
        app_settings_page.Verify_Printed_Successfully_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        add_a_printer_screen.disable_bluetooth()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        app_settings_page.click_wifi_tab()
        app_settings_page.click_Manage_Networks_Btn()
        common_method.handel_bluetooth_connection_required_pop_up()
        app_settings_page.click_Allow_Btn()
        network_list = device_networks.get_network_names()
        if network_list[0] != netw2:
            raise Exception(
                "Networks not in the order that we sorted before returning to the page after navigating to home page..")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        add_a_printer_screen.enable_bluetooth()
        device_networks.delete_the_network(netw2)
        """stop the app"""
        common_method.Stop_The_App()

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


#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45688():
    """""""""Verify Wifi Settings"""""
    """""Install the latest production app on the phone & printer should be added and it should be connected to wifi"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""
    test_steps = {
        1: [1, 'Click Printer Settings > select Printer Tab (e.g., ZSB-DP12) > Select Wi-Fi tab.'],
        2: [2,
            'Verify that the options "Current network," "Network Status," and "IP Address" are displayed, along with the "Manage Networks" button enabled in blue and the prompt message under the button.'],
        3: [3,
            'Click on the "Manage Networks" button. Confirm that the "Bluetooth Connection Required" dialog pops up with the expected text.'],
        4: [4,
            'Complete the pairing process if necessary. After finishing, verify that the "My Saved Networks" list is retrieved and the "Add Network" button is displayed at the bottom.'],
        5: [5,
            'Click the red icon to remove the current network. Check that the network is removed successfully and that the "Add Network" button is enabled.'],
        6: [6,
            'Click the "Add Network" button to add back the previously deleted network. Verify that the network can be added back successfully.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        """" Allow pop up before login for the fresh installation"""""
        login_page.click_LoginAllow_Popup()
        """""for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        """""click on the printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """""click on the printer tab"""
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_General_Tab()
        """"Verify the Test print button text & tab"""
        app_settings_page.Test_Print_button_is_present_on_printer_settings_page()
        """""""""" click on the wifi tab option"""""""""""
        app_settings_page.click_wifi_tab()
        """""""""validate the Current network text"""""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        app_settings_page.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
        common_method.show_message("Check manage networks is enabled and is blue in colour")
        """""""Validate the Network status text is present on the printer settings screen"""""""
        app_settings_page.test_Network_Status_Txt_is_present_on_printer_settings_page()
        """"validate network status result text on the printer settings screen"""
        app_settings_page.get_text_Network_Status_Result_Txt()
        """"""""" Verify IP address text is present on the printer settings screen"""""""""
        app_settings_page.get_text_IPAddress_Txt()
        """""""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
        app_settings_page.IS_Present_Save_Network_Message_Txt()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """""""verify manage networks text is present & clickable"""""""
        app_settings_page.click_Manage_Networks_Btn()
        """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
        common_method.handel_bluetooth_connection_required_pop_up()
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        device_networks.check_if_saved_network_list_is_displayed()
        device_networks.check_add_network_button_present()
        common_method.show_message("Check if the printer is connected to 'NESTWIFI' else connect it to 'NESTWIFI' and remove all other networks from saved networks. Wait for 'NESTWIFI' to show connected state.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """"""""""Verify the red remove icon next to the network name"""""
        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.delete_the_network(netw1)
        sleep(5)
        device_networks.check_add_network_button_enabled()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """"""""""Verify the Add Network text & button & click on that"""""""""""
        app_settings_page.click_Add_Network()
        sleep(3)
        """""""""""""Verify Add network page is opening and verify the text"""""""
        app_settings_page.get_text_Add_Network()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)
        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()
        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        common_method.wait_for_element_appearance("Connected", 200)
        device_networks.check_if_network_present_in_saved_networks(netw1)
        """stop the app"""
        common_method.Stop_The_App()

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


##"""""""""""""""""""""""""""""END"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45876():
    """	Check basic functions work well after upgrading"""

    """"Setup:
    1. The previous version has already been installed in test device
    2. Sign in the test account, with 1 printer added
    3. There is at least one design in My designs"""""

    """start the app"""""
    common_method.tearDown()
    common_method.Stop_The_App()
    # ##common_method.uninstall_app()
    # ##common_method.install_Older_app()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    app_settings_page.Home_text_is_present_on_homepage()
    """""""Verify the Already added Printer"""
    app_settings_page.Verify_Printer_is_already_added()
    common_method.Stop_The_App()
    #### common_method.uninstall_app()
    # ####common_method.install_app()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    app_settings_page.Home_text_is_present_on_homepage()
    app_settings_page.Verify_Printer_is_already_added()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
    add_a_printer_screen.click_FirstOne_In_Common_Design()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.Update_PrinterName_With_Different_Valid_Name()
    app_settings_page.verify_Printer_Name_Updated_Message()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.Update_PrinterName()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    common_method.Stop_The_App()
    """""The below steps need to be verified manually""""""""""""""
    7. Open printer cover
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
    """Check the status on home page is shown as "Cover Open"""""
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
    aps_notification.Verify_Printer_Status_Is_Present()


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45901():
    """Update Auto label feed setting(disable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.Check_toggle_button()
    """stop the app"""
    common_method.Stop_The_App()
    """""""web portal part needs to be verified Manually"""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Web_Portal_Verification_Manually()


# ## #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45882():
    """Verify sign in with non-Zebra account, check the design linked different format file from One Drive can be printed out successfully"""

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
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.Verify_Design_Preview_Screen_With_Details()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    add_a_printer_screen.click_SecondOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    common_method.Stop_The_App()
    """""The below step needs to be verified manually"""
    """"""""""2. Sign in the same account on Web portal, create design1, add text object, and link One Drive file with xlsx format. Create design2, add text object, and link One Drive file with csv format"""""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Design_Verification_On_Web_Portal_Manually()


# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45900():
    """Update Auto label feed setting(enable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.Check_toggle_button()
    """click on the toggle button"""
    app_settings_page.click_toggle_button()
    """stop the app"""
    common_method.Stop_The_App()
    """""""web portal part needs to be verified Manually"""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Darkness_Level_Verification_On_Web_Portal_Manually()


# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45886():
    """Check Mobile App can display correct printer status and notifications when printer status updates"""

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
    sleep(5)
    """Turn off the printer manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
    aps_notification.Verify_Printer_Status_AS_Offline()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Notifications_Tab()
    app_settings_page.Verify_Offline_Notification()
    """Head open on the printer manually """
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Open_The_Printer_Head_Manually()
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    app_settings_page.Verify_HeadOpen_Notification()
    """"Make the status as paper out manually """
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Remove_The_Cartridge_Manually()
    aps_notification.Verify_Printer_Status_AS_Paper_Out()
    app_settings_page.Verify_Paper_Out_Notification()
    """"Make the status as media low manually """
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Make_The_Status_AS_LowMedia_Manually()
    aps_notification.Verify_Printer_Status_AS_Media_LOW()
    app_settings_page.Verify_Media_LOW_Notification()
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Insert_Different_Cartridge_Manually()
    """"Check the preview page and the label would be re-sized in the preview page"""""
    """"POP UP FOR MANUAL INTERVENTION"""""
    common_method.Show_popup_To_Make_The_Status_AS_Online()
    app_settings_page.Verify_Online_Notification()
    common_method.Stop_The_App()


## #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45887():
    """	User modify the printer's darkness setting and perform test print"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.click_Test_Print_Button()
    """""Log into web portal and ensure darkness level is updated Manually""""""
    """"POP UP FOR MANUAL INTERVENTION"""
    common_method.Show_popup_To_Verify_Darkness_level_On_Web_Portal_Manually()
    """"Keep on the page and install another type of cartridge, such as LC1, LC4 Manually"""
    """"POP UP FOR MANUAL INTERVENTION"""
    common_method.Show_popup_To_Insert_Different_CartridgeLC1_4_Manually()
    app_settings_page.click_Test_Print_Button()
    """stop the app"""""
    common_method.Stop_The_App()
    """""Check it should print the template which matches the new cartridge Manually"""""""""""""
   """""""Test Print" button in the Printer Settings should be dimmed and inactive when the printer is offline for Mobile, to match Portal"""


# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45877():
    """	Verify create a brand new user with unregistered user in Mobile App."""

    #
    """"Setup:
    1. Create a new email address
    (Need to match the new register email format, for IDC, it should be soho_swdvt_xxxx@xxxx.com, for CDC, it should be soho_swdvt_xxxx@xxxx.com)
    2. Install the target build of ZSB app on mobile device"""""

    """start the app"""""
    common_method.tearDown()
    common_method.Clear_App()
    Common_Method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    common_method.show_message("Create new email before running")
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.verifyLinksInSignInPage()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")
    email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")

    registration_page.enter_user_email_for_registering(email)
    try:
        registration_page.wait_for_element_appearance("Resend Verification Code.", 10)
    except:
        raise Exception("Page to enter verification code did not appear. ")
    """Enter verification code manually"""
    common_method.show_message(
        "Enter verification code on the device ,verification code received in the newly created google account")
    """Enter the User Email"""
    registration_page.click_on_next()
    sleep(2)
    """Enter the first Name last name and the password"""
    first_n = "Zebra"
    last_n = "Z"
    password = "Zebra#123456789"
    registration_page.enter_the_fields(first_n, last_n, password)
    registration_page.select_the_country("India")
    registration_page.select_the_check_boxes()
    registration_page.click_submit_and_continue()
    sleep(2)
    registration_page.check_sign_up_successful()
    registration_page.click_continue_registration_page()
    registration_page.wait_for_element_appearance("Sign In")
    registration_page.clickSignIn()
    registration_page.wait_for_element_appearance_text("Continue with Google", 10)
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    registration_page.verify_if_on_EULA_page()
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")


# # ## """"""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_Smoke_Test_TestcaseID_45889():
    """	Check user can upload or link file to My Data"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    smoke_test_android.click_MyData_Tab()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_Upload_icon()
    smoke_test_android.Upload_First_Image()
    """""Login web portal and go to My Data page,Check the uploaded files from mobile app display in the my data page in web portal Manually""""""""""""
    """"Check switch to different menu or press F5 should be able to refresh the file list Manually"""""""""""""
    """"POP UP FOR MANUAL INTERVENTION"""
    common_method.Show_popup_For_Web_Portal_Verification_Manually()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_LinkFile()
    smoke_test_android.click_Microsoft_OneDrive_Tab()
    smoke_test_android.click_Google_Drive()
    smoke_test_android.click_On_PNG_File()
    smoke_test_android.click_On_Select_Btn()
    smoke_test_android.Verify_TheLinked_PNG_IS_Present()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_LinkFile()
    smoke_test_android.click_Microsoft_OneDrive_Tab()
    smoke_test_android.click_Google_Drive()
    smoke_test_android.click_On_Jpg_File()
    smoke_test_android.click_On_Select_Btn()
    smoke_test_android.Verify_TheLinked_JPG_IS_Present()
    smoke_test_android.Verify_Uploaded_Date_Is_Displaying()
    smoke_test_android.Verify_Name_Is_Present()


# # # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"""""""""""""""""""Others""""""""""""

def test_Others_TestcaseID_45799():
    pass
    common_method.show_message("test this manually in android 8.0 device")

    start_app("com.android.documentsui")
    t = ''
    others.install_the_zsb_apk_in_files_android_8()
    sleep(3)
    res = others.check_app_is_installed_on_android_8()
    if res:
        raise Exception("app is installed but it should not")

    others.go_back()
    others.go_back()

    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    while (1):
        if others.check_zsb_app_icon():
            t = 'present'
            break
        else:
            others.scroll_down()

    if t == 'present':
        raise Exception("app present")


def test_Others_TestcaseID_51703():
    pass
    common_method.show_message("Install the testing build on device")

    sleep(2)
    common_method.tearDown()

    others.check_allow_permission_for_location()
    login_page.click_loginBtn()
    try:
        others.click_on_allow()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass
    try:
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.click_an_google_account("zebra850.swdvt@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home", 30)
    res = others.check_home_page()
    if not res:
        raise Exception("Not in Home page")

    others.uninstall_and_install_zsb_series_on_google_play()
    common_method.wait_for_element_appearance_namematches("Uninstall", 30)
    stop_app("com.android.vending")

    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    while (1):
        if others.check_zsb_app_icon():
            t = 'present'
            break
        else:
            others.scroll_down()

    others.click_zsb_app_icon()
    sleep(5)

    try:
        others.check_allow_permission_for_location()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass

    try:
        login_page.click_loginBtn()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass
    try:
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.click_an_google_account("zebra850.swdvt@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home", 30)

    res = others.check_home_page()
    if not res:
        raise Exception("Not in Home page")


def test_Others_TestcaseID_51704(self):
    pass

    common_method.show_message("Install the older build in phone")
    common_method.show_message("now install 1. Install the new build, ")

    sleep(10)

    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_textmatches("location")
    others.check_allow_permission_for_location()
    try:
        others.click_on_allow()
    except:
        pass
    others.click_on_older_login()
    try:
        others.click_on_allow()
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    try:
        others.click_an_google_account("zebra850.swdvt@gmail.com")
        common_method.wait_for_element_appearance_namematches("Home", 20)
    except:
        pass
    try:
        others.check_continue_button_and_click_enter()
        others.check_continue_button_and_click_enter()
    except:
        pass
    res = others.check_home_page()

    if not res:
        raise Exception("Not in Home page")

    cmd = 'adb uninstall com.zebra.soho_app'
    res = others.run_the_command(cmd)
    print(res)

    common_method.show_message("install older build and new build again")
    sleep(15)
    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    while (1):
        if others.check_zsb_app_icon():
            t = 'present'
            break
        else:
            others.scroll_down()

    others.click_zsb_app_icon()
    sleep(5)

    others.check_allow_permission_for_location()
    try:
        others.click_on_allow()
    except:
        pass
    login_page.click_loginBtn()
    try:
        others.click_on_allow()
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    try:
        others.click_an_google_account("zebra850.swdvt@gmail.com")
        common_method.wait_for_element_appearance_namematches("Home", 20)
    except:
        pass

    try:
        others.check_continue_button_and_click_enter()
        others.check_continue_button_and_click_enter()
    except:
        pass

    res = others.check_home_page()

    if not res:
        raise Exception("Not in Home page")


def test_Others_TestcaseID_45874(self):
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Home")
    except:
        pass

    expected_version_no = common_method.get_user_input("enter the version number to be expected")
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()

    """get the version number of the current device"""
    actual_version_no = others.get_the_version_no()

    """If version number not same generate error"""
    if expected_version_no != actual_version_no:
        raise Exception("Version no did not match")

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##"""""""""""""""""""""""""""""END"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
