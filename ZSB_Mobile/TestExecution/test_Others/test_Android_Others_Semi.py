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


def test_Others_TestcaseID_45807(self):
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Recently")

    """SMBM-1774"""
    recently_printed_labels_before = others.get_recently_printed_labels()

    login_page.click_Menu_HamburgerICN()
    others.click_common_designs_button()
    sleep(2)
    netw_1_common_designs = others.get_designs_visible_designs()
    login_page.click_Menu_HamburgerICN()
    others.click_on_my_designs()
    common_method.wait_for_element_appearance_namematches("Showing")
    netw_1_my_designs = others.get_designs_visible_designs()
    login_page.click_Menu_HamburgerICN()
    others.click_on_my_data()
    sleep(2)
    netw_1_my_data = others.get_my_data_all()
    login_page.click_Menu_HamburgerICN()
    others.click_home_button()

    others.open_wifi_settings()
    sleep(3)
    others.select_wifi("POCO M3", "1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    login_page.click_Menu_HamburgerICN()
    others.click_home_button()
    sleep(2)
    res = others.check_home_page()
    if not res:
        raise Exception("home page not shown")
    recently_printed_labels_after = others.get_recently_printed_labels()

    res = others.check_same_after_switching_network(recently_printed_labels_before, recently_printed_labels_after)
    if not res:
        print("changing network not showing files properly")

    sleep(4)

    """For Common Design"""
    others.open_wifi_settings()
    others.select_wifi("ZGuest", "1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    login_page.click_Menu_HamburgerICN()
    others.click_common_designs_button()
    sleep(2)
    netw_2_common_designs = others.get_designs_visible_designs()

    res = others.check_same_after_switching_network(netw_1_common_designs, netw_2_common_designs)
    if not res:
        print("changing network not showing files properly")

    login_page.click_Menu_HamburgerICN()
    others.click_home_button()
    """For My Design"""
    others.open_wifi_settings()
    sleep(1)

    """Pass network 2 here"""
    others.select_wifi("POCO M3", "1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")

    common_method.wait_for_element_appearance_namematches("Home")
    login_page.click_Menu_HamburgerICN()
    others.click_on_my_designs()
    common_method.wait_for_element_appearance_namematches("Showing")
    netw_2_my_designs = others.get_designs_visible_designs()

    res = others.check_same_after_switching_network(netw_1_my_designs, netw_2_my_designs)
    if not res:
        print("changing network not showing files properly")

    """For my data"""

    login_page.click_Menu_HamburgerICN()
    others.click_home_button()

    others.open_wifi_settings()
    sleep(1)
    others.select_wifi("ZGuest", "1234567890")
    sleep(1)

    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_namematches("Home")
    login_page.click_Menu_HamburgerICN()
    others.click_on_my_data()
    sleep(2)
    netw_2_my_data = others.get_my_data_all()

    res = others.check_same_after_switching_network(netw_1_my_data, netw_2_my_data)
    if not res:
        print("changing network not showing files properly")

    def test_Others_TestcaseID_45874(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass

        expected_version_no = "1.4.5339"
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()

        """get the version number of the current device"""
        actual_version_no = others.get_the_version_no()

        """If version number not same generate error"""
        if expected_version_no != actual_version_no:
            raise Exception("Version no did not match")

    def test_Others_TestcaseID_46963(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()

        res = others.check_bluetooth_connection_required_diloge()

        if not res:
            raise Exception("bluetooth dialogue dint show")
        others.click_continue_in_bluetooth_connection_required()

        try:
            others.click_on_allow()
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Apply",20)
        others.scroll_down()
        others.click_add_network_button()
        common_method.wait_for_element_appearance_namematches("Network")
        sleep(5)

        """Pass the name of the netowrk here"""
        network2= "NESTWIFI"
        password="123456789"
        others.select_network_and_enter_password(network2,password)
        try:
            others.click_enter_network_manually()
            others.enter_network_name(network2)
            others.click_join_network()
        except:
            pass

        sleep(3)
        login_page.click_Menu_HamburgerICN()
        others.click_home_button()

        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()
        others.select_first_printer()
        others.click_wifi_button()
        others.click_manage_network_button()
        res = others.check_bluetooth_connection_required_diloge()
        if not res:
            raise Exception("dialogue dint show")
        others.click_continue_in_bluetooth_connection_required()
        common_method.wait_for_element_appearance_namematches("Apply")

        others.scroll_down()

        res,res1 = others.get_network_names()

        others.swap_two_networks(res1[1],res1[0])
        res = others.check_apply_changes_button_clickable()
        if not res:
            raise Exception("Apply changes button not clickable")
        others.click_apply_changes_button()
        sleep(5)
        res = others.check_apply_changes_button_clickable()
        if res:
            raise Exception("Apply changes button  clickable")
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(5)
        res,res1 = others.get_network_names()

        others.delete_one_network(res1[0])
        common_method.wait_for_element_appearance_namematches("Apply")

        sleep(2)

        try:
            common_method.wait_for_element_appearance_namematches(res1[0])
            raise Exception("network dint get deleted")
        except:
            pass
        sleep(1)

        login_page.click_Menu_HamburgerICN()

        others.click_home_button()

    def test_Others_TestcaseID_47945(self):
        pass

        """Has bug id: SMBM-2247"""
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        try:
            common_method.wait_for_element_appearance_namematches("Home")
        except:
            pass
        login_page.click_Menu_HamburgerICN()
        others.click_Printer_Settings()

        names, id = others.get_printer_names()
        others.select_printer_1(id[1])

        others.rename_printer(id[1],"")
        others.click_enter()

        res = others.get_null_name_error_and_space_for_printer_name()
        if res:
            print("ok")
        else:
            raise Exception("proper error msg not displayed for null value")

        others.rename_printer(id[1],"    ")
        others.click_enter()

        if res:
            print("ok")
        else:
            raise Exception("Space  accepted")

    def test_Others_TestcaseID_51704(self):
        pass

        cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5049.apk"'
        res = others.run_the_command(cmd)

        sleep(10)
        print(res)

        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_textmatches("location")
        others.check_allow_permission_for_location()
        try:
            others.click_on_allow()
        except:
            pass
        others.click_on_older_login()
        try:
            others.click_on_allow()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        try:
            others.click_an_google_account("zebratest850@gmail.com")
            common_method.wait_for_element_appearance_namematches("Home",20)
        except:
            pass
        try:
            others.check_continue_button_and_click_enter()
            others.check_continue_button_and_click_enter()
        except:
            pass
        res = others.check_home_page()

        if not res:
            raise Exception("Not in Home page")

        cmd ='adb uninstall com.zebra.soho_app'
        res = others.run_the_command(cmd)
        print(res)

        cmd = 'adb install "C:\\Users\\tr5927\Downloads\ZsbMobile-production-5132.apk"'
        res = others.run_the_command(cmd)
        print(res)
        sleep(15)
        poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

        while(1):
            if others.check_zsb_app_icon():
                t='present'
                break
            else:
                others.scroll_down()

        others.click_zsb_app_icon()
        sleep(5)

        others.check_allow_permission_for_location()
        try:
            others.click_on_allow()
        except:
            pass
        login_page.click_loginBtn()
        try:
            others.click_on_allow()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        try:
            others.click_an_google_account("zebratest850@gmail.com")
            common_method.wait_for_element_appearance_namematches("Home",20)
        except:
            pass

        try:
            others.check_continue_button_and_click_enter()
            others.check_continue_button_and_click_enter()
        except:
            pass

        res = others.check_home_page()

        if not res:
            raise Exception("Not in Home page")

    def test_Others_TestcaseID_45804(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Open navigation menu")
        """Has bugs SMBM 1801 ,and 997"""
        res = others.check_printer_online_status()
        if res == "Online":
            print("ok")
        else:
            raise Exception("Printer is not in Online state")

        others.select_first_label_from_home()
        others.click_print_button()
        sleep(3)
        others.check_error_print_preview()

        others.click_print_button()
        sleep(4)

        others.click_left_arrow()


        res = others.check_printer_online_status()
        if res == "Offline":
            print("ok")
        else:
            raise Exception("Printer is not in Offline state")

    def test_Others_TestcaseID_45805(self):
        pass
        """Has bugs SMBM 1801 ,and 997"""
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Open navigation menu")

        res = others.check_printer_online_status()
        if res == "Online":
            print("ok")
        else:
            raise Exception("Printer is not in Online state")

        others.select_first_label_from_home()
        others.click_print_button()
        sleep(3)
        others.check_error_print_preview()

        others.click_print_button()
        sleep(4)
        others.click_left_arrow()


        res = others.check_printer_online_status()
        if res == "Cover Open":
            print("ok")
        else:
            raise Exception("Printer is not in Cover Open state")


        others.select_first_label_from_home()
        others.click_print_button()
        sleep(3)
        others.check_error_print_preview()

        others.click_print_button()
        sleep(4)

        others.click_left_arrow()

    def test_Others_TestcaseID_47948(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Sign In")

        """Has bug id SMBM 604, 1887"""
        """login"""
        login_page.click_loginBtn()
        others.wait_for_element_appearance("Continue with Google",10)
        login_page.click_Loginwith_Google()
        others.wait_for_element_appearance_text("zebratest850@gmail.com",10)
        social_login.choose_a_google_account("zebratest850@gmail.com")
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
























