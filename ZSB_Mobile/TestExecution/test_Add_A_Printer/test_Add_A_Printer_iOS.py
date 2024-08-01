# from poco.drivers.ios import iosPoco
import uuid

import logdir
# import logdir
import poco.drivers.ios
from airtest.core.api import *
# from test.body import poco
from airtest.core.api import connect_device, sleep
from airtest.core.api import start_app
from poco.drivers.ios import iosPoco


# Specify the device's platform (Android or iOS) and other details

class Add_A_PrinterScreen:
    pass


device_info = {
    # specify the device ID or name

    "platform": "iOS",  # or "iOS"
    "uuid": "00008101-00051D400144001E",
}
print(f"device_info: {device_info}")
print(f"device function result: {device()}")
uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://"+uuid)
poco = iosPoco(device= Bonding)

auto_setup(logdir=logdir, compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho_app")
# sleep(2.0)
# poco = poco.iosPoco()
# poco = iosPoco()



def test_Addprinter_TestcaseID_45656():
    """"Adding the moneybadger while the mobile devices bluetooth is disabled"""


poco("Login").click()
sleep(1)

poco("Continue").click()
sleep(2)
"""""""select the login with google option"""""""""
poco("Continue with Google").click()
sleep(4)
"""""provide google user id & password"""
poco(name="Use another account").click()
sleep(3)
poco(name="Email or phone").click()
poco(text("soho.swdvt.01@gmail.com"))
poco(name="Next").click()
sleep(2)
poco(name="Enter your password").click()
poco(text("Swdvt@#123"))
"""""""""""click on login option"""""""""
# poco(text="Next").click()
sleep(7)
"""""""click on the left hamburger menu on the home page"""""""""
poco(name="Open navigation menu").click()
sleep(3)
"""""""get text method need to add for zebra logo text & account details"""""""""

"""""""click on add a printer"""""""
poco("Add A Printer").click()
sleep(2)

poco(name="Cancel").click()
sleep(3)
#

"""""""""click on add a printer"""""""""
poco("Add A Printer").click()
sleep(2)
poco("Let’s set up your printer").get_text()
sleep(2)
"""""decomission the printer manually"""
"""""""""click on add a printer"""""""""
poco("Start").click()
assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
sleep(5)
poco(name="Select your printer").get_text()

poco(name="android.widget.RadioButton").click()
poco(name="Select").click()
sleep(2)
""""""""""""" accept the pair request and pair it with proper wifi"""""""""""""""""""""""""""

# poco("Add A Printer", type="android.widget.Button").click()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """"""""" checking the moneybadger printer image is present or not """""
# """""decomission the printer manually"""
# """""""""click on add a printer"""""""""
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# device_id = '2A051JEGR15175'
# """Run the command to turn on the Bluetooth of the device."""""
# os.system(f"adb -s {device_id} shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE")
# time.sleep(5)
# poco(text="Allow", type="android.widget.Button").click()
# sleep(10)
# poco(name="Unable to pair your printer").exists()
# poco(name="Important: There was an error pairing the printer to your mobile device. Please open your device's Bluetooth settings and unpair your connection to this printer before trying again.").exists()
# device_id = '2A051JEGR15175'
# """Run the command to turn on the Bluetooth of the device."""""
# os.system(f"adb -s {device_id} shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
# time.sleep(5)
# poco(text="Allow", type="android.widget.Button").click()
# poco(name="Try Again").click()
# poco(name=" Pairing your printer").exists()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# sleep(8)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(4)
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)


# def test_Addprinter_TestcaseID_45657():
#     """"Check the cancle button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""
# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""decomission the printer manually"""
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(7)
# """"Click on 1st cancel option on bluetooth pairing popup"""""
# poco(name="android:id/action0").click()
# sleep(8)
# """"Click on 2nd cancel option on bluetooth pairing popup"""""
# poco(name="android:id/button2").click()
# poco(name="Unable to pair your printer").exists()
# poco(name="Important: There was an error pairing the printer to your mobile device. Please open your device's Bluetooth settings and unpair your connection to this printer before trying again.").exists()
#
# poco(name="Try Again").click()
# poco(name=" Pairing your printer").exists()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# sleep(8)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(4)
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)


# def test_Addprinter_TestcaseID_45658():
#     """"Check pairing bluetooth when the printer changes to offline"""
# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""decomission the printer manually"""
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# sleep(2)
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(7)
# """"Click on 1st cancel option on bluetooth pairing popup"""""
# poco(name="android:id/action0").click()
# sleep(8)
# """"Click on 2nd cancel option on bluetooth pairing popup"""""
# poco(name="android:id/button2").click()
# poco(name="Unable to pair your printer").exists()
# poco(name="Important: There was an error pairing the printer to your mobile device. Please open your device's Bluetooth settings and unpair your connection to this printer before trying again.").exists()
# poco(name="Watch Troubleshooting Video").exists()
# poco(name="Get Help").exists()
# poco(name="Try Again").click()
# poco(name=" Pairing your printer").exists()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# sleep(8)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(4)
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)

# def test_Addprinter_TestcaseID_45659():
#     """""""Check the Watch Troubleshooting video option works when failing to connect printer"""


# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""decomission the printer manually"""
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# sleep(3)
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(20)
# poco(name="Unable to pair your printer").exists()
# poco(name="Important: There was an error pairing the printer to your mobile device. Please open your device's Bluetooth settings and unpair your connection to this printer before trying again.").exists()
# poco(name="Watch Troubleshooting Video").exists()
# poco(name="Watch Troubleshooting Video").click()
# sleep(3)
# poco(name="com.android.systemui:id/back").click()
# sleep(3)


# def test_Addprinter_TestcaseID_45660():
#     """"Search the essids when the printer is offline"""


# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# sleep(10)
# poco(name="Searching for Wi-Fi Networks").exists()
# """""decomission the printer manually"""
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(4)
# """""""Scroll method to search ZGuest network"""""""
# scroll_view = poco("android.widget.ScrollView")
# # Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 200
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
#
#     # Check if the "Accept" element is present and enabled
#     Enter_Network_Manually = poco(name="Enter Network Manually...")
#     if Enter_Network_Manually.exists() and Enter_Network_Manually.attr('enabled'):
#         Enter_Network_Manually = poco(name="Enter Network Manually...").click()
#         # Accept button is visible and enabled, break out of the loop
#         break
#     sleep(3)
# poco(name="android.widget.EditText").click()
# sleep(2)
# poco(text("Zebra"))
# sleep(2)
# poco(name="Join").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(15)
# poco(name="Failed to Connect").exists()
# poco(name="Your printer is unable to connect to the Wi-Fi network at this time. Please check that the password and/or network name are correct.").exists()
# """""Turn on the printer"""
# sleep(4)
# poco(name="Retry").click()
# sleep(8)
# poco.scroll(duration=1)
# poco.scroll(duration=1)
# poco.scroll(duration=1)
# poco.scroll(duration=1)
# poco.scroll(duration=1)
# sleep(2)
# poco(name="Enter Network Manually...").click()
# poco(name="android.widget.EditText").click()
# poco(text("Zebra"))
# poco(name="Join").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# poco(name="ZSB Printer is now connecting to your network").exists()
# sleep(20)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)
# # -------------------------------------------------------------------------------------------------------

# def test_Addprinter_TestcaseID_45661():
#     """"Set printer wpa psk Essid but input incorrect password, and check Help"""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Connect").click()
# """""""Enter WRONG password manually----123456788"""""""
# poco(name="Submit").click()
# sleep(10)
# poco(name="Failed to Connect").exists()
# poco(name="Help").click()
# sleep(4)
# poco(name="Zebra Logo").exists()
# poco(text="Where to buy").exists()
# poco(name="Close tab").click()


# def test_Addprinter_TestcaseID_45662():
#     """"set printer open Essid when the printer change to offline, and retry"""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# """"""Turn off the Printer after displaying select you wifi network"""""""
# poco(name="Select Different Network").click()
# sleep(4)
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Failed to Connect").exists()
# poco(name="Your printer is unable to connect to the Wi-Fi network at this time. Please check that the password and/or network name are correct.").exists()
# sleep(4)
# poco(name="Retry").click()
# sleep(2)
# poco(name="Select Different Network").click()
# sleep(5)
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(8)
# poco(name="ZSB Printer is now connecting to your network").exists()
# sleep(20)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(4)
# poco(name="android.view.View").exists()
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="Printer Settings").click()
# time.sleep(2)
# poco(name="ZSB-DP12").click()
# time.sleep(2)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)

# def test_Addprinter_TestcaseID_45663():
#     """"	set printer wpa psk Essid manually when the printer change to offline, and go to Help"""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# """"""Turn off the Printer after displaying select you wifi network"""""""
# poco(name="Select Different Network").click()
# sleep(6)
# """""""Scroll method to search ZGuest network"""""""
# scroll_view = poco("android.widget.ScrollView")
# # Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 200
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
#
#     # Check if the "Accept" element is present and enabled
#     Enter_Network_Manually = poco(name="Enter Network Manually...")
#     if Enter_Network_Manually.exists() and Enter_Network_Manually.attr('enabled'):
#         Enter_Network_Manually = poco(name="Enter Network Manually...").click()
#         # Accept button is visible and enabled, break out of the loop
#         break
#     sleep(3)
# poco(name="android.widget.EditText").click()
# sleep(2)
# poco(text("Zebra"))
# sleep(2)
# poco(name="Join").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(15)
# poco(name="Failed to Connect").exists()
# poco(name="Your printer is unable to connect to the Wi-Fi network at this time. Please check that the password and/or network name are correct.").exists()
# sleep(4)
# poco(name="Help").click()
# sleep(4)
# poco(name="Zebra Logo").exists()
# poco(text="Where to buy").exists()
# poco(name="Close tab").click()
# """""Turn on the printer"""


# def test_Addprinter_TestcaseID_45664():
#     """"	set printer open Essid manually but input incorrect essid, and retry"""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(10)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(5)
# """""""Scroll method to search ZGuest network"""""""
# scroll_view = poco("android.widget.ScrollView")
# # Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 200
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
#
#     # Check if the "Accept" element is present and enabled
#     Enter_Network_Manually = poco(name="Enter Network Manually...")
#     if Enter_Network_Manually.exists() and Enter_Network_Manually.attr('enabled'):
#         Enter_Network_Manually = poco(name="Enter Network Manually...").click()
#         # Accept button is visible and enabled, break out of the loop
#         break
#     sleep(3)
# poco(name="android.widget.EditText").click()
# """""""Enter wrong network name"""""""
# poco(text("Zebraa"))
# poco(name="Join").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(9)
# poco(name="Failed to Connect").exists()
# poco(name="Your printer is unable to connect to the Wi-Fi network at this time. Please check that the password and/or network name are correct.").exists()
# sleep(4)
# poco(name="Retry").click()
# sleep(2)
# poco(name="Select Different Network").click()
# sleep(5)
# poco(name="Select your Wi-Fi network").exists()


# def test_Addprinter_TestcaseID_45665():
#     """Check the left top corner button of each page work during adding a moneybadger."""


# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# Check if the element exists on the screen
# home_object = poco(name="Home")
# print(home_object)
# sleep(2)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="MFW My First Workspace").exists()
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""Check the moneybadger image is present"""
# poco(name="android.widget.ImageView").get_position()
# poco(name="First we’ll pair your printer to your phone using Bluetooth. Tap Start to begin.").exists()
# poco(name="Start").get_name()
# """""Click on the cross icon of the Let's setup your printer page"""
# poco(name="android.widget.Button").click()
# """"Click on Cancel button of Exit printer setup popup"""
# poco(name="Cancel").click()
# sleep(1)
# poco("Let’s set up your printer").get_text()
# """""Click on the cross icon of the Let's setup your printer page"""
# poco(name="android.widget.Button").click()
# """""Click on the OK button of Exit printer setup popup"""
# poco(name="Ok").click()
# sleep(1)
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# sleep(5)
# poco(name="Select your printer").get_text()
# sleep(1)
# """""Click on the close icon of the Select printer page"""
# poco(name="android.widget.Button").click()
# sleep(1)
# poco("Let’s set up your printer").get_text()
# poco("Start", type="android.widget.Button").click()
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(8)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Select Different Network").click()
# sleep(6)
# """""close icons are not accessible for Connect wifi network page & Select your WI-FI network screen"""
# poco(name="Zebra").click()
# """"enter password manually"""""
# poco(name="Submit").click()
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)

# /////////////Phone A & B testcases are not automated////////////////////////////////


# def test_Addprinter_TestcaseID_45673():
#     """connect printer with Open Essid by choosing it"""


# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(6)
# """""""Select the open wifi network & proceed"""
# """""""Scroll method to search ZGuest network"""""""
# scroll_view = poco("android.widget.ScrollView")
# # Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 200
#
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
#
#     # Check if the "Accept" element is present and enabled
#     ZGuest = poco(name="ZGuest")
#     if ZGuest.exists() and ZGuest.attr('enabled'):
#         ZGuest = poco(name="ZGuest").click()
#         # Accept button is visible and enabled, break out of the loop
#         break
#     sleep(7)
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()
# sleep(3)


# def test_Addprinter_TestcaseID_45674():
#     """connect printer with Open ESSID manually, then cancel."""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# poco("Let’s set up your printer").get_text()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# assert_equal("Searching for your printer", "Searching for your printer", "Text is matching")
# # sleep(5)
# poco(name="Select your printer").get_text()
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Select Different Network").click()
# sleep(6)
# """""""Scroll method to search ZGuest network"""""""
# scroll_view = poco("android.widget.ScrollView")
# # Set the maximum number of swipes to avoid an infinite loop
# max_swipes = 200
# for _ in range(max_swipes):
#     # Swipe up on the ScrollView
#     scroll_view.swipe("up", duration=0.1)
#
#     # Check if the "Accept" element is present and enabled
#     Enter_Network_Manually = poco(name="Enter Network Manually...")
#     if Enter_Network_Manually.exists() and Enter_Network_Manually.attr('enabled'):
#         Enter_Network_Manually = poco(name="Enter Network Manually...").click()
#         # Accept button is visible and enabled, break out of the loop
#         break
#     sleep(3)
# poco(name="Open").click()
# poco(name="Open").click()
# sleep(1)
# poco(name="Cancel").click()
# sleep(2)
# poco(name="Select your Wi-Fi network").exists()


# def test_Addprinter_TestcaseID_45675():
#     """Connect printer with Open Essid manually when it's status is media out"""

# login_page = Login_Screen(poco)
# add_a_printer_screen = Add_A_Printer_Screen(poco)
# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# """""""""""""""Always use this to login"""""""""""""""
# sleep(7)
# """""""click on the left hamburger menu on the home page"""""""""
# poco(name="Open navigation menu").click()
# sleep(3)
# """""""get text method need to add for zebra logo text & account details"""""""""
#
# """""""click on add a printer"""""""
# add_a_printer_screen.click_Add_A_Printer()
# sleep(2)
# """""""""click on add a printer"""""""""
# poco(name="Start", type="android.widget.Button").click()
# # sleep(5)
# poco(name="android.widget.RadioButton").click()
# poco(name="Select", type="android.widget.Button").click()
# sleep(2)
# """""""pair & connect text on bluetooth paring popup"""""""
# poco(name="android:id/action0").click()
# """"""""""click on next allow button"""""
# poco(name="android:id/button1").click()
# poco(name="Pairing your printer").exists()
# sleep(7)
# poco(name="Searching for Wi-Fi Networks").exists()
# poco(name="Zebra").exists()
# poco(name="Connect").click()
# poco(name="Cancel").get_text()
# """""""Enter password manually----123456788"""""""
# poco(name="Submit").click()
# sleep(10)
# poco(name="Connecting to Wi-Fi Network").exists()
# sleep(7)
# poco(name="Registering your Printer").exists()
# poco(name="Connected!").exists()
# poco(name="Finish Setup").click()
# sleep(3)
# sleep(3)
# poco(name="Open navigation menu").click()
# sleep(3)
# poco(name="android.widget.Button").click()
# sleep(1)
# poco.scroll()
# sleep(2)
# poco(name="Log Out", type="android.widget.Button").click()

