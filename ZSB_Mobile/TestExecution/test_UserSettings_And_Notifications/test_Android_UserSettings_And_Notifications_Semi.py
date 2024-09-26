#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
from ...Common_Method import *
from ...PageObject.Social_Login.Social_Login import Social_Login
# from ...sphere_db import *

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


def test_Others_TestcaseID_45793():
    """Notifications some times will not sync properly"""
    # common_method.Stop_The_App()
    # common_method.Clear_App()
    # clear_app("com.google.android.googlequicksearchbox")
    # start_app("com.google.android.googlequicksearchbox")
    # others.click_google_search_bar()
    # others.Open_ZSB_WebPortal()
    # login_page.Verify_ALL_Allow_Popups()
    # login_page.click_loginBtn()
    # try:
    #     others.wait_for_element_appearance("Continue with Google", 10)
    #     login_page.click_Loginwith_Google()
    #     common_method.wait_for_element_appearance_textmatches("Choose an account")
    #     others.click_an_google_account("zebra850.swdvt@gmail.com")
    # except:
    #     pass
    #
    # others.wait_for_element_appearance_text("Home", 30)
    # sleep(3)
    # others.check_google_home_pop_up()
    #
    # others.click_hamburger_button_in_Google()
    # sleep(2)
    # others.click_Printer_Settings_in_google()
    #
    # others.click_hamburger_button_in_Google()

    """Pass the printer name"""
    others.Select_Printer()
    common_method.wait_for_element_appearance_textmatches("Auto Label")

    """others.google_scroll_down()"""
    others.scroll_down_till_printer_test_label_in_google()
    sleep(1)
    n = 2
    for i in range(n):
        others.click_google_print_test_button()
        sleep(5)

    """others.change_Darkness_level_in_google(50)"""

    others.wait_for_element_appearance_text("Home", 10)
    others.click_hamburger_button_in_Google()

    others.wait_for_element_appearance("Notifications", 5)

    others.click_notifications_button_in_google()
    others.click_hamburger_button_in_Google()
    res = others.check_text_history()
    if not res:
        others.scroll_up(1)
    """Clear The Notifications in google if present"""
    google_notification = others.get_notification_text_in_google()

    print(google_notification)
    sleep(2)

    common_method.tearDown()
    others.wait_for_element_appearance("Home", 15)
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification = others.get_notification_text_in_Android()
    sleep(3)
    print("notification", Android_notification, google_notification)

    res = others.verify_notifications(google_notification, Android_notification)
    if not res:
        raise Exception("Notfications not matching")
    print(res)
    common_method.Show_popup_To_Trigger_Some_Printer_Notification_Manually()



def test_Others_TestcaseID_47948():
    pass
    common_method.tearDown()
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


























