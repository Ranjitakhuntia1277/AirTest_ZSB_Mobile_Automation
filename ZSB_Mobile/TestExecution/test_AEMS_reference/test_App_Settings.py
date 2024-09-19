import inspect

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from airtest.core.api import connect_device


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)

# common_method.clear_directory()
ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()




# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


start_execution_loop(execID)

def test_AppSettings_TestcaseID_49665():
    """Manage network- Check Bluetooth Connection failed dialog will pop up after BT Paring Request dialog disappeared"""

    """"WIFI should not be connected in wifi section under printer name"""

    #

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Printer Settings/Printer name/Wi-Fi tab, click Manage Networks option\n'
               '- Verify Manage Networks option is clickable and navigates to the correct page'],
        2: [2, 'The "Bluetooth Connection Required" dialog pops up, click Continue button\n'
               '- Verify Bluetooth Connection Required dialog appears\n'
               '- Verify clicking Continue button'],
        3: [3, 'When the "Bluetooth Pairing Request" dialog pops up, do not click Cancel or Pair option\n'
               'Check Bluetooth Connection failed dialog will pop up after BT Pairing Request dialog disappears'],
        4: [4,
            'Click Continue, try to connect BT again, this time click pair on the "Bluetooth Pairing Request" dialog\n'
            '- Verify able to pair BT successfully\n'
            '- Verify able to manage networks']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    try:
        # Step 1: Go to Printer Settings/Printer name/Wi-Fi tab, click Manage Networks option
        start_time = time.time()

        common_method.tearDown()
        common_method.Clear_App()
        common_method.Start_The_App()
        """ Allow pop up before login for the fresh installation"""
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        """for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        """click on hamburger menu"""
        login_page.click_Menu_HamburgerICN()
        """"click printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """click on printer name"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """"click wifi tab"""
        app_settings_page.click_wifi_tab()
        """"click manage network buttons"""
        app_settings_page.click_Manage_Networks_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: The "Bluetooth Connection Required" dialog pops up, click Continue button
        start_time = time.time()

        """"verify bluetooth connection required text"""
        app_settings_page.get_text_Bluetooth_connection_required_Txt()
        """""click continue button on bluetooth connection required"""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Simulate not clicking Cancel or Pair on "Bluetooth Pairing Request" dialog
        start_time = time.time()

        add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
        """"verify bluetooth_connection failed popup"""
        app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Continue, try to connect BT again, this time click Pair on "Bluetooth Pairing Request" dialog
        start_time = time.time()

        """""click continue button on connection failed popup"""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
        """"click on manage networks button"""
        app_settings_page.click_Manage_Networks_Btn()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47911():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in to the ZSB App with printer added.'],
        2: [2, 'Click Printer Settings'],
        3: [3, 'Click printer tab'],
        4: [4, 'Check printer General tab information'],
        5: [5,
            'Try Changing darkness level or Change "Auto Label Feed on Printer Cover" value.Check auto Label Feed On Printer Cover Close value should show Enable / Disable not in loading or in progress.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # step 1: "Log in to the ZSB App with printer added."
        start_time = time.time()
        """ Verify auto Label Feed On Printer Cover Close value doesn't retrieve in progress after changing darkness level."""

        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify printer is already added"""
        app_settings_page.Verify_Printer_is_already_added()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 2: "Click Printer Settings"
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Printer settings tab"""
        app_settings_page.click_Printer_Settings()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 3: "Click printer tab"
        start_time = time.time()

        """"click on printer name on the printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 4: "Check printer General tab information"
        start_time = time.time()

        """verify general tab text"""
        app_settings_page.Verify_General_Tab_Text()
        """"verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 5: "Try Changing darkness level or Change 'Auto Label Feed on Printer Cover' value. Check auto Label Feed On Printer Cover Close value should show Enable / Disable not in loading or in progress."
        start_time = time.time()

        """verify darkness level bar is present & change the darkness level"""
        app_settings_page.Verify_Darkness_Level_Bar()
        """"change the darkness level"""
        app_settings_page.Change_Darkness_Level_Bar()
        """verify the darkness updated message"""
        app_settings_page.Verify_Darkness_Updated_Message()
        """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
        app_settings_page.Check_toggle_button()
        """click on the toggle button"""
        app_settings_page.click_toggle_button()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)
###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47918():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Install ZSB Series app'],
        2: [2, 'Launch the app'],
        3: [3, 'Select "Only this time" from all (Location, nearby) permission pop-ups'],
        4: [4,
            'Close and re-launch the app. Check that all permissions should ask for permission every time if the user has opted to ask for every time or denied']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:

        """	Verify ZSB app permission works fine."""
        """Freshly Install the latest stage/production app on the phone & printer should be added"""

        # step1:Install ZSB Series app
        start_time = time.time()

        common_method.tearDown()
        common_method.Stop_The_App()
        common_method.Clear_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # step2:Launch the app
        start_time = time.time()

        common_method.Start_The_App()
        """ Allow pop up before login for the fresh installation"""
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        """for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        """Relaunch the app"""
        common_method.relaunch_app()
        """ Allow pop up before login for the fresh installation"""
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # step3:Select "Only this time" from all (Location, nearby) permission pop-ups
        start_time = time.time()

        """for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # step4:Close and re-launch the app. Check all permission should ask for permission every time if user has opt to ask for every time or denied
        start_time = time.time()

        """Relaunch the app"""
        common_method.relaunch_app()
        """Permission is not displaying due to SMBM-1242"""
        login_page.Verify_LoginAllow_Popup_IS_Displaying()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)
##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47810():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB mobile app'],
        2: [2, 'Navigate to left slide page to click the button \'Add a Printer\''],
        3: [3, 'Register printer to mobile app'],
        4: [4, 'Go to Home > Recently Printed Designs.'],
        5: [5,
            'Verify "Recently Printed Labels" text is displayed. Check "Recently Printed Labels" text is displayed properly. There should not be any overlap in text.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
        """"Install the latest production app on the phone & printer should be added with logged in condition Create the object for Login page & Common_Method page to reuse the methods"""
        """""Check whether App is installed or not"""""

        """""start the app"""""
        # step 1: "Launch ZSB mobile app"
        start_time = time.time()

        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 2: "Navigate to left slide page to click the button 'Add a Printer'"
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 3: "Register printer to mobile app"
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 4: "Go to Home > Recently Printed Designs."
        start_time = time.time()

        """"Click on hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on  home tab"""
        app_settings_page.click_Home_Tab()
        sleep(2)
        """""verify printer is already added or not"""
        app_settings_page.Verify_Printer_is_already_added()
        sleep(1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 5: "Verify "Recently Printed Labels" text is displayed. Check "Recently Printed Labels" text is displayed properly. There should not be any overlap in text."
        start_time = time.time()

        """""""verify recently printed labels is present"""""""
        app_settings_page.Is_Present_Recently_Printed_Labels_Text()
        """""""verify first recent lebel is present"""""""
        app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
        """click on the first recently present label"""
        app_settings_page.click_Firstone_In_Recently_Prtinted_Label()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        common_method.stop_adb_log_capture()
        upload_case_files(execID, os.path.dirname(ADB_LOG), test_run_start_time)
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)
        end_execution_loop(execID)
        end_execution(execID)


###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
