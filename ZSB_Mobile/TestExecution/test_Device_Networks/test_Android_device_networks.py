#from poco import poco
import time
from airtest.core.api import *
from ...Common_Method import Common_Method
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
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
common_method= Common_Method(poco)
social_login = Social_Login(poco)
device_networks = Device_Networks_Android(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
aps_notification = APS_Notification(poco)


class Test_Android_device_networks():
    pass

    def go_till_printer_wifi_page(self,add_network=0):
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

    # def test_Device_Networks_TestcaseID_45693(self):
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")

        # self.go_till_printer_wifi_page(1)
        # name, status = device_networks.get_the_network_name_and_status()
        # if name != "NESTWIFI" or status != "Connected":
        #     raise Exception("fails:Check the Current Network, Network Status, info all are correct.")
        # others.click_add_network_button()
        # netw1 = "aruba-ap"
        # device_networks.wait_till_the_networks_list()
        # device_networks.click_network_by_name(netw1)
        #
        # try:
        #     common_method.wait_for_element_appearance_namematches("Printer")
        # except:
        #     raise Exception("did not redirect to the previous page")
        # others.wait_for_appearance_all("offline",20)
        # name,status = device_networks.get_the_network_name_and_status()
        # if name!="Not Connected" and status!="Not Connected":
        #     raise Exception("network and status did not get Not Connected")
        # try:
        #     others.wait_for_appearance_all("online",60)
        # except:
        #     raise Exception("Printer is online pop up dint shown up")
        #
        # common_method.wait_for_element_appearance_namematches("Connected",60)
        # name, status = device_networks.get_the_network_name_and_status()
        # if status != "Connected":
        #     raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")



    def test_Device_Networks_TestcaseID_45694(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        self.go_till_printer_wifi_page(1)
        others.click_add_network_button()
        netw1 = "POCO M3"
        netw1_pass = "1234567890"
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

        common_method.wait_for_element_appearance_namematches("Connected",60)
        name, status = device_networks.get_the_network_name_and_status()
        if name != netw1 or status != "Connected":
            raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

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

    def test_Device_Networks_TestcaseID_47943(self):
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


    # def test_Device_Networks_TestcaseID_45693(self):
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")
        #
        # self.go_till_printer_wifi_page(1)
        #
        # others.click_add_network_button()
        # netw1 = "aruba-ap"
        # device_networks.wait_till_the_networks_list()
        # device_networks.click_network_by_name(netw1)
        #
        # try:
        #     common_method.wait_for_element_appearance_namematches("Printer")
        # except:
        #     raise Exception("did not redirect to the previous page")
        # others.wait_for_appearance_all("offline",20)
        # name,status = device_networks.get_the_network_name_and_status()
        # if name!="Not Connected" and status!="Not Connected":
        #     raise Exception("network and status did not get Not Connected")
        # try:
        #     others.wait_for_appearance_all("online",60)
        # except:
        #     raise Exception("Printer is online pop up dint shown up")
        #
        # common_method.wait_for_element_appearance_namematches("Connected",60)
        # name, status = device_networks.get_the_network_name_and_status()
        # if status != "Connected":
        #     raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

    # def test_Device_Networks_TestcaseID_45708(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     self.go_till_printer_wifi_page(1)
    #     others.click_add_network_button()
    #     netw1 = "NESTWIFI"
    #     netw1_pass = "123456789"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw1)
    #     if not device_networks.check_the_wordings_in_connect_to_network():
    #         raise Exception("dialog dint pop up or the wordings are wrong")
    #     device_networks.click_on_cancel_button()
    #     try:
    #         device_networks.click_network_by_name(netw1)
    #     except:
    #         raise Exception("dialogue of connect to network did not close on clicking cancel button")
    #
    #     device_networks.enter_the_password(netw1_pass)
    #     device_networks.click_on_connect()
    #
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Printer is already connected to this network.")
    #     except:
    #         raise Exception("fails: Printer is already connected to this network pop up")

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
    #     common_method.wait_for_element_appearance_namematches(netw2,60)
    #     name,status = device_networks.get_the_network_name_and_status()
    #     if name!="Not Connected" and status!="Not Connected":
    #         raise Exception("network and status did not get Not Connected")
    #
    #     device_networks.swap_two_networks(netw1,netw2)
    #
    #     others.click_apply_changes_button()
    #     common_method.wait_for_element_appearance("Connected",100)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != netw2 or status != "Connected":
    #         raise Exception("fails : Check the Current Network, Network Status, IP Address would be updated accordingly")

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

    # def test_Device_Networks_TestcaseID_45698(self):
    #
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     # common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
    #     name1, status = device_networks.get_the_network_name_and_status()
    #     s1 = device_networks.get_network_names()
    #     others.click_add_network_button()
    #     netw1 = "EVT_ArubaOpen"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw1)
    #
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Printer")
    #     except:
    #         raise Exception("did not redirect to the previous page")
    #
    #     common_method.wait_for_element_appearance("Connected",200)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != name1:
    #         raise Exception("fails : check the Moneybadger would reset and it would still connect to Essid A")
    #
    #     s2 = device_networks.get_network_names()
    #     if netw1 not in s2 or len(s1)+1!=len(s2):
    #         raise Exception('newly added network is not present')

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
    #     common_method.wait_for_element_appearance("Connected",100)
    #
    #     try:
    #         device_networks.wait_for_the_printer_to_connect_network(name1)
    #     except:
    #         raise Exception("fails: check the network priority is updated and the printer would connect to the highest priority network ")

    # def test_Device_Networks_TestcaseID_45701(self):

        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")

        # self.go_till_printer_wifi_page(1)

        # """bug SMBM-2239"""
        # s1 = device_networks.get_network_names()
        #
        # dele_netw = s1[0]
        # device_networks.delete_the_network(dele_netw)
        # print(dele_netw)
        # print("\n","new line printed")
        #
        # common_method.wait_for_element_appearance_namematches("Deleting")
        # sleep(2)
        # s1 = device_networks.get_network_names()
        # if dele_netw in s1:
        #     raise Exception("deleted network is still present")
        # common_method.wait_for_element_appearance("Connected",100)
        # sleep(2)
        # name1, status = device_networks.get_the_network_name_and_status()
        # if name1 not in s1:
        #     raise Exception("fails : to connect to the highest priority network in existing networks")

    # def test_Device_Networks_TestcaseID_45702(self):

        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")
        #
        # self.go_till_printer_wifi_page(1)
        #
        # s1 = device_networks.get_network_names()
        #
        # dele_netw = s1[0]
        # device_networks.delete_the_network(dele_netw)
        #
        # common_method.wait_for_element_appearance_namematches("Deleting")
        # sleep(2)
        #
        # common_method.wait_for_element_appearance("Not Connected",100)
        # sleep(2)
        #
        # others.click_add_network_button()
        #
        # netw1 = "NESTWIFI"
        # netw1_pass = "123456789"
        # device_networks.wait_till_the_networks_list()
        # device_networks.click_network_by_name(netw1)
        #
        # device_networks.click_on_cancel_button()
        # try:
        #     device_networks.click_network_by_name(netw1)
        # except:
        #     raise Exception("dialogue of connect to network did not close on clicking cancel button")
        #
        # device_networks.enter_the_password(netw1_pass)
        # device_networks.click_on_connect()

        # common_method.wait_for_element_appearance("Connected",60)
        # name, status = device_networks.get_the_network_name_and_status()
        # if  status != "Connected":
        #     raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

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
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
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

    def test_Device_Networks_TestcaseID_45706(self):

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)

        s1 = device_networks.get_network_names()
        for i in range(len(s1)):
            dele_netw = s1[i]
            device_networks.delete_the_network(dele_netw)
            common_method.wait_for_element_appearance_namematches("Deleting")
            sleep(2)

        try:
            s1 = device_networks.get_network_names()
            raise Exception("all the networks did not get deleted")
        except ZeroDivisionError:
            pass

        common_method.wait_for_element_appearance("Not Connected")
        name,status = device_networks.get_the_network_name_and_status()

        if name!="Not Connected" and status!="Not Connected":
            raise Exception("network and status did not get Not Connected")

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

        common_method.wait_for_element_appearance_namematches(netw2,60)

    def test_Device_Networks_TestcaseID_45707(self):
        """NEED TO Complete"""
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
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

        others.wait_for_appearance_all("Failed to Connect to Wifi Network",300)
        if not device_networks:
            raise Exception("fails the wordings in the failed connected network")
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
        print(s1)
        if netw2 not in s1:
            raise Exception("fails: check the network is  added in the saved network list.")
        common_method.wait_for_element_appearance_namematches(netw2,60)

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


    def test_Device_Networks_TestcaseID_45807(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")

        """SMBM-1774"""
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

        others.open_wifi_settings()
        sleep(3)
        others.select_wifi("POCO M3","1234567890")
        sleep(1)

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        sleep(2)
        res = others.check_home_page()
        if not res:
            raise Exception("home page not shown")
        recently_printed_labels_after = others.get_recently_printed_labels()

        res = others.check_same_after_switching_network(recently_printed_labels_before,recently_printed_labels_after)
        if not res:
            print("changing network not showing files properly")

        sleep(4)

        """For Common Design"""
        others.open_wifi_settings()
        others.select_wifi("ZGuest","1234567890")
        sleep(1)

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_common_designs_button()
        sleep(2)
        netw_2_common_designs = others.get_designs_visible_designs()

        res = others.check_same_after_switching_network(netw_1_common_designs,netw_2_common_designs)
        if not res:
            print("changing network not showing files properly")

        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        """For My Design"""
        others.open_wifi_settings()
        sleep(1)

        """Pass network 2 here"""
        others.select_wifi("POCO M3","1234567890")
        sleep(1)

        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_designs()
        common_method.wait_for_element_appearance_namematches("Showing")
        netw_2_my_designs = others.get_designs_visible_designs()

        res = others.check_same_after_switching_network(netw_1_my_designs,netw_2_my_designs)
        if not res:
            print("changing network not showing files properly")

        """For my data"""

        login_page.click_Menu_HamburgerICN()
        others.click_home_button()

        others.open_wifi_settings()
        sleep(1)
        others.select_wifi("ZGuest","1234567890")
        sleep(1)

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_data()
        sleep(2)
        netw_2_my_data = others.get_my_data_all()

        res = others.check_same_after_switching_network(netw_1_my_data,netw_2_my_data)
        if not res:
            print("changing network not showing files properly")

    def test_Device_Networks_TestcaseID_46963(self):
        pass

        stop_app("com.zebra.soho_app")
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

        try:
            others.click_on_allow()
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Apply",20)
        others.scroll_down()
        others.click_add_network_button()
        common_method.wait_for_element_appearance_namematches("Network")
        sleep(5)

        """Pass the name of the netowrk here"""
        network2= "NESTWIFI"
        password="123456789"
        others.select_network_and_enter_password(network2,password)
        try:
            others.click_enter_network_manually()
            others.enter_network_name(network2)
            others.click_join_network()
        except:
            pass

        sleep(3)
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()
        res = others.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("dialogue dint show")
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply")

        others.scroll_down()

        res,res1 = others.get_network_names()

        others.swap_two_networks(res1[1],res1[0])
        res = others.check_apply_changes_button_clickable()
        if not res:
            raise Exception("Apply changes button not clickable")
        others.click_apply_changes_button()
        sleep(5)
        res = others.check_apply_changes_button_clickable()
        if res:
            raise Exception("Apply changes button  clickable")
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(5)
        res,res1 = others.get_network_names()

        others.delete_one_network(res1[0])
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(2)

        try:
            common_method.wait_for_element_appearance_namematches(res1[0])
            raise Exception("network dint get deleted")
        except:
            pass
        sleep(1)

        login_page.click_Menu_HamburgerICN()

        others.click_home_button()

    # def test_Device_Networks_TestcaseID_47794(self):
    #
    #
    #     # stop_app("com.zebra.soho_app")
    #     # start_app("com.zebra.soho_app")
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Sign In")
    #     except:
    #         pass
    #
    #     try:
    #         login_page.click_Menu_HamburgerICN()
    #         social_login.click_on_profile_edit()
    #         social_login.scroll_down(1)
    #         social_login.click_log_out_button()
    #         social_login.wait_for_element_appearance("Sign In", 10)
    #     except:
    #         pass
    #
    #     login_page.click_loginBtn()
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Continue with Google")
    #
    #         login_page.click_Loginwith_Google()
    #         common_method.wait_for_element_appearance_textmatches("Choose an account")
    #
    #         social_login.choose_a_google_account("zebratest850@gmail.com")
    #     except:
    #         pass
    #     social_login.wait_for_element_appearance("Home",10)
    #
    #     stop_app("com.zebra.soho_app")
    #
    #     device_networks.turn_off_wifi()
    #
    #     start_app("com.zebra.soho_app")
    #
    #     if not device_networks.check_internet_disconnect_error():
    #         raise Exception("internet disconnection error did not pop up")
    #     sleep(1)
    #     others.turn_on_wifi()
    #     sleep(1)

    def check_basic_functionalities(self):
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

    def logout_from_the_app(self):
        try:
            login_page.click_Menu_HamburgerICN()
        except:
            pass

        others.click_on_profile_edit()
        others.click_log_out_button()
        common_method.wait_for_element_appearance_namematches("Sign In")


    # def test_Device_Networks_TestcaseID_50768(self):
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")
        # others.turn_on_wifi()
        #
        # self.check_basic_functionalities()
        #
        # device_networks.turn_off_wifi()
        # sleep(1)
        # device_networks.refresh_home_page()
        # sleep(2)
        # if not device_networks.check_sudden_network_off_error():
        #     raise Exception("network disconnection error did not pop up")
        # sleep(2)
        # device_networks.click_on_continue_in_network_disconnect_error()
        # try:
        #     device_networks.click_on_continue_in_network_disconnect_error()
        # except:
        #     pass
        # try:
        #     device_networks.click_on_continue_in_network_disconnect_error()
        # except:
        #     pass
        #
        # others.turn_on_wifi()
        # sleep(4)
        # device_networks.refresh_home_page()
        #
        # self.check_basic_functionalities()
        #
        # self.logout_from_the_app()
        # login_page.click_loginBtn()
        # common_method.wait_for_element_appearance_namematches("Continue with Google")
        # login_page.click_Loginwith_Google()
        # try:
        #     common_method.wait_for_element_appearance_namematches("Choose an account")
        #     social_login.choose_a_google_account("zebratest850@gmail.com")
        # except:
        #     pass
        # common_method.wait_for_element_appearance_namematches("Home")
        #
        # self.check_basic_functionalities()

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


    # def test_Device_Networks_TestcaseID_50767(self):
        # # stop_app("com.zebra.soho_app")
        # # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")
        # others.turn_on_wifi()
        #
        # self.check_basic_functionalities()
        #
        # others.open_wifi_settings()
        # sleep(3)
        # others.select_wifi("POCO M3","1234567890")
        # sleep(1)
        #
        # start_app("com.zebra.soho_app")
        #
        # self.check_basic_functionalities()
        #
        # self.logout_from_the_app()
        # login_page.click_loginBtn()
        # common_method.wait_for_element_appearance_namematches("Continue with Google")
        # login_page.click_Loginwith_Google()
        # try:
        #     common_method.wait_for_element_appearance_namematches("Choose an account")
        #     social_login.choose_a_google_account("zebratest850@gmail.com")
        # except:
        #     pass
        # common_method.wait_for_element_appearance_namematches("Home")
        #
        # self.check_basic_functionalities()

    def test_Device_Networks_TestcaseID_52290(self):
        pass

        stop_app("com.zebra.soho_app")
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

        try:
            others.click_on_allow()
        except:
            pass

        name,status = device_networks.get_the_network_name_and_status()
        if status!="Connected":
            raise Exception("no network is connected to the device")

        device_networks.allow_nearby_devices_permission(0)

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
        common_method.wait_for_element_appearance("Connected",100)

    def test_Device_Networks_TestcaseID_52291(self):
        pass

        device_networks.allow_nearby_devices_permission(0)

        stop_app("com.zebra.soho_app")
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

    def test_Device_Networks_TestcaseID_52289(self):
        pass

        # others.run_the_command("adb uninstall com.zebra.soho_app")
        # sleep(5)
        #
        # cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5538.apk"'
        # res = others.run_the_command(cmd)
        # sleep(10)
        #
        #
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # try:
        #     try:
        #         others.click_on_allow()
        #     except:
        #         pass
        #     try:
        #         others.click_on_allow()
        #     except:
        #         pass
        #     social_login.wait_for_element_appearance("Sign In", 20)
        #     try:
        #         others.click_on_allow()
        #     except:
        #         pass
        #     login_page.click_loginBtn()
        # except:
        #     pass
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


    def test_Device_Networks_TestcaseID_52292(self):
        pass

        cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5538.apk"'

        res = others.run_the_command(cmd)
        sleep(10)
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        try:
            social_login.wait_for_element_appearance("Sign In", 10)

            login_page.click_loginBtn()
            try:
                common_method.wait_for_element_appearance_namematches("Continue with Google")

                login_page.click_Loginwith_Google()
                common_method.wait_for_element_appearance_textmatches("Choose an account")

                social_login.choose_a_google_account("zebratest850@gmail.com")
            except:
                pass
            social_login.wait_for_element_appearance("Home",10)
        except:
            pass

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

        try:
            others.click_on_allow()
        except:
            pass

        name,status = device_networks.get_the_network_name_and_status()
        if status!="Connected":
            raise Exception("no network is connected to the device")

        device_networks.allow_nearby_devices_permission(0)

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
        common_method.wait_for_element_appearance("Connected",100)



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

    # def test_Device_Networks_TestcaseID_50713(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #     others.turn_on_wifi()
    #
    #     self.check_basic_functionalities()
    #
    #     others.open_wifi_settings()
    #     sleep(3)
    #     others.select_wifi("POCO M3","1234567890")
    #     sleep(1)
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

#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45897():
    """Adding New network: Add Essids by using another phone."""


    """"start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page.click_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Security_Open()
    app_settings_page.click_WPA_PSK()
    app_settings_page.click_Keyboard_back_Icon()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page.Verify_Added_Network()
    """stop the app"""
    common_method.Stop_The_App()
# # # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""























