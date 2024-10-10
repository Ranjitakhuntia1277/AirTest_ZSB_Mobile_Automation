import inspect

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
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
from ...AEMS.store import execID, leftId


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

ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()

start_execution_loop(execID)


def test_Delete_Account_TestcaseID_45765():
    """Add 2 printer to this account before executing
    username - zebra05.swdvt@gmail.com
    password - Zebra#123456789"""
    pass
    test_steps = {
        1: [1, 'Test user logs into the Mobile App.'],
        2: [2,
            'On the home page, verify that two printers are displayed in the printer list (one online, one offline). Click the Pen icon to navigate to the User Settings page.'],
        3: [3, 'Verify the "Delete Account" button is displayed next to the "Logout" button.'],
        4: [4,
            'Click the "Delete Account" button and verify the Delete Account page appears with the following acknowledgments and checkboxes:'
            '- All data in your workspace will be removed'
            '- Your account will be de-identified, meaning it will not be associated with you'
            '- Ensure your printer is On to factory reset your ZSB Printer.'
            'Additionally, check that the text instructs the user to sign back in one last time to finalize and confirm the deletion, with two buttons: "Cancel" and "Continue" (Continue button is disabled).'],
        5: [5, 'Check all three checkboxes and verify the "Continue" button is enabled. Click "Continue".'],
        6: [6,
            'Verify the mobile app automatically logs out and displays the login screen with the notice: "Important: For security purposes, please log in one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."'],
        7: [7, 'Click the "Login" button, enter the test username and password, and click "Sign In".'],
        8: [8,
            'Verify the user logs in successfully, and the User Settings page is displayed with the Delete Account dialog asking for final confirmation.'],
        9: [9,
            'Click the "Delete" button on the Delete Account dialog, and verify the Account Deleted dialog pops up with the message: "Your account has been successfully deleted."'],
        10: [10,
             'Click the "OK" button on the Account Deleted dialog. Verify the account is deleted, the user is logged out, and the mobile app displays the login page. Check that the online printer is automatically decommissioned (power button shines yellow and the printer restarts).'],
        11: [11,
             'Turn on the previously offline printer, and after the printer is online, verify that it is automatically decommissioned (power button shines yellow and the printer restarts).'],
        12: [12,
             'Re-login to the Mobile App using the deleted account. Verify the EULA page is displayed, accept the EULA, and confirm that the home page shows no printers.'],
        13: [13, 'click add printer, check the 2 printers in available printer list, select one printer, check printer can be added again']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.show_message(
            "Add 2 printer to this account before executing\nusername - zebra05.swdvt@gmail.com\npassword - Zebra#12345678, make sure one is online and other is offline")
        """clear app data"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#12345678", 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        "In home page 2 printer show in printer list , one is online and one is offline, click pen icon go to user setting page-pending"
        """Verify that there is 1 offline printer in the account"""
        delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        delete_account_page.check_if_on_delete_account_page()
        """Check continue disabled"""
        delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
        """check there are 3 items need acknowledge """
        delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
        """Click continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """check mobile app will auto logout and show login screen with notice information:"""
        delete_account_page.verifyImportantMessageOnSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#12345678", 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.check_final_delete_account_pop_up()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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

        # Step 11
        start_time = time.time()

        common_method.show_message(
            "Turn on the offline printer. After the printer comes online, the printer will auto decommission (SMBUI-2480 WAD: Printer power-on button will shine with a yellow light and the printer will auto-restart).")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#12345678", 1, 0)
        data_sources_page.checkIfOnHomePage()
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

        # Step 13
        start_time = time.time()

        """"click on Add printer tab"""""
        add_a_printer_page.click_Add_A_Printer()
        """"click on the start button"""
        add_a_printer_page.click_Start_Button()
        add_a_printer_page.Click_Next_Button()
        """"Verify searching for your printer text"""
        add_a_printer_page.Verify_Searching_for_your_printer_Text()
        """"check the target printers in available printer list"""
        delete_account_page.checkTargetPrintersAvailable()
        common_method.show_message(
            "Check the printer which was removed associated with the account - zebra05.swdvt@gmail.com is present in the printer list.")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Delete_Account_TestcaseID_45768():
    pass
    test_steps = {
        1: [1,
            'Test user logs into the Mobile App using their Apple ID by clicking "Sign with Apple" on the login page (enter verification code if needed).'],
        2: [2, 'On the home page, verify no printer is displayed.'],
        3: [3,
            'Click the Pen icon to navigate to the User Settings page and verify the "Delete Account" button is displayed next to the "Logout" button.'],
        4: [4, 'Click the "Delete Account" button and check that the Delete Account page is displayed.'],
        5: [5, 'Check the three required checkboxes, then click the "Continue" button.'],
        6: [6,
            'Verify the mobile app logs out automatically and displays the login screen with the notice: "Important: For security purposes, please log in one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."'],
        7: [7,
            'Click the "Login" button, select "Sign in with Apple," enter the Apple ID and password, then proceed to sign in.'],
        8: [8,
            'Verify the Apple user successfully logs in, the User Settings page is displayed, and the Delete Account dialog pops up, asking for final confirmation.'],
        9: [9,
            'Click the "Delete" button on the Delete Account dialog and verify that an "Account Deleted" dialog appears with the message "Your account has been successfully deleted."'],
        10: [10,
             'Click the "OK" button on the Account Deleted dialog and verify that the user is logged out, and the mobile app displays the login page.'],
        11: [11,
             'Re-login to the Mobile App using the deleted Apple ID by clicking "Sign in with Apple." Verify that the EULA page is displayed, accept the EULA, and verify that the home page shows no printers.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        """Check if reached home page after login"""
        data_sources_page.checkIfOnHomePage()
        """Verify that there are no printers in the account"""
        delete_account_page.verifyNoPrinterInAccount()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        delete_account_page.check_if_on_delete_account_page()
        """check there are 3 items need acknowledge """
        delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Click continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.check_final_delete_account_pop_up()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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

        # Step 11
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        registration_page.login_Apple("Zebra#123456789", "zebra08.swdvt@gmail.com")
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        data_sources_page.checkIfOnHomePage()
        delete_account_page.verifyNoPrinterInAccount()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# def test_Delete_Account_TestcaseID_45771():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     data_sources_page.checkIfOnHomePage()
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     while not poco("Log Out").exists():
#         poco.scroll()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     """Check Delete Account page show up"""
#     try:
#         common_method.wait_for_element_appearance(
#             "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#             20)
#     except:
#         raise Exception("Delete account page did not show up.")
#     """Check continue disabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#         x = 1 / 0
#     except ZeroDivisionError:
#         raise Exception("Continue enabled without checking the three check boxes")
#     except Exception as e:
#         pass
#     """check there are 3 items need acknowledge """
#     try:
#         common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "All data in your workspace will be removed.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Your account will be de-identified, meaning it will not be associated with you.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Ensure your printer is ON to factory reset your ZSB printer.")
#     except:
#         raise Exception("Three checkboxes not present to acknowledge.")
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#     except:
#         raise Exception("Continue disabled even after checking the three check boxes")
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:
#     Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     try:
#         common_method.wait_for_element_appearance(
#             "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
#             20)
#     except:
#         raise Exception(
#             "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     try:
#         common_method.wait_for_element_appearance(
#             "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
#             20)
#     except:
#         raise Exception(
#             "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
#     """CLick delete in final confirmation pop up"""
#     delete_account_page.clickDelete()
#     """Verify Account Deleted dialog pop up"""
#     delete_account_page.checkAccountDeletedDialog()
#     """CLick Ok"""
#     delete_account_page.clickOk()
#     """Check if logged out automatically after clicking Ok"""
#     data_sources_page.checkIfInLoginPage()
#     """Cannot automate
#     11. Open Printer Tools click sign button check Login page show up, input the deleted user name and password click Sign in, check user can login printer tools successfully and no printer show in printer list.
#     has to be executed manually"""
#     common_method.show_message("11. Open Printer Tools click sign button check Login page show up, input the deleted user name and password click Sign in, check user can login printer tools successfully and no printer show in printer list.\nAccount info - username - zebra05.swdvt@gmail.com password- Zebra#123456789")
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     registration_page.verify_if_on_EULA_page()
#     """Accept EULA for future execution"""
#     """Check the EULA would be display with the new fonts and styles. pending"""
#     registration_page.click_accept()


# Existing bug:-
def test_Delete_Account_TestcaseID_45785():
    pass
    test_steps = {
        1: [1, 'Test user login Mobile App.'],
        2: [2,
            'Click on the Pen icon to get into user settings page. Check on the bottom of the page, "Delete Account" button shows next to Logout button.'],
        3: [3, 'Upload user photo, modify user first name and last name, change units of measurement to cm or mm.'],
        4: [4,
            'Click workspace edit button, click edit button, upload workspace photo, modify workspace name, save and exit.'],
        5: [5, 'Change theme against the default, save and exit.'],
        6: [6, 'Go to printer settings, change graphic options.'],
        7: [7, 'Click "Delete Account" button, check Delete Account page shows up.'],
        8: [8, 'Check 3 checkboxes and click continue button.'],
        9: [9,
            'Check the mobile app auto logs out and shows the login screen with the notice: "Important: For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."'],
        10: [10, 'Click Login button, input username and password, then proceed to sign in.'],
        11: [11, 'User logs in successfully, and the Delete Account dialog pops up asking for final confirmation.'],
        12: [12, 'Click Delete button on the Delete account dialog.'],
        13: [13, 'Check the account is deleted, and the Mobile App auto logs out.'],
        14: [14,
             'Login to the Mobile App again, check that the EULA page is displayed, accept the EULA, and the home page shows up. Check the theme has changed to the default.'],
        15: [15,
             'Go to user settings page, check no user photo shows up, and the first name, last name, and email have not changed (same as step 3). Check the units of measurement have reset to inches (default).'],
        16: [16,
             'Go to workspace edit page, check the workspace photo is cleared, and the workspace name has been reset to "My First Workspace."'],
        17: [17, 'Go to printer settings, check that the graphic options are set to solid (default).']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        """clear app data"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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

        # Step 3
        start_time = time.time()

        """""click on upload photo"""
        app_settings_page.click_User_upload_photo()
        """click on camera option"""
        app_settings_page.click_Mobile_Camera()
        """""click allow if it is present"""
        app_settings_page.Click_Allow_popup()
        """"click on click picture icon"""
        others_page.capture_the_image_button()
        data_sources_page.clickOk()
        """"Verify photo uploaded message"""""
        app_settings_page.Verify_Photo_Uploaded_Message()
        """Change first name"""
        delete_account_page.change_first_name()
        """Change last name"""
        delete_account_page.change_last_name()
        """Change unit of measurement"""
        delete_account_page.change_unit_of_measurement()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        app_settings_page.click_upload_photo()
        sleep(2)
        """""click on the 1st image"""
        delete_account_page.selectFirstImage()
        """Change workspace name"""
        delete_account_page.change_workspace_name()
        """click on the save & exit"""
        app_settings_page.click_Save_Exit_Btn()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        app_settings_page.click_Three_Dot_On_Workspace()
        """Click change theme"""
        app_settings_page.click_Change_Theme()
        """Change default theme to any other theme"""
        app_settings_page.check_Change_Electic_Theme()
        """click on the save & exit"""
        app_settings_page.click_Save_Exit_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        """"change the darkness level"""
        app_settings_page.Change_Darkness_Level_Bar()
        """verify the darkness updated message"""
        app_settings_page.Verify_Darkness_Updated_Message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()
        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
        """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
        """Check Delete Account page show up"""
        delete_account_page.check_if_on_delete_account_page()
        """Check continue disabled"""
        delete_account_page.check_if_continue_button_is_enabled_without_checking_three_checkboxes_in_delete_account_page()
        """check there are 3 items need acknowledge """
        delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Check continue enabled"""
        delete_account_page.check_if_continue_button_is_disabled_even_after_checking_three_checkboxes_in_delete_account_page()
        """Click continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9
        start_time = time.time()

        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11
        start_time = time.time()

        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.check_final_delete_account_pop_up()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12
        start_time = time.time()

        """CLick delete in final confirmation pop up"""
        delete_account_page.clickDelete()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13
        start_time = time.time()

        """Verify Account Deleted dialog pop up"""
        delete_account_page.checkAccountDeletedDialog()
        """CLick Ok"""
        delete_account_page.clickOk()
        """Check if logged out automatically after clicking Ok"""
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        """Check the EULA would be display with the new fonts and styles. pending"""
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        delete_account_page.verifyDefaultSettings()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        app_settings_page.click_Edit_Txt()
        """Verify if workspace settings are back to default"""
        delete_account_page.verifyDefaultWorkspaceSettings()
        data_sources_page.clickBackArrow()
        app_settings_page.click_Three_Dot_On_Workspace()
        """Click change theme"""
        app_settings_page.click_Change_Theme()
        """Verify if theme is back to default"""
        delete_account_page.verifyDefaultTheme()
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step17
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        delete_account_page.verifyIfSeekBarIsDefault()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# Existing bug:-
# def test_Delete_Account_TestcaseID_45779():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     data_sources_page.checkIfOnHomePage()
#     """Execute in Device A"""
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     while not poco("Log Out").exists():
#         poco.scroll()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     """Check Delete Account page show up"""
#     try:
#         common_method.wait_for_element_appearance(
#             "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#             20)
#     except:
#         raise Exception("Delete account page did not show up.")
#     """Check continue disabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#         x = 1 / 0
#     except ZeroDivisionError:
#         raise Exception("Continue enabled without checking the three check boxes")
#     except Exception as e:
#         pass
#     """check there are 3 items need acknowledge """
#     try:
#         common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "All data in your workspace will be removed.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Your account will be de-identified, meaning it will not be associated with you.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Ensure your printer is ON to factory reset your ZSB printer.")
#     except:
#         raise Exception("Three checkboxes not present to acknowledge.")
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#     except:
#         raise Exception("Continue disabled even after checking the three check boxes")
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:
#     Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     delete_account_page.verifyImportantMessageOnSignInPage()
#     """Login Again"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     delete_account_page.verifyDeleteAccountDialogPopUp()


# def test_Delete_Account_TestcaseID_45779_1():
#     pass
#     # """clear app data"""
#     # data_sources_page.clearAppData()
#     # common_method.tearDown()
#     # data_sources_page.allowPermissions()
#     # """Sign in"""
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # data_sources_page.checkIfOnHomePage()
#     # """Execute in device B"""
#     # """Click Hamburger Icon"""
#     # login_page.click_Menu_HamburgerICN()
#     # """Click on edit profile"""
#     # registration_page.click_on_profile_edit()
#     # while not poco("Log Out").exists():
#     #     poco.scroll()
#     # """Check If Delete Account is beside Logout button"""
#     # delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     # """Click Delete Account"""
#     # delete_account_page.clickDeleteAccount()
#     # """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     # """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     # """Check Delete Account page show up"""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#     #         20)
#     # except:
#     #     raise Exception("Delete account page did not show up.")
#     # """Check continue disabled"""
#     # try:
#     #     template_management_page.wait_for_appearance_enabled("Continue")
#     #     x = 1 / 0
#     # except ZeroDivisionError:
#     #     raise Exception("Continue enabled without checking the three check boxes")
#     # except Exception as e:
#     #     pass
#     # """check there are 3 items need acknowledge """
#     # try:
#     #     common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "All data in your workspace will be removed.")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "Your account will be de-identified, meaning it will not be associated with you.")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "Ensure your printer is ON to factory reset your ZSB printer.")
#     # except:
#     #     raise Exception("Three checkboxes not present to acknowledge.")
#     # """Click the three checkBoxes"""
#     # delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     # """Check continue enabled"""
#     # try:
#     #     template_management_page.wait_for_appearance_enabled("Continue")
#     # except:
#     #     raise Exception("Continue disabled even after checking the three check boxes")
#     # """Click continue"""
#     # data_sources_page.clickContinue()
#     # """check mobile app will auto logout and show login screen with notice information:
#     # Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     # delete_account_page.verifyImportantMessageOnSignInPage()
#     # """Login Again"""
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     # delete_account_page.verifyDeleteAccountDialogPopUp()


# def test_Delete_Account_TestcaseID_45779_2():
#     pass
#     # """Execute in device A"""
#     # """Click delete in final confirmation pop up"""
#     # delete_account_page.clickDelete()
#     # """Verify Account Deleted dialog pop up"""
#     # delete_account_page.checkAccountDeletedDialog()
#     # """CLick Ok"""
#     # delete_account_page.clickOk()
#     # """Check if logged out automatically after clicking Ok"""
#     # data_sources_page.checkIfInLoginPage()
#     # common_method.Stop_The_App()


# def test_Delete_Account_TestcaseID_45779_3():
#     pass
#     # """Execute in device B"""
#     # """Check if logged out automatically on device B after clicking Ok on device A"""
#     # data_sources_page.checkIfInLoginPage()
#     # common_method.Stop_The_App()


# def test_Delete_Account_TestcaseID_45773():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     data_sources_page.checkIfOnHomePage()
#     """Click Hamburger Icon"""
#     login_page.click_Menu_HamburgerICN()
#     """Click on edit profile"""
#     registration_page.click_on_profile_edit()
#     while not poco("Log Out").exists():
#         poco.scroll()
#     """Check If Delete Account is beside Logout button"""
#     delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     """Click Delete Account"""
#     delete_account_page.clickDeleteAccount()
#     """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     """Check Delete Account page show up"""
#     try:
#         common_method.wait_for_element_appearance(
#             "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#             20)
#     except:
#         raise Exception("Delete account page did not show up.")
#     """Check continue disabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#         x = 1 / 0
#     except ZeroDivisionError:
#         raise Exception("Continue enabled without checking the three check boxes")
#     except Exception as e:
#         pass
#     """check there are 3 items need acknowledge """
#     try:
#         common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "All data in your workspace will be removed.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Your account will be de-identified, meaning it will not be associated with you.")
#         delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#                                                                   "Ensure your printer is ON to factory reset your ZSB printer.")
#     except:
#         raise Exception("Three checkboxes not present to acknowledge.")
#     """Click the three checkBoxes"""
#     delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     """Check continue enabled"""
#     try:
#         template_management_page.wait_for_appearance_enabled("Continue")
#     except:
#         raise Exception("Continue disabled even after checking the three check boxes")
#     """Click continue"""
#     data_sources_page.clickContinue()
#     """check mobile app will auto logout and show login screen with notice information:
#     Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     delete_account_page.verifyImportantMessageOnSignInPage()


# def test_Delete_Account_TestcaseID_45773_1():
#     pass
#     # data_sources_page.clearAppData()
#     # common_method.tearDown()
#     # data_sources_page.allowPermissions()
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
#     #         20)
#     #     x=1/0
#     # except ZeroDivisionError:
#     #     raise Exception("Delete Account Dialog pop up is present when logged in with device B after initiating delete with device A.")
#     # except Exception as e:
#     #     pass
#     # common_method.Stop_The_App()


# def test_Delete_Account_TestcaseID_45773_2():
#     pass
#     # data_sources_page.clearAppData()
#     # common_method.tearDown()
#     # data_sources_page.allowPermissions()
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
#     #         20)
#     # except:
#     #     raise Exception(
#     #         "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
#     # """CLick delete in final confirmation pop up"""
#     # delete_account_page.clickDelete()
#     # """Verify Account Deleted dialog pop up"""
#     # delete_account_page.checkAccountDeletedDialog()
#     # """CLick Cancel"""
#     # data_sources_page.clickCancel()
#     # common_method.Stop_The_App()


# Existing bug:-
# def test_Delete_Account_TestcaseID_45772():
#     pass
# """clear app data"""
# data_sources_page.clearAppData()
# common_method.tearDown()
# data_sources_page.allowPermissions()
# """Sign in"""
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
# data_sources_page.checkIfOnHomePage()
# """Execute on device B"""
# data_sources_page.clearAppData()
# common_method.tearDown()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
# start_app("com.android.chrome")
# sleep(2)
# poco("com.android.chrome:id/tab_switcher_button").click()
# sleep(2)
# poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# data_sources_page.clearBrowsingData()
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# sleep(2)
# data_sources_page.clickEnter()
# sleep(2)
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
# data_sources_page.checkIfOnHomePageWeb()


# def test_Delete_Account_TestcaseID_45772_1():
#     """Execute this on Device A"""
#     pass
#     # """clear app data"""
#     # data_sources_page.clearAppData()
#     # common_method.tearDown()
#     # data_sources_page.allowPermissions()
#     # """Sign in"""
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # data_sources_page.checkIfOnHomePage()
#     # """Click Hamburger Icon"""
#     # login_page.click_Menu_HamburgerICN()
#     # """Click on edit profile"""
#     # registration_page.click_on_profile_edit()
#     # while not poco("Log Out").exists():
#     #     poco.scroll()
#     # """Check If Delete Account is beside Logout button"""
#     # delete_account_page.checkIfDeleteAccountIsNextToLogOut()
#     # """Click Delete Account"""
#     # delete_account_page.clickDeleteAccount()
#     # """ Check the Delete Account button displayed correctly and the styles would be match for the Figma pending"""
#     # """Check the fonts displayed correctly in Delete Account page with 3 check points checking. pending"""
#     # """Check Delete Account page show up"""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out.",
#     #         20)
#     # except:
#     #     raise Exception("Delete account page did not show up.")
#     # """Check continue disabled"""
#     # try:
#     #     template_management_page.wait_for_appearance_enabled("Continue")
#     #     x = 1 / 0
#     # except ZeroDivisionError:
#     #     raise Exception("Continue enabled without checking the three check boxes")
#     # except Exception as e:
#     #     pass
#     # """check there are 3 items need acknowledge """
#     # try:
#     #     common_method.wait_for_element_appearance("Please acknowledge the following to continue:")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "All data in your workspace will be removed.")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "Your account will be de-identified, meaning it will not be associated with you.")
#     #     delete_account_page.wait_for_element_appearance_name_type("android.widget.CheckBox",
#     #                                                               "Ensure your printer is ON to factory reset your ZSB printer.")
#     # except:
#     #     raise Exception("Three checkboxes not present to acknowledge.")
#     # """Click the three checkBoxes"""
#     # delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
#     # """Check continue enabled"""
#     # try:
#     #     template_management_page.wait_for_appearance_enabled("Continue")
#     # except:
#     #     raise Exception("Continue disabled even after checking the three check boxes")
#     # """Click continue"""
#     # data_sources_page.clickContinue()
#     # """check mobile app will auto logout and show login screen with notice information:
#     # Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active.",
#     #         20)
#     # except:
#     #     raise Exception(
#     #         "Warning message \" Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active.\" not displayed")
#     # """Login Again"""
#     # registration_page.clickSignIn()
#     # data_sources_page.signInWithEmail()
#     # registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     # """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
#     # try:
#     #     common_method.wait_for_element_appearance(
#     #         "Delete Account\nTo complete the ZSB account deletion process, select Delete.\nTo cancel the deletion process and retain your ZSB account, select Cancel.",
#     #         20)
#     # except:
#     #     raise Exception(
#     #         "User not taken to user settings page after login and no Delete Account Dialog pop up asking Final confirm user delete")
#     # """CLick delete in final confirmation pop up"""
#     # delete_account_page.clickDelete()
#     # """Verify Account Deleted dialog pop up"""
#     # delete_account_page.checkAccountDeletedDialog()
#     # """CLick Ok"""
#     # delete_account_page.clickOk()
#     # """Check if logged out automatically after clicking Ok"""
#     # data_sources_page.checkIfInLoginPage()


# def test_Delete_Account_TestcaseID_45772_2():
#     pass
#     # """Execute on device B"""
#     # common_method.Start_The_App()
#     # data_sources_page.checkIfInLoginPage()
#     # start_app("com.android.chrome")
#     # data_sources_page.checkIfInLoginPageWeb()


def test_Delete_Account_TestcaseID_45766():
    pass
    """Add a printer to this account before executing
    username - zebra05.swdvt@gmail.com
    password - Zebra#123456789"""
    test_steps = {
        1: [1, 'Test user login Mobile App with Google account by clicking "Sign with Google" on the login page.'],
        2: [2, 'On the home page, 1 printer shows up with offline status.'],
        3: [3,
            'Click on the Pen icon to get into the user settings page. Check if the "Delete Account" button shows next to Logout.'],
        4: [4, 'Click "Delete Account" button, check if the Delete Account page shows up.'],
        5: [5, 'Check 3 checkboxes and click the continue button.'],
        6: [6,
            'Check that the mobile app auto logs out and shows the login screen with notice information: "Important: For security purposes, please log in one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."'],
        7: [7,
            'Click the Login button, choose "Sign in with Google," input the Google username and password, and proceed to sign in.'],
        8: [8,
            'Google user logs in successfully, the User settings page is shown, and the Delete Account dialog pops up for final confirmation of the account deletion.'],
        9: [9,
            'Click the Delete button on the Delete Account dialog, and check if the "Account Deleted" dialog pops up with the message: "Your account has been successfully deleted."'],
        10: [10,
             'Click OK on the "Account Deleted" dialog. Check that the account is deleted and the user is auto-logged out of the Mobile App, and the app shows the Login page.'],
        11: [11,
             'Turn on the offline printer. After the printer comes online, the printer will auto decommission (SMBUI-2480 WAD: Printer power-on button will shine with a yellow light and the printer will auto-restart).'],
        12: [12,
             'Re-login to the Mobile app using the deleted Google account by clicking "Sign in with Google." Check that the EULA page is displayed, accept the EULA, and the home page shows up. Check that no printer is displayed on the home page.'],
        13: [13, 'Click "Add Printer," and check if the target printers are listed in the available printer list.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step
        start_time = time.time()

        common_method.show_message(
            "Add printer to account - zebra05.swdvt@gmail.com-Zebra#123456789 with google login and get the printer to offline state")
        common_method.tearDown()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        login_page.click_Loginwith_Google()
        help_page.chooseAcc("zebra05.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        """Verify that there is 1 offline printer in the account"""
        delete_account_page.checkIfThereIs1PrinterWithOfflineStatus()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        delete_account_page.check_if_on_delete_account_page()
        """check there are 3 items need acknowledge """
        delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Click continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """check mobile app will auto logout and show login screen with notice information:"""
        delete_account_page.verifyImportantMessageOnSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        registration_page.clickSignIn()
        login_page.click_Loginwith_Google()
        help_page.chooseAcc("zebra05.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.check_final_delete_account_pop_up()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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

        # Step 11
        start_time = time.time()

        common_method.show_message(
            "Turn on the offline printer. After the printer comes online, the printer will auto decommission (SMBUI-2480 WAD: Printer power-on button will shine with a yellow light and the printer will auto-restart).")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        login_page.click_Loginwith_Google()
        help_page.chooseAcc("zebra05.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
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

        # Step 13
        start_time = time.time()

        """"click on Add printer tab"""""
        add_a_printer_page.click_Add_A_Printer()
        others_page.click_on_allow()
        """"click on the start button"""
        add_a_printer_page.click_Start_Button()
        others_page.click_on_allow()
        add_a_printer_page.Click_Next_Button()
        """"Verify searching for your printer text"""
        add_a_printer_page.Verify_Searching_for_your_printer_Text()
        """"check the target printers in available printer list"""
        delete_account_page.checkTargetPrintersAvailable()
        common_method.show_message(
            "Check the printer which was removed associated with the account - zebra05.swdvt@gmail.com is present in the printer list.")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Delete_Account_TestcaseID_45788():
    pass
    test_steps = {
        1: [1, 'Login to the Mobile App.'],
        2: [2, 'On the home page, click the pen icon to go to the user settings page.'],
        3: [3, 'Check if the "Delete Account" button shows next to the Logout button at the bottom of the page.'],
        4: [4, 'Click the "Delete Account" button, and verify that the Delete Account page appears.'],
        5: [5, 'Check the 3 checkboxes for acknowledgment, and click the continue button.'],
        6: [6,
            'Verify that the app auto logs out and shows the login screen with the notice: "Important: For security purposes, please log in one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."'],
        7: [7, 'Click the Login button, input the test username and password, then click Sign in.'],
        8: [8,
            'Verify successful login and check that the User Settings page appears, with a Delete Account dialog asking for final confirmation.'],
        9: [9,
            'Click the Delete button on the Delete Account dialog, and verify that the "Account Deleted" dialog appears with the message: "Your account has been successfully deleted."'],
        10: [10,
             'Click OK on the Account Deleted dialog. Verify that the app logs the user out and returns to the Login page.'],
        11: [11, 'Click the Login button to confirm the login page is displayed.'],
        12: [12, 'Click "Reset Password" to check that the Password Recovery page appears.'],
        13: [13, 'In the Email input box, enter the deleted test user email address and click the SUBMIT button.'],
        14: [14, 'Verify the Success page appears. Click the URL provided to access the Reset Password page.'],
        15: [15,
             'Check the user email for the Reset Code. Input the Reset Code and new password twice, then click the submit button. Verify the "Reset Password Success" page appears.'],
        16: [16,
             'Click the "Return to Sign In" button, input the username and new password, and click Sign in. Verify the EULA page appears.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
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
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        registration_page.scroll_till_log_out()
        """Check If Delete Account is beside Logout button"""
        delete_account_page.checkIfDeleteAccountIsNextToLogOut()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Click Delete Account"""
        delete_account_page.clickDeleteAccount()
        """Check Delete Account page show up"""
        delete_account_page.check_if_on_delete_account_page()
        """check there are 3 items need acknowledge """
        delete_account_page.acknowledge_three_checkboxes_in_delete_account_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        """Click the three checkBoxes"""
        delete_account_page.checkThreeCheckboxesInDeleteAccountPage()
        """Click continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        """check mobile app will auto logout and show login screen with notice information:
        Important: For security purposes, please login one last time to finalize the deletion of your account . Failure to do so will result in your account still being active."""
        delete_account_page.verifyImportantMessageOnSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7
        start_time = time.time()

        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#123456789", 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8
        start_time = time.time()

        """Check If taken to user settings page after login and Delete Account Dialog pop up ask Final confirm user delete"""
        delete_account_page.check_final_delete_account_pop_up()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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

        # Step 11
        start_time = time.time()

        """Sign in with email and password"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12
        start_time = time.time()

        poco.scroll()
        registration_page.click_on_reset_password()
        registration_page.check_if_in_password_recovery_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13
        start_time = time.time()

        registration_page.Enter_Username_password_recovery_page("zebra05.swdvt@gmail.com")
        registration_page.click_SUBMIT()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14
        start_time = time.time()

        registration_page.wait_for_element_appearance_text("Success!", 10)
        registration_page.check_message_on_success_page()
        registration_page.checkClickHerePresent()
        registration_page.click_on_Click_here()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15
        start_time = time.time()

        registration_page.check_if_on_Reset_Password_page()
        """Enter otp manually"""
        common_method.show_message(
            "Enter the otp received on gmail account - zebra05.swdvt@gmail.com - Zebra#123456789 in the 'Temporary Password' field. Minimize the keyboard after entering the otp. Click Ok in the dialog after its done.")
        registration_page.fillNewPassword("Zebra#1234567819")
        registration_page.fillConfirmPassword("Zebra#1234567819")
        registration_page.click_SUBMIT()
        registration_page.check_successful_password_reset_page_message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16
        start_time = time.time()

        registration_page.click_on_Click_here()
        data_sources_page.checkIfInLoginPage()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra05.swdvt@gmail.com", "Zebra#1234567819", 1, 0)
        registration_page.verify_if_on_EULA_page()
        """Accept EULA for future execution"""
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        common_method.Stop_The_App()
        common_method.show_message("Change password of zebra05.swdvt@gmail.com in zebra login back to Zebra#123456789")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

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
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
        end_execution_loop(execID)
        end_execution(execID)
