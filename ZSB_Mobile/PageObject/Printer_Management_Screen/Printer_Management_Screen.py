# LoginFunction.py
from platform import platform

# import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
# from pipes import Template
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.assertions import assert_exists, assert_equal
from airtest.core.api import *
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen


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
        self.Buy_More_Labels = "Buy More Labels"
        self.NameOfDecommissioningPrinter = ""

    def setPrinterName(self, printername):
        printer_name = self.poco(self.Printer_Name)
        printer_name.click()
        printer_name.set_text("ZSB-DP12")

    def verifyPrinterNameAfterRenaming(self, printername):
        printer1 = self.poco(self.Printer1)
        expected_name = printername + "(1)"
        assert_equal(printer1.get_text(), expected_name,
                     "Successfully appended '(1)' on renaming both printers with same name")

    def get_printer_status(self):
        printer_info = self.poco("android.widget.ScrollView").child()[0].child().child().child().get_name()
        return printer_info.split('\n')[0]

    def clickThreeDotMenu(self):
        touch(self.Three_Dot_Menu)
        printer_details = poco("android.widget.ScrollView").child().child().child().child()[0].get_name()
        if printer_details[0:6] == "Online":
            self.NameOfDecommissioningPrinter += printer_details[6:len(printer_details) - 45]
        else:
            self.NameOfDecommissioningPrinter += printer_details[7:len(printer_details) - 45]

    def clickDelete(self):
        self.poco(self.Delete).click()

    def checkDeletePopUp(self, popupcount):
        popup_content = self.poco("android.view.View")[4].child().get_name()
        if popup_content[0:14] == "Delete Printer":
            return
        else:
            print(f"Popup number {popupcount} did not appear")
            return 1 / 0

    def clickYesDelete(self):
        self.poco(self.Yes_Delete).click()

    def checkUnpairBluetoothPopUp(self):
        unpairbluetoothtitle = self.poco("android.view.View")[4].child().get_name()[0:29]
        if unpairbluetoothtitle == "Unpair Bluetooth From Printer":
            return
        else:
            print("Unpair Printer From Bluetooth Pop Up not present.")
            return 1 / 0

    def checkDropDownMenuIconIsPresent(self):
        assert_exists(self.Drop_Down_Menu_Icon, "Drop Down Menu Icon is present.")

    def clickDropDownMenuIcon(self):
        touch(self.Drop_Down_Menu_Icon)

    def checkDropDownMenuInfo(self):
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

    def clickDoneOption(self):
        self.poco("android.view.View")[4].child().child().click()

    def checkBuyMoreLabelsOptionPresent(self):
        return self.poco(self.Buy_More_Labels).exists()

    def checkIfPrinterIsDecommissioned(self):
        printer_details = self.poco("android.widget.ScrollView").child().child().child().child()[0].get_name()
        if printer_details[0:6] == "Online":
            printerName = printer_details[6:len(printer_details) - 45]
        else:
            printerName = printer_details[7:len(printer_details) - 45]
        if printerName == self.NameOfDecommissioningPrinter:
            return
        else:
            print("Printer not decommissioned.")
            return 1/0

    def openBluetoothSettings(self):
        os.system('adb shell am start -a android.settings.BLUETOOTH_SETTINGS')

