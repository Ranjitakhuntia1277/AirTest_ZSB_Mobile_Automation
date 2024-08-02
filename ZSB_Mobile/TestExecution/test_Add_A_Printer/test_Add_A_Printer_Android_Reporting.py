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
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
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
registration_page = Registration_Screen(poco)

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# execID = 0
# leftId = {"0": "7"}


def test_Addprinter_TestcaseID_45656():
    """"Adding the moneybadger while the mobile devices bluetooth is disabled"""
    pass

    test_steps = {
        1: [1, 'Open the app and login the account to go to the overview page.'],
        2: [2, 'Click the menu button at the left corner.'],
        3: [3, ' Check the slide left page appear.'],
        4: [4, 'Disable the Bluetooth.'],
        5: [5, 'click the button Add a Printer.'],
        6: [6, 'Verify Turn on bluetooth prompt message.'],
        7: [7,
            'click on Cancel button."'],
        8: [8, 'Check the Lets set up your printer page will dismiss, and it will back to the slide left page.'],
        9: [9,
            'click the button Add a Printer button again.'],
        10: [10, 'Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879.'],
        11: [11,
             'click on Cancel button.'],
        12: [12,
             ' Turn on the Bluetooth.'],
        13: [13,
             ' click the button Add a Printer button again.'],
        14: [14, 'Check it would go to the page Lets set up your printer.'],

        15: [15, 'Disable the Bluetooth.'],
        16: [16, 'Check the moneybadger picture would appears at that page'],
        17: [17, 'click start button'],
        18: [18, 'Accept the popup'],
        19: [19, 'click on next button'],
        20: [20, 'Unable to find printer(s)" page'],
        21: [21, 'Turn on the Bluetooth'],
        22: [22, 'Check this time printer can connect to Wifi successfully'],
        23: [23, 'Follow the prompt to proceed the adding printer process, check the printer can be added successfully'],
        24: [24, 'Stop the app.']
    }
    start_time_main = time.time()
    stepId = 1
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_main(execID, leftId[test_case_id])
    try:

        # start_time = time.time()
        # """"1.Open the app and login the account to go to the overview page."""""
        # common_method.tearDown()
        # common_method.Clear_App()
        # common_method.Start_The_App()
        # login_page.click_LoginAllow_Popup()
        # login_page.click_Allow_ZSB_Series_Popup()
        # login_page.click_loginBtn()
        # login_page.click_LoginAllow_Popup()
        # login_page.click_Allow_ZSB_Series_Popup()
        # login_page.click_Loginwith_Google()
        # login_page.Loginwith_Added_Email_Id()
        # exec_time = (time.time() - start_time) / 60
        # insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
        #             exec_time)
        # stepId += 1

        # """2. Click the menu button at the left corner"""
        # start_time = time.time()
        # login_page.click_Menu_HamburgerICN()
        # exec_time = (time.time() - start_time) / 60
        # insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
        #             exec_time)
        # stepId += 1
        #
        # """3.Check the slide left page appear"""""
        # start_time = time.time()
        # add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
        # exec_time = (time.time() - start_time) / 60
        # insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
        #             exec_time)
        # stepId += 1

        """"Disable the Bluetooth"""
        start_time = time.time()
        app_settings_page.Disable_Bluetooth()
        sleep(4)
        """"click on Allow button on Bluetooth disable & enable popup"""
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"3. click the button 'Add a Printer'"""
        start_time = time.time()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"can not verify all these steps as these all are coming behind the popup"""
        ### """Check it would go to the page "Let's set up your printer"""
        ### add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
        #### """""Check the moneybadger picture would appears at that page."""
        #### add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
        #### """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
        """"Verify Turn on bluetooth prompt message"""""
        start_time = time.time()
        add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click on Cancel button"""
        start_time = time.time()
        add_a_printer_screen.click_On_Cancel_Btn()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Check the "Let's set up your printer" page will dismiss, and it will back to the slide left page"""
        start_time = time.time()
        add_a_printer_screen.Verify_Slideleft_Page_Is_Present()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click the button 'Add a Printer' button again"""
        start_time = time.time()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Verify Turn on Bluetooth to Allow "ZSB Printer App" to Connect" prompt message--SMBM-1879"""
        start_time = time.time()
        add_a_printer_screen.Verify_TurnOn_Bluetooth_PromptMessage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click on Cancel button"""
        start_time = time.time()
        add_a_printer_screen.click_On_Cancel_Btn()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Turn on the Bluetooth"""
        start_time = time.time()
        app_settings_page.Enable_Bluetooth()
        sleep(4)
        """"click on Allow button on Bluetooth disable & enable popup"""
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click the button 'Add a Printer' button again"""
        start_time = time.time()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Check it would go to the page "Let's set up your printer"""
        start_time = time.time()
        add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Disable the Bluetooth"""
        start_time = time.time()
        app_settings_page.Disable_Bluetooth()
        sleep(4)
        add_a_printer_screen.click_Add_A_Printer()
        """"click on Allow button on Bluetooth disable & enable popup"""
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""Check the moneybadger picture would appears at that page."""
        start_time = time.time()
        add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """click start button"""
        start_time = time.time()
        add_a_printer_screen.click_Start_Button()
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Accept the popup"""
        start_time = time.time()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""click on next button"""
        start_time = time.time()
        add_a_printer_screen.Click_Next_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Unable to find printer(s)" page"""
        start_time = time.time()
        add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Turn on the Bluetooth"""
        start_time = time.time()
        add_a_printer_screen.enable_bluetooth()
        sleep(4)
        add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """click on allow for enable bluetooth"""
        start_time = time.time()
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Unable to find printer(s)" page"""
        start_time = time.time()
        add_a_printer_screen.Verify_Unable_To_Find_Printers_Text_Is_Displaying()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click search again button"""
        start_time = time.time()
        add_a_printer_screen.click_Search_Again_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""Verify Searching Your printer text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Searching_for_your_printer_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Verify Select your printer text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Select_your_printer_Text_For_Add_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""Select the Target Printer"""
        start_time = time.time()
        add_a_printer_screen.Select_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Select button"""
        add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """""Check the printer can be paired successfully"""
        start_time = time.time()
        add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup1()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2()
        sleep(15)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Verify Searching for Wifi network text is displaying"""
        start_time = time.time()
        add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Turn off Bluetooth"""
        start_time = time.time()
        app_settings_page.Disable_Bluetooth()
        sleep(5)
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        """Verify Unable to connect to printer popup is displaying"""
        start_time = time.time()
        add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"Turn on Bluetooth"""
        start_time = time.time()
        app_settings_page.Enable_Bluetooth()
        sleep(5)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """click on Allow button"""
        start_time = time.time()
        add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click on try again"""
        start_time = time.time()
        add_a_printer_screen.click_Try_Again()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Verify Connect Wi-fi Network Text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click previous network """
        start_time = time.time()
        add_a_printer_screen.click_NESTWIFI_NETWORK()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """click on enter password"""
        start_time = time.time()
        add_a_printer_screen.Enter_Password_Field()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click on connect button on connect wifi network screen"""
        start_time = time.time()
        add_a_printer_screen.click_Connect_Button_ON_Join_Network()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"verify need the printer Setup Complete text"""
        start_time = time.time()
        add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click on finish setup button"""
        start_time = time.time()
        add_a_printer_screen.click_Finish_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """"click home tab"""
        start_time = time.time()
        add_a_printer_screen.click_Home_Tab()
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

# def test_Addprinter_TestcaseID_45670_SemiAuto():
#     """"using the phone B to pair the bluetooth Moneybadger, and don't quit the adding printer process wizard, then using the phone A to discover."""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Prepare two production users without adding any printer and sign in phone A and B" Manually.'],
#         3: [3, 'Connect to phone A.'],
#         4: [4, 'Click the menu button at the left corner.'],
#         5: [5, 'Check the slide left page appear.'],
#         6: [6, 'click the button Add a Printer.'],
#         7: [7, 'Check it would go to the page Lets set up your printer.'],
#         8: [8, 'Check the moneybadger picture would appears at that page.'],
#         9: [9, 'Click on Start setup button.'],
#         10: [10, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         11: [11, 'click on Next Button.'],
#         12: [12, 'Verify Searching For your Printer Text.'],
#         13: [13, 'Verify Select your Printer Text.'],
#         14: [14, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         15: [15, 'Select the Printer.'],
#         16: [16, 'Click on Next Button.'],
#         17: [17, 'Check the printer can be paired successfully.'],
#         18: [18, 'Verify Connecting to printer Text.'],
#         19: [19, 'Verify Printer Connected Text.'],
#         20: [20, 'Verify Searching for Wifi network text is displaying.'],
#         21: [21, 'Verify Connect Wi-fi Network Text.'],
#         22: [22, 'Use phone B, click the hamburger Icon and click on Add a Printer, click Start button Manually.'],
#         23: [23, 'Navigate till the Printer Discovery page Manually.'],
#         24: [24, 'Check the the target printer is not displayed on the Select your printer page.'],
#         25: [25, 'Stop the app.']
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
#         """""2.Prepare two production users without adding any printer and sign in phone A and B" Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_SignIn_PhoneA_And_B_Without_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"3.Connect to phone A"""
#         start_time = time.time()
#         common_method.Show_popup_To_Connect_To_PhoneA_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """4. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"6. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """7.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""8.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """9.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""11.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """15.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.Check the printer can be paired successfully"""
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
#         """""18.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"20.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """21.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""22.Use phone B, click the hamburger Icon and click on 'Add a Printer', click Start button Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Connect_To_PhoneB_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """23.Navigate till the 'Printer Discovery' page Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Navigate_Till_PrinterDiscovery_Page_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""24.Check the the target printer is not displayed on the "Select your printer" page"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Target_Printer_Is_Not_Displaying_On_Select_Your_PrinterPage_Manually()
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

# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_45678_SemiAuto():
#     """"retrieve moneybadger when no online moenybadgers at your area, then open one, retrieve again"""
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Verify there is no any moneybadger in your area Manually.'],
#         3: [3, 'Click the menu button at the left corner.'],
#         4: [4, 'Check the slide left page appear.'],
#         5: [5, 'click the button Add a Printer.'],
#         6: [6, 'Check it would go to the page Lets set up your printer.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Verify There should be no printer found and app will go to "No printers found" page.'],
#         14: [14, 'Verify "Please make sure your printer is on and Bluetooth Text.'],
#         15: [15, 'You can hold the reset button on the back of your printer for 5 seconds to reset the printer. Manually.'],
#         16: [16, 'Power on a moneybadger printer Manually.'],
#         17: [17, 'Click on Try Again button'],
#         18: [18, 'Verify Searching For your Printer Text.'],
#         19: [19, 'Verify Select your Printer Text.'],
#         20: [20, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         21: [21, 'Select the Printer.'],
#         22: [22, 'Click on Next Button.'],
#         23: [23, 'Check the printer can be paired successfully.'],
#         24: [24, 'Verify Connecting to printer Text.'],
#         25: [25, 'Verify Printer Connected Text.'],
#         26: [26, 'Verify Searching for Wifi network text is displaying.'],
#         27: [27, 'Verify Connect Wi-fi Network Text.'],
#         28: [28, 'click previous network.'],
#         29: [29, 'click on enter password.'],
#         30: [30, 'click on connect button on connect wifi network screen.'],
#         31: [31, 'verify need the printer Setup Complete text.'],
#         32: [32, 'click on finish setup button.'],
#         33: [33, 'click home tab.'],
#         34: [34, 'stop the app.']
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
#         """""2. Verify there is no any moneybadger in your area Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_There_Is_No_Moneybadger_In_Your_Area_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """4.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"5. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """6.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""13. Verify There should be no printer found and app will go to "No printers found" page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_No_Printers_Found_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14.Verify "Please make sure your printer is on and Bluetooth Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Your_Printer_is_ON_And_Bluetooth_Is_Enabled_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"15.You can hold the reset button on the back of your printer for 5 seconds to reset the printer. Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Reset_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Power on a moneybadger printer Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Turn_ON_The_Printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """ 17.Click on "Try Again" button."""""
#         start_time = time.time()
#         add_a_printer_screen.click_Try_Again()
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
#         """"20.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """21.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""23.Check the printer can be paired successfully"""
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
#         """""24.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""25.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """27.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"28.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """29.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"30.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
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
#         """34.stop the app"""
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
#

#     ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_45679_SemiAuto():
#     """"set wrong password of the PSK WPA Essid to printer by choosing it, then click 'Cancel'"""
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
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Check the printer can be paired successfully.'],
#         15: [15, 'Verify Connecting to printer Text.'],
#         16: [16, 'Verify Printer Connected Text.'],
#         17: [17, 'Verify Searching for Wifi network text is displaying.'],
#         18: [18, 'Verify Connect Wi-fi Network Text.'],
#         19: [19, 'Verify no duplicated Essids, all Essid is unique and only wpa psk and open securiy Essids in it Manually.'],
#         20: [20, 'choose the Essid which next to the lock icon.'],
#         21: [21, 'Check it would pop up the dialog "Enter Network Passwords.'],
#         22: [22, 'enter the incorrect passwod, and click "Submit.'],
#         23: [23, 'Check the page "Wifi Setup" is spinning.'],
#         24: [24, 'Check wait a few seconds, and the dialog Fail to Connect with incorrect passwod message and retry, help button.'],
#         25: [25, 'Click the X button at left upper corner.'],
#         26: [26, 'click on Exit on Exit Printer setup popup.'],
#         27: [27, 'Check the slide left page appear.'],
#         28: [28, 'click the button Add a Printer.'],
#         29: [29, 'click on start button.'],
#         30: [30, 'Accept the popup.'],
#         31: [31, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         32: [32, 'click on Next Button.'],
#         33: [33, 'Verify Searching For your Printer Text.'],
#         34: [34, 'Verify Select your Printer Text.'],
#         35: [35, 'Verify All the unprovision moneybadgr would appear at the page.'],
#         36: [36, 'Select the Printer.'],
#         37: [37, 'Click on Next Button.'],
#         38: [38, 'Check the printer can be paired successfully.'],
#         39: [39, 'Verify Connecting to printer Text.'],
#         40: [40, 'Verify Printer Connected Text.'],
#         41: [41, 'Verify Searching for Wifi network text is displaying.'],
#         42: [42, 'Verify Connect Wi-fi Network Text.'],
#         43: [43, 'click previous network.'],
#         44: [44, 'click on enter password.'],
#         45: [45, 'click on connect button on connect wifi network screen.'],
#         46: [46, 'verify need the printer Setup Complete text.'],
#         47: [47, 'click on finish setup button.'],
#         48: [48, 'click home tab.'],
#         49: [49, 'stop the app.']
#     }
#
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
#         """""14.Check the printer can be paired successfully"""
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
#         """""15.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """18.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19.Verify no duplicated Essids, all Essid is unique and only wpa psk and open securiy Essids in it Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_No_Duplicat_Essids_And_Other_Details_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """20. choose the Essid which next to the lock icon."""
#         start_time = time.time()
#         add_a_printer_screen.click_The_ESSID_Next_To_Lock_Icon()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.Check it would pop up the dialog "Enter Network Passwords"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Enter_Network_Passwords_Text_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22. enter the incorrect passwod, and click "Submit"""""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Longe_Wrong_Password_In_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23.Check the page "Wifi Setup" is spinning."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """24.Check wait a few seconds, and the dialog 'Fail to Connect' with incorrect passwod message and 'retry', 'help' button"""""""""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_Printer_To_Wifi_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""25. Click the 'X' button at left upper corner"""
#         start_time = time.time()
#         add_a_printer_screen.click_Close_Icon()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """26.click on Exit on Exit Printer setup popup"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """Check it would go to the page 'Continue printer setup' in Connect to WIfi step"""
#         """"9. click Next again and choose the Essid again, and input the correct password for it and submit"""
#         """10. check the wifi is connected and the printer is finished setup and added to account successfully."""
#         '''''''''''''''''''''''''''It is going to home page so could not automated all the above steps'''''
#
#         """27.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"28. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.click on start button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"30.Accept the popup"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"31.Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""32.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"34.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"35.Verify All the unprovision moneybadgr would appear at the page """
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """36.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"37.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#
#         """""38.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""39.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""40.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"41.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """42.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"43.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """44.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"45.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"46.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"47.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"48.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """49.stop the app"""
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

# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_45682():
#     """"connect printer with PSK WPA Essid manually, then cancel'"""
#     pass
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
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Check the printer can be paired successfully.'],
#         15: [15, 'Verify Connecting to printer Text.'],
#         16: [16, 'Verify Printer Connected Text.'],
#         17: [17, 'Verify Searching for Wifi network text is displaying'],
#         18: [18, 'Verify Connect Wi-fi Network Text.'],
#         19: [19, 'Check the page labelled  Connect Wi-Fi network pops up showing the wifi-to which device is connected.'],
#         20: [20, 'Select a different one and Check it would pop upSearching for Wifi Networks page.'],
#         21: [21, 'Click "Enter Network manually.'],
#         22: [22, 'Enter an ESSID password.'],
#         23: [23, 'Enter Password.'],
#         24: [24, 'click on cancel button on connect wifi network screen.'],
#         25: [25, 'Verify it would still at the Select your Wifi Network page.'],
#         26: [26, 'Stop the App.']
#
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#
#         stepId += 1
#
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """12.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"13.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""14.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""15.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""16.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"17.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """18.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""""19. Check the page labelled  Connect Wi-Fi network pops up showing the wifi-to which device is connected"""""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Added_Wifi_which_Is_Connected()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"20.Select a different one and Check it would pop upSearching for Wifi Networks page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """21.Click "Enter Network manually"""
#         start_time = time.time()
#         add_a_printer_screen.click_Enter_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""22.Enter an ESSID password"""""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Network_ESSID()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"23.Enter Password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field_On_Nwtwork_Manually_Filed()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"24.click on cancel button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """25.Verify it would still at the Select your Wifi Network page"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"26.Stop the App"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
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
#     # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_47714_SemiAuto():
#     """"Add printer BT pair Timeout : check when printer not in pair mode, check pair time"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         9: [9, 'add_a_printer_screen.click_Next_Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Start the timer on your device after clicking on next button.'],
#         15: [15, 'Check the printer can be paired successfully.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Unable to pair your printer.'],
#         18: [18, 'Stop the Timer Manually.'],
#         19: [19, 'Verify Unable to pair your printer.'],
#         20: [20, 'Check it would take less then 45 seconds to pair printer Manually.'],
#         21: [21, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#
#         """2. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """3.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"4. click the button 'Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """5.Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""6.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """7.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""9.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"10.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"11.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """12.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"13.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"""""""14.Start the timer on your device after clicking on next button"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Start_The_Timer_On_Your_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""15.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """""16.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"17.Verify Unable to pair your printer"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"18.Stop the Timer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Stop_The_Timer_On_Your_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"19.Verify Unable to pair your printer"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"20.Check it would take less then 45 seconds to pair printer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_It_Should_Take_less_than_45_Seconds_to_pair_printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#         stepId += 1
#
#         """"21.Stop the App"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                             exec_time)
#
#         stepId += 1
#
#     except Exception as e:
#                 insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#                 insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#                 insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#                 raise Exception(str(e))
#
#     finally:
#                 exec_time = (time.time() - start_time_main) / 60
#                 end_main(execID, leftId[test_case_id], exec_time)

#     ######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_47715_SemiAuto():
#     """"Add printer BT pair Timeout : check cancel Bluetooth Pairing request, check pair time"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page "Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Press target printer 3-5 second to enter pairing mode(blue light) Manually.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check it would popup bluetooth pairing mode and click on cancel button.'],
#         16: [16, 'Start the timer on your device after clicking on next button.'],
#         17: [17, 'Verify Connecting to printer Text.'],
#         18: [18, 'Verify Unable to pair your printer.'],
#         19: [19, 'Stop the Timer Manually.'],
#         20: [20, 'Verify Unable to pair your printer.'],
#         21: [21, 'Check it would take less then 45 seconds to pair printer Manually.'],
#         22: [22, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """""12. Press target printer 3-5 second to enter pairing mode(blue light) Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Make_The_Printer_To_Pairing_Mode_Manually()
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
#         """15.Check it would popup bluetooth pairing mode and click on cancel button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
#         add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup_If_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"""""""16.Start the timer on your device after clicking on next button"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Start_The_Timer_On_Your_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.Verify Unable to pair your printer"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19.Stop the Timer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Stop_The_Timer_On_Your_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"20.Verify Unable to pair your printer"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Pair_Your_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.Check it would take less then 45 seconds to pair printer Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_It_Should_Take_less_than_45_Seconds_to_pair_printer_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22.Stop the App"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#                 insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#                 insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#                 insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#                 raise Exception(str(e))
#
#     finally:
#                 exec_time = (time.time() - start_time_main) / 60
#                 end_main(execID, leftId[test_case_id], exec_time)

#     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_48436():
#     """"Verify the Cancel button functionality on "Join Network Page" while connceting to already connected / newly connected network"""
#
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page "Lets set up your printer.'],
#         6: [6, 'Check the moneybadger picture would appears at that page.'],
#         7: [7, 'Click on Start setup button.'],
#         8: [8, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         9: [9, 'click on Next Button.'],
#         10: [10, 'Verify Searching For your Printer Text.'],
#         11: [11, 'Verify Select your Printer Text.'],
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Check the printer can be paired successfully.'],
#         15: [15, 'Verify Connecting to printer Text.'],
#         16: [16, 'Verify Printer Connected Text.'],
#         17: [17, 'Verify Searching for Wifi network text is displaying.'],
#         18: [18, 'Verify Connect Wi-fi Network Text.'],
#         19: [19, 'click previous network.'],
#         20: [20, 'In The "Join Network" page, click a password that is incompatible from length point of view.'],
#         21: [21, 'The user should be shown message "Password should contain between 8 and 63 characters.'],
#         22: [22, 'click on cancel button on connect wifi network screen.'],
#         23: [23, 'The user should be navigated back to previous screen.'],
#         24: [24, 'In The Join Network page, click a password that is incompatible from length point of view.'],
#         25: [25, 'The user should be shown message "Password should contain between 8 and 63 characters.'],
#         26: [26, 'click on cancel button on connect wifi network screen.'],
#         27: [27, 'The user should be navigated back to previous screen.'],
#         28: [28, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """""14.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """18.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """20. In The "Join Network" page, click a password that is incompatible from length point of view"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Wrong_Password_In_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21. The user should be shown message "Password should contain between 8 and 63 characters"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Password_Should_Contain_Between_Message()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22.click on cancel button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23. The user should be navigated back to previous screen"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """24. In The "Join Network" page, click a password that is incompatible from length point of view"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Wrong_Password_In_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25. The user should be shown message "Password should contain between 8 and 63 characters"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Password_Should_Contain_Between_Message()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on cancel button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27. The user should be navigated back to previous screen"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28.stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#                 insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#                 insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#                 insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#                 raise Exception(str(e))
#
#     finally:
#                 exec_time = (time.time() - start_time_main) / 60
#                 end_main(execID, leftId[test_case_id], exec_time)

# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_48438():
#     """"Verify the timeout scenario when user enters the password and does not Continue"""
#     pass
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
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Verify Connecting to printer Text.'],
#         15: [15, 'Verify Printer Connected Text.'],
#         16: [16, 'Verify Searching for Wifi network text is displaying.'],
#         17: [17, 'Verify Connect Wi-fi Network Text.'],
#         18: [18, 'click previous network.'],
#         19: [19, 'click on enter password.'],
#         20: [20, 'Minimize the app for 3o minutes.'],
#         21: [21, 'Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward.'],
#         22: [22, 'Minimize the app for 3o minutes.'],
#         23: [23, 'Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward.'],
#         24: [24, 'click on the Connect button on Join Network.'],
#         25: [25, 'verify need the printer Setup Complete text.'],
#         26: [26, 'click on finish setup button.'],
#         27: [27, 'click home tab.'],
#         28: [28, 'Stop the App.'],
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
#     try:
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#
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
#         """"4. click the button Add a Printer'"""
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
#         """"8.Verify Lets make sure the printer is in Bluetooth pairing mode Text"""
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
#         """""Check the printer can be paired successfully"""
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""14.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """17.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18.click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """19.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Minimize the app for 3o minutes"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         sleep(1800)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""21.  Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward"""""
#         start_time = time.time()
#         common_method.Start_The_App()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""22.Minimize the app for 3o minutes"""
#         common_method.Stop_The_App()
#         sleep(1800)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""23.  Launch the app after 30 mins . The user should not be auto-logged out and user should be able to proceed forward"""""
#         start_time = time.time()
#         common_method.Start_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"24.click on the Connect button on Join Network"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28.stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#             insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#             insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#             insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#             raise Exception(str(e))
#     finally:
#             exec_time = (time.time() - start_time_main) / 60
#             end_main(execID, leftId[test_case_id], exec_time)
#
# # ############"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_48693():
#     """"Verify the Signal Strength UI for WiFi with Average connectivity"""
#     pass
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
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Check the printer can be paired successfully.'],
#         15: [15, 'Verify Connecting to printer Text.'],
#         16: [16, 'Verify Printer Connected Text.'],
#         17: [17, 'Verify Searching for Wifi network text is displaying.'],
#         18: [18, 'Verify Connect Wi-fi Network Text.'],
#         19: [19, 'Verify the signal Strength UI.'],
#         20: [20, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page Lets set up your printer"""
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
#         """"8.Verify Lets make sure the printer is in Bluetooth pairing mode Text"""
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
#         """""14.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """18.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19.Verify the signal Strength UI"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Signal_Strength_UI()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"Verify the signal Strength UI. The same should be shown in full strength in greyed out
#         This has been removed"""
#
#         """"20.Stop the App"""
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
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_47702_AemiAuto():
#     """"Add printer select network: Check search again to refresh current Wi-Fi list multi times will works fine"""
#     pass
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
#         12: [12, 'Select the Printer.'],
#         13: [13, 'Click on Next Button.'],
#         14: [14, 'Check the printer can be paired successfully.'],
#         15: [15, 'Verify Connecting to printer Text.'],
#         16: [16, 'Verify Printer Connected Text.'],
#         17: [17, 'Verify Searching for Wifi network text is displaying.'],
#         18: [18, 'Verify Connect Wi-fi Network Text.'],
#         19: [19, 'Verify it is displayed the WIFI network which the mobile phone is connected.'],
#         20: [20, 'Verify Discovered Network lists.'],
#         21: [21, 'click on Search Again.'],
#         22: [22, 'Verify Connect Wi-fi Network Text.'],
#         23: [23, 'Verify Known & Discovered networks are still same.'],
#         24: [24, 'shut done one network Manually.'],
#         25: [25, 'click on Search Again.'],
#         26: [26, 'Verify the shut down network not show in list Manually.'],
#         27: [27, 'Open a new network(eg: personal hotspot) Manually.'],
#         28: [28, 'Click search again, check the network refresh success.'],
#         29: [29, 'check the new added network appear in list Manually.'],
#         30: [30, 'Verify Connect Wi-fi Network Text.'],
#         31: [31, 'select A network to connect.'],
#         32: [32, 'click on enter password.'],
#         33: [33, 'click on connect button on connect wifi network screen.'],
#         34: [34, 'verify need the printer Setup Complete text.'],
#         35: [35, 'click on finish setup button.'],
#         36: [36, 'click home tab.'],
#         37: [36, 'stop the app.']
#
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page Lets set up your printer"""
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
#         """"8.Verify Let's make sure the printer is in Bluetooth pairing mode Text."""
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
#         """""14.Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """18.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """19.Verify it is displayed the WIFI network which the mobile phone is connected"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Known_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """20.Verify Discovered Network lists"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Network_Lists()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21.click on Search Again"""
#         start_time = time.time()
#         add_a_printer_screen.click_Search_Again_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """22.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"23.Verify Known & Discovered networks are still same"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Known_Network()
#         add_a_printer_screen.Verify_Network_Lists()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"24. shut done one network Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Shut_Down_One_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25.click on Search Again"""
#         start_time = time.time()
#         add_a_printer_screen.click_Search_Again_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.Verify the shut down network not show in list Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_The_Shut_Down_Network_Not_showing_In_The_List_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""27. Open a new network(eg: personal hotspot) Manually"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Open_A_New_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"28. Click search again, check the network refresh success"""
#         start_time = time.time()
#         add_a_printer_screen.click_Search_Again_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """29.check the new added network appear in list Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_The_New_Added_Network_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """30.Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """31.select A network to connect"""
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """32.click on enter password"""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Password_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"33.click on connect button on connect wifi network screen"""
#         start_time = time.time()
#         add_a_printer_screen.click_Connect_Button_ON_Join_Network()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"34.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"35.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"36.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """37.stop the app"""
#         start_time = time.time()
#         common_method.Stop_The_App()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#     except Exception as e:
#             insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#             insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#             insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#             raise Exception(str(e))
#     finally:
#             exec_time = (time.time() - start_time_main) / 60
#             end_main(execID, leftId[test_case_id], exec_time)
#     #######""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'""""


# def test_Addprinter_TestcaseID_53209_SemiAuto():
#     """"[New Fonts and UI checking]Perform the Add printer process and check all the page/toast font and dialogs and buttons displayed correctly"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Verify the Image & UI with Figma Manually.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check the printer can be paired successfully.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Printer Connected Text.'],
#         18: [18, 'Verify Searching for Wifi network text is displaying.'],
#         19: [19, 'Verify Connecting to Wi-Fi Network page displayed with new fonts and style.'],
#         20: [20, 'Verify Connect Wi-fi Network Text.'],
#         21: [21, 'select A network to connect.'],
#         22: [22, 'click on enter password.'],
#         23: [23, 'click on connect button on connect wifi network screen.'],
#         24: [24, 'verify need the printer Setup Complete text.'],
#         25: [25, 'Verify Printer Setup Complete Font & style Manually.'],
#         26: [26, 'click on finish setup button.'],
#         27: [27, 'click home tab.'],
#         28: [28, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
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
#         """""6.Verify the Image & UI with Figma Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9.Verify Lets make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10. click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
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
#         """""15. Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16. Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17. Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18. Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19. Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """20. Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """21.select A network to connect"""
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
#         """"24.verify need the printer Setup Complete text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25. Verify Printer Setup Complete Font & style Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Printer_Setup_Complete_Font_And_Style_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.click on finish setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Finish_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27.click home tab"""
#         start_time = time.time()
#         add_a_printer_screen.click_Home_Tab()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28.stop the app"""
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
# #     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_53210_SemiAuto():
#     """"[New Fonts and UI checking]Perform the Add printer process and check error message dialog display correct when adding printer,example Firmware update Error, internet access blocked"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Verify the Image & UI with Figma Manually.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Select the Printer.'],
#         14: [14, 'Click on Next Button.'],
#         15: [15, 'Check the printer can be paired successfull.'],
#         16: [16, 'Verify Connecting to printer Text.'],
#         17: [17, 'Verify Printer Connected Text.'],
#         18: [18, 'Verify Searching for Wifi network text is displaying.'],
#         19: [19, 'Verify Connecting to Wi-Fi Network page displayed with new fonts and style.'],
#         20: [20, 'Verify Connect Wi-fi Network Text.'],
#         21: [21, 'Select a Wi-Fi without network, click Connect button.'],
#         22: [22, 'Check Printer registration page displayed with new fonts and style Manually.'],
#         23: [23, 'Check internet access blocked error message would be prompted with new fonts and style.'],
#         24: [24, 'Verify New Fonts & style Manually for Internet Access Blocked Popup Manually.'],
#         25: [25, 'Check Firmware update Error error message would be prompted with new fonts and style Manually.'],
#         26: [26, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page Lets set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Verify the Image & UI with Figma Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7. Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8. Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9. Verify Lets make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10. click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11. Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12. Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """13. Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"14. Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""15. Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""16. Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""17. Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"18. Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"19. Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """20. Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """21. Select a Wi-Fi without network, click Connect button"""
#         """Check Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Select_A_WIFI_Without_Network_And_Chcek_The_Fonts_And_Style_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22. Check Printer registration page displayed with new fonts and style Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_New_Font_And_Style_Of_Registration_Page_Displayed_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """23. Check internet access blocked error message would be prompted with new fonts and style"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Internet_Access_Blocked_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""24.Verify New Fonts & style Manually for Internet Access Blocked Popup Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_NewFonts_And_Style_Of_Internet_Access_Popup_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"" 25. Check Firmware update Error error message would be prompted with new fonts and style Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Firmware_Update_Error_With_NewFonts_And_Style_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.Stop the App"""
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
# # ######""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_53211_SemiAuto():
#     """"[New Fonts and UI checking]Perform the Add printer process and check paired failed page display correct"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Verify the Image & UI with Figma Manually.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Verify The font & Style of Select your Printer page.'],
#         14: [14, 'Select the Printer.'],
#         15: [15, 'Click on Next Button.'],
#         16: [16, 'Verify Bluetooth pairing your printer page with new fonts and style.'],
#         17: [17, 'Click on Cancel button on the bluetooth pairing popup.'],
#         18: [18, 'Verify Unable to pair your printer page pops up.'],
#         19: [19, 'Verify the Unable To Connect to Printer page fonts & Style.'],
#         20: [20, 'Stop the App.']
#
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """3. Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"4. click the button Add a Printer '"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5. Check it would go to the page Lets set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Verify the Image & UI with Figma Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8.Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9.Verify Lets make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13.Verify The font & Style of Select your Printer page"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """14.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"15.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16.Verify Bluetooth pairing your printer page with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """17.Click on Cancel button on the bluetooth pairing popup"""
#         start_time = time.time()
#         add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""18. Verify Unable to pair your printer page pops up"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19. Verify the Unable To Connect to Printer page fonts & Style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"20. Stop the App"""
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
# # #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_53212_SemiAuto():
#     """"[New Fonts and UI checking]Perform the Add printer process and check Unable to connect the printer page display correct when adding a printer searching wifi step with turn off device bluetooth"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Verify the Image & UI with Figma Manually.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Verify The font & Style of Select your Printer page.'],
#         14: [14, 'Select the Printer.'],
#         15: [15, 'Click on Next Button.'],
#         16: [16, 'Verify Bluetooth pairing your printer page with new fonts and style.'],
#         17: [17, 'Click on Next Button.'],
#         18: [18, 'Check the printer can be paired successfully.'],
#         19: [19, 'Verify Connecting to printer Text.'],
#         20: [20, 'Verify Printer Connected Text.'],
#         21: [21, 'Verify Searching for Wifi network text is displaying.'],
#         22: [22, 'Verify Connecting to Wi-Fi Network page displayed with new fonts and style.'],
#         23: [23, 'Verify Connect Wi-fi Network Text.'],
#         24: [24, 'Select a Wi-Fi without network, click Connect button.'],
#         25: [25, 'Disable the Bluetooth.'],
#         26: [26, 'click on Allow button on Bluetooth disable & enable popup.'],
#         27: [27, 'click previous network.'],
#         28: [28, 'click on enter password.'],
#         29: [29, 'click on connect button on connect wifi network screen.'],
#         30: [30, 'Verify Unable to connect to the printer page displayed correct with the new fonts and styles.'],
#         31: [31, 'Verify the Unable To Connect to Printer page fonts & Style.'],
#         32: [32, 'Stop the App.'],
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5. Check it would go to the page "Let's set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6. Verify the Image & UI with Figma Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7. Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8. Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9. Verify Let's make sure the printer is in Bluetooth pairing mode. Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10. click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11. Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12. Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13. Verify The font & Style of Select your Printer page"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """14. Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"15. Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16.Verify Bluetooth pairing your printer page with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17. Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""18. Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19. Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20. Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21. Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22. Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """23. Verify Connect Wi-fi Network Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """24. Select a Wi-Fi without network, click Connect button"""
#         """Check Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Select_A_WIFI_Without_Network_And_Chcek_The_Fonts_And_Style_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25. Disable the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(4)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26. click on Allow button on Bluetooth disable & enable popup"""
#         start_time = time.time()
#         add_a_printer_screen.click_Allow_For_Disable_Enable_Bluetooth()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"27. click previous network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """28. click on enter password"""
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
#         """30. Verify Unable to connect to the printer page displayed correct with the new fonts and styles"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""31. Verify the Unable To Connect to Printer page fonts & Style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"32. Stop the App"""
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
# #     #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_53213_SemiAuto():
#     """"[New Fonts and UI checking]Perform the Add printer process and check Failed to connect page dislay correct when adding a printer with input wrong password"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Click the menu button at the left corner.'],
#         3: [3, 'Check the slide left page appear.'],
#         4: [4, 'click the button Add a Printer.'],
#         5: [5, 'Check it would go to the page Lets set up your printer.'],
#         6: [6, 'Verify the Image & UI with Figma Manually.'],
#         7: [7, 'Check the moneybadger picture would appears at that page.'],
#         8: [8, 'Click on Start setup button.'],
#         9: [9, 'Verify Lets make sure the printer is in Bluetooth pairing mode Text.'],
#         10: [10, 'click on Next Button.'],
#         11: [11, 'Verify Searching For your Printer Text.'],
#         12: [12, 'Verify Select your Printer Text.'],
#         13: [13, 'Verify The font & Style of Select your Printer page.'],
#         14: [14, 'Select the Printer.'],
#         15: [15, 'Click on Next Button.'],
#         16: [16, 'Verify Bluetooth pairing your printer page with new fonts and style.'],
#         17: [17, 'Click on Next Button.'],
#         18: [18, 'Check the printer can be paired successfully.'],
#         19: [19, 'Verify Connecting to printer Text.'],
#         20: [20, 'Verify Printer Connected Text.'],
#         21: [21, 'Verify Searching for Wifi network text is displaying.'],
#         22: [22, 'Verify Connecting to Wi-Fi Network page displayed with new fonts and style.'],
#         23: [23, 'Verify Connect Wi-fi Network Text.'],
#         24: [24, 'Select a wifi network.'],
#         25: [25, 'Input the invalid password and try to connect.'],
#         26: [26, 'Check the page "Wifi Setup" is spinning.'],
#         27: [27, 'Check fail to connect the printer page prompted with the new fonts and styles.'],
#         28: [28, 'Check fail to connect the printer page prompted with the new fonts and styles and Verify the new fonts and styles.'],
#         29: [29, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5.Check it would go to the page Lets set up your printer"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Setup_Your_Printer_Page_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Verify the Image & UI with Figma Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Image_And_UI_With_Figma_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7.Check the moneybadger picture would appears at that page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_MoneyBadger_Image_Is_Displaying()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """8. Click on Start setup button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Start_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"9. Verify Let's make sure the printer is in Bluetooth pairing mode Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_The_Printer_Is_In_Bluetooth_Paring_Mode_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""10.click on Next Button"""""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11.Verify Searching For your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Verify Select your Printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13.Verify The font & Style of Select your Printer page"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_The_Font_And_Style_Of_Select_Your_Printerpage_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """14.Select the Printer"""
#         start_time = time.time()
#         add_a_printer_screen.Click_The_Printer_Name_To_Select()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"15. Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"16. Verify Bluetooth pairing your printer page with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Bluetoothpairing_your_printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"17.Click on Next Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Next_Button()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""18. Check the printer can be paired successfully"""
#         start_time = time.time()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup1()
#         add_a_printer_screen.click_Bluetooth_pairing_Popup2()
#         sleep(5)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""19.Verify Connecting to printer Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connecting_To_Printer_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""20.Verify Printer Connected Text"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Printer_Connected_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"21. Verify Searching for Wifi network text is displaying"""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Searching_for_wifi_networks_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"22. Verify Connecting to Wi-Fi Network page displayed with new fonts and style"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Connecting_To_Wifi_Network_Page_Fonts_Manually()
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
#         """"24.Select a wifi network """
#         start_time = time.time()
#         add_a_printer_screen.click_NESTWIFI_NETWORK()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"25. Input the invalid password and try to connect"""""""""
#         start_time = time.time()
#         add_a_printer_screen.Enter_Longe_Wrong_Password_In_Field()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"26.Check the page "Wifi Setup" is spinning."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""27.Check fail to connect the printer page prompted with the new fonts and styles"""""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Unable_To_Connect_Printer_To_Wifi_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""28.Check fail to connect the printer page prompted with the new fonts and styles"""""""
#         """"Verify the new fonts and styles"""""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Unable_To_Connect_To_Printer_page_with_new_fonts_and_Style()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"29.Stop the App"""
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

#   #####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_53214_SemiAuto():
#     """"[New Fonts and UI checking]Check the permission dialog display correct, remove all the permission and turn off device Bluetooth, then click add printer"""
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Turn off the Bluetooth and location permission on the device Manually.'],
#         3: [3, 'Click the menu button at the left corner.'],
#         4: [4, 'Check the slide left page appear.'],
#         5: [5, 'click the button Add a Printer.'],
#         6: [6, 'Check the permission dialog display correctly with the new fonts and styles.'],
#         7: [7, 'Turn on Bluetooth permission on the device.'],
#         8: [8, 'Check the Location permission dialog display correctly with the new fonts and styles.'],
#         9: [9, 'Turn on location permission but turn off Bluetooth permission on the device Manually.'],
#         10: [10, 'Disable the Bluetooth.'],
#         11: [11, 'Check the Bluetooth permission dialog display correctly with the new fonts and styles Manually.'],
#         12: [12, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """2.Turn off the Bluetooth and location permission on the device Manually"""
#         """"Disable the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(4)
#         common_method.Show_popup_To_Disable_Location_Permission_On_The_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """3. Click the menu button at the left corner"""
#         start_time = time.time()
#         login_page.click_Menu_HamburgerICN()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """4.Check the slide left page appear"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"5. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6.Check the permission dialog display correctly with the new fonts and styles"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""""7. Turn on Bluetooth permission on the device"""""""
#         start_time = time.time()
#         app_settings_page.Enable_Bluetooth()
#         sleep(4)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8. Check the Location permission dialog display correctly with the new fonts and styles"""
#         start_time = time.time()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """9. Turn on location permission but turn off Bluetooth permission on the device Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Enable_Location_Permission_On_The_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"10.Disable the Bluetooth"""
#         start_time = time.time()
#         app_settings_page.Disable_Bluetooth()
#         sleep(4)
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"11. Check the Bluetooth permission dialog display correctly with the new fonts and styles Manually"""
#         start_time = time.time()
#         common_method.Show_popup_To_Verify_Bluetooth_Permission_Popup_With_New_Design_On_The_Device_Manually()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"12.Stop the App"""
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
####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Addprinter_TestcaseID_53069():
#     """"Printer Setup Screen-Check clicking the exit/cancel button on Exit Printer Setup dialog"""
#     pass
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
#         12: [12, 'heck the slide left page appear on home page(it will navigate to home page).'],
#         13: [13, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
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
#         """"4. click the button Add a Printer'"""
#         start_time = time.time()
#         add_a_printer_screen.click_Add_A_Printer()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """5. Check it would go to the page "Let's set up your printer"""
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
#         """"9. Verify It will stay on Setup Your Printer Screen"""
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
#         """"11. Click on Exit Button"""
#         start_time = time.time()
#         add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """12.Check the slide left page appear on home page(it will navigate to home page)"""""
#         start_time = time.time()
#         add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"13.Stop the App"""
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


#    #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Addprinter_TestcaseID_53072():
#     """"[Login-Splash Screen]:'Install the ZSB series app (.apk file) and check the Login Screen UI and Contents"""
#
#     pass
#     test_steps = {
#         1: [1, 'Open the app and login the account to go to the overview page.'],
#         2: [2, 'Verify the Zebra logo and name will be displayed on the login screen.'],
#         3: [3, 'ZSB Printer Text and ZSB printer image will be located at the centre of the page.'],
#         4: [4, 'Sign in button will be available below the printer image.'],
#         5: [5, 'Click on Sign in and check that it should navigate the user to login options.'],
#         6: [6, 'Sign in using any one of the signing options and check the user can login successfully without any issues.'],
#         7: [7, 'Logout from the mobile app and check the login splash screen is displayed as mentioned in the step 3.'],
#         8: [8, 'Stop the App.']
#     }
#     start_time_main = time.time()
#     stepId = 1
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_main(execID, leftId[test_case_id])
#     try:
#         """"1.Open the app and login the account to go to the overview page."""""
#         start_time = time.time()
#         common_method.tearDown()
#         common_method.Clear_App()
#         common_method.Start_The_App()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"2. Check the contents of the login splash screen."""
#         """"->2. Zebra logo and name will be displayed on the login screen."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_Zebra_Logo_Is_Present_On_Login_Screen()
#         add_a_printer_screen.Verify_Zebra_Text_Is_Present_On_Login_Screen()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"-> 3.ZSB Printer Text and ZSB printer image will be located at the centre of the page."""
#         start_time = time.time()
#         add_a_printer_screen.Verify_ZSB_Printer_Image_Is_Present()
#         add_a_printer_screen.Verify_ZSB_Printer_Text_Is_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """-> 4. Sign in button will be available below the printer image."""
#         start_time = time.time()
#         login_page.Verify_SignIn_Button_Is_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"5. Click on Sign in and check that it should navigate the user to login options."""
#         start_time = time.time()
#         login_page.click_loginBtn()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""6. Sign in using any one of the signing options and check the user can login successfully without any issues."""
#         start_time = time.time()
#         login_page.click_Loginwith_Google()
#         login_page.Loginwith_Added_Email_Id()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """""7. Logout from the mobile app and check the login splash screen is displayed as mentioned in the step 3."""
#         start_time = time.time()
#         common_method.Clear_App()
#         login_page.Verify_SignIn_Button_Is_Present()
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         """"8.Stop the App"""
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
# #####################""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Registration_TestcaseID_46303():
    """""""""To test the ZSB Wi-Fi performance Setup"""""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()

    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.Click_Next_Button()
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 30)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """Store the time till wi-fi turn green."""
    time_taken = registration_page.timeTillWiFiGreen()
    print(time_taken)
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()
# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




def test_Registration_TestcaseID_46307():
    """""""""To verify that user is able to continue with the printer after login with the different register login"""""

    """"1.Open the app and login the account to go to the overview page."""""
    common_method.tearDown()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()

    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.Click_Next_Button()
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """wait till wi-fi turn green."""
    registration_page.timeTillWiFiGreen()
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()
# ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Add_Printer_Test_TestcaseID_45885_SemiAuto():
    """Add a printer- use a printer which has ever been registered before and require a decommission."""


    """Step 1 needs to be verifiedManually """
    """""1.Turn on the testing printer, wait about 1 min, use a toothpick to press the button on the printer back for about 30s to do a decommission
    Check during this process, the power button is flashing yellow light and then white light, finally turn to blue flashing light and will auto feed the barcode info label. """

    """"decommission the added printer and then execute"""
    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
    """"verify pairing your printer text"""
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"verify pairing your printer text"""
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
    add_a_printer_screen.click_Password_Field_On_Join_Network()
    add_a_printer_screen.click_Submit_Button_ON_Join_Network()
    """"verify need the printer driver text"""
    add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
    """""verify registering your printer text"""
    add_a_printer_screen.Verify_Registering_your_Printer_Text()
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    app_settings_page.Verify_Printer_is_already_added()
    """stop the app"""
    common_method.Stop_The_App()
# # ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

