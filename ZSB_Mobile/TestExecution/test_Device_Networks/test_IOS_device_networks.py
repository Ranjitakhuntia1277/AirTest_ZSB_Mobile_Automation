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


class Test_Android_device_networks():
    pass

    def go_till_printer_wifi_page(self,add_network=0):
        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        if add_network:
            device_networks.click_manage_network_button()
            device_networks.click_continue_in_bluetooth_connection_required()
            common_method.wait_for_element_appearance_namematches("Apply Changes")

    def t_100(self,add_network=0):
        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        if add_network:
            device_networks.click_manage_network_button()
            device_networks.click_continue_in_bluetooth_connection_required()
            common_method.wait_for_element_appearance_namematches("Apply Changes")

    def test_Device_Networks_TestcaseID_45693(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)
        name, status = device_networks.get_the_network_name_and_status()
        if name != "NESTWIFI" or status != "Connected":
            raise Exception("fails:Check the Current Network, Network Status, info all are correct.")
        device_networks.click_add_network_button()
        netw1 = "aruba-ap"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")
        device_networks.wait_for_appearance_all("offline",20)
        name,status = device_networks.get_the_network_name_and_status()
        if name!="Not Connected" and status!="Not Connected":
            raise Exception("network and status did not get Not Connected")
        try:
            device_networks.wait_for_appearance_all("online",60)
        except:
            raise Exception("Printer is online pop up dint shown up")

        common_method.wait_for_element_appearance_namematches("Connected",60)
        name, status = device_networks.get_the_network_name_and_status()
        if status != "Connected":
            raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

    def test_Device_Networks_TestcaseID_45694(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        self.go_till_printer_wifi_page(1)
        device_networks.click_add_network_button()
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

    def test_Device_Networks_TestcaseID_47943(self):
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


    # def test_Device_Networks_TestcaseID_45693(self):
    #     stop_app("com.zebra.soho_app")
    #     start_app("com.zebra.soho_app")
    #     common_method.wait_for_element_appearance_namematches("Home")
    #
    #     self.go_till_printer_wifi_page(1)
    #
    #     device_networks.click_add_network_button()
    #     netw1 = "aruba-ap"
    #     device_networks.wait_till_the_networks_list()
    #     device_networks.click_network_by_name(netw1)
    #
    #     try:
    #         common_method.wait_for_element_appearance_namematches("Printer")
    #     except:
    #         raise Exception("did not redirect to the previous page")
    #     device_networks.wait_for_appearance_all("offline",20)
    #     name,status = device_networks.get_the_network_name_and_status()
    #     if name!="Not Connected" and status!="Not Connected":
    #         raise Exception("network and status did not get Not Connected")
    #     try:
    #         device_networks.wait_for_appearance_all("online",60)
    #     except:
    #         raise Exception("Printer is online pop up dint shown up")
    #
    #     common_method.wait_for_element_appearance_namematches("Connected",60)
    #     name, status = device_networks.get_the_network_name_and_status()
    #     if status != "Connected":
    #         raise Exception("fails : check Current Network, Network Status, IP Address all values are updated as the Essid just choose	")

    def test_Device_Networks_TestcaseID_45708(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
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
            common_method.wait_for_element_appearance_namematches("Printer is already connected to this network.")
        except:
            raise Exception("fails: Printer is already connected to this network pop up")

    def test_Device_Networks_TestcaseID_45698(self):

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        self.go_till_printer_wifi_page(1)
        name1, status = device_networks.get_the_network_name_and_status()
        s1 = device_networks.get_network_names()
        device_networks.click_add_network_button()
        netw1 = "EVT_ArubaOpen"
        device_networks.wait_till_the_networks_list()
        device_networks.click_network_by_name(netw1)

        try:
            common_method.wait_for_element_appearance_namematches("Printer")
        except:
            raise Exception("did not redirect to the previous page")

        common_method.wait_for_element_appearance("Connected",200)
        name, status = device_networks.get_the_network_name_and_status()
        if name != name1:
            raise Exception("fails : check the Moneybadger would reset and it would still connect to Essid A")

        s2 = device_networks.get_network_names()
        if netw1 not in s2 or len(s1)+1!=len(s2):
            raise Exception('newly added network is not present')

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

        device_networks.click_add_network_button()

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

    def test_Device_Networks_TestcaseID_46963(self):
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

        common_method.wait_for_element_appearance_namematches("Apply",20)
        device_networks.scroll_down()
        device_networks.click_add_network_button()
        common_method.wait_for_element_appearance_namematches("Network")
        sleep(5)

        """Pass the name of the netowrk here"""
        network2= "NESTWIFI"
        password="123456789"
        device_networks.select_network_and_enter_password(network2,password)
        try:
            device_networks.click_enter_network_manually()
            device_networks.enter_network_name(network2)
            device_networks.click_join_network()
        except:
            pass

        sleep(3)
        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()

        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_wifi_button()
        device_networks.click_manage_network_button()
        res = device_networks.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("dialogue dint show")
        device_networks.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply")

        device_networks.scroll_down()

        res,res1 = device_networks.get_network_names()

        device_networks.swap_two_networks(res1[1],res1[0])
        res = device_networks.check_apply_changes_button_clickable()
        if not res:
            raise Exception("Apply changes button not clickable")
        device_networks.click_apply_changes_button()
        sleep(5)
        res = device_networks.check_apply_changes_button_clickable()
        if res:
            raise Exception("Apply changes button  clickable")
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(5)
        res,res1 = device_networks.get_network_names()

        device_networks.delete_one_network(res1[0])
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(2)

        try:
            common_method.wait_for_element_appearance_namematches(res1[0])
            raise Exception("network dint get deleted")
        except:
            pass
        sleep(1)

        login_page.click_Menu_HamburgerICN()

        device_networks.click_home_button()

    def test_Device_Networks_TestcaseID_47794(self):


        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Sign In")
        except:
            pass

        try:
            login_page.click_Menu_HamburgerICN()
            device_networks.click_on_profile_edit()
            device_networks.scroll_down()
            device_networks.click_log_out_button()
            device_networks.wait_for_element_appearance("Sign In", 10)
        except:
            pass

        login_page.click_loginBtn()
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")

            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            device_networks.choose_a_google_account("zebratest850@gmail.com")
        except:
            pass
        device_networks.wait_for_element_appearance("Home",10)

        stop_app("com.zebra.soho_app")

        device_networks.turn_off_wifi()

        start_app("com.zebra.soho_app")

        if not device_networks.check_internet_disconnect_error():
            raise Exception("internet disconnection error did not pop up")
        sleep(1)
        """CURRRENTY DONT WORK FOR IOS , NEED TO CHANGE"""
        device_networks.turn_on_wifi()
        sleep(1)

    def check_basic_functionalities(self):
        """printing test label"""
        login_page.click_Menu_HamburgerICN()
        device_networks.click_Printer_Settings()
        device_networks.select_first_printer()
        device_networks.click_test_print()
        try:
            device_networks.wait_for_appearance_all("Print Complete")
            sleep(2)
        except:
            pass

        device_networks.change_Printer_Darkness_level(70)
        device_networks.change_Printer_Darkness_level(50)
        device_networks.wait_for_appearance_all("updated")
        sleep(2)

        login_page.click_Menu_HamburgerICN()
        device_networks.click_common_designs_button()
        device_networks.wait_for_appearance_all("Address")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_on_my_designs()
        device_networks.wait_for_appearance_all("My Designs")

        login_page.click_Menu_HamburgerICN()
        device_networks.click_home_button()

    def logout_from_the_app(self):
        try:
            login_page.click_Menu_HamburgerICN()
        except:
            pass

        device_networks.click_on_profile_edit()
        device_networks.click_log_out_button()
        common_method.wait_for_element_appearance_namematches("Sign In")




















