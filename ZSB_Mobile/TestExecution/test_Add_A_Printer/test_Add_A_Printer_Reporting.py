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


def test_Addprinter_TestcaseID_45656():
    """"Adding the moneybadger while the mobile devices bluetooth is disabled"""
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

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
        23: [23, 'Follow the prompt to proceed the adding printer process, check the printer can be added successfully']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])
    stepId = 1
    try:

        start_time = time.time()
        """"1.Open the app and login the account to go to the overview page."""""
        common_method.tearDown()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """2. Click the menu button at the left corner"""
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """3.Check the slide left page appear"""""
        start_time = time.time()
        add_a_printer_screen.Verify_UI_Of_The_Slideleft_Page_Is_Correct()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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
        start_time=time.time()
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
    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)

        # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def test_Addprinter_TestcaseID_45657():
        """"Check the cancle button on 'bluetooth pairing request' dialog when pairing the bluetooth moneybadger"""

        """"1.Open the app and login the account to go to the overview page."""""
        common_method.tearDown()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
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
        """"Verify All the unprovision moneybadgr would appear at the page """
        add_a_printer_screen.Verify_Unprovision_Moneybadgr_On_The_Screen()
        """Select the Printer"""
        add_a_printer_screen.Click_The_Printer_Name_To_Select()
        """"Click on Next Button"""
        add_a_printer_screen.click_Next_Button()
        """Click on Cancel button on the bluetooth pairing popup"""
        add_a_printer_screen.click_Cancel_On_Bluetooth_Paring_Popup()
        """""Verify "Unable to pair your printer"" page pops up"""
        add_a_printer_screen.Verify_Unable_To_Connect_To_Printer_Popup()
        """Verify Please try the following before attempting to connect to printer again. Text"""""
        add_a_printer_screen.Verify_Please_Try_The_Following_Before_Attempting_Again_Text()
        """"Check there are ""Try again"", ""Watch Troubleshooting Video"" and ""Get Help"" three options on the page----This has to be removed from testcase"""
        """"open your device's Bluetooth settings and unpair your connection to this printer before trying again."""""
        common_method.Stop_The_App()
        aps_notification.Stop_Android_App()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Settings_Text_On_SearchBar()
        aps_notification.click_Settings()
        aps_notification.click_Connected_Devices()
        app_settings_page.click_Unpair_Icon()
        app_settings_page.click_On_Unpair()
        app_settings_page.click_Confirm_Delete_Popup()
        aps_notification.Stop_Android_App()
        common_method.Start_The_App()
        """"click on Try Again button"""
        add_a_printer_screen.click_Try_Again()
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
        """Verify Connecting to Cloud Text"""
        add_a_printer_screen.Verify_Connecting_To_Cloud_Text()
        """"verify need the printer Setup Complete text"""
        add_a_printer_screen.Verify_Printer_Setup_Complete_Text()
        """"click on finish setup button"""
        add_a_printer_screen.click_Finish_Button()
        """"click home tab"""
        add_a_printer_screen.click_Home_Tab()
        """stop the app"""
        common_method.Stop_The_App()

    # ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""