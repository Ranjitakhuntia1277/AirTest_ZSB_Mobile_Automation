from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.APP_Settings_Screen import App_Settings_Screen
from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(2.0)

common_method = Common_Method(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)


def test_PrinterManagement_TestcaseID_47920():
    """""""""test"""""


# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# login_page.click_GooglemailId()
# sleep(5)
# login_page.add_Account()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"To enter password need to use the 2nd method """
# login_page.Enter_Google_Password()
#username - zsbswdvt@gmail.com
#password - zsbswdvt@1234
# # poco(text("Swdvt@#123"))
# # sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# help_page.chooseAcc()
"""Click hamburger icon to expand menu"""
sleep(5)
login_page.click_Menu_HamburgerICN()
sleep(2)
"""Swipe up"""
scroll_view = poco("android.widget.ScrollView")
# Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 1
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
# swipe((0.41574074074074074, 0.6816239316239316), (0.41574074074074074, 0.39487179487179486))
"""Open Printer settings"""
app_settings_page.click_Printer_Settings()
sleep(2)
"""Select printer"""
app_settings_page.click_PrinterName_On_Printersettings()
sleep(2)
"""Rename printer1 to printer2 name"""
printer_management_page.setPrinterName("ZSB-DP12")
sleep(2)
"""Verify is '(1)' is append to the duplicate name"""
"""Unable to verify due to BUG"""
printer_management_page.verifyPrinterNameAfterRenaming("ZSB-DP12")
sleep(2)


def test_PrinterManagement_TestcaseID_47882():
    """""""""test"""""


"""Click three dot menu of target printer"""
printer_management_page.clickThreeDotMenu()
sleep(5)
"""Click on delete printer"""
printer_management_page.clickDelete()
sleep(2)
"""Verify first Delete dialog pop up window"""
printer_management_page.checkDeletePopUp(1)
sleep(2)
"""Choose delete option"""
printer_management_page.clickDelete()
sleep(2)
"""Verify second Delete dialog pop up window"""
printer_management_page.checkDeletePopUp(2)
sleep(2)
"""Click Yes Delete option"""
printer_management_page.clickYesDelete()
sleep(2)
"""Verify if there is a pop up: Unpair Printer From Bluetooth"""
printer_management_page.checkUnpairBluetoothPopUp()
sleep(2)
"""Verify if the pop up has Drop Down option"""
printer_management_page.checkDropDownMenuIconIsPresent()
sleep(2)
"""Click Drop Down option"""
printer_management_page.clickDropDownMenuIcon()
sleep(2)
"""Verify if the info in the Drop DOwn matches with the expected info"""
printer_management_page.checkDropDownMenuInfo()
sleep(2)
"""Unpair device in blueetooth settings"""
"""Click Done"""
printer_management_page.clickDoneOption()


def test_PrinterManagement_TestcaseID_47785():
    """""""""test"""""


"""Click three dot menu of target printer"""
printer_management_page.clickThreeDotMenu()
sleep(5)
"""Click on delete printer"""
printer_management_page.clickDelete()
sleep(2)
"""Verify first Delete dialog pop up window"""
printer_management_page.checkDeletePopUp(1)
sleep(2)
"""Choose delete option"""
printer_management_page.clickDelete()
sleep(2)
"""Verify second Delete dialog pop up window"""
printer_management_page.checkDeletePopUp(2)
sleep(2)
"""Click Yes Delete option"""
printer_management_page.clickYesDelete()
sleep(2)
"""Verify Message box prompt appears "Unpair Bluetooth From Printer" along printer MAC address"""
printer_management_page.checkUnpairBluetoothPopUp()
"""Message box Does not contain MAC address"""
"""Click Drop Down option"""
printer_management_page.clickDropDownMenuIcon()
sleep(2)
"""Check if Done option is greyed out"""
printer_management_page.clickDoneOption()
printer_management_page.checkUnpairBluetoothPopUp()
"""Unpair device in blueetooth settings"""
"""Click Done"""
printer_management_page.clickDoneOption()
printer_management_page.checkBuyMoreLabelsOptionPresent()
"""Check if printer is decommissioned"""
printer_management_page.checkIfPrinterIsDecommissioned()

