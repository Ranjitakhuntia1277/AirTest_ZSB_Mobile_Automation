from platform import platform

import pytest
from airtest.core.api import *
from airtest.core.cv import Template
# from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import device as current_device
import os
__author__ = "zebra"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.ios import iosPoco
poco = iosPoco()

common_method = Common_Method(poco)
def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",a)
class Device_Networks_IOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Settings_Btn = "Printer Settings"
        self.wi_fi_button = "Wi-Fi\nTab 2 of 2"
        self.manage_network_button = "Manage Networks"
        self.add_network_button = "Add Network"
        self.continue_button = "Continue"
        self.common_designs_button = "Common Designs"
        self.my_designs_button = "My Designs"
        self.my_data_button = "My Data"
        self.click_Home_btn = "Home"
        self.profile_edit = "Button"
        self.log_out_button = "Log Out"
        self.test_print = "Test Print"

    def wait_till_the_networks_list(self):
        try:
            self.poco(nameMatches=".*NESTWIFI.*").wait_for_appearance(timeout=30)
        except:
            pass

    def click_add_network_button(self):
        while not self.poco("Add Network").exists():
            self.poco.scroll()
        add_network = self.poco(self.add_network_button)
        add_network.click()

    def change_Printer_Darkness_level(self,new_value):

        common_method.show_message("Change the darkness level to "+str(new_value))

    def click_Printer_Settings(self):
        # self.poco("My Designs").scroll()

        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def wait_for_element_appearance(self,element, time_out=20):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def choose_a_google_account(self,gmail):
        while not self.poco(label=gmail).exists():
            self.poco.scroll()
        a = self.poco(label=gmail).click()

    def click_test_print(self):
        while not self.poco("Test Print").exists():
            self.poco.scroll()
        test_prin = self.poco(self.test_print)
        test_prin.click()


    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        self.run_the_command(cmd)

    def select_first_printer(self):
        self.poco(nameMatches="(?s).*Common.*").parent().child()[1].click()

    def click_wifi_button(self):
        wifi_btn = self.poco(self.wi_fi_button)
        wifi_btn.click()

    def click_manage_network_button(self):
        m_n_btn = self.poco(self.manage_network_button)
        m_n_btn.click()

    def click_continue_in_bluetooth_connection_required(self):
        self.poco(self.continue_button).click()
    def click_network_by_name(self,name):
        count=0
        while not self.poco(nameMatches=".*"+name+".*").exists() and count<10:
            self.poco.scroll()
            count+=1
        self.poco(nameMatches=".*"+name+".*").click()

    def wait_for_appearance_all(self,elem,time_out=20):
        self.poco(nameMatches="(?s).*"+elem+".*").wait_for_appearance(timeout=time_out)

    def check_the_wordings_in_connect_to_network(self):
        a = self.poco(nameMatches=".*Please enter the password.*"+".*the printer to this network.*").exists()
        b = self.poco(nameMatches=".*Connect to Network.*").exists()

        return a and b


    def check_printer_online_status(self):
        child_names = [child.get_name() for child in self.poco(nameMatches="(?s).*prints left.*")]
        modified_list = [item.split('\n') for item in child_names]

        return modified_list[0][0]

    def click_on_cancel_button(self):
        try:
            self.poco("Cancel").click()
        except:
            self.poco("cancel").click()

    def enter_the_password(self,password):
        poco("Enter Password").click()
        text(password)
        sleep(2)

    def click_apply_changes_button(self):
        self.poco("Apply Changes").click()

    def click_on_connect(self):
        self.poco("Connect").click()

    def check_bluetooth_connection_required_diloge(self):

        a = self.poco(label="Bluetooth Connection Required").get_name()
        return a

    def click_on_allow_for_notification(self):
        try:
            self.poco(nameMatches=".*allow.*").click()
        except:
            self.poco(labelMatches=".*allow.*").click()

    def click_on_allow(self):
        self.poco(nameMatches=".*allow.*").click()

    def scroll_down(self):
        self.poco.scroll()

    def get_the_network_name_and_status(self):
        try:
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a,b
        except:
            self.poco.swipe([0.5,0.4],[0.5,0.9])
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a, b

    def click_log_out_button(self):
        log_out_btn = self.poco(self.log_out_button)
        log_out_btn.click()

    def select_network_and_enter_password(self,name,password):

        flag=0
        while not self.poco(name).exists():
            self.poco.scroll()

        if self.poco(name).exists():
            self.poco(name).click()

            self.poco("Enter Password").focus([0.5, 0.6]).click()
            text(password)
            self.poco("Submit").click()
            sleep(1)
            flag=1

        if not flag:
            count = 0
            while not self.poco("Enter Network Manually...").exists() and count<10:
                self.poco.scroll()
                count += 1

    def click_enter_network_manually(self):
        self.poco("Enter Network Manually...").click()

    def enter_network_name(self, network_name):
        self.select_network_and_enter_password(network_name)

    def click_join_network(self):
        self.poco("Join").click()

    def check_apply_changes_button_clickable(self):
        a = self.poco("Apply Changes", enabled=True).exists()
        return a

    def delete_one_network(self,network_name):

        #self.poco(nameMatches=".*"+network_name).focus([1, 0.5]).click()
        self.poco(network_name).focus([0.95, 0.4]).click()

    def click_on_profile_edit(self):

        self.poco(self.profile_edit).click()



    def swap_two_networks(self,netw1,netw2):
        temp2 = self.poco(nameMatches=".*" + ". " + netw2 + ".*").get_name()

        temp1 = self.poco(nameMatches=".*" + ". " + netw1 + ".*").get_name()

        temp2 = self.poco(temp2)
        temp1 = self.poco(temp1)

        temp2.drag_to(temp1)

    def check_add_network_button_enabled(self):
        while not self.poco("Add Network").exists():
            self.poco.scroll()
        a = self.poco("Add Network",enabled=True).exists()
        return a


    def get_network_names(self):
        temp = []
        for i in poco(type="Button", nameMatches="[0-9]. .*"):
            temp.append(i.get_name())
        res = []
        for i in temp:
            res.append(i[3:])
        return res

    def delete_the_network(self,name):
        pos = poco(type="Button", nameMatches=".*" + name + ".*").attr("pos")
        size = poco(type="Button", nameMatches=".*" + name + ".*").attr("size")

        right_middle_x = pos[0] + size[0] * 0.48

        right_middle_y = pos[1] - size[1] * 0.0

        self.poco.click([right_middle_x, right_middle_y])

    def wait_for_the_printer_to_connect_network(self,name):
        self.poco("Current Network").parent().child(name).wait_for_appearance(timeout=60)

    def turn_off_wifi(self):
        cmd = "adb shell svc wifi disable"
        self.run_the_command(cmd)

    def turn_on_cellular_data(self):
        cmd = "adb shell svc data enable"
        self.run_the_command(cmd)

    def turn_off_cellular_data(self):
        cmd = "adb shell svc data disable"
        self.run_the_command(cmd)

    def run_the_command(self, command):
        cmd = command

        # Using os.system() method
        a = os.system(cmd)
        return a

    def check_internet_disconnect_error(self):
        a = self.poco("Error\nThe service is currently unavailable.").exists()
        return a

    def check_sudden_network_off_error(self):
        a = self.poco("Error\nAn Unknown Error has Occured.").exists()
        b = self.check_internet_disconnect_error()
        return a or b

    def check_failed_to_connect_network_error(self):
        a = self.poco(nameMatches="(?s).*Printer failed to connect to Wifi Network. This could be caused by incorrect password, router rejecting the connection, or wifi network being out of range. Do you want to continue or cancel the changes?.*")

    def click_on_continue_in_network_disconnect_error(self):
        self.poco("Continue").click()

    def refresh_home_page(self):
        self.poco.swipe([0.5, 0.25], [0.5, 0.7], duration=0.5)
        sleep(2)


    def get_recently_printed_labels(self):
        child_names = [child.get_name() for child in self.poco(nameMatces='(?s).*" x .*')]
        res=[]
        for i in child_names:
            if "prints left" not in i:
                res.append(i)
        return res

    def click_common_designs_button(self):
        self.poco(self.common_designs_button).click()

    def get_designs_visible_designs(self):

        child_names = [child.get_name() for child in self.poco(nameMatces='(?s).*" x .*')]
        return child_names

    def click_on_my_designs(self):
        self.poco(self.my_designs_button).click()

    def click_on_my_data(self):
        self.poco(self.my_data_button).click()

    def get_my_data_all(self):
        child_names = [child.get_name() for child in
                       poco(nameMatches=".*ScrollView.*")[1].parent().child()[0].children()]
        return child_names

    def click_home_button(self):
        home_btn = self.poco(self.click_Home_btn)
        home_btn.click()

    def open_wifi_settings(self):
        # cmd = "adb shell am start -a android.settings.SETTINGS"
        # self.run_the_command(cmd)
        # sleep(2)
        # try:
        #     self.poco(text="Wi-Fi").click()
        #     return
        # except:
        #     pass
        # try:
        #     try:
        #         self.poco(text="Search settings").click()
        #     except:
        #         self.poco(textMatches="Search").click()
        #     self.poco(type="android.widget.EditText").set_text("wifi")
        #     keyevent("enter")
        #     sleep(1)
        #
        #     self.poco(text="Wi-Fi").click()
        # except:
        #     pass

        keyevent("HOME")
        poco("Settings").click()
        sleep(2)
        poco("WIFI").click()
        poco("NESTWIFI").click()

        text("123456789")

    def select_wifi(self,ssid, password):
        pass

        #self.poco(text="Internet").click()
        # self.run_the_command("adb shell svc wifi enable")
        # self.poco(label=ssid).wait_for_appearance(timeout=20)
        #
        # self.poco(label=ssid).click()
        # try:
        #     self.poco(type="android.widget.EditText").set_text(password)
        #     keyevent("enter")
        #
        # except:
        #     sleep(1)

    def check_home_page(self):
        a = self.poco("Home").exists()
        return a

    def check_same_after_switching_network(self,arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return 0
        return 1




    def check_failed_network(self):
        a = self.poco(nameMatches="(?s).*Failed to Connect to Wifi Network.*").exists()
        return a

    def check_the_my_designs_internet_lost_error(self):
        a = self.poco("An error occurred when loading your designs. Please tap to try again").exists()

        return a















