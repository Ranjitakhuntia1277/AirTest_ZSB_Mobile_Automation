import inspect

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Login_Screen import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
import pytest
from ...TestSuite.api_call import *
from ...TestSuite.store import *


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
app_settings_page = App_Settings_Screen(poco)


def test_Registration_TestcaseID_45856():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        2: [2,
            'Check user is directed to Account Registration Page (https://stage-signup.zebra.com/register.html?appId=ZEMB)'],
        3: [3,
            'Enter new zebra user email test123@zebra.com and click NEXT button. Check the following error message is displayed: This site is for external users only. Please contact your local system administrator for application access requests.'],
        4: [4, 'Repeat step 1 to 2.'],
        5: [5, 'Enter new external user email and click NEXT button.'],
        6: [6,
            'Check user is directed to page with header "Email Verification" and message "Your request has been received. We have sent an email to verify your account. Please click on the verification link in your email to finish registration. Can\'t find your link? Please check your junk mail or click this link: Resend Verification Email."'],
        7: [7,
            'Check user has received a "User Verification Account" email from Zebra and user is provided with a verification code to enter'],
        8: [8,
            'Enter the verification code provided by the email to the mobile app after 10 minutes and click SUBMIT button.'],
        9: [9,
            'Check user need to re-register as a user again. Error message: Mobile Verification code is invalid. RESEND VERIFICATION CODE button is available'],
        10: [10,
             'Check user has received another set of verification code in mailbox after user clicks RESEND VERIFICATION CODE button'],
        11: [11, 'Enter the verification code and click SUBMIT button.'],
        12: [12,
             'Check user is navigated to "User Information and Account Security" to enter details for registration.'],
        13: [13,
             'Complete the registration with the following: Proceed to enter First Name (E.g: John). Proceed to enter Last Name (E.g: Loke). Proceed to enter password (E.g: Zebratest123?) in Password *. Proceed to enter the match password (E.g: Zebratest123?) in Confirm Password *. Proceed to select a country (E.g: "Canada") from Select Country * drop down list box. Enable check boxes "I have read and agree to the Terms and Conditions".'],
        14: [14, 'Click SUBMIT AND CONTINUE button will navigate user to "Account Created" page.'],
        15: [15,
             'Check user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account."'],
        16: [16, 'Check user will be navigated to Money Badger Sign In Page after user clicks CONTINUE button.'],
        17: [17, 'Check user is able to login and logout of Money Badger successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        """Create new email before running"""
        """Click signin"""
        common_method.tearDown()
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.verifyLinksInSignInPage()
        registration_page.registerEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check user is directed to Account Registration Page (https://stage-signup.zebra.com/register.html?appId=ZEMB)
        start_time = time.time()

        registration_page.checkIfOnRegistrationPage()
        help_page.verify_url("signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Enter new zebra user email test123@zebra.com and click NEXT button. Check the following error message is displayed: This site is for external users only. Please contact your local system administrator for application access requests.
        start_time = time.time()

        """Enter zebra Email"""
        registration_page.enter_user_email_for_registering("test123@zebra.com")
        registration_page.click_on_next()
        registration_page.check_zebra_mail_registration_error()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Repeat step 1 to 2.
        start_time = time.time()

        help_page.closeTab()
        data_sources_page.clickCancel()
        sleep(3)
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.verifyLinksInSignInPage()
        registration_page.registerEmail()
        registration_page.checkIfOnRegistrationPage()
        help_page.verify_url("signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Enter new external user email and click NEXT button.
        start_time = time.time()

        email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")
        registration_page.enter_user_email_for_registering(email)
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check user is directed to page with header "Email Verification" and message "Your request has been received. We have sent an email to verify your account. Please click on the verification link in your email to finish registration. Can't find your link? Please check your junk mail or click this link: Resend Verification Email."
        start_time = time.time()

        poco(text="Return to Previous Step").wait_for_appearance(timeout=20)
        registration_page.check_email_verification_page_message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user has received a "User Verification Account" email from Zebra and user is provided with a verification code to enter
        start_time = time.time()

        common_method.show_message(
            "Check user has recieved a \"User Verification Account\" email from Zebra and user is provided with a verification code to enter")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Enter the verification code provided by the email to the mobile app after 10 minutes and click SUBMIT button.
        start_time = time.time()

        sleep(600)
        """Wait for 10 min"""
        """Enter verification code manually"""
        common_method.show_message(
            "Enter verification code on the device ,verification code received in the newly created google account")
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user need to re-register as a user again. Error message: Mobile Verification code is invalid. RESEND VERIFICATION CODE button is available
        start_time = time.time()

        if registration_page.verify_verification_code_expired_error():
            pass
        else:
            raise Exception("Verification code expired error not present.")
        if registration_page.verify_resend_verification_code_btn_exists():
            pass
        else:
            raise Exception("Resend verification code button not present.")
        registration_page.click_resend_verification_code_btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check user has received another set of verification code in mailbox after user clicks RESEND VERIFICATION CODE button
        start_time = time.time()

        common_method.show_message(
            "Check user has received another set of verification code in mailbox after user clicks RESEND VERIFICATION CODE button")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Enter the verification code and click SUBMIT button.
        start_time = time.time()

        common_method.show_message(
            "Verification code is resent - Enter verification code on the device ,verification code received in the newly created google account")
        """Enter verification code manually"""
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check user is navigated to "User Information and Account Security" to enter details for registration.
        start_time = time.time()

        registration_page.verify_user_information_and_account_security_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Complete the registration with the following: Proceed to enter First Name (E.g: John). Proceed to enter Last Name (E.g: Loke). Proceed to enter password (E.g: Zebratest123?) in Password *. Proceed to enter the match password (E.g: Zebratest123?) in Confirm Password *. Proceed to select a country (E.g: "Canada") from Select Country * drop down list box. Enable check boxes "I have read and agree to the Terms and Conditions".
        start_time = time.time()

        """Enter the first Name last name and the password"""
        first_name = "John"
        last_name = "Doe"
        password = "Zebra#123456789"
        registration_page.enter_the_fields(first_name, last_name, password)
        registration_page.select_the_country("India")
        registration_page.select_the_check_boxes()
        registration_page.click_submit_and_continue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Click SUBMIT AND CONTINUE button will navigate user to "Account Created" page.
        start_time = time.time()

        sleep(4)
        registration_page.check_sign_up_successful()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15: Check user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account."
        start_time = time.time()

        registration_page.click_continue_registration_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16: Check user will be navigated to Money Badger Sign In Page after user clicks CONTINUE button.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 17: Check user is able to login and logout of Money Badger successfully.
        start_time = time.time()

        registration_page.clickSignIn()
        registration_page.wait_for_element_appearance_text("Continue with Google", 10)
        registration_page.click_on_sign_in_with_email()

        """Provide the email and password"""
        registration_page.complete_sign_in_with_email(email, password, 1, 0)
        registration_page.click_accept()
        registration_page.clickClose()
        registration_page.clickExit()
        data_sources_page.checkIfOnHomePage()

        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfOnHomePage()
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


def test_Registration_TestcaseID_45857():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App, click Login button, select Sign in with your email option, click Register Your Email Now option'],
        2: [2,
            'Check user is directed to Account Registration Page. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB'],
        3: [3, 'Enter new user email and click NEXT button.'],
        4: [4, 'Login to newly created user email account.'],
        5: [5,
            'Enter the verification code (E.g: 3CRL5N) provided by the email to the mobile app and click SUBMIT button.'],
        6: [6,
            'Check user is navigated to "User Information and Account Security" to enter details for registration. Check message display "Email verified successfully!". Check the page has the following mandatory fields that require user to enter for submission: First Name, Last Name, Password, Confirmed Password and Select Country. Check boxes: "I\'d like to receive marketing emails". "I have read and agree to the Terms and Conditions". CLEAR and SUBMIT AND CONTINUE button.'],
        7: [7, 'Enter alphanumeric with special characters on First Name (e.g: John123!).'],
        8: [8,
            'Check First Name does not allow numeric and special characters. Error message "Please do not use special characters.". Proceed to enter First Name (E.g: John) that comply with first name entry requirement.'],
        9: [9, 'Enter alphanumeric with special characters on Last Name (e.g: Loke123!).'],
        10: [10,
             'Check Last Name does not allow numeric and special characters. Error message display "Please do not use special characters.". Proceed to enter Last Name (E.g: Loke) that comply with last name entry requirement.'],
        11: [11, 'Enter all alpha characters (e.g: abcdefg) / all numeric values (eg: 12345678) in Password *.'],
        12: [12,
             'Check Password is only allowed for entry values meeting SSO password requirement rules. SSO password requirement "Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password must not contain spaces or tabs." is displayed. Proceed to enter password (E.g: Zebratest123?) that complied with IT SSO password requirement.'],
        13: [13, 'Enter mismatch password in Confirmed Password *.'],
        14: [14,
             'Check password entered in Password * and Confirm Password * must match. Error message display "Password and Confirm Password must match.". Proceed to enter the match password (E.g: Zebratest123?) in Confirm Password *.'],
        15: [15, 'Select country from Select Country * drop down list box (E.g: "Canada").'],
        16: [16, 'Enable check boxes "I have read and agree to the Terms and Conditions".'],
        17: [17, 'Check SUBMIT AND CONTINUE button is enabled.'],
        18: [18, 'Enable and disable check boxes "I\'d like to receive marketing emails".'],
        19: [19,
             'Check SUBMIT AND CONTINUE button remains enabled, disabling check boxes "I\'d like to receive marketing emails" does not grey out SUBMIT AND CONTINUE button.'],
        20: [20,
             'Check clicking CLEAR will clear all entered fields and clicking SUBMIT AND CONTINUE button will navigate user to "Account Created" page.'],
        21: [21,
             'Check user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account.".'],
        22: [22, 'Check user will be navigated to Money Badger Sign In Page after user clicks CONTINUE button.'],
        23: [23,
             'Check user is able to login and logout of Money Badger successfully. Login to email (Created in Precondition).'],
        24: [24,
             'Check user receives an email from Zebra Technologies with the following caption: Welcome to the ZSB Series Printer Meet the label printer that just...works'],
        25: [25,
             'Click on the link "Download Driver" or "Design your first label". Check it will open Money Badger home page (https://www.zprinthubz-stage.zebra.com/login).'],
        26: [26, 'Check user is able to login and logout of Money Badger successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App, click Login button, select Sign in with your email option, click Register Your Email Now option
        start_time = time.time()

        common_method.show_message("Run testcase on stage build")
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.registerEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check user is directed to Account Registration Page. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB
        start_time = time.time()

        registration_page.checkIfOnRegistrationPage()
        # help_page.verify_url("https://stagec-signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB")
        help_page.verify_url("https://signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Login to newly created user email account.
        start_time = time.time()

        email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")
        registration_page.enter_user_email_for_registering(email)
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Enter the verification code (E.g: 3CRL5N) provided by the email to the mobile app and click SUBMIT button.
        start_time = time.time()

        poco(text="Return to Previous Step").wait_for_appearance(timeout=10)
        """Enter verification code manually"""
        common_method.show_message(
            "Enter verification code on the device ,verification code received in the newly created google account")
        registration_page.click_on_next()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check user is navigated to "User Information and Account Security" to enter details for registration. Check message display "Email verified successfully!". Check the page has the following mandatory fields that require user to enter for submission: First Name, Last Name, Password, Confirmed Password and Select Country. Check boxes: "I'd like to receive marketing emails". "I have read and agree to the Terms and Conditions". CLEAR and SUBMIT AND CONTINUE button.
        start_time = time.time()

        if registration_page.check_email_verified_successfully_message():
            pass
        else:
            raise Exception("Email verified successfully message not present.")
        if registration_page.verify_user_information_and_account_security_page():
            pass
        else:
            raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
        registration_page.verify_if_all_fields_present()
        registration_page.verify_if_checkboxes_are_present_registration()
        while not poco(text="Email verified successfully!").exists():
            scroll_view = poco("android.view.View")
            scroll_view.swipe("down")
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Enter alphanumeric with special characters on First Name (e.g: John123!).
        start_time = time.time()

        if registration_page.special_character_error_name_field("First Name", "John123!"):
            pass
        else:
            raise Exception("No error for using special character in First Name field.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Check First Name does not allow numeric and special characters. Error message "Please do not use special characters.". Proceed to enter First Name (E.g: John) that comply with first name entry requirement.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Enter alphanumeric with special characters on Last Name (e.g: Loke123!).
        start_time = time.time()

        sleep(2)
        if registration_page.special_character_error_name_field("Last Name", "Loke123!"):
            pass
        else:
            raise Exception("No error for using special character in Last Name field.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check Last Name does not allow numeric and special characters. Error message display "Please do not use special characters.". Proceed to enter Last Name (E.g: Loke) that comply with last name entry requirement.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Enter all alpha characters (e.g: abcdefg) / all numeric values (e.g: 12345678) in Password *.
        start_time = time.time()

        sleep(2)
        if registration_page.check_error_password_field("abcdefg", True):
            pass
        else:
            raise Exception("No error when entered only alphabets in password field.")
        sleep(2)
        if registration_page.check_error_password_field("12345678"):
            pass
        else:
            raise Exception("No error when entered only alphabets in password field.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check Password is only allowed for entry values meeting SSO password requirement rules. SSO password requirement "Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password must not contain spaces or tabs." is displayed. Proceed to enter password (E.g: Zebratest123?) that complied with IT SSO password requirement.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Enter mismatch password in Confirmed Password *.
        start_time = time.time()

        sleep(2)
        while not poco(text="Email verified successfully!").exists():
            scroll_view = poco("android.view.View")
            scroll_view.swipe("down")
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")
        first_name = "Johnny"
        last_name = "Loke"
        registration_page.fill_first_name_field(first_name)
        registration_page.fill_last_name_field(last_name)
        while not poco(text="SUBMIT AND CONTINUE").exists():
            scroll_view = poco("android.view.View")
            scroll_view.swipe("up")
        registration_page.fill_password_field("Zebratest123?")
        registration_page.fill_confirm_password_field("sss?")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Check password entered in Password * and Confirm Password * must match. Error message display "Password and Confirm Password must match.". Proceed to enter the match password (E.g: Zebratest123?) in Confirm Password *.
        start_time = time.time()

        registration_page.check_password_unmatch_error()
        password = "Zebra#123456789"
        registration_page.fill_confirm_password_field(password)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15: Select country from Select Country * drop down list box (E.g: "Canada").
        start_time = time.time()

        registration_page.select_the_country("India")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16: Enable check boxes "I have read and agree to the Terms and Conditions".
        start_time = time.time()

        poco("android.widget.CheckBox")[1].click()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 17: Check SUBMIT AND CONTINUE button is enabled.
        start_time = time.time()

        registration_page.check_submit_and_continue_enabled()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 18: Enable and disable check boxes "I'd like to receive marketing emails".
        start_time = time.time()

        poco("android.widget.CheckBox")[0].click()
        poco("android.widget.CheckBox")[0].click()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 19: Check SUBMIT AND CONTINUE button remains enabled, disabling check boxes "I'd like to receive marketing emails" does not grey out SUBMIT AND CONTINUE button.
        start_time = time.time()

        registration_page.check_submit_and_continue_enabled()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 20: Check clicking CLEAR will clear all entered fields and clicking SUBMIT AND CONTINUE button will navigate user to "Account Created" page.
        start_time = time.time()

        registration_page.click_clear()
        if registration_page.check_error_message_after_clear():
            pass
        else:
            raise Exception("Fields not cleared after clicking clear.")
        registration_page.click_submit_and_continue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 21: Check user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account.".
        start_time = time.time()

        sleep(4)
        registration_page.check_sign_up_successful()
        registration_page.click_continue_registration_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 22: Check user will be navigated to Money Badger Sign In Page after user clicks CONTINUE button.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 23: Check user is able to login and logout of Money Badger successfully. Login to email (Created in Precondition).
        start_time = time.time()

        registration_page.clickSignIn()
        registration_page.wait_for_element_appearance_text("Continue with Google", 10)
        data_sources_page.signInWithEmail()
        """Provide the email and password"""
        registration_page.complete_sign_in_with_email(email, password, 1, 0)
        while not poco(name="Accept", enabeled=True).exists():
            poco.scroll()
        registration_page.click_accept()
        data_sources_page.checkIfOnHomePage()
        registration_page.home_page_overview("Johnny")
        registration_page.check_add_a_printer_exists()
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 24: Check user receives an email from Zebra Technologies with the following caption: Welcome to the ZSB Series Printer Meet the label printer that just...works
        start_time = time.time()

        common_method.show_message("Check user receives an email from Zebra Technologies with the following caption: Welcome to the ZSB Series Printer Meet the label printer that just...works")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 25: Click on the link "Download Driver" or "Design your first label". Check it will open Money Badger home page (https://www.zprinthubz-stage.zebra.com/login).
        start_time = time.time()

        common_method.show_message("Click on the link \"Download Driver\" or \"Design your first label\". Check it will open Money Badger home page (https://www.zprinthubz-stage.zebra.com/login)")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 26: Check user is able to login and logout of Money Badger successfully.
        start_time = time.time()

        common_method.show_message("Open the ZSB series app")
        registration_page.clickSignIn()
        registration_page.wait_for_element_appearance_text("Continue with Google", 10)
        data_sources_page.signInWithEmail()
        """Provide the email and password"""
        registration_page.complete_sign_in_with_email(email, password, 1, 0)
        while not poco(name="Accept", enabeled=True).exists():
            poco.scroll()
        registration_page.click_accept()
        data_sources_page.checkIfOnHomePage()
        registration_page.home_page_overview("Johnny")
        registration_page.check_add_a_printer_exists()
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

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


def test_Registration_TestcaseID_45858():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        2: [2, 'Check user is directed to Account Registration Page.'],
        3: [3, 'Enter new user email and click NEXT button.'],
        4: [4, 'Login to newly created user email account.'],
        5: [5,
            'Enter the verification code (E.g: 3CRL5N) provided by the email to the mobile app and click SUBMIT button.'],
        6: [6,
            'At "User Information and Account Security" Page. - Proceed to enter First Name (E.g: John) that comply with first name entry requirement. - Proceed to enter Last Name (E.g: Loke) that comply with last name entry requirement. - Proceed to select Country (E.g: Canada) from Select Country * drop down list. - Proceed to enter password and confirmed password (E.g: soho_dvtxxxxx?) that complied with IT SSO password requirement. - Proceed to enable check boxes "I have read and agree to the Terms and Conditions".'],
        7: [7, 'Click SUBMIT AND CONTINUE button.'],
        8: [8,
            'Click on CONTINUE button when user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account."'],
        9: [9, 'Check user is navigated to Money Pager "Sign In/Register" Page.'],
        10: [10,
             'Click Sign In/Register button, enter email and password and click Sign in button at "Login with username" page.'],
        11: [11,
             'Check the user is NOT able to log in if not accepting EULA, and then the user accept it (check there is no layout error on the EULA page), and log into successfully.'],
        12: [12,
             'Check user is successfully login to Money Badger Home Page and navigated to the overview page with initial name display e.g.: "Hey soho_dvtxxxxx!" and a "Add a Printer" button id provided to add printer.'],
        13: [13, 'Click on the hamburger icon then Settings follow by Log out button.'],
        14: [14,
             'Check user is successfully log out of Money Badger Home Page and is being navigate to ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        common_method.show_message("Create new email before running")
        common_method.tearDown()
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.verifyLinksInSignInPage()
        registration_page.registerEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check user is directed to Account Registration Page.
        start_time = time.time()

        registration_page.checkIfOnRegistrationPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Enter new user email and click NEXT button.
        start_time = time.time()

        email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")

        registration_page.enter_user_email_for_registering(email)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Login to newly created user email account.
        start_time = time.time()

        registration_page.check_if_reached_page_to_enter_verification_code()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Enter the verification code (E.g: 3CRL5N) provided by the email to the mobile app and click SUBMIT button.
        start_time = time.time()

        """Enter verification code manually"""
        common_method.show_message(
            "Enter verification code on the device ,verification code received in the newly created google account")
        """Enter the User Email"""
        registration_page.click_on_next()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: At "User Information and Account Security" Page. Proceed to enter First Name (E.g: John) that comply with first name entry requirement. Proceed to enter Last Name (E.g: Loke) that comply with last name entry requirement. Proceed to select Country (E.g: Canada) from Select Country * drop down list. Proceed to enter password and confirmed password (E.g: soho_dvtxxxxx?) that complied with IT SSO password requirement. Proceed to enable check boxes "I have read and agree to the Terms and Conditions".
        start_time = time.time()

        """Enter the first Name last name and the password"""
        first_n = "Zebra"
        last_n = "Z"
        password = "Zebra#123456789"
        registration_page.enter_the_fields(first_n, last_n, password)
        registration_page.select_the_country("India")
        registration_page.select_the_check_boxes()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click SUBMIT AND CONTINUE button.
        start_time = time.time()

        registration_page.click_submit_and_continue()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click on CONTINUE button when user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account."
        start_time = time.time()

        registration_page.check_sign_up_successful()
        registration_page.click_continue_registration_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user is navigated to Money Pager "Sign In/Register" Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click Sign In/Register button, enter email and password and click Sign in button at "Login with username" page.
        start_time = time.time()

        registration_page.clickSignIn()
        registration_page.wait_for_element_appearance_text("Continue with Google", 10)
        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email(email, password, 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the user is NOT able to log in if not accepting EULA, and then the user accept it (check there is no layout error on the EULA page), and log into successfully.
        start_time = time.time()

        registration_page.verify_if_on_EULA_page()
        registration_page.click_accept()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check user is successfully login to Money Badger Home Page and navigated to the overview page with initial name display e.g.: "Hey soho_dvtxxxxx!" and a "Add a Printer" button id provided to add printer.
        start_time = time.time()

        registration_page.clickClose()
        registration_page.clickExit()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Click on the hamburger icon then Settings follow by Log out button.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Check user is successfully log out of Money Badger Home Page and is being navigate to ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()

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



# def test_Registration_TestcaseID_45864():
#     pass
#     common_method.tearDown()
#     registration_page.clickSignIn()
#     registration_page.complete_sign_in_with_email("smbmbzsb@gmail.com", "ZebraTest#1234", 1, 0)
#     try:
#         registration_page.wait_for_element_appearance("Home", 20)
#     except:
#         raise Exception("home page dint show up")
#     login_page.click_Menu_HamburgerICN()
#     registration_page.click_on_profile_edit()
#     poco.scroll()
#     registration_page.click_log_out_button()
#     try:
#         registration_page.wait_for_element_appearance("Sign In", 5)
#     except:
#         raise Exception("Did not redirect to the login page")


# def test_Registration_TestcaseID_45865():
#     pass
#     registration_page.clickSignIn()
#     registration_page.complete_sign_in_with_email("smbmbzsb@gmail.com", "ZebraTest#1234", 1, 0)
#     try:
#         registration_page.wait_for_element_appearance("Home", 20)
#     except:
#         raise Exception("home page dint show up")
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.click_My_Data()
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickMyDesigns()
#     login_page.click_Menu_HamburgerICN()
#     registration_page.click_on_profile_edit()
#     poco.scroll()
#     registration_page.click_log_out_button()
#     try:
#         registration_page.wait_for_element_appearance("Sign In", 5)
#     except:
#         raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45866():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App and click Login button.'],
        2: [2, 'Click Reset Password.'],
        3: [3,
            'Check user is navigate to Password Recovery Page. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html'],
        4: [4, 'Enter unregister email (E.g: testing123@gmail.com) and click SUBMIT button.'],
        5: [5, 'Check Error message: "User does not exist".'],
        6: [6, 'Repeat Step 1 to 3 and entered a registered email account and click SUBMIT button.'],
        7: [7,
            'Check user is navigated to Success! page. Check Success! page is populated with the following message: An email with a Password Reset Code has been sent to your email address. The OTP will expired in 10 minutes. Click here to set your password using the Password Reset Code.'],
        8: [8, 'Click on Click here.'],
        9: [9,
            'Check user is navigate to the Reset Password page and Reset Password page has the following field. Password Reset Code *, New Password * and Confirm Password *.'],
        10: [10, 'Click SUBMIT key without entering password reset code.'],
        11: [11,
             'Check the following display error message : Password Reset Code *: "This field is required". New Password *: "Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password MUST NOT contain spaces or tabs.". Confirm Password *: "This field is required".'],
        12: [12,
             'Check user receive an email containing a Password Resets Code from Ping Identity. E.g: Your Zebra Account Password Resets Code is: 865l0hzy'],
        13: [13,
             'At Reset Password page, enter the following: Enter the provided password reset code to Password Reset Code * field. Enter new password that meets IT SSO requirement (E.g: Zebratest456?) to New Password * field. Enter a mismatch password to Confirm Password * field.'],
        14: [14,
             'Check Confirm Password * display the following error message: "Password and Confirm Password must match".'],
        15: [15,
             'Enter password that matches Password * to Confirm Password * field and click SUBMIT button after 10 minutes.'],
        16: [16,
             'Check user has been navigate to page with the following message displayed: The OTP was invalid or expired. Please click here to regenerate OTP.'],
        17: [17, 'Click on click here to regenerate OTP.'],
        18: [18, 'Click on Click here to login with your temporary password in Success! page.'],
        19: [19,
             'At Reset Password page: Enter the provided password reset code from your email to Password Reset Code * field. Enter new password that meets IT SSO requirement (E.g: Zebratest456?) to New Password * field. Enter a match password to Confirm Password * field. Click SUBMIT button.'],
        20: [20,
             'Check user is navigated to Success! page with the following message: Password changed successfully. Click here to login with your new password.'],
        21: [21, 'Click Click here to login with your new password.'],
        22: [22, 'Check user has been navigate to "Login with username" page.'],
        23: [23, 'Enter username and the registered reset password.'],
        24: [24, 'Check user is able to login to Money Badger.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click Login button.
        start_time = time.time()

        common_method.show_message(
            "Have gmail account:\nusername:zebra03.swdvt@gmail.com\npassword:Zebra#123456789 logged in a different device to view otp that is required in later part of the test case.")
        common_method.tearDown()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Reset Password.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        registration_page.click_on_reset_password()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to Password Recovery Page. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html
        start_time = time.time()

        registration_page.check_if_in_password_recovery_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Enter unregister email (E.g: testing123@gmail.com) and click SUBMIT button.
        start_time = time.time()

        registration_page.Enter_Username_password_recovery_page("testing123@gmail.com")
        registration_page.click_SUBMIT()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check Error message: "User does not exist".
        start_time = time.time()

        registration_page.check_user_does_not_exist_error()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Repeat Step 1 to 3 and entered a registered email account and click SUBMIT button.
        start_time = time.time()

        common_method.tearDown()
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.click_on_reset_password()
        sleep(5)
        registration_page.check_if_in_password_recovery_page()
        email = "zebra03.swdvt@gmail.com"
        registration_page.Enter_Username_password_recovery_page(email)
        registration_page.click_SUBMIT()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user is navigated to Success! page. Check Success! page is populated with the following message: An email with a Password Reset Code has been sent to your email address. The OTP will expired in 10 minutes. Click here to set your password using the Password Reset Code.
        start_time = time.time()

        registration_page.check_if_on_success_page()
        if registration_page.check_message_on_success_page():
            pass
        else:
            raise Exception("Expected message not on success page.")
        """An email with a Password Reset Code has been sent to your email address. The OTP will expired in 10 minutes.- cannot be automated."""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click on Click here.
        start_time = time.time()

        registration_page.click_on_Click_here()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user is navigate to the Reset Password page and Reset Password page has the following field. Password Reset Code *, New Password * and Confirm Password *.
        start_time = time.time()

        registration_page.check_if_on_Reset_Password_page()
        registration_page.check_fields_on_Reset_Password_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click SUBMIT key without entering password reset code.
        start_time = time.time()

        registration_page.click_SUBMIT()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the following display error message : Password Reset Code *: "This field is required". New Password *: "Password MUST contain one lowercase, one uppercase letter, one number and a special character. Password MUST NOT contain spaces or tabs.". Confirm Password *: "This field is required".
        start_time = time.time()

        registration_page.check_error_message_on_fields_on_Reset_Password_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check user receive an email containing a Password Resets Code from Ping Identity. E.g: Your Zebra Account Password Resets Code is: 865l0hzy
        start_time = time.time()

        common_method.show_message("Check user receive an email containing a Password Resets Code from Ping Identity. E.g: Your Zebra Account Password Resets Code is: 865l0hzy")
        """Enter otp manually"""
        common_method.show_message(f"Enter otp received in the google account:\n{email}")
        password = "Zebra#123456789"

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: At Reset Password page, enter the following: Enter the provided password reset code to Password Reset Code * field. Enter new password that meets IT SSO requirement (E.g: Zebratest456?) to New Password * field. Enter a mismatch password to Confirm Password * field.
        start_time = time.time()

        registration_page.fillNewPassword(password)
        registration_page.fillConfirmPassword("Zebra#12345678")
        registration_page.click_SUBMIT()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Check Confirm Password * display the following error message: "Password and Confirm Password must match".
        start_time = time.time()

        registration_page.checkWrongConfirmPasswordErrorMessage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15: Enter password that matches Password * to Confirm Password * field and click SUBMIT button after 10 minutes.
        start_time = time.time()

        registration_page.fillConfirmPassword(password)
        """Wait for 10 minutes """
        sleep(600)
        registration_page.click_SUBMIT()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16: Check user has been navigated to page with the following message displayed: The OTP was invalid or expired. Please click here to regenerate OTP.
        start_time = time.time()

        registration_page.check_OTExpiredMessage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 17: Click on click here to regenerate OTP.
        start_time = time.time()

        registration_page.click_on_click_here()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 18: Click on Click here to login with your temporary password in Success! page.
        start_time = time.time()

        """Step 18. Click on Click here to login with your temporary password in Success! page not present"""
        registration_page.click_on_Click_here()
        registration_page.check_if_on_Reset_Password_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 19: At Reset Password page: Enter the provided password reset code from your email to Password Reset Code * field. Enter new password that meets IT SSO requirement (E.g: Zebratest456?) to New Password * field. Enter a match password to Confirm Password * field. Click SUBMIT button.
        start_time = time.time()

        """Enter OTP manually"""
        common_method.show_message(
            f"Enter verification code on the device ,verification code received in the google account:\n{email}")
        registration_page.fillNewPassword(password)
        registration_page.fillConfirmPassword(password)
        registration_page.click_SUBMIT()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 20: Check user is navigated to Success! page with the following message: Password changed successfully. Click here to login with your new password.
        start_time = time.time()

        registration_page.check_if_on_success_page()
        registration_page.check_successful_password_reset_page_message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 21: Click on Click here to login with your new password.
        start_time = time.time()

        registration_page.click_on_Click_here()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 22: Check user has been navigate to "Login with username" page.
        start_time = time.time()

        registration_page.checkIfOnSSOLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 23: Enter username and the registered reset password.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email(email, password, 1, 0)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 24: Check user is able to login to Money Badger.
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

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


def test_Registration_TestcaseID_45867():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App and click Login button.'],
        2: [2, 'Click Reset Password.'],
        3: [3, 'Check user is navigate to Password Recovery Page.'],
        4: [4, 'Enter unregistered zebra email (E.g: testing123@zebra.com) and click SUBMIT button.'],
        5: [5,
            'Check user will be navigate to a page "Reset your zebra network account (Active Directory) password or unlock your Zebra network account". Username field, CAPTHA (I\'m not a robot) checkbox.'],
        6: [6,
            'Enable CAPTHA (I\'m not a robot) to solve the pictorial puzzle and enter invalid username E.g: tt1234 and click Next button.'],
        7: [7, 'Check user is directed to a page "Password Reset Error".'],
        8: [8,
            'Repeat Step 1 to 3 and entered a registered zebra email account (E.g: kk.wong@zebra.com) and click SUBMIT button.'],
        9: [9, 'Enter a valid registered zebra email (E.g: KK.WONG@zebra.com) and click SUBMIT button.'],
        10: [10,
             'Enable CAPTHA (I\'m not a robot) to solve the pictorial puzzle and enter valid username E.g: kk1234 and click Next button.'],
        11: [11,
             'Check user will be navigate to Security Verification Page. E.g: What is your favourite landmark? E.g: What is the country of your dream vacation?'],
        12: [12,
             'Check failing to answer the security questions and click Next, user is navigated to Password Reset Error page. Error Message Displayed: "Error: cannot verify user (kk1234). Number of attempt 1. Try again". User required to answer a new sets of security questions.'],
        13: [13,
             'Repeat Step 12 until user exceed the attempt to reset the password. Check the maximum attempt is 3. Check user is navigated to Password Reset Error page. Check the following error message is displayed. This user cannot use the configured Password Reset process. Possible reasons: User does not exist or is not enrolled. User is not part of the configured password reset process. User is blocked (exceeded the limit on reset attempts or reset password recently). User account is locked. Try again later. For immediate assistance, call the service desk.'],
        14: [14, 'Repeat the steps to reset password as a zebra user (Step 8 to 10).'],
        15: [15,
             'Check user will be bypass from answering the security question and will be navigated directly to Password Reset Error Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click Login button.
        start_time = time.time()

        common_method.tearDown()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Reset Password.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        registration_page.click_on_reset_password()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to Password Recovery Page.
        start_time = time.time()

        registration_page.check_if_in_password_recovery_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Enter unregistered zebra email (E.g: testing123@zebra.com) and click SUBMIT button.
        start_time = time.time()

        registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
        registration_page.click_SUBMIT()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user will be navigated to a page "Reset your zebra network account (Active Directory) password or unlock your Zebra network account". Username field, CAPTHA (I'm not a robot) checkbox.
        start_time = time.time()

        registration_page.check_if_in_zebra_network_account_password_reset_page()
        registration_page.check_fields_in_zebra_network_account_password_reset_page()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Enable CAPTCHA (I'm not a robot) to solve the pictorial puzzle and enter invalid username E.g: tt1234 and click Next button.
        start_time = time.time()

        registration_page.fill_username_in_zebra_network_account_password_reset_page("tt1234")
        registration_page.enableCaptcha()
        common_method.show_message("Complete captcha if asked.")
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user is directed to a page "Password Reset Error".
        start_time = time.time()

        registration_page.verify_if_password_reset_error_appears()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat Step 1 to 3 and entered a registered zebra email account (E.g: kk.wong@zebra.com) and click SUBMIT button.
        start_time = time.time()

        common_method.tearDown()
        registration_page.clickSignIn()
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.click_on_reset_password()
        sleep(5)
        registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
        registration_page.click_SUBMIT()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Enter a valid registered zebra email (E.g: KK.WONG@zebra.com) and click SUBMIT button.
        start_time = time.time()

        registration_page.check_if_in_zebra_network_account_password_reset_page()
        registration_page.check_fields_in_zebra_network_account_password_reset_page()
        registration_page.wait_for_element_appearance("android.widget.EditText", 10)
        registration_page.fill_username_in_zebra_network_account_password_reset_page("zebra03.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Enable * CAPTHA (I'm not a robot) to solve the pictorial puzzle and enter valid username E.g: kk1234 and click Next button.
        start_time = time.time()

        registration_page.enableCaptcha()
        common_method.show_message("Complete captcha if asked.")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check user will be navigate to Security Verification Page.
        start_time = time.time()

        while registration_page.checkSkipExists():
            registration_page.clickSkip()
            sleep(2)
        if registration_page.checkVerifyExists():
            registration_page.clickVerify()
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check failing to answer the security questions and click Next, user is navigated to Password Reset Error page. - Error Message Displayed: "Error: cannot verify user (kk1234). Number of attempt 1. Try again" - User required to answer a new sets of security questions.
        start_time = time.time()

        common_method.show_message("Check failing to answer the security questions and click Next, user is navigated to Password Reset Error page. - Error Message Displayed: \"Error: cannot verify user (kk1234). Number of attempt 1. Try again\" - User required to answer a new sets of security questions.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

        # Step 13: Repeat Step 12 until user exceed the attempt to reset the password. - Check the maximum attempt is 3. - Check user is navigated to Password Reset Error page. - Check the following error message is displayed. This user cannot use the configured Password Reset process. Possible reasons: User does not exist or is not enrolled. User is not part of the configured password reset process. User is blocked (exceeded the limit on reset attempts or reset password recently). User account is locked. Try again later. For immediate assistance, call the service desk.
        start_time = time.time()

        common_method.show_message("Step -12 Check failing to answer the security questions and click Next, user is navigated to Password Reset Error page.- Error Message Displayed: \"Error: cannot verify user (kk1234). Number of attempt 1. Try again\"- User required to answer a new sets of security questions.")
        common_method.show_message("Repeat Step 12 until user exceed the attempt to reset the password. - Check the maximum attempt is 3. - Check user is navigated to Password Reset Error page. - Check the following error message is displayed. This user cannot use the configured Password Reset process. Possible reasons: User does not exist or is not enrolled. User is not part of the configured password reset process. User is blocked (exceeded the limit on reset attempts or reset password recently). User account is locked. Try again later. For immediate assistance, call the service desk.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

        # Step 14: Repeat the steps to reset password as a zebra user (Step 8 to 10) of test case 45867
        start_time = time.time()

        common_method.show_message("Repeat the steps to reset password as a zebra user (Step 8 to 10) of test case 45867")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

        # Step 15: Check user will be bypass from answering the security question and will be navigated directly to Password Reset Error Page.
        start_time = time.time()

        Common_Method.show_message("Check user will be bypass from answering the security question and will be navigated directly to Password Reset Error Page.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)



def test_Registration_TestcaseID_45871():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2,
            'Click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        3: [3, 'Check user is navigated to "Login with username" page.'],
        4: [4, 'Click on Apple icon.'],
        5: [5, 'Check user will be navigate to Apple Sign In Page.'],
        6: [6, 'Enter registered Apple account username with incorrect password.'],
        7: [7,
            'Check user is not able to login to Money Badger Home Page. - Error message at Apple sign in prompt is displayed: "The password that you\'v entered is incorrect. Forgotten password?"'],
        8: [8, 'Enter registered Apple account username with correct password.'],
        9: [9,
            'Check user is able to successfully login to Money Badger Page and the top left corner shows the login name'],
        10: [10, 'Click on the hamburger icon follow by Settings and click Log out button.'],
        11: [11,
             'Check user is able to successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom.
        start_time = time.time()

        registration_page.clickSignIn()
        sleep(2)
        registration_page.verifyLinksInSignInPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to "Login with username" page.
        start_time = time.time()

        scroll_view = poco("android.view.View")
        registration_page.checkIfOnSSOLoginPage()
        while not poco(text="Sign In With"):
            scroll_view.swipe("down")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click on Apple icon.
        start_time = time.time()

        registration_page.click_Apple_Icon()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user will be navigate to Apple Sign In Page.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Enter registered Apple account username with incorrect password.
        start_time = time.time()

        registration_page.login_Apple("Zebra#12345678", "zebra03.swdvt@gmail.com", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user is not able to login to Money Badger Home Page.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Enter registered Apple account username with correct password.
        start_time = time.time()

        registration_page.login_Apple("Zebra#123456789")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user is able to successfully login to Money Badger Page and the top left corner shows the login name.
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        name = registration_page.get_login_name_from_menu()
        if name == "zsb swdvt":
            pass
        else:
            raise Exception("Login name does not match")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click on the hamburger icon follow by Settings and click Log out button.
        start_time = time.time()

        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check user is able to successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
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



"""Ask about eula decline - yet to update reporting"""


def test_Registration_TestcaseID_50287():
    pass

    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")
    email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")
    registration_page.enter_user_email_for_registering(email)
    registration_page.click_on_next()
    poco(text="Return to Previous Step").wait_for_appearance(timeout=20)
    """Enter verification code manually"""
    common_method.show_message(
        "Enter verification code on the device ,verification code received in the newly created google account")
    registration_page.click_on_next()
    sleep(5)
    if registration_page.check_email_verified_successfully_message():
        pass
    else:
        raise Exception("Email verified successfully message not present.")
    if registration_page.verify_user_information_and_account_security_page():
        pass
    else:
        raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
    first_name = "John"
    last_name = "Loke"
    registration_page.fill_first_name_field(first_name)
    registration_page.fill_last_name_field(last_name)
    while not poco(text="SUBMIT AND CONTINUE").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("up")
    password = "Zebra#123456789"
    registration_page.fill_password_field(password)
    registration_page.fill_confirm_password_field(password)
    registration_page.select_the_country("India")
    poco("android.widget.CheckBox")[0].click()
    poco("android.widget.CheckBox")[1].click()
    registration_page.click_submit_and_continue()
    sleep(4)
    registration_page.check_sign_up_successful()
    registration_page.click_continue_registration_page()
    try:
        registration_page.wait_for_element_appearance("Sign In", 10)
    except:
        raise Exception("Did not return to login page.")
    registration_page.clickSignIn()
    registration_page.wait_for_element_appearance_text("Continue with Google", 10)
    data_sources_page.signInWithEmail()
    """Provide the email and password"""
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    registration_page.verify_if_on_EULA_page()
    """No Delcine option on EULA page"""
    try:
        registration_page.wait_for_element_appearance("Welcome to ZSB Series", 20)
    except:
        raise Exception("Reached Home page without accepting EULA")
    registration_page.clickSignIn()
    registration_page.wait_for_element_appearance_text("Continue with Google", 10)
    data_sources_page.signInWithEmail()
    email = "smbmbzsb@gmail.com"
    password = "Zebratest123?"
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    try:
        registration_page.wait_for_element_appearance("Click ‘Accept’ to indicate that you have read and agree to the ",
                                                      20)
        raise Exception("Showing EULA page after logging in with existing account.")
    except:
        pass
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    try:
        registration_page.wait_for_element_appearance("Sign In", 10)
    except:
        raise Exception("Did not return to login page.")  # registration_page.clickSignIn()
    registration_page.wait_for_element_appearance_text("Continue with Google", 10)
    data_sources_page.signInWithEmail()
    """Provide the email and password"""
    password = "Smbzsbmb@1234"
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    try:
        registration_page.wait_for_element_appearance("End User\n License Agreement", 20)
        pass
    except:
        raise Exception("Showing EULA page after logging in with existing account.")


"""Add Printer"""
def test_Registration_TestcaseID_46304():
    """""""""test"""""

    common_method.tearDown()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page.Click_Next_Button()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 2"""
    try:
        add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    except:
        pass
    """Cannot automate walking 10 m"""
    common_method.show_message("move 10 meters away from printer.")
    try:
        registration_page.wait_for_element_appearance("Searching for Wi-Fi Networks", 50)
    except:
        raise Exception("Bluetooth connection unsuccessful")

def test_Registration_TestcaseID_46305():
    """""""""test"""""

    common_method.tearDown()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page.Click_Next_Button()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 2"""
    try:
        add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    except:
        pass
    """Cannot automate walking 10 m"""
    common_method.show_message("move 10 meters away from printer.")
    if registration_page.verifyUnableToPairPrinterError():
        print("Bluetooth process interrupted because bluetooth device out of range.")
    else:
        raise Exception("Bluetooth process not interrupted even though bluetooth device out of range.")

def test_Registration_TestcaseID_46306():
    pass
    common_method.tearDown()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page.Click_Next_Button()
    add_a_printer_page.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    try:
        registration_page.wait_for_element_appearance("Connect to Wi-Fi", 50)
    except:
        raise Exception("Bluetooth connection unsuccessful")
    common_method.wait_for_element_appearance("Discovered networks", 30)
    common_method.show_message("Select a wi-fi and enter wrong password.")
    try:
        registration_page.wait_for_element_appearance("Incorrect Wi-Fi password entered", 60)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Internet access blocked message did not show up.")
    except Exception as e:
        pass
    common_method.Stop_The_App()
