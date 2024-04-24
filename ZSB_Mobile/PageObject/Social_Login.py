from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
# from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import device as current_device
import os
# from ZSB_Mobile.PageObject.Login_Screen import Login_Screen_Android


def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates", a)


class Social_Login:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.google_login = "Continue with Google"
        self.apple_login = "Continue with Apple"
        self.facebook_login = "Continue with Facebook"
        self.sign_in_with_email = "Sign In with your email"
        self.submit_button_text = "SUBMIT"
        self.log_out_button = "Log Out"

    def check_login_with_google(self):
        temp = self.poco(text=self.google_login).exists()
        return temp

    def check_login_with_apple(self):
        temp = self.poco(text=self.apple_login).exists()
        return temp

    def check_login_with_facebook(self):
        temp = self.poco(text=self.facebook_login).exists()
        return temp

    def click_login_with_facebook(self):
        self.poco(text=self.facebook_login).click()

    def click_login_with_apple(self):
        self.poco(text=self.apple_login).click()

    def check_sign_in_with_email(self):
        temp = self.poco(text=self.sign_in_with_email).exists()
        return temp

    def check_zebra_logo(self):
        a = self.poco(type="android.widget.Image", text="Zebra Logo").exists()
        return a

    def check_text_of_free_benifits(self):
        a = self.poco(text="Learn more about the ").exists()
        b = self.poco(text="Benefits of a Free ZSB Account").exists()
        c = self.poco("Benefits of a Free ZSB Account", touchable=True).exists()

        return (a and b and c)

    def click_on_benefits_of_zebra_account(self):
        self.poco("Benefits of a Free ZSB Account").click()

    def scroll_down(self, count):

        for i in range(count):
            self.poco.scroll()

    def check_the_cookie_text(self):
        a = actual_value = self.poco("android.widget.TextView")[5].get_text()

        print(actual_value)

        assert_equal(a,
                     "This site uses cookies to manage user authentication, analytics, and to provide an improved digital experience. You can learn more about the cookies we use as well as how you can change your cookie settings by clicking here. By continuing to use this site without changing your settings, you are agreeing to our use of cookies. Review Zebra's Privacy Statement to learn more.",
                     "ok.")

    def check_options_under_cookie_text(self):
        a = self.poco("Zebra.com").exists()
        b = self.poco("Legal Notice").exists()
        c = self.poco("Privacyself. Statement").exists()

        return a and b and c

    def check_the_text_of_benefits_of_free_account_page(self):
        a = self.poco(text="Create, design and print labels from your PC or Mac.").exists()

        b = self.poco(
            text="Design custom labels from scratch and print using the ZSB Label Designer on your PC or Mac").exists()

        c = self.poco(text="Create a free Zebra account and register your printer for access to :").exists()

        self.poco.scroll()

        d = self.poco(text="Create and design labels in your own web-based custom workspace.").exists()

        e = self.poco(
            text="Thousands of pre-made design templates with high quality artwork perfect for home or business use.").exists()

        f = self.poco(text="Automatic software updates with the latest features and bug fixes.").exists()

        g = self.poco(text="And much more !").exists()

        return a and b and c and d and e and f and g

    def check_the_back_button(self):
        a = self.poco(text="back").exists()
        return a

    def click_on_the_back_button(self):
        self.poco(text="back").click()

    def scroll_up(self, count):
        start_point = [0.5, 0.2]
        end_point = [0.5, 0.8]

        # Perform the scroll-up action

        for i in range(count):
            self.poco.swipe(start_point, end_point, duration=0.1)

    def swipe_down_half(self, count):
        start_point = [0.5, 0.6]
        end_point = [0.5, 0.3]
        for i in range(count):
            self.poco.swipe(start_point, end_point, duration=0.1)

    def check_both_images_in_benefits_of_free_account_page(self):

        image_1 = Template(os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                                        "tpl1706352005910.png"), record_pos=(-0.281, -0.23), resolution=(1080, 2340))

        image_2 = Template(os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                                        "tpl1706352031764.png"), record_pos=(-0.281, 0.43), resolution=(1080, 2340))

        assert_exists(image_1)
        self.poco.scroll()
        assert_exists(image_2)

    def click_on_zebra_link(self):
        self.poco("Zebra.com").click()

    def click_on_legal_notice_link(self):
        self.poco("Legal Notice").click()

    def click_on_privacy_statement_link(self):
        self.poco("Privacy Statement").click()

    def complete_sign_in_with_email(self, user_name, password, click_on_sign_in=1, click_back=1):

        if click_back:
            keyevent("back")
        self.poco("android.widget.EditText")[0].set_text(user_name)

        self.poco("android.widget.EditText")[1].set_text(password)

        # self.poco(text="Sign In").click()
        if click_on_sign_in:
            self.poco("android.widget.Button")[1].click()

    def click_on_submit_button(self):
        self.poco(self.submit_button_text).click()

    def click_on_reset_password(self):
        self.poco(" Reset Password").focus([0.2, 0.3]).click()

    def check_for_password_change_page(self):
        self.poco(text="Password Recovery").exists()

    def enter_user_name_to_change_password(self):
        # self.poco("android.widget.EditText").click()

        self.poco("android.widget.EditText").set_text("zebra850@gmail.com")

    def open_change_password_page(self):
        self.poco("Click here ").click()

    def enter_the_new_password_with_temporary_password(self, temp, new_pass):
        self.poco("android.widget.EditText")[0].set_text(temp)

        self.poco("android.widget.EditText")[1].set_text(new_pass)

        self.poco("android.widget.EditText")[2].set_text(new_pass)

    def check_password_changed_successfully(self):
        self.poco(text="Password changed successfully.").click()

    def return_to_login_page(self):
        self.poco("RETURN TO LOGIN").click()

    def click_on_sign_in_with_email(self):
        self.poco(text=self.sign_in_with_email).click()

    def wait_for_element_appearance(self, element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance_text(self, element, time_out):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance_text_wild_string(self, element, time_out):
        self.poco(textMatches=".*"+element+".*").wait_for_appearance(timeout=time_out)


    def check_username_and_password_feilds(self):
        a = self.poco(text="Username*").exists()
        b = self.poco(text="Password*").exists()
        return a & b

    def check_sign_in_button(self):
        c = self.poco(text="Sign In", enabled=True).exists()
        return c

    def check_close_button(self):
        a = self.poco(text="Close", enabled=True).exists()
        return a

    def check_text_of_register_your_email(self):
        e = self.poco(text="Don't have an account? ").exists()
        # e = self.poco(text="Don't have an account? ").exists()
        f = self.poco(" Register Your Email Now").exists()

        return f

    def check_reset_password_text(self):
        # g = self.poco(text="Forgot your password? ").exists()
        g = self.poco(text="Learn more about the ").click()
        h = self.poco(" Reset Password").exists()

        return h

    def click_on_close_button(self):
        self.poco(text="Close", enabled=True).click()

    def click_register_your_email(self):
        self.poco(" Register Your Email Now").focus([0.1, 0.3]).click()

    def check_registration_of_email(self):
        return self.poco(text="ZSB Printer Account Registration").exists()

    def enter_user_email_for_registering(self, email):
        self.poco("android.widget.EditText").set_text(email)

    def click_on_next(self):
        self.poco(text="Next").click()

    def enter_the_verification_code(self, code):
        self.poco("android.widget.EditText").set_text(code)

    def enter_the_fields(self, firstname, lastname, password):
        temp2 = self.poco("android.widget.EditText")[0]
        temp1 = self.poco(text="signup.zebra.com")
        temp2.drag_to(temp1)
        sleep(3)

        self.poco("android.widget.EditText")[0].set_text(firstname)

        self.poco("android.widget.EditText")[1].set_text(lastname)

        self.poco("android.widget.EditText")[2].set_text(password)

        self.poco("android.widget.EditText")[3].set_text(password)

        self.poco(text="-- Select --").click()

    def select_the_country(self, country):
        scroll_view = self.poco("android.widget.ListView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 26
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.scroll()

            # Check if the "Accept" element is present and enabled
            search = self.poco(text=country)
            if search.exists():
                self.poco(text=country).click()
                # Accept button is visible and enabled, break out of the loop
                break

    def select_the_check_boxes(self):

        self.poco("android.widget.CheckBox")[0].click()

        self.poco("android.widget.CheckBox")[1].click()

    def click_submit_and_continue(self):
        start_point = [0.5, 0.7]
        end_point = [0.5, 0.4]
        for i in range(1):
            self.poco.swipe(start_point, end_point, duration=0.1)
        self.poco(text="SUBMIT AND CONTINUE").click()

    def check_sign_up_successful(self):
        self.poco(text="ZSB Printer registration completed.").click()

    def click_on_continue(self):
        try:
            self.poco("CONTINUE").click()
        except:
            self.poco(text="Continue").click()

    def accept_EULA_agreement(self):
        while self.poco(name="Accept", enabled=False):
            start_point = [0.5, 0.8]
            end_point = [0.5, 0.1]
            self.poco.swipe(start_point, end_point, duration=0.1)

        sleep(2)

        self.poco(name="Accept", enabled=True).click()

    def check_EULA(self):
        a = self.poco("End User\n License Agreement").exists()
        return a

    def click_on_profile_edit(self):

        self.poco("android.widget.Button").click()

    def click_log_out_button(self):
        log_out_btn = self.poco(self.log_out_button)
        log_out_btn.click()

    def validate_the_details_of_account(self, v_f, v_l, v_e):
        first_name = \
        self.poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View")[1].child(
            "android.view.View").child()[0].child("android.widget.EditText")[0].get_text()

        last_name = self.poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View")[1].child(
            "android.view.View").child()[0].child("android.widget.EditText")[1].get_text()

        email = self.poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View")[1].child(
            "android.view.View").child()[0].child("android.view.View")[0].get_text()

        res = (first_name == v_f) and (last_name == v_l) and (email == v_e)

        return res

    def check_focused_of_user_name(self):

        a = self.poco("android.widget.EditText", focused=True).exists()
        return a

    def check_key_board(self):
        a = self.poco(nameMatches=".*keyboard.*").exists()
        return a

    def choose_a_google_account(self, gmail):
        a = self.poco(text=gmail).click()

    def check_the_email_in_profile_page(self, loged_in_mail):
        email = self.poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View")[1].child(
            "android.view.View").child()[0].child("android.view.View")[0].get_text()

        return email == loged_in_mail

    def verify_choose_an_account_text(self):
        a = self.poco(text="Choose an account").exists()
        return a

    def open_in_chrome(self):
        self.poco("com.android.chrome:id/menu_button").click()
        self.poco(text="Open in Chrome browser").click()

    def verify_the_url(self, url):
        a = self.poco(textMatches=".*" + url + ".*").exists()
        return a

    def go_back(self):
        keyevent("back")

    def swith_back_the_app(self):
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)
        keyevent("KEYCODE_APP_SWITCH")

    def get_the_password(self):
        a = self.poco("android.widget.EditText")[1].get_text()
        return a

    def show_the_password(self):
        self.poco(text="eyehide").click()

    def check_for_blank_value_error_of_both(self):
        a = self.poco(text="Please fill out username field.").exists()

        b = self.poco(text="Please fill out password field.").exists()

        return a and b

    def check_for_blank_value_error_of_password(self):
        a = self.poco(text="Please fill out password field.").exists()
        return a

    def check_for_incorrect_user_name_or_password_sign_in_with_email(self):

        a = self.poco(text="We didn't recognize the username or password you entered. Please try again.").exists()
        return a

    def enter_user_name_in_google(self, user_name):
        a = "zsb@gmail.com"
        self.poco("identifierId").set_text(user_name)

    def sign_in_with_google(self):
        self.poco(text="Use another account").click()
        self.poco(text="Add account to device").click()

    def check_for_incorrect_username_in_google(self):
        a = self.poco(text="Couldn’t find your Google Account").exists
        return a

    def click_on_next_in_google_sing_in(self):
        self.poco(text="Next").click()

    def click_on_both_check_boxes_in_google_first_time_login(self):
        try:
            temp = Template(Basic_path("tpl1706871993959.png"))
            touch(temp)
            touch(temp)
        except:
            self.poco("android.view.View")[5].focus([0.05, 0.4]).click()

            self.poco("android.view.View")[5].focus([0.05, 0.3]).click()

    def click_on_submit_in_facebook(self):
        self.poco(text="Submit").click()

    def enter_username_and_password_in_facebook(self, user_name, password):
        self.poco("android.widget.EditText")[0].set_text(user_name)
        self.poco("android.widget.EditText")[1].set_text(password)

    def enter_apple_id_and_password(self, apple_id, password):

        self.poco("android.widget.EditText")[0].set_text(apple_id)
        self.poco(text="Continue").click()

        self.poco("android.widget.EditText")[1].set_text(password)

        self.poco(text="Sign In").click()

    def check_for_incorrect_error_in_apple(self):

        self.poco(text="Your Apple\xa0ID or password was incorrect.").exists()

    def continue_in_facebook(self):
        self.poco(textMatches=".*Continue.*").click()

    def click_an_element_by_text(self,a):
        self.poco(text=a).click()















































