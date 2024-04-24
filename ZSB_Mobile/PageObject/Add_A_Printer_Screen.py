# LoginFunction.py
from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method

class Add_A_Printer_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.Add_A_Printer_Btn = "Add A Printer"

    def click_Add_A_Printer(self):
        add_a_printer_btn = self.poco(self.Add_A_Printer_Btn)
        add_a_printer_btn.click()


