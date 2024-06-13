import logging

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
# from ZSB_Mobile.PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
import pytest
from airtest.core.api import connect_device
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_PDF_Printing:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
pdf_printing = PDF_Printing_Screen(poco)
""""""""""Printer should be added in Google account-zebra21.dvt@gmail.com
Password: Swdvt@#123""""""
# delete_account.switch_to_different_app()
# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

