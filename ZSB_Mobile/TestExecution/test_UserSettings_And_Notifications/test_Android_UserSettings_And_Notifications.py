# from poco import poco
import time
import self
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import poco
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
from ...Common_Method import *
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Social_Login.Social_Login import Social_Login
# from ZSB_Mobile.sphere_db import *
import pytest
import os
from ...TestSuite.store import *
from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_UserSettings_And_Notifications.store import execID, leftId
import inspect

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method = Common_Method(poco)
social_login = Social_Login(poco)
registration_page = Registration_Screen(poco)
aps_notification = APS_Notification(poco)
app_settings_page = App_Settings_Screen(poco)

ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()
start_execution_loop(execID)


def test_Notifications_TestcaseID_45794():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Slide the left slide page to choose 'Notifications' item. Check it goes to the 'Notifications' page. Check it displays all notifications generated on setup."],
        2: [2,
            "Click one notification item. Check it displays the 'Dismiss' button under the clicked notification item."],
        3: [3, "Click 'Dismiss' button. Check the notification is dismissed."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.Clear_App()
        common_method.tearDown()

        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        login_page.click_loginBtn()
        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Continue with Google")

        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        login_page.Loginwith_Added_Email_Id()
        social_login.wait_for_element_appearance("Home", 30)
        sleep(2)

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        others.click_Testprint()
        app_settings_page.Verify_Printed_Successfully_Text()
        sleep(2)
        others.click_Testprint()
        app_settings_page.Verify_Printed_Successfully_Text()
        sleep(2)

        """Generate less than 5 notifications"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        others.click_notifications_button()
        sleep(3)
        others.click_down_arrow_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        others.click_dismiss_printer_notification()
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


def test_UserSettings_TestcaseID_45796():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Click the hamburger button at the left corner to open the left slide page."],
        2: [2,
            "Click the pen icon at the left slide page to go to the settings page. Check the head icon of the account only displays the default picture. Check there is no 'Remove Image' link next to the button 'Upload Photo' on the page."],
        3: [3,
            "Click the 'Upload Photo' button. Check it appears with 2 options at the bottom: 'Photo Gallery' and 'Camera'."],
        4: [4,
            "Click 'Photo Gallery'. Check it pops up the system dialog '\"ZSB Series\" Would like to Access your Photos' with 2 buttons 'Allow' or 'Deny' (iOS's dialog is different from Android, but they express the same meaning)."],
        5: [5,
            "Choose one picture to upload. Check the picture of the account at the settings page and at the slide left page is updated. Check other platforms' account picture is updated. Check there is a 'Remove Image' link next to the button 'Upload Photo' on the page."],
        6: [6,
            "Go to the settings page and click 'Remove Image'. Check the picture of the account at the settings page and at the slide left page is changed to the default picture. Check other platforms' account picture is changed to the default picture."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.Stop_The_App()
        common_method.Start_The_App()
        app_settings_page.Home_text_is_present_on_homepage()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        others.click_on_profile_edit()

        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")

        res = others.check_remove_image_button_exists()
        if res:
            raise Exception("Remove image button found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        others.click_upload_photo()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        others.select_photo_gallery()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        others.select_first_image_from_gallery()
        sleep(3)
        res = others.verify_default_image()
        if res:
            raise Exception("default image found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        res = others.check_remove_image_button_exists()
        if not res:
            raise Exception("Remove image button not found")

        others.click_remove_image_button()
        sleep(2)
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")
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


def test_UserSettings_TestcaseID_45797():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Sign in to the test account in the app."],
        2: [2, "Click the hamburger button at the left corner to open the left slide page."],
        3: [3,
            "Click the pen icon on the left slide page to go to the settings page. Check the head icon of the account only displays the default picture. Check there is no 'Remove Image' link next to the 'Upload Photo' button."],
        4: [4,
            "Click the 'Upload Photo' button. Check it appears with 2 options at the bottom: 'Photo Gallery' and 'Camera'."],
        5: [5,
            "Click 'Camera'. Check it pops up the system dialog '\"ZSB Series\" Would like to Access the Camera' with 2 buttons 'OK' or 'Don't Allow' (iOS's dialog is different from Android, but they express the same meaning)."],
        6: [6, "Click 'OK' button of the dialog. Check it opens the camera app."],
        7: [7, "Take a photo. Check it appears with 2 buttons 'Retake' and 'Use Photo'."],
        8: [8,
            "Click 'Retake' button to take a photo again. Check it appears with 2 buttons 'Retake' and 'Use Photo'."],
        9: [9,
            "Click 'Use Photo' button. Check the picture of the account at the settings page and at the slide left page is updated. Check other platforms' account picture is updated. Check there is a 'Remove Image' link next to the 'Upload Photo' button."],
        10: [10,
             "Go to the settings page and click 'Remove Image'. Check the picture of the account at the settings page and at the slide left page is changed to the default picture. Check other platforms' account picture is changed to the default picture."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.tearDown()
        app_settings_page.Home_text_is_present_on_homepage()
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        others.wait_for_element_appearance("Home", 30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        others.click_on_profile_edit()

        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")

        res = others.check_remove_image_button_exists()
        if res:
            raise Exception("Remove image button found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        others.click_upload_photo()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        others.select_camera()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        try:
            res = others.verify_text_camera_permission()
            if res:
                print("ok")
            else:
                pass
            others.click_allow()
        except:
            try:
                others.click_allow()
            except:
                pass
        sleep(1)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        others.capture_the_image_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        others.retake_the_image_button()
        others.capture_the_image_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # ----------------------
        # Step 9
        start_time = time.time()
        others.use_the_image_button()

        sleep(3)
        res = others.verify_default_image()
        if res:
            raise Exception("default image found")

        res = others.check_remove_image_button_exists()
        if not res:
            raise Exception("Remove image button not found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        others.click_remove_image_button()
        sleep(2)
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")
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


def test_UserSettings_TestcaseID_45798():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Open the app and login."],
        2: [2, "Click the hamburger button at the left corner to open the left slide page."],
        3: [3, "Click the pen icon on the left slide page to go to the settings page."],
        4: [4,
            "Click the 'Upload Photo' button. Check it appears with 2 options at the bottom: 'Photo Gallery' and 'Camera'."],
        5: [5,
            "Click 'Photo Gallery'. Check it pops up the system dialog '\"ZSB Series\" Would like to Access your Photos' with 2 buttons 'Allow' or 'Deny' (iOS's dialog is different from Android, but they express the same meaning)."],
        6: [6,
            "Click 'Deny' button of the dialog. Check the system dialog disappears. Check it doesn't open the file window."],
        7: [7, "Repeat step 4 and 5, and click 'Allow' button. Check it opens the file window."],
        8: [8,
            "Click 'Cancel' button for iOS or hit the 'back' physical button for Android. Check it goes back to the app. Check the account picture wasn't changed."],
        9: [9,
            "Repeat step 4 and click the 'Camera' button. Check it pops up the system dialog '\"ZSB Series\" Would like to Access the Camera' with 2 buttons 'OK' or 'Don't Allow' (iOS's dialog is different from Android, but they express the same meaning)."],
        10: [10,
             "Click 'Don't Allow' button of the system dialog. Check the system dialog disappears. Check it doesn't open the camera app."],
        11: [11,
             "Repeat step 4 and click the 'Camera' button and click 'OK' button of the system dialog. Check it opens the camera."],
        12: [12,
             "Click 'Cancel' button for iOS or hit the 'back' physical button for Android. Check it goes back to the app. Check the account picture wasn't changed."]
    }
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        """has bug id:SMBM-2711"""

        common_method.tearDown()
        try:
            app_settings_page.Home_text_is_present_on_homepage()
            login_page.click_Menu_HamburgerICN()
            others.click_on_profile_edit()
            others.scroll_down()
            others.click_log_out_button()
        except:
            pass

        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()

        others.wait_for_element_appearance("Home", 30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Click on the profile edit"""
        others.click_on_profile_edit()

        """verify the default image"""
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """select upload photo gallery"""
        others.click_upload_photo()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """select photo gallery"""
        others.select_photo_gallery()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        others.go_back()
        sleep(1)
        others.go_back()
        sleep(2)

        """verify the default image"""
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Select Camera upload"""
        others.click_upload_photo()
        others.select_camera()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        try:
            others.dont_allow_permission()
        except:
            pass
        try:
            others.click_upload_photo()
        except:
            pass
        others.go_back()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        try:
            others.select_camera()
        except:
            raise Exception("dint redirect to the previous page or dint ask for the permission")
        try:
            others.click_allow()
        except:
            pass
        others.go_back()

        """verify the default image"""
        try:
            res = others.verify_default_image()
            if not res:
                raise Exception("default image not found")
        except:
            others.go_back()
            res = others.verify_default_image()
            if not res:
                raise Exception("default image not found")
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


def setup_logout():
    common_method.tearDown()

    try:
        others.wait_for_element_appearance("Sign In", 10)
    except:
        pass

    try:
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
    except:
        pass
    sleep(2)


def test_Notifications_TestcaseID_45795():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Slide the left slide page to choose 'Notifications' item. Check it goes to the 'Notifications' page. 'No notifications' text is displayed if there is no notification. Check it displays all notifications generated before."],
        2: [2,
            "Reopen the app, then go to the 'Notifications' page again. Check it still displays all notifications generated before."],
        3: [3,
            "Relogin to the account, then go to the 'Notifications' page again. Check it still displays all notifications generated before."],
        4: [4,
            "Delete the app and reinstall it, then go to the 'Notifications' page again. Check the notification items are dismissed."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.tearDown()
        others.wait_for_element_appearance("Home", 10)
        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()
        Android_notification = others.get_notifications_in_first_page_android()
        sleep(3)

        common_method.tearDown()

        others.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification_after_closing_app = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification, Android_notification_after_closing_app)

        if not res:
            raise Exception("Notifications did match appear after reopening the app")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        others.wait_for_element_appearance("Home", 30)
        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()
        Android_notification_after_logout = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification, Android_notification_after_logout)
        if not res:
            raise Exception("Notifications are not same after log out")

        #####others.uninstall_and_install_zsb_series_on_google_play()
        ##### others.open_the_zsb_series_app_in_play_store()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        common_method.Clear_App()
        common_method.Start_The_App()
        others.wait_for_element_appearance("Sign In", 10)
        others.check_allow_permission_for_location()
        registration_page.clickSignIn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        others.wait_for_element_appearance("Home", 30)
        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()
        Android_notification_after_deleting_app = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification, Android_notification_after_deleting_app)
        if res:
            raise Exception("Notifications did not disappear after deleting the app")
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


# ##-------------------------------------------------------------------------------------

def test_Notifications_TestcaseID_53234():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Click on the left side hamburger menu from Home page."],
        2: [2, "Navigate to Notifications Page and check all the fonts in the notification history."],
        3: [3, "Check all the fonts in the Notification Settings page and Messages tab."],
        4: [4, "Change the toggle buttons displayed in the Notification Settings page and Messages tab."],
        5: [5, "Revert the toggle buttons and check they can be changed back to the previous value (Enabled/Disabled)."]
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
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """"click on Notifications Tab"""
        app_settings_page.click_Notifications_Tab()
        """"Scroll till Notification Settings Tab"""
        app_settings_page.Scroll_Till_Notification_Settings_Tab()
        """click on notification settings tab"""
        app_settings_page.click_Notification_Settings_Tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """"verify notification settings toggle buttons and text"""
        app_settings_page.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
        """"scroll till messages tab"""
        app_settings_page.Scroll_Till_Messages_Tab()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """""click Messages tab"""
        app_settings_page.click_Mesages_Tab()
        """verify messages text and toggle button"""
        app_settings_page.Verify_Messages_Text_And_Toggle_Buttons()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """"click on hamburger icon"""
        app_settings_page.Disable_And_Enable_Toggle_Buttons()
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


# def test_Others_TestcaseID_53232():
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, "Click on the left side hamburger menu from Home page."],
#         2: [2, "Navigate to My Designs and check all design names are displayed in bold with the new font style."],
#         3: [3,
#             "Click on the Search button and enter matched text to search. Check all fonts in the search box and results found are displayed with the new font style."],
#         4: [4,
#             "Click on the Search button and enter non-matched text to search. Check all fonts in the search box and 'No results found' (Description) are displayed with the new font style."],
#         5: [5, "Check 'Showing \"n\" Designs' is displayed in bold."],
#         6: [6,
#             "Select any design from My Designs and check all four options (Print/Rename/Duplicate/Delete) are displayed with the new font style."],
#         7: [7, "Click on Print and check all fonts in the print preview page are displayed with the new font style."],
#         8: [8,
#             "Click on Print from the print preview page and check the notification pops up at the top of the page with the new font style."]
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#     try:
#         start_time = time.time()
#         """"start the app"""
#         common_method.tearDown()
#         login_page.click_LoginAllow_Popup()
#         login_page.click_Allow_ZSB_Series_Popup()
#         """click on the hamburger icon"""
#         login_page.click_Menu_HamburgerICN()
#         """"click on Notifications Tab"""
#         app_settings_page.click_Notifications_Tab()
#         app_settings_page.Verify_Generated_Notification()
#         app_settings_page.Expand_And_Verify_Printername_AndType()
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


def test_UserSettings_TestcaseID_45800():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login to the test account."],
        2: [2,
            "Go to User Account Profile Page, check there is no error message on the user settings page (Due to bug SMBM-1295)."],
        3: [3,
            "Update 'First Name' and 'Last Name' to some valid values. Check that user can update these successfully."],
        4: [4, "Change Password. Check that user can change the password successfully."],
        5: [5, "After changing password successfully, click here to sign in. Check it returns to the login page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()

        common_method.tearDown()
        common_method.Clear_App()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        login_page.click_Login_With_Email_Tab()
        login_page.click_Password_TextField()
        login_page.Enter_Zebra_Password()
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
        app_settings_page.click_First_Name_Text_Field()
        """"clear first name field"""
        sleep(3)
        app_settings_page.clear_First_Name()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """""Update first name with valid names"""
        app_settings_page.Update_Default_First_Name()
        sleep(3)
        poco.scroll()
        """""click last name text field"""
        app_settings_page.click_Last_Name_Text_Field()
        """"clear Last name field"""
        app_settings_page.clear_Last_Name()
        """""Update last name with valid names"""
        app_settings_page.Update_Default_Last_Name()
        sleep(3)
        """""click keyboard back icon"""
        app_settings_page.click_Keyboard_back_Icon()
        """"verify the updated names message"""
        app_settings_page.verify_Your_changes_have_been_saved_Message()
        sleep(3)
        app_settings_page.Scroll_till_Delete_Account()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        app_settings_page.click_Change_Password_Btn()
        app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
        app_settings_page.click_Close_Icon_On_Password_Recovery_Page()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        app_settings_page.Enter_Password()
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

# #####----------------------------------------------------------------------------------------------
