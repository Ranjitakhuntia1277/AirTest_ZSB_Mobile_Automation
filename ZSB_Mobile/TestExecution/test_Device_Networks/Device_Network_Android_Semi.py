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


def test_Device_Networks_TestcaseID_45695(self):
    """NEED TO Complete"""
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)

    others.click_add_network_button()

    netw2 = "POCO M3"
    netw2_pass = "12345678"
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)

    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    others.wait_for_appearance_all("Failed to Connect to Wifi Network", 300)
    if not device_networks:
        raise Exception("fails the wordings in the failed connected network")
    device_networks.click_on_cancel_button()

    common_method.wait_for_element_appearance("Connected", 100)
    sleep(2)
    s1 = device_networks.get_network_names()
    if netw2 in s1:
        raise Exception("fails: check the network is not added in the saved network list.")
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


def test_Device_Networks_TestcaseID_45696(self):
    # stop_app("com.zebra.soho_app")
    # start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    self.go_till_printer_wifi_page(1)
    others.click_add_network_button()
    netw1 = "NESTWIFI"
    netw1_pass = "123456789"

    netw2 = "POCO M3"
    netw2_pass = "1234567890"
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)
    if not device_networks.check_the_wordings_in_connect_to_network():
        raise Exception("dialog dint pop up or the wordings are wrong")
    device_networks.click_on_cancel_button()
    try:
        device_networks.click_network_by_name(netw2)
    except:
        raise Exception("dialogue of connect to network did not close on clicking cancel button")

    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    try:
        common_method.wait_for_element_appearance_namematches("Printer")
    except:
        raise Exception("did not redirect to the previous page")

    common_method.wait_for_element_appearance_namematches(netw2,60)
    name,status = device_networks.get_the_network_name_and_status()
    if name!="Not Connected" and status!="Not Connected":
        raise Exception("network and status did not get Not Connected")

    device_networks.swap_two_networks(netw1,netw2)

    others.click_apply_changes_button()
    common_method.wait_for_element_appearance("Connected",100)
    name, status = device_networks.get_the_network_name_and_status()
    if name != netw2 or status != "Connected":
        raise Exception("fails : Check the Current Network, Network Status, IP Address would be updated accordingly")


def test_Device_Networks_TestcaseID_45697(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    self.go_till_printer_wifi_page(1)

    name, status = device_networks.get_the_network_name_and_status()
    if status != "Connected":
        raise Exception("fails:Check the Current Network, Network Status, info all are correct.")

    if device_networks.check_add_network_button_enabled():
        raise Exception("Add network is enabled even after adding 5 networks")

def test_Device_Networks_TestcaseID_45699(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    self.go_till_printer_wifi_page(0)

    name, status = device_networks.get_the_network_name_and_status()
    if status != "Not Connected":
        raise Exception("the network shows connected")

    sleep(100)
    others.click_manage_network_button()
    others.click_continue_in_bluetooth_connection_required()
    common_method.wait_for_element_appearance_namematches("Apply Changes")

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

    name,status = device_networks.get_the_network_name_and_status()
    if name!="Not Connected" and status!="Not Connected":
        raise Exception("network and status did not get Not Connected")

    common_method.wait_for_element_appearance("Connected",60)
    name, status = device_networks.get_the_network_name_and_status()
    if name != netw1 or status != "Connected":
        raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")


def test_Device_Networks_TestcaseID_45700(self):

    # stop_app("com.zebra.soho_app")
    # start_app("com.zebra.soho_app")
    # common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)
    name1, status = device_networks.get_the_network_name_and_status()
    s1 = device_networks.get_network_names()

    s1.remove(name1)
    dele_netw = s1[0]
    device_networks.delete_the_network(dele_netw)

    common_method.wait_for_element_appearance_namematches("Deleting")
    s1 = device_networks.get_network_names()
    if dele_netw in s1:
        raise Exception("deleted network is still present")
    common_method.wait_for_element_appearance("Connected",100)

    try:
        device_networks.wait_for_the_printer_to_connect_network(name1)
    except:
        raise Exception("fails: check the network priority is updated and the printer would connect to the highest priority network ")

def test_Device_Networks_TestcaseID_45701(self):

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)

    """bug SMBM-2239"""
    s1 = device_networks.get_network_names()

    dele_netw = s1[0]
    device_networks.delete_the_network(dele_netw)
    print(dele_netw)
    print("\n","new line printed")

    common_method.wait_for_element_appearance_namematches("Deleting")
    sleep(2)
    s1 = device_networks.get_network_names()
    if dele_netw in s1:
        raise Exception("deleted network is still present")
    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    name1, status = device_networks.get_the_network_name_and_status()
    if name1 not in s1:
        raise Exception("fails : to connect to the highest priority network in existing networks")

def test_Device_Networks_TestcaseID_45702(self):

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)

    s1 = device_networks.get_network_names()

    dele_netw = s1[0]
    device_networks.delete_the_network(dele_netw)

    common_method.wait_for_element_appearance_namematches("Deleting")
    sleep(2)

    common_method.wait_for_element_appearance("Not Connected",100)
    sleep(2)

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

    common_method.wait_for_element_appearance("Connected",60)
    name, status = device_networks.get_the_network_name_and_status()
    if  status != "Connected":
        raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

def test_Device_Networks_TestcaseID_45703(self):

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    res = others.check_printer_online_status()
    if res != "online":
        raise Exception("printer not in online state")
    others.wait_for_appearance_all("offline")
    sleep(3)
    res = others.check_printer_online_status()
    if res != "offline":
        raise Exception("fails : check the printer would go to offline and back to online")

def test_Device_Networks_TestcaseID_45704(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    sleep(2)
    res = others.check_printer_online_status()
    if res != "offline":
        raise Exception("fails : check the printer would go to offline and back to online")

    self.go_till_printer_wifi_page(1)
    name,status = device_networks.get_the_network_name_and_status()
    if name!="Not Connected" and status!="Not Connected":
        raise Exception("network and status did not get Not Connected")

    others.click_add_network_button()

    netw2 = "POCO M3"
    netw2_pass = "1234567890"
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)

    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    try:
        common_method.wait_for_element_appearance_namematches("Printer")
    except:
        raise Exception("did not redirect to the previous page")

    common_method.wait_for_element_appearance_namematches(netw2,60)
    name,status = device_networks.get_the_network_name_and_status()

    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    name, status = device_networks.get_the_network_name_and_status()
    if name != netw2 or status != "Connected":
        raise Exception("fails : Check the Current Network, Network Status, IP Address would be updated accordingly")

def test_Device_Networks_TestcaseID_45707(self):
    """NEED TO Complete"""
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)

    others.click_add_network_button()

    netw2 = "Redmi"
    netw2_pass = "w45454oldiersss"
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)

    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    others.wait_for_appearance_all("Failed to Connect to Wifi Network",300)
    device_networks.click_on_cancel_button()

    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    s1=device_networks.get_network_names()
    if netw2 in s1:
        raise Exception("fails: check the network is not added in the saved network list.")
    others.click_add_network_button()
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)
    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    others.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
    device_networks.click_on_continue_in_network_disconnect_error()
    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    s1 = device_networks.get_network_names()
    if netw2 not in s1:
        raise Exception("fails: check the network is  added in the saved network list.")
    common_method.wait_for_element_appearance_namematches(netw2,60)

def test_Device_Networks_TestcaseID_45897(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    self.go_till_printer_wifi_page(1)
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

    common_method.wait_for_element_appearance_namematches("Connected", 60)
    name, status = device_networks.get_the_network_name_and_status()
    if name != netw1 or status != "Connected":
        raise Exception(
            "fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

def test_Device_Networks_TestcaseID_47912(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(0)

    sleep(300)

    others.click_manage_network_button()
    common_method.wait_for_element_appearance_namematches("Apply Changes")
    try:
        s1 = device_networks.get_network_names()
    except:
        raise Exception("network names did not shown after rebooting printer")

def test_Device_Networks_TestcaseID_50766(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    others.turn_on_wifi()

    self.check_basic_functionalities()

    device_networks.turn_off_wifi()
    device_networks.turn_on_cellular_data()
    sleep(4)

    self.check_basic_functionalities()

    self.logout_from_the_app()
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    try:
        common_method.wait_for_element_appearance_namematches("Choose an account")
        social_login.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home")

    self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_50767(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    others.turn_on_wifi()

    self.check_basic_functionalities()

    others.open_wifi_settings()
    sleep(3)
    others.select_wifi("POCO M3","1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")

    self.check_basic_functionalities()

    self.logout_from_the_app()
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    try:
        common_method.wait_for_element_appearance_namematches("Choose an account")
        social_login.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home")

    self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_50768(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    others.turn_on_wifi()

    self.check_basic_functionalities()

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

    others.turn_on_wifi()
    sleep(4)
    device_networks.refresh_home_page()

    self.check_basic_functionalities()

    self.logout_from_the_app()
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    try:
        common_method.wait_for_element_appearance_namematches("Choose an account")
        social_login.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home")

    self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_50769(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    others.turn_on_wifi()

    self.check_basic_functionalities()

    others.open_wifi_settings()
    sleep(3)
    others.select_wifi("POCO M3","1234567890")
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

    others.open_wifi_settings()
    sleep(3)
    others.select_wifi("ZGuest", "1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")
    sleep(2)

    sleep(4)

    self.check_basic_functionalities()

    self.logout_from_the_app()
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    try:
        common_method.wait_for_element_appearance_namematches("Choose an account")
        social_login.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home")

    self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_50782(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Open navigation menu")

    device_networks.turn_off_wifi()

    login_page.click_Menu_HamburgerICN()
    others.click_on_my_designs()
    sleep(2)
    if not device_networks.check_the_my_designs_internet_lost_error():
        raise Exception("fails: Check there is an error message showing up on My designs")
    login_page.click_Menu_HamburgerICN()
    others.click_home_button()

    device_networks.refresh_home_page()
    if not device_networks.check_sudden_network_off_error():
        raise Exception("network disconnection error did not pop up")

def test_Device_Networks_TestcaseID_52289(self):
    pass

    others.run_the_command("adb uninstall com.zebra.soho_app")
    sleep(5)

    cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5538.apk"'
    res = others.run_the_command(cmd)
    sleep(10)


    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
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
    except:
        pass
    try:
        common_method.wait_for_element_appearance_namematches("Continue with Google")

        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")

        social_login.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass

    common_method.wait_for_element_appearance_namematches("Home",20)


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



