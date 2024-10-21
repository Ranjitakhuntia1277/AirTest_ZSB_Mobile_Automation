from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Others import Others
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_APS_Testcases.store import execID, leftId
import inspect


class Android_APS_Others:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
others = Others
aps_notification = APS_Notification(poco)
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()
start_execution_loop(execID)


def test_APS_Others_TestcaseID_49156():
    """Check APS would be deleted after deleting ZSB Series app"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Delete ZSB app from the Android device."],
        2: [2,
            "Go to Settings -> Connection & sharing -> More connection settings -> Printing in Android device. Check APS has been removed."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        common_method.Stop_The_App()
        #### common_method.uninstall_app()
        aps_notification.Stop_Android_App()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Settings_Text_On_SearchBar()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        aps_notification.click_Settings()
        aps_notification.click_Connected_Devices()
        aps_notification.click_Connection_Preferences()
        aps_notification.click_Printing_Tab()
        aps_notification.ZSB_Series_Is_Not_Present()
        aps_notification.Stop_Android_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_APS_Others_TestcaseID_49540():
    """Check ZSB printers are fetched out in ZSB APS after keep ZSB APP idle for more than 1 day"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Open ZSB App and login with test user."],
        2: [2, "Go to mobile phone settings -> connected devices -> Connection preferences -> Printing."],
        3: [3, "Check ZSB Series is on and printers can be fetched in ZSB APS."],
        4: [4, "Back to homepage and keep ZSB App running in the background for more than 1 day."],
        5: [5, "Go to ZSB APS list to check printers are fetched the next day."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""""click on the left hamburger menu on the home page"""""""""
        login_page.click_Menu_HamburgerICN()
        common_method.Stop_The_App()
        aps_notification.Stop_Android_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Settings_Text_On_SearchBar()
        aps_notification.click_Settings()
        aps_notification.click_Connected_Devices()
        aps_notification.click_Connection_Preferences()
        aps_notification.click_Printing_Tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        aps_notification.click_ZSB_Series()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

        """""4. Back to homepage keep ZSB APP running in background for more than 1 day needs to be verified Manually"""
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


#
# # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_APS_Others_TestcaseID_49788():
    """Check user can disable ZSB series print service and cannot fetch any Money badger printer"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Go to mobile phone settings - Connected devices - Connection preferences - Printing (Samsung path: settings - Connections - More connection settings - Printing). Check 'ZSB Series' is in Print Services list."],
        2: [2,
            "Turn off 'ZSB Series'. Click 'ZSB Series' to go to ZSB Series print service settings. Check ZSB Series is off. Check no ZSB printers are fetched."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        common_method.Stop_The_App()
        aps_notification.Stop_Android_App()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Settings_Text_On_SearchBar()
        aps_notification.click_Settings()
        aps_notification.click_Connected_Devices()
        aps_notification.click_Connection_Preferences()
        aps_notification.click_Printing_Tab()
        aps_notification.click_ZSB_Series()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"Turn off the printer option"""
        aps_notification.Verify_And_Turn_OFF_APS()
        aps_notification.Stop_Android_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
    #


#
# #     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_APS_Others_TestcaseID_49789():
    """Check user can disable ZSB series print service and cannot fetch any Money badger printer"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Go to mobile phone settings - Connected devices - Connection preferences - Printing (Samsung path: settings - Connections - More connection settings - Printing). Check 'ZSB Series' is in Print Services list."],
        2: [2,
            "Turn off 'ZSB Series'. Click 'ZSB Series' to go to ZSB Series print service settings, then turn on 'ZSB Series'. Check all ZSB printers are fetched."],

    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        common_method.Stop_The_App()
        aps_notification.Stop_Android_App()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Settings_Text_On_SearchBar()
        aps_notification.click_Settings()
        aps_notification.click_Connected_Devices()
        aps_notification.click_Connection_Preferences()
        aps_notification.click_Printing_Tab()
        aps_notification.click_ZSB_Series()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"Turn on the printer option"""
        aps_notification.Verify_And_Turn_ON_APS()
        aps_notification.Stop_Android_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        common_method.stop_adb_log_capture()
        upload_case_files(execID, os.path.dirname(ADB_LOG), test_run_start_time, uploaded_files)
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
        end_execution_loop(execID)
        end_execution(execID)

#     # ##"""""""""""""""""""""""""""""""""""""""End""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #######"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
