import datetime
import os
import time
import random
import string

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
import platform
if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\\templates",
                            a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)

common_method = Common_Method(poco)


class Registration_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.log_out_button = "Log Out"
        self.Google_Icon = Template(Basic_path(r"Google_Icon.png"), record_pos=(-0.319, -0.173),
                                    resolution=(1080, 2340))
        self.Facebook_Icon = Template(Basic_path(r"Facebook_Icon.png"), record_pos=(-0.316, 0.094),
                                      resolution=(1080, 2340))
        self.Apple_Icon = Template(Basic_path(r"Apple_Icon.png"), record_pos=(-0.317, -0.043), resolution=(1080, 2340))
        self.next_tab_iOS = Template(Basic_path(r"next_tab_iOS.png"), record_pos=(-0.328, 0.279), resolution=(1170, 2532))
        self.Password_Field = "SecureTextField"

    def clickSignIn(self):
        sleep(5)
        signInBtn = self.poco("Sign In")
        signInBtn.click()
        sleep(2)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        else:
            packagename = "com.zebra.soho"
            stop_app(packagename)
            sleep(2)
            start_app(packagename)
            sleep(4)
            signInBtn = self.poco("Sign In")
            signInBtn.click()
            sleep(2)
            self.poco("Continue").click()
        sleep(3)

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance(self, element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def complete_sign_in_with_email(self, user_name, password, wrong_password=False,
                                    enter_only_password=False):
        sleep(4)
        if not enter_only_password:
            text(user_name)
        sleep(4)
        start_point = (0.57, 0.47)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.297, 0.211)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        password = self.poco(self.Password_Field)
        password.click()
        sleep(2)
        self.poco(text("Zebra#123456789"))
        if wrong_password:
            try:
                self.poco("We didn't recognize the username or password you entered. Please try again.")
            except:
                raise Exception("Error message not displayed for wrong password.")
        sleep(4)

    def click_on_profile_edit(self):
        sleep(5)
        self.poco("Button").click()

    def scroll_till_log_out(self):
        while not self.poco("Log Out").exists():
            start_point = (0.5, 0.8)
            vector = (0.5, 0.4)
            swipe(start_point, vector)

    def click_log_out_button(self):
        log_out_btn = self.poco(self.log_out_button)
        log_out_btn.click()

    def click_Google_Icon(self):
        touch(self.Google_Icon)

    def click_Facebook_Icon(self):
        try:
            self.poco("Continue with Facebook").click()
        except:
            touch(self.Facebook_Icon)

    def click_Apple_Icon(self):
        sleep(3)
        touch(self.Apple_Icon)
        sleep(5)
        if self.poco(nameMatches="(?s).*Do you want to sign in to ZSB Series with your Apple.*").exists():
            print("inside if")
            self.poco(nameMatches=".*Use a different Apple.*").click()

    def click_on_next(self):
        self.poco(text="Next").click()

    def addAccountToDevice(self):
        add_acc = self.poco(text="Add account to device")
        add_acc.click()

    def sign_In_With_Google(self, password, username=None, wrong_password=False):
        if username is not None:
            self.poco("Email or phone").wait_for_appearance(timeout=20)
            self.poco("Email or phone").click()
            text(username)
        try:
            self.poco("Your device will ask for your fingerprint, face, or screen lock").wait_for_appearance(timeout=20)
            self.poco("Try another way").click()
            self.poco("Enter your password").click()
            self.poco("Enter your password").click()
            text(password)
            if wrong_password:
                try:
                    self.wait_for_element_appearance(
                        "Wrong password. Try again or click ‘Forgot password’ to reset it.")
                except:
                    try:
                        self.wait_for_element_appearance_text(
                            "Wrong password. Try again or click Forgot password to reset it.")
                    except:
                        raise Exception(
                            "Error message: \"Wrong password. Try again or click Forgot password to reset it.\" not displayed.")
        except PocoTargetTimeout:
            pass
        try:
            self.poco("Enter your password").wait_for_appearance(timeout=20)
            self.poco("Enter your password").click()
            text(password)
            if wrong_password:
                try:
                    self.wait_for_element_appearance(
                        "Wrong password. Try again or click ‘Forgot password’ to reset it.")
                except:
                    try:
                        self.wait_for_element_appearance_text(
                            "Wrong password. Try again or click Forgot password to reset it.")
                    except:
                        raise Exception(
                            "Error message: \"Wrong password. Try again or click Forgot password to reset it.\" not displayed.")
        except Exception as e:
            raise Exception(e)
        try:
            self.poco("ZSB Series wants additional access to your Google Account").wait_for_appearance(timeout=20)
            start_point = (0.5, 0.8)
            vector = (0.5, 0.4)
            swipe(start_point, vector)
            self.poco("Continue").click()
        except PocoTargetTimeout:
            pass

    def login_Facebook(self, password, username=None, wrong_password=False):
        if username is not None:
            start_point = (0.5, 0.8)
            vector = (0.5, 0.4)
            swipe(start_point, vector)

            self.poco("English (UK)").click()

            start_point = (0.5, 0.4)
            vector = (0.5, 0.8)
            swipe(start_point, vector)

            self.poco("TextField").click()
            text(username)

        self.poco("SecureTextField").click()
        text(password)

        sleep(2)
        if self.poco("We can send you a login code").exists():
            self.poco("Try Another Way").click()
            sleep(2)
            if self.poco("This is your recommended way to log in.").exists():
                self.poco("Try Another Way")[1].focus([0.5, 0.9]).click()
                self.poco("Enter Password to Log In").click()
                self.poco("Continue").click()
                sleep(2)
                self.poco("SecureTextField").click()
                text(password)
        if wrong_password:
            try:
                self.wait_for_element_appearance("Incorrect password.")
                self.wait_for_element_appearance("Have you forgotten your password?")
            except:
                try:
                    self.wait_for_element_appearance("Incorrect password. Try again.")
                except:
                    raise Exception(
                        "Error message \"Incorrect password. Try again.\"not displayed for wrong password.")

    def login_Apple(self, password, username=None, wrong_password=False):
        if username is not None:
            self.poco("Email or Phone Number").wait_for_appearance(timeout=10)
            self.poco("Email or Phone Number").click()
            text(username)
        self.poco("password").wait_for_appearance(timeout=10)
        self.poco("password").click()
        text(password)
        # changed during datasources test id- 45731
        if wrong_password:
            if self.poco(nameMatches="Your Apple.*ID or password was incorrect.").exists():
                print("Successfully displayed Error message for wrong password")
                return
            else:
                print("Error message not displayed for wrong password.")
                raise Exception("Error message not displayed for wrong password.")
        # message = "Enter otp received on google account " + username + password
        # common_method.show_message(message)
        sleep(5)
        try:
            self.poco("Trust").wait_for_appearance(timeout=40)
            self.poco("Trust").click()
        except:
            pass
        try:
            self.poco("Continue").wait_for_appearance(timeout=20)
            self.poco("Continue").click()
        except:
            pass

    def clickSubmit(self):
        sleep(2)
        try:
            self.poco("Submit").click()
        except:
            self.poco(text="Submit").click()

    def clickClose(self):
        sleep(3)
        if self.poco("Set up your printer").exists():
            self.poco("Set up your printer").parent().child("Button").click()

    def clickExit(self):
        sleep(3)
        if self.poco("Exit").exists():
            self.poco("Exit").click()

    def verify_if_on_EULA_page(self):
        sleep(10)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        try:
            self.wait_for_element_appearance("Click ‘Accept’ to indicate that you have read and agree to the ", 20)
        except:
            raise Exception("Did not reach EULA page")

    def click_accept(self):
        sleep(10)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        if self.poco("Accept").exists():
            self.poco("Accept").click()

    def registerEmail(self):
        sleep(4)
        start_point = (0.57, 0.47)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.297, 0.211)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        self.poco("Register Your Email Now").click()
        sleep(2)

    def click_on_reset_password(self):
        sleep(4)
        start_point = (0.57, 0.47)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.297, 0.211)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        self.poco("Reset Password").focus([.9, .2]).click()
        sleep(2)

    def enter_user_email_for_registering(self, email="zebra05.swdvt@gmail.com"):
        sleep(5)
        self.poco("TextField").click()
        text(email)

    def check_email_already_exists_page_title(self):
        try:
            self.wait_for_element_appearance("ZSB Account Already Exist.")
        except:
            raise Exception("Email already exists message did not appear.")

    def check_email_already_Exists_page_message(self):
        try:
            self.wait_for_element_appearance(
                "You already have an account with us, Please click the below \"Continue\" button to redirect to the application.")
        except:
            raise Exception(
                "\"You already have an account with us, Please click the below \"Continue\" button to redirect to the application.\" did not appear.")

    def check_if_on_ZSB_printer_account_registration_page(self):
        try:
            self.wait_for_element_appearance("ZSB Account Registration", 20)
        except:
            raise Exception("register user page dint show.")

    def check_if_in_password_recovery_page(self):
        try:
            self.wait_for_element_appearance("Password Recovery", 20)
        except:
            raise Exception("Did not navigate to 'Password Recovery' Page")
        sleep(2)

    def Enter_Username_password_recovery_page(self, email):
        sleep(2)
        self.poco("TextField").click()
        sleep(2)
        text(email)

    def check_message_on_success_page(self):
        return_message = False
        self.wait_for_element_appearance("Success!", 20)
        sleep(2)
        if self.poco("An email with a Password Reset Code has been sent to your email address.").exists():
            if self.poco("The OTP will expire in 10 minutes").exists():
                return_message = True
        if return_message:
            return
        else:
            raise Exception("Expected message not found on password reset success page.")

    def checkClickHerePresent(self):
        sleep(3)
        if self.poco("Click here").exists():
            pass
        else:
            raise Exception("\"Click here\" not present.")
        sleep(3)

    def click_on_Click_here(self):
        sleep(3)
        self.poco("Click here").click()

    def check_if_on_Reset_Password_page(self):
        try:
            self.wait_for_element_appearance("Reset Password")
        except:
            raise Exception("Did not navigate to password reset page.")

    def fillNewPassword(self, password):
        sleep(2)
        self.poco("SecureTextField")[0].click()
        sleep(2)
        text(password)

    def fillConfirmPassword(self, password):
        sleep(2)
        self.poco("SecureTextField")[1].click()
        sleep(2)
        text(password)

    def click_SUBMIT(self):
        sleep(2)
        start_point = (0.57, 0.47)
        vector = (0.297, 0.211)
        swipe(start_point, vector)
        sleep(3)
        self.poco("SUBMIT").click()
