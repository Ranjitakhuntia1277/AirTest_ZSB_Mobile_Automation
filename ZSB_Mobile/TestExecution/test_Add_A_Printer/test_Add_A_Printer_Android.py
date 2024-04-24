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
        self.Start_Btn = "Start Setup"
        self.Lets_Make_Sure_Text = "Let's make sure the printer is in Bluetooth pairing mode."
        self.Searching_For_Your_Printer_Tex = "Searching for your printer"
        self.Next_Button= "Next"
        self.Printer_LED_Not_Flashing_Text = "My Printer’s LED is Not Flashing Blue What Does The LED Light Indicator Mean"
        self.Blue_Left_LED = "Blue Left LED"
        self.To_Find_Your_Printer_Text = "To find your printer, please ensure your printer’s LED is flashing blue like the example below."
        self.Printer_LED_Image = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1705903757611.png"), record_pos=(-0.007, 0.041),
                                          resolution=(1080, 2400))
        self.LED_Light_Behavior_Support_Text = "LED Light Behavior Support"
        self.the_Position_of_all_the_Buttons = Template(os.path.join(os.path.expanduser('~'),
                                                                     "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                     "tpl1705913879009.png"), record_pos=(0.001, 0.002),
                                                        resolution=(1080, 2400))
        self.LED_Guide_Button = "LED Guide"
        self.Red_Right_LED = "Red Right LED"
        self.Printer_LED_Guide_Done_Btn = "Dismiss"
        self.Select_your_printer_Text = "Select your printer"
        self.Pairing_Your_Printer_Text = "Connecting to printer"
        self.Printer_Name_To_Select = ""
        self.Bluetooth_pairing_Popup1 = "android:id/action0"
        self.Bluetooth_pairing_Popup2 = "android:id/button1"
        self.Searching_for_wifi_networks_Text = "Searching for Wi-Fi Networks"
        self.Select_Different_Network_Text = "Select Different Network"
        self.Zebra_Network = "Zebra"
        self.Discovered_Devices_Text = "Discovered printers"
        self.ZSB_Printer_images = Template(os.path.join(os.path.expanduser('~'),
                                                        "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                        "tpl1706510933463.png"), record_pos=(-0.334, -0.229),
                                           resolution=(1080, 2400))

        self.Show_All_Printers = "Show all printers"
        self.Added_Printer = "ZSB-DP12C710B9"
        self.Second_Printer_Name = "android.widget.RadioButton"
        self.Connect_Wifi_Network_Text = "Connect Wi-Fi Network"



        self.Select_Button_on_Select_Your_Printer = "Next"
        self.Connect_Btn_On_Connect_Wifi_Network_Screen = "Connect"
        self.Password_Field_On_Join_Network = Template(r"tpl1712913927236.png", record_pos=(-0.048, -0.44), resolution=(1080, 2400))

        self.Submit_Button_ON_Join_Network = "Submit"
        self.Registering_your_Printer_Text = "Registering your Printer"
        self.Finish_Setup_Button = "Finish Setup"

        # """"""""""""""""""""""""""""""""""""""""""""""""smoke test-need to add""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.FirstOne_In_MyDesign = ""

        self.Print_Option = "Print"
        self.Print_Button = "Print"
        self.Design_Preview_With_Details = Template(os.path.join(os.path.expanduser('~'),
                                                                 "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                 "tpl1707902210476.png"), record_pos=(0.047, 0.202),
                                                    resolution=(1170, 2532))
        self.Back_Icon_Of_Print_Review_Screen = "android.widget.Button"
        self.SecondOne_In_MyDesign = ""
        self.Common_Design_Tab = "Common Designs"

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
        led_not_flashing_text= self.poco(self.Printer_LED_Not_Flashing_Text)
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
        sleep(2)
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

    # def Verify_same_ZSB_image_for_all_items(self):
    #
    #     # if assert_exists(self.ZSB_Printer_images, "Only ZSB Printers are present"):
    #     if (self.ZSB_Printer_images, "Only ZSB Printers are present").exists():
    #         print("ZSB Printers are present for all items.")
    #     else:
    #         print("ZSB Printers are not present for all items.")

    def Verify_same_ZSB_image_for_all_items(self):
        if self.ZSB_Printer_images.exists():
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
        Connecting_to_WiFi_Network_Text= self.poco(name="Connecting to Wi-Fi Network")
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
        assert_exists(self.Design_Preview_With_Details, "Design Preview With Details is displaying correctly")

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


    def Click_Next_Button(self):
        sleep(1)
        Next_Button = self.poco(self.Next_Button)
        Next_Button.click()

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