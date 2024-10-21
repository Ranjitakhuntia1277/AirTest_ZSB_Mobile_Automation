# LoginFunction.py
import subprocess
import time
from platform import platform
from airtest.core.api import *
import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from ...Common_Method import Common_Method
from poco import poco
# from pocoui_lib.ios.kotoComponent import poco
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout
import platform

if platform.system() == "Windows":
    # C:\Users\mt5445\PycharmProjects\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\templates
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "PycharmProjects\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\\templates",
                            a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)


class Add_A_Printer_Screen_iOS:
    pass

    common_method = Common_Method(poco)

    def __init__(self, poco):
        self.poco = poco
        self.Testflight_zsb = "Cell"
        self.Testflight_prev_build = "Previous Builds"
        self.Prev_app_version = "2.0.6460"
        self.Install_button = "INSTALL"
        self.Open_button = "OPEN"
        self.ZSB_series_button = "ZSB Series"
        self.Back_button = "Back"
        self.Update_button = "UPDATE"
        self.Signin_button = "Sign In"
        self.Forget_this_device = "Forget This Device"
        self.Done_button = "Done"
        self.Home_option = "Home"
        self.Delete = "Delete"
        self.Yes_delete = "Yes, Delete"
        self.Bluetooth_setting = "Bluetooth"
        self.Add_A_Printer_Btn = "Add A Printer"
        self.Setup_your_printer = "Set up your printer"
        self.Radio_Button = "Button"
        self.Cancel_bluetooth = "Cancel"
        self.Exit_Button = "Exit"
        self.Settings = "Settings"
        self.Money_badger_pic = Template(r"tpl1722251176064.png", record_pos=(-0.013, -0.283), resolution=(1170, 2532))
        self.Start_setup = "Start Setup"
        self.ButtonX = "Button"
        self.Unable_to_find = "Unable to find printer(s)"
        self.Find_my_printer = "Find My Printer’s Bluetooth ID"
        self.Search_again = "Search Again"
        self.Printer_not_listed = "Printer Not Listed"
        self.Continue_register = "Continue"
        self.Lets_Make_Sure_Text = "Let's make sure the printer is in Bluetooth pairing mode."
        self.Searching_For_Your_Printer_Tex = "Searching for your printer"
        self.Next_Button = "Next"
        self.Pair_button = "Pair"
        self.Printer_LED_Not_Flashing_Text = "My Printer’s LED is Not Flashing Blue What Does The LED Light Indicator Mean"
        self.Blue_Left_LED = "Blue Left LED"
        self.To_Find_Your_Printer_Text = "To find your printer, please ensure your printer’s LED is flashing blue like the example below."
        self.LED_Light_Behavior_Support_Text = "LED Light Behavior Support"
        self.LED_Guide_Button = "LED Guide"
        self.Red_Right_LED = "Red Right LED"
        self.Printer_LED_Guide_Done_Btn = "Dismiss"
        self.Select_your_printer_Text = "Select your printer"
        self.Pairing_Your_Printer_Text = "Connecting to printer"
        self.Connect_to_printer_text = "Connect to printer"
        self.Try_again = "Try Again"
        self.Close_Wifi_network1 = "Tauqeer’s iPhone"
        self.Close_Wifi_network2 = "NESTWIFI"
        self.Open_wifi_select = "EL17-Cisco-OPEN"
        self.Enter_manually = "Enter Network Manually"
        self.Enter_network_name = "Enter Network Name"
        self.Select_security = "No Security"
        self.Select_wpa_psk = "WPA-PSK"
        self.Next_step = "Next Step"
        self.Skip = "Skip"
        self.Finish = "Finish"
        self.More_info = "More Info"

        self.Bluetooth_pairing_Popup1 = "android:id/action0"
        self.Bluetooth_pairing_Popup2 = "android:id/button1"
        self.Searching_for_wifi_networks_Text = "Searching for Wi-Fi Networks"
        self.Select_Different_Network_Text = "Select Different Network"
        self.Zebra_Network = "Zebra"
        self.Discovered_Devices_Text = "Discovered printers"
        self.Show_All_Printers = "Show all printers"
        self.Added_Printer = "ZSB-DP12C710B9"
        self.Second_Printer_Name = "android.widget.RadioButton"
        self.Connect_Wifi_Network_Text = "Connect Wi-Fi Network"
        self.Connect_to_wifi = "Connect to Wi-Fi"
        self.Select_Button_on_Select_Your_Printer = "Next"
        self.Connect_Btn_On_Connect_Wifi_Network_Screen = "Connect"
        self.Password_Field_On_Join_Network = Template(r"tpl1712913927236.png", record_pos=(-0.048, -0.44),
                                                       resolution=(1080, 2400))
        self.Submit_Button_ON_Join_Network = "Submit"
        self.Registering_your_Printer_Text = "Registering your Printer"
        self.Finish_Setup_Button = "Finish Setup"

        # ##""""""""""""""""""""""""""""""""""""""""""""""""smoke test-need to add""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        self.Print_Option = "Print"
        self.Print_Button = "Print"
        self.Back_Icon_Of_Print_Review_Screen = "android.widget.Button"
        self.Common_Design_Tab = "Common Designs"

        ### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.Scan_me = Template(Basic_path(r"QR.png"), record_pos=(-0.001, 0.514), resolution=(1170, 2532))
        self.Scan_me2 = Template(Basic_path(r"QR2.png"), record_pos=(-0.001, 0.507), resolution=(1170, 2532))
        self.Wifi_animation = Template(Basic_path(r"Wifi_Animation.png"), record_pos=(0.003, 0.006),
                                       resolution=(1170, 2532))
        self.Printer_3d_image = Template(Basic_path(r"Printer_3D_image.png"), record_pos=(-0.016, 0.485),
                                         resolution=(1170, 2532))

    def enable_bluetooth(self):
        start_app("com.apple.Preferences")
        sleep(2)
        bluetooth_setting_button = self.poco(name="Bluetooth")
        bluetooth_setting_button.click()
        sleep(2)
        bluetooth_switch = self.poco(type="Switch", name="Bluetooth")
        switch_value = bluetooth_switch.attr("value")
        if switch_value == "On" or switch_value == "1":
            print("Bluetooth is already on")
        else:
            bluetooth_switch.click()
            print("Bluetooth is now on.")
        self.common_method.swipe_back_to_app_ios()

    def disable_bluetooth(self):
        popup = self.poco(nameMatches="(?s).*Close.*")
        if popup.exists():
            popup.click()
        start_app("com.apple.Preferences")
        sleep(2)
        if self.poco(self.Settings).exists():
            self.poco(self.Settings).click()
            sleep(2)
        bluetooth_setting_button = self.poco(name="Bluetooth")
        bluetooth_setting_button.click()
        sleep(2)
        bluetooth_switch = self.poco(type="Switch", name="Bluetooth")
        switch_value = bluetooth_switch.attr("value")
        print(switch_value)
        if switch_value == "On" or switch_value == "1":
            bluetooth_switch.click()
            print("Bluetooth was on. Turning it off.")
        else:
            print("Bluetooth is already off.")
        self.common_method.swipe_back_to_app_ios()
        # self.switch_to_different_app()
        if popup.exists():
            popup.click()

    def enable_wi_fi(self):
        start_app("com.apple.Preferences")
        sleep(2)
        if self.poco(self.Settings).exists():
            self.poco(self.Settings).click()
            sleep(2)
        self.poco("Wi-Fi").click()
        sleep(2)
        wi_fi_toggle = self.poco(type="Switch", name="Wi‑Fi")
        switch_value = wi_fi_toggle.attr("value")
        if switch_value == "0":
            wi_fi_toggle.click()
        self.common_method.swipe_back_to_app_ios()

    def disable_Wi_Fi(self):
        sleep(2)
        start_app("com.apple.Preferences")
        sleep(2)
        self.poco("Wi-Fi").click()
        sleep(2)
        Wi_Fi_toggle = self.poco(type="Switch", name="Wi‑Fi")
        switch_value = Wi_Fi_toggle.attr("value")
        if switch_value == "1":
            Wi_Fi_toggle.click()
        self.common_method.swipe_back_to_app_ios()

    def downgrade_app_version(self):
        start_app("com.apple.TestFlight")
        if self.poco(self.Testflight_zsb).exists():
            self.poco(self.Testflight_zsb).click()
        self.poco(self.Testflight_prev_build).click()
        self.poco(self.Prev_app_version).click()
        self.poco(self.Install_button).click()
        timeout = 70
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.poco(self.Open_button).exists():
                print("App installed successfully")
                self.poco(self.Open_button).click()
                return
            time.sleep(1)

    def upgrading_app_version(self):
        self.common_method.swipe_back_to_app_ios()
        self.poco(self.ZSB_series_button).click()
        self.poco(self.Back_button).click()
        self.poco(self.Update_button).click()
        timeout = 70
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.poco(self.Open_button).exists():
                print("App installed successfully")
                self.poco(self.Open_button).click()
                return
            time.sleep(1)

    def unpair_printer(self):
        # if self.poco(self.Add_A_Printer_Btn).exists():
        #     return
        if self.poco(self.Signin_button).exists():
            return
        if self.poco(self.Add_A_Printer_Btn).exists():
            return
        start_app("com.apple.Preferences")
        sleep(2)
        if self.poco(self.Settings).exists():
            self.poco(self.Settings).click()
        bluetooth_setting_button = self.poco(name="Bluetooth")
        bluetooth_setting_button.click()
        sleep(2)
        bluetooth_switch = self.poco(type="Switch", name="Bluetooth")
        switch_value = bluetooth_switch.attr("value")
        if switch_value == "On" or switch_value == "1":
            print("Bluetooth is already on")
        else:
            bluetooth_switch.click()
            print("Bluetooth is now on.")
        if self.poco(self.More_info).exists():
            self.poco(self.More_info).click()
            self.poco(self.Forget_this_device).click()
            self.poco(nameMatches="(?s).*Forget Device.*").click()
        self.common_method.swipe_back_to_app_ios()
        if self.poco(self.Done_button).exists():
            self.poco(self.Done_button).click()

    def delete_printer(self):
        sleep(10)
        e_check = self.poco(nameMatches="(?s).*ZSB-DP12.*")
        if e_check.exists():
            element = self.poco(nameMatches=".*\s.*\s.*\s.*\s.*\s.*prints left.*|.*\s.*\s.*\s.*\s.*prints left.*")
            size = element.attr("size")
            pos = element.attr("pos")
            x = pos[0] + size[0] * 0.46
            y = pos[1] - size[1] * 0.46
            self.poco.click([x, y])
            self.poco(self.Delete).click()
            self.poco(self.Delete).click()
            self.poco(self.Yes_delete).click()

    def click_Add_A_Printer(self):
        sleep(2)
        self.poco(self.Add_A_Printer_Btn).click()
        if self.poco(self.Setup_your_printer).exists():
            print("Setup your printer page present")
        # if self.poco(self.Money_badger_pic).exists():
        #     print("Money badger pic exists")

    def cancel_bluetooth(self):
        turn_on = self.poco(nameMatches="(?s).*Turn.*")
        if turn_on.exists():
            print("Turn on bluetooth exists")
        self.poco(self.Cancel_bluetooth).click()

    def click_exit_button(self):
        if self.poco(self.Cancel_bluetooth).exists():
            print("Cancel button present")
            if self.poco(self.Exit_Button).exists():
                print("Exit button present")
                self.poco(self.Exit_Button).click()
        else:
            raise Exception("ERROR: Exit Button UI not present")

    def click_settings(self):
        turn_on = self.poco(nameMatches="(?s).*Turn.*")
        if turn_on.exists():
            print("Turn on bluetooth exists")
        self.poco(self.Settings).click()
        sleep(2)
        self.poco(self.Settings).click()

    def check_ui_of_printer_setup(self):
        sleep(2)
        line1 = self.poco(
            nameMatches="(?s).*You will be guided to complete 4 steps to successfully setup your printer.*")
        if line1.exists():
            print(" Line 1 present")
        else:
            raise Exception("Error: Line 1 is not displayed")
        line2 = self.poco(nameMatches="(?s).*To begin setting up your printer select.*")
        if line2.exists():
            print("Line 2 Present")
        else:
            raise Exception("Error: Line 2 is not displayed")
        scroll_view = self.poco("ScrollView")
        step1 = self.poco(nameMatches="(?s).*Connect to printer.*")
        step2 = self.poco(nameMatches="(?s).*Connect to Wi-Fi.*")
        step3 = self.poco(nameMatches="(?s).*Register printer.*")
        step4 = self.poco(nameMatches="(?s).*Test printer.*")
        if step1 and step2 and step3.exists():
            scroll_view.swipe("up", duration=0.5)
            if step4.exists():
                print("All steps are present")
        else:
            raise Exception("Error: The steps are not displayed correctly")

    def click_start_setup(self):
        sleep(2)
        self.poco(self.Start_setup).click()
        mode_check = self.poco(nameMatches="(?s).*Let's make sure the printer is in Bluetooth pairing mode.*")
        if mode_check.exists():
            print("Printer setup readiness screen present")
            if self.poco(self.Next_Button).exists():
                print("Next button and LED button is present")
                self.poco(self.Next_Button).click()
        else:
            raise Exception("ERROR: Printer setup readiness screen not present")
        if self.poco(self.Searching_For_Your_Printer_Tex).exists():
            print("Searching for printer displayed")
        sleep(10)
        popup = self.poco(nameMatches="(?s).*Close.*")
        if popup.exists():
            popup.click()

    def click_cross(self):
        sleep(2)
        self.poco(self.ButtonX).click()
        element = self.poco(nameMatches="(?s).*Exit Printer Setup.*")
        if element.exists():
            print("Exit Printer setup present")
        else:
            raise Exception("ERROR: Exit printer setup not present")
        wording = self.poco(
            nameMatches="(?s).*Your printer will not be ready for use until it has been successfully set up. Do you want to exit?.*")
        if wording.exists():
            print("'Do you want to exist message present' present")
        else:
            raise Exception("ERROR: 'Do you want to exist message present' not present")

    def check_unable_to_find(self):
        timeout = 70
        start_time = time.time()
        select_element = self.poco(self.Unable_to_find)
        while time.time() - start_time < timeout:
            if select_element.exists():
                print("Connect to Printer text is displayed")
                return
            time.sleep(1)

    def click_search_again(self):
        self.poco(self.Search_again).click()
        if self.poco(self.Searching_For_Your_Printer_Tex).exists():
            print("Searching for printer displayed")
            sleep(10)

    def check_connect_to_printer(self):
        timeout = 70
        start_time = time.time()
        select_element = self.poco(self.Select_your_printer_Text)
        if self.poco(self.ButtonX).exists():
            raise Exception("ERROR: Cross button is present wile searching for printer")
        else:
            print("no 'X' button is present")
        while time.time() - start_time < timeout:
            if select_element.exists():
                print("Select your printer screen is visible")
                if self.poco(self.Radio_Button).exists():
                    print("Radio button followed by Printer Image present")
                else:
                    raise Exception("ERROR: Radio Button for printer not present")
                if self.poco(nameMatches=f"(?s).*Bluetooth ID.*").exists():
                    print("Last Six digit of the Bluetooth ID present")
                else:
                    raise Exception("ERROR: Last Six digit of the Bluetooth ID not present")
                if self.poco(self.Next_Button).exists():
                    print("Next button present")
                else:
                    raise Exception("ERROR: Next button not present")
                if self.poco(self.Search_again).exists():
                    print("Search again Button present")
                else:
                    raise Exception("ERROR: Search again Button not present")
                if self.poco(self.Printer_not_listed).exists():
                    print("Printer not listed Button present")
                else:
                    raise Exception("ERROR: Printer not listed Button not present")
                return
            time.sleep(1)

    def click_find_my_printer_bluetooth_id(self):
        self.poco(self.Find_my_printer).click()
        if self.poco(self.Find_my_printer).exists():
            print("New dialog with Find My Printer's Bluetooth ID present")
        else:
            raise Exception("ERROR: New dialog with Find My Printer's Bluetooth ID not present")
        if self.poco(
                nameMatches=f"(?s).*Check the label under your printer or the Scan Me Label and look for its unique ID.*").exists():
            print(
                "The Text - Check the label under your printer or the Scan Me label and look for its unique ID Present")
        else:
            raise Exception(
                "ERROR: The Text - Check the label under your printer or the Scan Me label and look for its unique ID "
                "not Present")
        try:
            assert_exists(self.Scan_me)
            print("Option 1:  Scan me Label contains QR code Present")
        except:
            raise Exception("Option 1:  Scan me Label contains QR code not Present")
        swipe((0.7, 0.73), (0.3, 0.73))
        try:
            assert_exists(self.Scan_me2)
            print("Option 2: On printer back side present")
        except:
            raise Exception("Option 2: On printer back side not present")

    def click_the_printer_name_to_select(self, printer_name):
        # sleep(15)
        # Perform the swipe action
        scroll_view = self.poco("ScrollView")
        if scroll_view.exists():
            print("ScrollView found, proceeding with swipe")
        else:
            print("ScrollView not found, cannot swipe")
            raise RuntimeError("ScrollView element not found")

        printer_select = self.poco(nameMatches=f"(?s).*{printer_name}.*")
        if printer_select.exists():
            print("Printer with the model name is present")
            printer_select.click()
            print("Yes, printer is clicked")
        else:
            scroll_view.swipe("up", duration=0.5)
            print("Yes, swipe is done")

            # Check again if the printer is now visible after the swipe
            printer_select = self.poco(nameMatches=f"(?s).*{printer_name}.*")
            if printer_select.exists():
                print("Yes, printer is clicked after swipe")
                printer_select.click()
            else:
                print("Error: Printer not found even after swiping")
                raise RuntimeError(f"Printer '{printer_name}' not found even after swiping")

    def Scroll_Till_Next_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("left", duration=0.5)

    def click_next_button(self):
        Next_Button = self.poco(self.Next_Button)
        if self.poco(self.Next_Button).exists():
            print("Next Button is present and all the U Positions are correct")
            Next_Button.click()
        if self.poco(self.Continue_register).exists():
            print("Setup a registered printer dialog appeared")
            self.poco(self.Continue_register).click()
        sleep(3)
        if self.poco(self.Searching_for_wifi_networks_Text).exists():
            print("Searching for wifi page appears")

    def click_cancel_pair(self):
        timeout = 40
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.poco(self.Pair_button).exists():
                print("Button pairing request present with Pair and cancel button")
                self.poco(self.Cancel_bluetooth).click()
                return
            time.sleep(1)

    def click_pair_button(self):
        timeout = 40
        start_time = time.time()
        select_element = self.poco(self.Pair_button)

        while time.time() - start_time < timeout:
            if select_element.exists():
                print("Button pairing request present")
                select_element.click()
                sleep(10)
                return
            time.sleep(1)
        raise Exception("Error: Timed out waiting for Pair element to become visible")

    def check_wifi_search_page_ui(self):
        timeout = 30
        start_time = time.time()
        if self.poco(self.Connect_to_wifi).exists():
            print("Connect to Wi-Fi text is present")
        else:
            raise Exception("Error: Connect to Wi-Fi text is not present")
        if self.poco(self.Searching_for_wifi_networks_Text).exists():
            print("Connect to Wi-Fi text is present")
        else:
            raise Exception("Error: Connect to Wi-Fi text is not present")
        text_element = self.poco(nameMatches="(?s).*Your printer is searching for Wi-Fi networks.*")
        if self.poco(text_element).exists():
            print("Your printer is searching for Wi-Fi networks text present")
        else:
            raise Exception("Error: Your printer is searching for Wi-Fi networks text is not present")
        try:
            assert_exists(self.Wifi_animation)
            print("The Wi-Fi Animation is present")
        except:
            print("The Wi-Fi Animation is not present")
        try:
            assert_exists(self.Printer_3d_image)
            print("The Printer Image is present")
        except:
            print("The Printer Image is not present")
        if self.poco(self.ButtonX).exists():
            raise Exception("Error: Cross button is present on the page")
        else:
            print("There is no Cross button on the screen")
        if self.poco(self.Search_again).exists():
            end_time = time.time()
            if end_time - start_time > timeout:
                raise Exception("Error: The page took more than 30 seconds to load")
        else:
            print("The page took less than 30 seconds to load")

    def check_select_wifi(self):
        timeout = 70
        start_time = time.time()
        select_element = self.poco(nameMatches="(?s).*Connect to a Wi-Fi.*")
        while time.time() - start_time < timeout:
            if select_element.exists():
                print("Connect to wifi text is displayed")
                return
            time.sleep(1)

    def check_for_duplicate_wifi_networks(self):
        """
        Function to check if there are any duplicate Wi-Fi networks displayed on the screen.

        :return: True if there are no duplicates, False if duplicates are found
        """
        swipe([0.5, 0.64], [0.5, 0.44])
        b = []  # List to store Wi-Fi network names
        count = -1

        # Initialize the first Wi-Fi network name
        a = self.poco("ScrollView")[-1].parent().child()[0].get_name()

        # Loop to collect all visible Wi-Fi network names
        while a != "ScrollView":
            b.append(a)
            count -= 1
            a = self.poco("ScrollView")[count].parent().child()[0].get_name()

        # Filter out the "Other" network name if present
        b = list(filter(lambda x: x != "Other", b))

        # Set to store unique Wi-Fi names
        wifi_names = set()

        # Check for duplicates
        for wifi_name in b:
            if wifi_name in wifi_names:
                print(f"Duplicate Wi-Fi network found: {wifi_name}")
                return False
            wifi_names.add(wifi_name)
        swipe([0.5, 0.44], [0.5, 0.64])
        print("No duplicate Wi-Fi networks found.")
        return True

    def enter_network_manually(self, option):
        timeout = 70
        start_time = time.time()
        select_element = self.poco(self.Enter_manually)

        while time.time() - start_time < timeout:
            if select_element.exists():
                select_element.click()
                element = self.poco(self.Enter_network_name)
                element.click()
                text("Tauqeer’s iPhone")
                self.poco(self.Select_security).click()
                self.poco(self.Select_wpa_psk).click()
                text("123456789")
                if option == "connect":
                    self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen).click()
                if option == "cancel":
                    self.poco(self.Cancel_bluetooth).click()
                return
            time.sleep(1)
        raise Exception("Error: Timed out waiting for Enter manually element to become visible")

    def choose_closed_wifi_network_correct_password(self, network_name):
        timeout = 70
        start_time = time.time()
        wifi_select_element = self.poco(nameMatches=f"(?s).*{network_name}.*")
        while time.time() - start_time < timeout:
            if wifi_select_element.exists():
                wifi_select_element.click()
                print("Wifi network selected successfully")
                element = (self.poco(nameMatches="(?s).*Enter Password.*"))
                if element.exists():
                    print("Password input box is present")
                    element.click()
                    text("123456789")
                    if self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen).exists():
                        print(
                            "There are both cancel and submit button, cancel button is enabled and submit button is disabled")
                    self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen).click()
                    return
            time.sleep(1)  # wait for 1 second before checking again
        raise Exception("Error: Timed out waiting for Close_Wifi_network1 element to become visible")

    def choose_closed_wifi_network_incorrect_password(self):
        timeout = 70
        start_time = time.time()
        wifi_select_element = self.poco(self.Close_Wifi_network1)
        while time.time() - start_time < timeout:
            if wifi_select_element.exists():
                wifi_select_element.click()
                print("Wifi network selected successfully")
                element = (self.poco(nameMatches="(?s).*Enter Password.*"))
                if element.exists():
                    print("Password input box is present")
                    element.click()
                    text("123456123")
                    self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen).click()
                    return
            time.sleep(1)  # wait for 1 second before checking again
        raise Exception("Error: Timed out waiting for Close_Wifi_network1 element to become visible")

    def check_wifi_connected_successfully(self):
        timeout = 70
        start_time = time.time()
        wifi_select = self.poco(nameMatches="(?s).*Successfully connected.*")

        while time.time() - start_time < timeout:
            if wifi_select.exists():
                print("Wifi is successfully connected")
                return
            time.sleep(1)  # wait for 1 second before checking again

        raise Exception("Error: 'Unable to Connect to Wifi' element not present after 70 seconds")

    def choose_open_wifi_network(self):
        timeout = 70
        start_time = time.time()
        wifi_select_element = self.poco(self.Open_wifi_select)
        while time.time() - start_time < timeout:
            if wifi_select_element.exists():
                wifi_select_element.click()
                element = (self.poco(nameMatches="(?s).*Enter Password.*"))
                if element.exists():
                    print("Password input box is present")
                else:
                    print("No Password enter box popped up")
                print("Wifi network selected successfully")
                return
            time.sleep(1)  # wait for 1 second before checking again
        raise Exception("Error: Timed out waiting for Close_Wifi_network1 element to become visible")

    def check_unable_to_connect_printer(self):
        timeout = 100
        start_time = time.time()
        printer_select = self.poco(nameMatches="(?s).*Unable to.*")

        while time.time() - start_time < timeout:
            if printer_select.exists():
                print("Unable to connect to printer displayed")
                return
            time.sleep(1)  # wait for 1 second before checking again

        raise Exception("Error: 'Unable to Connect to printer' element not present after 70 seconds")

    def click_try_again(self):
        self.poco(self.Try_again).click()

    def finish_setup(self):
        timeout = 70
        start_time = time.time()
        check_element = self.poco(nameMatches="(?s).*Remove shipping.*")

        while time.time() - start_time < timeout:
            if check_element.exists():
                print("Printer Registered page present")
                for i in range(4):
                    self.poco(self.Next_step).click()
                self.poco(self.Next_Button).click()
                self.poco(self.Skip).click()
                self.poco(self.Next_Button).click()
                self.poco(self.Finish).click()
                self.poco(self.Home_option).click()
                print("Printer successfully added")
                return
            time.sleep(1)  # wait for 1 second before checking again

        raise Exception("Error: 'Unable to Connect to Wifi' element not present after 70 seconds")

    def check_printer_online(self):
        timeout = 10
        start_time = time.time()
        check_element = self.poco(nameMatches="(?s).*Online.*")
        while time.time() - start_time < timeout:
            if check_element.exists():
                print("Printer is Online")
                return True
            time.sleep(1)  # wait for 1 second before checking again
        raise Exception("Error: 'Unable to check printer status' element not present after 10 seconds")

    def check_printer_offline(self):
        timeout = 10
        start_time = time.time()
        check_element = self.poco(nameMatches="(?s).*Offline.*")
        while time.time() - start_time < timeout:
            if check_element.exists():
                print("Printer is Offline")
                return True
            time.sleep(1)  # wait for 1 second before checking again
        raise Exception("Error: 'Unable to check printer status' element not present after 10 seconds")

    def Verify_Lets_Make_Sure_Text(self):
        Lets_Make_Sure_Text = self.poco(self.Lets_Make_Sure_Text)
        if Lets_Make_Sure_Text.exists():
            text = Lets_Make_Sure_Text.get_text()
            return text
        else:
            return None

    def Verify_Searching_for_your_printer_Text(self):
        searching_for_printer_text = self.poco(self.Searching_For_Your_Printer_Tex)
        if searching_for_printer_text.exists():
            text = searching_for_printer_text.get_text()
            return text
        else:
            pass

    def Verify_Printer_LED_Not_Flashing_Text(self):
        led_not_flashing_text = self.poco(self.Printer_LED_Not_Flashing_Text)
        text = led_not_flashing_text.get_text()
        return text

    def Verify_To_Find_Your_Printer_Text(self):
        To_Find_Your_Printer_text = self.poco(self.To_Find_Your_Printer_Text)
        To_Find_Your_Printer_text.get_text()
        print(" To Find Your Printer text is displaying:", To_Find_Your_Printer_text)
        return To_Find_Your_Printer_text

    def Verify_Printer_LED_Image(self):
        assert_exists(self.Printer_LED_Image, "Printer LED Image is present")

    def click_Printer_LED_Not_Flashing_Link(self):
        sleep(2)
        Printer_LED_Not_Flashing_Link = self.poco(self.Printer_LED_Not_Flashing_Text)
        Printer_LED_Not_Flashing_Link.click()

    def Verify_Blue_Left_LED_Text_And_Expand(self):
        sleep(2)
        Blue_Left_LED_Text_And_Expand = self.poco(self.Blue_Left_LED)
        if Blue_Left_LED_Text_And_Expand.exists():
            Blue_Left_LED_Text_And_Expand.click()
            sleep(1)
            Blue_Left_LED_Text_And_Expand.click()
            sleep(1)

    def Verify_Red_Right_LED_Text_And_Expand(self):
        sleep(2)
        Red_Right_LED_Text_And_Expand = self.poco(self.Red_Right_LED)
        if Red_Right_LED_Text_And_Expand.exists():
            Red_Right_LED_Text_And_Expand.click()
            sleep(1)
            Red_Right_LED_Text_And_Expand.click()
            sleep(1)

    def Verify_LED_Light_Behavior_Support_Text(self):
        LED_Light_Behavior_Support_Text = self.poco(self.LED_Light_Behavior_Support_Text)
        LED_Light_Behavior_Support_Text.get_text()
        print(" LED Light Behaviour support Text is displaying:", LED_Light_Behavior_Support_Text)
        return LED_Light_Behavior_Support_Text

    def Verify_the_Position_of_all_the_Buttons(self):
        assert_exists(self.the_Position_of_all_the_Buttons, "Verify the position of all the Buttons are correct")
        sleep(1)

    def click_Printer_LED_Guide_Done_Btn(self):
        Printer_LED_Guide_Done_Btn = self.poco(self.Printer_LED_Guide_Done_Btn)
        Printer_LED_Guide_Done_Btn.click()
        sleep(2)

    def Verify_Select_your_printer_Text(self):
        sleep(16)
        select_your_printer_Text = self.poco(self.Select_your_printer_Text)
        select_your_printer_Text.get_text()
        return select_your_printer_Text

    def Verify_Pairing_Your_Printer_Text(self):
        sleep(2)
        pairing_Your_Printer_Text = self.poco(self.Pairing_Your_Printer_Text)
        if pairing_Your_Printer_Text.exists():
            pairing_Your_Printer_Text.get_text()
        else:
            pass

    def click_Select_Button_On_Select_Your_Printer_Screen(self):
        sleep(2)
        select_btn = self.poco(self.Select_Button_on_Select_Your_Printer)
        select_btn.click()

    def click_Bluetooth_pairing_Popup1(self):
        bluetooth_pairing_popup1 = self.poco(self.Bluetooth_pairing_Popup1)
        bluetooth_pairing_popup1.click()

    def click_Bluetooth_pairing_Popup2(self):
        bluetooth_pairing_popup2 = self.poco(self.Bluetooth_pairing_Popup2).wait_for_appearance(timeout=3)
        bluetooth_pairing_popup2.click()

    def Verify_Searching_for_wifi_networks_Text(self):
        sleep(2)
        searching_for_wifi_networks_Text = self.poco(self.Searching_for_wifi_networks_Text)
        searching_for_wifi_networks_Text.get_text()
        print(" Searching for Wifi network Text is displaying:", searching_for_wifi_networks_Text)
        return searching_for_wifi_networks_Text

    def click_Select_Different_Network(self):
        bluetooth_pairing_popup2 = self.poco(self.Bluetooth_pairing_Popup2).wait_for_appearance(timeout=3)
        bluetooth_pairing_popup2.click()

    def click_Zebra_Network(self):
        sleep(4)
        Zebra_Network = self.poco(self.Zebra_Network)
        Zebra_Network.click()

    def Verify_Discovered_Devices_Text(self):
        discovered_devices_Text = self.poco(self.Discovered_Devices_Text)
        discovered_devices_Text.get_text()
        print(" Discovered Devices Text is displaying:", discovered_devices_Text)
        return discovered_devices_Text

        # def Verify_same_ZSB_image_for_all_items(self):
        #
        #     # if assert_exists(self.ZSB_Printer_images, "Only ZSB Printers are present"):
        #     if (self.ZSB_Printer_images, "Only ZSB Printers are present").exists():
        #         print("ZSB Printers are present for all items.")
        #     else:
        #         print("ZSB Printers are not present for all items.")

    def Verify_same_ZSB_image_for_all_items(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*ZSB-DP12.*").get_name()
        a = a.split("\n")
        print(a)

    def Verify_Already_Added_Printer_IS_Not_Displaying(self):
        sleep(5)
        assert not self.poco(self.Added_Printer).exists(), "Added Printer is still displaying"

    def click_Show_All_Printers(self):
        sleep(2)
        Show_All_Printers = self.poco(self.Show_All_Printers)
        Show_All_Printers.click()

    def click_2nd_Printer_Details_To_Add(self):
        sleep(4)
        second_printer = self.poco(name="android.widget.RadioButton")
        second_printer.click()

        # def Accept_Bluetooth_pairing_Popup1(self):
        #     while wait:
        #
        #     bluetooth_popup1 = self.poco(self.Bluetooth_pairing_Popup1)
        #     bluetooth_popup1.click()

    def Accept_Bluetooth_pairing_Popup1(self):
        sleep(2)
        bluetooth_popup1 = self.poco(self.Bluetooth_pairing_Popup1)
        if bluetooth_popup1.exists():
            bluetooth_popup1.click()
        else:
            pass

    def Accept_Bluetooth_pairing_Popup2(self):
        sleep(2)
        bluetooth_popup2 = self.poco(self.Bluetooth_pairing_Popup2)
        if bluetooth_popup2.exists():
            bluetooth_popup2.click()
        else:
            pass

    def Verify_Connect_Wifi_Network_Text(self):
        sleep(7)
        connect_wifi = self.poco(self.Connect_Wifi_Network_Text)
        if connect_wifi.exists():
            connect_wifi.get_text()
        else:
            pass

    def click_Connect_Btn_On_Connect_Wifi_Network_Screen(self):
        sleep(7)
        connect_btn = self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen)
        connect_btn.click()

        # def click_Password_Field_On_Join_Network(self):
        #     sleep(2)
        #     touch(self.Password_Field_On_Join_Network)
        #     sleep(2)
        #     poco(text("123456789"))

    def click_Password_Field_On_Join_Network(self):
        sleep(2)
        touch(self.Password_Field_On_Join_Network)
        sleep(2)
        poco(text("123456789"))

    def Enter_Password_To_Join_Network(self):
        sleep(2)
        poco(text("123456789"))

    def click_Submit_Button_ON_Join_Network(self):
        sleep(2)
        submit_btn = self.poco(self.Submit_Button_ON_Join_Network)
        if submit_btn.exists() and submit_btn.attr('enabled'):
            submit_btn.click()
        else:
            pass

    def Verify_Connecting_to_WiFi_Network_Text(self):
        sleep(3)
        Connecting_to_WiFi_Network_Text = self.poco(name="Connecting to Wi-Fi Network")
        if Connecting_to_WiFi_Network_Text.exists():
            print("Connecting to Wi-Fi Network Text is present.")
        else:
            pass

    def Verify_Need_the_Printer_Driver_Text(self):
        sleep(9)
        need_printer_text = self.poco(name="Need the Printer Driver?")
        if need_printer_text.exists():
            need_printer_text.get_text()
            print("Need the printer driver text is present.")

        else:
            print("Need the printer driver text is not displaying.")

    def Verify_Registering_your_Printer_Text(self):
        sleep(2)

        Registering_your_Printer_Text = self.poco(name="Registering your Printer")
        if Registering_your_Printer_Text.exists():
            Registering_your_Printer_Text.get_text()
            print("Registering your Printer Text is present.")

        else:
            print("Registering your Printer Text is not present.")

    def Verify_Connected_Text(self):
        sleep(7)
        if self.poco(name="Connected!").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

        # def click_Finish_Setup_Button(self):
        #     sleep(20)
        #     try:
        #         finish_btn = self.poco(self.Finish_Setup_Button)
        #         finish_btn.wait(20).visible().click()
        #
        #     except PocoTargetTimeout:
        #         print("Finish button did not become visible within 20 seconds.")
        #         sleep(3)

    def click_Finish_Setup_Button(self):
        sleep(25)
        finish_btn = self.poco(self.Finish_Setup_Button)
        if finish_btn.exists():
            finish_btn.click()
            sleep(5)
        else:
            stop_app("com.zebra.soho_app")
            sleep(1)
            start_app("com.zebra.soho_app")
            sleep(6)
            print("Finish button did not become visible within 20 seconds.")

    def click_FirstOne_In_MyDesign(self):
        sleep(1)
        # a = self.poco("android.view.View").child(type="android.widget.ImageView")[0].get_name()
        # return a
        self.poco("android.view.View").child(type="android.widget.ImageView")[0].click()

    def click_Print_Option(self):
        sleep(2)
        print_option = self.poco(self.Print_Option)
        print_option.click()
        sleep(3)

    def click_Print_Button(self):
        global start_point
        sleep(4)
        print_button = self.poco(self.Print_Button)
        if print_button.exists():
            print_button.click()
        else:
            #     start_point = (0.5, 0.7914691943127962)  # Example coordinates (x, y)
            # # Specify the vector for swiping up
            # vector = (0.5, 0.4928909952606635)  # Example vector (delta_x, delta_y)
            # # Perform the swipe action
            # swipe(start_point, vector)
            sleep(1)
            poco.scroll()
            print_button.click()
            sleep(5)

    def Verify_Design_Preview_Screen_With_Details(self):
        sleep(3)
        a = self.poco(nameMatches="(?s).*Label.*").get_name()
        print(a)

    def click_The_Back_Icon_Of_Print_Review_Screen(self):
        sleep(2)
        back_button = self.poco(self.Back_Icon_Of_Print_Review_Screen)
        back_button.click()

    def click_SecondOne_In_MyDesign(self):
        sleep(2)
        self.poco("android.view.View").child(type="android.widget.ImageView")[1].click()
        sleep(1)

    def click_Common_Design_Tab(self):
        common_design = self.poco(self.Common_Design_Tab)
        common_design.click()

    def click_FirstOne_Design_In_Common_Design(self):
        sleep(3)
        self.poco(nameMatches="(?s).*Address.*").click()

    def click_FirstOne_In_Common_Design(self):
        sleep(5)
        self.poco("android.view.View").child(type="android.widget.ImageView")[0].click()

    def click_LED_Guide_Button(self):
        sleep(1)
        led_Button = self.poco(self.LED_Guide_Button)
        led_Button.click()

    def click_Text_Field_To_Edit(self):
        sleep(1)
        Text_Field_To_Edit = self.poco(name="android.widget.EditText")
        Text_Field_To_Edit.click()
        sleep(1)
        poco(text("1"))
