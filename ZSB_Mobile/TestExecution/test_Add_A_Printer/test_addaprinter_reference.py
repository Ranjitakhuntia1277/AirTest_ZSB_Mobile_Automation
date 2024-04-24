import poco
from airtest.core.api import *
from airtest.core.api import *
from airtest.core.api import connect_device, device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


# from test.body import poco


# Specify the device's platform (Android or iOS) and other details

class Add_A_PrinterScreen:
    pass


device_info = {
    # specify the device ID or name
    "platform": "Android",  # or "iOS"
    "device": "2A051JEGR15175",
    # """"""ios device"""
    # "device": "00008101-00051D400144001E",
}

# Connect to the device
connect_device("Android:///" + device_info["device"])
# connect_device("iOS:///" + device_info["device"])
start_app("com.zebra.soho_app")
sleep(2.0)

# Initialize Poco
poco = AndroidUiautomationPoco()


# # poco = iosPoco()
#
#
# def test_Addprinter_TestcaseID_45656():
#     """"Adding the moneybadger while the mobile devices bluetooth is disabled"""


# device_id = '2A051JEGR15175'
# """Run the command to turn on the Bluetooth of the device."""
# os.system(f"adb -s {device_id} shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE")
# time.sleep(5)
# """""""""Click on the allow option after disabling the bluetooth"""""""""""
#
# poco(text="Allow", type="android.widget.Button").click()
# sleep(2)
# # """"""""Allow pop up before login for the fresh installation"""""""""
# # login_page.click_LoginAllow_Popup()
# # Find and click the "Login" button
# poco("Login", type="android.widget.Button").click()
# sleep(1)
# """""""select the login with google option"""""""""
# poco("Continue with Google", type="android.view.View").click()
# sleep(2)
# """""provide google user id & password"""
# poco(text="SWDVT IDC test account", type="android.widget.TextView").click()
# sleep(2)
# # poco(text("soho.swdvt.01@gmail.com"))
# poco(text("Swdvt@#123"))
# """""""""""click on login option"""""""""
# poco(text="Next", type="android.widget.Button").click()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# # poco(type="android.widget.Button").click()
# """"Click on settings button"""
# poco(name="Settings", type="android.widget.Button").click()
# poco(name="Navigate up").click()
# sleep(3)
# """"Click on cancel button"""
# poco("Cancel", type="android.widget.Button").click()
# sleep(2)
# # poco(name="Cancel", type= "android.widget.Button").click()
# """""""Turn on the Bluetooth of the device"""""""
# device_id = '2A051JEGR15175 '
# """Run the command to turn on the Bluetooth of the device."""
# os.system(f"adb -s {device_id} shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
# time.sleep(5)
# # """""""""Click on the allow option after enabling the bluetooth"""""""""""
# poco(text="Allow", type="android.widget.Button").click()
# sleep(3)
# """""""""click on add a printer"""""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""decomission the printer manually"""
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer", type="android.view.View ").get_text()
#
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """"""""""""" accept the pair request and pair it with proper wifi"""""""""""""""""""""""""""
#
def test_Addprinter_TestcaseID_45657():
    """"Check the cancle button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""

#
# # """"""""Allow pop up before login for the fresh installation"""""""""
# # login_page.click_LoginAllow_Popup()
# # Find and click the "Login" button
# poco("Login", type="android.widget.Button").click()
# sleep(1)
# """""""select the login with google option"""""""""
# poco("Continue with Google", type="android.view.View").click()
# sleep(2)
# """""provide google user id & password"""
# poco(text="SWDVT IDC test account", type="android.widget.TextView").click()
# sleep(2)
# poco(text("soho.swdvt.01@gmail.com"))
# poco(text("Swdvt@#123"))
# """""""""""click on login option"""""""""
# poco(text="Next", type="android.widget.Button").click()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer", type="android.view.View ").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""need to cancel pair button and verify the error message""""
# """"""verify 3 options & click on retry & pair the printer"""""
#
#
# def test_Addprinter_TestcaseID_45658():
#     """"Check pairing bluetooth when the printer changes to offline"""
#
#
# # poco("Login", type="android.widget.Button").click()
# # sleep(1)
# """""""select the login with google option"""""""""
# poco("Continue with Google", type="android.view.View").click()
# sleep(2)
# """""provide google user id & password"""
# poco(text="SWDVT IDC test account", type="android.widget.TextView").click()
# sleep(2)
# poco(text("soho.swdvt.01@gmail.com"))
# poco(text("Swdvt@#123"))
# """""""""""click on login option"""""""""
# poco(text="Next", type="android.widget.Button").click()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# sleep(3)
# """""""click on add a printer"""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer", type="android.view.View ").get_text()
#
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""""need to turn off the printer and verify the error message"""""
# """""""""verify 3 options & power on the printer and click on try again""""""""
# """"""""check pairing message and pair and add successfully"""""
#
#
# def test_Addprinter_TestcaseID_45659():
#     """""""Check the Watch Troubleshooting video option works when failing to connect printer"""
#
# # poco("Login", type="android.widget.Button").click()
# # sleep(1)
# """""""select the login with google option"""""""""
# poco("Continue with Google", type="android.view.View").click()
# sleep(2)
# """""provide google user id & password"""
# poco(text="SWDVT IDC test account", type="android.widget.TextView").click()
# sleep(2)
# # poco(text("soho.swdvt.01@gmail.com"))
# poco(text("Swdvt@#123"))
# """""""""""click on login option"""""""""
# poco(text="Next", type="android.widget.Button").click()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# sleep(3)
# """""""click on add a printer"""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer", type="android.view.View ").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""""need to turn off the printer and verify the error message"""""
# """""""""verify 3 options & power on the printer and click on troubleshooting video """"""""
# """"""""check the video and click on any blank space to dismiss"""""
#
#
#
#
# def test_Addprinter_TestcaseID_45660():
#     """"Search the essids when the printer is offline"""
#
# # poco("Login", type="android.widget.Button").click()
# # sleep(1)
# """""""select the login with google option"""""""""
# poco("Continue with Google", type="android.view.View").click()
# sleep(2)
# """""provide google user id & password"""
# poco(text="SWDVT IDC test account", type="android.widget.TextView").click()
# sleep(2)
# poco(text("soho.swdvt.01@gmail.com"))
# poco(text("Swdvt@#123"))
# """""""""""click on login option"""""""""
# poco(text="Next", type="android.widget.Button").click()
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# login_page.click_Menu_HamburgerICN()
# sleep(3)
# """""""click on add a printer"""""""
# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer", type="android.view.View ").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """"""''"""accept the pair button and on select your wifi network, turn off the printer & select enter network manually option"""""
# """"provide wifi id & password & check the failed to connect popup & messsage then turn on the printer provide wifi id & password and complete"""
#
