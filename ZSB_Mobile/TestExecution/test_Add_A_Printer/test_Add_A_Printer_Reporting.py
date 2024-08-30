import inspect

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
import pytest
from airtest.core.api import connect_device

from ...PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen
from ...TestSuite.api_call import insert_step, insert_case_results
from ...TestSuite.api_call import *
from ...TestSuite.api_call import *
import inspect
from ...TestSuite.store import *


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Add_A_Printer_Android:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
pdf_printing_android = PDF_Printing_Screen(poco)


# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# execID = 0
# leftId = {"0": "7"}


# def test_Addprinter_TestcaseID_45656():
#     """"Adding the moneybadger while the mobile devices bluetooth is disabled"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, ' Check the slide left page appear.'],
#         4: [4, 'Disable the Bluetooth.'],
#         5: [5, 'click the button Add a Printer.'],
#         6: [6, 'Verify Turn on bluetooth prompt message.'],
#         7: [7,
#             'click on Cancel button."'],
#         8: [8, 'Check the Lets set up your printer page will dismiss, and it will back to the slide left page.'],
#         9: [9,
#             'click the button Add a Printer button again.'],
#         10: [10, 'Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879.'],
#         11: [11,
#              'click on Cancel button.'],
#         12: [12,
#              ' Turn on the Bluetooth.'],
#         13: [13,
#              ' click the button Add a Printer button again.'],
#         14: [14, 'Check it would go to the page Lets set up your printer.'],
#
#         15: [15, 'Disable the Bluetooth.'],
#         16: [16, 'Check the moneybadger picture would appears at that page'],
#         17: [17, 'click start button'],
#         18: [18, 'Accept the popup'],
#         19: [19, 'click on next button'],
#         20: [20, 'Unable to find printer(s)" page'],
#         21: [21, 'Turn on the Bluetooth'],
#         22: [22, 'Check this time printer can connect to Wifi successfully'],
#         23: [23, 'Follow the prompt to proceed the adding printer process, check the printer can be added successfully'],
#         24: [24, 'Stop the app.']
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#
#         start_time = time.time()
#         """"1.Open the app and login the account to go to the overview page."""""
#         common_method.tearDown()
#         common_method.Clear_App()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         login_page.click_loginBtn()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         login_page.click_Loginwith_Google()
#         login_page.Loginwith_Added_Email_Id()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Disable the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(4)
#         """"click on Allow button on Bluetooth disable & enable popup"""
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"3. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"can not verify all these steps as these all are coming behind the popup"""
#         ### """Check it would go to the page "Let's set up your printer"""
#         ### add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         #### """""Check the moneybadger picture would appears at that page."""
#         #### add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         #### """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
#         """"Verify Turn on bluetooth prompt message"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click on Cancel button"""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Cancel_Btn()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Check the "Let's set up your printer" page will dismiss, and it will back to the slide left page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Slideleft_Page_Is_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click the button 'Add a Printer' button again"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click on Cancel button"""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Cancel_Btn()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Turn on the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Enable_Bluetooth()
#         sleep(4)
#         """"click on Allow button on Bluetooth disable & enable popup"""
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click the button 'Add a Printer' button again"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Disable the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(4)
#         add_a_printer_screen.click_Add_A_Printer()
#         """"click on Allow button on Bluetooth disable & enable popup"""
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """click start button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Accept the popup"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""click on next button"""
#         start_time = time.time()
#         add_a_printer_screen.Click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Unable to find printer(s)" page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Turn on the Bluetooth"""
#         start_time = time.time()
#         add_a_printer_screen.enable_bluetooth()
#         sleep(4)
#         add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """click on allow for enable bluetooth"""
#         start_time = time.time()
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Unable to find printer(s)" page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click search again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Search_Again_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""Verify Searching Your printer text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Verify Select your printer text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text_For_Add_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""Select the Target Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Select_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Select button"""
#         add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(15)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Turn off Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(5)
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#         """Verify Unable to connect to printer popup is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Turn on Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Enable_Bluetooth()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """click on Allow button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click on try again"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)
#
#         # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_Addprinter_TestcaseID_45657():
#     """"Check the cancle button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'Check it would go to the page Lets set up your printer.'],
#         5: [5, 'Check the moneybadger picture would appears at that page.'],
#         6: [6, 'Click on Start setup button.'],
#         7: [7, 'Verify Lets make sure the printer is in Bluetooth pairing mode. Text.'],
#         8: [8, 'click on Next Button.'],
#         9: [9, 'Verify Searching For your Printer Text.'],
#         10: [10, 'Verify Select your Printer Text.'],
#         11: [11, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Click on Cancel button on the bluetooth pairing popup.'],
#         15: [15, 'Verify "Unable to pair your printer"" page pops up.'],
#         16: [16, 'Verify Please try the following before attempting to connect to printer again.'],
#         17: [17, 'Open your devices Bluetooth settings and unpair your connection to this printer before trying again'],
#         18: [18, 'click on Try Again button.'],
#         19: [19, 'Check the printer can be paired successfully.'],
#         20: [20, 'Verify Connecting to printer Text.'],
#         21: [21, 'Verify Printer Connected Text.'],
#         22: [22, 'Verify Searching for Wifi network text is displaying.'],
#         23: [23, 'Verify Connect Wi-fi Network Text.'],
#         24: [24, 'Click previous network.'],
#         25: [25, 'Click on enter password.'],
#         26: [26, 'Click on connect button on connect wifi network screen.'],
#         27: [27, 'Verify Connecting to Cloud Text.'],
#         28: [28, 'Verify need the printer Setup Complete text.'],
#         29: [29, 'Click on finish setup button.'],
#         30: [30, 'click home tab.'],
#         31: [31, 'Stop the app.']
#
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#         start_time = time.time()
#         """"1.Open the app and login the account to go to the overview page."""""
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"3. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """4.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""5.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """6.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"7.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""8.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """12.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """14.Click on Cancel button on the bluetooth pairing popup"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Verify "Unable to pair your printer"" page pops up"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """16.Verify Please try the following before attempting to connect to printer again. Text"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Please_Try_The_Following_Before_Attempting_Again_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Check there are ""Try again"", ""Watch Troubleshooting Video"" and ""Get Help"" three options on the page----This has to be removed from testcase"""
#         """"17.Open your device's Bluetooth settings and unpair your connection to this printer before trying again."""""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         aps_notification.Stop_Android_App()
#         aps_notification.click_Mobile_SearchBar()
#         aps_notification.click_On_Searchbar2()
#         aps_notification.Enter_Settings_Text_On_SearchBar()
#         aps_notification.click_Settings()
#         aps_notification.click_Connected_Devices()
#         app_settings_page.click_Unpair_Icon()
#         app_settings_page.click_On_Unpair()
#         app_settings_page.click_Confirm_Delete_Popup()
#         aps_notification.Stop_Android_App()
#         common_method.Start_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.click on Try Again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""21.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """23.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"24.Click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """25.Click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.Click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """27.Verify Connecting to Cloud Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"28.Verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.Click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"30.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """31.stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)
#
# # ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
# def test_Addprinter_TestcaseID_45658_SemiAuto():
#     """"Check pairing bluetooth when the printer changes to offline"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         13: [13, 'Turn off the target printer from front panel Manually.'],
#         14: [14, 'Check the target printer on "Select your printer" page and click Select.'],
#         15: [15, 'Click on Next Button.'],
#         16: [16, 'Verify "Unable to pair your printer"" page pops up.'],
#         17: [17, 'Verify Please try the following before attempting to connect to printer again'],
#         18: [18, 'Power on the printer Manually.'],
#         19: [19, 'click on Try Again button.'],
#         20: [20, 'Check the printer can be paired successfully.'],
#         21: [21, 'Verify Connecting to printer Text.'],
#         22: [22, 'Verify Printer Connected Text.'],
#         23: [23, 'Verify Searching for Wifi network text is displaying.'],
#         24: [24, 'Verify Connect Wi-fi Network Text.'],
#         25: [25, 'click previous network.'],
#         26: [26, 'click on enter password.'],
#         27: [27, 'click on connect button on connect wifi network screen.'],
#         28: [28, 'Verify Connecting to Cloud Text.'],
#         29: [29, 'verify need the printer Setup Complete text.'],
#         30: [30, 'click on finish setup button.'],
#         31: [31, 'click home tab.'],
#         32: [32, 'Stop the app.']
#
#     }
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"12.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"13. Turn off the target printer from front panel Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"14. Check the target printer on "Select your printer" page and click Select"""
#         """Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"15.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""16.Verify "Unable to pair your printer"" page pops up"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """17.Verify Please try the following before attempting to connect to printer again. Text"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Please_Try_The_Following_Before_Attempting_Again_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""""18.Power on the printer Manually"""""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"19.click on Try Again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""20.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""21.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """""22.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"23.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """24.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """"25.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
# #         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
# #                     exec_time)
# #         stepId += 1

#         """26.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28.Verify Connecting to Cloud Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"30.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)
#
# # ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_45660_SemiAuto():
#     """"Search the essids when the printer is offline"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check the printer can be paired successfully.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Printer Connected Text.'],
#         18: [18, 'Verify Searching for Wifi network text is displaying.'],
#         19: [19, 'Verify Connect Wi-fi Network Text.'],
#         20: [20, 'Turn OFF The Printer Manually.'],
#         21: [21, 'Select Enter Network Manually Option.'],
#         22: [22, 'Enter an ESSID and click join button, (Need to enter the pw if the essids with pw.'],
#         23: [23, 'click on connect button on connect wifi network screen.'],
#         24: [24, 'Verify "Unable to pair your printer"" page pops up.'],
#         25: [25, 'Power on the printer Manually.'],
#         26: [26, 'click on Try Again button.'],
#         27: [27, 'Select Enter Network Manually Option.'],
#         28: [28, 'Enter an ESSID and click join button, (Need to enter the pw if the essids with pw).'],
#         29: [29, 'click on connect button on connect wifi network screen.'],
#         30: [30, 'Verify Connecting to Cloud Text.'],
#         31: [31, 'verify need the printer Setup Complete text.'],
#         32: [32, 'click on finish setup button.'],
#         33: [33, 'click home tab.'],
#         34: [34, 'Stop the app.']
#
#     }
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """13.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """19.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Turn OFF The Printer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.Select Enter Network Manually Option"""
#         start_time = time.time()
#         add_a_printer_screen.click_Enter_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""22.Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Network_ESSID()
#         add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""24.Verify "Unable to pair your printer"" page pops up"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""25.Power on the printer Manually"""""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on Try Again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.Select Enter Network Manually Option"""
#         start_time = time.time()
#         add_a_printer_screen.click_Enter_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""28.Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Network_ESSID()
#         add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """30.Verify Connecting to Cloud Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"32.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)

# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_45662_SemiAuto():
#     """"set printer open Essid when the printer change to offline, and retry"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check the printer can be paired successfully.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Printer Connected Text.'],
#         18: [18, 'Verify Searching for Wifi network text is displaying.'],
#         19: [19, 'Verify Connect Wi-fi Network Text.'],
#         20: [20, 'Turn OFF The Printer Manually.'],
#         21: [21, 'click previous network.'],
#         22: [22, 'click on enter password.'],
#         23: [23, 'click on connect button on connect wifi network screen.'],
#         24: [24, 'Verify "Unable to pair your printer"" page pops up.'],
#         25: [25, 'Power on the printer Manually.'],
#         26: [26, 'click on Try Again button.'],
#         27: [27, 'click previous network.'],
#         28: [28, 'click on enter password.'],
#         29: [29, 'click on connect button on connect wifi network screen.'],
#         30: [30, 'Verify Connecting to Cloud Text.'],
#         31: [31, 'verify need the printer Setup Complete text.'],
#         32: [32, 'click on finish setup button.'],
#         33: [33, 'click home tab.'],
#         34: [34, 'Stop the app.']
#
#     }
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                             exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """13.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """19.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Turn OFF The Printer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """22.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""24.Verify "Unable to pair your printer"" page pops up"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""25.Power on the printer Manually"""""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on Try Again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """30.Verify Connecting to Cloud Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"32.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)

# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_45663_SemiAuto():
#     """"set printer wpa psk Essid manually when the printer change to offline, and go to Help"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check the printer can be paired successfully.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Printer Connected Text.'],
#         18: [18, 'Verify Searching for Wifi network text is displaying.'],
#         19: [19, 'Verify Connect Wi-fi Network Text.'],
#         20: [20, 'Turn OFF The Printer Manually.'],
#         21: [21, 'Select Enter Network Manually Option.'],
#         22: [22, 'Enter an ESSID and click join button, Need to enter the pw if the essids with pw.'],
#         23: [23, 'click on connect button on connect wifi network screen.'],
#         24: [24, 'Verify Unable to pair your printer page pops up.'],
#         25: [25, 'Power on the printer Manually.'],
#         26: [26, 'click on Try Again button.'],
#         27: [27, 'Select Enter Network Manually Option.'],
#         28: [28, 'Enter an ESSID and click join button, Need to enter the pw if the essids with pw.'],
#         29: [29, 'click on connect button on connect wifi network screen.'],
#         30: [30, 'Verify Connecting to Cloud Text.'],
#         31: [31, 'verify need the printer Setup Complete text.'],
#         32: [32, 'click on finish setup button.'],
#         33: [33, 'click on home tab.'],
#         34: [34, 'Stop the app.']
#
#     }
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """13.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """19.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Turn OFF The Printer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_OFF_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.Select Enter Network Manually Option"""
#         start_time = time.time()
#         add_a_printer_screen.click_Enter_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""22.Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Network_ESSID()
#         add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""24.Verify "Unable to pair your printer"" page pops up"""''
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""25.Power on the printer Manually"""""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on Try Again button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.Select Enter Network Manually Option"""
#         start_time = time.time()
#         add_a_printer_screen.click_Enter_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""28.Enter an ESSID and click join button, (Need to enter the pw if the essids with pw)"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Network_ESSID()
#         add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """30.Verify Connecting to Cloud Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"32.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)


# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_45665():
#     """"Check the left top corner button of each page work during adding a moneybadger."""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'click on the close icon.'],
#         7: [7, 'Verify Exit Printer Setup Popup.'],
#         8: [8, 'Click on Cancel Button.'],
#         9: [9, 'Verify It will stay on Setup Your Printer Screen.'],
#         10: [10, 'click on the close icon.'],
#         11: [11, 'Click on Exit Button.'],
#         12: [12, 'Check the slide left page appear.'],
#         13: [13, 'click the button Add a Printer.'],
#         14: [14, 'click on start button.'],
#         15: [15, 'Accept the popup.'],
#         16: [16, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         17: [17, 'click on Next Button.'],
#         18: [18, 'Verify Searching For your Printer Text.'],
#         19: [19, 'Verify Select your Printer Text.'],
#         20: [20, 'click on Close icon on Select Your Printer page.'],
#         21: [21, 'Click on Exit Button.'],
#         22: [22, 'Verify Select your Printer Text.'],
#         23: [23, 'Select the Printer.'],
#         24: [24, 'Click on Next Button.'],
#         25: [25, 'Check the printer can be paired successfully.'],
#         26: [26, 'Verify Connecting to printer Text.'],
#         27: [27, 'Verify Printer Connected Text.'],
#         28: [28, 'Verify Searching for Wifi network text is displaying.'],
#         29: [29, 'Verify Connect Wi-fi Network Text.'],
#         30: [30, 'click on Close icon on Select Your Printer page.'],
#         31: [31, 'Click on Exit Button.'],
#         32: [32, 'Check it would go to the page Lets set up your printer.'],
#         33: [33, 'click on the close icon.'],
#         34: [34, 'Click on Exit Button.'],
#         35: [35, 'Check the slide left page appear.'],
#         36: [36, 'click the button Add a Printer.'],
#         37: [37, 'click on start button.'],
#         38: [38, 'Accept the popup.'],
#         39: [39, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         40: [40, 'click on Next Button.'],
#         41: [41, 'Verify Searching For your Printer Text.'],
#         42: [42, 'Verify Select your Printer Text.'],
#         43: [43, 'click on Close icon on Select Your Printer page.'],
#         44: [44, 'Click on Exit Button.'],
#         45: [45, 'Verify Select your Printer Text.'],
#         46: [46, 'Select the Printer.'],
#         47: [47, 'Click on Next Button.'],
#         48: [48, 'Verify Connecting to printer Text.'],
#         49: [49, 'Verify Printer Connected Text.'],
#         50: [50, 'Verify Searching for Wifi network text is displaying.'],
#         51: [51, 'Verify there is no close icon.'],
#         52: [52, 'Stop the app.']
#
#
#     }
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#     stepId = 1
#     try:
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"6.click on the close icon"""
#         start_time = time.time()
#         add_a_printer_screen.click_Close_Icon()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"7.Verify Exit Printer Setup Popup"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Exit_Printer_Setup_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8.Click on Cancel Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Cancel_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9.Verify It will stay on Setup Your Printer Screen"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.click on the close icon"""
#         start_time = time.time()
#         add_a_printer_screen.click_Close_Icon()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """12.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.click on start button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"15.Accept the popup"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.click on Close icon on Select Your Printer page"""""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#
#         """"22.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """23.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"24.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""25.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""26.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""27.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"28.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()x
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """29.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""30.click on Close icon on Select Your Printer page"""""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """32.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.click on the close icon"""
#         start_time = time.time()
#         add_a_printer_screen.click_Close_Icon()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"34.Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """35.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"36. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"37.click on start button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"38.Accept the popup"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"39.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""40.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"41.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"42.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""43.click on Close icon on Select Your Printer page"""""
#         start_time = time.time()
#         add_a_printer_screen.click_On_Close_Icon_On_Select_Your_Printer_Page()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"44.Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"45.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """46.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"47.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""48.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""49.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"50.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """51.Verify there is no close icon"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Close_Icon_Is_Not_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         raise Exception(str(e))
#
#     finally:
#         exec_time = (time.time() - start_time_main) / 60
#         end_main(execID, leftId[test_case_id], exec_time)

# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Addprinter_TestcaseID_45670_SemiAuto():
    """"using the phone B to pair the bluetooth Moneybadger, and don't quit the adding printer process wizard, then using the phone A to discover."""
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open the app and login the account to go to the overview page.'],
        2: [2, 'Prepare two production users without adding any printer and sign in phone A and B" Manually.'],
        3: [3, 'Connect to phone A.'],
        4: [4, 'Click the menu button at the left corner.'],
        5: [5, 'Check the slide left page appear.'],
        6: [6, 'click the button Add a Printer.'],
        7: [7, 'Check it would go to the page Lets set up your printer.'],
        8: [8, 'Check the moneybadger picture would appears at that page.'],
        9: [9, 'Click on Start setup button.'],
        10: [10, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
        11: [11, 'click on Next Button.'],
        12: [12, 'Verify Searching For your Printer Text.'],
        13: [13, 'Verify Select your Printer Text.'],
        14: [14, 'Verify All the unprovision moneybadgr would appear at the page.'],
        15: [15, 'Select the Printer.'],
        16: [16, 'Click on Next Button.'],
        17: [17, 'Check the printer can be paired successfully.'],
        18: [18, 'Verify Connecting to printer Text.'],
        19: [19, 'Verify Printer Connected Text.'],
        20: [20, 'Verify Searching for Wifi network text is displaying.'],
        21: [21, 'Verify Connect Wi-fi Network Text.'],
        22: [22, 'Use phone B, click the hamburger Icon and click on Add a Printer, click Start button Manually.'],
        23: [23, 'Navigate till the Printer Discovery page Manually.'],
        24: [24, 'Check the the target printer is not displayed on the Select your printer page.'],
        25: [25, 'Stop the app.']

    }
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])
    stepId = 1
    try:
        """"1.Open the app and login the account to go to the overview page."""""
        start_time = time.time()
        common_method.tearDown()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""2.Prepare two production users without adding any printer and sign in phone A and B" Manually"""
        start_time = time.time()
        common_method.Show_popup_To_SignIn_PhoneA_And_B_Without_Printer_Manually()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"3.Connect to phone A"""
        start_time = time.time()
        common_method.Show_popup_To_Connect_To_PhoneA_Manually()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """4. Click the menu button at the left corner"""
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """5.Check the slide left page appear"""""
        start_time = time.time()
        add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"6. click the button 'Add a Printer'"""
        start_time = time.time()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """7.Check it would go to the page "Let's set up your printer"""
        start_time = time.time()
        add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""8.Check the moneybadger picture would appears at that page."""
        start_time = time.time()
        add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """9.Click on Start setup button"""
        start_time = time.time()
        add_a_printer_screen.click_Start_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"10.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""11.click on Next Button"""""
        start_time = time.time()
        add_a_printer_screen.click_Next_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"12.Verify Searching For your Printer Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Searching_for_your_printer_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"13.Verify Select your Printer Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Select_your_printer_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"14.Verify All the unprovision moneybadgr would appear at the page """
        start_time = time.time()
        add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """15.Select the Printer"""
        start_time = time.time()
        add_a_printer_screen.Click_The_Printer_Name_To_Select()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"16.Click on Next Button"""
        start_time = time.time()
        add_a_printer_screen.click_Next_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""17.Check the printer can be paired successfully"""
        start_time = time.time()
        add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup1()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2()
        sleep(5)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""18.Verify Connecting to printer Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Connecting_To_Printer_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""19.Verify Printer Connected Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Printer_Connected_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"20.Verify Searching for Wifi network text is displaying"""
        start_time = time.time()
        add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """21.Verify Connect Wi-fi Network Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""22.Use phone B, click the hamburger Icon and click on 'Add a Printer', click Start button Manually"""
        start_time = time.time()
        common_method.Show_popup_To_Connect_To_PhoneB_Manually()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """23.Navigate till the 'Printer Discovery' page Manually"""""
        start_time = time.time()
        common_method.Show_popup_To_Navigate_Till_PrinterDiscovery_Page_Manually()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""24.Check the the target printer is not displayed on the "Select your printer" page"""
        start_time = time.time()
        common_method.Show_popup_To_Verify_Target_Printer_Is_Not_Displaying_On_Select_Your_PrinterPage_Manually()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """stop the app"""
        start_time = time.time()
        common_method.Stop_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)

    # #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Addprinter_TestcaseID_45678_SemiAuto():
    """"retrieve moneybadger when no online moenybadgers at your area, then open one, retrieve again"""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""2. Verify there is no any moneybadger in your area Manually"""
    common_method.Show_popup_To_Verify_There_Is_No_Moneybadger_In_Your_Area_Manually()
    """2. Click the menu button at the left corner"""
    login_page.click_Menu_HamburgerICN()
    """3.Check the slide left page appear"""""
    add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
    """"3. click the button 'Add a Printer'"""
    add_a_printer_screen.click_Add_A_Printer()
    """Check it would go to the page "Let's set up your printer"""
    add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
    """""Check the moneybadger picture would appears at that page."""
    add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
    """Click on Start setup button"""
    add_a_printer_screen.click_Start_Button()
    """"Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
    add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
    """""click on Next Button"""""
    add_a_printer_screen.click_Next_Button()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """""5. Verify There should be no printer found and app will go to "No printers found" page"""
    add_a_printer_screen.Verify_No_Printers_Found_Text()
    """"Verify "Please make sure your printer is on and Bluetooth Text"""
    add_a_printer_screen.Verify_Your_Printer_is_ON_And_Bluetooth_Is_Enabled_Text()
    """"You can hold the reset button on the back of your printer for 5 seconds to reset the printer. Manually"""""
    common_method.Show_popup_To_Reset_The_Printer_Manually()
    """""Power on a moneybadger printer Manually"""""
    common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
    """ Click on "Try Again" button."""""
    add_a_printer_screen.click_Try_Again()
    """"Verify Searching For your Printer Text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"Verify Select your Printer Text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"Verify All the unprovision moneybadgr would appear at the page """
    add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
    """Select the Printer"""
    add_a_printer_screen.Click_The_Printer_Name_To_Select()
    """"Click on Next Button"""
    add_a_printer_screen.click_Next_Button()
    """""Check the printer can be paired successfully"""
    add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
    add_a_printer_screen.click_Bluetooth_pairing_Popup1()
    add_a_printer_screen.click_Bluetooth_pairing_Popup2()
    sleep(5)
    """""Verify Connecting to printer Text"""
    add_a_printer_screen.Verify_Connecting_To_Printer_Text()
    """""Verify Printer Connected Text"""
    add_a_printer_screen.Verify_Printer_Connected_Text()
    """"Verify Searching for Wifi network text is displaying"""
    add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click previous network """
    add_a_printer_screen.click_NESTWIFI_NETWORK()
    """click on enter password"""
    add_a_printer_screen.Enter_Password_Field()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Button_ON_Join_Network()
    """"verify need the printer Setup Complete text"""
    add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Button()
    """"click home tab"""
    add_a_printer_screen.click_Home_Tab()
    """stop the app"""
    common_method.Stop_The_App()


#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
