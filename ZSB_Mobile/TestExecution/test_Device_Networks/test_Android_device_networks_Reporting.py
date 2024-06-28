#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others.Others import Others
from ZSB_Mobile.Common_Method import *
from ZSB_Mobile.PageObject.Social_Login.Social_Login import Social_Login
# from ZSB_Mobile.sphere_db import *
from ZSB_Mobile.PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android

import os
import logging
from ...TestSuite.api_calls import *
import inspect
from ...TestSuite.store import *


logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method=Common_Method(poco)
social_login = Social_Login(poco)
device_networks = Device_Networks_Android(poco)
#
# """EXECID and LEFTID need to be changed"""
# execID=0
# leftId = {}

def go_till_printer_wifi_page(self=0,add_network=0):
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.click_wifi_button()
    if add_network:
        others.click_manage_network_button()
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply Changes")

def t_100(self,add_network=0):
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.click_wifi_button()
    if add_network:
        others.click_manage_network_button()
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply Changes")

def test_Device_Networks_TestcaseID_45706(self):

    test_steps = {
        1: [1, 'User logs in, goes to Printer settings>Printer Name, switches to Wi-Fi tab'],
        2: [2, 'Clicks on the Manage Networks button. (Pairs Bluetooth successfully)'],
        3: [3, 'When the saved network lists show up, delete all the networks'],
        4: [4, 'Check if all the networks are deleted, all the statuses will be Not Connected (Current Network/Network Status/IP Address)'],
        5: [5, 'Check it can manage networks again, can add networks after deleting all networks']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: User logs in, goes to Printer settings>Printer Name, switches to Wi-Fi tab
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Clicks on the Manage Networks button. (Pairs Bluetooth successfully)
        start_time = time.time()
        s1 = device_networks.get_network_names()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: When the saved network lists show up, delete all the networks
        start_time = time.time()
        for i in range(len(s1)):
            dele_netw = s1[i]
            device_networks.delete_the_network(dele_netw)
            common_method.wait_for_element_appearance_namematches("Deleting")
            sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Check if all the networks are deleted, all the statuses will be Not Connected (Current Network/Network Status/IP Address)
        start_time = time.time()
        try:
            s1 = device_networks.get_network_names()
            raise Exception("all the networks did not get deleted")
        except ZeroDivisionError:
            pass

        common_method.wait_for_element_appearance("Not Connected")
        name, status = device_networks.get_the_network_name_and_status()

        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Check it can manage networks again, can add networks after deleting all networks
        start_time = time.time()
        others.click_add_network_button()

        netw2 = "NESTWIFI"
        netw2_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)

        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()
        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        common_method.wait_for_element_appearance_namematches(netw2, 60)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_45693(self):
    test_steps = {
        1: [1, 'Slide the left slide page to choose "Printer Settings" item'],
        2: [2, 'Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        3: [3, 'Click the Wi-Fi tab and wait for all info to appear'],
        4: [4, 'Check the Current Network, Network Status, IP Address, and My saved Networks info'],
        5: [5, 'Click "Add Network" button and choose an open Essid'],
        6: [6, 'Check it goes back to the Wi-Fi tab and updates the network info']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Slide the left slide page to choose "Printer Settings" item
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Click the Wi-Fi tab and wait for all info to appear
        start_time = time.time()
        name, status = device_networks.get_the_network_name_and_status()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Check the Current Network, Network Status, IP Address, and My saved Networks info
        start_time = time.time()
        if name != "NESTWIFI" or status != "Connected":
            raise Exception("fails: Check the Current Network, Network Status, info all are correct.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Click "Add Network" button and choose an open Essid
        start_time = time.time()
        others.click_add_network_button()
        netw1 = "aruba-ap"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        others.wait_for_appearance_all("offline", 20)

        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        exec_time = (time.time() - start_time) / 60

        try:
            others.wait_for_appearance_all("online", 60)
        except:
            raise Exception("Printer is online pop up didn't show up")

        common_method.wait_for_element_appearance_namematches("Connected", 60)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 6: Check it goes back to the Wi-Fi tab and updates the network info
        start_time = time.time()
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception(
                "fails: check Current Network, Network Status, IP Address all values are updated as the Essid just chosen")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_45694(self):
    test_steps = {
        1: [1, 'Slide the left slide page to choose "Printer Settings" item'],
        2: [2, 'Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
        3: [3,
            'Click the Wi-Fi tab, then click "Manage networks" button, after the network list loaded, click on "Add network" button'],
        4: [4, 'Choose WPA PSK Essid'],
        5: [5, 'Click "Cancel" button and verify dialog is dismissed'],
        6: [6, 'Choose WPA PSK Essid again and verify dialog appears'],
        7: [7, 'Input the correct password, click "Submit", verify network info is updated']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Slide the left slide page to choose "Printer Settings" item
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Click the Wi-Fi tab, then click "Manage networks" button, after the network list loaded, click on "Add network" button
        start_time = time.time()
        go_till_printer_wifi_page(1)

        others.click_add_network_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Choose WPA PSK Essid
        start_time = time.time()

        netw1 = "POCO M3"
        netw1_pass = "1234567890"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        if not device_networks.check_the_wordings_in_connect_to_network():
            raise Exception("dialog didn't pop up or the wordings are wrong")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Click "Cancel" button and verify dialog is dismissed
        start_time = time.time()
        device_networks.click_on_cancel_button()
        try:
            device_networks.click_network_by_name(netw1)
        except:
            raise Exception("dialogue of connect to network did not close on clicking cancel button")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 6: Choose WPA PSK Essid again and verify dialog appears
        start_time = time.time()
        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 7: Input the correct password, click "Submit", verify network info is updated
        start_time = time.time()
        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        common_method.wait_for_element_appearance_namematches("Connected", 60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception(
                "fails: check Current Network, Network Status, IP Address all values are updated as the Essid just chosen")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_47943(self):
    test_steps = {
        1: [1, 'Start with the printer connected to an iPhone hotspot - Pink iPhone'],
        2: [2, 'Go to Printer Settings/Manage network'],
        3: [3, 'Add a Wi-Fi access point (Koala) successfully and check for Offline and Online toast messages'],
        4: [4, 'Check the "Current Network" and "IP Address" updated accordingly']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Start with the printer connected to an iPhone hotspot - Pink iPhone
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Go to Printer Settings/Manage network
        start_time = time.time()
        others.click_add_network_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Add a Wi-Fi access point (Koala) successfully and check for Offline and Online toast messages
        start_time = time.time()
        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)
        if not device_networks.check_the_wordings_in_connect_to_network():
            raise Exception("dialog didn't pop up or the wordings are wrong")

        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Check the "Current Network" and "IP Address" updated accordingly
        start_time = time.time()
        name, status = device_networks.get_the_network_name_and_status()
        if name != "Not Connected" and status != "Not Connected":
            raise Exception("network and status did not get Not Connected")

        common_method.wait_for_element_appearance_namematches("Connected", 60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception(
                "fails: check Current Network, Network Status, IP Address all values are updated as the Essid just chosen")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



# def test_Device_Networks_TestcaseID_45693(self):
#     stop_app("com.zebra.soho_app")
#     start_app("com.zebra.soho_app")
#     common_method.wait_for_element_appearance_namematches("Home")
#
#     go_till_printer_wifi_page(1)
#
#     others.click_add_network_button()
#     netw1 = "aruba-ap"
#     device_networks.wait_till_the_networks_list()
#     device_networks.click_network_by_name(netw1)
#
#     try:
#         common_method.wait_for_element_appearance_namematches("Printer")
#     except:
#         raise Exception("did not redirect to the previous page")
#     others.wait_for_appearance_all("offline",20)
#     name,status = device_networks.get_the_network_name_and_status()
#     if name!="Not Connected" and status!="Not Connected":
#         raise Exception("network and status did not get Not Connected")
#     try:
#         others.wait_for_appearance_all("online",60)
#     except:
#         raise Exception("Printer is online pop up dint shown up")
#
#     common_method.wait_for_element_appearance_namematches("Connected",60)
#     name, status = device_networks.get_the_network_name_and_status()
#     if status != "Connected":
#         raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")


def test_Device_Networks_TestcaseID_45708(self):

    test_steps = {
        1: [1, 'User logs in, goes to Printer settings>Printer Name, switches to Wi-Fi tab'],
        2: [2, 'Clicks on the Manage Networks button. (Pairs Bluetooth successfully)'],
        3: [3, 'Clicks on the Add Network button, selects the network which is already in the saved list to add.'],
        4: [4, 'Check it will not be added again, and prompt "Printer is already connected to this network" will pop up']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: User logs in, goes to Printer settings>Printer Name, switches to Wi-Fi tab
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Clicks on the Manage Networks button. (Pairs Bluetooth successfully)
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Clicks on the Add Network button, selects the network which is already in the saved list to add.
        start_time = time.time()

        others.click_add_network_button()

        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)
        if not device_networks.check_the_wordings_in_connect_to_network():
            raise Exception("dialog didn't pop up or the wordings are wrong")
        device_networks.click_on_cancel_button()
        try:
            device_networks.click_network_by_name(netw1)
        except:
            raise Exception("dialogue of connect to network did not close on clicking cancel button")

        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Check it will not be added again, and prompt "Printer is already connected to this network" will pop up
        start_time = time.time()
        try:
            common_method.wait_for_element_appearance_namematches("Printer is already connected to this network.")
        except:
            raise Exception("fails: Printer is already connected to this network pop up")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45698(self):

    test_steps = {
        1: [1, 'Open the app and login'],
        2: [2, 'Slide left slide page to choose "printer settings"'],
        3: [3, 'Click the target Moneybadger tab'],
        4: [4, 'Click the Wi-Fi tab'],
        5: [5, 'Click "add network" button to add the Essid B and check the hint display "adding Essid B Check the Moneybadger would reset and it would still connect to Essid A,Check the network name list would display: Essid A and Essid B']
    }


    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Open the app and login
        start_time = time.time()
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Slide left slide page to choose "printer settings"
        start_time = time.time()
        go_till_printer_wifi_page(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Click the target Moneybadger tab
        start_time = time.time()


        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Click the Wi-Fi tab
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Click "add network" button to add the Essid B and check the hint display "adding Essid B"
        start_time = time.time()

        name1, status = device_networks.get_the_network_name_and_status()
        s1 = device_networks.get_network_names()
        others.click_add_network_button()

        name1, status = device_networks.get_the_network_name_and_status()
        s1 = device_networks.get_network_names()
        others.click_add_network_button()
        netw1 = "EVT_ArubaOpen"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        common_method.wait_for_element_appearance("Connected", 200)
        name, status = device_networks.get_the_network_name_and_status()
        if name != name1:
            raise Exception("fails: check the Moneybadger would reset and it would still connect to Essid A")

        s2 = device_networks.get_network_names()
        if netw1 not in s2 or len(s1) + 1 != len(s2):
            raise Exception('newly added network is not present')

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)



    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_Device_Networks_TestcaseID_45807(self):
    test_steps = {
        1: [1, 'Login Mobile app'],
        2: [2, 'Home page displayed, click common design, all category list out'],
        3: [3, 'Go mobile device settings > wifi, select a different wifi to connect'],
        4: [4, 'After new wifi network connected, switch to Mobile App'],
        5: [5, 'Click home to show home page. Check Home page show up with printer and Recently printed labels list'],
        6: [6, 'Repeat step 3-4, then open Common Design/My Design/My Data']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Login Mobile app
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 2: Home page displayed, click common design, all category list out
        start_time = time.time()
        recently_printed_labels_before = others.get_recently_printed_labels()
        login_page.click_Menu_HamburgerICN()
        others.click_common_designs_button()
        sleep(2)
        netw_1_common_designs = others.get_designs_visible_designs()
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_designs()
        common_method.wait_for_element_appearance_namematches("Showing")
        netw_1_my_designs = others.get_designs_visible_designs()
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_data()
        sleep(2)
        netw_1_my_data = others.get_my_data_all()
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Go mobile device settings > wifi, select a different wifi to connect
        start_time = time.time()
        others.open_wifi_settings()
        sleep(3)
        others.select_wifi("POCO M3", "1234567890")
        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: After new wifi network connected, switch to Mobile App
        start_time = time.time()
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        sleep(2)
        res = others.check_home_page()
        if not res:
            raise Exception("Home page not shown")
        recently_printed_labels_after = others.get_recently_printed_labels()
        res = others.check_same_after_switching_network(recently_printed_labels_before, recently_printed_labels_after)
        if not res:
            print("Changing network not showing files properly")
        sleep(4)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Click home to show home page. Check Home page show up with printer and Recently printed labels list
        start_time = time.time()
        others.open_wifi_settings()
        others.select_wifi("ZGuest", "1234567890")
        sleep(1)
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_common_designs_button()
        sleep(2)
        netw_2_common_designs = others.get_designs_visible_designs()
        res = others.check_same_after_switching_network(netw_1_common_designs, netw_2_common_designs)
        if not res:
            print("Changing network not showing files properly")
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 6: Repeat step 3-4, then open Common Design/My Design/My Data
        start_time = time.time()
        others.open_wifi_settings()
        sleep(1)
        others.select_wifi("POCO M3", "1234567890")
        sleep(1)
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_designs()
        common_method.wait_for_element_appearance_namematches("Showing")
        netw_2_my_designs = others.get_designs_visible_designs()
        res = others.check_same_after_switching_network(netw_1_my_designs, netw_2_my_designs)
        if not res:
            print("Changing network not showing files properly")
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        others.open_wifi_settings()
        sleep(1)
        others.select_wifi("ZGuest", "1234567890")
        sleep(1)
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_data()
        sleep(2)
        netw_2_my_data = others.get_my_data_all()
        res = others.check_same_after_switching_network(netw_1_my_data, netw_2_my_data)
        if not res:
            print("Changing network not showing files properly")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_46963(self):
    test_steps = {
        1: 'In home page click main menu and select printer settings',
        2: 'Go target printer > Wi-Fi Tab',
        3: 'Click Manage Network button under Wi-Fi tab, check Bluetooth Connection Required dialog pop up',
        4: 'Click continue Button on the dialog, check bluetooth pairing request pop, click pair on the dialog',
        5: 'After printer pair done, it show manage network page success and not error occurs (Step 1 go network page pass)',
        6: 'Click Add network button, check available network list show up, select a network or manually enter a network to connect',
        7: 'Click main menu and go home page',
        8: 'Click main menu > Printer Settings > target printer > Wi-Fi tab',
        9: 'Click manage Network and click continue button on Bluetooth Connection Required dialog with continue and cancel button, check it show manage network page successfully (Step 3 Re-enter Manage Network pass)',
        10: 'Press the second network and move to the top of the network list, check Apply Changes button is able to click',
        11: 'Click Apply changes button, check apply success, apply change button change to disable (Step 4: Resort network pass)',
        12: 'Click the delete icon on any one of the network, check network will be deleted and not show in network list (Step 5: Delete network pass)',
        13: 'Go home page'
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: In home page click main menu and select printer settings
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 1, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 2: Go target printer > Wi-Fi Tab
        start_time = time.time()
        others.select_first_printer()
        others.click_wifi_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 2, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 3: Click Manage Network button under Wi-Fi tab, check Bluetooth Connection Required dialog pop up
        start_time = time.time()
        others.click_manage_network_button()
        res = others.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("Bluetooth dialog did not show")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 3, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 4: Click continue Button on the dialog, check bluetooth pairing request pop, click pair on the dialog
        start_time = time.time()
        others.click_continue_in_bluetooth_connection_required()
        try:
            others.click_on_allow()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Apply", 20)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 4, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 5: After printer pair done, it show manage network page success and not error occurs
        start_time = time.time()
        others.scroll_down()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 5, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 6: Click Add network button, check available network list show up, select a network or manually enter a network to connect
        start_time = time.time()
        others.click_add_network_button()
        common_method.wait_for_element_appearance_namematches("Network")
        sleep(5)
        network2 = "NESTWIFI"
        password = "123456789"
        others.select_network_and_enter_password(network2, password)
        try:
            others.click_enter_network_manually()
            others.enter_network_name(network2)
            others.click_join_network()
        except:
            pass
        sleep(3)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 6, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 7: Click main menu and go home page
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 7, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 8: Click main menu > Printer Settings > target printer > Wi-Fi tab
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 8, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 9: Click manage Network and click continue button on Bluetooth Connection Required dialog with continue and cancel button
        start_time = time.time()
        others.click_manage_network_button()
        res = others.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("Bluetooth dialog did not show")
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 9, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 10: Press the second network and move to the top of the network list, check Apply Changes button is able to click
        start_time = time.time()
        others.scroll_down()
        res, res1 = others.get_network_names()
        others.swap_two_networks(res1[1], res1[0])
        res = others.check_apply_changes_button_clickable()
        if not res:
            raise Exception("Apply changes button not clickable")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 10, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 11: Click Apply changes button, check apply success, apply change button change to disable
        start_time = time.time()
        others.click_apply_changes_button()
        sleep(5)
        res = others.check_apply_changes_button_clickable()
        if res:
            raise Exception("Apply changes button still clickable")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 11, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 12: Click the delete icon on any one of the network, check network will be deleted and not show in network list
        start_time = time.time()
        res, res1 = others.get_network_names()
        others.delete_one_network(res1[0])
        common_method.wait_for_element_appearance_namematches("Apply")
        sleep(2)
        try:
            common_method.wait_for_element_appearance_namematches(res1[0])
            raise Exception("Network did not get deleted")
        except:
            pass
        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 12, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 13: Go home page
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["46963"], 13, stepId, test_steps[stepId], "Pass", exec_time)

    except Exception as e:
        insert_step(execID, leftId["46963"], stepId, stepId, test_steps[stepId], "Fail", 0)
        raise Exception(str(e))


def test_Device_Networks_TestcaseID_47794(self):
    test_steps = {
        1: 'Open the app and ensure Sign In screen is displayed',
        2: 'Logout if already logged in and return to Sign In screen',
        3: 'Log in with Google account',
        4: 'Close the app',
        5: 'Turn off Wi-Fi on the device',
        6: 'Re-open the app and check for internet disconnect error',

    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Open the app and ensure Sign In screen is displayed
        start_time = time.time()
        try:
            common_method.wait_for_element_appearance_namematches("Sign In")
        except:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 1, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 2: Logout if already logged in and return to Sign In screen
        start_time = time.time()
        try:
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 2, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 3: Log in with Google account
        start_time = time.time()
        login_page.click_loginBtn()
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        social_login.wait_for_element_appearance("Home", 10)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 3, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 4: Close the app
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 4, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 5: Turn off Wi-Fi on the device
        start_time = time.time()
        device_networks.turn_off_wifi()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 5, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        # Step 6: Re-open the app and check for internet disconnect error
        start_time = time.time()
        start_app("com.zebra.soho_app")
        if not device_networks.check_internet_disconnect_error():
            raise Exception("Internet disconnection error did not pop up")
        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId["47794"], 6, stepId, test_steps[stepId], "Pass", exec_time)
        stepId += 1

        others.turn_on_wifi()
        sleep(1)

    except Exception as e:
        insert_step(execID, leftId["47794"], stepId, stepId, test_steps[stepId], "Fail", 0)
        raise Exception(str(e))

def check_basic_functionalities(self=0):
    """printing test label"""
    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.click_test_print()
    try:
        others.wait_for_appearance_all("Print Complete")
        sleep(2)
    except:
        pass

    others.change_Printer_Darkness_level(70)
    others.change_Printer_Darkness_level(50)
    others.wait_for_appearance_all("updated")
    sleep(2)

    login_page.click_Menu_HamburgerICN()
    others.click_common_designs_button()
    others.wait_for_appearance_all("Address")

    login_page.click_Menu_HamburgerICN()
    others.click_on_my_designs()
    others.wait_for_appearance_all("My Designs")

    login_page.click_Menu_HamburgerICN()
    others.click_home_button()

def logout_from_the_app(self=0):
    try:
        login_page.click_Menu_HamburgerICN()
    except:
        pass

    others.click_on_profile_edit()
    others.click_log_out_button()
    common_method.wait_for_element_appearance_namematches("Sign In")


def test_Device_Networks_TestcaseID_52290(self):
    test_steps = {
        1: [0, 'Sign in to the test account'],
        2: [1,
            'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog'],
        3: [2, 'Minimize ZSB series, open its app info, disable ZSB Nearby devices permission'],
        4: [3, 'Repeat step 2 and check if it asks for nearby devices permission'],
        5: [4, 'Allow ZSB series to find, connect to nearby devices when the dialog pops up'],
        6: [5, 'Wait for the printer to pair successfully and check the network list'],
        7: [6, 'Try to add/delete/sort the network and check if able to manage networks successfully']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:
        # Step 1: Sign in to the test account
        start_time = time.time()
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

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
            raise Exception("Bluetooth dialogue didn't show")

        others.click_continue_in_bluetooth_connection_required()

        try:
            others.click_on_allow()
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Apply Changes")
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("No network is connected to the device")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 3: Minimize ZSB series, open its app info, disable ZSB Nearby devices permission
        start_time = time.time()
        device_networks.allow_nearby_devices_permission(0)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 4: Repeat step 2 and check if it asks for nearby devices permission
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
            raise Exception("Bluetooth dialogue didn't show")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 5: Allow ZSB series to find, connect to nearby devices when the dialog pops up
        start_time = time.time()
        others.click_continue_in_bluetooth_connection_required()
        others.click_on_allow()
        common_method.wait_for_element_appearance_namematches("Apply Changes")
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("No network is connected to the device")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # Step 6: Wait for the printer to pair successfully and check the network list
        start_time = time.time()
        netw1 = "EVT_ArubaOpen"
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("Did not redirect to the previous page")

        common_method.wait_for_element_appearance("Connected", 100)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)


    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_52291(self):
    test_steps = {
        1: [1, 'Install the latest ZSB Series version, after installing successfully, click Open'],
        2: [2, 'When the app launches, check that the "Allow ZSB Series... of nearby devices" pops up directly'],
        3: [3, 'Click the Allow option'],
        4: [4, 'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog (If BT pair dialog pops up, allow it). Check that the network list will be displayed correctly']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:

        # step1: "Install the latest ZSB Series version, after installing successfully, click Open"
        start_time = time.time()

        device_networks.allow_nearby_devices_permission(0)

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step2: "When the app launches, check that the 'Allow ZSB Series... of nearby devices' pops up directly"
        start_time = time.time()

        try:
            others.wait_for_appearance_all("Allow")
        except:
            others.wait_for_appearance_all("allow")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step3: "Click the Allow option"
        start_time = time.time()
        try:
            others.click_allow()
        except:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step4: "Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog (If BT pair dialog pops up, allow it). Check that the network list will be displayed correctly"
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
        try:
            s1 = device_networks.get_network_names()
        except:
            raise Exception("network names not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Device_Networks_TestcaseID_50713(self):
    test_steps = {
        1: [1, 'Make sure test device connects to Wi-Fi network, sign in mobile app'],
        2: [2, 'Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        3: [3, 'Connect another Wi-Fi network for the device, make sure Wi-Fi is connected'],
        4: [4, 'Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error'],
        5: [5, 'Sign out and sign in again. Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error']
    }

    start_time_main = time.time()

    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])


    try:

        # step1: "Make sure test device connects to Wi-Fi network, sign in mobile app"
        start_time = time.time()

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        others.turn_on_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step2: "Check the basic functions on the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error"
        start_time = time.time()

        check_basic_functionalities()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step3: "Connect another Wi-Fi network for the device, make sure Wi-Fi is connected"
        start_time = time.time()

        others.open_wifi_settings()
        sleep(3)
        others.select_wifi("POCO M3", "1234567890")
        sleep(1)

        start_app("com.zebra.soho_app")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step4: "Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error"
        start_time = time.time()
        check_basic_functionalities()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

        # step5: "Sign out and sign in again. Recheck basic functions of the app, like printing test label, my design, common design, update printer settings and so on. Check all functions work well without any error"
        start_time = time.time()

        logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")

        check_basic_functionalities()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def setup_logout():
    common_method.tearDown()

    try:
        others.wait_for_element_appearance("Sign In", 10)
    except:
        pass

    try:
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
    except:
        pass
    sleep(2)





















