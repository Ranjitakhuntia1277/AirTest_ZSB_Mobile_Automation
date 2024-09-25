# from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others
from ...Common_Method import *
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Social_Login.Social_Login import Social_Login
# from ZSB_Mobile.sphere_db import *
import pytest
import os
from ...TestSuite.store import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method = Common_Method(poco)
social_login = Social_Login(poco)
registration_page = Registration_Screen(poco)
aps_notification = APS_Notification(poco)

#semi-auto
def test_Others_TestcaseID_45793():
    """Notifications some times will not sync properly"""
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()

    start_app("com.google.android.googlequicksearchbox")

    others.click_google_search_bar()
    others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
    others.click_enter()
    try:
        others.wait_for_element_appearance("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.click_an_google_account("zebra21.dvt@gmail.com")
    except:
        pass

    others.wait_for_element_appearance_text("Home", 30)
    sleep(3)
    others.check_google_home_pop_up()

    others.click_hamburger_button_in_Google()
    sleep(2)
    others.click_Printer_Settings_in_google()

    others.click_hamburger_button_in_Google()

    """Pass the printer name"""

    others.select_first_printer_in_google()
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
    try:
        others.wait_for_element_appearance("Home", 15)
        sleep(2)
    except:
        """*** - Ask tarun if we should login and if this test case is semi automated."""

    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification = others.get_notification_text_in_Android()
    sleep(3)
    print("notification", Android_notification, google_notification)

    res = others.verify_notifications(google_notification, Android_notification)
    if not res:
        raise Exception("Notfications not matching")
    print(res)

    """This step need to be manually executed:
    5. Idle mobile app 30 to 1 h, back to the app, trigger some printer notification (cover open/close/media out)
    Check the notification pops up correctly"""


def test_Others_TestcaseID_45794():
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

    login_page.click_Loginwith_Google()
    common_method.wait_for_element_appearance_textmatches("Choose an account")

    """Enter the email"""
    email = "zebra850.swdvt@gmail.com"
    password = "Zebra#123456789"
    social_login.choose_a_google_account(email)
    social_login.wait_for_element_appearance("Home", 30)
    sleep(2)

    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    others.select_first_printer()
    others.click_test_print()
    others.wait_for_appearance_all("Print complete")
    sleep(2)
    others.click_test_print()
    others.wait_for_appearance_all("Print complete")
    sleep(2)

    """Generate less than 5 notifications"""
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification_before = others.get_notifications_in_first_page_android()
    sleep(3)

    others.click_down_arrow_button()
    others.click_dismiss_printer_notification()

    Android_notification_after = others.get_notifications_in_first_page_android()

    if len(Android_notification_before) > len(Android_notification_after):
        print("Success")
    else:
        raise Exception(" Notification dint dismiss ")


def test_Others_TestcaseID_45796():
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")

    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()

    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")

    res = others.check_remove_image_button_exists()
    if res:
        raise Exception("Remove image button found")

    others.click_upload_photo()
    others.select_photo_gallery()

    others.select_first_image_from_gallery()
    sleep(3)
    res = others.verify_default_image()
    if res:
        raise Exception("default image found")

    res = others.check_remove_image_button_exists()
    if not res:
        raise Exception("Remove image button not found")

    others.click_remove_image_button()
    sleep(2)
    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")


def test_Others_TestcaseID_45797():
    pass

    common_method.tearDown()
    common_method.wait_for_element_appearance_namematches("Home")
    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()
    others.scroll_down()
    others.click_log_out_button()

    try:
        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")

        """enter email here"""
        email = "zebra850.swdvt@gmail.com"
        others.choose_google_account(email)
    except:
        pass
    others.wait_for_element_appearance("Home", 30)

    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()

    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")

    res = others.check_remove_image_button_exists()
    if res:
        raise Exception("Remove image button found")

    others.click_upload_photo()
    others.select_camera()
    try:
        res = others.verify_text_camera_permission()
        if res:
            print("ok")
        else:
            pass
        others.click_allow()
    except:
        try:
            others.click_allow()
        except:
            pass
    sleep(1)
    others.capture_the_image_button()
    others.retake_the_image_button()
    others.capture_the_image_button()
    others.use_the_image_button()

    sleep(3)
    res = others.verify_default_image()
    if res:
        raise Exception("default image found")

    res = others.check_remove_image_button_exists()
    if not res:
        raise Exception("Remove image button not found")

    others.click_remove_image_button()
    sleep(2)
    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")


def test_Others_TestcaseID_45798():
    pass

    """has bug id:SMBM-2711"""

    common_method.tearDown()
    try:
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
    except:
        pass

    others.wait_for_element_appearance("Sign In", 10)
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()

    """enter email here"""
    email = "zebra850.swdvt@gmail.com"
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    others.choose_google_account(email)

    others.wait_for_element_appearance("Home", 30)

    login_page.click_Menu_HamburgerICN()
    """Click on the profile edit"""
    others.click_on_profile_edit()

    """verify the default image"""
    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")

    """select upload photo gallery"""
    others.click_upload_photo()

    """select photo gallery"""
    others.select_photo_gallery()

    others.go_back()
    sleep(1)
    others.go_back()
    sleep(2)

    """verify the default image"""
    res = others.verify_default_image()
    if not res:
        raise Exception("default image not found")

    """Select Camera upload"""
    others.click_upload_photo()
    others.select_camera()
    try:
        others.dont_allow_permission()
    except:
        pass
    try:
        others.click_upload_photo()
    except:
        pass
    try:
        others.select_camera()
    except:
        raise Exception("dint redirect to the previous page or dint ask for the permission")
    try:
        others.click_allow()
    except:
        pass
    others.go_back()

    """verify the default image"""
    try:
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")
    except:
        others.go_back()
        res = others.verify_default_image()
        if not res:
            raise Exception("default image not found")


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


def test_Others_TestcaseID_45795():
    pass

    common_method.tearDown()

    others.wait_for_element_appearance("Home", 10)

    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification = others.get_notifications_in_first_page_android()
    sleep(3)

    common_method.tearDown()

    others.wait_for_element_appearance("Home", 10)

    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification_after_closing_app = others.get_notifications_in_first_page_android()

    res = others.check_two_arrays_same(Android_notification, Android_notification_after_closing_app)

    if not res:
        raise Exception("Notifications did match appear after reopening the app")

    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()
    others.scroll_down()
    others.click_log_out_button()
    others.wait_for_element_appearance("Sign In", 10)
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()

    """enter email here"""
    email = "zsbswdvt@gmail.com"
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    others.choose_google_account(email)

    others.wait_for_element_appearance("Home", 20)
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification_after_logout = others.get_notifications_in_first_page_android()

    res = others.check_two_arrays_same(Android_notification, Android_notification_after_logout)
    if not res:
        raise Exception("Notifications are not same after log out")

    # others.uninstall_and_install_zsb_series_on_google_play()
    # others.open_the_zsb_series_app_in_play_store()
    common_method.Clear_App()
    common_method.Start_The_App()
    others.wait_for_element_appearance("Sign In", 10)
    others.check_allow_permission_for_location()
    registration_page.clickSignIn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()

    """pass email here"""
    email = "zsbswdvt@gmail.com"
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    others.choose_google_account(email)

    others.wait_for_element_appearance("Home", 20)

    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()

    Android_notification_after_deleting_app = others.get_notifications_in_first_page_android()

    res = others.check_two_arrays_same(Android_notification, Android_notification_after_deleting_app)
    if res:
        raise Exception("Notifications did not disappear after deleting the app")


