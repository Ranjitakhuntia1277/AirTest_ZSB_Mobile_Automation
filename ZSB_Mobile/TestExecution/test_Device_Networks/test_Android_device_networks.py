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

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method=Common_Method(poco)
social_login = Social_Login(poco)
device_networks = Device_Networks_Android(poco)

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

    # def test_Device_Networks_TestcaseID_45694(self):
    #     # self.go_till_printer_wifi_page(1)
    #     # others.click_add_network_button()
    #     netw1 = "POCO M3"
    #     netw1_pass = "1234567890"
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
    #         common_method.wait_for_element_appearance_namematches("Printer")
    #     except:
    #         raise Exception("did not redirect to the previous page")
    #
    #     name,status = device_networks.get_the_network_name_and_status()
    #     if name!="Not Connected" and status!="Not Connected":
    #         raise Exception("network and status did not get Not Connected")
    #
    #     common_method.wait_for_element_appearance_namematches("Connected",60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if name != netw1 or status != "Connected":
    #         raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

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

    def test_Device_Networks_TestcaseID_45698(self):

        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)
        name1, status = device_networks.get_the_network_name_and_status()
        s1 = device_networks.get_network_names()

        s1.remove(name1)






    




















