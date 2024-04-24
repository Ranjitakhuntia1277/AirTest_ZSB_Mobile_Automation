import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Social_Login.Social_Login import Social_Login
from ZSB_Mobile.Common_Method import *
import os
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen

class test_Others():
    pass

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)

login_page = Login_Screen(poco)
social_login = Social_Login(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)

def test_Social_Login_TestcaseID_48464():
    pass

# try:
#     social_login.click_on_allow_for_notification()
# except:
#     pass
#
# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# res = social_login.check_zebra_logo()
# if not res:
#     raise Exception("Zebra logo not present")
#
# res = social_login.check_login_with_google()
# if not res:
#     raise Exception("Login with google not present")
#
# res = social_login.check_login_with_apple()
# if not res:
#     raise Exception("Login with Apple not present")
#
# res = social_login.check_login_with_facebook()
# if not res:
#     raise Exception("Login with Facebook not present")
#
# res = social_login.check_sign_in_with_email()
# if not res:
#     raise Exception("Sign in with email not present")
#
# res = social_login.check_text_of_free_benifits()
# if not res:
#     raise Exception("Check under the Sign in with your email option, there is a Learn more about the Benefits of Creating a Free ZSB Account, and the Benefits of Creating a Free Account is highlighted in blue")
#
# social_login.scroll_down(1)
#
# social_login.check_the_cookie_text()
#
# res = social_login.check_options_under_cookie_text()
# if not res:
#     raise Exception("options are not proper or missing")

# stop_app("com.zebra.soho_app")
# start_app("com.zebra.soho_app")
def test_Social_Login_TestcaseID_48465():
    pass

# try:
#     social_login.click_on_allow_for_notification()
# except:
#     pass
# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# social_login.click_on_benefits_of_zebra_account()
# sleep(2)
# res = social_login.check_the_text_of_benefits_of_free_account_page()
# if not res:
#     raise Exception("the page text dint match")
# social_login.scroll_up(1)
# social_login.check_both_images_in_benefits_of_free_account_page()
# res = social_login.check_the_back_button()
# if not res:
#     raise Exception("No back button")
# social_login.click_on_the_back_button()
# res = social_login.check_login_with_google()
# if not res:
#     raise Exception("6. Click on the back button Check it will back to sign in page fails")

def test_Social_Login_TestcaseID_48466():
    pass

# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# try:
#     social_login.open_in_chrome()
# except:
#     pass
# social_login.swith_back_the_app()
# sleep(1)
# social_login.scroll_down(1)
# social_login.click_on_zebra_link()
# if not social_login.verify_the_url("zebra.com."):
#     raise Exception("zebra.com url not present")
# social_login.go_back()
# social_login.swith_back_the_app()
# social_login.click_on_legal_notice_link()
# if not social_login.verify_the_url("zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html"):
#     raise Exception("zebra.com url not present")
# social_login.go_back()
# social_login.swith_back_the_app()
# sleep(1)
# social_login.click_on_privacy_statement_link()
# if not social_login.verify_the_url("zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html"):
#     raise Exception("zebra.com url not present")

def test_Social_Login_TestcaseID_48475():
    pass

# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# social_login.click_on_sign_in_with_email()
# keyevent("back")
# sleep(1)
# social_login.scroll_down(1)
#
# """Reset The password"""
# social_login.click_on_reset_password()
# social_login.wait_for_element_appearance_text("Password Recovery",20)
# sleep(1)
# username = "zebratest850@gmail.com"
# social_login.enter_user_name_to_change_password(username)
# social_login.click_on_submit_button()
#
# common_method.wait_for_element_appearance_namematches("Click here")
# social_login.click_here_button_click()
# """Cant Automate this step 3. Input the prepare email address, follow the steps to finish reseting pw
# Check the pw can be reset successfully without any error"""
# """Enter the temp_pass was temporary password which is got through Mail and enter new password"""
#
# """Semi automated here pass temp password"""
#
# """Part2"""
# common_method.wait_for_element_appearance_textmatches("Reset Password",30)
# sleep(30)
# new_pass = "Zebra#@85085085"
# social_login.enter_the_new_password_with_temporary_password(new_pass)
#
# social_login.click_on_submit_button()

# try:
#     social_login.wait_for_element_appearance_text("Password changed successfully.",20)
# except:
#     raise Exception("password changed confirmation dint receive")
#
# try:
#     common_method.wait_for_element_appearance_namematches("Click here")
#     social_login.click_here_button_click()
# except:
#     pass
# common_method.wait_for_element_appearance_namematches("Continue with Google",15)
# social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email("zebratest850@gmail.com",new_pass)
#
# try:
#     social_login.wait_for_element_appearance("Home",20)
# except:
#     raise Exception("dint sign in properly")

def test_Social_Login_TestcaseID_48473():
    pass

# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# social_login.click_on_sign_in_with_email()
# try:
#     social_login.check_element_present_name_matches("keyboard")
#     keyevent("back")
# except:
#     pass
#
# if not social_login.check_zebra_logo():
#     raise Exception("Zebra Logo not present")
#
# if not social_login.check_username_and_password_feilds():
#     raise Exception("user name or password fields not present ")
#
# if not social_login.check_sign_in_button():
#     raise Exception("sign in button not present")
#
# social_login.swipe_down_half(1)
#
# if not social_login.check_close_button():
#     raise Exception("close button not present")
#
# if not social_login.check_text_of_register_your_email():
#     raise Exception("text not matching for register your email now")
#
# if not social_login.check_reset_password_text():
#     raise Exception("text not matching for reset password feild")
#
# social_login.click_on_close_button()
#
# if social_login.check_close_button():
#     raise Exception("page dint close")

def test_Social_Login_TestcaseID_48474():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",20)
#
# social_login.click_on_sign_in_with_email()
# try:
#     social_login.click_register_your_email()
# except:
#     social_login.go_back()
#     social_login.click_register_your_email()
#
# sleep(2)
# common_method.wait_for_element_appearance_textmatches("ZSB Printer",20)
# a=social_login.check_registration_of_email()
# if not a:
#     raise Exception("register user page dint show")
#
# """Enter the User Email"""
# email="testzebra141@gmail.com"
# social_login.enter_user_email_for_registering(email)
# social_login.click_on_next()

# try:
#     social_login.wait_for_element_appearance("Resend Verification Code.",30)
# except:
#     raise Exception("Second step dint work")

# """Semi automated """
# """Enter Verification code"""
# verification_code = "31RPAG"
# social_login.enter_the_verification_code(verification_code)
# social_login.scroll_down(1)
# social_login.click_on_next()

# """Enter the first Name last name and the password"""
# common_method.wait_for_element_appearance_textmatches("ZSB Printer User Information and Account Security")
# sleep(2)
# first_n = "Zebra"
# last_n = "Z"
# password = "Zebra#123456789"
# social_login.enter_the_fields(first_n, last_n, password)
# social_login.select_the_country("India")
# try:
#     social_login.select_the_check_boxes()
#     social_login.select_the_check_boxes()
# except:
#     try:
#         social_login.scroll_down(1)
#         social_login.select_the_check_boxes()
#         social_login.select_the_check_boxes()
#     except:
#         pass
# social_login.click_submit_and_continue()
# sleep(2)
# social_login.check_sign_up_successful()
# social_login.click_on_continue()
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide the email and password"""
# social_login.complete_sign_in_with_email(email,password)

# try:
#     social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement")
# except:
#     raise Exception("EULA page dint show up")
#
# social_login.click_on_cancel_button_in_eula()
# social_login.click_on_exit_in_eula()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48482():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide new_user name and password which is not registered"""
# email = "testzebra120@gmail.com"
# password = "Zebra#123456789"
# first_name = "Zebra"
# last_name = "Z"
#
# social_login.complete_sign_in_with_email(email,password)
# social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement",20)
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.accept_EULA_agreement()
# social_login.click_on_cancel_button()
# social_login.click_on_exit_in_eula()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
#
# social_login.validate_the_details_of_account(first_name, last_name, email)
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
# sleep(2)
# social_login.complete_sign_in_with_email(email,password)
# common_method.wait_for_element_appearance_namematches("Home")
# if social_login.check_EULA():
#     raise Exception("Eula is dispayed")

def test_Social_Login_TestcaseID_50646():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# if not social_login.check_focused_of_user_name():
#     raise Exception("user name is not focused")
# if not social_login.check_key_board():
#     raise Exception("No key board displayed")
# if not social_login.check_key_board():
#     raise Exception("keyboard dint show up")

def test_Social_Login_TestcaseID_48467():
    pass

# """Login with an existing account"""
# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# password = "Zebra#123456789"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",30)
#
# """Check whether logged in to same account as email"""
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("the email is not matching")
#
# """Log out"""
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",10)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_50643():
    pass

# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
#
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",10)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
#
# login_page.click_Loginwith_Google()
#
# if not social_login.verify_choose_an_account_text():
#     raise Exception("did not redirect to the choose an acoount page")

def test_Social_Login_TestcaseID_50612():
    pass

# login_page.click_loginBtn()
#
# common_method.wait_for_element_appearance_namematches("Continue with Google")
# """Enter the email and password"""
# email = "zebratest850@gmail.com"
# password = 'Zebra#123456789'
#
# social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email(email,password,0)
# social_login.show_the_password()
# sleep(4)
# res = social_login.get_the_password()
# print(res)
# if str(res) != str(password):
#     raise Exception("password is not matching")

def test_Social_Login_TestcaseID_48486():
    pass

# login_page.click_loginBtn()
#
# """Enter the email and password"""
# email = ""
# password = ''
# common_method.wait_for_element_appearance_namematches("Continue with Google")
#
# social_login.click_on_sign_in_with_email()
#
# social_login.complete_sign_in_with_email(email,password,1)
# sleep(3)
# if not social_login.check_for_blank_value_error_of_both():
#     raise Exception("Error not displayed for blank values")
#
# email = "zebratest852@gmail.com"
# social_login.complete_sign_in_with_email(email,password,1,0)
# if not social_login.check_for_blank_value_error_of_password():
#     raise Exception("Error not displayed for blank values")
#
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email , password , 1,0)
# try:
#     social_login.wait_for_element_appearance("Home",20)
# except:
#     raise Exception('did not sign in properly')

def test_Social_Login_TestcaseID_48483():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide new_user name and password which is registered"""
# email = "zebratest852@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password)
# if social_login.check_EULA():
#     social_login.accept_EULA_agreement()
#
# social_login.wait_for_element_appearance("Home", 20)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# first_name = "Zebra"
# last_name = "Zebra"
# social_login.validate_the_details_of_account(first_name, last_name, email)
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("Email are not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48485():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google")
# social_login.click_on_sign_in_with_email()
# """Incorrect password but correct email"""
# """Enter the email and password"""
# email = "zebratest852@gmail.com"
# password = 'Zebra#1234567890'
#
# # social_login.click_on_sign_in_with_email()
# social_login.complete_sign_in_with_email(email,password,1)
# if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
#     raise Exception("Error not displayed for incorrect password values")
#
# sleep(1)
# """Incorrect Email but correct password"""
# email = "zebratest85@gmail.com"
# password = 'Zebra#123456789'
#
# social_login.click_on_sign_in_with_email()
#
# social_login.complete_sign_in_with_email(email,password,1,1)
# if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
#     raise Exception("Error not displayed for incorrect email")
#
# sleep(1)
# social_login.click_on_sign_in_with_email()
#
# """Correct password and email"""
# email = "testzebra141@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password,1,1)
# if social_login.wait_for_element_appearance("Home",10):
#     raise Exception('did not sign in properly')

def test_Social_Login_TestcaseID_48479():
    pass

# """Enter invalid user name in google id feild"""
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google")
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
# social_login.sign_in_with_google()
# common_method.wait_for_element_appearance_textmatches("ext")
#
# social_login.enter_user_name_in_google("zsb@gmail.com")
# social_login.click_on_next_in_google_sing_in()
# sleep(1)
#
# if not social_login.check_for_incorrect_username_in_google():
#     raise Exception("error not found for incorrect email")
#
# """Select a proper gmail account"""
# social_login.go_back()
# social_login.go_back()
# login_page.click_loginBtn()
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google")
# login_page.click_Loginwith_Google()
#
# t=social_login.get_one_of_the_gmail_accounts()
# social_login.choose_a_google_account(t)
#
# social_login.wait_for_element_appearance("Home",10)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# social_login.wait_for_element_appearance("Sign In",10)

def test_Social_Login_TestcaseID_48470():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
# email="testzebra118@gmail.com"
# social_login.choose_a_google_account(email)
# sleep(3)
# try:
#     social_login.click_on_continue()
# except:
#     pass
# try:
#     social_login.click_on_both_check_boxes_in_google_first_time_login()
#     social_login.click_on_submit_button()
#     sleep(2)
#     social_login.click_on_continue()
# except:
#     pass
# try:
#     social_login.click_on_continue()
# except:
#     pass
# social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement",20)
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.accept_EULA_agreement()
# social_login.click_on_cancel_button()
# social_login.click_on_exit_in_eula()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Semi automated check manually"""
# """Pass the first name last name and email to be expected"""
# # first_name = "Zebra"
# # last_name = "Test"
# # if not social_login.check_the_email_in_profile_page(email):
# #     raise Exception("emails are not matching ")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
#
# if social_login.check_EULA():
#     raise Exception("Eula is dispayed")

def test_Social_Login_TestcaseID_48472():
    pass
# email = "testswdvt@gmail.com"
# password = "Zebra#123456789"
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
#
# try:
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log In")
# except:
#     pass
#
# social_login.continue_in_facebook()
# social_login.wait_for_element_appearance_text("Submit",10)
#
# try:
#     social_login.click_on_both_check_boxes_in_google_first_time_login()
#     social_login.click_on_submit_in_facebook()
#     social_login.wait_for_element_appearance_text("Continue",10)
#     social_login.click_on_continue()
# except:
#     pass
#
# social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement",20)
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.accept_EULA_agreement()
# social_login.click_on_cancel_button()
# social_login.click_on_exit_in_eula()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# """Semi automated"""
# # first_name = "Zebra"
# # last_name = "Zebra"
# # # social_login.validate_the_details_of_account(first_name, last_name, email)
# # if not social_login.check_the_email_in_profile_page(email):
# #     raise Exception("email not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
# try:
#
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log In")
#     sleep(3)
#
# except:
#     pass
#
# social_login.continue_in_facebook()
#
# social_login.wait_for_element_appearance("Home",10)
#
# if social_login.check_EULA():
#     raise Exception("Eula is dispayed")

def test_Social_Login_TestcaseID_48481():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
# social_login.wait_for_element_appearance_text("Log in",10)
#
# email = "wrongemail.com"
# password = "Zebra#123456"
# social_login.enter_username_and_password_in_facebook(email,password)
# try:
#     social_login.click_element_by_text("Log In")
# except:
#     social_login.click_element_by_text("Log in")
# sleep(3)
# social_login.go_back()
#
# if not social_login.check_wrong_user_name_error_in_facebook():
#     raise Exception("error not shown for wrong user name")
#
# email = "testswdvt@gmail.com"
# password = "Zebra#1234567"
# social_login.enter_username_and_password_in_facebook(email,password)
# try:
#     social_login.click_element_by_text("Log In")
# except:
#     social_login.click_element_by_text("Log in")
# sleep(3)
#
# social_login.go_back()
#
# if not social_login.check_wrong_password_error_in_facebook():
#     raise Exception("error not shown for wrong password")
#
# try:
#     email = "testswdvt@gmail.com"
#     password = "Zebra#123456789"
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log in")
#     sleep(3)
#
# except:
#     try:
#         social_login.click_element_by_text("Log In")
#     except:
#         pass
#
# social_login.continue_in_facebook()
#
# social_login.wait_for_element_appearance("Home",20)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# first_name = "Zebra"
# last_name = "Zebra"
# # social_login.validate_the_details_of_account(first_name, last_name, email)
# email="testswdvt@gmail.com"
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("email not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48469():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
#
# try:
#     social_login.wait_for_element_appearance_text("Log in", 10)
#
#     email = "testswdvt@gmail.com"
#     password = "Zebra#123456789"
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log in")
#     sleep(3)
#
# except:
#     pass
#
# social_login.continue_in_facebook()
#
# try:
#     common_method.wait_for_element_appearance_namematches("For the best experience, we need a couple things from you.",3)
#     social_login.click_on_both_check_boxes_in_google_first_time_login()
#     social_login.click_on_submit_button()
# except:
#     pass
#
# try:
#     social_login.continue_in_facebook()
# except:
#     pass
#
# social_login.wait_for_element_appearance("Home",30)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Pass the first name last name and email to be expected"""
# first_name = "Zebra"
# last_name = "Zebra"
# # social_login.validate_the_details_of_account(first_name, last_name, email)
# email = "testswdvt@gmail.com"
# if not social_login.check_the_email_in_profile_page(email):
#     raise Exception("email not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48478():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
#
# try:
#     social_login.wait_for_element_appearance_text("Log In", 10)
#
#     email = "testswdvt@gmail.com"
#     password = "Zebra#123456789"
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log In")
#     sleep(3)
#
# except:
#     pass
#
# social_login.continue_in_facebook()
#
# social_login.wait_for_element_appearance("Home",20)
#
# """Semi automated"""
# # login_page.click_Menu_HamburgerICN()
# # add_a_printer_page.click_Add_A_Printer()
# #
# # add_a_printer_page.click_Start_Button()
# # add_a_printer_page.click_Show_All_Printers()
# # sleep(4)
# #
# # social_login.selectPrinter("ZSB-DP12\n6CC28F")
# # social_login.clickSelect()
# # try:
# #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
# # except:
# #     pass
# # try:
# #     social_login.click_Bluetooth_pairing_Popup2()
# # except:
# #     pass
# #
# # social_login.clickConnect()
# # sleep(2)
# # social_login.Enter_Password_Join_Network("123456789")
# # sleep(2)
# # poco(text("123456789"))
# # #
# # common_method.wait_for_element_appearance("Submit")
# #
# # social_login.clickSubmit()
# # social_login.clickFinishSetup()
# sleep(2)
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
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
#
# try:
#     social_login.wait_for_element_appearance_text("Log In", 10)
#
#     email = "testswdvt@gmail.com"
#     password = "Zebra#123456789"
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log In")
#     sleep(3)
#
# except:
#     pass
#
# social_login.continue_in_facebook()
#
# social_login.wait_for_element_appearance("Home",20)
#
# if not social_login.check_printer_not_there_in_home_page():
#     raise Exception("printer found in home page")

def test_Social_Login_TestcaseID_48480():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot",10)
#
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#12345678"
# social_login.enter_apple_id_and_password(apple_id,password)
#
# social_login.click_element_by_text("Apple\xa0ID")
# sleep(2)
#
# if not social_login.check_for_incorrect_error_in_apple():
#     raise Exception("No error raised for wrong password or username")
#
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#123456789"
# social_login.enter_apple_id_and_password(apple_id,password)
#
# """Enter two factor authentication if required"""
# try:
#     common_method.wait_for_element_appearance_textmatches("Two-",4)
#     # social_login.go_back()
#     code="661850"
#     social_login.two_factor_authentication_for_apple(code)
#     sleep(2)
# except:
#     pass
#
# try:
#     social_login.apple_trust_this_browser()
# except:
#     pass
# social_login.click_on_continue()
# social_login.wait_for_element_appearance("Home")
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48471():
    pass

# """Need to create a new apple account"""
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#123456789"
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot ",10)
# try:
#     social_login.enter_apple_id_and_password(apple_id,password)
# except:
#     pass
#
# try:
#     social_login.click_on_continue()
# except:
#     pass
#
# """Enter the two factor authentication code sent in phone """
# a = "183795"
# try:
#     social_login.two_factor_authentication_for_apple(a)
# except:
#     pass
#
# social_login.apple_trust_this_browser()
# social_login.continue_steps_in_apple()
#
# try:
#     social_login.click_on_both_check_boxes_in_google_first_time_login()
#     sleep(1)
#     social_login.click_on_submit_button()
#     sleep(2)
# except:
#     pass
#
# social_login.click_on_continue()
#
# social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement",20)
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.accept_EULA_agreement()
# social_login.click_on_cancel_button()
# social_login.click_on_exit_in_eula()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# """Semi automated check manually"""
# """Pass the first name last name and email to be expected"""
# # first_name = "Zebra"
# # last_name = "Zebra"
# # email = "testzebra101@gmail.com"
# # social_login.validate_the_details_of_account(first_name, last_name, email)
# # """if you hide email in the first time sign in process email cannot be validated"""
# # if not social_login.check_the_email_in_profile_page(email):
# #     print("email did not match")
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot ",10)
# try:
#
#     social_login.enter_apple_id_and_password(apple_id,password)
# except:
#     pass
#
# try:
#     social_login.click_on_continue()
# except:
#     pass
# social_login.wait_for_element_appearance("Home")
#
# if social_login.check_EULA():
#     raise Exception("Eula is dispayed")

def test_Social_Login_TestcaseID_48468():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",15)
#
# social_login.click_login_with_apple()
# common_method.wait_for_element_appearance_textmatches("Forgot",15)
#
# """Sign in"""
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#123456789"
# social_login.enter_apple_id_and_password(apple_id,password)
#
#
# """IF two factor authentication requires"""
# try:
#     common_method.wait_for_element_appearance_textmatches("Two-factor authentication",4)
#     # social_login.go_back()
#     code="902509"
#     social_login.two_factor_authentication_for_apple(code)
# except:
#     pass
# try:
#     common_method.wait_for_element_appearance_textmatches("Trust",6)
#     social_login.apple_trust_this_browser()
# except:
#     pass
# sleep(1)
#
# social_login.click_on_continue()
# social_login.wait_for_element_appearance("Home",30)
#
# """Log out"""
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# first_name = "swdvt"
# last_name = "test"
# if not social_login.validate_the_details_of_account(first_name, last_name):
#     raise Exception("credentials not matching")
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_test_48477():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot ",10)
#
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#123456789"
# social_login.enter_apple_id_and_password(apple_id,password)
#
# try:
#     code="259063"
#     social_login.two_factor_authentication_for_apple(code)
# except:
#     pass
#
# try:
#     social_login.apple_trust_this_browser()
# except:
#     pass
#
# social_login.click_on_continue()
# social_login.wait_for_element_appearance("Home",30)
#
# """Semi automated"""
# # login_page.click_Menu_HamburgerICN()
# # add_a_printer_page.click_Add_A_Printer()
# #
# # add_a_printer_page.click_Start_Button()
# # add_a_printer_page.click_Show_All_Printers()
# # sleep(4)
# #
# # social_login.selectPrinter("ZSB-DP12\n6CC28F")
# # social_login.clickSelect()
# # try:
# #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
# # except:
# #     pass
# # try:
# #     social_login.click_Bluetooth_pairing_Popup2()
# # except:
# #     pass
# #
# # social_login.clickConnect()
# # sleep(2)
# # social_login.Enter_Password_Join_Network("123456789")
# # sleep(2)
# # poco(text("123456789"))
# # #
# # common_method.wait_for_element_appearance("Submit")
# #
# # social_login.clickSubmit()
# # social_login.clickFinishSetup()
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
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot ",10)
#
# social_login.enter_apple_id_and_password(apple_id,password)
#
# try:
#     code="259063"
#     social_login.two_factor_authentication_for_apple(code)
# except:
#     pass
#
# try:
#     social_login.apple_trust_this_browser()
# except:
#     pass
#
# social_login.click_on_continue()
# social_login.wait_for_element_appearance("Home",30)
#
# if not social_login.check_printer_not_there_in_home_page():
#     raise Exception("printer found in home page")


def test_Social_Login_TestcaseID_50223():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
# email="testzebra265@gmail.com"
# social_login.choose_a_google_account(email)
# sleep(3)
# try:
#     social_login.click_on_continue()
# except:
#     pass
# try:
#     social_login.click_on_both_check_boxes_in_google_first_time_login()
#     social_login.click_on_submit_button()
#     sleep(2)
#     social_login.click_on_continue()
# except:
#     pass
# social_login.wait_for_element_appearance_namematches_all("End User",20)
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.decline_EULA_agreement()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# common_method.wait_for_element_appearance_namematches("Continue with Google")
#
# login_page.click_Loginwith_Google()
# common_method.wait_for_element_appearance_textmatches("Choose an account")
#
# social_login.choose_a_google_account("zebratest850@gmail.com")
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
#
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google",10)
#
# login_page.click_Loginwith_Google()
# social_login.choose_a_google_account(email)

# social_login.wait_for_element_appearance_namematches_all("End User",20)
#
# if not social_login.check_EULA():
#     raise Exception("EULA Not displayed")
#
# social_login.accept_EULA_agreement()
# social_login.wait_for_element_appearance("Home",10)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google",10)
#
#
# login_page.click_Loginwith_Google()
# social_login.choose_a_google_account(email)
# sleep(5)
# if social_login.check_EULA():
#     raise Exception("EULA  displayed")

def test_Social_Login_TestcaseID_48484():
    pass

# """Sign in with email"""
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# social_login.click_on_sign_in_with_email()
#
# """Provide the email and password"""
# email = "zebratest852@gmail.com"
# password = "Zebra#123456789"
# social_login.complete_sign_in_with_email(email,password)
#
# try:
#     social_login.wait_for_element_appearance("Home",20)
# except:
#     raise Exception("home page dint show up")
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# """Google sign in"""
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",10)
# except:
#     raise Exception("Did not redirect to the login page")
#
# """Apple sign in"""
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_apple()
# social_login.wait_for_element_appearance_text("Forgot ",10)
#
# """Sign in"""
# apple_id = "testzebra101@gmail.com"
# password = "Zebra#123456789"
# social_login.enter_apple_id_and_password(apple_id,password)
#
# """semi automated"""
# try:
#     common_method.wait_for_element_appearance_textmatches("Two-",4)
#     social_login.go_back()
#     code="666773"
#     social_login.two_factor_authentication_for_apple(code)
#     sleep(1)
# except:
#     pass
#
# try:
#     social_login.apple_trust_this_browser()
#     sleep(2)
# except:
#     pass
#
# social_login.click_on_continue()
# social_login.wait_for_element_appearance("Home")
#
# """Log out"""
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")
#
# """Facebook Sign in"""

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
#
# social_login.click_login_with_facebook()
#
# try:
#     social_login.wait_for_element_appearance_text("Log In", 10)
#
#     email = "testswdvt@gmail.com"
#     password = "Zebra#123456789"
#     social_login.enter_username_and_password_in_facebook(email,password)
#     social_login.click_element_by_text("Log In")
#     sleep(3)
#
# except:
#     pass
#
# social_login.continue_in_facebook()
#
# social_login.wait_for_element_appearance("Home",20)
#
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()

# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",5)
# except:
#     raise Exception("Did not redirect to the login page")

def test_Social_Login_TestcaseID_48476():
    pass
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
#
# """Enter the email"""
# email = "zebratest850@gmail.com"
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",10)
#
# # login_page.click_Menu_HamburgerICN()
# # add_a_printer_page.click_Add_A_Printer()
# #
# # add_a_printer_page.click_Start_Button()
# # add_a_printer_page.click_Show_All_Printers()
# # sleep(4)
# #
# # social_login.selectPrinter("ZSB-DP12\n6CC28F")
# # social_login.clickSelect()
# # try:
# #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
# # except:
# #     pass
# # try:
# #     social_login.click_Bluetooth_pairing_Popup2()
# # except:
# #     pass
# #
# # social_login.clickConnect()
# # sleep(2)
# # social_login.Enter_Password_Join_Network("123456789")
# # sleep(2)
# # poco(text("123456789"))
# # #
# # common_method.wait_for_element_appearance("Submit")
# #
# # social_login.clickSubmit()
# # social_login.clickFinishSetup()
# #
# # login_page.click_Menu_HamburgerICN()
# # social_login.click_Printer_Settings()
# # social_login.click_on_first_printer()
# # social_login.click_test_print()
# # sleep(3)
# login_page.click_Menu_HamburgerICN()
# social_login.click_home_button()
# social_login.click_three_dots_in_printer()
# social_login.click_delete_button()
# social_login.click_delete_button()
#
# social_login.confirm_delete_printer()
# add_a_printer_page.disable_bluetooth()

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
# login_page.click_Menu_HamburgerICN()
# social_login.click_on_profile_edit()
#
# social_login.scroll_down(1)
# social_login.click_log_out_button()
# try:
#     social_login.wait_for_element_appearance("Sign In",10)
# except:
#     raise Exception("Did not redirect to the login page")
#
# login_page.click_loginBtn()
# social_login.wait_for_element_appearance_text("Continue with Google",10)
# login_page.click_Loginwith_Google()
#
# social_login.choose_a_google_account(email)
# social_login.wait_for_element_appearance("Home",20)
#
# if not social_login.check_printer_not_there_in_home_page():
#     raise Exception("printer found in home page")

def test_Social_Login_TestcaseID_50613():
    pass

# login_page.click_loginBtn()
# social_login.wait_for_element_appearance("Continue with Google")
# login_page.click_Loginwith_Google()
# social_login.sign_in_with_google()
# social_login.wait_for_element_appearance("identifierId")
# #
# social_login.enter_user_name_in_google("zebratest_o1@outlook.com")
# social_login.click_on_next_in_google_sing_in()
# if not social_login.check_for_incorrect_username_in_google():
#     raise Exception("error not found for incorrect email")