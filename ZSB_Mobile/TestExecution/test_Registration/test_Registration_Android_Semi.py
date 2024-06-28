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
    """Create new email before running"""
    """Click signin"""
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.verifyLinksInSignInPage()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")
    help_page.verify_url("signup.zebra.com/content/userreg/us/en/register.html?appId=ZEMB")
    """Enter zebra Email"""
    registration_page.enter_user_email_for_registering("test123@zebra.com")
    registration_page.click_on_next()
    registration_page.check_zebra_mail_registration_error()
    help_page.closeTab()
    data_sources_page.clickCancel()
    sleep(3)
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    if poco("com.android.chrome:id/coordinator").exists():
        poco("com.android.chrome:id/coordinator").click()
    keyevent("back")
    registration_page.verifyLinksInSignInPage()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")

    email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")
    registration_page.enter_user_email_for_registering(email)
    registration_page.click_on_next()
    poco(text="Return to Previous Step").wait_for_appearance(timeout=20)
    registration_page.check_email_verification_page_message()
    sleep(600)
    """Wait for 10 min"""
    """Enter verification code manually"""
    common_method.show_message(
        "Enter verification code on the device ,verification code received in the newly created google account")
    registration_page.click_on_next()
    if registration_page.verify_verification_code_expired_error():
        pass
    else:
        raise Exception("Verification code expired error not present.")
    if registration_page.verify_resend_verification_code_btn_exists():
        pass
    else:
        raise Exception("Resend verification code button not present.")
    registration_page.click_resend_verification_code_btn()
    sleep(30)
    """Enter verification code manually"""
    registration_page.click_on_next()
    registration_page.verify_user_information_and_account_security_page()
    """Enter the first Name last name and the password"""
    first_name = "John"
    last_name = "Doe"
    password = "Zebra#123456789"
    registration_page.enter_the_fields(first_name, last_name, password)
    registration_page.select_the_country("India")
    registration_page.select_the_check_boxes()
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
    registration_page.click_on_sign_in_with_email()

    """Provide the email and password"""
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
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
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45857():
    pass
    common_method.show_message("Run testcase on stage build")
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
    poco(text="Return to Previous Step").wait_for_appearance(timeout=10)
    sleep(20)
    """Wait for 10 min"""
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
    registration_page.verify_if_all_fields_present()
    registration_page.verify_if_checkboxes_are_present_registration()
    while not poco(text="Email verified successfully!").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")
    scroll_view = poco("android.view.View")
    scroll_view.swipe("down")
    if registration_page.special_character_error_name_field("First Name", "John123!"):
        pass
    else:
        raise Exception("No error for using special character in First Name field.")
    sleep(2)
    if registration_page.special_character_error_name_field("Last Name", "Loke123!"):
        pass
    else:
        raise Exception("No error for using special character in Last Name field.")
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
    sleep(2)
    while not poco(text="Email verified successfully!").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")
    scroll_view = poco("android.view.View")
    scroll_view.swipe("down")
    first_name = "John"
    last_name = "Loke"
    registration_page.fill_first_name_field(first_name)
    registration_page.fill_last_name_field(last_name)
    while not poco(text="SUBMIT AND CONTINUE").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("up")
    registration_page.fill_password_field("Zebratest123?")
    registration_page.fill_confirm_password_field("sss?")
    registration_page.check_password_unmatch_error()
    password = "Zebra#123456789"
    registration_page.fill_confirm_password_field(password)
    registration_page.select_the_country("India")
    poco("android.widget.CheckBox")[1].click()
    poco("android.widget.CheckBox")[0].click()
    poco("android.widget.CheckBox")[0].click()
    registration_page.click_clear()
    if registration_page.check_error_message_after_clear():
        pass
    else:
        raise Exception("Fields not cleared after clicking clear.")
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
    while not poco(name="Accept", enabeled=True).exists():
        poco.scroll()
    registration_page.click_accept()
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    registration_page.home_page_overview("Johnny")
    registration_page.check_add_a_printer_exists()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")


def test_Registration_TestcaseID_45858():
    pass
    common_method.show_message("Create new email before running")
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.verifyLinksInSignInPage()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")
    email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")

    registration_page.enter_user_email_for_registering(email)
    try:
        registration_page.wait_for_element_appearance("Resend Verification Code.", 10)
    except:
        raise Exception("Page to enter verification code did not appear. ")
    """Enter verification code manually"""
    common_method.show_message(
        "Enter verification code on the device ,verification code received in the newly created google account")
    """Enter the User Email"""
    registration_page.click_on_next()
    sleep(2)
    """Enter the first Name last name and the password"""
    first_n = "Zebra"
    last_n = "Z"
    password = "Zebra#123456789"
    registration_page.enter_the_fields(first_n, last_n, password)
    registration_page.select_the_country("India")
    registration_page.select_the_check_boxes()
    registration_page.click_submit_and_continue()
    sleep(2)
    registration_page.check_sign_up_successful()
    registration_page.click_continue_registration_page()
    registration_page.wait_for_element_appearance("Sign In")
    registration_page.clickSignIn()
    registration_page.wait_for_element_appearance_text("Continue with Google", 10)
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    registration_page.verify_if_on_EULA_page()
    registration_page.click_accept()
    registration_page.clickClose()
    registration_page.clickExit()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")


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
    common_method.show_message(
        "Have gmail account:\nusername:zebra03.swdvt@gmail.com\npassword:Zebra#123456789 logged in a different device to view otp that is required in later part of the test case.")
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.click_on_reset_password()
    sleep(5)
    try:
        registration_page.check_if_in_password_recovery_page()
    except:
        raise Exception("Did not navigate to 'Password Recovery' Page")
    registration_page.Enter_Username_password_recovery_page("testing123@gmail.com")
    registration_page.click_SUBMIT()
    sleep(3)
    if registration_page.check_user_does_not_exist_error():
        pass
    else:
        raise Exception("User does not exist' error did not show up even after entering a non registered email.")
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.click_on_reset_password()
    sleep(5)
    try:
        registration_page.check_if_in_password_recovery_page()
    except:
        raise Exception("Did not navigate to 'Password Recovery' Page")
    email = "zebra03.swdvt@gmail.com"
    registration_page.Enter_Username_password_recovery_page(email)
    registration_page.click_SUBMIT()
    registration_page.wait_for_element_appearance_text("Success!", 10)
    if registration_page.check_message_on_success_page():
        pass
    else:
        raise Exception("Expected message not on success page.")
    """An email with a Password Reset Code has been sent to your email address. The OTP will expired in 10 minutes.- cannot be automated."""
    registration_page.click_on_Click_here()
    try:
        registration_page.check_if_on_Reset_Password_page()
    except:
        raise Exception("Did not navigate to password reset page.")
    registration_page.check_fields_on_Reset_Password_page()
    registration_page.click_SUBMIT()
    if registration_page.check_error_message_on_fields_on_Reset_Password_page():
        pass
    else:
        raise Exception("Error messages not as expected.")
    """Enter otp manually"""
    common_method.show_message(f"Enter otp received in the google account:\n{email}")
    password = "Zebra#123456789"
    registration_page.fillNewPassword(password)
    registration_page.fillConfirmPassword("Zebra#12345678")
    registration_page.click_SUBMIT()
    if registration_page.checkWrongConfirmPasswordErrorMessage():
        pass
    else:
        raise Exception(
            "\"Fields do not match.\" not displayed when entered different 'New Password' and 'Confirm Password'")
    registration_page.fillConfirmPassword(password)
    """Wait for 10 minutes """
    sleep(600)
    registration_page.click_SUBMIT()
    sleep(5)
    if registration_page.check_OTExpiredMessage():
        pass
    else:
        raise Exception("Expected OTP expired message not displayed.")
    registration_page.click_on_click_here()
    """Step 18. Click on Click here to login with your temporary password in Success! page not present"""
    registration_page.click_on_Click_here()
    registration_page.wait_for_element_appearance_text("Reset Password", 10)
    """Enter OTP manually"""
    common_method.show_message(
        f"Enter verification code on the device ,verification code received in the google account:\n{email}")
    registration_page.fillNewPassword(password)
    registration_page.fillConfirmPassword(password)
    registration_page.click_SUBMIT()
    registration_page.wait_for_element_appearance_text("Success!", 10)
    registration_page.check_successful_password_reset_page_message()
    registration_page.click_on_Click_here()
    try:
        registration_page.wait_for_element_appearance_text("Sign In With", 10)
    except:
        raise Exception("Did not reach Sign in page")
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email(email, password, 1, 0)
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")


def test_Registration_TestcaseID_45867():
    pass
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.click_on_reset_password()
    sleep(5)
    registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
    registration_page.click_SUBMIT()
    sleep(3)
    registration_page.check_if_in_zebra_network_account_password_reset_page()
    registration_page.check_fields_in_zebra_network_account_password_reset_page()
    registration_page.fill_username_in_zebra_network_account_password_reset_page("tt1234")
    registration_page.enableCaptcha()
    common_method.show_message("Complete captcha if asked.")
    registration_page.click_on_next()
    try:
        registration_page.wait_for_element_appearance_text("Password Reset Error", 10)
    except:
        raise Exception("Did not redirected to a page \"Password Reset Error\" page.")
    common_method.tearDown()
    registration_page.clickSignIn()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.click_on_reset_password()
    sleep(5)
    registration_page.Enter_Username_password_recovery_page("testing123@zebra.com")
    registration_page.click_SUBMIT()
    sleep(3)
    registration_page.check_if_in_zebra_network_account_password_reset_page()
    registration_page.check_fields_in_zebra_network_account_password_reset_page()
    registration_page.wait_for_element_appearance("android.widget.EditText", 10)
    registration_page.fill_username_in_zebra_network_account_password_reset_page("jd4936")
    registration_page.enableCaptcha()
    common_method.show_message("Complete captcha if asked.")
    sleep(2)
    while registration_page.checkSkipExists():
        registration_page.clickSkip()
        sleep(2)
    if registration_page.checkVerifyExists():
        registration_page.clickVerify()
    registration_page.click_on_next()


def test_Registration_TestcaseID_45871():
    pass

    common_method.tearDown()
    registration_page.clickSignIn()
    sleep(2)
    registration_page.verifyLinksInSignInPage()
    scroll_view = poco("android.view.View")
    try:
        common_method.wait_for_element_appearance_text("Sign In With")
    except:
        raise Exception("Did not navigate to Sign In with page.")
    while not poco(text="Sign In With"):
        scroll_view.swipe("down")
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("zDLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com", True)
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    name = registration_page.get_login_name_from_menu()
    if name == "zsb swdvt":
        pass
    else:
        raise Exception("Login name does not match")
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    common_method.Stop_The_App()


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


"""Ask about eula decline"""


# def test_Registration_TestcaseID_50287():
#     pass
#
#     common_method.tearDown()
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.registerEmail()
#     try:
#         registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
#     except:
#         raise Exception("register user page dint show")
#     email = common_method.get_user_input("Create a new google account and enter the mail-id in the input box")
#     registration_page.enter_user_email_for_registering(email)
#     registration_page.click_on_next()
#     poco(text="Return to Previous Step").wait_for_appearance(timeout=20)
#     """Enter verification code manually"""
#     common_method.show_message(
#         "Enter verification code on the device ,verification code received in the newly created google account")
#     registration_page.click_on_next()
#     sleep(5)
#     if registration_page.check_email_verified_successfully_message():
#         pass
#     else:
#         raise Exception("Email verified successfully message not present.")
#     if registration_page.verify_user_information_and_account_security_page():
#         pass
#     else:
#         raise Exception("Did not navigate to 'ZSB Printer User Information and Account Security' page.")
#     first_name = "John"
#     last_name = "Loke"
#     registration_page.fill_first_name_field(first_name)
#     registration_page.fill_last_name_field(last_name)
#     while not poco(text="SUBMIT AND CONTINUE").exists():
#         scroll_view = poco("android.view.View")
#         scroll_view.swipe("up")
#     password = "Zebra#123456789"
#     registration_page.fill_password_field(password)
#     registration_page.fill_confirm_password_field(password)
#     registration_page.select_the_country("India")
#     poco("android.widget.CheckBox")[0].click()
#     poco("android.widget.CheckBox")[1].click()
#     registration_page.click_submit_and_continue()
#     sleep(4)
#     registration_page.check_sign_up_successful()
#     registration_page.click_continue_registration_page()
#     try:
#         registration_page.wait_for_element_appearance("Sign In", 10)
#     except:
#         raise Exception("Did not return to login page.")
#     registration_page.clickSignIn()
#     registration_page.wait_for_element_appearance_text("Continue with Google", 10)
#     data_sources_page.signInWithEmail()
#     """Provide the email and password"""
#     registration_page.complete_sign_in_with_email(email, password, 1, 0)
#     registration_page.verify_if_on_EULA_page()
#     """No Delcine option on EULA page"""
#     try:
#         registration_page.wait_for_element_appearance("Welcome to ZSB Series", 20)
#     except:
#         raise Exception("Reached Home page without accepting EULA")
#     registration_page.clickSignIn()
#     registration_page.wait_for_element_appearance_text("Continue with Google", 10)
#     data_sources_page.signInWithEmail()
#     email = "smbmbzsb@gmail.com"
#     password = "Zebratest123?"
#     registration_page.complete_sign_in_with_email(email, password, 1, 0)
#     try:
#         registration_page.wait_for_element_appearance("Click ‘Accept’ to indicate that you have read and agree to the ",
#                                                       20)
#         raise Exception("Showing EULA page after logging in with existing account.")
#     except:
#         pass
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
#     try:
#         registration_page.wait_for_element_appearance("Sign In", 10)
#     except:
#         raise Exception("Did not return to login page.")  # registration_page.clickSignIn()
#     registration_page.wait_for_element_appearance_text("Continue with Google", 10)
#     data_sources_page.signInWithEmail()
#     """Provide the email and password"""
#     password = "Smbzsbmb@1234"
#     registration_page.complete_sign_in_with_email(email, password, 1, 0)
#     try:
#         registration_page.wait_for_element_appearance("End User\n License Agreement", 20)
#         pass
#     except:
#         raise Exception("Showing EULA page after logging in with existing account.")


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