#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
from ...Common_Method import *
from ...PageObject.Social_Login.Social_Login import Social_Login
from ...sphere_db import *

import os
from ...TestSuite.store import *



poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method=Common_Method(poco)
social_login = Social_Login(poco)

def test_Others_TestcaseID_47948():
    pass
    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Sign In")

    """Has bug id SMBM 604, 1887"""
    """login"""

    common_method.show_message("connect a printer if already there ignore")
    common_method.show_message("keep the app and printer idle for overnight")
    login_page.click_loginBtn()
    others.wait_for_element_appearance("Continue with Google",10)
    login_page.click_Loginwith_Google()
    others.wait_for_element_appearance_text("zebra850.swdvt@gmail.com",10)
    social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
    others.wait_for_element_appearance("Open navigation menu",20)

    """print a test printer"""


    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.scroll_down()
    others.click_test_print()

    """Leave Phone and printer idle for whole night"""
    login_page.click_Menu_HamburgerICN()
    others.click_home_button()

    """check the status of printer"""
    res = others.check_printer_online_status()
    if res == "Offline":
        print("ok")


def setup_logout():
    common_method.tearDown()

    try:
        others.wait_for_element_appearance("Sign In", 10)
    except:
        pass

    try:
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
    except:
        pass
    sleep(2)

def test_Others_TestcaseID_45800():
    pass

    common_method.show_message("Provide existing user email and password which is registered")
    """has bug: SMBM-1098,SMBM-2234"""
    common_method.tearDown()
    setup_logout()
    login_page.click_loginBtn()
    social_login.wait_for_element_appearance_text("Continue with Google", 10)
    social_login.click_on_sign_in_with_email()

    """Provide new_user name and password which is registered"""
    email = common_method.get_user_input("Enter email")
    password=common_method.get_user_input("enter current password")
    password = "Zebra#85185180"
    social_login.complete_sign_in_with_email(email, password)

    others.wait_for_element_appearance("Home", 30)
    sleep(1)
    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()

    first_name = "zebra"
    others.edit_first_name(first_name)
    try:
        common_method.wait_for_element_appearance_namematches("have been saved", 5)
    except:
        pass

    last_name = "t"
    others.edit_last_name(last_name)
    try:
        common_method.wait_for_element_appearance_namematches("have been saved", 5)
    except:
        pass

    current_first_name = others.get_first_name()
    current_last_name = others.get_last_name()

    if first_name == current_first_name and last_name == current_last_name:
        print("ok")
    else:
        raise Exception("dint update")

    others.scroll_down()
    others.change_password_for_user_account()
    common_method.wait_for_element_appearance_textmatches("Please enter your username")
    others.enter_user_name_for_change_password("zebratest851@gmail.com")
    sleep(2)
    others.click_on_submit()

    common_method.wait_for_element_appearance_textmatches("Change Password")
    newpass= common_method.get_user_input("enter new password different from old password")
    others.change_old_password_to_new_password(password, newpass)
    others.click_on_submit()

    try:
        common_method.wait_for_element_appearance_textmatches("Password changed successfully")
    except:
        raise Exception("confirmation did not receive")

    others.click_here_to_login_after_changing_password()

    others.wait_for_element_appearance("Sign In", 5)
























