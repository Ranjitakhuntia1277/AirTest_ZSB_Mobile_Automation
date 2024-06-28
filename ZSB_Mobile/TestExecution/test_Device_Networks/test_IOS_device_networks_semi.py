from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco


from airtest.core.api import connect_device


uuid = "00008103-000C718814E3401E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)
auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])

#start_app("com.zebra.soho_app")


from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Device_Networks.Device_Network_IOS import Device_Networks_IOS
from ZSB_Mobile.Common_Method import *


login_page = Login_Screen(poco)
device_networks = Device_Networks_IOS(poco)
common_method=Common_Method(poco)


def test_Device_Networks_TestcaseID_52292(self):
    pass

    cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5538.apk"'

    res = device_networks.run_the_command(cmd)
    sleep(10)
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")

    try:
        device_networks.wait_for_element_appearance("Sign In", 10)

        login_page.click_loginBtn()
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")

            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass
        device_networks.wait_for_element_appearance("Home", 10)
    except:
        pass

    common_method.wait_for_element_appearance_namematches("Home")

    login_page.click_Menu_HamburgerICN()
    device_networks.click_Printer_Settings()
    device_networks.select_first_printer()
    device_networks.click_wifi_button()
    device_networks.click_manage_network_button()

    res = device_networks.check_bluetooth_connection_required_diloge()

    if not res:
        raise Exception("bluetooth dialogue dint show")
    device_networks.click_continue_in_bluetooth_connection_required()

    try:
        device_networks.click_on_allow()
    except:
        pass

    name, status = device_networks.get_the_network_name_and_status()
    if status != "Connected":
        raise Exception("no network is connected to the device")

    # device_networks.allow_nearby_devices_permission(0)
    common_method.show_message("go to settings and turn of near by device permission")

    start_app("com.zebra.soho_app")

    common_method.wait_for_element_appearance_namematches("Home")

    login_page.click_Menu_HamburgerICN()
    device_networks.click_Printer_Settings()
    device_networks.select_first_printer()
    device_networks.click_wifi_button()
    device_networks.click_manage_network_button()

    res = device_networks.check_bluetooth_connection_required_diloge()

    if not res:
        raise Exception("bluetooth dialogue dint show")
    device_networks.click_continue_in_bluetooth_connection_required()

    device_networks.click_on_allow()

    common_method.wait_for_element_appearance_namematches("Apply Changes")
    name, status = device_networks.get_the_network_name_and_status()
    if status != "Connected":
        raise Exception("no network is connected to the device")

    netw1 = "EVT_ArubaOpen"
    device_networks.click_add_network_button()
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw1)

    try:
        common_method.wait_for_element_appearance_namematches("Printer")
    except:
        raise Exception("did not redirect to the previous page")
    common_method.wait_for_element_appearance("Connected", 100)

def test_Device_Networks_TestcaseID_50713(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        device_networks.turn_on_wifi()

        self.check_basic_functionalities()

        # device_networks.open_wifi_settings()
        # sleep(3)
        # device_networks.select_wifi("POCO M3","1234567890")
        # sleep(1)
        common_method.show_message("select different network")


        start_app("com.zebra.soho_app")

        self.check_basic_functionalities()

        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")

        self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_52291(self):
        pass

        # device_networks.allow_nearby_devices_permission(0)
        common_method.show_message("complete the setup conditions")

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        device_networks.click_manage_network_button()

        res = device_networks.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        device_networks.click_continue_in_bluetooth_connection_required()

        try:
            device_networks.click_on_allow()
        except:
            pass

        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")
        try:
            s1 = device_networks.get_network_names()
        except:
            raise Exception("network names not displayed")


def test_Device_Networks_TestcaseID_52290(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        device_networks.click_manage_network_button()

        res = device_networks.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        device_networks.click_continue_in_bluetooth_connection_required()

        try:
            device_networks.click_on_allow()
        except:
            pass

        name,status = device_networks.get_the_network_name_and_status()
        if status!="Connected":
            raise Exception("no network is connected to the device")

        # device_networks.allow_nearby_devices_permission(0)
        common_method.show_message("go to settings and turn off nearby device permission")

        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        device_networks.click_manage_network_button()

        res = device_networks.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        device_networks.click_continue_in_bluetooth_connection_required()

        device_networks.click_on_allow()

        common_method.wait_for_element_appearance_namematches("Apply Changes")
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")


        netw1 = "EVT_ArubaOpen"
        device_networks.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        common_method.wait_for_element_appearance("Connected",100)


def test_Device_Networks_TestcaseID_50767(self):
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        device_networks.turn_on_wifi()

        self.check_basic_functionalities()
        #
        # device_networks.open_wifi_settings()
        # sleep(3)
        # device_networks.select_wifi("POCO M3","1234567890")
        # sleep(1)
        common_method.show_message("select different network")


        start_app("com.zebra.soho_app")

        self.check_basic_functionalities()

        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")

        self.check_basic_functionalities()


def test_Device_Networks_TestcaseID_50769(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        device_networks.turn_on_wifi()

        self.check_basic_functionalities()
        #
        # device_networks.open_wifi_settings()
        # sleep(3)
        # device_networks.select_wifi("POCO M3","1234567890")
        # sleep(1)
        common_method.show_message("select different network")


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
        #
        # device_networks.open_wifi_settings()
        # sleep(3)
        # device_networks.select_wifi("ZGuest", "1234567890")
        # sleep(1)
        common_method.show_message("select different network")


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
            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home")

        self.check_basic_functionalities()

def test_Device_Networks_TestcaseID_45807(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")

        """SMBM-1774"""
        recently_printed_labels_before = device_networks.get_recently_printed_labels()

        login_page.click_Menu_HamburgerICN()
        device_networks.click_common_designs_button()
        sleep(2)
        netw_1_common_designs = device_networks.get_designs_visible_designs()
        login_page.click_Menu_HamburgerICN()
        device_networks.click_on_my_designs()
        common_method.wait_for_element_appearance_namematches("Showing")
        netw_1_my_designs = device_networks.get_designs_visible_designs()
        login_page.click_Menu_HamburgerICN()
        device_networks.click_on_my_data()
        sleep(2)
        netw_1_my_data = device_networks.get_my_data_all()
        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()

        # device_networks.open_wifi_settings()
        # sleep(3)
        # device_networks.select_wifi("POCO M3","1234567890")
        # sleep(1)
        common_method.show_message("select a different wifi")

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()
        sleep(2)
        res = device_networks.check_home_page()
        if not res:
            raise Exception("home page not shown")
        recently_printed_labels_after = device_networks.get_recently_printed_labels()

        res = device_networks.check_same_after_switching_network(recently_printed_labels_before,recently_printed_labels_after)
        if not res:
            print("changing network not showing files properly")

        sleep(4)

        """For Common Design"""
        # device_networks.open_wifi_settings()
        # device_networks.select_wifi("ZGuest","1234567890")
        # sleep(1)
        common_method.show_message("select different network")

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        device_networks.click_common_designs_button()
        sleep(2)
        netw_2_common_designs = device_networks.get_designs_visible_designs()

        res = device_networks.check_same_after_switching_network(netw_1_common_designs,netw_2_common_designs)
        if not res:
            print("changing network not showing files properly")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()
        """For My Design"""
        # device_networks.open_wifi_settings()
        # sleep(1)
        #
        # """Pass network 2 here"""
        # device_networks.select_wifi("POCO M3","1234567890")
        # sleep(1)
        common_method.show_message("select diferrent network")


        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        device_networks.click_on_my_designs()
        common_method.wait_for_element_appearance_namematches("Showing")
        netw_2_my_designs = device_networks.get_designs_visible_designs()

        res = device_networks.check_same_after_switching_network(netw_1_my_designs,netw_2_my_designs)
        if not res:
            print("changing network not showing files properly")

        """For my data"""

        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()

        # device_networks.open_wifi_settings()
        # sleep(1)
        # device_networks.select_wifi("ZGuest","1234567890")
        # sleep(1)
        common_method.show_message("select different network")


        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        device_networks.click_on_my_data()
        sleep(2)
        netw_2_my_data = device_networks.get_my_data_all()

        res = device_networks.check_same_after_switching_network(netw_1_my_data,netw_2_my_data)
        if not res:
            print("changing network not showing files properly")

def test_Device_Networks_TestcaseID_45695(self):
    """NEED TO Complete"""
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    self.go_till_printer_wifi_page(1)

    device_networks.click_add_network_button()

    netw2 = "POCO M3"
    netw2_pass = "12345678"
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)

    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    device_networks.wait_for_appearance_all("Failed to Connect to Wifi Network",300)
    if not device_networks:
        raise Exception("fails the wordings in the failed connected network")
    device_networks.click_on_cancel_button()

    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    s1=device_networks.get_network_names()
    if netw2 in s1:
        raise Exception("fails: check the network is not added in the saved network list.")
    device_networks.click_add_network_button()
    device_networks.wait_till_the_networks_list()
    device_networks.click_network_by_name(netw2)
    device_networks.enter_the_password(netw2_pass)
    device_networks.click_on_connect()

    device_networks.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
    device_networks.click_on_continue_in_network_disconnect_error()
    common_method.wait_for_element_appearance("Connected",100)
    sleep(2)
    s1 = device_networks.get_network_names()
    print(s1)
    if netw2 not in s1:
        raise Exception("fails: check the network is  added in the saved network list.")
    common_method.wait_for_element_appearance_namematches(netw2,60)

def test_Device_Networks_TestcaseID_45696(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    self.go_till_printer_wifi_page(1)
    device_networks.click_add_network_button()
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

    device_networks.click_apply_changes_button()
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
    device_networks.click_manage_network_button()
    device_networks.click_continue_in_bluetooth_connection_required()
    common_method.wait_for_element_appearance_namematches("Apply Changes")

    device_networks.click_add_network_button()
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

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

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

    device_networks.click_add_network_button()

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
    res = device_networks.check_printer_online_status()
    if res != "online":
        raise Exception("printer not in online state")
    device_networks.wait_for_appearance_all("offline")
    sleep(3)
    res = device_networks.check_printer_online_status()
    if res != "offline":
        raise Exception("fails : check the printer would go to offline and back to online")

def test_Device_Networks_TestcaseID_45704(self):
    # stop_app("com.zebra.soho_app")
    # start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    sleep(2)
    res = device_networks.check_printer_online_status()
    if res != "offline":
        raise Exception("fails : check the printer would go to offline and back to online")

    self.go_till_printer_wifi_page(1)
    name,status = device_networks.get_the_network_name_and_status()
    if name!="Not Connected" and status!="Not Connected":
        raise Exception("network and status did not get Not Connected")

    device_networks.click_add_network_button()

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
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)

        device_networks.click_add_network_button()

        netw2 = "POCO M3"
        netw2_pass = "1234567890"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)

        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        device_networks.wait_for_appearance_all("Failed to Connect to Wifi Network", 300)
        device_networks.click_on_cancel_button()

        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        if netw2 in s1:
            raise Exception("fails: check the network is not added in the saved network list.")
        device_networks.click_add_network_button()
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw2)
        device_networks.enter_the_password(netw2_pass)
        device_networks.click_on_connect()

        device_networks.wait_for_appearance_all("Failed to Connect to Wifi Network", 400)
        device_networks.click_on_continue_in_network_disconnect_error()
        common_method.wait_for_element_appearance("Connected", 100)
        sleep(2)
        s1 = device_networks.get_network_names()
        if netw2 not in s1:
            raise Exception("fails: check the network is  added in the saved network list.")
        common_method.wait_for_element_appearance_namematches(netw2, 60)

def test_Device_Networks_TestcaseID_45897(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    self.go_till_printer_wifi_page(1)
    device_networks.click_add_network_button()
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

    device_networks.click_manage_network_button()
    common_method.wait_for_element_appearance_namematches("Apply Changes")
    try:
        s1 = device_networks.get_network_names()
    except:
        raise Exception("network names did not shown after rebooting printer")

def test_Device_Networks_TestcaseID_50766(self):
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    device_networks.turn_on_wifi()

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
        device_networks.choose_a_google_account("zebratest850@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home")

    self.check_basic_functionalities()
def test_Device_Networks_TestcaseID_50768(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        device_networks.turn_on_wifi()

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

        device_networks.turn_on_wifi()
        sleep(4)
        device_networks.refresh_home_page()

        self.check_basic_functionalities()

        self.logout_from_the_app()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        try:
            common_method.wait_for_element_appearance_namematches("Choose an account")
            device_networks.choose_a_google_account("zebratest850@gmail.com")
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
    device_networks.click_on_my_designs()
    sleep(2)
    if not device_networks.check_the_my_designs_internet_lost_error():
        raise Exception("fails: Check there is an error message showing up on My designs")
    login_page.click_Menu_HamburgerICN()
    device_networks.click_home_button()

    device_networks.refresh_home_page()
    if not device_networks.check_sudden_network_off_error():
        raise Exception("network disconnection error did not pop up")

def test_Device_Networks_TestcaseID_52289(self):
        pass

        device_networks.run_the_command("adb uninstall com.zebra.soho_app")
        sleep(5)

        cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5538.apk"'
        res = device_networks.run_the_command(cmd)
        sleep(10)


        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            try:
                device_networks.click_on_allow()
            except:
                pass
            try:
                device_networks.click_on_allow()
            except:
                pass
            device_networks.wait_for_element_appearance("Sign In", 20)
            try:
                device_networks.click_on_allow()
            except:
                pass
            login_page.click_loginBtn()
        except:
            pass
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")

            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Home",20)


        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        device_networks.click_manage_network_button()

        res = device_networks.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        device_networks.click_continue_in_bluetooth_connection_required()

        try:
            device_networks.click_on_allow()
        except:
            pass

        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("no network is connected to the device")
        try:
            s1 = device_networks.get_network_names()
        except:
            raise Exception("network names not displayed")







