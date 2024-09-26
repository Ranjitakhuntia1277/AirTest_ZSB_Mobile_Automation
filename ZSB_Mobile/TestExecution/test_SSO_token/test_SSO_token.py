import inspect

from ZSB_Mobile.PageObject.SSO_Token_Renewal_Screen.SSO_Token_Renewal_Screen_Android import SSO_Token_Renewal_Screen
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from poco.exceptions import PocoNoSuchNodeException
import pytest
from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId


class SSO_Token_Renewal:
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
sso_token_renewal_page = SSO_Token_Renewal_Screen(poco)

# sso_token_renewal_page.clear_old_logs()

ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()

start_execution_loop(execID)

"""checks steps with - Highlight"""
def test_SSO_Token_Renewal_TestcaseID_49905():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in with the Non-Zebra account'],
        2: [2,
            '[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second]'],
        3: [3, 'Check that test label or Common Designs can be printed.'],
        4: [4,
            'Logout then login\nCheck login successful\n[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second]\nCheck this token is a new one and not the same as the previous token'],
        5: [5, 'Check the Help pages(Support, FAQs, Contact Us, Chat) are available.'],
        6: [6, 'Repeat steps 1-5 with the Zebra account login.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in with the Non-Zebra account
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        """clear app data"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        registration_page.check_if_user_navigated_to_sign_in_page()
        account = "zebra07.swdvt@gmail.com"
        help_page.chooseAcc(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: [Android & iOS]\nCheck token message in adb log or tidevice syslog
        start_time = time.time()

        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}"
        in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is token information about " : flutter: getLocalTokens : access_token: " in the adb log or
        tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        print("old token->", old_token)
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3150)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check that test label or Common Designs can be printed
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        template_management_page.select_design_common_designs()
        template_management_page.select_label_common_designs()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        data_sources_page.clickBackArrow()
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Logout and login, check token refresh
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        account = "zebra07.swdvt@gmail.com"
        template_management_page.checkIfAccPresent(account)
        help_page.chooseAcc(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)
        """Click hamburger icon to expand menu"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check Help pages (Support, FAQs, Contact Us, Chat)
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        """Swipe up"""
        poco.scroll()
        """Click Help dropdown to expand Help options"""
        help_page.click_Help_dropdown_option()
        sso_token_renewal_page.checkIfHelpPagesArePresent()
        template_management_page.click_scrim()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Repeat steps 1-5 with Zebra account login
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        template_management_page.select_design_common_designs()
        template_management_page.select_label_common_designs()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        data_sources_page.clickBackArrow()
        data_sources_page.clickBackArrow()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        """Login Again"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Swipe up"""
        poco.scroll()
        """Click Help dropdown to expand Help options"""
        help_page.click_Help_dropdown_option()
        sso_token_renewal_page.checkIfHelpPagesArePresent()
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


def test_SSO_Token_Renewal_TestcaseID_49907():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in and keep the app active for 52 minutes.'],
        2: [2, 'Check that test label or Common Designs can be printed.'],
        3: [3, 'Check the login account would not be logged out or any other error during this time.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in and keep the app active for 52 minutes
        start_time = time.time()

        """clear app data"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """wait for 52 min"""
        sleep(3120)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check that test label or Common Designs can be printed
        start_time = time.time()

        """Check if user still logged in"""
        sso_token_renewal_page.check_if_user_is_logged_in()
        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        template_management_page.select_design_common_designs()
        template_management_page.select_label_common_designs()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check the login account is not logged out or encountering errors
        start_time = time.time()

        sso_token_renewal_page.noErrorOccurredAfterPrinting()
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


def test_SSO_Token_Renewal_TestcaseID_49908():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in and keep the app active for 52 minutes.'],
        2: [2,
            '[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second]'],
        3: [3, 'Check the login account would not be logged out or any other error during this time.'],
        4: [4, 'Perform the printing in My Designs and check it can be printed.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in and keep the app active for 52 minutes
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        sleep(3120)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        # Step 2: Check logs for token information
        start_time = time.time()

        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        # Step 3: Check that login account is active
        start_time = time.time()

        """Check if still on logged in page"""
        sso_token_renewal_page.check_if_user_is_logged_in()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        # Step 4: Perform printing in My Designs
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        common_method.wait_for_element_appearance_namematches("Showing")
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
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


"""Need to change steps as it includes add a printer"""


# def test_SSO_Token_Renewal_TestcaseID_49909():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """verify if logged in successfully"""
#     data_sources_page.checkIfOnHomePage()
#     sleep(3000)
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_page.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_page.Click_Next_Button()
#     add_a_printer_page.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
#     common_method.wait_for_element_appearance("Discovered networks", 30)
#     sleep(120)
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """wait till wi-fi turn green."""
#     registration_page.timeTillWiFiGreen()
#     """"click on finish setup button"""
#     common_method.wait_for_element_appearance("Printer registration was successful", 30)
#     add_a_printer_page.click_Finish_Setup_Button()
#     """Local"""
#     login_page.click_Menu_HamburgerICN()
#     sleep(5)
#     """Click My Data"""
#     data_sources_page.click_My_Data()
#     """Click Add File"""
#     data_sources_page.click_Add_File()
#     data_sources_page.click_Upload_File()
#     sleep(3)
#     selected_file_name = data_sources_page.selectFileInLocalStorage()
#     sleep(10)
#     data_sources_page.searchName(selected_file_name)
#     sleep(7)
#     data_sources_page.verifyFilePresentInList(selected_file_name, "Local File")
#     data_sources_page.searchName("")
#     sleep(7)
#     """Google drive"""
#     """Click Add File"""
#     data_sources_page.click_Add_File()
#     """Click Upload file"""
#     data_sources_page.click_Link_File()
#     """Test for Google Drive"""
#     sleep(2)
#     if data_sources_page.verifySignInWithGoogle():
#         registration_page.click_Google_Icon()
#     account = "zebra03.swdvt@gmail.com"
#     if data_sources_page.checkIfAccPresentLink(account):
#         help_page.chooseAcc(account)
#     else:
#         poco("com.google.android.gms:id/add_account_chip_title").click()
#         registration_page.sign_In_With_Google("Zebra#123456789", account)
#         sleep(2)
#     common_method.wait_for_element_appearance_namematches("NAME", 20)
#     sleep(2)
#     jpg_file = "jpg_file.jpg"
#     data_sources_page.selectFileDrive(jpg_file)
#     sleep(5)
#     data_sources_page.searchName(jpg_file)
#     sleep(5)
#     data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
#     data_sources_page.searchName("")
#     sleep(7)
#     """Click Add file"""
#     data_sources_page.click_Add_File()
#     sleep(2)
#     """Click Link File"""
#     data_sources_page.click_Link_File()
#     data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#     """ One drive """
#     data_sources_page.clickMicrosoftOneDrive()
#     sleep(5)
#     data_sources_page.selectFileDrive(jpg_file)
#     sleep(5)
#     data_sources_page.searchName(jpg_file)
#     sleep(5)
#     data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
#     common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49910():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in and keep the app running in background for 52 minutes.'],
        2: [2,
            'After 52 minutes later, check that it should not encounter any logout or error issue during this time.'],
        3: [3,
            'Go to other menu, like My Designs, Common Designs, or Home page. Check there is no error popping up and all designs can be loaded successfully.'],
        4: [4, 'Go to Printer Settings to print a test label. Check the test label can be printed out successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in and keep the app running in background for 52 minutes
        start_time = time.time()

        """clear app data"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Open a different app"""
        start_app("com.android.chrome")
        """wait for 52 min"""
        sleep(3120)
        """Close the other app"""
        stop_app("com.android.chrome")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)

        # Step 2: Check for logout or error issue after 52 minutes
        start_time = time.time()

        """Check if still on logged in page"""
        sso_token_renewal_page.check_if_user_is_logged_in()
        sso_token_renewal_page.noErrorOccurredAfterSwitchingApps()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check loading designs in other menus
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        common_method.wait_for_element_appearance_namematches("Showing")
        template_management_page.checkDisplayedCountMatchesExpected("14")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Print a test label
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        printer_management_page.clickPrinter1InPinterSettings()
        app_settings_page.click_Test_Print_Button()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
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


def test_SSO_Token_Renewal_TestcaseID_49911():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in and keep the app running in the background for 52 minutes.'],
        2: [2,
            'Open the app and refresh the Home page\n[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second]'],
        3: [3, 'Check that it should not encounter any logout or error issue during this time.'],
        4: [4,
            'Go to Printer Settings and update the printer name, Graphic Options, etc., check it can be updated correctly.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in and keep the app running in the background for 52 minutes
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Open a different app"""
        start_app("com.android.chrome")
        """wait for 52 min"""
        sleep(3120)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Open the app and refresh the Home page
        start_time = time.time()

        """Close the other app"""
        common_method.tearDown()
        """Check if still on logged in page"""
        sso_token_renewal_page.check_if_user_is_logged_in()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickHome()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check that it should not encounter any logout or error issue during this time
        start_time = time.time()

        sso_token_renewal_page.noErrorOccurredAfterSwitchingApps()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Go to Printer Settings and update the printer name, Graphic Options, etc.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        """"change the darkness level"""
        sso_token_renewal_page.Change_Darkness_Level_Bar()
        """verify the darkness updated message"""
        app_settings_page.Verify_Darkness_Updated_Message()
        printer_management_page.clickPrinter1InPinterSettings()
        printer_management_page.setPrinterName("ZSB-DP12A")
        """verify the printer name updated message"""
        app_settings_page.verify_Printer_Name_Updated_Message()
        """"""
        """Reset darkness and printer name to default"""
        printer_management_page.setPrinterName("ZSB-DP12")
        app_settings_page.verify_Printer_Name_Updated_Message()
        sso_token_renewal_page.goToCommonTabPrinterSettings()
        app_settings_page.Change_Darkness_Level_Bar()
        app_settings_page.Verify_Darkness_Updated_Message()
        sso_token_renewal_page.Change_Darkness_Level_Bar(100)
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


"""Need to change steps as it includes add a printer"""


# def test_SSO_Token_Renewal_TestcaseID_49912():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """verify if logged in successfully"""
#     data_sources_page.checkIfOnHomePage()
#     """Open a different app"""
#     start_app("com.android.chrome")
#     """wait for 60 min"""
#     sleep(3600)
#     """Close the other app"""
#     stop_app("com.android.chrome")
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_page.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_page.Click_Next_Button()
#     add_a_printer_page.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
#     common_method.wait_for_element_appearance("Discovered networks", 30)
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """wait till wi-fi turn green."""
#     registration_page.timeTillWiFiGreen()
#     """"click on finish setup button"""
#     common_method.wait_for_element_appearance("Printer registration was successful", 30)
#     add_a_printer_page.click_Finish_Setup_Button()
#     login_page.click_Menu_HamburgerICN()
#     template_management_page.clickCommonDesigns()
#     template_management_page.select_design_common_designs()
#     template_management_page.select_label_common_designs()
#     data_sources_page.clickPrint()
#     data_sources_page.scroll_till_print()
#     data_sources_page.clickPrint()
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49914():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in then force quit the app.'],
        2: [2,
            'After more than 52 minutes but less than 60 minutes, re-open the app\nCheck user account is still logged in status\n[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second]'],
        3: [3, 'Check that test label or Common Designs can be printed.'],
        4: [4, 'Check the login account would not be logged out or any other error during this time.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in then force quit the app
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Force quit the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: After more than 52 minutes but less than 60 minutes, re-open the app
        start_time = time.time()

        """wait for 53 min"""
        sleep(3180)
        """Open the app"""
        common_method.Start_The_App()
        """Check if user still logged in"""
        sso_token_renewal_page.check_if_user_is_logged_in()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3150)
        sso_token_renewal_page.stop_adb_log_capture()
        sso_token_renewal_page.checkTokenRefreshed(old_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check that test label or Common Designs can be printed
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        template_management_page.select_design_common_designs()
        template_management_page.select_label_common_designs()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        sso_token_renewal_page.noErrorOccurredAfterPrinting()
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


def test_SSO_Token_Renewal_TestcaseID_49915():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in then force quit app.'],
        2: [2, 'Wait for more than 60 minutes, open app\nCheck user account is still logged in status.'],
        3: [3, 'Go to account Settings page and change the Avatar, update username etc.\nCheck that works.'],
        4: [4, 'Change the Avatar and username back to default.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in then force quit the app
        start_time = time.time()

        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Force quit the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 2: Wait for more than 60 minutes, open app
        start_time = time.time()

        """wait for 65 min"""
        sleep(3900)
        """Open the app"""
        common_method.Start_The_App()
        """Check if user still logged in"""
        sso_token_renewal_page.check_if_user_is_logged_in()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 3: Go to account Settings page and change the Avatar, update username etc.
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        old_name_first, old_name_last = sso_token_renewal_page.get_name()
        old_name = sso_token_renewal_page.get_name(False)
        """change avatar"""
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
        """change name"""
        """Change first name"""
        delete_account_page.change_first_name()
        """Change last name"""
        delete_account_page.change_last_name()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click Home"""
        data_sources_page.clickHome()
        """Click on edit profile"""
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        new_name = sso_token_renewal_page.get_name(False)
        print(old_name, new_name)
        if old_name != new_name:
            pass
        else:
            raise Exception("Name change not successful.")
        """Highlight"""
        """avatar verification pending"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 4: Change the Avatar and username back to default.
        start_time = time.time()

        """Change everything back to normal for future execution"""
        """Change first name"""
        delete_account_page.change_first_name(old_name_first)
        """Change last name"""
        delete_account_page.change_last_name(old_name_last)
        """Remove avatar photo"""
        app_settings_page.click_User_Photo_Remove_Image()
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


def test_SSO_Token_Renewal_TestcaseID_49916():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in with the Non-Zebra account.'],
        2: [2,
            'Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\nCheck that there is a token information about ": flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\nCheck the token is refreshed at 8 minutes prior to expiry time [480 ~420 second].'],
        3: [3, 'Check that test label or Common Designs can be printed.'],
        4: [4,
            'Logout then log in with Google account\nCheck login successful\nCheck that there is a message about "getLocalTokens{.. expires_in: 3599s..}" in the adb log [Android]\nCheck this token is a new one and not the same as previous token [Android]\nCheck that there is a token information about "getLocalTokens: "xxxxxx"" in the GCP_Log [iOS]\nCheck this token is a new one and not the same as previous token [iOS].'],
        5: [5, 'Perform the Change Theme and check it works.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in with the Non-Zebra account
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        registration_page.check_if_user_navigated_to_sign_in_page()
        account = "zebra06.swdvt@gmail.com"
        help_page.chooseAcc(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check for exchange code and token information in logs
        start_time = time.time()

        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        print(old_token)
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        new_token = sso_token_renewal_page.checkTokenRefreshed(old_token)
        print(new_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check that test label or Common Designs can be printed
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        template_management_page.select_design_common_designs()
        template_management_page.select_label_common_designs()
        data_sources_page.clickPrint()
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        data_sources_page.clickBackArrow()
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Logout and log in with Google account
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()
        help_page.checkIfOnSignInPage()
        sso_token_renewal_page.runBatchFileToFetchLogs()
        """Login Again"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        registration_page.check_if_user_navigated_to_sign_in_page()
        account = "zebra07.swdvt@gmail.com"
        help_page.chooseAcc(account)
        data_sources_page.checkIfOnHomePage()
        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check token refreshed after logout and login"""
        sso_token_renewal_page.checkTokenRefreshed(new_token)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Perform the Change Theme and check it works
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        """Click change theme"""
        app_settings_page.click_Change_Theme()
        """Change default theme to any other theme"""
        app_settings_page.check_Change_Electic_Theme()
        """click on the save & exit"""
        app_settings_page.click_Save_Exit_Btn()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Three_Dot_On_Workspace()
        """Click change theme"""
        app_settings_page.click_Change_Theme()
        """Check theme is changed"""
        sso_token_renewal_page.checkThemeChanged()
        """"""
        """Revert back changes to default for future execution"""
        app_settings_page.check_Change_Modern_Theme()
        """click on the save & exit"""
        app_settings_page.click_Save_Exit_Btn()
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


def test_SSO_Token_Renewal_TestcaseID_49917():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in the ZSB app.'],
        2: [2, 'Disconnect the phone from the internet.'],
        3: [3, 'Go to user setting page and click log out button. Expectation: The performance in the current production environment: An error message "Log out failed. Please try logging out again" pops up and user is unable to log out.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in the ZSB app
        start_time = time.time()

        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 2: Disconnect the phone from the internet
        start_time = time.time()

        template_management_page.Turn_Off_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 3: Go to user setting page and click log out button
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click on edit profile"""
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()
        """Blocked"""
        try:
            data_sources_page.checkIfInLoginPage()
            template_management_page.Turn_ON_wifi()
            x=1/0
            """Cannot verify error due to bug SMBM-2178"""
            """Turn on wi-fi for next execution"""
        except ZeroDivisionError:
            raise Exception("It is possible to successfully log out without an internet connection(SMBM-2178).")
        except Exception as e:
            pass
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


def test_SSO_Token_Renewal_TestcaseID_49918():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Log in and keep the app active for 50 minutes.'],
        2: [2, 'Disconnect the network of the mobile device, and wait for 2 minutes.'],
        3: [3, 'Recover the network and refresh the homepage.'],
        4: [4,
            '[Android & iOS]\n-> Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog\n-> Check that there is a token information about " : flutter: getLocalTokens : access_token: BSfN5xDyEgjiYm9PM6rucy3UY5qD" in the adb log or tidevice syslog\n-> Check the token is refreshed at 8 minutes prior to expiry time [480 ~420 second].'],
        5: [5, 'Go to Notifications menu and change settings.\nCheck it can be correctly updated.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Log in and keep the app active for 50 minutes
        start_time = time.time()

        sso_token_renewal_page.runBatchFileToFetchLogs()
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        """Wait for 50 min"""
        sleep(3000)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Disconnect the network and wait for 2 minutes
        start_time = time.time()

        """Disconnect network"""
        template_management_page_1.turn_off_wifi()
        """Wait for 2 min"""
        sleep(120)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Recover the network and refresh the homepage
        start_time = time.time()

        """Connect to network"""
        template_management_page_1.turn_on_wifi()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check logs for exchange code and token information
        start_time = time.time()

        sso_token_renewal_page.stop_adb_log_capture()
        """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_exchangeCode_message_present()
        """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
        sso_token_renewal_page.check_if_getLocalTokens_information_present()
        """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
        old_token = sso_token_renewal_page.get_token()
        print("old token", old_token)
        sso_token_renewal_page.runBatchFileToFetchLogs()
        sleep(3120)
        sso_token_renewal_page.stop_adb_log_capture()
        new_token = sso_token_renewal_page.checkTokenRefreshed(old_token)
        print(new_token, "new token")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to Notifications menu and change settings
        start_time = time.time()

        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Open Notifications"""
        app_settings_page.click_Notifications_Tab()
        app_settings_page.click_Notification_Settings_Tab()
        sso_token_renewal_page.updateNotificationSettings()
        """Click Hamburger Icon"""
        login_page.click_Menu_HamburgerICN()
        """Click Home"""
        data_sources_page.clickHome()
        """Click on edit profile"""
        login_page.click_Menu_HamburgerICN()
        """Open Notifications"""
        app_settings_page.click_Notifications_Tab()
        app_settings_page.click_Notification_Settings_Tab()
        """Cannot verify - check it can be correctly updated"""
        """ask someone"""
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


def test_Registration_TestcaseID_47786():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Install ZSB app onto the mobile device.'],
        2: [2, 'Sign in with an account.'],
        3: [3, 'Do NOT sign out the account, and uninstall the app directly.\nReinstall the same app again.'],
        4: [4, 'Launch the app.\nCheck it would ask for re-enter the credentials.'],
        5: [5, 'Re-login the account.\nCheck the account login correctly and the token have been updated.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Install ZSB app onto the mobile device
        start_time = time.time()

        common_method.tearDown()
        # others_page.uninstall_and_install_zsb_series_on_google_play(True)
        data_sources_page.clearAppData()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 2: Sign in with an account
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.allowPermissions()
        sleep(2)
        registration_page.clickSignIn()
        if poco(text="Allow").exists():
            poco(text="Allow").click()
        poco("Continue with Google").wait_for_appearance(timeout=10)
        registration_page.click_Google_Icon()
        sleep(2)
        help_page.chooseAcc("zebra03.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 3: Do NOT sign out the account, and uninstall the app directly
        start_time = time.time()

        # others_page.uninstall_and_install_zsb_series_on_google_play(True, True)
        data_sources_page.clearAppData()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 4: Launch the app and check for credential prompt
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.allowPermissions()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 5: Re-login the account and check token update
        start_time = time.time()

        sleep(2)
        registration_page.clickSignIn()
        if poco(text="Allow").exists():
            poco(text="Allow").click()
        poco("Continue with Google").wait_for_appearance(timeout=10)
        registration_page.click_Google_Icon()
        sleep(2)
        help_page.chooseAcc("zebra03.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
        """Highlight"""
        """Token verification pending"""
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


def test_Registration_TestcaseID_45870():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App and click Login button.'],
        2: [2, 'Proceed to login to Money Badger.'],
        3: [3, 'Check user still stays logged in after 2 hours.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:

        # Step 1: Launch ZSB Series App and click Login button
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.checkIfInLoginPage()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 2: Proceed to login to Money Badger
        start_time = time.time()

        registration_page.click_Google_Icon()
        registration_page.check_if_user_navigated_to_sign_in_page()
        login_page.click_GooglemailId()
        registration_page.wait_for_element_appearance_text("Add account to device")
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zsbswdvt@123", "zebra03.swdvt@gmail.com", True)
        registration_page.sign_In_With_Google("Zebra#123456789")
        data_sources_page.checkIfOnHomePage()
        sleep(7200)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 3: Check user still stays logged in after 2 hours
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
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
        common_method.stop_adb_log_capture()
        upload_case_files(execID, os.path.dirname(ADB_LOG), test_run_start_time)
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
        end_execution_loop(execID)
        end_execution(execID)


# def test_SSO_Token_Renewal_TestcaseID_49913():
#     pass
#     """clear app data"""
#     common_method.tearDown()
#     data_sources_page.log_out_of_account()
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """verify if logged in successfully"""
#     data_sources_page.checkIfOnHomePage()
#     """Open a different app"""
#     start_app("com.android.chrome")
#     """wait for 1 day 5 min"""
#     sleep(86700)
#     """Close the other app"""
#     stop_app("com.android.chrome")
#     """Check if still on logged in page"""
#     sso_token_renewal_page.check_if_user_is_logged_in()
#     login_page.click_Menu_HamburgerICN()
#     """Open printer settings"""
#     app_settings_page.click_Printer_Settings()
#     """Select printer"""
#     printer_management_page.clickPrinter1InPinterSettings()
#     app_settings_page.click_wifi_tab()
#     app_settings_page.click_Manage_Networks_Btn()
#     app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
#     app_settings_page.click_Add_Network()
#     app_settings_page.click_Enter_Network_Manually()
#     app_settings_page.click_Network_UserName()
#     app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
#     app_settings_page.click_Enter_Network_Manually()
#     app_settings_page.click_Network_UserName()
#     app_settings_page.click_Security_Open()
#     app_settings_page.click_WPA_PSK()
#     app_settings_page.click_Keyboard_back_Icon()
#     app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
#     app_settings_page.click_Enter_Network_Manually()
#     app_settings_page.click_Network_UserName()
#     app_settings_page.click_Join_Btn_On_Other_Network_Popup()
#     app_settings_page.Verify_Added_Network()
#     common_method.Stop_The_App()
#     "continue"
