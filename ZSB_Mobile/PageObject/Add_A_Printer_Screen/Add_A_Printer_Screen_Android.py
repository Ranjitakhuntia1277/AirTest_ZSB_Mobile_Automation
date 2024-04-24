# LoginFunction.py
import subprocess
from platform import platform
from airtest.core.api import *
import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout
from pocoui_lib.android.kotoComponent import poco
import subprocess
from time import sleep


def disable_bluetooth():
    os.system('adb shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE> nul 2>&1')
    # os.system(f"adb -s {device_id} shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE")

    shell_element = poco(text="Allow")
    try:
        shell_element.exists()
        shell_element.click()
        sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}. Skipping.")


class Add_A_Printer_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.Add_A_Printer_Btn = "Add A Printer"
        self.Start_Btn = "Start"
        self.Searching_For_Your_Printer_Text = "Searching for your printer"
        self.Printer_LED_Not_Flashing_Text = "My Printer’s LED is Not Flashing Blue What Does The LED Light Indicator Mean"
        self.To_Find_Your_Printer_Text = "To find your printer, please ensure your printer’s LED is flashing blue like the example below."
        self.Printer_LED_Image = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1705903757611.png"), record_pos=(-0.007, 0.041),
                                          resolution=(1080, 2400))
        self.LED_Light_Behavior_Support_Text = "LED Light Behavior Support"
        self.the_Position_of_all_the_Buttons = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1705913879009.png"), record_pos=(0.001, 0.002), resolution=(1080, 2400))




        self.Printer_LED_Guide_Done_Btn = "Done"
        self.Select_your_printer_Text = "Select your printer"
        self.Pairing_Your_Printer_Text = "Pairing your printer"
        self.Printer_Name_To_Select = ""
        self.Bluetooth_pairing_Popup1 = "android:id/action0"
        self.Bluetooth_pairing_Popup2 = "android:id/button1"
        self.Searching_for_wifi_networks_Text = "Searching for Wi-Fi Networks"
        self.Select_Different_Network_Text = "Select Different Network"
        self.Zebra_Network = "Zebra"
        self.Discovered_Devices_Text = "Discovered Devices"
        self.ZSB_Printer_images = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1706510933463.png"), record_pos=(-0.334, -0.229), resolution=(1080, 2400))


        self.Show_All_Printers = "Show all printers"
        self.Added_Printer = "ZSB-DP12C710B9"
        self.Second_Printer_Name = "android.widget.RadioButton"
        self.Connect_Wifi_Network_Text = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1707286425683.png"), record_pos=(0.026, -0.911), resolution=(1080, 2400))


        self.Select_Button_on_Select_Your_Printer = "Select"
        self.Connect_Btn_On_Connect_Wifi_Network_Screen = "Connect"
        self.Password_Field_On_Join_Network = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1707135468156.png"), record_pos=(0.006, 0.084), resolution=(1080, 2400))

        self.Submit_Button_ON_Join_Network = "Submit"
        self.Registering_your_Printer_Text = "Registering your Printer"
        self.Finish_Setup_Button = "Finish Setup"

    # """"""""""""""""""""""""""""""""""""""""""""""""smoke test-need to add""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.FirstOne_In_MyDesign = Template(os.path.join(os.path.expanduser('~'),
                                                          "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                          "tpl1707820626487.png"), record_pos=(-0.011, -0.003),
                                             resolution=(1170, 2532))

        self.Print_Option = "Print"
        self.Print_Button = "Print"
        self.Design_Preview_With_Details = Template(os.path.join(os.path.expanduser('~'),
                                                                 "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                 "tpl1707902210476.png"), record_pos=(0.047, 0.202),
                                                    resolution=(1170, 2532))
        self.Back_Icon_Of_Print_Review_Screen = "Button"
        self.SecondOne_In_MyDesign = Template(os.path.join(os.path.expanduser('~'),
                                                           "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                           "tpl1707902210476.png"), record_pos=(0.047, 0.202),
                                              resolution=(1170, 2532))
        self.Common_Design_Tab = "Common Designs"
        self.FirstOne_Design_In_Common_Design = "Other"
        self.FirstOne_In_Common_Design = "Other"

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def disable_bluetooth(self):
        try:
            # Disable Bluetooth using ADB
            subprocess.run(
                ['adb', 'shell', 'am', 'start', '-a', 'android.bluetooth.adapter.action.REQUEST_DISABLE'],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check for the 'Allow' element using poco
            shell_element = poco(text="Allow")
            if shell_element.exists():
                shell_element.click()
                sleep(1)
            else:
                print("No 'Allow' element found. Skipping.")

        except subprocess.CalledProcessError as e:
            print(f"ADB command failed with error: {e}. Skipping.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Skipping.")

    def enable_bluetooth(self):
        try:
            subprocess.run(
                ['adb', 'shell', 'am', 'start', '-a', 'android.bluetooth.adapter.action.REQUEST_ENABLE'],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check for the 'Allow' element using poco
            shell_element = poco(text="Allow")
            if shell_element.exists():
                shell_element.click()
                sleep(1)
            else:
                print("No 'Allow' element found. Skipping.")

        except subprocess.CalledProcessError as e:
            print(f"ADB command failed with error: {e}. Skipping.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Skipping.")

    def click_Add_A_Printer(self):
        add_a_printer_btn = self.poco(self.Add_A_Printer_Btn)
        add_a_printer_btn.click()

    def click_Start_Button(self):
        sleep(2)
        start_btn = self.poco(self.Start_Btn)
        start_btn.click()

    def Verify_Searching_for_your_printer_Text(self):
        searching_for_printer_text = self.poco(self.Searching_For_Your_Printer_Text)
        if searching_for_printer_text.exists():
            text = searching_for_printer_text.get_text()

        else:
            pass

    def Verify_Printer_LED_Not_Flashing_Text(self):
        assert_exists(self.Printer_LED_Not_Flashing_Text, "Printer led not flashing text is displaying")

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

    def Verify_LED_Light_Behavior_Support_Text(self):
        LED_Light_Behavior_Support_Text = self.poco(self.LED_Light_Behavior_Support_Text)
        LED_Light_Behavior_Support_Text.get_text()
        print(" LED Light Behaviour support Text is displaying:", LED_Light_Behavior_Support_Text)
        return LED_Light_Behavior_Support_Text

    def Verify_the_Position_of_all_the_Buttons(self):
        assert_exists(self.the_Position_of_all_the_Buttons, "Verify the position of all the Buttons are correct")

    def click_Printer_LED_Guide_Done_Btn(self):
        Printer_LED_Guide_Done_Btn = self.poco(self.Printer_LED_Guide_Done_Btn)
        Printer_LED_Guide_Done_Btn.click()
        sleep(2)

    def Verify_Select_your_printer_Text(self):
        sleep(2)
        select_your_printer_Text = self.poco(self.Select_your_printer_Text)
        select_your_printer_Text.get_text()
        return select_your_printer_Text

    def Verify_Pairing_Your_Printer_Text(self):
        sleep(2)
        pairing_Your_Printer_Text = self.poco(self.Pairing_Your_Printer_Text)
        pairing_Your_Printer_Text.get_text()
        print(" LED Light Behaviour support Text is displaying:", pairing_Your_Printer_Text)
        return pairing_Your_Printer_Text

    def Click_The_Printer_Name_To_Select(self):
        Printer_Name_To_Select = self.poco(self.Printer_Name_To_Select).wait_for_appearance(timeout=4)
        Printer_Name_To_Select.click()

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

    def Verify_same_ZSB_image_for_all_items(self):

        if assert_exists(self.ZSB_Printer_images, "Only ZSB Printers are present"):
            print("ZSB Printers are present for all items.")
        else:
            print("ZSB Printers are not present for all items.")

    def Verify_Already_Added_Printer_IS_Not_Displaying(self):
        sleep(5)
        assert not self.poco(self.Added_Printer).exists(), "Added Printer is still displaying"

    def click_Show_All_Printers(self):
        sleep(2)
        Show_All_Printers = self.poco(self.Show_All_Printers)
        Show_All_Printers.click()

    def click_2nd_Printer_Details_To_Add(self):
        sleep(4)
        second_printer = self.poco(self.Second_Printer_Name)
        second_printer.click()

    # def Accept_Bluetooth_pairing_Popup1(self):
    #     while wait:
    #
    #     bluetooth_popup1 = self.poco(self.Bluetooth_pairing_Popup1)
    #     bluetooth_popup1.click()

    def Accept_Bluetooth_pairing_Popup1(self):
        sleep(2)
        bluetooth_popup1 = self.poco(self.Bluetooth_pairing_Popup1)
        bluetooth_popup1.click()

    def Accept_Bluetooth_pairing_Popup2(self):
        sleep(2)
        bluetooth_popup2 = self.poco(self.Bluetooth_pairing_Popup2)
        bluetooth_popup2.click()

    def Verify_Connect_Wifi_Network_Text(self):
        if assert_exists(self.Connect_Wifi_Network_Text, "Connect Wi-Fi Network Text is displaying"):
            print("Connect Wi-Fi Network Text is displaying.")
        else:
            print("Connect Wi-Fi Network Text is not displaying.")

    def click_Connect_Btn_On_Connect_Wifi_Network_Screen(self):
        connect_btn = self.poco(self.Connect_Btn_On_Connect_Wifi_Network_Screen)
        connect_btn.click()

    def click_Password_Field_On_Join_Network(self):
        sleep(2)
        password = self.poco(self.Password_Field_On_Join_Network)
        if password.exists() and password.attr('enabled'):
            password.click()
            sleep(2)
            poco(text("123456789"))
        else:
            pass

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
        if self.poco(name="Connecting to Wi-Fi Network").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def Verify_Need_the_Printer_Driver_Text(self):
        sleep(3)
        if self.poco(name="Need the Printer Driver?").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def Verify_Registering_your_Printer_Text(self):
        sleep(2)
        if self.poco(name="Registering your Printer").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def Verify_Connected_Text(self):
        sleep(7)
        if self.poco(name="Connected!").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def click_Finish_Setup_Button(self):
        try:
            finish_btn = self.poco(self.Finish_Setup_Button)
            finish_btn.wait(20).visible().click()
        except PocoTargetTimeout:
            print("Finish button did not become visible within 10 seconds.")
            sleep(3)

    def click_FirstOne_In_MyDesign(self):
        touch(self.FirstOne_In_MyDesign)

    def click_Print_Option(self):
        print_option = self.poco(self.Print_Option)
        print_option.click()
        sleep(3)

    def click_Print_Button(self):
        sleep(2)
        sleep(2)
        start_point = (0.5, 0.7914691943127962)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.5, 0.4928909952606635)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        print_button = self.poco(self.Print_Button)
        print_button.click()
        sleep(5)

    def Verify_Design_Preview_Screen_With_Details(self):
        sleep(3)
        assert_exists(self.Design_Preview_With_Details, "Design Preview With Details is displaying correctly")

    def click_The_Back_Icon_Of_Print_Review_Screen(self):
        sleep(2)
        back_button = self.poco(self.Back_Icon_Of_Print_Review_Screen)
        back_button.click()

    def click_SecondOne_In_MyDesign(self):
        touch(self.SecondOne_In_MyDesign)

    def click_Common_Design_Tab(self):
        common_design = self.poco(self.Common_Design_Tab)
        common_design.click()


    def click_FirstOne_Design_In_Common_Design(self):
        sleep(3)
        FirstOne_Design_In_Common_Design = self.poco(self.FirstOne_Design_In_Common_Design)
        FirstOne_Design_In_Common_Design.click()

    def click_FirstOne_In_Common_Design(self):
        sleep(5)
        FirstOne_In_Common_Design = self.poco(self.FirstOne_In_Common_Design)
        FirstOne_In_Common_Design.click()
