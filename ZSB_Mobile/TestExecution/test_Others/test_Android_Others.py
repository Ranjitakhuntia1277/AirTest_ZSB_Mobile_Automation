#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others.Others import Others
from ZSB_Mobile.Common_Method import *
from ZSB_Mobile.PageObject.Social_Login.Social_Login import Social_Login
from ZSB_Mobile.sphere_db import *

import os



poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method=Common_Method(poco)
social_login = Social_Login(poco)

class test_Others():
    pass
    def test_Others_TestcaseID_45793(self):

        """Notifications some times will not sync properly"""
        start_app("com.google.android.googlequicksearchbox")

        others.click_google_search_bar()
        others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
        others.click_enter()
        try:
            others.wait_for_element_appearance("Continue with Google",10)
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            others.click_an_google_account("zsbswdvt@gmail.com")
        except:
            pass

        others.wait_for_element_appearance_text("Home",30)
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

        others.wait_for_element_appearance_text("Home",10)
        others.click_hamburger_button_in_Google()

        others.wait_for_element_appearance("Notifications",5)

        others.click_notifications_button_in_google()
        others.click_hamburger_button_in_Google()
        res = others.check_text_history()
        if not res:
            others.scroll_up(1)
        """Clear The Notifications in google if present"""
        google_notification = others.get_notification_text_in_google()

        print(google_notification)
        sleep(2)

        start_app("com.zebra.soho_app")

        others.wait_for_element_appearance("Home",15)
        sleep(2)

        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification = others.get_notification_text_in_Android()
        sleep(3)
        print("notification",Android_notification,google_notification)

        res = others.verify_notifications(google_notification,Android_notification)
        if not res:
            raise Exception("Notfications not matching")
        print(res)

        """This step need to be manually executed:
        5. Idle mobile app 30 to 1 h, back to the app, trigger some printer notification (cover open/close/media out)
        Check the notification pops up correctly"""

    def test_Others_TestcaseID_45794(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        common_method.wait_for_element_appearance_namematches("Home")

        """Generate less than 5 notifications"""
        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification_before = others.get_notifications_in_first_page_android()
        sleep(3)

        others.click_down_arrow_button()
        others.click_dismiss_printer_notification()

        Android_notification_after = others.get_notifications_in_first_page_android()

        if len(Android_notification_before)>len(Android_notification_after):
            print("Success")
        else:
            raise Exception(" Notification dint dismiss ")

    def test_Others_TestcaseID_45796(self):
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

    def test_Others_TestcaseID_45797(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()

        try:
            others.wait_for_element_appearance("Sign In",10)
            login_page.click_loginBtn()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            """enter email here"""
            email = "zebratest850@gmail.com"
            others.choose_google_account(email)
        except:
            pass
        others.wait_for_element_appearance("Home",30)

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

    def test_Others_TestcaseID_45798(self):
        pass

        """has bug id:SMBM-2711"""

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            others.click_on_profile_edit()
            others.scroll_down()
            others.click_log_out_button()
        except:
            pass

        others.wait_for_element_appearance("Sign In",10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """enter email here"""
        email = "zebratest850@gmail.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)

        others.wait_for_element_appearance("Home",30)

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

    def test_Others_TestcaseID_45800(self):
        pass

        """has bug: SMBM-1098,SMBM-2234"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google",10)
        social_login.click_on_sign_in_with_email()

        """Provide new_user name and password which is registered"""
        email = "zebratest851@gmail.com"
        password = "Zebra#8518518"
        social_login.complete_sign_in_with_email(email,password)

        others.wait_for_element_appearance("Home",30)
        sleep(1)
        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()

        first_name = "zebra"
        others.edit_first_name(first_name)
        try:
            common_method.wait_for_element_appearance_namematches("have been saved",5)
        except:
            pass

        last_name = "t"
        others.edit_last_name(last_name)
        try:
            common_method.wait_for_element_appearance_namematches("have been saved",5)
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
        others.change_old_password_to_new_password(password,"Zebra#85185180")
        others.click_on_submit()

        try:
            common_method.wait_for_element_appearance_textmatches("Password changed successfully")
        except:
            raise Exception("confirmation did not receive")

        others.click_here_to_login_after_changing_password()

        others.wait_for_element_appearance("Sign In",5)

    def test_Others_TestcaseID_45801(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Sign In")
            login_page.click_loginBtn()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            login_page.click_Loginwith_Google()
            """enter email here"""
            email = "zebratest850@gmail.com"
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            others.choose_google_account(email)
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass

        login_page.click_Menu_HamburgerICN()
        others.click_common_designs_button()
        others.search_designs("Address")
        sleep(4)
        others.select_first_design()
        sleep(4)

        others.search_designs("Asset")
        sleep(3)
        others.select_first_design()

        others.click_on_copy_to_my_designs()
        common_method.wait_for_element_appearance_namematches("successfully")
        sleep(2)
        others.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        others.click_on_my_designs()
        others.search_designs("Asset")
        sleep(3)
        others.select_first_design()

        others.click_print_button()
        sleep(4)

        others.click_enter_data_for_design()
        others.enter_data_for_design("123456789")
        others.check_error_print_preview()
        sleep(3)
        res = others.check_for_keyboard()
        if not res:
            raise Exception("Keyboard not found")

        others.go_back()
        others.click_enter_text_for_design()

        others.check_error_print_preview()

        others.enter_text_for_design("My text")
        others.check_error_print_preview()
        sleep(3)
        res = others.check_for_keyboard()
        if not res:
            raise Exception("Keyboard not found")
        others.go_back()
        others.click_print_button()

        """check the template print out with updated value successfully. need to be done manually """


    def test_Others_TestcaseID_47946(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass
        """take the previous number of cartridges"""
        previous = others.get_no_of_left_cartridge()

        """click on navigation option"""
        login_page.click_Menu_HamburgerICN()

        """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
        others.click_Printer_Settings()
        others.select_first_printer()
        sleep(2)
        n = 2

        """test the printer to print the label"""
        for i in range(n):
            others.click_test_print()
            others.wait_for_appearance_all("Print complete")
            sleep(2)
        sleep(5)
        """Go to the Home Page"""
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()
        sleep(2)

        """After printing Get the number of cartridges"""
        after = others.get_no_of_left_cartridge()

        """Check wheather the cartridges are updated"""
        res = others.check_auto_update_cartridge(previous,after,n)
        if not res:
            raise Exception("number of cartridge count not updated")

    def test_Others_TestcaseID_47955(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Open navigation menu")
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        names, id = others.get_printer_names()
        print(names,id)
        others.select_printer_1(id[1])
        others.rename_printer(id[1], names[2])
        sleep(1)
        keyevent("enter")
        res = others.verify_text_update_printer_name_fail()
        print(res)
        if not res:
            raise Exception("printer update failed not raised")

    def test_Others_TestcaseID_47972(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass

        login_page.click_Menu_HamburgerICN()

        sleep(1)

        """ Select the Printer Settings """
        others.click_Printer_Settings()

        others.swipe_left()
        """ Select a printer """
        others.select_first_printer()
        sleep(2)

        """ Click on the icon """
        others.click_icon()
        sleep(1)

        """Click On the Demo video"""
        others.click_demo_video()
        sleep(5)

        others.click_on_the_vedio_while_playing()

        """Close The Demo Video"""
        others.close_demo_video()

        """Check if closed"""
        if not others.check_demo_video_closed():
            raise Exception("demo video not closed")

    def test_Others_TestcaseID_49203(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass
        """Click On the Three dots of the Home page Printer"""
        others.click_three_dots()

        """Click on the Delete Button"""
        others.click_delete_button()

        """Verify the text image (Currently The text cannot be extracted so verifying using the name)"""
        try:
            others.verify_delete_printer_text()
        except:
            raise Exception("step 2-2 fails, which does not match the wordings")

        """Check cancel and delete button exists"""
        others.check_cancel_and_delete_button()

        """cancel the delete printer dialogue"""
        others.click_cancel_delete_printer()

    def test_Others_TestcaseID_51703(self):
        pass


        others.install_zsb_series_on_google_play()
        common_method.wait_for_element_appearance_namematches("Uninstall",50)
        others.open_the_zsb_series_app_in_play_store()
        others.check_allow_permission_for_location()
        login_page.click_loginBtn()
        try:
            others.click_on_allow()
        except:
            pass
        try:
            others.click_on_allow()
        except:
            pass
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            others.click_an_google_account("zebratest850@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home",30)
        res = others.check_home_page()
        if not res:
            raise Exception("Not in Home page")

        others.uninstall_and_install_zsb_series_on_google_play()
        common_method.wait_for_element_appearance_namematches("Uninstall",30)
        stop_app("com.android.vending")

        poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

        while(1):
            if others.check_zsb_app_icon():
                t='present'
                break
            else:
                others.scroll_down()

        others.click_zsb_app_icon()
        sleep(5)

        try:
            others.check_allow_permission_for_location()
        except:
            pass
        try:
            others.click_on_allow()
        except:
            pass

        try:
            login_page.click_loginBtn()
        except:
            pass
        try:
            others.click_on_allow()
        except:
            pass
        try:
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            others.click_an_google_account("zebratest850@gmail.com")
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Home",30)

        res = others.check_home_page()
        if not res:
            raise Exception("Not in Home page")


    def test_Others_TestcaseID_45795(self):
        pass

        start_app("com.zebra.soho_app")

        others.wait_for_element_appearance("Home",10)

        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification = others.get_notifications_in_first_page_android()
        sleep(3)

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        others.wait_for_element_appearance("Home",10)

        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification_after_closing_app = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification,Android_notification_after_closing_app)

        if not res:
            raise Exception("Notifications did match appear after reopening the app")

        login_page.click_Menu_HamburgerICN()
        others.click_on_profile_edit()
        others.scroll_down()
        others.click_log_out_button()
        others.wait_for_element_appearance("Sign In",10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """enter email here"""
        email = "zsbswdvt@gmail.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)

        others.wait_for_element_appearance("Home",20)
        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification_after_logout = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification,Android_notification_after_logout)
        if not res:
            raise Exception("Notifications are not same after log out")

        others.uninstall_and_install_zsb_series_on_google_play()
        others.open_the_zsb_series_app_in_play_store()
        others.wait_for_element_appearance("Sign In",10)
        others.check_allow_permission_for_location()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """pass email here"""
        email = "zsbswdvt@zebra.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)

        others.wait_for_element_appearance("Home",20)

        login_page.click_Menu_HamburgerICN()
        others.click_notifications_button()

        Android_notification_after_deleting_app = others.get_notifications_in_first_page_android()

        res = others.check_two_arrays_same(Android_notification,Android_notification_after_deleting_app)
        if res:
            raise Exception("Notifications did not disappear after deleting the app")

    def test_Others_TestcaseID_45802(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Sign In")

        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        others.click_on_sign_in_with_email()
        common_method.wait_for_element_appearance_textmatches("Sign In")

        email="zebratest851@gmail.com"
        password="Zebra#85185180"
        social_login.complete_sign_in_with_email(email,password,0)

        sleep_time = 60*29
        sleep(sleep_time)

        others.click_on_sign_in()
        common_method.wait_for_element_appearance_namematches("Home",30)

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        login_page.click_Menu_HamburgerICN()

    def test_Others_TestcaseID_45803(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        """Has bugs SMBM 1801 ,and 997"""
        res = others.check_printer_online_status()
        if res == "Online":
            print("ok")
        else:
            raise Exception("Printer is in offline or other state turn it on")

        login_page.click_Menu_HamburgerICN()

        """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
        others.click_Printer_Settings()

        """pass the printer name"""
        others.select_first_printer()
        sleep(2)

        others.click_test_print()
        login_page.click_Menu_HamburgerICN()

        others.click_home_button()

        res = others.check_printer_online_status()
        if res == "Paper out":
            print("ok")
        else:
            raise Exception("Paper out should be shown but not shown")

        login_page.click_Menu_HamburgerICN()

        """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
        others.click_Printer_Settings()

        """pass the printer name"""
        others.select_first_printer()
        sleep(2)

        others.click_test_print()

        login_page.click_Menu_HamburgerICN()

        others.click_home_button()

        res = others.check_printer_online_status()
        if res == "Online":
            print("ok")
        else:
            raise Exception("Printer is in offline state turn it on")



    def test_Others_TestcaseID_45872(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Sign In")

        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        others.click_on_sign_in_with_email()
        sleep(1)
        others.go_back()

        others.enter_user_name_in_sign_with_email("zebratest851@gmail.com")

        others.enter_password_in_sign_with_email("Zebra#85185180")

        sleep_time = 60*31
        sleep(sleep_time)

        others.click_on_sign_in()

        try:
            others.wait_for_element_appearance("Home",10)
            raise Exception("The page does not timeout")
        except ZeroDivisionError:
            pass

    def test_Others_TestcaseID_45799(self):
        pass

        start_app("com.android.documentsui")
        t=''
        others.install_the_zsb_apk_in_files_android_8()
        sleep(3)
        res = others.check_app_is_installed_on_android_8()
        if res:
            raise Exception("app is installed but it should not")

        others.go_back()
        others.go_back()

        poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

        while(1):
            if others.check_zsb_app_icon():
                t='present'
                break
            else:
                others.scroll_down()

        if t == 'present':
            raise Exception("app present")

