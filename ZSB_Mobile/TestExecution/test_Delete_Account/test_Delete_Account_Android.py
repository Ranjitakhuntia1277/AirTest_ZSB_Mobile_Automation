from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen

import pytest
from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_Delete_Account.store import execID, leftId
import inspect


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
delete_account_page = Delete_Account_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
device_network_page = Device_Networks_Android(poco)

ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()

start_execution_loop(execID)


def test_delete_account_testcase_id_45760():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login to the Mobile App'],
        2: [2, 'On the home page, click the pen icon to go to the user settings page'],
        3: [3,'Check that the "Delete Account" button is displayed next to the "Logout" button at the bottom of the page'],
        4: [4,'Click the "Delete Account" button\nVerify that the "Delete Account" page appears\nAcknowledge the three required items before proceeding'],
        5: [5,'Click the "X" button\nCheck that the "Delete Account" page closes and the user settings page is displayed'],
        6: [6, 'Click the "Delete Account" button again\nVerify that the "Delete Account" page appears again'],
        7: [7, 'Click the "X" button and log out'],
        8: [8, 'Re-login to the Mobile App\nCheck that the user can log in without issues']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Close Delete Account pop up dialog"""
        delete_account_page.clickCloseButtonInDeleteAccountPage()
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        delete_account_page.clickCloseButtonInDeleteAccountPage()
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        app_settings_page.Home_text_is_present_on_homepage()
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


def test_delete_account_testcase_id_45761():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    test_steps = {
        1: [1, 'Login Mobile App'],
        2: [2, 'In home page, click pen icon go to user setting page'],
        3: [3, 'Check on the bottom of the page, "Delete Account" button show next to Logout button'],
        4: [4,'Click "Delete Account" button, check Delete Account page show up\nThere are 3 items need acknowledge and checked then can continue'],
        5: [5, 'Check 3 checkbox and click continue button'],
        6: [6,'Check mobile app will auto logout and show login screen with notice information:\nImportant: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.'],
        7: [7, 'Click Login button and input test user name and password click sign in button'],
        8: [8,'User login successfully and show User setting page and Delete Account Dialog pop up ask Final confirm user delete']
    }
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        app_settings_page.Home_text_is_present_on_homepage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        while not poco("Log Out").exists():
            poco.scroll()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """9. Click X button to close the Delete account dialog - no X button."""
        data_sources_page.clickCancel()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Check if user is in settings page after closing Delete Account dialog"""
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        registration_page.click_log_out_button()
        common_method.wait_for_element_appearance("Sign In")
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception(
                "Delete account dialog popped up after canceling delete account and re-loging into the same account.")
        except Exception as e:
            pass
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        # -----------------------------------------
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


def test_delete_account_testcase_id_45762():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Mobile App'],
        2: [2, 'In home page, click pen icon go to user setting page'],
        3: [3, 'Check on the bottom of the page, "Delete Account" button show next to Logout button'],
        4: [4,'Click Delete Account button, check Delete Account page show up\nThere are 3 items need acknowledge and checked then can continue'],
        5: [5, 'Click Cancel button check Delete Account page closed and show user setting page'],
        6: [6, 'Click Delete Account button again, check Delete Account page show up again'],
        7: [7, 'Click Cancel button and logout'],
        8: [8, 'Re-login Mobile App check user can login without issue']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Close Delete Account pop up dialog"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        delete_account_page.clickCloseButtonInDeleteAccountPage()
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        """Click Delete Account"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        delete_account_page.clickCloseButtonInDeleteAccountPage()
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        registration_page.click_log_out_button()
        common_method.wait_for_element_appearance("Sign In")
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        app_settings_page.Home_text_is_present_on_homepage()
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


def test_delete_account_testcase_id_45763():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Mobile App'],
        2: [2, 'In home page, click pen icon go to user setting page'],
        3: [3, 'Check on the bottom of the page, "Delete Account" button show next to Logout button'],
        4: [4,'Click "Delete Account" button, check Delete Account page show up\nThere are 3 items need acknowledge and checked then can continue'],
        5: [5, 'Check 3 checkbox and click continue button'],
        6: [6,'Check mobile app will auto logout and show login screen with notice information:\nImportant: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.'],
        7: [7, 'Click Login button and input test user name and password click sign in button'],
        8: [8,'User login successfully and show User setting page and Delete Account Dialog pop up ask Final confirm user delete'],
        9: [9, 'Click Cancel button on the Delete account dialog'],
        10: [10, 'Check the dialog dismiss and user keep stay in account setting page.'],
        11: [11, 'Logout account and re-login, check Delete account dialog not pop up anymore.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        """Login Again"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """9. Click X button to close the Delete account dialog - no X button."""
        data_sources_page.clickCancel()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Check if user is in settings page after closing Delete Account dialog"""
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        registration_page.click_log_out_button()
        common_method.wait_for_element_appearance("Sign In")
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception(
                "Delete account dialog popped up after canceling delete account and re-loging into the same account.")
        except Exception as e:
            pass
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


def test_delete_account_testcase_id_45764():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Mobile App'],
        2: [2, 'In home page, click pen icon go to user setting page'],
        3: [3, 'Check on the bottom of the page, "Delete Account" button show next to Logout button'],
        4: [4,'Click "Delete Account" button, check Delete Account page show up\nPlease acknowledge the following to continue (with 3 checkbox):\n- All data in your workspace will be removed\n- Your account will be de-identified, meaning it will not be associated with you\n- Ensure your printer is On to factory reset your ZSB Printer\nFor your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select "Continue" to sign out.\nEmail: <login email address>\nThere are 2 buttons: Cancel and Continue (Continue button is disabled)\nCheck only if 3 checkboxes all are checked, then Continue button is clickable'],
        5: [5, 'Check 3 checkbox and click continue button'],
        6: [6,'Check mobile app will auto logout and show login screen with notice information:\nImportant: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.'],
        7: [7, 'Click Login button and input test user name and password click sign in button'],
        8: [8,'User login successfully and show User setting page and Delete Account Dialog pop up ask Final confirm user delete'],
        9: [9,'Click Delete button on the Delete account dialog\nCheck Account Deleted dialog pop up: Your account has been successfully deleted'],
        10: [10,'Click OK button on the Account Deleted dialog, Check the account will delete and user auto logout Mobile App and mobile app show Login page']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45769():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with Zebra account"],
        2: [2, "In home page, click pen icon go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button show next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check Delete Account page show up. There are 3 items need acknowledge and checked then can continue"],
        5: [5, "check 3 checkbox and click continue button"],
        6: [6,
            "check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Click Login button and input test user name and password click sign in button"],
        8: [8,
            "User login successfully and show User setting page and Delete Account Dialog pop up ask Final confirm user delete"],
        9: [9,
            "Click Delete button on the Delete account dialog check Account Deleted dialog pop up: Your account has been successfully deleted"],
        10: [10,
             "Click OK button on the Account Deleted dialog, Check the account will delete and user auto logout Mobile App and mobile app show Login page"],
        11: [11, "Click sign button and input the deleted zebra user name and password click Sign in"],
        12: [12, "Check EULA page displayed, scroll all to view EULA and click accept button"],
        13: [13, "Check home page show up, check there is no printer in Home page"],
        14: [14, "Click My Data, check there is no data file in My Data"],
        15: [15, "Click My Designs, check there is no designs in My Designs"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        # data_sources_page.checkIfOnHomePage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        delete_account_page.verifyNoPrinterInAccount()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 14
        start_time = time.time()
        data_sources_page.click_My_Data()
        delete_account_page.verifyMyDataEmpty()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 15
        start_time = time.time()
        data_sources_page.clickMyDesigns()
        delete_account_page.verifyMyDesignsEmpty()
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


def test_delete_account_testcase_id_45780():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that Delete Account page shows up. There are 3 items that need acknowledgment and to be checked before continuing"],
        5: [5, "Check the 3 checkboxes and click the continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Lock device screen for more than 1 hour"],
        8: [8, "Unlock device screen, check that the login page still shows the important notice message"],
        9: [9,
            "Click login button, input test username and password, check that it should pop up a dialog showing that account deletion was expired"],
        10: [10, "Logout user, check on the login page that there is no important message."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        data_sources_page.lock_phone()
        # sleep(3600)
        sleep(30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        wake()
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        delete_account_page.click_Cancel_Btn()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Click Log Out"""
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        delete_account_page.verifyNoImportantMessageOnSignInPage()
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


def test_delete_account_testcase_id_45781():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and to be checked before continuing"],
        5: [5, "Check the 3 checkboxes and click the continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Click Login button, login another user for more than 1 hour then logout, check that the login page still shows the Important message"],
        8: [8,
            "Click login button, input test username and password, check that it should pop up a dialog showing that account deletion was expired. Currently, there is no dialog informing the user the deletion is expired, confirmed with PM, this was WAD."],
        9: [9, "Click OK on the dialog, check that the dialog dismisses and the user is not deleted."],
        10: [10, "Logout user, check on the login page that there is no important message."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        # sleep(3600)
        sleep(30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        delete_account_page.click_Cancel_Btn()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        """Click Log Out"""
        registration_page.click_log_out_button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        try:
            common_method.wait_for_element_appearance(
                "Home", 20)
        except:
            raise Exception("Did not reach home page after login")
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Click Log Out"""
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        delete_account_page.verifyNoImportantMessageOnSignInPage()
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


def test_delete_account_testcase_id_45782():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and to be checked before continuing"],
        5: [5, "Check the 3 checkboxes and click the continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Force quit the app and wait for more than 1 hour"],
        8: [8, "Re-open Mobile App, check that the important information still shows on the login page"],
        9: [9,
            "Click login button, input test username and password, check that a dialog pops up showing that the delete user session was expired. Currently, there is no dialog informing the user the deletion is expired, confirmed with PM, this was WAD."],
        10: [10, "Logout user, check on the login page that there is no important message."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Force quit the app"""
        common_method.Stop_The_App()
        """Wait for 1 hour"""
        # sleep(3600)
        sleep(30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Open the app"""
        common_method.Start_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        delete_account_page.click_Cancel_Btn()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Click Log Out"""
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        delete_account_page.verifyNoImportantMessageOnSignInPage()
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


def test_delete_account_testcase_id_45783():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and to be checked before continuing"],
        5: [5, "Check the 3 checkboxes and click the continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Force quit the app and wait for more than 1 hour. Note: Due to SMBM-1303, this was WAD, so there is no Delete Account dialog and error popping up after 1 hour to sign in. Skip steps 8 to 10."],
        8: [8,
             "In Mobile app, click Delete Account button again, check that the Delete Account page shows up. There are 3 items that need acknowledgment and to be checked before continuing"],
        9: [9, "Check the 3 checkboxes and click the continue button"],
        10: [10, "Check that the mobile app will auto logout and show the login screen with notice information."],
        14: [14, "Click sign in button and log in with the test user"],
        15: [15,
             "Check that user login successfully and the User setting page shows up with Delete Account dialog pop up asking for final confirmation to delete user"],
        16: [16, "Click Delete button on the Delete account dialog, check that user delete success dialog pops up."],
        17: [17,
             "Click OK button on the delete success dialog, check that user is deleted and the mobile app auto logs out."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.Start_The_App()
        login_page.Verify_ALL_Allow_Popups()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        common_method.tearDown()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        common_method.Stop_The_App()
        """Wait for 1 hour"""
        sleep(3605)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        common_method.Start_The_App()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        common_method.Start_The_App()
        delete_account_page.click_Cancel_Btn()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")

        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 14
        
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45786():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Open Mobile App"],
        2: [2, "Login in with test user"],
        3: [3, "Go to user setting page"],
        4: [4, "Connect to a poor network (move far away from Wi-Fi area) or disconnect mobile device network"],
        5: [5, "Click Delete Account button"],
        6: [6, "Check 3 checkboxes and click continue button"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        ### registration_page.click_accept()
        ### registration_page.clickClose()
        ### registration_page.clickExit()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        """Scroll till log out button"""
        registration_page.scrollTillLogOutAppears()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Disconnect mobile device network"""
        template_management_page.Turn_Off_wifi()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        delete_account_page.verifyServiceUnavailableErrorPopUp()
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


def test_delete_account_testcase_id_45770():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App"],
        2: [2, "In home page, click pen icon go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check Delete Account page shows up. There are 3 items need acknowledgment and checked then can continue"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Click Login button and input test username and password, click sign in button"],
        8: [8,
            "User login successfully and shows User setting page and Delete Account Dialog pop up asking for final confirmation to delete user"],
        9: [9,
            "Click Delete button on the Delete account dialog, check Account Deleted dialog pop up: Your account has been successfully deleted"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check the account will delete and user auto logout Mobile App and mobile app shows Login page"],
        11: [11, "Open Web Portal, click sign button and input the deleted username and password, click Sign in"],
        12: [12, "Check EULA page displayed, scroll all to view EULA and click accept button"],
        13: [13,
             "Check Web Portal home page shows up, check there is no printer in Home page and no designs in Recently Printed Labels list."],
        14: [14, "Click My Data, check there is no data file in My Data"],
        15: [15, "Click My Designs, check there are no designs in My Designs"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        template_management_page.Turn_ON_wifi()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        start_app("com.android.chrome")
        sleep(2)
        delete_account_page.Open_Web_Portal()
        data_sources_page.clickEnter()
        sleep(2)
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        delete_account_page.verifyNoPrinterInAccountWeb()
        poco.scroll()
        data_sources_page.lock_phone()
        wake()
        delete_account_page.VerifyIfNoRecentlyPrintedDesignsPresent()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 14
        start_time = time.time()
        data_sources_page.click_My_Data()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        delete_account_page.verifyMyDataEmpty()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 15
        start_time = time.time()
        data_sources_page.clickMyDesigns()
        login_page.click_Menu_HamburgerICN()
        delete_account_page.verifyMyDesignsEmptyWeb()
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


def test_delete_account_testcase_id_45775():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check Delete Account page shows up. There are 3 items need acknowledgment and checked then can continue"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Click login button, input test username and password, login, check user setting page displayed and pop up Account Delete dialog"],
        8: [8, "Switch to the other app, and switch back to Mobile App (within 1 hour)"],
        9: [9, "Check Mobile app still shows user setting page with Delete account dialog pop up"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check the account will delete and user auto logout Mobile App and mobile app shows Login page"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Switch to different app"""
        delete_account_page.switch_to_different_app()
        # sleep(60)
        sleep(10)
        """Switch back to the app"""
        delete_account_page.switch_to_different_app()
        sleep(5)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45776():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check Delete Account page shows up. There are 3 items that need acknowledgment and checked then can continue"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Lock screen for about 50 mins and unlock screen. Check the important notification still shows there"],
        8: [8,
            "Click login button, input test username and password, login, check user setting page displayed and pop up Account Delete dialog"],
        9: [9,
            "Click Delete button on the Delete account dialog, check Account Deleted dialog pops up: Your account has been successfully deleted"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check the account will delete and user auto logout Mobile App and mobile app shows Login page"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        delete_account_page.Verify_Service_Unavailable_Popup()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        data_sources_page.lock_phone()
        "wait for 50 min"
        # sleep(3000)
        sleep(20)
        wake()
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        delete_account_page.Verify_Service_Unavailable_Popup()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45774():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check Delete Account page shows up. There are 3 items that need acknowledgment and must be checked before continuing"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Click login button, input test username and password, login, check that user setting page is displayed and pop up Account Delete dialog"],
        8: [8, "Force quit the app, wait within 1 hour"],
        9: [9, "Re-open mobile app, check that Mobile app shows user setting page and Delete account dialog pops up"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check that the account will delete and user auto logout Mobile App, and the mobile app shows normal Login page"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.Clear_App()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        # data_sources_page.checkIfOnHomePage()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Force quit the app"""
        common_method.Stop_The_App()
        """Wait for 1 hour"""
        # sleep(3600)
        sleep(20)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """Open the app"""
        common_method.Start_The_App()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45777():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and must be checked before continuing"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Click login button, login with a different user for about 50 mins (within 1 hour), go to user setting page and click logout. Check that the login page still shows notice information."],
        8: [8,
            "Click login button, input test username and password, login, check that the user setting page is displayed and the Account Delete dialog pops up"],
        9: [9,
            "Click Delete button on the Delete account dialog, check that the Account Deleted dialog pops up: Your account has been successfully deleted"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check that the account will delete and the user auto logout Mobile App, and the mobile app shows normal Login page (no notice information)"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        "wait for 50 min"
        # sleep(3000)
        sleep(30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        registration_page.click_log_out_button()
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Login Again"""
        registration_page.clickSignIn()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
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


def test_delete_account_testcase_id_45778():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App with test account with test device"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and must be checked before continuing"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7,
            "Click login button, input test username and password, login, check that the user setting page is displayed and the Account Delete dialog pops up"],
        8: [8, "Lock device screen for more than 1 hour"],
        9: [9, "Unlock screen, in mobile app, click delete button, check that the Delete Error dialog pops up"],
        10: [10,
             "Click OK on delete fail dialog, check that the dialog dismisses and the user is not deleted, Mobile app still stays on the User setting page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.verifyDeleteAccountDialogPopUp()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        data_sources_page.lock_phone()
        "wait for 65 min"
        # sleep(3900)
        sleep(30)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        wake()
        delete_account_page.verifyDeleteAccountDialogPopUp()
        """Click delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        "check"
        delete_account_page.checkDeleteErrorDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if on settings after clicking Ok"""
        try:
            common_method.wait_for_element_appearance("Settings")
        except:
            raise Exception("Did not return to settings page.")
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


def test_delete_account_testcase_id_45784():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Test user login Mobile App"],
        2: [2, "In home page, 1 printer shows up with offline status"],
        3: [3,
            "Click on the Pen icon to go to user setting page. Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4, "Click 'Delete Account' button, check that the Delete Account page shows up"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Click Login button and input username and password then process to sign in"],
        8: [8,
            "User logs in successfully and shows the User setting page with the Delete Account dialog popping up asking for final confirmation to delete the user"],
        9: [9, "Click Delete button on the Delete account dialog"],
        10: [10, "Check that the account is deleted and the user auto logs out of the Mobile App"],
        11: [11,
             "Log in on the web portal with username and password, check that the EULA page is displayed, accept the EULA, and the home page shows up"],
        12: [12,
             "Turn on the offline printer; after the printer is online, it will auto decommission (Printer power on button will shine with yellow light and will auto restart). Check that no printer is visible on the home page in the web portal."],
        13: [13,
             "Login to the mobile app, click add printer, and check the target printers in the available printer list"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Verify that there is 1 offline printer in the account"""
        delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()

        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:"""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        """CLick Ok"""
        delete_account_page.clickOk()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        start_app("com.android.chrome")
        sleep(4)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        sleep(2)
        data_sources_page.clickEnter()
        sleep(2)
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        delete_account_page.verifyIfOnEULAPageWeb()
        delete_account_page.AcceptEULAWeb()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        data_sources_page.clickGotItWeb()
        registration_page.wait_for_element_appearance_text("Home", 25)
        """""printer will auto decomission (Printer power on button will shine with yellow light and will auto restart)"""
        delete_account_page.verifyNoPrinterInAccountWeb()
        stop_app("com.android.chrome")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        common_method.Start_The_App()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        """"click on Add printer tab"""""
        add_a_printer_page.click_Add_A_Printer()
        """"click on the start button"""
        add_a_printer_page.click_Start_Button()
        add_a_printer_page.Click_Next_Button()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"Verify searching for your printer text"""
        add_a_printer_page.Verify_Searching_for_your_printer_Text()
        """"check the target printers in available printer list"""
        delete_account_page.checkTargetPrintersAvailable()
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


def test_delete_account_testcase_id_45787():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Login Mobile App"],
        2: [2, "In home page, click pen icon to go to user setting page"],
        3: [3, "Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: [4,
            "Click 'Delete Account' button, check that the Delete Account page shows up. There are 3 items that need acknowledgment and must be checked to continue"],
        5: [5, "Check 3 checkboxes and click continue button"],
        6: [6,
            "Check that the mobile app will auto logout and show the login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [7, "Click Login button and input test username and password, then click sign in button"],
        8: [8,
            "User logs in successfully and shows the User setting page with the Delete Account dialog popping up asking for final confirmation to delete the user"],
        9: [9,
            "Click Delete button on the Delete account dialog, check that the Account Deleted dialog pops up: Your account has been successfully deleted"],
        10: [10,
             "Click OK button on the Account Deleted dialog, check that the account is deleted and the user auto logs out of the Mobile App, and the mobile app shows the Login page"],
        11: [11, "Click login button, the login page is displayed"],
        12: [12, "Click Register Now URL, check that the Registration page is displayed"],
        13: [13,
             "In the Email input box, input the deleted test user address then click Next button, check that the page shows the message: This email already exists. It looks like this email has already been registered. Please try logging in with your credentials."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Login Again"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        """Sign in with email and password"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        if poco("com.android.chrome:id/coordinator").exists():
            poco("com.android.chrome:id/coordinator").click()
        keyevent("back")
        poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        registration_page.registerEmail()
        try:
            registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
        except:
            raise Exception("register user page dint show")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        """Enter the User Email"""
        registration_page.enter_user_email_for_registering("zebra03.swdvt@gmail.com")
        registration_page.click_on_next()
        """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
        """Verify Account already exists page title"""
        registration_page.check_email_already_exists_page_title()
        """Verify Account already exists page message"""
        registration_page.check_email_already_Exists_page_message()
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


def test_delete_account_testcase_id_53205():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Go to the user profile page after clicking the edit button in the left side menu. Check that the Delete Account button is displayed correctly and the styles match the Figma design."],
        2: [2,
            "Click the Delete Account button. Check that the fonts are displayed correctly on the Delete Account page with 3 checkpoints."],
        3: [3,
            "Click the continue button and check that the app auto logs out. Verify that the login page displays the notice information correctly."],
        4: [4,
            "Login with the target account. Check that the final delete dialog displays correctly with the new fonts and styles."],
        5: [5,
            "Click the Delete button and login again. Check that the EULA is displayed with the new fonts and styles."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.signInWithEmail()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()

        app_settings_page.Home_text_is_present_on_homepage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Click continue"""
        data_sources_page.clickContinue()
        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        try:
            common_method.wait_for_element_appearance(
                "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
                20)
        except:
            raise Exception(
                "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        """Login Again"""
        registration_page.clickSignIn()
        delete_account_page.Login_With_Email_Tab()
        printer_management_page.click_Password_TextField()
        printer_management_page.Enter_Zebra_Password()
        login_page.click_SignIn_Button()
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        """Check the EULA would be display with the new fonts and styles. pending"""
        registration_page.click_accept()
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


def test_delete_account_testcase_id_45767():
    """Add a printer to this facebook account before executing and log out of facebook
#     # username - zebra09.swdvt@gmail.com
#     # password - Zebra#123456789"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: ["Test user login Mobile App with Facebook account by clicking Sign with Facebook on the login page"],
        2: ["In home page, 1 printer shows up with Online status"],
        3: [
            "Click on the Pen icon to get into user setting page. Check on the bottom of the page, 'Delete Account' button shows next to Logout button"],
        4: ["Click 'Delete Account' button, check Delete Account page shows up"],
        5: ["Check 3 checkbox and click continue button"],
        6: [
            "Check mobile app will auto logout and show login screen with notice information: Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."],
        7: [
            "Click Login button and choose sign in with Facebook, input Facebook username and password then process to sign in"],
        8: [
            "Facebook user login successfully and shows User setting page and Delete Account Dialog pop up asking for final confirmation to delete"],
        9: [
            "Click Delete button on the Delete account dialog, check Account Deleted dialog pop up: Your account has been successfully deleted"],
        10: [
            "Click OK button on the Account Deleted dialog, check the account will delete and user auto logout Mobile App, mobile app shows Login page"],
        11: [
            "Check printer will auto decommission (Printer power on button will shine with yellow light and auto restart)"],
        12: [
            "Re-login Mobile App with the deleted Facebook account by clicking Sign in with Facebook, check EULA page displayed, accept EULA and home page shows up, check no printer in home page."],
        13: ["Click add printer, check the target printers in available printer list"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        registration_page.login_Facebook("Zebra#123456789", "zebra09.swdvt@gmail.com")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Verify that there is 1 online printer in the account"""
        delete_account_page.checkIfThereIs1PrinterWithOnlineStatus()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        while not poco("Log Out").exists():
            poco.scroll()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        try:
            common_method.wait_for_element_appearance(
                "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
                20)
        except:
            raise Exception("Delete account page did not show up.")
        """Check continue disabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Continue enabled without checking the three check boxes")
        except Exception as e:
            pass
        """check there are 3 items need acknowledge """
        try:
            common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "All data in your workspace will be removed.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Your account will be de-identified, meaning it "
                                                                      "will not be associated with you.")
            delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
                                                                      "Ensure your printer is ON to factory reset "
                                                                      "your ZSB printer.")
        except:
            raise Exception("Three checkboxes not present to acknowledge.")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        try:
            template_management_page.wait_for_appearance_enabled("Continue")
        except:
            raise Exception("Continue disabled even after checking the three check boxes")
        """Click continue"""
        data_sources_page.clickContinue()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """check mobile app will auto logout and show login screen with notice information:"""
        delete_account_page.verifyImportantMessageOnSignInPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        delete_account_page.clickContinueAsInFacebookLogin()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 8
        start_time = time.time()
        app_settings_page.Home_text_is_present_on_homepage()
        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user
        delete"""
        try:
            common_method.wait_for_element_appearance(
                "To complete the ZSB account deletion process, select Delete.",
                20)
        except:
            raise Exception(
                "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final "
                "confirm user delete")
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 9
        start_time = time.time()
        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()
        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 10
        start_time = time.time()
        """CLick Ok"""
        delete_account_page.clickOk()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 11
        start_time = time.time()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 12
        start_time = time.time()
        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        delete_account_page.clickContinueAsInFacebookLogin()
        app_settings_page.Home_text_is_present_on_homepage()
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        data_sources_page.checkIfOnHomePage()
        delete_account_page.verifyNoPrinterInAccount()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 13
        start_time = time.time()
        """13. click add printer, check the target printers in available printer list-pending"""
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

