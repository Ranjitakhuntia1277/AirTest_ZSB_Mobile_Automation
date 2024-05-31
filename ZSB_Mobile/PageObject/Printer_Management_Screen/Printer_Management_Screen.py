# LoginFunction.py
from platform import platform

# import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
# from pipes import Template
from airtest.core.cv import Template
from poco import poco
from ...Common_Method import Common_Method
from airtest.core.assertions import assert_exists, assert_equal
from airtest.core.api import *
from ...PageObject.Login_Screen import Login_Screen


class Printer_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Name = "android.widget.EditText"
        self.Printer1 = "ZSB-DP12_2"
        self.Three_Dot_Menu = Template(r"tpl1705378684557.png", record_pos=(0.402, -0.5), resolution=(1080, 2340))
        self.Delete = "Delete"
        self.Yes_Delete = "Yes, Delete"
        self.Drop_Down_Menu_Icon = Template(r"tpl1705382553515.png", record_pos=(0.334, 0.155), resolution=(1080, 2340))
        self.Drop_Down_Menu_Info = "1.\nOpen your mobile device Settings\n2.\nSelect Bluetooth\n3.\nEnable Bluetooth if it's OFF\n4.\nSelect Device info ZSB-DP14-C66CB7 from My Devices\n5.\nSelect Forget This Device"
        """name = drop_down_info.split("\n")[-3][19:-16]"""
        self.Buy_More_Labels = "Buy More Labels"
        self.NameOfDecommissioningPrinter = ""

    def setPrinterName(self, printername):
        printer_name_field = self.poco("android.widget.EditText")
        printer_name_field.click()
        printer_name_field.set_text(printername)

    def verifyPrinterNameAfterRenaming(self, printername):
        expected_name = printername + "(1)"
        printer_1_name = self.poco("android.widget.HorizontalScrollView").child()[1].get_name().split("\n")[0]
        print(expected_name, printer_1_name)
        if printer_1_name == expected_name:
            pass
        else:
            raise Exception("Renaming printer 1 with same name as printer 2 not succesful.")

    def get_printer_status(self):
        printer_info = self.poco("android.widget.ScrollView").child()[0].child().child().child().get_name()
        return printer_info.split('\n')[0]

    def clickThreeDotMenu(self):
        NameOfDecommissioningPrinter = self.poco(nameMatches="(?s).*line.*").get_name()
        touch(self.Three_Dot_Menu)
        return NameOfDecommissioningPrinter

    def clickDelete(self):
        self.poco(self.Delete, enabled=True).wait_for_appearance(timeout=10)
        self.poco(self.Delete).click()

    def checkDeletePopUp(self, popupcount):
        try:
            if popupcount == 1:
                self.poco(nameMatches="(?s).*Delete Printer.*").wait_for_appearance(timeout=10)
            else:
                self.poco("Delete Printer\nAre you sure you want to delete your printer?").wait_for_appearance(timeout=10)
        except:
            if popupcount == 1:
                raise Exception("Message box prompt\"Unpair Bluetooth From Printer\" did not appear")
            else:
                raise Exception("\"Delete Printer\nAre you sure you want to delete your printer?\" pop up did not appear")

    def clickYesDelete(self):
        self.poco(self.Yes_Delete).click()

    def checkUnpairBluetoothPopUp(self):
        try:
            self.poco(nameMatches="(?s).*Unpair Bluetooth From Printer.*").wait_for_appearance(timeout=20)
        except:
            raise Exception("Unpair Printer From Bluetooth Pop Up not present.")

    def checkDropDownMenuIconIsPresent(self):
        assert_exists(self.Drop_Down_Menu_Icon, "Drop Down Menu Icon is present.")

    def clickDropDownMenuIcon(self):
        touch(self.Drop_Down_Menu_Icon)

    def checkDropDownMenuInfo(self):
        """change this"""
        dropdowninfo = self.poco("android.view.View")[4].child().get_name()[197:]
        if dropdowninfo == self.Drop_Down_Menu_Info:
            return
        else:
            print("info on app\n" + dropdowninfo)
            print("------------")
            print("expected info:\n" + self.Drop_Down_Menu_Info)
            print("DropDown Menu info doesn't match.")
            return 1 / 0

    def checkDoneOptionIsPresent(self):
        if self.poco("android.view.View")[4].child().child().get_name() == "Done":
            return
        else:
            print("Done option not present.")
            return 1 / 0

    def checkElementIsGreyedOut(self, element):
        return self.poco(element, enabled=False).exists()

    def clickDoneOption(self):
        self.poco("android.view.View")[4].child().child().click()

    def checkBuyMoreLabelsOptionPresent(self):
        return self.poco(self.Buy_More_Labels).exists()

    def getDeviceNameSettings(self, index):
        device = self.poco("android:id/title")[index].get_text()
        if device[0] is not "Z":
            device = device[1:-1]
        return device

    def checkIfPrinterIsDecommissioned(self, printer_name):
        printer_details = self.poco("android.widget.ScrollView").child().child().child().child()[0].get_name()
        if printer_details[0:6] == "Online":
            printerName = printer_details[6:len(printer_details) - 45]
        else:
            printerName = printer_details[7:len(printer_details) - 45]
        if printerName == self.NameOfDecommissioningPrinter:
            return
        else:
            raise Exception("Printer not decommissioned.")

    def openBluetoothSettings(self):
        os.system('adb shell am start -a android.settings.BLUETOOTH_SETTINGS')

    def switchApp(selfself):
        os.system('adb shell input keyevent KEYCODE_APP_SWITCH')

    def getDeviceNameToUnpair(self):
        return self.poco(nameMatches="(?s).*Unpair.*").get_name().split("\n")[-3].split(" ")[-4]

    def unpair_bluetooth_device(self):
        connected_device = 0
        device_name = self.getDeviceNameToUnpair()
        self.openBluetoothSettings()
        self.poco(nameMatches="(?s).*device.*").wait_for_appearance(timeout=10)
        prev_last_dev = ""
        curr_last_dev = self.getDeviceNameSettings(-2)
        while prev_last_dev != curr_last_dev:
            print("1")
            if self.poco(textMatches="(?s).*"+device_name+".*").exists():
                print("2")
                if self.poco("com.android.settings:id/recycler_view").exists():
                    print("3")
                    print(connect_device)
                    connected_device = len(self.poco("com.android.settings:id/recycler_view").child())
                    print(connected_device)
                elif self.poco("com.android.settings:id/tw_expandable_listview").exists():
                    print("4")
                    connected_device = len(self.poco("com.android.settings:id/tw_expandable_listview").child())

                for i in range(connected_device-1):
                    print(i)
                    curr_device = self.getDeviceNameSettings(i)
                    print(self.getDeviceNameSettings(i))

                    if curr_device == device_name:
                        self.poco(textMatches="(?s).*"+device_name+".*").parent().parent().focus([0.95, 0.5]).click()
                        # try:
                        #     self.poco("com.android.settings:id/preference_detail")[i].exists()
                        #     self.poco("com.android.settings:id/preference_detail")[i].click()
                        # except:
                        #     try:
                        #         self.poco("com.android.settings:id/settings_button")[i].exists()
                        #         self.poco("com.android.settings:id/settings_button")[i].click()
                        #     except:
                        #         self.poco("com.android.settings:id/deviceDetails")[i].exists()
                        #         self.poco("com.android.settings:id/deviceDetails")[i].click()
                        break
                break
            self.poco.scroll()
            prev_last_dev = curr_last_dev
            curr_last_dev = self.getDeviceNameSettings(-2)

        if self.poco(text="Unpair").exists():
            self.poco(text="Unpair").click()
            if self.poco(text="Unpair").exists():
                self.poco(text="Unpair").click()
        if self.poco(text="Forget").exists():
            self.poco(text="Forget").click()
        self.switchApp()
        self.switchApp()

    def clickPrinter1InPinterSettings(self):
        self.poco(nameMatches="(?s).*Common.*").wait_for_appearance(timeout=10)
        # self.poco("android.widget.HorizontalScrollView").child()[1].click()
        self.poco(nameMatches="(?s).*Common.*").parent().child()[1].click()

    def getPrinter2NameInPrinterSettings(self):
        return self.poco("android.widget.HorizontalScrollView").child()[2].get_name().split("\n")[0]

