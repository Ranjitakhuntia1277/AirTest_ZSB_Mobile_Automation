import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Social_Login.Social_Login import Social_Login
from ...Common_Method import *
import os
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Others.Others import Others
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...PageObject.PDF_Printing.PDF_Printing_Android import PDF_Printing_Screen

import tkinter as tk
from tkinter import simpledialog


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring("Input", "Please enter your value:")
    return user_input


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)

social_login = Social_Login(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
others = Others(poco)
data_sources_page = Data_Sources_Screen(poco)
help_page = Help_Screen(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
aps_notification = APS_Notification(poco)
pdf_printing = PDF_Printing_Screen(poco)


class test_Android_Social_Login():
    pass

    def setup_logout(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        sleep(5)

        try:
            others.wait_for_element_appearance("Sign In", 20)
        except:
            pass

        try:
            common_method.wait_for_element_appearance_namematches("Home", 20)
            login_page.click_Menu_HamburgerICN()
            others.click_on_profile_edit()
            others.scroll_down()
            others.click_log_out_button()
        except:
            pass

    def test_Social_Login_TestcaseID_48464(self):
        pass

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
        res = social_login.check_zebra_logo()
        if not res:
            raise Exception("Zebra logo not present")

        res = social_login.check_login_with_google()
        if not res:
            raise Exception("Login with google not present")

        res = social_login.check_login_with_apple()
        if not res:
            raise Exception("Login with Apple not present")

        res = social_login.check_login_with_facebook()
        if not res:
            raise Exception("Login with Facebook not present")

        res = social_login.check_sign_in_with_email()
        if not res:
            raise Exception("Sign in with email not present")

        res = social_login.check_text_of_free_benifits()
        if not res:
            raise Exception(
                "Check under the Sign in with your email option, there is a Learn more about the Benefits of Creating a Free ZSB Account, and the Benefits of Creating a Free Account is highlighted in blue")

        social_login.scroll_down(1)

        social_login.check_the_cookie_text()

        res = social_login.check_options_under_cookie_text()
        if not res:
            raise Exception("options are not proper or missing")

        common_method.tearDown()

    def test_Social_Login_TestcaseID_48465(self):
        pass

        common_method.tearDown()
        self.setup_logout()
        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        social_login.click_on_benefits_of_zebra_account()
        sleep(5)
        res = social_login.check_the_text_of_benefits_of_free_account_page()
        if not res:
            raise Exception("the page text dint match")
        social_login.scroll_up(1)
        social_login.check_both_images_in_benefits_of_free_account_page()
        res = social_login.check_the_back_button()
        if not res:
            raise Exception("No back button")
        social_login.click_on_the_back_button()
        social_login.check_login_with_google()

    def test_Social_Login_TestcaseID_48466(self):
        pass
        self.setup_logout()
        login_page.Verify_ALL_Allow_Popups()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.Verify_Login_Option_Is_Present()
        social_login.click_on_zebra_link()
        social_login.Verify_Zebra_URL()
        social_login.click_Browser_Close_Icon()
        login_page.click_Cancel_Btn()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.Verify_Login_Option_Is_Present()
        social_login.click_on_legal_notice_link()
        social_login.Verify_Legal_Notice_Page()
        if not help_page.verify_url("zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html"):
            raise Exception(
                "\"zebra.com/us/en/about-zebra/company-information/legal/legal/terms-of-use.html\" url not present")
        social_login.click_Browser_Close_Icon()
        login_page.click_Cancel_Btn()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.Verify_Login_Option_Is_Present()
        social_login.click_on_privacy_statement_link()
        if not help_page.verify_url("zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html"):
            raise Exception(
                "\"zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html\" url not present")
        social_login.click_Browser_Close_Icon()
        login_page.click_Cancel_Btn()

    def test_Social_Login_TestcaseID_48475(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        social_login.click_on_sign_in_with_email()
        keyevent("back")
        sleep(1)
        social_login.scroll_down(1)

        """Reset The password"""
        social_login.click_on_reset_password()
        social_login.wait_for_element_appearance_text("Password Recovery", 20)
        sleep(1)
        username = common_method.get_user_input("enter the user email here")
        social_login.enter_user_name_to_change_password(username)
        social_login.click_on_submit_button()

        common_method.wait_for_element_appearance_namematches("Click here")
        social_login.click_here_button_click()
        """Cant Automate this step 3. Input the prepare email address, follow the steps to finish reseting pw
        Check the pw can be reset successfully without any error"""
        """Enter the temp_pass was temporary password which is got through Mail and enter new password"""

        """Semi automated here pass temp password"""

        """Part2"""

        common_method.wait_for_element_appearance_textmatches("Reset Password", 30)
        sleep(3)

        common_method.show_message("enter the temp password and new password here")

        social_login.click_on_submit_button()

        try:
            social_login.wait_for_element_appearance_text("Password changed successfully.", 20)
        except:
            raise Exception("password changed confirmation dint receive")

        try:
            common_method.wait_for_element_appearance_namematches("Click here")
            social_login.click_here_button_click()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Continue with Google", 15)
        social_login.click_on_sign_in_with_email()
        common_method.show_message("enter the email and password and continue till home page")

        try:
            social_login.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("dint sign in properly")

    def test_Others_TestcaseID_45802(self):
        pass
        common_method.tearDown()
        try:
            social_login.click_on_allow_for_notification()
        except:
            pass
        self.setup_logout()
        common_method.wait_for_element_appearance_namematches("Sign In")

        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        others.click_on_sign_in_with_email()
        common_method.wait_for_element_appearance_textmatches("Sign In")

        email = "zebratest851@gmail.com"
        password = "Zebra#85185180"
        social_login.complete_sign_in_with_email(email, password, 0)

        sleep(30)
        others.click_on_sign_in()
        common_method.wait_for_element_appearance_namematches("Home", 30)

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        login_page.click_Menu_HamburgerICN()

    def test_Others_TestcaseID_45872(self):
        pass

        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        others.click_on_sign_in_with_email()
        sleep(1)
        others.go_back()
        others.enter_user_name_in_sign_with_email("zebratest851@gmail.com")
        others.enter_password_in_sign_with_email("Zebra#85185180")
        sleep(30)
        others.click_on_sign_in()

        try:
            others.wait_for_element_appearance("Home", 10)
            raise Exception("The page does not timeout")
        except ZeroDivisionError:
            pass

    def test_Social_Login_TestcaseID_48473(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.click_on_sign_in_with_email()
        social_login.verify_Zebraaccount_page()
        social_login.check_zebra_logo()
        social_login.check_username_and_password_feilds()
        login_page.Dismiss_Keyboard()
        social_login.check_sign_in_button()
        social_login.check_close_button()
        social_login.check_text_of_register_your_email()
        social_login.check_reset_password_text()
        social_login.click_on_close_button()

    def test_Social_Login_TestcaseID_48474(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_on_sign_in_with_email()
        try:
            social_login.click_register_your_email()
        except:
            social_login.go_back()
            social_login.click_register_your_email()

        sleep(2)
        common_method.wait_for_element_appearance_textmatches("ZSB Printer", 20)
        a = social_login.check_registration_of_email()
        if not a:
            raise Exception("register user page dint show")

        """Enter the User Email"""
        email = "testzebra141@gmail.com"
        social_login.enter_user_email_for_registering(email)
        social_login.click_on_next()

        try:
            social_login.wait_for_element_appearance("Resend Verification Code.", 30)
        except:
            raise Exception("Second step dint work")

        """Semi automated """
        """Enter Verification code"""
        verification_code = common_method.get_user_input("enter the code which is got through testzebra141@gmail.com")
        social_login.enter_the_verification_code(verification_code)
        social_login.scroll_down(1)
        social_login.click_on_next()

        """Enter the first Name last name and the password"""
        common_method.wait_for_element_appearance_textmatches("ZSB Printer User Information and Account Security")
        sleep(2)
        first_n = "Zebra"
        last_n = "Z"
        password = "Zebra#123456789"
        social_login.enter_the_fields(first_n, last_n, password)
        social_login.select_the_country("India")
        try:
            social_login.select_the_check_boxes()
            social_login.select_the_check_boxes()
        except:
            try:
                social_login.scroll_down(1)
                social_login.select_the_check_boxes()
                social_login.select_the_check_boxes()
            except:
                pass
        social_login.click_submit_and_continue()
        sleep(2)
        social_login.check_sign_up_successful()
        social_login.click_on_continue()

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide the email and password"""
        social_login.complete_sign_in_with_email(email, password)

        try:
            social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement")
        except:
            raise Exception("EULA page dint show up")

        social_login.click_on_cancel_button_in_eula()
        social_login.click_on_exit_in_eula()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48482(self):
        pass

        common_method.show_message(
            "Prepare an external account which hasn't been signed in once in ZSB series app (new registered)")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide new_user name and password which is not registered"""
        email = common_method.get_user_input("enter the new email")
        password = common_method.get_user_input("enter the password")

        social_login.complete_sign_in_with_email(email, password)
        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""

        common_method.show_message("check the user first name and last name")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()
        sleep(2)
        social_login.complete_sign_in_with_email(email, password)
        common_method.wait_for_element_appearance_namematches("Home")
        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_50646(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        if not social_login.check_focused_of_user_name():
            raise Exception("user name is not focused")
        if not social_login.check_key_board():
            raise Exception("No key board displayed")
        if not social_login.check_key_board():
            raise Exception("keyboard dint show up")

    def test_Social_Login_TestcaseID_48467(self):
        pass

        common_method.tearDown()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        login_page.click_Loginwith_Google()
        social_login.loginwith_Sociallogin_EmailID()
        app_settings_page.Home_text_is_present_on_homepage()
        """Check whether logged in to same account as email"""
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.Verify_Email()
        """Log out"""
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        login_page.Verify_Login_Option_Is_Present()

    def test_Social_Login_TestcaseID_50643(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")

        """Enter the email"""
        email = "zebra850.swdvt@gmail.com"
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()

        login_page.click_Loginwith_Google()

        if not social_login.verify_choose_an_account_text():
            raise Exception("did not redirect to the choose an acoount page")

    def test_Social_Login_TestcaseID_50612(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        """Enter the email and password"""
        email = "zebra850.swdvt@gmail.com"
        password = 'Zebra#123456789'

        social_login.click_on_sign_in_with_email()
        social_login.complete_sign_in_with_email(email, password, 0)
        social_login.show_the_password()
        sleep(4)
        res = social_login.get_the_password()
        print(res)
        if str(res) != str(password):
            raise Exception("password is not matching")

    def test_Social_Login_TestcaseID_48486(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        """Enter the email and password"""
        email = ""
        password = ''
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        social_login.click_on_sign_in_with_email()
        social_login.complete_sign_in_with_email(email, password, 1)
        sleep(3)
        if not social_login.check_for_blank_value_error_of_both():
            raise Exception("Error not displayed for blank values")

        email = "zebratest852@gmail.com"
        social_login.complete_sign_in_with_email(email, password, 1, 0)
        if not social_login.check_for_blank_value_error_of_password():
            raise Exception("Error not displayed for blank values")

        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email, password, 1, 0)
        try:
            social_login.wait_for_element_appearance("Home", 20)
        except:
            raise Exception('did not sign in properly')

    def test_Social_Login_TestcaseID_48483(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(2)
        social_login.click_on_sign_in_with_email()
        """Provide new_user name and password which is registered"""
        email = "zebratest852@gmail.com"
        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email, password)
        if social_login.check_EULA():
            social_login.accept_EULA_agreement()

        social_login.wait_for_element_appearance("Home", 20)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        first_name = "Zebra"
        last_name = "Zebra"
        social_login.validate_the_details_of_account(first_name, last_name, email)
        if not social_login.check_the_email_in_profile_page(email):
            raise Exception("Email are not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48485(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        login_page.Verify_Login_Option_Is_Present()
        social_login.click_on_sign_in_with_email()
        """Incorrect password but correct email"""
        """Enter the email and password"""
        email = "zebratest852@gmail.com"
        password = 'Zebra#1234567890'

        #### social_login.click_on_sign_in_with_email()
        social_login.complete_sign_in_with_email(email, password, 1)
        if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
            raise Exception("Error not displayed for incorrect password values")

        sleep(1)
        """Incorrect Email but correct password"""
        email = "zebratest85@gmail.com"
        password = 'Zebra#123456789'

        social_login.click_on_sign_in_with_email()

        social_login.complete_sign_in_with_email(email, password, 1, 1)
        sleep(2)
        if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
            raise Exception("Error not displayed for incorrect email")

        sleep(1)
        social_login.click_on_sign_in_with_email()

        """Correct password and email"""
        email = "zebratest852@gmail.com"
        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email, password, 1, 1)
        if social_login.wait_for_element_appearance("Home", 20):
            raise Exception('did not sign in properly')

    def test_Social_Login_TestcaseID_48479(self):
        pass

        common_method.tearDown()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_loginBtn()
        login_page.Verify_ALL_Allow_Popups()
        registration_page.Enter_Correct_Username()
        registration_page.Enter_Wrong_Password()
        login_page.click_SignIn_Button()
        registration_page.Verify_We_Didnot_recognize_Please_Try_Again()
        data_sources_page.signInWithEmail()
        registration_page.Enter_Correct_Username()
        registration_page.Enter_Correct_Password()
        login_page.click_SignIn_Button()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        registration_page.Verify_SignIn_Page()
        common_method.Stop_The_App()

    def test_Social_Login_TestcaseID_48470(self):
        pass

        common_method.show_message("add a new google account to the phone")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        email = common_method.get_user_input("enter the new gmail account")
        social_login.choose_a_google_account(email)
        sleep(3)
        try:
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
            sleep(2)
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        common_method.show_message("check the first name last name and email are matching as provided")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 10)

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_48472(self):
        pass

        common_method.show_message("create a new facebook account")
        self.setup_logout()
        email = common_method.get_user_input("enter the new facebook email here")
        password = common_method.get_user_input("enter the new password here")
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
        except:
            pass

        social_login.continue_in_facebook()
        social_login.wait_for_element_appearance_text("Submit", 10)

        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_in_facebook()
            social_login.wait_for_element_appearance_text("Continue", 10)
            social_login.click_on_continue()
        except:
            pass

        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        """Semi automated"""
        common_method.show_message("check the email, first name and last name is as expected")

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()
        try:

            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 10)

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_48481(self):
        pass
        # Log in to your Facebook account to connect with Zebra Technologies
        self.setup_logout()
        login_page.click_loginBtn()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()
        social_login.wait_for_element_appearance_text(
            "Log in to your Facebook account to connect to Zebra Technologies")

        email = "wrongemail.com"
        password = "Zebra#123456"
        social_login.enter_username_and_password_in_facebook(email, password)
        try:
            social_login.click_element_by_text("Log In")
        except:
            social_login.click_element_by_text("Log in")
        sleep(3)

        if not social_login.check_wrong_user_name_error_in_facebook():
            raise Exception("error not shown for wrong user name")

        email = "testswdvt@gmail.com"
        password = "Zebra#1234567"
        social_login.enter_username_and_password_in_facebook(email, password)
        try:
            social_login.click_element_by_text("Log In")
        except:
            social_login.click_element_by_text("Log in")
        sleep(3)

        if not social_login.check_wrong_password_error_in_facebook():
            raise Exception("error not shown for wrong password")

        try:
            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log in")
            sleep(3)

        except:
            try:
                social_login.click_element_by_text("Log In")
            except:
                pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        first_name = "Zebra"
        last_name = "Zebra"
        # social_login.validate_the_details_of_account(first_name, last_name, email)
        email = "testswdvt@gmail.com"
        if not social_login.check_the_email_in_profile_page(email):
            raise Exception("email not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48469(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log in", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log in")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        try:
            common_method.wait_for_element_appearance_namematches(
                "For the best experience, we need a couple things from you.", 3)
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
        except:
            pass

        common_method.show_message("if the page ask for otp or code provide that and continue till the homr page")

        try:
            social_login.continue_in_facebook()
        except:
            pass

        social_login.wait_for_element_appearance("Home", 30)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        first_name = "Zebra"
        last_name = "Zebra"
        # social_login.validate_the_details_of_account(first_name, last_name, email)
        email = "testswdvt@gmail.com"
        if not social_login.check_the_email_in_profile_page(email):
            raise Exception("email not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48478(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        common_method.show_message("if not signed in , then sign in")

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        common_method.show_message("add a printer to this account")
        """Semi automated"""
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        social_login.click_Printer_Settings()
        social_login.click_on_first_printer()
        social_login.click_test_print()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        social_login.click_home_button()
        social_login.click_three_dots_in_printer()
        social_login.click_delete_button()
        social_login.click_delete_button()

        social_login.confirm_delete_printer()
        add_a_printer_page.disable_bluetooth()

        try:
            social_login.click_element_by_text("ALLOW")
        except:
            try:
                social_login.click_element_by_text("Allow")
            except:
                pass
        sleep(2)

        social_login.click_done_enabled()
        sleep(5)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_48480(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        try:
            social_login.wait_for_element_appearance_text("Forgot", 10)
        except:
            pass

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#12345678"
        social_login.enter_apple_id_and_password(apple_id, password)

        social_login.click_element_by_text("Apple\xa0ID")
        sleep(2)

        if not social_login.check_for_incorrect_error_in_apple():
            raise Exception("No error raised for wrong password or username")

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """Enter two factor authentication if required"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-", 4)
            # social_login.go_back()
            code = "661850"
            social_login.two_factor_authentication_for_apple(code)
            sleep(2)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass
        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home")

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48471(self):
        pass

        common_method.show_message("Create a new apple account")
        self.setup_logout()
        """Need to create a new apple account"""
        apple_id = common_method.get_user_input("Enter the new apple account")
        password = common_method.get_user_input("Enter the password for the apple account")
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)
        try:
            social_login.enter_apple_id_and_password(apple_id, password)
        except:
            pass

        try:
            social_login.click_on_continue()
        except:
            pass

        """Enter the two factor authentication code sent in phone """
        a = common_method.get_user_input("enter the code")
        try:
            social_login.two_factor_authentication_for_apple(a)
        except:
            pass

        social_login.apple_trust_this_browser()
        social_login.continue_steps_in_apple()

        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            sleep(1)
            social_login.click_on_submit_button()
            sleep(2)
        except:
            pass

        social_login.click_on_continue()

        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Semi automated check manually"""
        """Pass the first name last name and email to be expected"""
        common_method.show_message("check the email , first name and last name are as expected")

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)
        try:

            social_login.enter_apple_id_and_password(apple_id, password)
        except:
            pass

        try:
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance("Home")

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_48468(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 15)

        social_login.click_login_with_apple()
        common_method.wait_for_element_appearance_textmatches("Forgot", 15)

        """Sign in"""
        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """IF two factor authentication requires"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-factor authentication", 4)
            # social_login.go_back()
            code = common_method.get_user_input("Enter the apple id code")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass
        try:
            common_method.wait_for_element_appearance_textmatches("Trust", 6)
            social_login.apple_trust_this_browser()
        except:
            pass
        sleep(1)

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        """Log out"""
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        first_name = "swdvt"
        last_name = "test"
        if not social_login.validate_the_details_of_account(first_name, last_name):
            raise Exception("credentials not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48477(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        try:
            code = common_method.show_message("enter the code")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        common_method.show_message("add a printer to this account")
        """Semi automated"""
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()

        login_page.click_Menu_HamburgerICN()
        social_login.click_Printer_Settings()
        social_login.click_on_first_printer()
        social_login.click_test_print()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        social_login.click_home_button()
        social_login.click_three_dots_in_printer()
        social_login.click_delete_button()
        social_login.click_delete_button()

        social_login.confirm_delete_printer()
        add_a_printer_page.disable_bluetooth()

        try:
            social_login.click_element_by_text("ALLOW")
        except:
            try:
                social_login.click_element_by_text("Allow")
            except:
                pass
        sleep(2)

        social_login.click_done_enabled()
        sleep(5)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)

        social_login.enter_apple_id_and_password(apple_id, password)

        try:
            code = common_method.get_user_input("enter the code here")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_50223(self):
        pass

        common_method.show_message("create a new google account")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        email = common_method.get_user_input("enter the new email account")
        social_login.choose_a_google_account(email)
        sleep(3)
        try:
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
            sleep(2)
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance_namematches_all("End User", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.decline_EULA_agreement()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")

        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")

        social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()

        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance("Continue with Google", 10)

        login_page.click_Loginwith_Google()
        social_login.choose_a_google_account(email)

        social_login.wait_for_element_appearance_namematches_all("End User", 20)

        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance("Continue with Google", 10)

        login_page.click_Loginwith_Google()
        social_login.choose_a_google_account(email)
        sleep(5)
        if social_login.check_EULA():
            raise Exception("EULA  displayed")

    def test_Social_Login_TestcaseID_48484(self):
        pass
        self.setup_logout()
        """Sign in with email"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide the email and password"""
        email = "zebratest852@gmail.com"
        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email, password)

        try:
            social_login.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("home page dint show up")

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 15)
        except:
            raise Exception("Did not redirect to the login page")

        """Google sign in"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()

        """Enter the email"""
        email = "zebra850.swdvt@gmail.com"
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 20)
        except:
            raise Exception("Did not redirect to the login page")

        """Apple sign in"""
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 20)

        """Sign in"""
        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """semi automated"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-", 4)
            social_login.go_back()
            code = "666773"
            social_login.two_factor_authentication_for_apple(code)
            sleep(1)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
            sleep(2)
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home")

        """Log out"""
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

        """Facebook Sign in"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 15)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48476(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)
        login_page.click_Loginwith_Google()

        """Enter the email"""
        email = "zebra850.swdvt@gmail.com"
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)

        common_method.show_message("add a printer to this account")
        # sleep(60 * 5)
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()
        #
        # login_page.click_Menu_HamburgerICN()
        # social_login.click_Printer_Settings()
        # social_login.click_on_first_printer()
        # social_login.click_test_print()
        # sleep(3)
        # login_page.click_Menu_HamburgerICN()
        # social_login.click_home_button()
        # social_login.click_three_dots_in_printer()
        # social_login.click_delete_button()
        # social_login.click_delete_button()
        #
        # social_login.confirm_delete_printer()
        # add_a_printer_page.disable_bluetooth()
        #
        # try:
        #     social_login.click_element_by_text("ALLOW")
        # except:
        #     try:
        #         social_login.click_element_by_text("Allow")
        #     except:
        #         pass
        # sleep(2)
        #
        # social_login.click_done_enabled()
        # sleep(5)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()

        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_50613(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        common_method.Turn_Off_The_Phone()
        sleep(2)
        common_method.Turn_ON_The_Phone()
        sleep(4)
        social_login.wait_for_element_appearance("Continue with Google")
        login_page.click_Loginwith_Google()
        social_login.sign_in_with_new_google()
        sleep(5)
        social_login.enter_user_name_in_google("zebratest_o1@outlook.com")
        social_login.click_on_next_in_google_sing_in()
        if not social_login.check_for_incorrect_username_in_google():
            raise Exception("error not found for incorrect email")

    #   ####""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def test_Social_Login__TestcaseID_45883(self):
        """Verify sign in sign out with registered social accounts in Mobile App."""

        """start the app"""
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
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """""""""" check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy")"""""""""""
        smoke_test_android.Verify_SignIn_With_Text_Is_Present()
        smoke_test_android.click_Continue_With_Facebook_Option()
        """""due to some issue, it is directly login to the facebook account without asking for password"""
        login_page.click_Continue_On_Facebbok_Login_Page()
        login_page.click_Menu_HamburgerICN()
        smoke_test_android.Verify_Facebook_UserName_Is_Displaying()
        login_page.click_Continue_On_Facebbok_Login_Page()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        smoke_test_android.click_Continue_With_Apple_Option()
        smoke_test_android.Enter_Apple_Login_Email()
        smoke_test_android.click_Continue_For_Apple_Password()
        smoke_test_android.click_Continue_With_Password_ForApple_Login()
        smoke_test_android.click_On_Sign_In_Option()
        common_method.Stop_The_App()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        login_page.click_Menu_HamburgerICN()
        smoke_test_android.Verify_Google_UserName_Is_Displaying()
        common_method.Stop_The_App()

    #
    # # ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #
