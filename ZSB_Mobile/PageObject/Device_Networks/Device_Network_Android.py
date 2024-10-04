from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ...Common_Method import Common_Method
from airtest.core.api import device as current_device
import os

import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "Desktop\ZSB_Automation\ZSB_Mobile\\TestExecution\\test_Smoke_Test", a)
else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)


class Device_Networks_Android:
    pass

    def __init__(self, poco):
        self.poco = poco

    def wait_till_the_networks_list(self):
        self.poco(name="android.widget.ImageView").child("android.view.View").wait_for_appearance(timeout=30)
        sleep(3)

    def click_network_by_name(self, name):
        count = 0
        while not self.poco(nameMatches=".*" + name + ".*").exists() and count < 10:
            self.poco.scroll()
            count += 1
        self.poco(nameMatches=".*" + name + ".*").click()

    def check_the_wordings_in_connect_to_network(self):
        a = self.poco(nameMatches=".*Please enter the password.*" + ".*the printer to this network.*").exists()
        b = self.poco(nameMatches=".*Connect to Network.*").exists()

        return a and b

    def click_on_cancel_button(self):
        try:
            self.poco("Cancel").click()
        except:
            self.poco("cancel").click()

    def enter_the_password(self, password):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(password)
        keyevent("enter")

    def click_on_connect(self):
        self.poco("Connect").click()

    def get_the_network_name_and_status(self):
        self.poco(nameMatches=".*Apply Changes").wait_for_appearance(timeout=40)
        sleep(3)
        try:
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a, b
        except:
            self.poco.swipe([0.5, 0.4], [0.5, 0.9])
            a = self.poco(name="Current Network").parent().child()[2].get_name()
            b = self.poco(name="Current Network").parent().child()[4].get_name()
            return a, b

    def swap_two_networks(self, netw1, netw2):
        temp2 = self.poco(nameMatches=".*" + ". " + netw2 + ".*").get_name()

        temp1 = self.poco(nameMatches=".*" + ". " + netw1 + ".*").get_name()

        temp2 = self.poco(temp2)
        temp1 = self.poco(temp1)

        temp2.drag_to(temp1)

    def check_add_network_button_enabled(self):
        while not self.poco("Add Network").exists():
            self.poco.scroll()
        a = self.poco("Add Network", enabled=True).exists()
        return a

    def get_network_names(self):
        self.poco(nameMatches="Apply Changes").wait_for_appearance(timeout=30)
        temp = []
        for i in self.poco(type="android.widget.Button", nameMatches="[0-9]. .*"):
            temp.append(i.get_name())
        res = []
        for i in temp:
            res.append(i[3:])
        return res

    def check_network_not_added(self, network):
        self.poco(nameMatches="Apply Changes", enabled=True).wait_for_appearance(timeout=30)
        if self.poco(nameMatches=".*. " + network + ".*").exists():
            raise Exception("Network added even after clicking cancel in \n'Failed to Connect to Wifi network'\n page.")

    def check_network_added(self, network):
        self.poco(nameMatches="Apply Changes", enabled=True).wait_for_appearance(timeout=80)
        sleep(3)
        if not self.poco(nameMatches=".*. " + network + ".*").exists():
            raise Exception("Network not added even after entering the right credentials.")

    def delete_the_network(self, name):
        self.poco(nameMatches="Apply Changes").wait_for_appearance(timeout=80)
        sleep(3)
        self.poco(nameMatches=".*. " + name + ".*").wait_for_appearance(timeout=30)

        pos = self.poco(type="android.widget.Button", nameMatches=".*" + name + ".*").attr("pos")
        size = self.poco(type="android.widget.Button", nameMatches=".*" + name + ".*").attr("size")

        right_middle_x = pos[0] + size[0] * 0.48

        right_middle_y = pos[1] - size[1] * 0.0

        self.poco.click([right_middle_x, right_middle_y])
        self.poco(nameMatches="(?s).*Deleting.*").wait_for_appearance(timeout=20)
        sleep(7)

    def check_if_network_present_in_saved_networks(self, network):
        self.poco(nameMatches="Apply Changes").wait_for_appearance(timeout=80)
        if not self.poco(nameMatches=".*. " + network + ".*").exists():
            raise Exception("Network is not present in the list.")

    def check_if_network_not_present_in_saved_networks(self, network):
        self.poco(nameMatches="Apply Changes").wait_for_appearance(timeout=80)
        if self.poco(nameMatches=".*. " + network + ".*").exists():
            raise Exception("Network is present in the list.")

    def wait_for_the_printer_to_connect_network(self, name):
        self.poco("Current Network").parent().child(name).wait_for_appearance(timeout=60)

    def turn_off_wifi(self):
        cmd = "adb shell svc wifi disable"
        self.run_the_command(cmd)
        sleep(2)

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
        a = self.poco("The service is currently unavailable.").exists()
        return a

    def check_sudden_network_off_error(self):
        sleep(4)
        a = self.poco("Error")
        b = self.poco("The service is currently unavailable.").exists()
        c = self.check_internet_disconnect_error()
        return a or b or c

    def check_failed_to_connect_network_error(self):
        a = self.poco(
            nameMatches="(?s).*Printer failed to connect to Wifi Network. This could be caused by incorrect password, router rejecting the connection, or wifi network being out of range. Do you want to continue or cancel the changes?.*")

    def click_on_continue_in_network_disconnect_error(self):
        self.poco("Continue").click()

    def refresh_home_page(self):
        self.poco.swipe([0.5, 0.25], [0.5, 0.7], duration=0.5)
        sleep(5)

    def allow_nearby_devices_permission(self, allow=1):

        cmd = "adb shell am start -a android.settings.SETTINGS"
        self.run_the_command(cmd)
        sleep(2)
        try:
            try:
                try:
                    self.poco(text="Search settings").click()
                except:
                    self.poco(textMatches="Search").click()
                self.poco(type="android.widget.EditText").set_text("zsb")
                keyevent("enter")
                sleep(1)

                self.poco(textMatches=".*ZSB.*").click()
            except:
                pass

            self.poco(text="ZSB Series").click()
            self.poco(text="Permissions").click()
            self.poco(text="Nearby devices").click()
        except:
            pass

        if allow:
            self.poco(nameMatches=".*allow.*").click()
        else:
            self.poco(nameMatches=".*deny.*").click()

    def check_failed_network(self):
        a = self.poco(nameMatches="(?s).*Failed to Connect to Wifi Network.*").exists()
        return a

    def check_the_my_designs_internet_lost_error(self):
        a = self.poco("An error occurred when loading your designs. Please tap to try again").exists()

        return a

    def check_if_device_is_connected_to_a_network(self, status):
        sleep(2)
        if status != "Connected":
            raise Exception("no network is connected to the device")

    def check_if_bluetooth_connection_failed_pop_up_is_displayed(self):
        sleep(3)
        try:
            self.poco(nameMatches="Bluetooth Connection Failed").wait_for_appearance(timeout=20)
        except:
            raise Exception("'Bluetooth Connection Failed' pop up did not appear.")

    def check_if_saved_network_list_is_displayed(self):
        try:
            self.poco("NETWORK NAME").wait_for_appearance(timeout=20)
            self.poco("Apply Changes").wait_for_appearance(timeout=20)
        except:
            raise Exception("Saved network list is not displayed.")

    def check_number_of_saved_networks_as_expected(self, count, networklist):
        if len(networklist) > count:
            error = f"There are more than {count} networks in the saved networks list."
            raise Exception(error)

    def check_no_networks_in_saved_networks(self):
        try:
            self.poco("Apply Changes").wait_for_appearance(timeout=60)
            self.get_network_names()
            raise Exception("all the networks did not get deleted")
        except ZeroDivisionError:
            pass
        self.poco("Not Connected").wait_for_appearance(timeout=20)

    def check_printer_is_already_connected_to_the_network_message(self):
        try:
            self.poco(nameMatches=".*Printer is already connected to this network.*").wait_for_appearance(timeout=20)
        except:
            raise Exception("'Printer is already connected to this network.' message not displayed when trying to connect to already connected network.")

    def check_add_network_button_present(self):
        if self.poco("Add Network").exists():
            pass
        else:
            self.poco.scroll()
            if not self.poco("Add Network").exists():
                raise Exception("'Add Network' button not present.")

    def check_if_nearby_device_permission_pop_up_displayed(self):
        sleep(10)
        continue_btn = self.poco("Continue")
        if continue_btn.exists():
            continue_btn.click()
        try:
            self.poco(textMatches=".*Allow ZSB Series to find, connect to, and determine the relative position of nearby devices?.*").wait_for_appearance(timeout=25)
        except:
            raise Exception("'Allow ZSB Series to find, connect to, and determine the relative position of nearby devices?' pop up not displayed.")
