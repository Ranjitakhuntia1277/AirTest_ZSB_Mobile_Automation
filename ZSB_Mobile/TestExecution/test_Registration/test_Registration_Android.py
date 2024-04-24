from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
# start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)


def test_Registration_TestcaseID_45855():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# sleep(2)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# registration_page.enter_user_email_for_registering("zebraswtest2@gmail.com")
# registration_page.click_on_next()
# """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
# """Verify Account already exists page title"""
# registration_page.check_email_already_exists_page_title()
# """Verify Account already exists page message"""
# registration_page.check_email_already_Exists_page_message()
# """No RETURN TO LOGIN button."""
# """Click Continue"""
# data_sources_page.clickContinue()
# if registration_page.check_if_in_login_page():
#     pass
# else:
#     raise Exception("Did not return to login page.")


def test_Registration_TestcaseID_45856():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# sleep(5)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# registration_page.enter_user_email_for_registering("test123@zebra.com")
# registration_page.click_on_next()
# if registration_page.check_zebra_mail_registration_error():
#     pass
# else:
#     raise Exception("NO error when trying to register with zebra mail id.")
# help_page.closeTab()
# data_sources_page.clickCancel()
# sleep(3)
# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# sleep(5)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# registration_page.enter_user_email_for_registering("smbzsb7@gmail.com")
# registration_page.click_on_next()
# poco(text="Return to Previous Step").wait_for_appearance(timeout=10)
# if registration_page.check_email_verification_page_message():
#     pass
# else:
#     raise Exception("Email verification page message not matching.")
# verification_code = "asdtfdsa"
# registration_page.enter_the_verification_code(verification_code)
# registration_page.click_on_next()
# if registration_page.verify_verification_code_expired_error():
#     pass
# else:
#     raise Exception("Verification code expired error not present.")
# if registration_page.verify_resend_verification_code_btn_exists():
#     pass
# else:
#     raise Exception("Resend verification code button not present.")
# registration_page.click_resend_verification_code_btn()
# verification_code = "CLG67B"
# registration_page.enter_the_verification_code(verification_code)
# registration_page.click_on_next()
# sleep(5)
# if registration_page.verify_user_information_and_account_security_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
#
# """Enter the first Name last name and the password"""
# first_name = "John"
# last_name = "Wick"
# password = "Zebra#123456789"
# registration_page.enter_the_fields(first_name, last_name, password)
# registration_page.select_the_country("India")
# registration_page.select_the_check_boxes()
# registration_page.click_submit_and_continue()
# sleep(4)
# registration_page.check_sign_up_successful()
# registration_page.click_continue_registration_page()
# poco("Login").wait_for_appearance(timeout=10)
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# registration_page.click_on_sign_in_with_email()
#
# """Provide the email and password"""
# email = "smbzsb7@gmail.com"
# password = "Zebra#123456789"
# registration_page.complete_sign_in_with_email(email, password, 1, 0)
# while not poco(name="Accept", enabeled=True).exists():
#     poco.scroll()
# registration_page.click_accept()
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
#
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45857():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# poco("android.widget.EditText").wait_for_appearance(timeout=20)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
# registration_page.enter_user_email_for_registering("smbmbzsb@gmail.com")
# registration_page.click_on_next()
# poco(text="Return to Previous Step").wait_for_appearance(timeout=10)
# verification_code = "1B6D0R"
# registration_page.enter_the_verification_code(verification_code)
# registration_page.click_on_next()
# sleep(5)
# if registration_page.check_email_verified_successfully_message():
#     pass
# else:
#     raise Exception("Email verified successfully message not present.")
# if registration_page.verify_user_information_and_account_security_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
# registration_page.verify_if_all_fields_present()
# registration_page.verify_if_checkboxes_are_present_registration()
# while not poco(text="Email verified successfully!").exists():
#     scroll_view = poco("android.view.View")
#     scroll_view.swipe("down")
# scroll_view = poco("android.view.View")
# scroll_view.swipe("down")
# if registration_page.special_character_error_name_field("First Name", "John123!"):
#     pass
# else:
#     raise Exception("No error for using special character in First Name field.")
# sleep(2)
# if registration_page.special_character_error_name_field("Last Name", "Loke123!"):
#     pass
# else:
#     raise Exception("No error for using special character in Last Name field.")
# sleep(2)
# if registration_page.check_error_password_field("abcdefg", True):
#     pass
# else:
#     raise Exception("No error when entered only alphabets in password field.")
# sleep(2)
# if registration_page.check_error_password_field("12345678"):
#     pass
# else:
#     raise Exception("No error when entered only alphabets in password field.")
# sleep(2)
# while not poco(text="Email verified successfully!").exists():
#     scroll_view = poco("android.view.View")
#     scroll_view.swipe("down")
# scroll_view = poco("android.view.View")
# scroll_view.swipe("down")
# first_name = "John"
# last_name = "Loke"
# registration_page.fill_first_name_field(first_name)
# registration_page.fill_last_name_field(last_name)
# while not poco(text="SUBMIT AND CONTINUE").exists():
#     scroll_view = poco("android.view.View")
#     scroll_view.swipe("up")
# registration_page.fill_password_field("Zebratest123?")
# registration_page.fill_confirm_password_field("sss?")
# registration_page.check_password_unmatch_error()
# registration_page.fill_confirm_password_field("Zebratest123?")
# registration_page.select_the_country("India")
# poco("android.widget.CheckBox")[1].click()
# poco("android.widget.CheckBox")[0].click()
# poco("android.widget.CheckBox")[0].click()
# registration_page.click_clear()
# if registration_page.check_error_message_after_clear():
#     pass
# else:
#     raise Exception("Fields not cleared after clicking clear.")
# registration_page.click_submit_and_continue()
# sleep(4)
# registration_page.check_sign_up_successful()
# registration_page.click_continue_registration_page()
# poco("Login").wait_for_appearance(timeout=10)
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# """Provide the email and password"""
# email = "smbmbzsb@gmail.com"
# password = "Zebratest123?"
# registration_page.complete_sign_in_with_email(email, password, 1, 0 )
# while not poco("http://www.zebra.com").exists():
#     poco.scroll()
# registration_page.click_decline()
# sleep(2)
# if registration_page.check_if_in_login_page():
#     pass
# else:
#     raise Exception("Logged in successfully even though declined EULA")
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# email = "smbmbzsb@gmail.com"
# password = "Zebratest123?"
# registration_page.complete_sign_in_with_email(email, password, 1, 0 )
# while not poco(name="Accept", enabeled=True).exists():
#     poco.scroll()
# registration_page.click_accept()
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# registration_page.home_page_overview("Johnny")
# registration_page.check_add_a_printer_exists()
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45858():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# poco("android.widget.EditText").wait_for_appearance(timeout=10)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# registration_page.enter_user_email_for_registering("smbmzsb7@gmail.com")
# registration_page.click_on_next()
#
# try:
#     registration_page.wait_for_element_appearance("Resend Verification Code.", 10)
# except:
#     raise Exception("Second step dint work")
#
# verification_code = "SLS9820000"
# registration_page.enter_the_verification_code(verification_code)
# registration_page.click_on_next()
# sleep(2)
# """Enter the first Name last name and the password"""
# first_n = "Zebra"
# last_n = "Z"
# password = "Zebra#123456789"
# registration_page.enter_the_fields(first_n, last_n, password)
# registration_page.select_the_country("India")
# registration_page.select_the_check_boxes()
# registration_page.click_submit_and_continue()
# sleep(2)
# registration_page.check_sign_up_successful()
# registration_page.click_continue_registration_page()
# poco("Login").wait_for_appearance(timeout=10)
#
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# """Provide the email and password"""
# email = "zebra852@gmail.com"
# password = "Zebra#123456789"
# registration_page.complete_sign_in_with_email(email, password)
"""step 11 et to do"""


# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
#
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45859():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("soho_dvtxxxxx@hotmail.com", "soho_dvtxxxxx@hotmail.com", 1, 0, True)
# if poco("android.widget.TextView")[3].get_text() == "Username*":
#     print("Page stays at Login with username.")
# else:
#     raise Exception("Page not at Login with username.")


def test_Registration_TestcaseID_45860():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("zebra852@gmail.comm", "Zebra#1234567890", 1, 0, True)
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("zebra852@gmail.comm", "Zebra#123456789", 1, 0, False, True)
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Registration_TestcaseID_45861():
    """""""""test"""""


# login_page.click_loginBtn()
# sleep(2)
# registration_page.click_Google_Icon()
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# sleep(2)
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45862():
    """""""""test"""""


# login_page.click_loginBtn()
# registration_page.click_Google_Icon()
# sleep(3)
# registration_page.verify_Sign_In_With_Google_Page()
# registration_page.sign_In_With_Google("zsbswdvt@123", "zsbswdvt@gmail.com", True)
# registration_page.sign_In_With_Google("zsbswdvt@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# name = registration_page.get_login_name_from_menu()
# if name == "swdvt zsb":
#     pass
# else:
#     raise Exception("Login name does not match")
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45863():
    """""""""test"""""


# login_page.click_loginBtn()
# registration_page.click_Facebook_Icon()
# registration_page.login_Facebook("zsbswdvt@123", "zsbswdvt@gmail.com", True)
# registration_page.login_Facebook("zsbswdvt@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# name = registration_page.get_login_name_from_menu()
# if name == "swdvt zsb":
#     pass
# else:
#     raise Exception("Login name does not match")
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")

# data_sources_page.signInWithEmail()


def test_Registration_TestcaseID_45864():
    """""""""test"""""


# login_page.click_loginBtn()
# registration_page.complete_sign_in_with_email("smbmbzsb@gmail.com", "ZebraTest#1234", 1, 0 )
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45865():
    """""""""test"""""


# login_page.click_loginBtn()
# # registration_page.complete_sign_in_with_email("smbmbzsb@gmail.com", "ZebraTest#1234", 1, 0 )
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45866():
    """""""""test"""""


# start_app("com.zebra.soho_app")
# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.click_on_reset_password()
# sleep(5)
# if registration_page.check_if_in_password_recovery_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'Password Recovery' Page")
# registration_page.Enter_Username_password_recovery_page("a1@gmail.com")
# registration_page.click_SUBMIT()
# sleep(3)
# if registration_page.check_user_does_not_exist_error():
#     pass
# else:
#     raise Exception("'User does not exist' error did not show up even after entering a non registered email.")
# stop_app("com.zebra.soho_app")
# start_app("com.zebra.soho_app")
# login_page.click_loginBtn()
# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.click_on_reset_password()
# sleep(5)
# if registration_page.check_if_in_password_recovery_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'Password Recovery' Page")
# registration_page.Enter_Username_password_recovery_page("smbmbzsb@gmail.com")
# registration_page.click_SUBMIT()
# registration_page.wait_for_element_appearance_text("Success!", 10)
# if registration_page.check_message_on_success_page():
#     pass
# else:
#     raise Exception("Expected message not on success page.")
# registration_page.click_on_Click_here()
# if registration_page.check_if_on_Reset_Password_page():
#     pass
# else:
#     raise Exception("Did not navigate to password reset page.")
# registration_page.check_fields_on_Reset_Password_page()
# registration_page.click_SUBMIT()
# if registration_page.check_error_message_on_fields_on_Reset_Password_page():
#     pass
# else:
#     raise Exception("Error messages not as expected.")
# otp = "gqocrd0a"
# registration_page.fillPasswordResetCode(otp)
# registration_page.fillNewPassword("ZebraTest#1234")
# registration_page.fillConfirmPassword("ZebraTest#123")
# registration_page.click_SUBMIT()
# if registration_page.checkWrongConfirmPasswordErrorMessage():
#     pass
# else:
#     raise Exception("\"Password and Confirm Password must match\" not displayed when entered different 'New Password' and 'Confirm Password'")
# """Wait for 10 minutes """
# registration_page.fillConfirmPassword("ZebraTest#1234")
# registration_page.click_SUBMIT()
# sleep(5)
# if registration_page.check_OTExpiredMessage():
#     pass
# else:
#     raise Exception("Expected OTP expired message not displayed.")
# registration_page.click_on_click_here()
# """Step 18. Click on Click here to login with your temporary password in Success! page not present"""
# registration_page.click_on_Click_here()
# registration_page.wait_for_element_appearance_text("Reset Password", 10)
# otp = "nbv474tm"
# registration_page.fillPasswordResetCode(otp)
# registration_page.fillNewPassword("ZebraTest#1234")
# registration_page.fillConfirmPassword("ZebraTest#1234")
# registration_page.click_SUBMIT()
# registration_page.wait_for_element_appearance_text("Success!", 10)
# registration_page.check_successful_password_reset_page_message()
# registration_page.click_on_Click_here()
# try:
#     registration_page.wait_for_element_appearance_text("Sign In With", 10)
# except:
#     raise Exception("Did not reach Sign in page")
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("smbmbzsb@gmail.com", "ZebraTest#1234", 1, 0 )
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")


def test_Registration_TestcaseID_45867():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.click_on_reset_password()
# sleep(5)
# registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
# registration_page.click_SUBMIT()
# sleep(3)
# registration_page.check_if_in_zebra_network_account_password_reset_page()
# registration_page.check_fields_in_zebra_network_account_password_reset_page()
# registration_page.fill_username_in_zebra_network_account_password_reset_page("tt1234")
# registration_page.enableCaptcha()
# registration_page.click_on_next()
# try:
#     registration_page.wait_for_element_appearance_text("Password Reset Error", 10)
# except:
#     raise Exception("Did not redirected to a page \"Password Reset Error\" page.")
# stop_app("com.zebra.soho_app")
# start_app("com.zebra.soho_app")
# login_page.click_loginBtn()
# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.click_on_reset_password()
# sleep(5)
# registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
# registration_page.click_SUBMIT()
# sleep(3)
# registration_page.check_if_in_zebra_network_account_password_reset_page()
# registration_page.check_fields_in_zebra_network_account_password_reset_page()
# registration_page.wait_for_element_appearance("android.widget.EditText", 10)
# registration_page.fill_username_in_zebra_network_account_password_reset_page("jd4936")
# registration_page.enableCaptcha()
# sleep(2)
# while registration_page.checkSkipExists():
#     registration_page.clickSkip()
#     sleep(2)
# if registration_page.checkVerifyExists():
#     registration_page.clickVerify()
# registration_page.click_on_next()


def test_Registration_TestcaseID_45868():
    """""""""test"""""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.click_on_reset_password()
# sleep(5)
# if registration_page.check_if_in_password_recovery_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'Password Recovery' Page")
# registration_page.Enter_Username_password_recovery_page("smbmbzsb@gmail.com")
# registration_page.click_SUBMIT()
# if registration_page.check_submit_is_clickable():
#     raise Exception("Submit is clickable.")
# else:
#     print("Submit is not clickable.")


def test_Registration_TestcaseID_45869():
    """""""""test"""""


# login_page.click_loginBtn()
# login_page.click_Loginwith_Google()
# registration_page.click_Buy_More_Labels()
# help_page.verify_url("https://www.zebra.com/smb/us/en/labels.html")
# keyevent("back")
# keyevent("back")


def test_Registration_TestcaseID_45870():
    """""""""test"""""


# login_page.click_loginBtn()
# registration_page.click_Google_Icon()
# sleep(3)
# registration_page.verify_Sign_In_With_Google_Page()
# registration_page.sign_In_With_Google("zsbswdvt@123", "zsbswdvt@gmail.com", True)
# registration_page.sign_In_With_Google("zsbswdvt@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")


def test_Registration_TestcaseID_45871():
    """""""""test"""""


# login_page.click_loginBtn()
# registration_page.click_Apple_Icon()
# registration_page.login_Apple("zDLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com", True)
# registration_page.login_Apple("DLpwhvr@JCQ5Gkx")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# name = registration_page.get_login_name_from_menu()
# if name == "zsb swdvt":
#     pass
# else:
#     raise Exception("Login name does not match")
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_46303():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.click_Add_A_Printer()
# add_a_printer_page.click_Start_Button()
# add_a_printer_page.click_Show_All_Printers()
# sleep(3)
# registration_page.selectPrinter("ZSB-DP12\nC66871")
# data_sources_page.clickSelect()
# add_a_printer_page.click_Bluetooth_pairing_Popup1()
# add_a_printer_page.click_Bluetooth_pairing_Popup2()
# registration_page.clickConnect()
# sleep(3)
# registration_page.Enter_Password_Join_Network()
# sleep(2)
# poco(text("123456789"))
# registration_page.clickSubmit()
# time_taken = registration_page.timeTillWiFiGreen()
# print(time_taken)


def test_Registration_TestcaseID_46304():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.disable_bluetooth()
# if poco("android:id/message").exists():
#     add_a_printer_page.click_Bluetooth_pairing_Popup2()
# add_a_printer_page.click_Add_A_Printer()
# registration_page.verifyTurnOnBluetoothPopUp()
# add_a_printer_page.enable_bluetooth()
# sleep(2)
# if poco("android:id/message").exists():
#     add_a_printer_page.click_Bluetooth_pairing_Popup2()
#     data_sources_page.clickCancel()
# add_a_printer_page.click_Start_Button()
# add_a_printer_page.click_Show_All_Printers()
# sleep(5)
# registration_page.selectPrinter("ZSB-DP12\n879647")
# data_sources_page.clickSelect()
# """Cannot automate walking 10 m"""
# try:
#     registration_page.wait_for_element_appearance("Searching for Wi-Fi Networks", 50)
# except:
#     raise Exception("Bluetooth connection unsuccessful")


def test_Registration_TestcaseID_46305():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.disable_bluetooth()
# if poco("android:id/message").exists():
#     add_a_printer_page.click_Bluetooth_pairing_Popup2()
# add_a_printer_page.click_Add_A_Printer()
# registration_page.verifyTurnOnBluetoothPopUp()
# add_a_printer_page.enable_bluetooth()
# sleep(2)
# if poco("android:id/message").exists():
#     add_a_printer_page.click_Bluetooth_pairing_Popup2()
#     data_sources_page.clickCancel()
# add_a_printer_page.click_Start_Button()
# add_a_printer_page.click_Show_All_Printers()
# sleep(5)
# registration_page.selectPrinter("ZSB-DP12\n879647")
# data_sources_page.clickSelect()
# """Cannot automate walking 10 m"""
# if registration_page.unableToPairPrinterError():
#     print("Bluetooth process interrupted because bluetooth device out of range.")
# else:
#     raise Exception("Bluetooth process not interrupted even though bluetooth device out of range.")


def test_Registration_TestcaseID_46306():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.click_Add_A_Printer()
# add_a_printer_page.click_Start_Button()
# add_a_printer_page.click_Show_All_Printers()
# sleep(3)
# registration_page.selectPrinter("ZSB-DP12\nC66871")
# data_sources_page.clickSelect()
# add_a_printer_page.click_Bluetooth_pairing_Popup1()
# add_a_printer_page.click_Bluetooth_pairing_Popup2()
# try:
#     registration_page.wait_for_element_appearance("Searching for Wi-Fi Networks", 50)
# except:
#     raise Exception("Bluetooth connection unsuccessful")


def test_Registration_TestcaseID_46307():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.click_Add_A_Printer()
# add_a_printer_page.click_Start_Button()
# add_a_printer_page.click_Show_All_Printers()
# sleep(3)
# registration_page.selectPrinter("ZSB-DP12\n6CC28F")
# data_sources_page.clickSelect()
# registration_page.clickConnect()
# sleep(2)
# registration_page.Enter_Password_Join_Network()
# poco(text("123456789"))
# registration_page.clickSubmit()
# registration_page.clickFinishSetup()


def test_Registration_TestcaseID_47786():
    """""""""test"""""


# """Tell Tarun to change """
# others_page.uninstall_and_install_zsb_series_on_google_play(True)
# sleep(2)
# login_page.click_loginBtn()
# poco("Continue with Google").wait_for_appearance(timeout=10)
# login_page.click_Loginwith_Google()
# sleep(2)
# others_page.uninstall_and_install_zsb_series_on_google_play(True, True)
# sleep(2)
# login_page.click_loginBtn()
# poco("Continue with Google").wait_for_appearance(timeout=10)
# login_page.click_Loginwith_Google()
# sleep(2)
# """Token verification pending"""


def test_Registration_TestcaseID_47930():
    """""""""test"""""


# login_page.click_Menu_HamburgerICN()
# add_a_printer_page.click_Add_A_Printer()
# add_a_printer_page.click_Start_Button()
# registration_page.selectPrinter("ZSB-DP12\6CC28F")
# data_sources_page.clickSelect()
# registration_page.verifyUnableToPairPrinterError()
# registration_page.clickTryAgain()
# add_a_printer_page.click_Bluetooth_pairing_Popup1()
# add_a_printer_page.click_Bluetooth_pairing_Popup2()
# registration_page.clickConnect()
# sleep(3)
# registration_page.Enter_Password_Join_Network()
# sleep(2)
# poco(text("123456789"))
# registration_page.clickSubmit()


def test_Registration_TestcaseID_50287():
    """""""test"""


# login_page.click_loginBtn()
# data_sources_page.signInWithEmail()
# if poco("com.android.chrome:id/coordinator").exists():
#     poco("com.android.chrome:id/coordinator").click()
# registration_page.registerEmail()
# poco("android.widget.EditText").wait_for_appearance(timeout=20)
# a = registration_page.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
# registration_page.enter_user_email_for_registering("smbzsbmb@gmail.com")
# registration_page.click_on_next()
# poco(text="Return to Previous Step").wait_for_appearance(timeout=20)
# verification_code = "3U8H92"
# registration_page.enter_the_verification_code(verification_code)
# registration_page.click_on_next()
# sleep(5)
# if registration_page.check_email_verified_successfully_message():
#     pass
# else:
#     raise Exception("Email verified successfully message not present.")
# if registration_page.verify_user_information_and_account_security_page():
#     pass
# else:
#     raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
# first_name = "John"
# last_name = "Loke"
# registration_page.fill_first_name_field(first_name)
# registration_page.fill_last_name_field(last_name)
# while not poco(text="SUBMIT AND CONTINUE").exists():
#     scroll_view = poco("android.view.View")
#     scroll_view.swipe("up")
# registration_page.fill_password_field("Smbzsbmb@1234")
# registration_page.fill_confirm_password_field("Smbzsbmb@1234")
# registration_page.select_the_country("India")
# poco("android.widget.CheckBox")[0].click()
# poco("android.widget.CheckBox")[1].click()
# registration_page.click_submit_and_continue()
# sleep(4)
# registration_page.check_sign_up_successful()
# registration_page.click_continue_registration_page()
# poco("Login").wait_for_appearance(timeout=10)
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# """Provide the email and password"""
# email = "smbzsbmb@gmail.com"
# password = "Smbzsbmb@1234"
# registration_page.complete_sign_in_with_email(email, password, 1, 0 )
# while not poco(name="Accept", enabeled=True).exists():
#     poco.scroll()
# registration_page.click_decline()
# sleep(2)
# if registration_page.check_if_in_login_page():
#     pass
# else:
#     raise Exception("Logged in successfully even though declined EULA")
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# email = "smbmbzsb@gmail.com"
# password = "Zebratest123?"
# registration_page.complete_sign_in_with_email(email, password, 1, 0 )
# try:
#     registration_page.wait_for_element_appearance("End User\n License Agreement", 20)
#     raise Exception("Showing EULA page after logging in with existing account.")
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# try:
#     registration_page.wait_for_element_appearance("Login", 5)
# except:
#     raise Exception("Did not redirect to the login page")
# poco("Login").wait_for_appearance(timeout=10)
# login_page.click_loginBtn()
# registration_page.wait_for_element_appearance_text("Continue with Google", 10)
# data_sources_page.signInWithEmail()
# """Provide the email and password"""
# email = "smbzsbmb@gmail.com"
# password = "Smbzsbmb@1234"
# registration_page.complete_sign_in_with_email(email, password, 1, 0 )
# try:
#     registration_page.wait_for_element_appearance("End User\n License Agreement", 20)
#     pass
# except:
#     raise Exception("Showing EULA page after logging in with existing account.")

registration_page.create_google_account()
