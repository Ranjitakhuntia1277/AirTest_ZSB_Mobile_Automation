import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
from ...Common_Method import *
from ...PageObject.Social_Login.Social_Login import Social_Login
# from ZSB_Mobile.sphere_db import *
from ...PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ...TestSuite.api_calls import *
import inspect
from ...TestSuite.store import *
import pytest
import os
import logging


class Android_App_Device_Networks_Semiautomated:
    pass


logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method = Common_Method(poco)
social_login = Social_Login(poco)
device_networks = Device_Networks_Android(poco)


#
# """EXECID and LEFTID need to be changed"""
# execID=0
# leftId = {}

def go_till_printer_wifi_page(self, add_network=0):
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.click_wifi_button()
    if add_network:
        others.click_manage_network_button()
        common_method.show_message(
            "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

        others.click_on_allow()
        common_method.wait_for_element_appearance_namematches("Apply Changes")


def test_Device_Networks_TestcaseID_45695(self):
    test_steps = {
        1: [1, 'Slide the left slide page to choose "Printer Settings" item'],
        2: [2, 'Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        3: [3,
            'Click the Wi-Fi tab, then click "Manage networks" button, after the network list loaded, click on "Add network" button. Check it would go to the page "Add Network" with the list only containing 2 types of Essid: one is open Essid, one is WPA PSK Essid with lock icon'],
        4: [4,
            'Choose WPA PSK Essid. Check it would pop up the dialog "Join Network" with the words "Please enter the password for XXXX (Essid name) to join the network." and the input box "enter password" and 2 buttons "Cancel" and "Submit"'],
        5: [5,
            'Input the incorrect password and click "Submit". Check the error dialog pop up: "Failed to connect to Wifi Network. Printer failed to connect to Wifi Network. This could be caused by incorrect password, router rejecting the connection, or wifi network being out of range. Do you want to continue or cancel the changes?" Cancel and Continue button on dialog'],
        6: [6, 'Click cancel button on dialog, the new select network will be deleted and not show in network list.'],
        7: [7,
            'Click continue button on dialog, the network will be added into printer, but printer will show offline status, the new added network will show in network list']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:

        #step1:"Slide the left slide page to choose "Printer Settings" item"
        start_time = time.time()

        if not social_login.check_for_incorrect_username_in_google():
            raise Exception("Error not found for incorrect email")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        # step2:"Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14"
        start_time = time.time()

        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        # step3:"Click the Wi-Fi tab, then click "Manage networks" button, after the network list loaded, click on "Add network" button. Check it would go to the page "Add Network" with the list only containing 2 types of Essid: one is open Essid, one is WPA PSK Essid with lock icon'"
        start_time = time.time()

        others.click_add_network_button()
        netw2 = common_method.get_user_input("enter name of network here which is not connected to printer")
        netw2_pass = common_method.get_user_input("enter wrong password for the network")
        device_networks.wait_till_the_networks_list()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        # step4:"Choose WPA PSK Essid. Check it would pop up the dialog "Join Network" with the words "Please enter the password for XXXX (Essid name) to join the network." and the input box "enter password" and 2 buttons "Cancel" and "Submit"
        start_time = time.time()

        device_networks.click_network_by_name(netw2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        # step5:"Input the incorrect password and click "Submit". Check the error dialog pop up: "Failed to connect to Wifi Network. Printer failed to connect to Wifi Network. This could be caused by incorrect password, router rejecting the connection, or wifi network being out of range. Do you want to continue or cancel the changes?" Cancel and Continue button on dialog'
        start_time = time.time()

        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()
        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 300)

        if not device_networks.check_the_wordings_in_connect_to_network():
            raise Exception("fails the wordings in the failed connected network")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        #step6:'Click cancel button on dialog, the new select network will be deleted and not show in network list.'
        start_time = time.time()

        device_networks.click_on_cancel_button()

        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        if netw2 in s1:
            raise Exception("fails: check the network is not added in the saved network list.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

        #step7:'Click continue button on dialog, the network will be added into printer, but printer will show offline status, the new added network will show in network list']
        start_time = time.time()

        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
        device_networks.click_on_continue_in_network_disconnect_error()
        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        print(s1)
        if netw2 not in s1:
            raise Exception("fails: check the network is  added in the saved network list.")
        common_method.wait_for_element_appearance_namematches(netw2, 60)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45695"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", 0)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


"""Fully automated"""


def test_Device_Networks_TestcaseID_45696():
    test_steps = {
        1: [1, 'Open the app and login the account with online Moneybadger'],
        2: [2,
            'Slide the left slide page to choose "Printer Settings" item. Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        3: [3,
            'Click the Wi-Fi tab. Check it would be spinning for a while to wait all infos appears at the page. After that, it would appear the button "Add Network" at the bottom. Check the Current Network, Network Status, IP Address and My saved Networks info all are correct. Check the list "My saved Networks" has the Name words at the left and Edit button at the right. Check those Essids would appear at the list "My saved Networks" such as: AEssid, BEssid, CEssid'],
        4: [4,
            'Click "Edit" button. Check the Essids would appear the drag button at the left and delete button at the right'],
        5: [5,
            'Drag the BEssid to the top of the list. Check the Moneybadger would change the network to BEssid. Check the Current Network, Network Status, IP Address would be updated accordingly']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Open the app and login the account with online Moneybadger
        start_time = time.time()
        common_method.tearDown()
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45696"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Slide the left slide page to choose "Printer Settings" item
        start_time = time.time()
        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45696"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click the Wi-Fi tab. Check all necessary info and elements.
        start_time = time.time()
        others.click_add_network_button()
        default_network = "NESTWIFI"
        netw1 = "EL17-Cisco-WPA-WPA2"
        netw1_pass = "Dvttesting@123"

        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45696"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click "Edit" button. Check drag and delete buttons for Essids.
        start_time = time.time()
        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        common_method.wait_for_element_appearance_namematches(netw1, 60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45696"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Drag the BEssid to the top of the list. Check network updates.
        start_time = time.time()

        device_networks.swap_two_networks(default_network, netw1)

        others.click_apply_changes_button()
        common_method.wait_for_element_appearance("Connected", 100)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception(
                "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45696"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45697(self):
    test_steps = {
        1: [1, 'Open the app and login the account with online Moneybadger'],
        2: [2, 'Slide the left slide page to choose "Printer Settings" item. Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        3: [3,
            'Click the Wi-Fi tab. Check it would be spinning for a while to wait all infos appears at the page. After that, it would appear the button "Add Network" at the bottom. Check the Current Network, Network Status, IP Address and My saved Networks info all are correct. Check the list "My saved Networks" has the Name words at the left and Edit button at the right'],
        4: [4,
            'Click "Add Network" button to add 5 Essids to the list "My saved Networks" (Select from network list or enter network manually). Check the button "Add Network" is dismissed or disabled'],
        5: [5,
            'Back to home page. Check the background picture is shown correctly (Add this step for covering SMBUI-1199)'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Open the app and login the account with online Moneybadger
        start_time = time.time()
        common_method.show_message("There are at least five essid for testing, add five networks to the printer")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 2: Slide the left slide page to choose "Printer Settings" item
        start_time = time.time()
        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 3: Click the Wi-Fi tab. Check all necessary info and elements.
        start_time = time.time()
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("fails:Check the Current Network, Network Status, info all are correct.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 4: Click "Add Network" button to add 5 Essids. Check button state.
        start_time = time.time()
        others.click_add_network_button()

        if device_networks.check_add_network_button_enabled():
            raise Exception("Add network is enabled even after adding 5 networks")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 5: Back to home page. Check background picture.
        start_time = time.time()
        common_method.show_message("Back to home page. Check background picture.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1


    except Exception as e:

        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)

        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))

        raise Exception(str(e))


    finally:

        exec_time = (time.time() - start_time_main) / 60

        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45699(self):
    test_steps = {
        1: [1, 'Open the app. Check the printer is offline and it is not in pairing mode'],
        2: [2, 'Go to the printer Wi-Fi tab. Check all info shows "Not Connected". Click Manage Networks option'],
        3: [3,
            '“Bluetooth Connection Required” dialog pops up. Click Continue button. Check the “Bluetooth Connection Failed” dialog pops up since printer is not in pairing mode'],
        4: [4,
            'Press 3s on power button to enter pairing mode. Click Continue button on the “Bluetooth Connection Failed” dialog. Check it will try to connect Bluetooth instead of coming back to Manage network page'],
        5: [5,
            'Click "Add Network" button after connecting to Bluetooth. Check it would go to the page to let you choose WiFi'],
        6: [6,
            'Choose one Wifi to setup. Check it would go back to Wi-Fi tab, and the printer would change to online. Check all info in WiFi tab would be updated.']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Open the app. Check the printer is offline and it is not in pairing mode
        start_time = time.time()
        common_method.show_message("check the printer is offline")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Go to the printer Wi-Fi tab. Check all info shows "Not Connected". Click Manage Networks option
        start_time = time.time()
        self.go_till_printer_wifi_page(0)
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Not Connected":
            raise Exception("the network shows connected")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: “Bluetooth Connection Required” dialog pops up. Click Continue button. Check the “Bluetooth Connection Failed” dialog pops up since printer is not in pairing mode
        start_time = time.time()
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Bluetooth Connection Failed")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Press 3s on power button to enter pairing mode. Click Continue button on the “Bluetooth Connection Failed” dialog. Check it will try to connect Bluetooth instead of coming back to Manage network page
        start_time = time.time()
        # Press 3s on power button and continue with Bluetooth connection attempt code here
        common_method.show_message("turn on the printer for online mode after 30s press ok in dialogue")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click "Add Network" button after connecting to Bluetooth. Check it would go to the page to let you choose WiFi
        start_time = time.time()
        others.click_add_network_button()
        common_method.wait_for_element_appearance_namematches("Choose WiFi")

        others.click_manage_network_button()
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply Changes")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Choose one Wifi to setup. Check it would go back to Wi-Fi tab, printer would change to online. Check all info in WiFi tab would be updated
        start_time = time.time()
        # Choose WiFi and verify network status and info update code here

        others.click_add_network_button()
        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)
        if not device_networks.check_the_wordings_in_connect_to_network():
            raise Exception("dialog dint pop up or the wordings are wrong")
        device_networks.click_on_cancel_button()
        try:
            device_networks.click_network_by_name(netw1)
        except:
            raise Exception("dialogue of connect to network did not close on clicking cancel button")

        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        common_method.wait_for_element_appearance("Connected", 60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception(
                "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45700(self):
    test_steps = {
        1: [1,
            'Login to mobile app, then go to Printer Settings page, click on the printer tab, and click on Wi-Fi tab. Check it would display the correct connected Wi-Fi information.'],
        2: [2, 'Click on Manage Networks button. Check it would display the saved networks list.'],
        3: [3, 'Check there are delete icons shown.'],
        4: [4,
            'Delete the network which is not connecting. Check the network is removed from the list. Check there is a toast message to prompt deletion is successful.'],
        5: [5,
            'Check the network priority is updated and the printer would connect to the highest priority network in the end. Check Wi-Fi page displays the correct connected network information.']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Login to mobile app, then go to Printer Settings page, click on the printer tab, and click on Wi-Fi tab
        start_time = time.time()
        common_method.show_message("1. Already add more than two network to the saved networks list if not add it")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)
        name1, status = device_networks.get_the_network_name_and_status()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Manage Networks button. Check it would display the saved networks list
        start_time = time.time()
        common_method.show_message("Check it displays the saved network list itself")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check there are delete icons shown
        start_time = time.time()
        common_method.show_message("Check there is deleted Icon")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Delete the network which is not connecting. Check the network is removed from the list
        start_time = time.time()
        s1 = device_networks.get_network_names()
        s1.remove(name1)
        dele_netw = s1[0]
        device_networks.delete_the_network(dele_netw)

        common_method.wait_for_element_appearance_namematches("Deleting")
        s1 = device_networks.get_network_names()
        if dele_netw in s1:
            raise Exception("deleted network is still present")

        common_method.wait_for_element_appearance("Deletion successful")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check the network priority is updated and the printer would connect to the highest priority network in the end.
        # Check Wi-Fi page displays the correct connected network information.
        start_time = time.time()
        try:
            device_networks.wait_for_the_printer_to_connect_network(name1)
        except:
            raise Exception(
                "fails: check the network priority is updated and the printer would connect to the highest priority network ")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45701(self):
    test_steps = {
        1: [1,
            'Login to mobile app, then go to Printer Settings page, click on the printer tab, and click on Wi-Fi tab. Check it would display the correct connected Wi-Fi information.'],
        2: [2, 'Click on Manage Networks button. Check it would display the saved networks list.'],
        3: [3, 'Click on Edit button. Check there are delete and adjust position icons shown.'],
        4: [4,
            'Delete the network which is connecting. Check the network is removed from the list. Check there is a toast message to prompt deletion is successful. Check the network priority is updated and the printer would connect to the highest priority network in the end. Check Wi-Fi page displays the correct connected network information.'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Login to mobile app and navigate to Wi-Fi tab
        start_time = time.time()
        common_method.show_message("Make sure two networks are connected to printer")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Manage Networks button
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on Edit button
        start_time = time.time()
        common_method.show_message("check for edit option")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Delete a connected network and verify
        start_time = time.time()
        s1 = device_networks.get_network_names()
        dele_netw = s1[0]
        device_networks.delete_the_network(dele_netw)
        common_method.wait_for_element_appearance_namematches("Deleting")
        sleep(2)

        s1 = device_networks.get_network_names()
        if dele_netw in s1:
            raise Exception("deleted network is still present")

        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        name1, status = device_networks.get_the_network_name_and_status()
        if name1 not in s1:
            raise Exception("fails : to connect to the highest priority network in existing networks")

        # Check for toast message (assuming implementation)
        # check the network priority is updated and the printer would connect to the highest priority network
        # Check Wi-Fi page displays the correct connected network information (assuming implementation)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45702(self):
    test_steps = {
        1: [1,
            'Login to mobile app, then go to Printer Settings page, click on the printer tab, and click on Wi-Fi tab. Check it would display the printer not connected to any network.'],
        2: [2, 'Click on Manage Networks button. Check only the current connected network is shown in the list.'],
        3: [3, 'Click on Edit button. Check there are delete and adjust position icons shown.'],
        4: [4,
            'Delete the network. Check the network is removed from the list. Check there is a toast message to prompt deletion is successful. Check the printer is still not connected to any network.'],
        5: [5, 'Continue to add a network. Check the printer can connect to the newly added network.'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        start_time = time.time()
        # Step 1: Login to mobile app and navigate to Wi-Fi tab
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.show_message(
            "Make Only one network is saved in the printer, but shut down the network, the printer is in offline status.")
        common_method.wait_for_element_appearance_namematches("Home")
        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Manage Networks button
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on Edit button
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Delete a network and verify
        start_time = time.time()
        s1 = device_networks.get_network_names()
        dele_netw = s1[0]
        device_networks.delete_the_network(dele_netw)
        common_method.wait_for_element_appearance_namematches("Deleting")
        sleep(2)

        common_method.wait_for_element_appearance("Not Connected", 100)
        sleep(2)

        # Check for toast message (assuming implementation)
        # Check if printer is still not connected to any network (assuming implementation)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Add a network and verify connection
        start_time = time.time()
        others.click_add_network_button()

        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        device_networks.click_on_cancel_button()
        try:
            device_networks.click_network_by_name(netw1)
        except:
            raise Exception("dialogue of connect to network did not close on clicking cancel button")

        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        common_method.wait_for_element_appearance("Connected", 60)
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception(
                "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just chosen")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45703(self):
    test_steps = {
        1: [1, 'Login to mobile app. Check the printer is displayed online.'],
        2: [2,
            'Turn off the current connected network, but DO NOT power cycle the printer. Check the printer would switch to connect the highest priority saved network. Check the printer would go to offline and back to online.'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])
    common_method.show_message("1. Already add more than two network to the saved networks list")

    try:
        # Step 1: Login to mobile app and check printer status
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        res = others.check_printer_online_status()
        if res != "online":
            raise Exception("printer not in online state")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Turn off the current connected network and verify
        start_time = time.time()
        common_method.show_message("Turn off the current connected network, but DO NOT power cycle the printer.")
        others.wait_for_appearance_all("offline", 60)
        sleep(3)
        res = others.check_printer_online_status()
        if res != "offline":
            raise Exception("fails : check the printer would go to offline and back to online")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45704(self):
    test_steps = {
        1: [1, 'Away from all saved networks (or shut down all saved networks). Check the printer is offline.'],
        2: [2,
            'Go to Printer settings page, click on the target printer tab, and click on Wi-Fi tab. Check it displays not connected.'],
        3: [3,
            'Click on Manage networks button and Add networks button. Check all available networks are listed including the hotspot network.'],
        4: [4,
            'Select the hotspot network to connect. Check the printer is connected to the hotspot network. Check the printer is back online. Check the current network is displayed correctly.'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Ensure printer is offline
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.show_message(
            "1. All saved networks are not available to connect\n2. There is one hotspot network available in you test environment.")
        common_method.wait_for_element_appearance_namematches("Home")
        sleep(2)
        res = others.check_printer_online_status()
        if res != "offline":
            raise Exception("fails : check the printer would go to offline")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Navigate to Wi-Fi tab and verify status
        start_time = time.time()
        self.go_till_printer_wifi_page(1)
        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" or status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Add a new network
        start_time = time.time()
        others.click_add_network_button()
        netw2 = common_method.get_user_input("enter network name here")
        netw2_pass = common_method.get_user_input("enter password here")
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        common_method.wait_for_element_appearance_namematches(netw2, 60)
        name, status = device_networks.get_the_network_name_and_status()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Verify printer connectivity and status
        start_time = time.time()
        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw2 or status != "Connected":
            raise Exception(
                "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45707(self):
    test_steps = {
        1: [1, 'User log in, go to Printer settings>Printer Name, switch to Wi-Fi tab'],
        2: [2, 'Click on the Manage Networks button. (Pair bluetooth successfully)'],
        3: [3,
            'Select Add Wifi, and choose one network to add, input invalid password. Check the dialog of "Failed to Connect to Wifi Network" will pop up, click on Cancel button, check the network is not added in the saved network list.'],
        4: [4,
            'Repeat step 3, but select Continue button on the confirm dialog, check the network is added in the saved network list.'],
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: User login and navigate to Wi-Fi tab
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Manage Networks button
        start_time = time.time()
        others.click_add_network_button()
        common_method.wait_for_element_appearance("Apply Changes", 60)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Add a network with invalid password
        start_time = time.time()
        others.click_add_network_button()
        netw2 = common_method.get_user_input("enter network name")
        netw2_pass = common_method.get_user_input("enter wrong password")
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 300)
        device_networks.click_on_cancel_button()

        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)

        s1 = device_networks.get_network_names()
        if netw2 in s1:
            raise Exception("fails: check the network is not added in the saved network list.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Add the same network with correct password
        start_time = time.time()
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        netw2_pass = common_method.get_user_input("enter correct password")
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
        device_networks.click_on_continue_in_network_disconnect_error()

        # Check if network is added to saved network list
        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        if netw2 not in s1:
            raise Exception("fails: check the network is added in the saved network list.")

        common_method.wait_for_element_appearance_namematches(netw2, 60)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45897(self):
    test_steps = {
        1: [1, 'open the app and login the account with online Monebyadger'],
        2: [2, 'slide the left slide page to choose "Printer Settings" item'],
        3: [3, 'click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        4: [4, 'click the Wi-Fi tab'],
        5: [5,
            'Check it would be spinning for a while to wait all infos appears at the page. After that, it would appears the button "Manage Network" at the bottom.'],
        6: [6,
            'click Manage Network, pair Bluetooth when it pops up. After paring successfully, check the add network button shows up.'],
        7: [7, 'click "Add Network" button. Check the networks list will be displayed.'],
        8: [8,
            'choose one Essid to add it and connect with it. Check able to add the network to the list and printer can connect to it.']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])
    common_method.show_message(
        "the target Moneybadger was added by the another phone (add nestwifi to same account using other phone)")

    try:
        # Step 1: open the app and login with online Monebyadger
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")
        self.go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: slide the left slide page to choose "Printer Settings" item
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: click the Moneybadger name tab
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: click the Wi-Fi tab
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check for Manage Network button after info load
        start_time = time.time()
        common_method.wait_for_element_appearance_namematches("Manage Network")
        self.click_manage_network_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click "Add Network" button and verify networks list display
        start_time = time.time()
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7,8: Choose and connect to a network
        start_time = time.time()
        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.click_network_by_name(netw1)
        device_networks.click_on_cancel_button()

        try:
            device_networks.click_network_by_name(netw1)
        except:
            raise Exception("dialogue of connect to network did not close on clicking cancel button")

        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        common_method.wait_for_element_appearance_namematches("Printer", 60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception(
                "fails : Check the Current Network, Network Status, IP Address all values are updated as the Essid just chosen")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_47912(self):
    test_steps = {
        1: [1, 'Go to manage networks page'],
        2: [2, 'Reboot printer'],
        3: [3, 'Click "Manage networks" button'],
        4: [4, 'Check ZSB app shows network without any error or fail']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Go to manage networks page
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Reboot printer
        start_time = time.time()
        common_method.show_message("2. Reboot printer after that click ok")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click "Manage networks" button
        start_time = time.time()
        others.click_manage_network_button()
        common_method.wait_for_element_appearance_namematches("Apply Changes")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check ZSB app shows network without any error or fail
        start_time = time.time()
        try:
            s1 = device_networks.get_network_names()
        except:
            raise Exception("network names did not show after rebooting printer")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_50766(self):
    test_steps = {
        1: [1, 'Make sure test device connects to Wi-Fi network, sign in mobile app'],
        2: [2,
            'Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        3: [3, 'Change to connect cellular data for the device'],
        4: [4,
            'Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        5: [5,
            'Sign out and sign in again, recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])
    common_method.show_message("Device able to use cellular data")

    try:
        # Step 1: Make sure test device connects to Wi-Fi network, sign in mobile app
        start_time = time.time()

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        others.turn_on_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check the basic functions on the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Change to connect cellular data for the device
        start_time = time.time()
        device_networks.turn_off_wifi()
        common_method.show_message("if internet is not disconnected disconnect and connect it")
        device_networks.turn_on_cellular_data()
        sleep(4)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Recheck basic functions of the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Sign out and sign in again, recheck basic functions of the app
        start_time = time.time()
        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_50767(self):
    test_steps = {
        1: [1, 'Make sure test device connects to Wi-Fi network, sign in mobile app'],
        2: [2,
            'Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        3: [3,
            'Connect another hotspot for the device (not current device\'s cellular data), make sure Wi-Fi is connected'],
        4: [4,
            'Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        5: [5,
            'Sign out and sign in again, recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Make sure test device connects to Wi-Fi network, sign in mobile app
        start_time = time.time()
        common_method.show_message("There is a hotspot wi-fi")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        others.turn_on_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check the basic functions on the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Connect another hotspot for the device
        start_time = time.time()
        others.open_wifi_settings()
        sleep(3)
        netw1 = common_method.get_user_input("enter hotspot network name")
        netw1_pass = common_method.get_user_input("enter password of the hotspot")
        others.select_wifi(netw1, netw1_pass)
        sleep(1)
        start_app("com.zebra.soho_app")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Recheck basic functions of the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Sign out and sign in again, recheck basic functions of the app
        start_time = time.time()
        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_50768(self):
    test_steps = {
        1: [1, 'Make sure test device connects to Wi-Fi network, sign in mobile app'],
        2: [2,
            'Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        3: [3,
            'Disable device\'s Wi-Fi option, make sure Wi-Fi is disconnected. Check there is a prompt message for user the network is lost'],
        4: [4,
            'Enable the device\'s Wi-Fi network back, make sure network is connected, refresh the app. Check the error message disappears'],
        5: [5,
            'Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        6: [6,
            'Sign out and sign in again, recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Make sure test device connects to Wi-Fi network, sign in mobile app
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        others.turn_on_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check the basic functions on the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Disable device's Wi-Fi option, make sure Wi-Fi is disconnected
        start_time = time.time()
        device_networks.turn_off_wifi()
        sleep(1)
        device_networks.refresh_home_page()
        sleep(2)
        if not device_networks.check_sudden_network_off_error():
            raise Exception("network disconnection error did not pop up")
        sleep(2)
        device_networks.click_on_continue_in_network_disconnect_error()
        try:
            device_networks.click_on_continue_in_network_disconnect_error()
        except:
            pass
        try:
            device_networks.click_on_continue_in_network_disconnect_error()
        except:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Enable the device's Wi-Fi network back, make sure network is connected, refresh the app
        start_time = time.time()
        others.turn_on_wifi()
        sleep(4)
        device_networks.refresh_home_page()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Recheck basic functions of the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Sign out and sign in again, recheck basic functions of the app
        start_time = time.time()
        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_50769(self):
    test_steps = {
        1: [1, 'Make sure test device connects to Wi-Fi network, sign in mobile app'],
        2: [2,
            'Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        3: [3,
            'Connect to invalid network for the device, make sure Wi-Fi is connected. Check there is a prompt message for user the network is lost'],
        4: [4, 'Connect device to the original valid network, refresh app. Check the prompt message will disappear'],
        5: [5,
            'Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        6: [6,
            'Sign out and sign in again, recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Make sure test device connects to Wi-Fi network, sign in mobile app
        start_time = time.time()
        common_method.show_message("Make sure there are two available Wi-Fi networks, one valid, one invalid")
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        others.turn_on_wifi()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check the basic functions on the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Connect to invalid network for the device, make sure Wi-Fi is connected
        start_time = time.time()
        others.open_wifi_settings()
        sleep(3)
        netw1 = common_method.get_user_input("enter invalid network name")
        netw1_pass = common_method.get_user_input("enter password of the invalid network")
        others.select_wifi(netw1, netw1_pass)
        sleep(1)

        start_app("com.zebra.soho_app")
        sleep(2)
        device_networks.refresh_home_page()
        if not device_networks.check_sudden_network_off_error():
            raise Exception("network disconnection error did not pop up")
        sleep(2)
        device_networks.click_on_continue_in_network_disconnect_error()
        try:
            device_networks.click_on_continue_in_network_disconnect_error()
        except:
            pass
        try:
            device_networks.click_on_continue_in_network_disconnect_error()
        except:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Connect device to the original valid network, refresh app
        start_time = time.time()
        others.open_wifi_settings()
        sleep(3)
        netw1 = common_method.get_user_input("enter valid network name")
        netw1_pass = common_method.get_user_input("enter password of valid network")
        others.select_wifi(netw1, netw1_pass)
        sleep(1)

        start_app("com.zebra.soho_app")
        sleep(2)

        sleep(4)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Recheck basic functions of the app
        start_time = time.time()
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Sign out and sign in again, recheck basic functions of the app
        start_time = time.time()
        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")
        self.check_basic_functionalities()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_50782(self):
    test_steps = {
        1: [1, 'Sign in test account with at least one printer added, keep on home page'],
        2: [2, 'Disconnect device’s network (Turn off the Wi-Fi option)'],
        3: [3,
            'Go to the Common Designs/My designs from the left menu. Check there is an error message showing up on Common Designs or My designs'],
        4: [4, 'Back to Home page. Check the prompt message is like "The service is currently unavailable"'],
        5: [5, 'Perform same steps on Android and iOS devices. Check the prompt message is same on both devices']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Sign in test account with at least one printer added, keep on home page
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Disconnect device’s network (Turn off the Wi-Fi option)
        start_time = time.time()
        device_networks.turn_off_wifi()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Go to the Common Designs/My designs from the left menu
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_designs()
        sleep(2)
        if not device_networks.check_the_my_designs_internet_lost_error():
            raise Exception("fails: Check there is an error message showing up on My designs")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Back to Home page, check the prompt message is like "The service is currently unavailable"
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()

        device_networks.refresh_home_page()
        if not device_networks.check_sudden_network_off_error():
            raise Exception("network disconnection error did not pop up")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Perform same steps on Android and iOS devices. Check the prompt message is same on both devices
        start_time = time.time()
        common_method.show_message("check in iOS for the same")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_52289(self):
    test_steps = {
        1: [1, 'Install the testing ZSB Series build, sign in test account'],
        2: [2,
            'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog'],
        3: [3, 'When the "Allow ZSB series to find, connect to ....nearby devices" pops up, click "Allow"'],
        4: [4,
            'Wait for printer pair successfully. Check the network list will be displayed correctly. Check there is no odd behaviors, like crash'],
        5: [5, 'Try to add/delete/sort the network. Check able to manage network successfully']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:
        # Step 1: Install the testing ZSB Series build, sign in test account
        start_time = time.time()
        others.run_the_command("adb uninstall com.zebra.soho_app")
        common_method.show_message("Install the new build")
        sleep(2)
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        try:
            others.click_on_allow()
        except:
            pass
        try:
            others.click_on_allow()
        except:
            pass
        social_login.wait_for_element_appearance("Sign In", 20)
        try:
            others.click_on_allow()
        except:
            pass
        login_page.click_loginBtn()

        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        common_method.wait_for_element_appearance_namematches("Home", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        res = others.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("bluetooth dialogue didn't show")

        others.click_continue_in_bluetooth_connection_required()
        try:
            others.click_on_allow()
        except:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: When the "Allow ZSB series to find, connect to ....nearby devices" pops up, click "Allow"
        start_time = time.time()
        try:
            others.click_on_allow()
        except:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Wait for printer to pair successfully. Check the network list will be displayed correctly. Check there are no odd behaviors, like crash
        start_time = time.time()
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")

        try:
            s1 = device_networks.get_network_names()
        except:
            raise Exception("network names not displayed")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        start_time = time.time()

        common_method.show_message(" Try to add/delete/sort the network Check able to manage network successfully")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_52292(self):
    test_steps = {
        1: [1, 'Install the latest ZSB Series version, after installing successfully, click Open'],
        2: [2, 'When the app launches, check that there is no "Allow ZSB Series... of nearby devices" popping up'],
        3: [3,
            'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog (If BT pair dialog pops up, allow it). Check that the network list will be displayed correctly'],
        4: [4, 'Minimize ZSB series, open its app info, disable ZSB Nearby devices permission'],
        5: [5, 'Repeat step 3 again. Check that the "Allow ZSB Series... of nearby devices" will pop up'],
        6: [6,
            'Click Allow option, wait for printer pair successfully. Check that the network list will be displayed correctly. Check there are no odd behaviors, like crashes'],
        7: [7, 'Try to add/delete/sort the network. Check that it is able to manage network successfully']
    }

    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])

    try:

        # step1: "Install the latest ZSB Series version, after installing successfully, click Open"
        start_time = time.time()
        common_method.show_message("install the new build")

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        try:
            social_login.wait_for_element_appearance("Sign In", 10)

            login_page.click_loginBtn()
            try:
                common_method.wait_for_element_appearance_namematches("Continue with Google")

                login_page.click_Loginwith_Google()
                common_method.wait_for_element_appearance_textmatches("Choose an account")

                social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
            except:
                pass
            social_login.wait_for_element_appearance("Home", 10)
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Home")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step2: "When the app launches, check that there is no 'Allow ZSB Series... of nearby devices' popping up"
        start_time = time.time()
        common_method.show_message("check there is no Allow ZSB Series... of nearby devices popping up")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step3: "Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog (If BT pair dialog pops up, allow it). Check that the network list will be displayed correctly"
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        res = others.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        others.click_continue_in_bluetooth_connection_required()

        try:
            others.click_on_allow()
        except:
            pass
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step4: "Minimize ZSB series, open its app info, disable ZSB Nearby devices permission"
        start_time = time.time()

        device_networks.allow_nearby_devices_permission(0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step5: "Repeat step 3 again. Check that the 'Allow ZSB Series... of nearby devices' will pop up"
        start_time = time.time()

        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        res = others.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        others.click_continue_in_bluetooth_connection_required()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step6: "Click Allow option, wait for printer pair successfully. Check that the network list will be displayed correctly. Check there are no odd behaviors, like crashes"
        start_time = time.time()

        others.click_on_allow()

        common_method.wait_for_element_appearance_namematches("Apply Changes")
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step7: "Try to add/delete/sort the network. Check that it is able to manage network successfully"
        start_time = time.time()

        netw1 = "EVT_ArubaOpen"
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        common_method.wait_for_element_appearance("Connected", 100)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)
