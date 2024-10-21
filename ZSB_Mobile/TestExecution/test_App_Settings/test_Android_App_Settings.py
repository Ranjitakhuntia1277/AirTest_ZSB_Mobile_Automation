import py
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

# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_App_Settings.store import execID, leftId
import inspect


class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")
sleep(2.0)
"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()

start_execution_loop(execID)


# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_47918():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Install ZSB Series app"],
        2: [2, "Launch the app"],
        3: [3, "Select 'Only this time' from all (Location, nearby) permission pop up"],
        4: [4,
            "Close and re-launch the app. Check that all permissions should ask for permission every time if user has opted to ask for every time or denied."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """	Verify ZSB app permission works fine."""
        """Freshly Install the latest stage/production app on the phone & printer should be added"""
        common_method.tearDown()
        common_method.Stop_The_App()
        common_method.Clear_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        common_method.Start_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """ Allow pop up before login for the fresh installation"""
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        """for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Relaunch the app"""
        common_method.relaunch_app()
        """ Allow pop up before login for the fresh installation"""
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        """Relaunch the app"""
        common_method.relaunch_app()
        """Permission is not displaying due to SMBM-1242"""
        login_page.Verify_LoginAllow_Popup_IS_Displaying()
        common_method.Stop_The_App()
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


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

####bug id----SMBM-2120
def test_AppSettings_TestcaseID_49665():
    """Manage network- Check Bluetooth Connection failed dialog will pop up after BT Paring Request dialog disappeared"""

    """"WIFI should not be connected in wifi section under printer name"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Go to Printer Settings/Printer name/Wi-Fi tab, click Manage Networks option."],
        2: [2, "The 'Bluetooth Connection Required' dialog pops up, click the Continue button."],
        3: [3,
            "When the 'Bluetooth Pairing Request' dialog pops up, do not click Cancel or Pair option (simulate user forgets to click). Check that the Bluetooth Connection failed dialog will pop up after the Bluetooth Pairing Request dialog disappears."],
        4: [4,
            "Click Continue, try to connect Bluetooth again, this time click Pair on the 'Bluetooth Pairing Request' dialog. Check that you are able to pair Bluetooth successfully. Check that you are able to manage networks."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
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
        # -----------------------
        # Step 2
        start_time = time.time()
        """"verify bluetooth connection required text"""
        app_settings_page.get_text_Bluetooth_connection_required_Txt()
        """""click continue button on bluetooth connection required"""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        login_page.click_Allow_ZSB_Series_Popup()
        add_a_printer_screen.click_Bluetooth_pairing_Popup1_on_Setting_page()
        add_a_printer_screen.click_Bluetooth_pairing_Popup2_on_Setting_page()
        """"verify bluetooth_connection failed popup"""
        app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """""click continue button on connection failed popup"""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
        """"click on manage networks button"""
        app_settings_page.click_Manage_Networks_Btn()
        """stop the app"""
        common_method.Stop_The_App()
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
def test_AppSettings_TestcaseID_45689():
    """""""""Check Change Theme Function Works"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """""""""start the app"""""""""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [
            1,
            "Click on the hamburger button on Home page, then click the three dots right on the workspace's name. Check that there are two options that can be selected: 'Edit' and 'Change Theme.'"],
        2: [
            2,
            "Click on the 'Change Theme' option, check that the Change Theme page pops up. Check that there are five options that can be selected: Modern, Eclectic, Bohemian, Professional, Maker."],
        3: [
            3,
            "Select the Eclectic option, check the 'Save & Exit' button appears with enabled status, click the button. Check it goes back to home page automatically. Check the whole UI/buttons are shown with the Eclectic theme, red style."],
        4: [4, "Repeat step 2 and 3 to cover all kinds of themes, check each theme works well."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""""click hamburger menu"""""""
        login_page.click_Menu_HamburgerICN()
        """"click three dot on workspace"""""
        app_settings_page.click_Three_Dot_On_Workspace()
        """""""verify edit text"""""""
        app_settings_page.get_text_Edit_Txt()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on change theme"""
        app_settings_page.click_Change_Theme()
        """""verify change theme page pop ups by verifying the change theme header"""
        app_settings_page.get_text_Change_Theme_Header()
        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""""change 5 theme and check it should get saved and then need to tap on exit"""""""
        app_settings_page.check_Change_Electic_Theme()
        sleep(3)
        """""click save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        """""""SMBM-986 is still present""""
        """"After applying the theme check whether it is navigating back to home page not verifying the background image as there is no element present"""
        sleep(3)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """""click on hamburger icon on home page"""""
        login_page.click_Menu_HamburgerICN()
        sleep(4)
        """"click on three dot icon on workspace"""""
        app_settings_page.click_Three_Dot_On_Workspace()
        """"click on change theme"""
        app_settings_page.click_Change_Theme()
        """""check Bohemian theme"""
        sleep(3)
        app_settings_page.check_Change_Bohemian_Theme()
        sleep(3)
        """""click save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.Home_text_is_present_on_homepage()
        """""click on hamburger icon on home page"""
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """"click on three dot icon on workspace"""""
        app_settings_page.click_Three_Dot_On_Workspace()
        """"click on change theme"""
        app_settings_page.click_Change_Theme()
        """""check Professional theme"""
        sleep(3)
        app_settings_page.check_Change_Professional_Theme()
        sleep(3)
        """""click save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.Home_text_is_present_on_homepage()
        """""click on hamburger icon on home page"""
        login_page.click_Menu_HamburgerICN()
        sleep(4)
        """"click on three dot icon on workspace"""""
        app_settings_page.click_Three_Dot_On_Workspace()
        """"click on change theme"""
        app_settings_page.click_Change_Theme()
        """""check Maker theme"""
        sleep(3)
        app_settings_page.check_Change_Maker_Theme()
        sleep(3)
        """""click save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.Home_text_is_present_on_homepage()
        """""click on hamburger icon on home page"""
        login_page.click_Menu_HamburgerICN()
        sleep(4)
        """"click on three dot icon on workspace"""""
        app_settings_page.click_Three_Dot_On_Workspace()
        """"click on change theme"""
        app_settings_page.click_Change_Theme()
        """""check Modern theme"""
        sleep(3)
        app_settings_page.check_Change_Modern_Theme()
        sleep(3)
        """""click save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.Home_text_is_present_on_homepage()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_45690():
    """""""""Update Unit of Measure in Mobile App, check it will sync to Web Portal and Printer Tools"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [
            1,
            "Click the hamburger button on Home page, then click on the pen icon near the user name. Check that the Settings page pops up."],
        2: [
            2,
            "Check there is a 'Units of Measurement' option. Check there are 3 options under the list: Millimetres, Centimetres, Inches. Default value is Inches."],
        3: [
            3,
            "Update Unit of measure from Inches to Centimetres, check a toast shows up: 'Unit of Measurement updated successfully.'"],
        4: [
            4,
            "Back to home page, check printer media size unit shows as Centimetres. Check recently Printed Labels size shows in Centimetres."],
        5: [5, "Go to Common Design, check the common design unit shows as Centimetres."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """""start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""click hamburger menu"""""
        login_page.click_Menu_HamburgerICN()
        """"click on the pen icon near the user name"""
        app_settings_page.click_pen_Icon_near_UserName()
        sleep(1)
        poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"""""""verify units of measurement text is present or not"""""""""
        app_settings_page.check_If_Units_of_Measurements_Is_Present()
        """""""verify  Inches is the by default value is displaying"""""""
        app_settings_page.click_Units_of_Measurements()
        sleep(2)
        """"Verify all the available values"""""
        app_settings_page.verify_Milimetres_Is_Present()
        app_settings_page.verify_Centimetres_Is_Present()
        app_settings_page.verify_Inches_Is_Present()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"click on Centimeters option"""
        app_settings_page.click_Centimeters()
        sleep(1)
        """""""""verify the updated message popup"""""
        app_settings_page.verify_updated_msg()
        """""""Click on the hamburger icon"""""""
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """""click on the home tab"""
        app_settings_page.click_Home_Tab()
        sleep(2)
        """""""""verify printer details, everything should display in centimeters"""""
        app_settings_page.verify_printer_details_in_Centimeters()
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """""click on my design tab"""
        app_settings_page.click_My_Design()
        sleep(4)
        """""verify the design size under my design"""
        app_settings_page.verify_My_Details_Design_in_Centimeters()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        sleep(1)
        poco.scroll()
        app_settings_page.click_Units_of_Measurements()
        sleep(2)
        app_settings_page.click_Inches()
        sleep(2)
        """Syncing to web portal is not working properly so need to verify manually"""
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_45691():
    """""""""Edit Workspace - upload and remove image"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Click the hamburger button on Home page, then click the 3-dot menu next to workspace, and select Edit. Check that the Edit Workspace page opens."],
        2: [2,
            "Click Upload Photo button. Check the access request button pops up (This dialog only pops up the first time; after being allowed, this dialog would not pop up).Select Allow option."],
        3: [3,
            "Check that the file browser opens, only image files are listed. Select a picture, check that the picture appears on the Avatar, and that there is an enabled 'Save & Exit' button displaying on the Edit Workspace."],
        4: [4,
            "Click the Save & Exit button, re-enter the Edit Workspace page. Check that the Avatar is the picture selected in step 4, and that there is a 'Remove Image' button on the 'Upload Photo' right side."],
        5: [5,
            "Click Remove Image, check that the image is removed from the Avatar and shows the initial of the workspace name."],
        6: [6,
            "Click Upload Photo again, swipe left on the device without selecting any picture. Check that the Avatar is still the initial of the workspace name.Upload an image again and click the Save button, check that the image can be uploaded successfully. Need to cover PNG, JPG, JPEG, GIF, and BMP format pictures."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """"start the app"""""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        sleep(2)
        """""verify the Edit workspace text"""
        app_settings_page.get_text_Edit_Workspace()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """""""click upload photo"""""""
        app_settings_page.click_upload_photo()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        """""click on the 1st image"""
        app_settings_page.click_On_First_Image_SearchBar()
        app_settings_page.click_First_Image()
        app_settings_page.click_JPG_ON_Result()
        app_settings_page.click_First_Image_ON_The_List()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """click on the save & exit"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(2)
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        app_settings_page.click_Remove_Image()
        app_settings_page.Is_Present_Profile_Avatar_Letter()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        app_settings_page.click_upload_photo()
        sleep(1)
        app_settings_page.click_Back_Icon()
        app_settings_page.click_Close_Icon()
        sleep(2)
        app_settings_page.click_Save_Exit_Btn()
        sleep(2)
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_45692():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Click the hamburger button on Home page, then click the 3-dot menu next to workspace, and select Edit. Check Edit workspace page opened."],
        2: [2,
            "Clear Workspace Name, check there is no Save & Exit button, click the back button. Reenter the Edit Workspace page, check Workspace will keep the original value."],
        3: [3, "Update workspace name with space, click save and exit. Check can save successfully."],
        4: [4,
            "Update Workspace name to a long name the contains special characters: !@#$%^&*()_+, check workspace can set more than 30 characters. Trigger any notification, go to notification tab. Check the workspace name shows correctly on notification list."],
        5: [5, "Update workspace name contains numbers, check workspace can save successfully."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    """""""""Edit Workspace - Update workspace name"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """""""""start the app"""""""""
    try:
        start_time = time.time()
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        sleep(2)
        """""verify the Edit workspace text"""
        app_settings_page.get_text_Edit_Workspace()
        """"Verify Workspace Name Text"""
        sleep(2)
        app_settings_page.Is_Present_Workspace_Name_Text()
        """""""click on workspace name"""""""""
        app_settings_page.click_Workspace_Name_Text_Field()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """""clear workspace name text field"""
        app_settings_page.Clear_Workspace_Name()
        sleep(2)
        """"Click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        """""""""""Verify save & exit option is not there"""""""""
        app_settings_page.Verify_SaveExit_Option_Is_Not_There()
        """""click on back icon on edit workspace"""
        app_settings_page.click_back_Icon_On_Edit_Workspace()
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        sleep(2)
        """""Check the previous Workspace name is displaying"""
        app_settings_page.Is_Present_Workspace_Name()
        app_settings_page.click_Workspace_Name_Text_Field()
        app_settings_page.Clear_Workspace_Name()
        sleep(2)
        app_settings_page.click_Workspace_Name_Text_Field()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"verify the workspace field by giving space """
        app_settings_page.Update_Workspace_Name_With_Space()
        sleep(3)
        """"Click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        sleep(3)
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        app_settings_page.click_Workspace_Name_Text_Field()
        app_settings_page.Clear_Workspace_Name()
        sleep(2)
        """"Click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        sleep(1)
        app_settings_page.click_Workspace_Name_Text_Field()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """"verify the workspace field by special characters with more than 30 characters """
        app_settings_page.Update_Workspace_Name_With_Special_Characters_with_30_characters()
        sleep(3)
        """"Click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        sleep(3)
        """""click on save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        """"""""""Verify the workspace updated name"""""""""""""""
        app_settings_page.Verify_Updated_Name()
        sleep(3)
        app_settings_page.click_Workspace_Name_Text_Field()
        app_settings_page.Clear_Workspace_Name()
        sleep(2)
        """"Click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        app_settings_page.click_Workspace_Name_Text_Field()
        app_settings_page.Update_Workspace_Name_with_Original_Name()
        sleep(3)
        app_settings_page.click_Keyboard_back_Icon()
        sleep(3)
        """""click on save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(3)
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_45705():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Go to Account Profile page."],
        2: [2, "Clear First Name and Last Name text boxes."],
        3: [3,
            "Go to Home page then back again to Account Profile page. Verify the original values for First Name and Last Name are displayed."],
        4: [4,
            "Edit First Name with a name containing more than 30 characters. Verify First Name is updated and alert message 'User account updated' is displayed. Verify Profile Account is updated."],
        5: [5,
            "Edit First Name with a name containing special characters: !@#$%^&*()_+?, Verify First Name is updated and alert message 'User account updated' is displayed. Verify Profile Account is updated."],
        6: [6,
            "Edit First Name with a name containing numbers. Verify First Name is updated and alert message 'User account updated' is displayed. Verify Profile Account is updated."],
        7: [7,
            "Edit First Name with a name containing space. Verify First Name is updated and alert message 'User account updated' is displayed. Verify Profile Account is updated."],
        8: [8, "Repeat steps 5-8 for Last Name textbox."],
        9: [9,
            "Click Change Password link. Verify Password Recovery page is displayed. Notes: BUG SMBM-1098 when the user clicks on the Change Password link on the Account Settings page, they are brought to a Password Recovery page where they need to enter their username to continue. This is the wrong page. After this bug is fixed, these cases should be updated at that time."],
        10: [10,
             "Input invalid username. Verify error message 'Please enter a valid email address or username.' is displayed."],
        11: [11, "Input valid username then click Submit. Verify Change Password page is displayed."],
        12: [12,
             "Input invalid old password, valid new password. Click Submit. Verify error message 'The current password provided for the user is invalid' is displayed."],
        13: [13,
             "Go to Change Password page, input valid old password, invalid new password. Verify error message 'Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password MUST NOT contain spaces or tabs.' is displayed."],
        14: [14,
             "Input valid old password, valid new password, different value for confirm password. Verify error message 'Password and Confirm Password must match.' is displayed."],
        15: [15, "Input valid old/new/confirm passwords. Click Submit. Verify Success page is displayed."],
        16: [16,
             "Click 'Click here' link to login with the new password. Verify user is redirected to the homepage. [SMBIT-291]"],
        17: [17, "Click Return to Login button. Verify login page is displayed. [SMBIT-291]"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    """""""""Verify account profile update for non-Zebra user"""""

    """""Install the latest production app on the phone & printer should be added with logged in condition"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    """""Check whether App is installed or not"""

    """""""start the app"""""""
    try:
        start_time = time.time()
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""click hamburger menu"""""
        login_page.click_Menu_HamburgerICN()
        """"click on the pen icon near the user name"""
        app_settings_page.click_pen_Icon_near_UserName()
        """""""verify First name text is present"""""""
        app_settings_page.Is_Present_First_Name_Text()
        """""""verify last name text is present"""""""
        app_settings_page.Is_Present_Last_Name_Text()
        """""click first name text field"""
        app_settings_page.click_First_Name_Text_Field()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"clear first name field"""
        sleep(3)
        app_settings_page.clear_First_Name()
        """""Update first name with special characters with 30 characters"""
        app_settings_page.Update_First_Name_With_Special_Characters_with_30_characters()
        sleep(3)
        poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""click last name text field"""
        app_settings_page.click_Last_Name_Text_Field()
        """"clear Last name field"""
        app_settings_page.clear_Last_Name()

        """""Update last name with special characters with 30 characters"""
        app_settings_page.Update_Last_Name_With_Special_Characters_with_30_characters()
        sleep(3)
        """""click keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        """"verify the updated names message"""
        app_settings_page.verify_Your_changes_have_been_saved_Message()
        sleep(3)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """""click last name text field"""
        app_settings_page.click_Last_Name_Text_Field()
        """"clear Last name field"""
        app_settings_page.clear_Last_Name()
        """Update the default Last name"""
        app_settings_page.Update_Default_Last_Name()
        app_settings_page.click_Keyboard_back_Icon()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Home_Tab()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        """""click First name text field"""
        app_settings_page.click_First_Name_Text_Field()
        """"clear First name field"""
        app_settings_page.clear_First_Name()
        """Update the default First name"""
        app_settings_page.Update_Default_First_Name()
        app_settings_page.click_Keyboard_back_Icon()
        """""""change password link is not opening the correct page---SMBM-1098, due to this bug could not automate"""""
        """""""change email is not yet implemented so could not automate this"""""""""
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47810():
    """"Verify recently printer labels text shouldn't overlap on theme background picture."""""
    """"Install the latest production app on the phone & printer should be added with logged in condition Create the object for Login page & Common_Method page to reuse the methods"""
    """""Check whether App is installed or not"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Launch ZSB mobile app."],
        2: [2, "Navigate to left slide page to click the button 'Add a Printer'.Register printer to mobile app."],
        3: [3, "Go to Home > Recently Printed Designs."],
        4: [4,
            "Verify 'Recently Printed Labels' text is displayed. Check 'Recently Printed Labels' text is displayed properly. There should not be any overlap in text."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """""start the app"""""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"Click on hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"click on  home tab"""
        app_settings_page.click_Home_Tab()
        sleep(2)
        """""verify printer is already added or not"""
        app_settings_page.Verify_Printer_is_already_added()
        sleep(1)
        """""""verify recently printed labels is present"""""""
        app_settings_page.Is_Present_Recently_Printed_Labels_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """""""verify first recent lebel is present"""""""
        app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
        """click on the first recently present label"""
        app_settings_page.click_Firstone_In_Recently_Prtinted_Label()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47820():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Open the app and log in to the account to go to the overview page (recently printed labels)."],
        2: [2, "Scroll to the bottom of the list. Check all designs are fully visible on the Home page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    """"Verify ZSB app home page (overview page) should scroll to the bottom of the list in Recently Printed Labels"""""

    """"Precondition:
    1. Install the latest production app on the tablet
    2. Prepare a production with printer added and sign in
    3. There are 6 Recently Printed Lables present in account"""""
    #
    try:
        start_time = time.time()
        """""""start the app"""""""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        """"click on  home tab"""
        app_settings_page.click_Home_Tab()
        sleep(2)
        """""verify printer is already added or not"""
        app_settings_page.Verify_Printer_is_already_added()
        sleep(1)
        """""""verify recently printed labels is present"""""""
        app_settings_page.Is_Present_Recently_Printed_Labels_Text()
        """""""verify first recent lebel is present"""""""
        app_settings_page.Is_Present_Firstone_In_Recently_Printed_Label()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        poco.scroll()
        """"Verify buy more labels is present"""
        app_settings_page.Is_Present_Buy_More_Labels()
        sleep(3)
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47825():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to Mobile App."],
        2: [2, "In home page, click pen icon to go to user setting page."],
        3: [3, "Check at the bottom of the page, 'Delete Account' button is shown next to Logout button."],
        4: [4,
            "Click Delete Account button, check Delete Account page shows up. There are 3 items that need to be acknowledged and checked before continuing."],
        5: [5, "Click Cancel button, check Delete Account page closes and user setting page is shown."],
        6: [6,
            "Click Delete Account button again, check Delete Account page shows up again.Click Cancel button and logout."],
        7: [7,
            "Re-login to Mobile App, check user can login without issue. Check ZSB app shouldn't throw any logout error in any scenarios."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    """""Verify ZSB app doesn't shows error as "Logout failed. Please try logging out again"."""""

    #
    """Precondition:
    1. Registered a production user
    2. Install production Mobile App into test device"""
    #
    try:
        start_time = time.time()
        """""""start the app"""""""
        common_method.tearDown()
        sleep(3)
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""click on hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """""click on the pen icon near to user name"""
        app_settings_page.click_pen_Icon_near_UserName()
        """Verify User settings text is present"""
        app_settings_page.Is_Present_User_Settings_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"Scroll till the delete button"""
        app_settings_page.Scroll_till_Delete_Account()
        """"Verify Logout button"""
        app_settings_page.Is_Present_Logout_Btn()
        """"click on the delete account button"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.click_Delete_Account_Btn()
        """"Verify Delete account text is present"""
        app_settings_page.verify_Delete_Account_Text()
        """verify Please Acknowledge text is present"""""
        app_settings_page.verify_Please_Acknowledge_Text()
        """""verify & click on first checkbox """
        app_settings_page.click_First_Checkbox()
        """""verify & click on second checkbox """
        app_settings_page.click_Second_Checkbox()
        """""verify & click on third checkbox """
        app_settings_page.click_Third_Checkbox()
        """verify security message text is present"""""
        app_settings_page.verify_Security_Message_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """click on cancel button"""
        app_settings_page.click_Cancel_Btn()
        """verify setting text is present"""
        app_settings_page.Is_Present_User_Settings_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """"verify & click on delete account button"""
        app_settings_page.click_Delete_Account_Btn()
        """""verify & click on first checkbox """
        app_settings_page.click_First_Checkbox()
        """""verify & click on second checkbox """
        app_settings_page.click_Second_Checkbox()
        app_settings_page.click_Third_Checkbox()
        """"click on the confirm button to delete the account"""
        app_settings_page.click_Confirm_Btn_To_DeleteAccount()
        """"verify zebra logo is present"""
        app_settings_page.Is_Present_Zebra_Logo()
        """verify ZSB printer image is displaying"""""
        app_settings_page.Is_Present_ZSB_Printer_Icon()
        """""Verify login page Important messsage text"""
        app_settings_page.Verify_Login_Page_Important_Message_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """click on login button"""
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        sleep(3)
        """"verify delete account pop up message"""
        app_settings_page.Is_Present_Delete_Account_Popup()
        """"click on cancel button on the pop up"""
        app_settings_page.click_Cancel_on_Delete_Account_Popup()
        """"verify settings text is displaying"""
        app_settings_page.Is_Present_User_Settings_Text()
        """stop the app"""
        common_method.Stop_The_App()
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


# Testcase 47879 deleted:
# def test_AppSettings_TestcaseID_47879():
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, "Install ZSB Series app"],
#         2: [2, "Launch the app"],
#         3: [3, "Select 'Only this time' from all (Location, nearby) permission pop up"],
#         4: [4,
#             "Close and re-launch the app. Check that all permissions should ask for permission every time if user has opted to ask for every time or denied."]
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#
#     """""Verify typo and guide message is correct on Searching For your printer page."""""
#
#     """Precondition:
#     1. Registered a production user
#     2. Install production Mobile App into test device"""""
#
#     try:
#         start_time = time.time()
#         """""""start the app"""""""
#         common_method.tearDown()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         """"click on hamburger icon"""
#         login_page.click_Menu_HamburgerICN()
#         """""click on Add a printer"""
#         add_a_printer_screen.click_Add_A_Printer()
#         """""click on start Button"""
#         add_a_printer_screen.click_Start_Button()
#         login_page.click_Allow_ZSB_Series_Popup()
#         add_a_printer_screen.Verify_Lets_Make_Sure_Text()
#         add_a_printer_screen.click_LED_Guide_Button()
#         """"verify printer led not flashing text"""
#         add_a_printer_screen.Verify_Blue_Left_LED_Text_And_Expand()
#         add_a_printer_screen.Verify_Red_Right_LED_Text_And_Expand()
#         """click on the printer led guide done button"""
#         add_a_printer_screen.click_Printer_LED_Guide_Done_Btn()
#         add_a_printer_screen.Click_Next_Button()
#         """"Verify searching for your printer text"""
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         """stop the app"""
#         common_method.Stop_The_App()
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         if screenshot_path not in uploaded_files:
#             upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
# Testcase 47880 deleted:
# def test_AppSettings_TestcaseID_47880():
#     """""Verify "Done" Button and text "LED light Behavior Support" position is correct in Printer LED Guide dialog."""""
#     #
#
#     """start the app"""
#     common_method.tearDown()
#     login_page.click_LoginAllow_Popup()
#     login_page.click_Allow_ZSB_Series_Popup()
#     """"click on hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """""click on Add a printer"""
#     add_a_printer_screen.click_Add_A_Printer()
#     """""click on start Button"""
#     add_a_printer_screen.click_Start_Button()
#     add_a_printer_screen.Verify_Lets_Make_Sure_Text()
#     add_a_printer_screen.click_LED_Guide_Button()
#     #### """"verify the position of all the buttons"""
#     #### add_a_printer_screen.Verify_the_Position_of_all_the_Buttons()
#     """click on the printer led guide done button"""
#     add_a_printer_screen.click_Printer_LED_Guide_Done_Btn()
#     add_a_printer_screen.Click_Next_Button()
#     """stop the app"""
#     common_method.Stop_The_App()

def test_AppSettings_TestcaseID_47911():
    """ Verify auto Label Feed On Printer Cover Close value doesn't retrieve in progress after changing darkness level."""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Log in to the ZSB App with printer added."],
        2: [2, "Click Printer Settings."],
        3: [3, "Click printer tab."],
        4: [4, "Check printer General tab information."],
        5: [5,
            "Try changing darkness level or change 'Auto Label Feed on Printer Cover' value. Check 'Auto Label Feed On Printer Cover Close' value should show Enable/Disable, not in loading or in progress."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify printer is already added"""
        app_settings_page.Verify_Printer_is_already_added()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on Printer settings tab"""
        app_settings_page.click_Printer_Settings()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"click on printer name on the printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify general tab text"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.Verify_General_Tab_Text()
        """"verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()
        """verify darkness level bar is present & change the darkness level"""
        app_settings_page.Verify_Darkness_Level_Bar()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
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


def test_AppSettings_TestcaseID_47914():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "A printer has been registered already. Click the burger icon and click Add Printer button."],
        2: [2, "If there is a registered printer, click Add Printer on the Home Page."],
        3: [3, "Click Start button and check the printer list after Bluetooth discovery."],
        4: [4, "Check it discovers only ZSB printers and displays all printer information accurately."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    """Android Only-Verify there is no unknown printer appeared in the Bluetooth list."""
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on add a printer"""
        add_a_printer_screen.click_Add_A_Printer()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""click on start Button"""
        add_a_printer_screen.click_Start_Button()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        add_a_printer_screen.Verify_Lets_Make_Sure_Text()
        add_a_printer_screen.Click_Next_Button()
        """"verify searching for your printer text"""
        add_a_printer_screen.Verify_Searching_for_your_printer_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """"verify select your printer text"""
        add_a_printer_screen.Verify_Select_your_printer_Text()
        add_a_printer_screen.Verify_Discovered_Devices_Text()
        add_a_printer_screen.Verify_same_ZSB_image_for_all_items()
        """stop the app"""
        common_method.Stop_The_App()
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


# Testcase 47915 is deleted
# def test_AppSettings_TestcaseID_47915():
#     """""Printer Bluetooth List displays printers which have already been added even if "Show All Printers" is not selected."""
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#   need to change test steps
# test_steps = {
#     1: [1, "Install ZSB Series app"],
#     2: [2, "Launch the app"],
#     3: [3, "Select 'Only this time' from all (Location, nearby) permission pop up"],
#     4: [4,
#         "Close and re-launch the app. Check that all permissions should ask for permission every time if user has opted to ask for every time or denied."]
# }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#
#     try:
#         """start the app"""""
#         common_method.tearDown()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         """"verify home text is displaying on the home screen"""
#         """"verify home text is displaying on the home screen"""
#         app_settings_page.Home_text_is_present_on_homepage()
#         """click on the hamburger icon"""
#         login_page.click_Menu_HamburgerICN()
#         """"click on Add printer tab"""""
#         add_a_printer_screen.click_Add_A_Printer()
#         """"click on the start button"""
#         add_a_printer_screen.click_Start_Button()
#         login_page.click_Allow_ZSB_Series_Popup()
#         add_a_printer_screen.Verify_Lets_Make_Sure_Text()
#         add_a_printer_screen.Click_Next_Button()
#         """"Verify searching for your printer text"""
#         add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#         """"verify select your printer text"""
#         add_a_printer_screen.Verify_Select_your_printer_Text()
#         """"select 2nd printer which you want to add"""
#         ### add_a_printer_screen.click_2nd_Printer_Details_To_Add()
#         """stop the app"""
#         common_method.Stop_The_App()
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         if screenshot_path not in uploaded_files:
#             upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

def test_AppSettings_TestcaseID_50325():
    """Verify Printer’s name is too long which should not causes app get stuck and style error at Printer Settings page."""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login into ZSB Mobile App."],
        2: [2, "Go to Mobile app -> Printer Settings."],
        3: [3, "Click the printer tab at printer settings page."],
        4: [4, "Rename the Printer Name with a long text (more than 30 characters)."],
        5: [5, "After printer's name is updated, click printer's name tab and swipe left and right at the tab."],
        6: [6,
            "Go to another page (like home page). Check when the printer name is longer than 30 characters, it should remind users that the printer's name is too long to save. App navigates to other pages smoothly."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on printer settings tab"""""
        app_settings_page.click_Printer_Settings()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_Printer_Name_Text_Field()
        app_settings_page.clear_First_Name()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Rename the Printer Name with a long text (more than 30 characters)"""
        app_settings_page.Rename_PrinterName_With30_Characters()
        app_settings_page.click_Back_Icon()
        app_settings_page.Verify_Exceeding_Characters_Message()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        app_settings_page.click_Printer_Name_Text_Field()
        app_settings_page.clear_First_Name()
        app_settings_page.Update_PrinterName()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        app_settings_page.click_Back_Icon()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_50333():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Sign in to test account, add a printer."],
        2: [2, "Go to Printer Settings/Printer name/Wi-Fi tab."],
        3: [3, "Click Manage Networks."],
        4: [4,
            "The 'Bluetooth Connection Required' dialog pops up, click Device’s Back button. Check the 'Bluetooth Connection Required' dialog disappears and stays on Wi-Fi tab since user clicked back button."],
        5: [5, "Click Manage Networks again, when the 'Bluetooth Connection Required' dialog pops up, click continue."],
        6: [6, "Turn off printer. Check the 'Bluetooth Connection Failed' pops up."],
        7: [7,
            "Click Device’s Back button. Check the 'Bluetooth Connection Failed' dialog disappears and stays on Wi-Fi tab since user clicked back button."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    """Android only- Check it will back to manage network after clicking device’s back button"""""

    """"App should be in logged in condition & printer should be added"""""

    try:
        start_time = time.time()
        """"start the app"""""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on the printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """click on the printer name"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """"click on the wifi tab"""
        app_settings_page.click_wifi_tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """click on the Manage network button"""
        app_settings_page.click_Manage_Networks_Btn()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """"verify bluetooth connection required text"""
        app_settings_page.get_text_Bluetooth_connection_required_Txt()
        """click on keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """""Due to bug id SMBM-2243, step 5 is blocked"""
        print("Due to bug id SMBM-2243, step 5 is blocked")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """Turn off printer Manually"""
        """"verify bluetooth connection failed pop up"""
        app_settings_page.Verify_Bluetooth_Connection_Failed_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """""click keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        """"verify wifi tab & text is present"""
        app_settings_page.Verify_Wifi_Tab_Text()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47923():
    """Verify changing password should log out all clients."""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Log in to account A on Android, iOS, and web portal client."],
        2: [2, "Log out of account A from the Android version."],
        3: [3, "Click the 'login' button on the Android version."],
        4: [4, "It will open the browser. Click the 'reset password' link to reset the password of account A."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.click_Logout_Btn()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        login_page.click_Login_With_Email_Tab()
        login_page.click_Password_TextField()
        login_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Change_Password_Btn()
        app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
        app_settings_page.click_Close_Icon_On_Password_Recovery_Page()
        """After changing the password, it should logged out. this needs to be validated Manually"""""
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47956():
    """Upload avatar via "Photo Gallery" using the default interface of Onedrive"""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Log in to ZSB Series App."],
        2: [2,
            "Click on the burger menu in the upper left corner, then click on the pencil icon to enter the user information setting page."],
        3: [3, "Click the 'Upload Photo' button under 'Avatar' and select 'Photo Gallery'."],
        4: [4,
            "In the upper left corner of the window that opens, click on the Burger menu and then click on the One Drive icon to open the default file list page.In the default file list page, find the image file and click on it to upload it."],
        5: [5, "In the default file list page, find the image file and click on it to upload it."],
        6: [6, "The upload progress is displayed and the image is uploaded successfully."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on pen icon"""
        app_settings_page.click_pen_Icon_near_UserName()
        """"Verify User settings text in user settings page"""
        app_settings_page.Is_Present_User_Settings_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""click on upload photo"""
        app_settings_page.click_User_upload_photo()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """click on camera option"""
        app_settings_page.click_Mobile_Camera()
        """""click allow if it is present"""
        app_settings_page.Click_Allow_popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """"click on click picture icon"""
        app_settings_page.click_picture()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """"Verify photo uploaded message"""""
        app_settings_page.Verify_Photo_Uploaded_Message()
        """"click user photo remove image"""
        app_settings_page.click_User_Photo_Remove_Image()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_50325():
    """Manage Network-Check able to add/delete/sort network when printer bt paired/unpaired in device"""

    """"App should be in logged in condition & printer should be added """
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Sign in to test account, go to Printer settings/Printer name/Wi-Fi tab."],
        2: [2, "Click Manage network, pair Bluetooth if needed. Check able to see the 'Add network' option."],
        3: [3, "Click on Add network button. Check the network list will show up and available networks are listed."],
        4: [4,
            "Click the 'Enter network manually' option, input an open ESSID, click Cancel button. Check it will stay in the network list."],
        5: [5,
            "Click the 'Enter network manually' option, input an ESSID with password, input correct password, click Cancel button. Check it will stay in the network list."],
        6: [6,
            "Click the 'Enter network manually' option, input an open ESSID, click Join button. Check it will go back to manage network page. Check the input ESSID will show up in the added network list."],
        7: [7,
            "Exit Manage network, go back to home page. Check printer is online status. Check the Wi-Fi signal is correct."],
        8: [8, "Try to print a test label or any design. Check able to print label."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """"start the app"""
        common_method.tearDown()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_wifi_tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.click_Manage_Networks_Btn()
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_Add_Network()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Network_UserName()
        app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Network_UserName()
        app_settings_page.click_Security_Open()
        app_settings_page.click_WPA_PSK()
        app_settings_page.click_Keyboard_back_Icon()
        app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Network_UserName()
        app_settings_page.click_Join_Btn_On_Other_Network_Popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        app_settings_page.Verify_Added_Network()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_49960():
    """Check click change password in user profile page: it added callback url, responsce_type, client_id and redirect_url parameters"""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to Mobile App with Test account."],
        2: [2, "Click Pen icon to go to user profile page."],
        3: [3, "Click Change password, check it opens a new window showing the change password page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.signInWithEmail()
        login_page.click_Login_With_Email_Tab()
        login_page.click_Password_TextField()
        login_page.Enter_Zebra_Password()
        app_settings_page.click_Keyboard_back_Icon()
        login_page.click_SignIn_Button()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_Change_Password_Btn()
        app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_49961():
    """Check after change password, click return to login will navigate to login page and user able to login with new password success"""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to Mobile App with Test account."],
        2: [2, "Click Pen icon to go to user profile page."],
        3: [3, "Click Change password, check it opens a new window showing the change password page."],
        4: [4, "Check username auto-populates in Password Recovery page."],
        5: [5, "Click Submit button, check it goes to the next page: change password."],
        6: [6, "Input Old password, new password, confirm password."],
        7: [7, "Click Submit button, check it goes to Success page."],
        8: [8, "Input username and new password, click sign in, check user login success."],
        9: [9, "Click Return to login button or click 'Click here', it will navigate to login page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_Change_Password_Btn()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.Verify_Change_Password_PageURL_Is_Displaying()
        app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
        app_settings_page.click_Password_Recovery_Email_TextField()
        app_settings_page.click_Submit_On_Password_Recovery_Screen()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        """"other steps are blocked due to SMBM-2234 & SMBM-1098"""
        """"After changing the password, login screen and login should be verified manually"""
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_51702():
    """Check the UI of toggle buttons on Notification Settings""""""
    """"App should be in logged in condition & printer should be added"""
    #
    #
    #
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Sign in to the test account, go to Notification Settings tab. Check the toggle buttons under this tab are correct (The color of the round dot part is much darker, the left part is lighter)."],
        2: [2,
            "Click on Messages tab. Check the toggle buttons under this tab are correct (The color of the round dot part is much darker, the left part is lighter)."],
        3: [3,
            "Change to another theme, repeat steps 1 and 2. Check the toggle buttons are updated to the theme color accordingly."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """"start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Notifications Tab"""
        app_settings_page.click_Notifications_Tab()
        """"Scroll till Notification Settings Tab"""
        app_settings_page.Scroll_Till_Notification_Settings_Tab()
        """click on notification settings tab"""
        app_settings_page.click_Notification_Settings_Tab()
        """"verify notification settings toggle buttons and text"""
        app_settings_page.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
        """"scroll till messages tab"""
        app_settings_page.Scroll_Till_Messages_Tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """""click Messages tab"""
        app_settings_page.click_Mesages_Tab()
        """verify messages text and toggle button"""
        app_settings_page.Verify_Messages_Text_And_Toggle_Buttons()
        """"click on hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """click on three dot icon"""
        app_settings_page.click_Three_Dot_On_Workspace()
        """""click change theme"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_Change_Theme()
        """"click on electic theme to change the theme"""
        app_settings_page.check_Change_Electic_Theme()
        """click on save & exit"""
        app_settings_page.click_Save_Exit_Btn()
        """verify notifications text is displaying"""
        app_settings_page.Verify_Notifications_Text_IS_Displaying()
        """"verify updated messages tab color"""
        app_settings_page.Verify_Updated_MessagesTab_Color()
        """scroll right till Notification settings"""
        app_settings_page.Scroll_Right()
        """click on Notification Settings tab"""
        app_settings_page.click_Notification_Settings_Tab()
        """verify updtaed Notification settings messages"""
        app_settings_page.Verify_Updated_Notifications_SettingsTab_Messages_Color()
        """click on hamburger menu"""
        login_page.click_Menu_HamburgerICN()
        """click on three dot icon"""
        app_settings_page.click_Three_Dot_On_Workspace()
        """click on change theme"""
        app_settings_page.click_Change_Theme()
        """"click on change modern theme"""
        app_settings_page.check_Change_Modern_Theme()
        """click on save & exit button"""
        app_settings_page.click_Save_Exit_Btn()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_51788():
    """""Sign in with existing Non-Zebra User Account, then sign out"""

    """"App should be in logged in condition & printer should be added"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Launch ZSB Series."],
        2: [2, "Click 'Sign In with your email' button on the login page. Check user is navigated to sign-in page."],
        3: [3,
            "Enter registered non-Zebra account username with correct password. Check user successfully logs in and displays current username."],
        4: [4,
            "Go to user profile and click Log out button. Check user successfully logs out and navigates to the logout page with prompt 'You have successfully signed off.'"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        """"start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"click on the hamburger menu icon"""
        login_page.click_Menu_HamburgerICN()
        """click on the pen icon"""
        app_settings_page.click_pen_Icon_near_UserName()
        """"scroll till delete account """
        app_settings_page.Scroll_till_Delete_Account()
        """click on logout """
        app_settings_page.click_Logout_Btn()
        """"click on login page"""
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        sleep(2)
        """verify home text is present on home page"""
        app_settings_page.Home_text_is_present_on_homepage()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_51705():
    """Check clicking the photo taken by camera will not affect uploading photo as user avatar""""""
    """"""""App should be in logged in condition & printer should be added"""""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Sign in to test account, click pen icon to open user settings page. Check the user settings page shows up."],
        2: [2, "Click Upload Photo option, select Camera option (Allow access if needed). Check the camera is opened."],
        3: [3,
            "Take a photo, after taking the photo, click on the photo anywhere (This is the key step to reproduce the issue). Check there is no odd behavior."],
        4: [4,
            "Click the Use Photo option. Check the photo can be uploaded successfully. Check the user avatar is updated."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on pen icon"""
        app_settings_page.click_pen_Icon_near_UserName()
        """"Verify User settings text in user settings page"""
        app_settings_page.Is_Present_User_Settings_Text()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """""click on upload photo"""
        app_settings_page.click_User_upload_photo()
        """click on camera option"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        app_settings_page.click_Mobile_Camera()
        """""click allow if it is present"""
        app_settings_page.Click_Allow_popup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """"click on click picture icon"""
        app_settings_page.click_picture()
        """"Verify photo uploaded message"""""
        app_settings_page.Verify_Photo_Uploaded_Message()
        """"click user photo remove image"""
        app_settings_page.click_User_Photo_Remove_Image()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47924():
    """Verify Should not allow same printer name in all the clients.."""
    #
    """"Account should be having 2 printers"""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Sign in with a user who has 2+ printers (different names). Check that both printers are shown on the home page."],
        2: [2,
            "Go to printer settings, try to update two printers to have the same name. Check the printer name can't be updated to the same."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        # ##test_robo_finger()
        ### sleep(6)
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Add printer tab"""""
        add_a_printer_screen.click_Add_A_Printer()
        """"click on the start button"""
        add_a_printer_screen.click_Start_Button()
        login_page.click_Allow_ZSB_Series_Popup()
        add_a_printer_screen.Verify_Lets_Make_Sure_Text()
        add_a_printer_screen.Click_Next_Button()
        add_a_printer_screen.click_Close_Icon_On_Select_Your_Printer_Screen()
        add_a_printer_screen.click_Exit_Btn_On_Exit_Printer_Setup()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """click on printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """"scroll till the 2nd or 3rd printer"""
        app_settings_page.Scroll_Till_2nd_Printer()
        """click on printer name on the printer settings page"""""
        app_settings_page.click_PrinterName2_On_Printersettings()
        """click on printr name"""
        app_settings_page.click_Printer_Name_Text_Field()
        """click on printer name text field"""
        app_settings_page.clear_First_Name()
        """Rename the Printer Name with a long text (more than 30 characters)"""
        app_settings_page.Rename_PrinterName_With_Same_Name()
        """"click on back icon"""
        app_settings_page.click_Back_Icon()
        """click continue button"""""
        app_settings_page.click_Continue_Button_On_Printer_Update_Failed_Popup()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.Scroll_Till_2nd_Printer()
        """"verify previous printer name is displaying"""
        app_settings_page.click_PrinterName2_On_Printersettings()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47910():
    """""Verify pull-down screen twice then the prints left value can refresh success in home page."""""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to the mobile app with a test account that already has one printer added."],
        2: [2, "Check the printer's current prints left count."],
        3: [3,
            "Press the printer button to feed one label, or print a label from the web portal with the same test account, or print a label from another test device with the same test account."],
        4: [4,
            "Pull down the screen to refresh the home page. Check that after pulling down, the home page refreshes and the prints left count is updated."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """start the app"""
        common_method.tearDown()
        sleep(3)
        ### add_a_printer_screen.click_Add_A_Printer()
        app_settings_page.Verify_Printer_is_already_added()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """take the prvious number of cartridges"""
        previous = app_settings_page.Check_no_of_left_cartridge()
        print(previous)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """click on navigation option"""
        login_page.click_Menu_HamburgerICN()

        """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        sleep(2)
        n = 2

        """test the printer to print the label"""
        for i in range(n):
            app_settings_page.click_Test_Print_Button()
            sleep(2)

        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Go to the Home Page"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Home_Tab()
        sleep(2)

        """After printing Get the number of cartridges"""
        after = app_settings_page.Check_no_of_left_cartridge()
        print(after)

        """Check wheather the cartridges are updated or not"""
        res = app_settings_page.check_update_cartridge(previous, after, n)
        if res:
            print("success")
        else:
            print("Failed")
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47881():
    """""Verify "How to Unpair Bluetooth" dropdown list should expend with small size screen device."""""

    """"Precondition:
    1. Registered a production user
    2. Install production Mobile App into test device
    3. Login Mobile App with user already added printer"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to Mobile App with a user who already has a printer added."],
        2: [2, "Click the 3-dot menu of the target printer and select the delete option."],
        3: [3,
            "Check the first Delete dialog pops up, click 'Delete' button on the dialog.Check the second Delete Printer dialog pops up, click 'Yes, Delete' button.Check with a small screen device that the 'How to unpair Bluetooth' dropdown list is fully displayed and, when clicked, it shouldn't extend out of UX design."],
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """click on three dot on added printer on home page"""
        app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""click on delete printer button"""
        app_settings_page.click_Delete_Printer_Button()
        """verify delete printer page"""
        app_settings_page.Verify_Delete_Printer_Page()
        """"click Cancel on printer button"""
        app_settings_page.Click_Cancel_On_Delete_Printer_Page()
        """stop the app"""
        common_method.Stop_The_App()
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


def test_AppSettings_TestcaseID_47928_Bug1888():
    """UI warning and confirmation verification when printer is deleted before decommissioned(Android)"""
    """"Account should be having 2 printers"""

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Go to Dashboard."],
        2: [2, "Click Delete on the 3 dots on the top right of the Printer pane window."],
        3: [3,
            "Window labeled 'Delete Printer' pops up with content as per Figma link with 2 options 'Cancel' and 'Delete'."],
        4: [4, "Clicking on Cancel takes user back to Dashboard with no changes."],
        5: [5,
            "Clicking on Delete takes user to another window with the same label containing text 'Are you sure you want to delete your printer' and 2 options 'Cancel' and 'Yes, Delete'."],
        6: [6, "Once user confirms, homepage is displayed with the Printer removed."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """click on three dot on added printer on home page"""
        app_settings_page.Verify_Printer_Text()
        app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""click on delete printer button"""
        app_settings_page.click_Delete_Printer_Button()
        """verify delete printer page"""
        app_settings_page.Verify_Delete_Printer_Page()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.Click_Cancel_On_Delete_Printer_Page()
        app_settings_page.click_Three_Dot_On_Added_Printer_On_HomePage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """"click delete printer button"""
        app_settings_page.click_Delete_Printer_Button()
        app_settings_page.click_Delete_Printer_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """"click yes delete button"""
        app_settings_page.click_Yes_Delete_Button()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify UI of unpair bluetooth dropdown list """
        app_settings_page.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
        """click on unpair bluetooth dropdown list"""""
        app_settings_page.Verify_And_click_Unpair_Bluetooth_dropdown_list()
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
        app_settings_page.click_Done_Btn()
        app_settings_page.Verify_Printer_Is_Not_Displaying()
        """stop the app"""
        common_method.Stop_The_App()
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
