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
from poco.exceptions import PocoTargetTimeout
import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join("Documents\\New_ZSB_Automation\ZSB_Mobile\\templates", a)

else:
    def Basic_path(a):
        # return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)
        return os.path.join(os.path.expanduser('~'),
                            "Desktop\ZSB_Automation\ZSB_Mobile\\TestExecution\\test_App_Settings", a)


class Printer_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Name = "android.widget.EditText"
        self.Printer1 = "ZSB-DP12_2"
        self.Three_Dot_Menu = Template(Basic_path(r"tpl1720170900189.png"), record_pos=(0.414, -0.557), resolution=(1080, 2400))
            # Template(Basic_path(r"tpl1705378684557.png"), record_pos=(0.402, -0.5), resolution=(1080, 2340)))
        self.Delete = "Delete"
        self.Yes_Delete = "Yes, Delete"
        self.Drop_Down_Menu_Icon = Template(Basic_path("tpl1705382553515.png"), record_pos=(0.334, 0.155), resolution=(1080, 2340))
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
        try:
            touch(self.Three_Dot_Menu)
        except:
            self.poco(nameMatches="(?s).*line.*").focus([0.95, 0.1]).click()
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
        sleep(3)
        noPrinter = self.poco(nameMatches="(?s).*Add a printer to get started. We’ll help you set things up.*").exists()
        if noPrinter:
            pass
        else:
            printer_details = self.poco("android.widget.ScrollView").child().child().child().child()[0].get_name()
            if printer_details == printer_name:
                raise Exception("Printer not decommissioned.")

    def openBluetoothSettings(self):
        os.system('adb shell am start -a android.settings.BLUETOOTH_SETTINGS')

    def switchApp(selfself):
        os.system('adb shell input keyevent KEYCODE_APP_SWITCH')

    def getDeviceNameToUnpair(self):
        device_name = self.poco(nameMatches="(?s).*Unpair.*").get_name().split("\n")[-3].split(" ")[-4]
        if device_name[0] == "(":
            device_name = device_name[4:]
        return device_name

    def unpair_bluetooth_device(self):
        connected_device = 0
        device_name = self.getDeviceNameToUnpair()
        print(device_name)
        self.openBluetoothSettings()
        self.poco(nameMatches="(?s).*device.*").wait_for_appearance(timeout=10)
        sleep(3)
        if self.poco(text="See all").exists():
            self.poco(text="See all").click()
        prev_last_dev = ""
        curr_last_dev = self.getDeviceNameSettings(-1)
        while prev_last_dev != curr_last_dev:
            print(curr_last_dev)
            print(prev_last_dev)
            print("1")
            if self.poco(textMatches="(?s).*"+device_name+".*").exists():
                print("2")
                if self.poco("com.android.settings:id/recycler_view").exists():
                    print("3")
                    connected_device = len(self.poco("com.android.settings:id/recycler_view").child())
                    print("length", connected_device)
                elif self.poco("com.android.settings:id/tw_expandable_listview").exists():
                    print("4i")
                    connected_device = len(self.poco("com.android.settings:id/tw_expandable_listview").child())

                for i in range(connected_device-1):
                    print("i", i)
                    curr_device = self.getDeviceNameSettings(i)
                    print(self.getDeviceNameSettings(i))

                    if device_name in curr_device:
                        print("last")
                        self.poco(textMatches="(?s).*"+device_name+".*").parent().parent().focus([0.95, 0.5]).click()
                        sleep(5)
                        try:
                            self.poco(text="Forget device").click()
                        except:
                            self.poco(text="Forget").click()
                            sleep(2)
                            self.poco(text="Forget device").click()
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
            curr_last_dev = self.getDeviceNameSettings(-1)

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

    def Login_With_Email_Tab(self):
            sleep(9)
            zebra_login = self.poco(text="Sign In with your email")
            zebra_login.click()
            sleep(2)
            self.poco(text(""))
            self.poco(text("zebra04.swdvt@gmail.com"))
            sleep(1)

    def Enter_Zebra_Password(self):
        password = self.poco("android.widget.EditText")[1]
        password.set_text("Zebra#123456789")

    def click_Password_TextField(self):
        sleep(1)
        # poco.scroll()
        sleep(1)
        self.poco(name="submit_id").click()

    def click_SignIn_Button(self):
        sleep(1)
        self.poco("android.widget.Button")[1].click()
        sleep(10)