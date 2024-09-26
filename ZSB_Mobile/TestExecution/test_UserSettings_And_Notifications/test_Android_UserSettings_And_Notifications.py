# from poco import poco
import time
import self
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco import poco
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
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
app_settings_page = App_Settings_Screen(poco)

def test_Notifications_TestcaseID_45794():
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
    login_page.Loginwith_Added_Email_Id()
    social_login.wait_for_element_appearance("Home", 30)
    sleep(2)

    login_page.click_Menu_HamburgerICN()
    others.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    others.click_Testprint()
    app_settings_page.Verify_Printed_Successfully_Text()
    sleep(2)
    others.click_Testprint()
    app_settings_page.Verify_Printed_Successfully_Text()
    sleep(2)

    """Generate less than 5 notifications"""
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()
    sleep(3)
    others.click_down_arrow_button()
    others.click_dismiss_printer_notification()



def test_UserSettings_TestcaseID_45796():
    pass

    common_method.Stop_The_App()
    common_method.Start_The_App()
    app_settings_page.Home_text_is_present_on_homepage()
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


def test_UserSettings_TestcaseID_45797():
    pass

    common_method.tearDown()
    app_settings_page.Home_text_is_present_on_homepage()
    login_page.click_Menu_HamburgerICN()
    others.click_on_profile_edit()
    others.scroll_down()
    others.click_log_out_button()
    others.wait_for_element_appearance("Sign In", 10)
    login_page.click_loginBtn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
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


def test_UserSettings_TestcaseID_45798():
    pass

    """has bug id:SMBM-2711"""

    common_method.tearDown()
    try:
        app_settings_page.Home_text_is_present_on_homepage()
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
    login_page.Loginwith_Added_Email_Id()

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
    others.go_back()
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


def test_Notifications_TestcaseID_45795():
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
    login_page.Loginwith_Added_Email_Id()
    others.wait_for_element_appearance("Home", 30)
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()
    Android_notification_after_logout = others.get_notifications_in_first_page_android()

    res = others.check_two_arrays_same(Android_notification, Android_notification_after_logout)
    if not res:
        raise Exception("Notifications are not same after log out")

    #####others.uninstall_and_install_zsb_series_on_google_play()
    ##### others.open_the_zsb_series_app_in_play_store()
    common_method.Clear_App()
    common_method.Start_The_App()
    others.wait_for_element_appearance("Sign In", 10)
    others.check_allow_permission_for_location()
    registration_page.clickSignIn()
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    others.wait_for_element_appearance("Home", 30)
    login_page.click_Menu_HamburgerICN()
    others.click_notifications_button()
    Android_notification_after_deleting_app = others.get_notifications_in_first_page_android()

    res = others.check_two_arrays_same(Android_notification, Android_notification_after_deleting_app)
    if res:
        raise Exception("Notifications did not disappear after deleting the app")
# ##-------------------------------------------------------------------------------------

def test_Notifications_TestcaseID_53234():
    pass

    """"start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Notifications Tab"""
    app_settings_page.click_Notifications_Tab()
    """"Scroll till Notification Settings Tab"""
    app_settings_page.Scroll_Till_Notification_Settings_Tab()
    """click on notification settings tab"""
    app_settings_page.click_Notification_Settings_Tab()
    """"verify notification settings toggle buttons and text"""
    app_settings_page.Verify_NotificationSettings_Toggle_Buttons_Text_Present()
    """"scroll till messages tab"""
    app_settings_page.Scroll_Till_Messages_Tab()
    """""click Messages tab"""
    app_settings_page.click_Mesages_Tab()
    """verify messages text and toggle button"""
    app_settings_page.Verify_Messages_Text_And_Toggle_Buttons()
    """"click on hamburger icon"""
    app_settings_page.Disable_And_Enable_Toggle_Buttons()


def test_Others_TestcaseID_53232():
    pass
    """"start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Notifications Tab"""
    app_settings_page.click_Notifications_Tab()
    app_settings_page.Verify_Generated_Notification()
    app_settings_page.Expand_And_Verify_Printername_AndType()


def test_UserSettings_TestcaseID_45800():
    pass

    common_method.tearDown()
    common_method.Clear_App()
    login_page.click_loginBtn()
    login_page.Verify_ALL_Allow_Popups()
    login_page.signInWithEmail()
    login_page.click_Login_With_Email_Tab()
    login_page.click_Password_TextField()
    login_page.Enter_Zebra_Password()
    login_page.click_SignIn_Button()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.click_First_Name_Text_Field()
    """"clear first name field"""
    sleep(3)
    app_settings_page.clear_First_Name()
    """""Update first name with valid names"""
    app_settings_page.Update_Default_First_Name()
    sleep(3)
    poco.scroll()
    """""click last name text field"""
    app_settings_page.click_Last_Name_Text_Field()
    """"clear Last name field"""
    app_settings_page.clear_Last_Name()
    """""Update last name with valid names"""
    app_settings_page.Update_Default_Last_Name()
    sleep(3)
    """""click keyboard back icon"""
    app_settings_page.click_Keyboard_back_Icon()
    """"verify the updated names message"""
    app_settings_page.verify_Your_changes_have_been_saved_Message()
    sleep(3)
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Change_Password_Btn()
    app_settings_page.Verify_Password_Recovery_Text_Is_Displaying()
    app_settings_page.click_Close_Icon_On_Password_Recovery_Page()
    app_settings_page.Enter_Password()

# #####----------------------------------------------------------------------------------------------






