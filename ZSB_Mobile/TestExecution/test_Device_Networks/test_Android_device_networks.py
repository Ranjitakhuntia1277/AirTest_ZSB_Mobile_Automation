import inspect

from poco import poco
import time
from airtest.core.api import *
from ...Common_Method import Common_Method
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...PageObject.Others.Others import Others
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Social_Login.Social_Login import Social_Login
# from ...sphere_db import *
from ...PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
import os
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

others = Others(poco)
common_method = Common_Method(poco)
social_login = Social_Login(poco)
device_networks = Device_Networks_Android(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
help_page = Help_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
aps_notification = APS_Notification(poco)

"""
change this in the end all at once to a better statement:
fails : Check the Current Network, Network Status, IP Address would be updated accordingly
"""


class Test_Android_device_networks:
    pass

    def go_till_printer_wifi_page(self, add_network=0):
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        if add_network:
            others.click_manage_network_button()
            common_method.show_message(
                "Check if message'\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.'\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

            others.click_on_allow()
            common_method.wait_for_element_appearance_namematches("Apply Changes")

    def add_wifi_network(self, network_name="NESTWIFI", network_password="123456789"):
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(network_name)
        try:
            device_networks.enter_the_password(network_password)
            device_networks.click_on_connect()
        except:
            pass
        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        common_method.wait_for_element_appearance_enabled("Apply Changes", 100)
        device_networks.check_network_added(network_name)

    def t_100(self, add_network=0):
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

    def test_Device_Networks_TestcaseID_45693(self):
        pass
        test_steps = {
            1: [1,
                'Open the app. Slide the left slide page to choose "Printer Settings" item. Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14"). Click the Wi-Fi tab. Check if it spins for a while and then displays all information. Verify the "Add Network" button appears at the bottom. \nEnsure Current Network, Network Status, IP Address, and My saved Networks info are correct. Verify that "My saved Networks" has the name on the left and the Edit button on the right. \nConfirm that the connected Essid appears at the top of "My saved Networks".'],
            2: [2,
                'Click "Add Network" button. Check if the button spins and goes to the "Add Network" page with only 2 types of Essid: one open Essid and one WPA PSK Essid with a lock icon.'],
            3: [3,
                'Select the open Essid. Verify it returns to the Wi-Fi tab of the printer page. Confirm that Current Network, Network Status, and IP Address display "unconnected". \nCheck for the "Printer is offline" notification at the top. Wait for the "Printer is online" notification and confirm that Current Network, Network Status, and IP Address are updated as per the selected Essid.']
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
            data_sources_page.checkIfOnHomePage()
            self.go_till_printer_wifi_page(1)
            device_networks.check_add_network_button_present()
            device_networks.check_if_saved_network_list_is_displayed()
            name, status = device_networks.get_the_network_name_and_status()
            print("name->", name, "\nstatus->", status)
            if name != "NESTWIFI" or status != "Connected":
                raise Exception("fails:Check the Current Network, Network Status, info all are correct.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            others.click_add_network_button()
            netw1 = "EVT_ArubaOpen"
            device_networks.wait_till_the_networks_list()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            device_networks.click_network_by_name(netw1)
            try:
                common_method.wait_for_element_appearance_namematches("Printer")
            except:
                raise Exception("did not redirect to the previous page")
            try:
                others.wait_for_appearance_all("offline", 100)
            except:
                raise Exception("Printer is offline pop up dint shown up")
            common_method.wait_for_element_appearance_enabled("Apply Changes", 60)
            name, status = device_networks.get_the_network_name_and_status()
            print("name1->", name, "\nstatus1->", status)
            if name != "Not Connected" and status != "Not Connected":
                raise Exception("network and status did not get Not Connected")
            try:
                others.wait_for_appearance_all("online", 100)
            except:
                raise Exception("Printer is online pop up dint shown up")

            common_method.wait_for_element_appearance_namematches("Connected", 60)
            name, status = device_networks.get_the_network_name_and_status()
            print("name2->", name, "\nstatus2->", status)
            if status != "Connected":
                device_networks.delete_the_network(netw1)
                raise Exception(
                    "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")
            device_networks.delete_the_network(netw1)
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

    def test_Device_Networks_TestcaseID_45694(self):
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        self.go_till_printer_wifi_page(1)
        others.click_add_network_button()
        netw1 = "EL17-Cisco-WPA-WPA2"
        netw1_pass = "Dvttesting@123"
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
        print("name->", name, "\nstatus->", status)

        if name != "Not Connected" and status != "Not Connected":
            error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
            raise Exception(error)
        sleep(3)

        common_method.wait_for_element_appearance("Connected", 60)
        name, status = device_networks.get_the_network_name_and_status()
        print("name1->", name, "\nstatus1->", status)
        if name != netw1 or status != "Connected":
            device_networks.delete_the_network(netw1)
            error = "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose\n" + name + "->name" + status + "->status"
            raise Exception(error)
        device_networks.delete_the_network(netw1)

    def test_Device_Networks_TestcaseID_45699(self):
        pass
        test_steps = {
            1: [1, 'Open the app. Check the printer is offline and it is not in pairing mode.'],
            2: [2,
                'Go to the printer Wi-Fi tab, check all info are Not Connected. Click Manage Networks option. "Bluetooth Connection Required" dialog pops up, click Continue button. Check the "Bluetooth Connection Failed" dialog pops up since printer is not in pairing mode. Press 3s on power button to enter pairing mode, click Continue button on the "Bluetooth Connection Failed" dialog. Check it will try to connect Bluetooth instead of coming back to Manage network page.'],
            3: [3,
                'Click "Add Network" button after connecting to Bluetooth. Check it would go to the page to let you choose WiFi.'],
            4: [4,
                'Choose one WiFi to setup. Check it would go back to Wi-Fi tab, and the printer would change to online. Check all info in Wi-Fi tab would be updated.']
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
            data_sources_page.checkIfOnHomePage()
            common_method.show_message(
                "Put the printer associated with the account zebra901.swdvt@gmail.com into offline mode by connecting to a mobile hotspot and wait until it shows offline in the status. Make sure only that hotspot network is under saved networks. Remove any additional wifi networks if present. Click Ok in the pop up once done.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            self.go_till_printer_wifi_page(1)
            name, status = device_networks.get_the_network_name_and_status()
            print("name->", name, "\nstatus->", status)
            if status != "Not Connected":
                raise Exception("the network shows connected")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            others.click_add_network_button()
            netw1 = "NESTWIFI"
            netw1_pass = "123456789"
            device_networks.wait_till_the_networks_list()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4
            start_time = time.time()

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
            print("name1->", name, "\nstatus1->", status)
            if name != "Not Connected" and status != "Not Connected":
                error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
                raise Exception(error)
            sleep(3)
            common_method.wait_for_element_appearance("Connected", 60)
            name, status = device_networks.get_the_network_name_and_status()
            print("name2->", name, "\nstatus2->", status)
            if name != netw1 or status != "Connected":
                common_method.show_message("remove the hotspot from wifi tab under the printer.")
                error = "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose\n" + name + "->name" + status + "->status"
                raise Exception(error)
            common_method.show_message("remove the hotspot from wifi tab under the printer.")
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

    """Cannot automate-requires 2 devices"""

    def test_Device_Networks_TestcaseID_45897(self):
        pass
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block
        try:
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
            common_method.wait_for_element_appearance_namematches("Open navigation menu")
            self.go_till_printer_wifi_page(1)
            others.click_add_network_button()
            netw1 = "EL17-Cisco-WPA-WPA2"
            netw1_pass = "Dvttesting@123"
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
                error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
                raise Exception(error)
            sleep(3)
            common_method.wait_for_element_appearance("Connected", 60)
            name, status = device_networks.get_the_network_name_and_status()
            if name != netw1 or status != "Connected":
                device_networks.delete_the_network(netw1)
                error = "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose\n" + name + "->name" + status + "->status"
                raise Exception(error)
            device_networks.delete_the_network(netw1)

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

    def test_Device_Networks_TestcaseID_47943(self):
        pass
        test_steps = {
            1: [1, 'Start with the printer connected to an mobile hotspote.'],
            2: [2, 'Go to Printer Settings/Manage network.'],
            3: [3,
                'Add a Wi-Fi access point successfully (i.e., receive Offline and then Online toast messages). Check that the "Current Network" and "IP Address" are updated accordingly.']
        }
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block
        try:
            # Step 1
            start_time = time.time()

            common_method.show_message(
                "Go to wifi tab under the printer associated with the account zebra901.swdvt@gmail.com. Connect the printer to mobile hotspot and remove any wifi networks in the saved networks. Click Ok once done.")
            hotspot_name = common_method.get_user_input("Enter the hotspot name the printer is connected to.")
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            self.go_till_printer_wifi_page(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            others.click_add_network_button()
            netw1 = "NESTWIFI"
            netw1_pass = "123456789"
            device_networks.wait_till_the_networks_list()
            device_networks.click_network_by_name(netw1)
            device_networks.enter_the_password(netw1_pass)
            device_networks.click_on_connect()
            try:
                common_method.wait_for_element_appearance_namematches("Printer")
            except:
                raise Exception("did not redirect to the previous page")
            try:
                others.wait_for_appearance_all("offline", 100)
            except:
                raise Exception("Printer is offline pop up dint shown up")
            common_method.wait_for_element_appearance_enabled("Apply Changes", 60)
            name, status = device_networks.get_the_network_name_and_status()
            print("name1->", name, "\nstatus1->", status)
            if name != "Not Connected" and status != "Not Connected":
                error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
                raise Exception(error)
            try:
                others.wait_for_appearance_all("online", 100)
            except:
                raise Exception("Printer is online pop up dint shown up")
            sleep(3)
            common_method.wait_for_element_appearance("Connected", 60)
            name, status = device_networks.get_the_network_name_and_status()
            if name != netw1 or status != "Connected":
                device_networks.delete_the_network(hotspot_name)
                error = "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose\n" + name + "->name" + status + "->status"
                raise Exception(error)
            device_networks.delete_the_network(hotspot_name)
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

    def test_Device_Networks_TestcaseID_45708(self):
        pass
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        self.go_till_printer_wifi_page(1)
        others.click_add_network_button()
        netw1 = "NESTWIFI"
        netw1_pass = "123456789"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)
        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()
        device_networks.check_printer_is_already_connected_to_the_network_message()
        common_method.Stop_The_App()

    def test_Device_Networks_TestcaseID_45698(self):
        pass
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        self.go_till_printer_wifi_page(1)
        name1, status = device_networks.get_the_network_name_and_status()
        print("name1->", name1, "\nstatus->", status)
        s1 = device_networks.get_network_names()
        netw1 = "EVT_ArubaOpen"
        self.add_wifi_network(netw1)
        common_method.wait_for_element_appearance("Connected", 200)
        name, status = device_networks.get_the_network_name_and_status()
        print("name->", name1, "\nstatus1->", status)
        if name != name1:
            raise Exception("fails : check the Moneybadger would reset and it would still connect to Essid A")

        s2 = device_networks.get_network_names()
        if netw1 not in s2 or len(s1) + 1 != len(s2):
            device_networks.delete_the_network(netw1)
            raise Exception('newly added network is not present')
        device_networks.delete_the_network(netw1)
        common_method.Stop_The_App()

    def test_Device_Networks_TestcaseID_45703(self):

        common_method.show_message(
            "Connect the printer associated with the account zebra901.swdvt@gmail.com to mobile hotspot. Make sure it is connected to one more wifi network under the wifi tab.Make the mobile hotspot network higher priority and the current network is the hotspot network..")
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        res = others.check_printer_online_status()
        if res != "Online":
            print(res)
            raise Exception("printer not in Online state")
        common_method.show_message("Turn off the hotspot and wait for offline state to reflect in the app.")
        others.wait_for_appearance_all("Offline")
        others.wait_for_appearance_all("Online", 100)
        res = others.check_printer_online_status()
        if res != "Online":
            print(res)
            raise Exception(
                "fails : check the printer would go to Offline and back to Online when the primary network id turned off and it automatically switches to highest priority secondary network.")
        common_method.show_message("Remove the mobile hotspot connected from the connected wifi networks list.")

    def test_Device_Networks_TestcaseID_45706(self):

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        self.go_till_printer_wifi_page(1)

        s1 = device_networks.get_network_names()
        print("s1->", s1)
        for i in range(len(s1)):
            dele_netw = s1[i]
            device_networks.delete_the_network(dele_netw)
        try:
            device_networks.check_no_networks_in_saved_networks()
        except:
            self.add_wifi_network()
        name, status = device_networks.get_the_network_name_and_status()
        print("name->", name, "\nstatus->", status)
        if name != "Not Connected" and status != "Not Connected":
            error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
            raise Exception(error)
        self.add_wifi_network()

    def test_Device_Networks_TestcaseID_45707(self):
        pass
        test_steps = {
            1: [1, 'Open ZSB app.'],
            2: [2, 'Go to Printer settings > Printer Name, switch to Wi-Fi tab.Click on the Manage Networks button. (Pair Bluetooth successfully)'],
            3: [3,
                'Select Add Wifi, and choose one network to add. Input invalid password. Check the dialog of "Failed to Connect to Wifi Network" will pop up. Click on Cancel button, check the network is not added in the saved network list.'],
            4: [4,
                'Repeat step 3, but select Continue button on the confirm dialog. Check the network is added in the saved network list.']
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
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            self.go_till_printer_wifi_page(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            others.click_add_network_button()
            netw2 = "EL17-Cisco-WPA-WPA2"
            netw2_pass = "w45454oldiersss"
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

            # Step 4
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
            if netw2 not in s1:
                raise Exception("fails: check the network is  added in the saved network list.")
            device_networks.delete_the_network(netw2)
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

    def test_Device_Networks_TestcaseID_45695(self):
        pass
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        self.go_till_printer_wifi_page(1)

        others.click_add_network_button()

        netw2 = "EL17-Cisco-WPA-WPA2"
        netw2_pass = "12345678"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)

        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 300)
        if not device_networks:
            raise Exception("fails the wordings in the failed connected network")
        device_networks.click_on_cancel_button()
        common_method.wait_for_element_appearance("Apply Changes", 100)

        common_method.wait_for_element_appearance("Connected", 20)
        sleep(2)
        s1 = device_networks.get_network_names()
        if netw2 in s1:
            raise Exception("Network added even after clicking cancel in \n'Failed to Connect to Wifi network'\n page.")
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        others.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
        device_networks.click_on_continue_in_network_disconnect_error()
        common_method.wait_for_element_appearance_enabled("Apply Changes")
        common_method.wait_for_element_appearance("Not Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        print(s1)
        if netw2 not in s1:
            raise Exception("fails: check the network is  added in the saved network list.")
        device_networks.delete_the_network(netw2)

    def test_Device_Networks_TestcaseID_45807(self):
        test_steps = {
            1: [1, 'Login Mobile app'],
            2: [2, 'Home page displayed, click common design, all category list out'],
            3: [3, 'Go mobile device settings > wifi, select a different wifi to connect'],
            4: [4, 'After new wifi network connected, switch to Mobile App'],
            5: [5,
                'Click home to show home page. Check Home page show up with printer and Recently printed labels list'],
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

            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
            common_method.wait_for_element_appearance_namematches("Recently")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

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
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Go mobile device settings > wifi, select a different wifi to connect
            start_time = time.time()

            others.open_wifi_settings()
            netw1 = "EL17-Cisco-WPA-WPA2"
            netw1_pass = "Dvttesting@123"
            others.select_wifi(netw1, netw1_pass)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: After new wifi network connected, switch to Mobile App
            start_time = time.time()

            common_method.Start_The_App()
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click home to show home page. Check Home page show up with printer and Recently printed labels list
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            others.click_home_button()
            data_sources_page.checkIfOnHomePage()
            recently_printed_labels_after = others.get_recently_printed_labels()
            res = others.check_same_after_switching_network(recently_printed_labels_before,
                                                            recently_printed_labels_after)
            if not res:
                print("Changing network not showing files properly")
            login_page.click_Menu_HamburgerICN()
            others.click_common_designs_button()
            netw_2_common_designs = others.get_designs_visible_designs()
            res = others.check_same_after_switching_network(netw_1_common_designs, netw_2_common_designs)
            if not res:
                print("Changing network not showing files properly")
            login_page.click_Menu_HamburgerICN()
            others.click_home_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Repeat step 3-4, then open Common Design/My Design/My Data
            start_time = time.time()

            others.open_wifi_settings()
            sleep(1)
            others.select_wifi("EVT_Cisco_Open")
            sleep(1)
            common_method.Start_The_App()
            data_sources_page.checkIfOnHomePage()
            login_page.click_Menu_HamburgerICN()
            others.click_on_my_designs()
            common_method.wait_for_element_appearance_namematches("Showing")
            netw_2_my_designs = others.get_designs_visible_designs()
            res = others.check_same_after_switching_network(netw_1_my_designs, netw_2_my_designs)
            if not res:
                print("Changing network not showing files properly")
            login_page.click_Menu_HamburgerICN()
            others.click_on_my_data()
            sleep(2)
            netw_2_my_data = others.get_my_data_all()
            res = others.check_same_after_switching_network(netw_1_my_data, netw_2_my_data)
            if not res:
                print("Changing network not showing files properly")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Device_Networks_TestcaseID_46963(self):
        pass
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        self.go_till_printer_wifi_page(1)
        others.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        sleep(5)

        """Pass the name of the netowrk here"""
        netw1 = "EL17-Cisco-WPA-WPA2"
        netw1_pass = "Dvttesting@123"
        device_networks.click_network_by_name(netw1)
        device_networks.enter_the_password(netw1_pass)
        device_networks.click_on_connect()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        data_sources_page.checkIfOnHomePage()

        self.go_till_printer_wifi_page(1)

        others.scroll_down()

        res1 = device_networks.get_network_names()

        device_networks.swap_two_networks(res1[1], res1[0])
        res = others.check_apply_changes_button_clickable()
        if not res:
            raise Exception("Apply changes button not clickable after swapping networks.")
        others.click_apply_changes_button()
        res = others.check_apply_changes_button_clickable()
        if res:
            raise Exception("Apply changes button is still clickable even after clicking it.")

        device_networks.delete_the_network(netw1)
        device_networks.check_if_network_not_present_in_saved_networks(netw1)
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        common_method.Stop_The_App()

    def test_Device_Networks_TestcaseID_47794(self):
        pass
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        account = "zebra901.swdvt@gmail.com"
        help_page.chooseAcc(account)
        registration_page.BugFix_For_Google(account)
        data_sources_page.checkIfOnHomePage()
        common_method.Stop_The_App()
        common_method.disable_wifi()
        common_method.Start_The_App()
        if not device_networks.check_internet_disconnect_error():
            common_method.enable_wifi()
            raise Exception("internet disconnection error did not pop up")
        common_method.enable_wifi()
        common_method.Stop_The_App()

    def check_basic_functionalities(self):
        """printing test label"""
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_test_print()
        try:
            others.wait_for_appearance_all("Print complete")
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

    def logout_from_the_app(self):
        try:
            login_page.click_Menu_HamburgerICN()
        except:
            pass

        others.click_on_profile_edit()
        others.click_log_out_button()
        common_method.wait_for_element_appearance_namematches("Sign In")

    def test_Device_Networks_TestcaseID_50769(self):
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        others.turn_on_wifi()

        self.check_basic_functionalities()

        others.open_wifi_settings()
        common_method.show_message("Connect the device to a network without internet.")

        common_method.Start_The_App()
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

        others.open_wifi_settings()
        others.select_wifi("NESTWIFI", "123456789")

        common_method.Start_The_App()
        sleep(2)
        data_sources_page.checkIfOnHomePage()

        self.check_basic_functionalities()

        self.logout_from_the_app()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        account = "zebra901.swdvt@gmail.com"
        help_page.chooseAcc(account)
        registration_page.BugFix_For_Google(account)
        data_sources_page.checkIfOnHomePage()

        self.check_basic_functionalities()

    def test_Device_Networks_TestcaseID_50782(self):
        pass
        test_steps = {
            1: [1, 'Sign in to the test account with at least one printer added, keep on the home page.'],
            2: [2, 'Disconnect the device’s network (Turn off the Wi-Fi option).'],
            3: [3,
                'Go to the Common Designs/My Designs from the left menu. Check if there is an error message showing up on Common Designs or My Designs.'],
            4: [4,
                'Back to the Home page and check the prompt message. It should be like "The service is currently unavailable."'],
            5: [5,
                'Perform the same steps on Android and iOS devices. Check if the prompt message is the same on both devices.']
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
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            device_networks.turn_off_wifi()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            others.click_on_my_designs()
            sleep(2)
            if not device_networks.check_the_my_designs_internet_lost_error():
                common_method.enable_wifi()
                raise Exception("fails: Check there is an error message showing up on My designs")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            others.click_home_button()

            device_networks.refresh_home_page()
            if not device_networks.check_sudden_network_off_error():
                common_method.enable_wifi()
                raise Exception("network disconnection error did not pop up")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5
            start_time = time.time()

            common_method.show_message(
                "Perform the following steps on Android and iOS devices. Check if the prompt message is the same on both devices.\n1. Sign in test account with at least one printer added, keep on home page\n2. Disconnect device’s network (Turn off the wi-fi option)\n3. Go to the Common Designs/My designs from the left menu. Check there is an error message showing up on Common Designs or My designs\n4. Back to Home page. Check the prompt message is like \"The service is currently unavailable\"")
            common_method.enable_wifi()
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

    def test_Device_Networks_TestcaseID_52290(self):
        pass
        test_steps = {
            1: [1, 'Open zebra application.'],
            2: [2,
                'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog (If BT pair dialog pops up, allow it). Check the network list will be displayed correctly.'],
            3: [3, 'Minimize ZSB series, open its app info, disable ZSB Nearby devices permission.'],
            4: [4, 'Repeat step 2. Check this time it will ask for nearby devices.'],
            5: [5, 'When the "Allow ZSB series to find, connect to ....nearby devices" pops up, click "Allow."'],
            6: [6,
                'Wait for printer pair to successfully complete. Check the network list will be displayed correctly. Check there is no odd behavior like crashes.'],
            7: [7, 'Try to add/delete/sort the network. Check able to manage network successfully.']
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
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            others.click_Printer_Settings()
            others.select_first_printer()
            others.click_wifi_button()
            others.click_manage_network_button()
            common_method.show_message(
                "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")
            others.click_on_allow()
            name, status = device_networks.get_the_network_name_and_status()
            print("name->", name, "\nstatus->", status)
            device_networks.check_if_device_is_connected_to_a_network(status)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            device_networks.allow_nearby_devices_permission(0)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4
            start_time = time.time()

            common_method.Start_The_App()
            data_sources_page.checkIfOnHomePage()
            login_page.click_Menu_HamburgerICN()
            others.click_Printer_Settings()
            others.select_first_printer()
            others.click_wifi_button()
            others.click_manage_network_button()
            common_method.show_message(
                "Check if message\nBluet1ooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5
            start_time = time.time()

            others.click_on_allow()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6
            start_time = time.time()

            name, status = device_networks.get_the_network_name_and_status()
            print("name1->", name, "\nstatus1->", status)
            if status != "Connected":
                raise Exception("no network is connected to the device")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7
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
            device_networks.delete_the_network(netw1)
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

    """Retest"""
    def test_Device_Networks_TestcaseID_52291(self):
        pass

        device_networks.allow_nearby_devices_permission(0)
        common_method.tearDown()
        device_networks.check_if_nearby_device_permission_pop_up_displayed()
        others.click_on_allow()
        data_sources_page.checkIfOnHomePage()

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        common_method.show_message(
            "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

        others.click_on_allow()

        name, status = device_networks.get_the_network_name_and_status()
        print("name->", name, "\nstatus->", status)

        device_networks.check_if_device_is_connected_to_a_network(status)
        try:
            s1 = device_networks.get_network_names()
            print(s1)
        except:
            raise Exception("network names not displayed")

    def test_Device_Networks_TestcaseID_52289(self):
        pass
        test_steps = {
            1: [1, 'Install the testing ZSB Series build, sign in test account.'],
            2: [2,
                'Go to Printer Settings/Wi-Fi tab, click Manage Networks button and Continue on the Bluetooth Connection Required dialog.'],
            3: [3, 'When the "Allow ZSB series to find, connect to ....nearby devices" pops up, click "Allow."'],
            4: [4,
                'Wait for printer pair to successfully complete. Check the network list will be displayed correctly. Check there is no odd behavior like crashes.'],
            5: [5, 'Try to add/delete/sort the network. Check able to manage network successfully.']
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
            data_sources_page.log_out_of_account()
            data_sources_page.clearAppData()
            data_sources_page.allowPermissions()
            """Sign in"""
            registration_page.clickSignIn()
            registration_page.click_Google_Icon()
            account = "zebra901.swdvt@gmail.com"
            help_page.chooseAcc(account)
            registration_page.BugFix_For_Google(account)
            """verify if logged in successfully"""
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            others.click_Printer_Settings()
            others.select_first_printer()
            others.click_wifi_button()
            others.click_manage_network_button()
            common_method.show_message(
                "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            others.click_on_allow()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4
            start_time = time.time()

            name, status = device_networks.get_the_network_name_and_status()
            if status != "Connected":
                raise Exception("no network is connected to the device")
            device_networks.check_if_saved_network_list_is_displayed()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5
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
            device_networks.delete_the_network(netw1)

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

    def test_Device_Networks_TestcaseID_52292(self):
        pass

        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        account = "zebra901.swdvt@gmail.com"
        help_page.chooseAcc(account)
        registration_page.BugFix_For_Google(account)
        """verify if logged in successfully"""

        data_sources_page.checkIfOnHomePage()

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        common_method.show_message(
            "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

        others.click_on_allow()

        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")

        device_networks.allow_nearby_devices_permission(0)

        common_method.Start_The_App()
        data_sources_page.checkIfOnHomePage()

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        common_method.show_message(
            "Check if message\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

        others.click_on_allow()

        common_method.wait_for_element_appearance_namematches("Apply Changes")
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")

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
        device_networks.delete_the_network(netw1)

    def test_Device_Networks_TestcaseID_50713(self):
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        others.turn_on_wifi()
        self.check_basic_functionalities()
        others.open_wifi_settings()
        netw1 = "EL17-Cisco-WPA-WPA2"
        netw1_pass = "Dvttesting@123"
        others.select_wifi(netw1, netw1_pass)
        common_method.Start_The_App()
        self.check_basic_functionalities()
        self.logout_from_the_app()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        account = "zebra901.swdvt@gmail.com"
        help_page.chooseAcc(account)
        registration_page.BugFix_For_Google(account)
        data_sources_page.checkIfOnHomePage()
        self.check_basic_functionalities()
        common_method.Stop_The_App()

    def test_Device_Networks_TestcaseID_45696(self):
        test_steps = {
            1: [1, 'Open the app and login the account with online Moneybadger'],
            2: [2,
                'Slide the left slide page to choose "Printer Settings" item. Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14"), Click the Wi-Fi tab. Check it would be spinning for a while to wait all infos appears at the page. After that, it would appear the button "Add Network" at the bottom. '],
            3: [3,
                'Add 3 networks in saved networks if not already present. Check the Current Network, Network Status, IP Address and My saved Networks info all are correct. Check the list "My saved Networks" has the Name words at the left and Edit button at the right. Check those Essids would appear at the list "My saved Networks" such as: AEssid, BEssid, CEssid'],
            4: [4,
                'Click "Edit" button. Check the Essids would appear the drag button at the left and delete button at the right'],
            5: [5,
                'Drag the BEssid to the top of the list. Check the Moneybadger would change the network to BEssid. Check the Current Network, Network Status, IP Address would be updated accordingly']
        }

        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block
        try:
            # Step 1: Open the app and login the account with online Moneybadger
            start_time = time.time()

            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2
            start_time = time.time()

            self.go_till_printer_wifi_page(1)
            device_networks.check_add_network_button_present()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3
            start_time = time.time()

            others.click_add_network_button()
            default_network = "NESTWIFI"
            netw1 = "EL17-Cisco-WPA-WPA2"
            netw1_pass = "Dvttesting@123"
            device_networks.wait_till_the_networks_list()
            device_networks.click_network_by_name(netw1)
            device_networks.enter_the_password(netw1_pass)
            device_networks.click_on_connect()
            try:
                common_method.wait_for_element_appearance_namematches("Printer")
            except:
                raise Exception("did not redirect to the previous page")
            common_method.wait_for_element_appearance_namematches(netw1, 60)
            netw2 = "EVT_ArubaOpen"
            self.add_wifi_network(netw2)
            common_method.wait_for_element_appearance("Connected", 200)
            name, status = device_networks.get_the_network_name_and_status()
            if name != netw1 or status != "Connected":
                error = "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose\n" + name + "->name" + status + "->status"
                raise Exception(error)
            device_networks.check_if_saved_network_list_is_displayed()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4
            start_time = time.time()

            common_method.show_message("Check there are delete and adjust position icon shown for each saved network.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5
            start_time = time.time()

            device_networks.swap_two_networks(default_network, netw1)
            others.click_apply_changes_button()
            common_method.wait_for_element_appearance("Not Connected", 100)
            common_method.wait_for_element_appearance("Connected", 100)

            name, status = device_networks.get_the_network_name_and_status()
            if name != netw1 or status != "Connected":
                device_networks.delete_the_network(netw1)
                device_networks.delete_the_network(netw2)
                raise Exception(
                    "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")
            device_networks.delete_the_network(netw1)
            device_networks.delete_the_network(netw2)
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

    def test_Device_Networks_TestcaseID_45697(self):
        test_steps = {
            1: [1, 'Open the app and login the account with online Moneybadger'],
            2: [2,
                'Slide the left slide page to choose "Printer Settings" item. Click the Moneybadger name tab (such as "ZSB-DP12", "ZSB-DP14")'],
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
            common_method.tearDown()
            common_method.show_message(
                "There are at least five essid for testing, add five networks to the printer associated with the account zebra901.swdvt@gmail.com.\nAlso keep a note of the background picture on the home page.\n clickOk once done. ")
            data_sources_page.checkIfOnHomePage()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Slide the left slide page to choose "Printer Settings" item
            start_time = time.time()
            self.go_till_printer_wifi_page(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Click the Wi-Fi tab. Check all necessary info and elements.
            start_time = time.time()
            name, status = device_networks.get_the_network_name_and_status()
            if status != "Connected":
                raise Exception("fails:Check the Current Network, Network Status, info all are correct.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click "Add Network" button to add 5 Essids. Check button state.
            start_time = time.time()

            network_list = device_networks.get_network_names()
            expected_count_of_saved_networks = 5
            device_networks.check_number_of_saved_networks_as_expected(expected_count_of_saved_networks, network_list)
            others.click_add_network_button()

            if device_networks.check_add_network_button_enabled():
                raise Exception("Add network is enabled even after adding 5 networks")
            common_method.show_message(
                "Remove all the networks other than nest wifi from the networks connected to the printer and then click Ok.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Back to home page. Check background picture.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            data_sources_page.clickHome()
            data_sources_page.checkIfOnHomePage()
            common_method.show_message(
                "Check background picture on the home page is the same as the one in the beginning(this step for covering SMBUI-1199).")
            common_method.Stop_The_App()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45697"], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1


        except Exception as e:

            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
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
            common_method.show_message(
                "Add more than two network to the saved networks list under wifi tab under the printer associated with the account zebra901.swdvt@gmail.com if not already present in it.")
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
            self.go_till_printer_wifi_page(1)
            name, status = device_networks.get_the_network_name_and_status()
            print("name->", name, "\nstatus->", status)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on Manage Networks button. Check it would display the saved networks list
            start_time = time.time()

            device_networks.check_if_saved_network_list_is_displayed()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check there are delete icons shown
            start_time = time.time()
            common_method.show_message("Check there are deleted Icons displayed along with the network name.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Delete the network which is not connecting. Check the network is removed from the list
            start_time = time.time()
            s1 = device_networks.get_network_names()
            s1.remove(name)
            delete_network_name = s1[0]
            device_networks.delete_the_network(delete_network_name)
            s1 = device_networks.get_network_names()
            if delete_network_name in s1:
                raise Exception("deleted network is still present even after clicking the delete button.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Check the network priority is updated and the printer would connect to the highest priority network in the end.
            # Check Wi-Fi page displays the correct connected network information.
            start_time = time.time()
            try:
                device_networks.wait_for_the_printer_to_connect_network(name)
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
            2: [2,
                'Click on Manage Networks button. Check it would display the saved networks list. Check if there are more than 1 network is saved if not add a network.'],
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
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
            self.go_till_printer_wifi_page(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on Manage Networks button
            start_time = time.time()

            others.click_add_network_button()
            default_network = "NESTWIFI"
            netw1 = "EL17-Cisco-WPA-WPA2"
            netw1_pass = "Dvttesting@123"
            device_networks.wait_till_the_networks_list()
            device_networks.click_network_by_name(netw1)
            device_networks.enter_the_password(netw1_pass)
            device_networks.click_on_connect()
            try:
                common_method.wait_for_element_appearance_namematches("Printer")
            except:
                raise Exception("did not redirect to the previous page")
            device_networks.check_network_added(netw1)
            device_networks.swap_two_networks(default_network, netw1)
            others.click_apply_changes_button()
            common_method.wait_for_element_appearance("Not Connected", 100)
            common_method.wait_for_element_appearance("Connected", 100)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Click on Edit button
            start_time = time.time()

            common_method.show_message("Check there are delete and adjust position icon shown for each saved network.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Delete a connected network and verify
            start_time = time.time()
            s1 = device_networks.get_network_names()
            delete_network_name = s1[0]
            device_networks.delete_the_network(delete_network_name)
            sleep(2)

            s1 = device_networks.get_network_names()
            if delete_network_name in s1:
                raise Exception("deleted network is still present")

            common_method.wait_for_element_appearance("Connected", 100)
            sleep(2)
            name1, status = device_networks.get_the_network_name_and_status()
            if name1 not in s1:
                raise Exception("fails : to connect to the highest priority network in existing networks")
            common_method.Stop_The_App()

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
            common_method.tearDown()
            common_method.show_message(
                "Go to the wifi tab under printer settings in the account zebra901.swdvt@gmail.com.\nAdd your device personal hotspot to the saved networks and make sure it is the only saved network your printer is connected to.\nWait until network status is shown Connected and then turn off the hotspot wait for printer to go to offline state. Once its offline click Ok on the po up displayed.")
            data_sources_page.checkIfOnHomePage()
            self.go_till_printer_wifi_page(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on Manage Networks button
            start_time = time.time()

            network_list = device_networks.get_network_names()
            expected_count_of_saved_networks = 1
            device_networks.check_number_of_saved_networks_as_expected(expected_count_of_saved_networks, network_list)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Click on Edit button
            start_time = time.time()

            common_method.show_message("Check there are delete and adjust position icon shown for each saved network.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Delete a network and verify
            start_time = time.time()
            dele_netw = network_list[0]
            device_networks.delete_the_network(dele_netw)
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
            device_networks.enter_the_password(netw1_pass)
            device_networks.click_on_connect()
            common_method.wait_for_element_appearance("Connected", 100)
            name, status = device_networks.get_the_network_name_and_status()
            if status != "Connected":
                raise Exception(
                    "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just chosen")
            common_method.Stop_The_App()

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
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
            common_method.show_message(
                "Account-Zebra901.swdvt@gmail.com\nHave two mobile hotspots in hand and remove any wi-fi network from saved networks if present and connect the printer to one of the hotspot and wait for it to show 'ONLINE'.")
            common_method.show_message(
                "Turn off the hotspot which is currently connected to the printer and wait for 'OFFLINE' status of printer to reflect on the app\n Make sure the other hotspot which is not present in the saved networks is on and available for connection.\n Once the above steps are completed click 'Ok' on the pop up displayed.")
            sleep(2)
            res = others.check_printer_online_status()
            if res != "Offline":
                raise Exception("The printer is not in offline state.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Navigate to Wi-Fi tab and verify status
            start_time = time.time()
            self.go_till_printer_wifi_page(1)
            name, status = device_networks.get_the_network_name_and_status()
            print("name->", name, "\nstatus->", status)
            if name != "Not Connected" or status != "Not Connected":
                raise Exception("network and status did not get Not Connected")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Add a new network
            start_time = time.time()
            others.click_add_network_button()
            netw1 = common_method.get_user_input(
                "Enter the name of the first hotspot network that is in saved networks.")
            netw2 = common_method.get_user_input(
                "Enter the name of the second hotspot network that you have turned on.")
            netw2_pass = common_method.get_user_input("Enter password of the second hotspot.")
            device_networks.wait_till_the_networks_list()
            device_networks.click_network_by_name(netw2)
            device_networks.enter_the_password(netw2_pass)
            device_networks.click_on_connect()

            try:
                common_method.wait_for_element_appearance_namematches("Printer")
            except:
                raise Exception("did not redirect to the previous page")

            common_method.wait_for_element_appearance_namematches(netw2, 100)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Verify printer connectivity and status
            start_time = time.time()
            common_method.wait_for_element_appearance("Connected", 100)
            sleep(2)
            name, status = device_networks.get_the_network_name_and_status()
            print("name1->", name, "\nstatus1->", status)
            if name != netw2 or status != "Connected":
                device_networks.delete_the_network(netw2)
                device_networks.delete_the_network(netw1)
                self.add_wifi_network()
                raise Exception(
                    "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")
            device_networks.delete_the_network(netw2)
            device_networks.delete_the_network(netw1)
            self.add_wifi_network()

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
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()

            self.go_till_printer_wifi_page(0)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Reboot printer
            start_time = time.time()
            common_method.show_message(
                "Reboot printer associated with the account-zebra901.swdvt@gmail.com and wait for network status to show 'Connected' after that click ok")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Click "Manage networks" button
            start_time = time.time()
            others.click_manage_network_button()
            common_method.show_message(
                "Check if message'\nBluetooth Connection Required\nYou are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into \"pairing mode\" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.'\nis displayed.\nIf so perform the actions mentioned in the pop up and click \"Continue\" button once done.")

            others.click_on_allow()
            common_method.wait_for_element_appearance_namematches("Apply Changes", 60)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Check ZSB app shows network without any error or fail
            start_time = time.time()
            try:
                device_networks.get_network_names()
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

        try:
            # Step 1: Make sure test device connects to Wi-Fi network, sign in mobile app
            start_time = time.time()

            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()

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
            """No cellular network on test devices-TDMS"""
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
            data_sources_page.allowPermissions()
            """Sign in"""
            registration_page.clickSignIn()
            registration_page.click_Google_Icon()
            account = "zebra901.swdvt@gmail.com"
            help_page.chooseAcc(account)
            registration_page.BugFix_For_Google(account)
            data_sources_page.checkIfOnHomePage()
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

            common_method.show_message("Keep a hotspot network in hand.")
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
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
            netw1 = common_method.get_user_input("Enter the name of the hotspot network in the textbox below.")
            netw1_pass = common_method.get_user_input("Enter the password of the hotspot network in the textbox below.")
            others.select_wifi(netw1, netw1_pass)
            common_method.Start_The_App()

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
            data_sources_page.allowPermissions()
            """Sign in"""
            registration_page.clickSignIn()
            registration_page.click_Google_Icon()
            account = "zebra901.swdvt@gmail.com"
            help_page.chooseAcc(account)
            registration_page.BugFix_For_Google(account)
            data_sources_page.checkIfOnHomePage()
            self.check_basic_functionalities()

            others.open_wifi_settings()
            netw1 = "NESTWIFI"
            netw1_pass = "123456789"
            others.select_wifi(netw1, netw1_pass)
            common_method.Stop_The_App()

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
            common_method.tearDown()
            data_sources_page.checkIfOnHomePage()
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

            # Step 4: Enable the device's Wi-Fi network back, make sure network is connected, refresh the app
            start_time = time.time()
            others.turn_on_wifi()
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
            data_sources_page.allowPermissions()
            """Sign in"""
            registration_page.clickSignIn()
            registration_page.click_Google_Icon()
            account = "zebra901.swdvt@gmail.com"
            help_page.chooseAcc(account)
            registration_page.BugFix_For_Google(account)
            data_sources_page.checkIfOnHomePage()
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

    "_______________DUPLICATES_______________________"

    # def test_Device_Networks_TestcaseID_45696(self):
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     self.go_till_printer_wifi_page(1)
    #     others.click_add_network_button()
    #     netw1 = "NESTWIFI"
    #     netw1_pass = "123456789"
    #
    #     netw2 = "POCO M3"
    #     netw2_pass = "1234567890"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw2)
    #     if not device_networks.check_the_wordings_in_connect_to_network():
    #         raise Exception("dialog dint pop up or the wordings are wrong")
    #     device_networks.click_on_cancel_button()
    #     try:
    #         device_networks.click_network_by_name(netw2)
    #     except:
    #         raise Exception("dialogue of connect to network did not close on clicking cancel button")
    #
    #     device_networks.enter_the_password(netw2_pass)
    #     device_networks.click_on_connect()
    #
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Printer")
    #     except:
    #         raise Exception("did not redirect to the previous page")
    #
    #     common_method.wait_for_element_appearance_namematches(netw2, 60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != "Not Connected" and status != "Not Connected":
    #         raise Exception("network and status did not get Not Connected")
    #
    #     device_networks.swap_two_networks(netw1, netw2)
    #
    #     others.click_apply_changes_button()
    #     common_method.wait_for_element_appearance("Connected", 100)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != netw2 or status != "Connected":
    #         raise Exception(
    #             "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")
    #
    # def test_Device_Networks_TestcaseID_45697(self):
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     self.go_till_printer_wifi_page(1)
    #
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if status != "Connected":
    #         raise Exception("fails:Check the Current Network, Network Status, info all are correct.")
    #
    #     if device_networks.check_add_network_button_enabled():
    #         raise Exception("Add network is enabled even after adding 5 networks")
    #
    # def test_Device_Networks_TestcaseID_45699(self):
    #     test_steps = {
    #         1: [1, 'Open the app. Check the printer is offline and it is not in pairing mode'],
    #         2: [2, 'Go to the printer Wi-Fi tab. Check all info shows "Not Connected". Click Manage Networks option'],
    #         3: [3,
    #             '“Bluetooth Connection Required” dialog pops up. Click Continue button. Check the “Bluetooth Connection Failed” dialog pops up since printer is not in pairing mode'],
    #         4: [4,
    #             'Press 3s on power button to enter pairing mode. Click Continue button on the “Bluetooth Connection Failed” dialog. Check it will try to connect Bluetooth instead of coming back to Manage network page'],
    #         5: [5,
    #             'Click "Add Network" button after connecting to Bluetooth. Check it would go to the page to let you choose WiFi'],
    #         6: [6,
    #             'Choose one Wifi to setup. Check it would go back to Wi-Fi tab, and the printer would change to online. Check all info in WiFi tab would be updated.']
    #     }
    #
    #     start_time_main = time.time()
    #     stepId = 1
    #     current_function_name = inspect.currentframe().f_code.co_name
    #     test_case_id = current_function_name.split("_")[-1]
    #     start_main(execID, leftId[test_case_id])
    #
    #     try:
    #         # Step 1: Open the app. Check the printer is offline and it is not in pairing mode
    #         start_time = time.time()
    #         common_method.show_message(
    #             "check the printer associated with the account zebra901.swdvt@gmail.com is offline and see the status iis reflected on the app.")
    #         common_method.tearDown()
    #         data_sources_page.checkIfOnHomePage()
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #         # Step 2: Go to the printer Wi-Fi tab. Check all info shows "Not Connected". Click Manage Networks option
    #         start_time = time.time()
    #         self.go_till_printer_wifi_page(0)
    #         name, status = device_networks.get_the_network_name_and_status()
    #         if status != "Not Connected":
    #             raise Exception("the network shows connected")
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #         # Step 3: “Bluetooth Connection Required” dialog pops up. Click Continue button. Check the “Bluetooth Connection Failed” dialog pops up since printer is not in pairing mode
    #         start_time = time.time()
    #         others.click_continue_in_bluetooth_connection_required()
    #         common_method.wait_for_element_appearance_namematches("Bluetooth Connection Failed")
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #         # Step 4: Press 3s on power button to enter pairing mode. Click Continue button on the “Bluetooth Connection Failed” dialog. Check it will try to connect Bluetooth instead of coming back to Manage network page
    #         start_time = time.time()
    #         # Press 3s on power button and continue with Bluetooth connection attempt code here
    #         common_method.show_message("turn on the printer for online mode after 30s press ok in dialogue")
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #         # Step 5: Click "Add Network" button after connecting to Bluetooth. Check it would go to the page to let you choose WiFi
    #         start_time = time.time()
    #         others.click_add_network_button()
    #         common_method.wait_for_element_appearance_namematches("Choose WiFi")
    #
    #         others.click_manage_network_button()
    #         others.click_continue_in_bluetooth_connection_required()
    #         common_method.wait_for_element_appearance_namematches("Apply Changes")
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #         # Step 6: Choose one Wifi to setup. Check it would go back to Wi-Fi tab, printer would change to online. Check all info in WiFi tab would be updated
    #         start_time = time.time()
    #         # Choose WiFi and verify network status and info update code here
    #
    #         others.click_add_network_button()
    #         netw1 = "NESTWIFI"
    #         netw1_pass = "123456789"
    #         device_networks.wait_till_the_networks_list()
    #         device_networks.click_network_by_name(netw1)
    #         if not device_networks.check_the_wordings_in_connect_to_network():
    #             raise Exception("dialog dint pop up or the wordings are wrong")
    #         device_networks.click_on_cancel_button()
    #         try:
    #             device_networks.click_network_by_name(netw1)
    #         except:
    #             raise Exception("dialogue of connect to network did not close on clicking cancel button")
    #
    #         device_networks.enter_the_password(netw1_pass)
    #         device_networks.click_on_connect()
    #
    #         try:
    #             common_method.wait_for_element_appearance_namematches("Printer")
    #         except:
    #             raise Exception("did not redirect to the previous page")
    #
    #         name, status = device_networks.get_the_network_name_and_status()
    #         if name != "Not Connected" and status != "Not Connected":
    #             raise Exception("network and status did not get Not Connected")
    #
    #         common_method.wait_for_element_appearance("Connected", 60)
    #         name, status = device_networks.get_the_network_name_and_status()
    #         if name != netw1 or status != "Connected":
    #             raise Exception(
    #                 "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")
    #
    #         exec_time = (time.time() - start_time) / 60
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
    #                     exec_time)
    #         stepId += 1
    #
    #     except Exception as e:
    #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
    #         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
    #         raise Exception(str(e))
    #
    #     finally:
    #         exec_time = (time.time() - start_time_main) / 60
    #         end_main(execID, leftId[test_case_id], exec_time)
    #
    # def test_Device_Networks_TestcaseID_45700(self):
    #
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     # common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
    #     name1, status = device_networks.get_the_network_name_and_status()
    #     s1 = device_networks.get_network_names()
    #
    #     s1.remove(name1)
    #     dele_netw = s1[0]
    #     device_networks.delete_the_network(dele_netw)
    #
    #     common_method.wait_for_element_appearance_namematches("Deleting")
    #     s1 = device_networks.get_network_names()
    #     if dele_netw in s1:
    #         raise Exception("deleted network is still present")
    #     common_method.wait_for_element_appearance("Connected", 100)
    #
    #     try:
    #         device_networks.wait_for_the_printer_to_connect_network(name1)
    #     except:
    #         raise Exception(
    #             "fails: check the network priority is updated and the printer would connect to the highest priority network ")
    #
    # def test_Device_Networks_TestcaseID_45701(self):
    #
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
    #
    #     """bug SMBM-2239"""
    #     s1 = device_networks.get_network_names()
    #
    #     dele_netw = s1[0]
    #     device_networks.delete_the_network(dele_netw)
    #     print(dele_netw)
    #     print("\n", "new line printed")
    #
    #     common_method.wait_for_element_appearance_namematches("Deleting")
    #     sleep(2)
    #     s1 = device_networks.get_network_names()
    #     if dele_netw in s1:
    #         raise Exception("deleted network is still present")
    #     common_method.wait_for_element_appearance("Connected", 100)
    #     sleep(2)
    #     name1, status = device_networks.get_the_network_name_and_status()
    #     if name1 not in s1:
    #         raise Exception("fails : to connect to the highest priority network in existing networks")
    #
    # def test_Device_Networks_TestcaseID_45702(self):
    #
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
    #
    #     s1 = device_networks.get_network_names()
    #
    #     dele_netw = s1[0]
    #     device_networks.delete_the_network(dele_netw)
    #
    #     common_method.wait_for_element_appearance_namematches("Deleting")
    #     sleep(2)
    #
    #     common_method.wait_for_element_appearance("Not Connected", 100)
    #     sleep(2)
    #
    #     others.click_add_network_button()
    #
    #     netw1 = "NESTWIFI"
    #     netw1_pass = "123456789"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw1)
    #
    #     device_networks.click_on_cancel_button()
    #     try:
    #         device_networks.click_network_by_name(netw1)
    #     except:
    #         raise Exception("dialogue of connect to network did not close on clicking cancel button")
    #
    #     device_networks.enter_the_password(netw1_pass)
    #     device_networks.click_on_connect()
    #
    #     common_method.wait_for_element_appearance("Connected", 60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if status != "Connected":
    #         raise Exception(
    #             "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")
    #
    # def test_Device_Networks_TestcaseID_45704(self):
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     sleep(2)
    #     res = others.check_printer_online_status()
    #     if res != "Offline":
    #         raise Exception("fails : check the printer would go to offline and back to online")
    #
    #     self.go_till_printer_wifi_page(1)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != "Not Connected" and status != "Not Connected":
    #         error = "network and status did not get Not Connected\n" + name + "->name" + status + "->status"
    #         raise Exception(error)
    #
    #     others.click_add_network_button()
    #
    #     netw2 = "POCO M3"
    #     netw2_pass = "1234567890"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw2)
    #
    #     device_networks.enter_the_password(netw2_pass)
    #     device_networks.click_on_connect()
    #
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Printer")
    #     except:
    #         raise Exception("did not redirect to the previous page")
    #
    #     common_method.wait_for_element_appearance_namematches(netw2, 60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #
    #     common_method.wait_for_element_appearance("Connected", 100)
    #     sleep(2)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != netw2 or status != "Connected":
    #         raise Exception(
    #             "fails : Check the Current Network, Network Status, IP Address would be updated accordingly")
    #
    # def test_Device_Networks_TestcaseID_50767(self):
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     others.turn_on_wifi()
    #
    #     self.check_basic_functionalities()
    #
    #     others.open_wifi_settings()
    #     others.select_wifi("POCO M3", "1234567890")
    #
    #     start_app("com.zebra.soho_app")
    #
    #     self.check_basic_functionalities()
    #
    #     self.logout_from_the_app()
    #     login_page.click_loginBtn()
    #     common_method.wait_for_element_appearance_namematches("Continue with Google")
    #     login_page.click_Loginwith_Google()
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Choose an account")
    #         social_login.choose_a_google_account("zebratest850@gmail.com")
    #     except:
    #         pass
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.check_basic_functionalities()
    #
    # def test_Device_Networks_TestcaseID_50766(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     others.turn_on_wifi()
    #
    #     self.check_basic_functionalities()
    #
    #     device_networks.turn_off_wifi()
    #     device_networks.turn_on_cellular_data()
    #     sleep(4)
    #
    #     self.check_basic_functionalities()
    #
    #     self.logout_from_the_app()
    #     login_page.click_loginBtn()
    #     common_method.wait_for_element_appearance_namematches("Continue with Google")
    #     login_page.click_Loginwith_Google()
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Choose an account")
    #         social_login.choose_a_google_account("zebratest850@gmail.com")
    #     except:
    #         pass
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.check_basic_functionalities()
    #
    # def test_Device_Networks_TestcaseID_47912(self):
    #     common_method.tearDown()
    #     data_sources_page.checkIfOnHomePage()
    #
    #     self.go_till_printer_wifi_page(0)
    #
    #     sleep(300)
    #
    #     others.click_manage_network_button()
    #     common_method.wait_for_element_appearance_namematches("Apply Changes")
    #     try:
    #         s1 = device_networks.get_network_names()
    #     except:
    #         raise Exception("network names did not shown after rebooting printer")
    #
    # def test_Device_Networks_TestcaseID_45693(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
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
    #     others.wait_for_appearance_all("offline", 20)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != "Not Connected" and status != "Not Connected":
    #         raise Exception("network and status did not get Not Connected")
    #     try:
    #         others.wait_for_appearance_all("online", 60)
    #     except:
    #         raise Exception("Printer is online pop up dint shown up")
    #
    #     common_method.wait_for_element_appearance_namematches("Connected", 60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if status != "Connected":
    #         raise Exception(
    #             "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")
    #
    # def test_Device_Networks_TestcaseID_50768(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     others.turn_on_wifi()
    #
    #     self.check_basic_functionalities()
    #
    #     device_networks.turn_off_wifi()
    #     sleep(1)
    #     device_networks.refresh_home_page()
    #     sleep(2)
    #     if not device_networks.check_sudden_network_off_error():
    #         raise Exception("network disconnection error did not pop up")
    #     sleep(2)
    #     device_networks.click_on_continue_in_network_disconnect_error()
    #     try:
    #         device_networks.click_on_continue_in_network_disconnect_error()
    #     except:
    #         pass
    #     try:
    #         device_networks.click_on_continue_in_network_disconnect_error()
    #     except:
    #         pass
    #
    #     others.turn_on_wifi()
    #     sleep(4)
    #     device_networks.refresh_home_page()
    #
    #     self.check_basic_functionalities()
    #
    #     self.logout_from_the_app()
    #     login_page.click_loginBtn()
    #     common_method.wait_for_element_appearance_namematches("Continue with Google")
    #     login_page.click_Loginwith_Google()
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Choose an account")
    #         social_login.choose_a_google_account("zebratest850@gmail.com")
    #     except:
    #         pass
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.check_basic_functionalities()
