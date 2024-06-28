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

common_method = Common_Method(poco)


class Registration_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.log_out_button = "Log Out"
        self.Google_Icon = Template(r"Google_Icon.png", record_pos=(-0.319, -0.173), resolution=(1080, 2340))
        self.Facebook_Icon = Template(r"Facebook_Icon.png", record_pos=(-0.316, 0.094), resolution=(1080, 2340))
        self.Apple_Icon = Template(r"Apple_Icon.png", record_pos=(-0.317, -0.043), resolution=(1080, 2340))
        self.next_tab_iOS = Template(r"next_tab_iOS.png", record_pos=(-0.328, 0.279), resolution=(1170, 2532))

    def clickSignIn(self):
        signInBtn = self.poco("Sign In")
        signInBtn.click()
        self.poco("Continue").click()

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance(self, element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def complete_sign_in_with_email(self, user_name, password, wrong_password=False,
                                    enter_only_password=False):

        if not enter_only_password:
            text(user_name)
        touch(self.next_tab_iOS)
        text(password)
        if wrong_password:
            try:
                self.poco("We didn't recognize the username or password you entered. Please try again.")
            except:
                raise Exception("Error message not displayed for wrong password.")

    def click_on_profile_edit(self):
        sleep(3)
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
        self.poco("Continue").click()

    def click_Facebook_Icon(self):
        try:
            self.poco("Continue with Facebook").click()
        except:
            touch(self.Facebook_Icon)

    def click_Apple_Icon(self):
        touch(self.Apple_Icon)

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

    def login_Apple(self, password, username=False, wrong_password=False):
        if username:
            self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
            self.poco("android.widget.EditText").set_text(username)
            self.poco("android.widget.Button")[1].click()
            if self.poco("com.android.chrome:id/coordinator").exists():
                self.poco("com.android.chrome:id/coordinator").click()
        self.poco("android.widget.EditText")[1].wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText")[1].set_text(password)
        self.poco(text="Sign In").click()
        # changed during datasources test id- 45731
        if wrong_password:
            self.poco("android.widget.TextView")[7].click()
            error_message = [self.poco("android.widget.TextView")[11].get_text()][0]
            print(error_message)
            if error_message == "Your Apple\xa0ID or password was incorrect.":
                print("Successfully displayed Error message for wrong password")
                return
            else:
                print("Error message not displayed for wrong password.")
                raise Exception("Error message not displayed for wrong password.")
        "Enter OTP manually"
        sleep(60)
        try:
            self.poco(text="Trust").wait_for_appearance(timeout=40)
            self.poco(text="Trust").click()
        except:
            pass
        try:
            self.poco(text="Continue").wait_for_appearance(timeout=20)
            self.poco(text="Continue").click()
        except:
            pass

    def clickSubmit(self):
        try:
            self.poco("Submit").click()
        except:
            self.poco(text="Submit").click()
