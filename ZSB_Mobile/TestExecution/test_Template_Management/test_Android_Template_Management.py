# from poco import poco
import time
import pytest
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Others.Others import Others
from ZSB_Mobile.PageObject.Social_Login.Social_Login import Social_Login

import os


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)
template_management = Template_Management_Android(poco)
login_page = Login_Screen(poco)
common_method = Common_Method(poco)
others = Others(poco)
social_login = Social_Login(poco)


class test_Android_Template_Management:
    # pass
    def __init__(self):
        pass
    def test_Template_Management_TestcaseID_45902(self):
        pass
        # stop_app("com.zebra.soho_app")
        # start_app("com.zebra.soho_app")
        # try:
        #     common_method.wait_for_element_appearance_namematches("Home")
        #     login_page.click_Menu_HamburgerICN()
        #     others.click_on_profile_edit()
        #     others.scroll_down()
        #     others.click_log_out_button()
        # except:
        #     pass
        #
        # try:
        #     others.wait_for_element_appearance("Sign In",10)
        #     login_page.click_loginBtn()
        #     common_method.wait_for_element_appearance_namematches("Continue with Google")
        #     login_page.click_Loginwith_Google()
        #
        #     """enter email here"""
        #     email = "zebratest850@gmail.com"
        #     common_method.wait_for_element_appearance_textmatches("Choose an account")
        #     others.choose_google_account(email)
        # except:
        #     pass
        common_method.wait_for_element_appearance_namematches("Recently")

        total_designs = template_management.get_all_designs_in_recently_printed_labels()
        if len(total_designs)!=0:
            raise Exception("Label found in recently printed design even without printing")

    def test_Template_Management_TestcaseID_45903(self):
        pass
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

        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """enter email here"""
        email = "zebratest850@gmail.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        prev = template_management.get_first_design_in_my_designs()
        template_management.click_first_design_in_my_designs()
        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",10)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed properly")
        template_management.click_print_button_enabled()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")
        sleep(2)
        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(2)
        curr = template_management.get_first_design_in_recently_printed_labels()

        if prev != curr:
            raise Exception("the top of recently printed label is not as expected")

        curr_mon,curr_date,curr_year = template_management.get_current_date()
        des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
        if curr_mon != des_mon or curr_date != des_date or curr_year != des_year:
            raise Exception("dates not matching")

    def test_Template_Management_TestcaseID_45904(self):
        pass
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

        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """enter email here"""
        email = "zebratest850@gmail.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)
        common_method.wait_for_element_appearance_namematches("Showing")
        total_my_designs = template_management.get_all_designs_in_my_designs()
        design_7 = total_my_designs[6]

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()


        for i in total_my_designs[:6]:
            common_method.wait_for_element_appearance_namematches("Showing.")
            template_management.click_design_in_my_designs_by_full_name(i)
            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")
            template_management.click_print_button_enabled()
            try:
                common_method.wait_for_element_appearance_namematches("Print complete",10)
            except:
                raise Exception("print_toast_dint_pop up")
            common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(2)
            common_method.wait_for_element_appearance("Recently Printed Labels")
            curr = template_management.get_first_design_in_recently_printed_labels()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

    def test_Template_Management_TestcaseID_45905(self):
        pass
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

        others.wait_for_element_appearance("Sign In", 10)
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()

        """enter email here"""
        email = "zebratest850@gmail.com"
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)
        common_method.wait_for_element_appearance_namematches("Home",20)

        """Copy design from common design to my design"""

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Address"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        curr_design = template_management.get_first_design_in_my_designs()
        template_management.click_element_by_name_or_text(curr_design)
        curr_design = template_management.get_names_of_design_in_search_designs([curr_design])[0]

        template_management.get_the_full_name_of_design_and_click_in_my_design(curr_design,1)

        template_management.click_on_copy_to_my_designs()
        template_management.wait_for_element_appearance_name_matches_all("successfully copied")
        sleep(2)
        template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        template_management.search_designs(curr_design)

        common_method.wait_for_element_appearance_namematches("Showing",20)
        template_management.click_first_design_in_my_designs()
        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print",30)
        template_management.click_print_button_enabled()

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        common_method.wait_for_element_appearance("Recently Printed Labels")
        curr = template_management.get_first_design_in_recently_printed_labels()
        curr = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(curr_design,0)
        print(curr)
        curr_mon,curr_date,curr_year = template_management.get_current_date()
        des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
        if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
            raise Exception("dates not matching")

    def test_Template_Management_TestcaseID_45906(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance("Home",10)

        """Copy design from common design to my design"""

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        template_management.search_designs("Address")
        common_method.wait_for_element_appearance_namematches("Categories")
        template_management.select_first_design()

        template_management.wait_for_designs_in_comm_design()

        template_management.click_first_design_in_common_design()
        sleep(2)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",10)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed properly")
        template_management.click_print_button_enabled()

        """Will fail if the first design is not updated with the recently printed label"""

        common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
        template_management.click_left_arrow()
        common_method.wait_for_element_appearance_enabled("android.widget.Button",10)
        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        common_method.wait_for_element_appearance("Recently Printed Labels")
        curr = template_management.get_first_design_in_recently_printed_labels()

        curr_mon,curr_date,curr_year = template_management.get_current_date()
        des_mon,des_date,des_year = template_management.get_design_last_print_date(curr)
        if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
            raise Exception("dates not matching")

    def test_Template_Management_TestcaseID_45907(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        if not template_management.verify_element_exists_by_name("Recently Printed Labels"):
            raise Exception("no recently printed label text")

        """pass no of designs printed as parameter"""
        all_designs = template_management.get_all_designs_in_recently_printed_labels(6)

        names,sizes= template_management.get_names_and_sizes_in_recently_printed_labels(all_designs)

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        common_method.wait_for_element_appearance("Recently Printed Labels")

        curr = template_management.click_first_design_in_recently_printed_labels()
        a = template_management.verify_options_clickable_in_design()
        if not a:
            raise Exception("some options are not clickable")

        template_management.close_menu_of_design_in_home()

        template_management.check_the_dates_of_last_print_in_recent_print_labels(all_designs)

        template_management.click_and_close_menu_designs_in_home(all_designs)

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        common_method.wait_for_element_appearance("Recently Printed Labels")

    def test_Template_Management_TestcaseID_45908(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        prev = template_management.get_no_of_left_cartridge()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        total = template_management.get_all_designs_in_my_designs()
        template_management.click_on_design_which_is_not_printed_yet(total)

        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print",10)
        template_management.click_print_button_enabled()
        sleep(2)
        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        curr = template_management.get_no_of_left_cartridge()
        if prev!=curr:
            raise Exception("number of prints left is updated after printer being turned off")

        sleep(30)
        """Turn on the printer to be Online """
        common_method.swipe_by_positions([0.5,0.5], [0.5,1.0])

        after = template_management.get_no_of_left_cartridge()

        if after-1 != curr:
            raise Exception("number of prints left is not updated")

    def test_Template_Management_TestcaseID_45910(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        prev_designs = template_management.get_all_designs_in_recently_printed_labels()
        template_management.turn_off_wifi()

        template_management.refresh_the_home_page_till_you_see_error()
        template_management.check_the_error_msg_of_turning_off_wifi()
        template_management.click_on_continue()
        try:
            template_management.click_on_continue()
        except:
            pass
        try:
            template_management.click_on_continue()
        except:
            pass

        curr_designs = template_management.get_all_designs_in_recently_printed_labels()
        if len(curr_designs)>0:
            raise Exception("designs are displayed after turning off the wifi  ")

        template_management.turn_on_wifi()

        template_management.refresh_the_home_page_()

        common_method.wait_for_element_appearance("Recently Printed Labels")

        after_designs = template_management.get_all_designs_in_recently_printed_labels()

        if prev_designs!=after_designs:
            raise Exception("designs are not matching before and after turning on wifi")

    def test_Template_Management_TestcaseID_45909(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Print a design before staring this test case"""
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        t = template_management.get_first_design_in_my_designs()
        t = template_management.get_names_of_design_in_search_designs([t])[0]
        template_management.get_the_full_name_of_design_and_click_in_my_design(t)
        template_management.click_print_button()
        template_management.wait_for_element_appearance_name_matches_all("Label")
        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button_enabled()

        start_app("com.google.android.googlequicksearchbox")

        others.click_google_search_bar()
        others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
        others.click_enter()
        try:
            others.wait_for_element_appearance("Continue with Google",10)
            login_page.click_Loginwith_Google()
            sleep(2)
            email = "zebratest850@gmail.com"
            social_login.choose_a_google_account(email)
        except:
            pass

        others.wait_for_element_appearance_text("Home",20)

        others.scroll_down()
        google_design = template_management.get_first_design_in_recently_printed_design_in_google()

        if t != google_design:
            raise Exception("printed design and first design in recently printed label of google are not same")
        curr_date = template_management.get_current_date_in_mm_dd_yy_format()

        print_date = template_management.get_printer_date_in_google()

        if curr_date != print_date:
            print(curr_date)
            print(print_date)
            raise Exception("dates are not matching")

    def test_Template_Management_TestcaseID_45911(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        name="45911"

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",10)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed properly")

        try:
            common_method.wait_for_element_appearance_namematches(name)
        except:
            raise Exception("name does not match")

        if not template_management.check_element_exists("Label 1 of 1"):
            raise Exception("Label 1 of 1 not displayed")

        try:
            template_management.check_element_exists("android.widget.EditText",1)
        except:
            pass

        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")
        sleep(2)
        prev_copies=template_management.get_no_of_copies()

        if not template_management.check_element_exists_name_or_text_matches("labels left"):
            raise Exception("labels left not displayed")

        curr_copies = template_management.get_no_of_copies()

        if prev_copies!=curr_copies:
            raise Exception("prev and curr copies are not same")

        template_management.check_element_exists("Total of 1 label")

        prev_count = template_management.get_no_of_labels_left_in_print_page()
        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")
        sleep(2)
        common_method.wait_for_element_appearance_enabled("Print")

        curr_count = template_management.get_no_of_labels_left_in_print_page()

        if not int(prev_count) == int(curr_count)+1:
            raise Exception("no of labels not updated")

        sleep(3)
        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45995(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Address"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()

        template_management.click_element_by_name_or_text(all_designs_in_categories[-1])

        template_management.click_on_copy_to_my_designs()
        try:
            common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
        except:
            raise Exception("design copied successfully is not displayed. is not displayed")

    def test_Template_Management_TestcaseID_45996(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        name = template_management.get_normal_design_if_there_in_first_screen_my_design()
        existing_design = template_management.get_names_of_design_in_search_designs([name])[0]

        temp=["Address","Barcode"]
        for text in temp[1:]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t=template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size=template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name=names[0]

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()

            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing",30)
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(name+" copy",1)
            except:
                raise Exception("copied name not found")

            try:
                template_management.click_the_duplicate_button()
            except:
                social_login.scroll_down(1)
                try:
                    template_management.get_the_full_name_of_design_and_click_in_my_design(name + " copy", 1)
                except:
                    raise Exception("copied name not found")
                template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            existing_name = existing_design
            template_management.enter_name_in_duplicate_designs(existing_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")

            duplicate_name=template_management.get_the_default_duplicate_name()

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")
            sleep(1)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            print("duplicate name",duplicate_name)
            try:
                d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name+" (1)", 1)
            except:
                raise Exception("c. Verify the copied design is displayed with correct name  (Name used in step 8 appended with number (1)). this step fails")

            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            common_method.wait_for_element_appearance_namematches("successfully removed")

    def test_Template_Management_TestcaseID_45997(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]

        for text in temp[1:]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t=template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size=template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name=names[0]

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()

            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            """Give the name of existing design here"""

            original_copy = name+" copy"
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            """Enter Zebra defined name here"""

            enter_name=name
            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")

            duplicate_name=enter_name+" (1)"

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            print("duplicate",duplicate_name)
            try:
                d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("failing this step:","c. Verify the Duplicate Design is displayed with correct name (Name used in step 6 appended with number (1)).")

    def test_Template_Management_TestcaseID_45998(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]

        for text in temp[1:]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()

            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            original_copy = name+" copy"

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            duplicate_name=template_management.get_the_default_duplicate_name()
            if original_copy+" copy"!=duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            enter_name="ab12c3!#"

            template_management.enter_name_in_duplicate_designs(enter_name)
            sleep(3)
            if not template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error not displayed for invalid name")

            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(enter_name,0)
                raise Exception("duplicate name found after cancelling")
            except:
                pass

    def test_Template_Management_TestcaseID_45999(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address",
                "Shipping", "Small Multipurpose"]

        for text in temp[:1]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            prev_designs = template_management.get_showing_n_designs_number()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()

            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            """Give the name of existing design here"""
            curr_designs = template_management.get_showing_n_designs_number()

            original_copy = name+" copy"

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)
            original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            duplicate_name=template_management.get_the_default_duplicate_name()
            if original_copy+" copy"!=duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            enter_name="!Special_123"
            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for valid name")
            duplicate_name=template_management.get_the_default_duplicate_name()

            template_management.click_on_save_button()
            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name,1)
            except:
                raise Exception("duplicate name not found")

            curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if int(original_date)!=0:
                raise Exception("last date displayed for not printed label ")

            if curr_size!= original_size or curr_date!=original_date:
                raise Exception("duplicate copy and original copy sizes not matching")

            if int(prev_designs)+1!=int(curr_designs):
                raise Exception("showing n designs not updated after copying a design")

            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            sleep(2)

    def test_Template_Management_TestcaseID_46001(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]

        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            prev_designs = template_management.get_showing_n_designs_number()
            #
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()
            #
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            original_copy = name+" copy"

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)

            prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            default_value= template_management.get_the_default_rename_text()
            if default_value!=original_copy:
                raise Exception("default value not matches the design's name")

            new_name = "somenamemyown"

            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")
            #
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            sleep(1)
            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(new_name, 1)
            except:
                raise Exception("design not found after updating")
            print("full name",full_name)
            curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size!=prev_size:
                raise Exception("size is not matching after renaming the design")

            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            sleep(2)

    def test_Template_Management_TestcaseID_46002(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]

        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            prev_designs = template_management.get_showing_n_designs_number()
            #
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()
            #
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev=template_management.get_showing_n_designs_number()

            original_copy = name+" copy"
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)
            prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            """Enter unique name here"""

            unique_name="uniquename"
            template_management.enter_name_in_duplicate_designs(unique_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")

            duplicate_name=unique_name

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            sleep(1)
            try:
                d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size!=prev_size:
                raise Exception("duplicate copy and original copy sizes not matching",duplicate_size,prev_size)

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy,0)
            except:
                raise Exception("original name not found")
            curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if  prev_size!=curr_size:
                raise Exception("original copy date or size has been changed")

            n_curr=template_management.get_showing_n_designs_number()
            if int(n_curr)!=int(n_prev)+1:
                raise Exception("Showing designs count not updated")

            template_management.select_design_in_my_design_by_name_and_return(duplicate_name,1)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")

            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            sleep(2)

    def test_Template_Management_TestcaseID_46003(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()
        """Pass the existing name design here"""
        name = template_management.get_normal_design_if_there_in_first_screen_my_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        duplicate_name = template_management.get_the_default_duplicate_name()
        if duplicate_name!=original_copy+" copy":
            raise Exception("default duplicate name is not as expected")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button not clickable")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button not clickable")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")
        sleep(1)

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=prev_size:
            raise Exception("duplicate copy and original copy sizes not matching",duplicate_size,prev_size)

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if prev_size!=curr_size or prev_date!=curr_date:
            raise Exception("original copy date or size has been changed")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev)+1:
            raise Exception("Showing designs count not updated")

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        duplicate_name = template_management.get_the_default_duplicate_name()
        if duplicate_name!=original_copy+" copy":
            raise Exception("default duplicate name is not as expected")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button not clickable")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button not clickable")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")
        sleep(1)

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name+" (1)", 0)
        except:
            raise Exception("duplicate name not found after duplicating again")

        temp=["Address"]
        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            prev_designs = template_management.get_showing_n_designs_number()
            #
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()
            #
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev=template_management.get_showing_n_designs_number()

            original_copy = name+" copy"
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)
            prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            duplicate_name = template_management.get_the_default_duplicate_name()
            if duplicate_name != original_copy + " copy":
                raise Exception("default duplicate name is not as expected")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button not clickable")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button not clickable")

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            sleep(1)

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != prev_size:
                raise Exception("duplicate copy and original copy sizes not matching", duplicate_size, prev_size)

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if prev_size != curr_size or prev_date != curr_date:
                raise Exception("original copy date or size has been changed")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) + 1:
                raise Exception("Showing designs count not updated")

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            duplicate_name = template_management.get_the_default_duplicate_name()
            if duplicate_name != original_copy + " copy":
                raise Exception("default duplicate name is not as expected")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button not clickable")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button not clickable")

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            sleep(1)

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name + " (1)", 0)
            except:
                raise Exception("duplicate name not found after duplicating again")

    def test_Template_Management_TestcaseID_45969(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Address"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Address"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            try:
                if int(copy_lastdate) != 0:
                    raise Exception("last printed date displayed for copied design without printing")
            except:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45970(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Barcodes"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Barcodes"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate) != 0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pm,pd,py=template_management.get_design_last_print_date(full_name)

            cm,cd,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45971(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="File Folder"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "File Folder"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate) != 0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45972(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Jewelry"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Jewelry"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate) != 0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45973(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Small Multipurpose"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Small Multipurpose"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate) != 0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")


    def test_Template_Management_TestcaseID_45975(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Shipping"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        for text in all_names[:1]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Shipping"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size != copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate) != 0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.scroll_till_print_enabled()
            except:
                raise Exception("print page is not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()
            common_method.wait_for_element_appearance_namematches("Label")
            template_management.scroll_till_print_enabled_button()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete",10)
                sleep(3)
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",0)

            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45974(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        text="Multipurpose"
        template_management.search_designs(text,1)
        template_management.wait_for_element_appearance_name_matches_all(text)
        template_management.click_element_name_matches_all(text,0)

        template_management.wait_until_designs_load_after_clicking_categories()
        all_designs_in_categories = template_management.get_all_designs_in_my_designs()
        all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)

        template_management.click_left_arrow()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        print(all_names)
        for text in all_names[7:8]:
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            texts = "Multipurpose"
            template_management.search_designs(texts, 1)
            template_management.wait_for_element_appearance_name_matches_all(texts)
            template_management.click_element_name_matches_all(texts, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            template_management.search_designs(text,1)
            template_management.wait_for_designs_in_comm_design()
            full_name=template_management.get_the_full_name_of_design_and_click_in_common_design_search(text,1)
            original_size,original_lastdate= template_management.get_the_size_and_lastprint_of_design(full_name)

            """4. Type in unique name for the design. Click "Save"
            this step is not applicable """

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(3)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(text+" copy",1)
                copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

            except:
                raise Exception("copied template not shown or is incorrect name")

            if original_size!=copy_size:
                raise Exception("copyied and original design sizes are not same")
            if int(copy_lastdate)!=0:
                raise Exception("last printed date displayed for copied design without printing")

            template_management.click_print_button_enabled()
            try:
                common_method.wait_for_element_appearance_namematches("Label")
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button_enabled()

            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete")
                sleep(3)
            except:
                raise Exception("print notification not displayed after print")

            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count)+1:
                raise Exception("no of labels not updated")

            sleep(3)
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.select_design_in_my_design_by_name_and_return(text+" copy",1)
            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            common_method.wait_for_element_appearance_namematches("removed")
            sleep(2)
            pd,pm,py=template_management.get_design_last_print_date(full_name)

            cd,cm,cy=template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45912(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        name="45912"
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",10)
            sleep(3)
        except:
            raise Exception("print page not displayed properly")

        initial_text = "Sample123"

        curr_text = template_management.get_text_from_element("android.widget.EditText",0)
        if initial_text!=curr_text:
            raise Exception("initial text not matching")

        template_management.input_text_in_element_by_name("android.widget.EditText","",0)
        curr_text = template_management.get_text_from_element("android.widget.EditText",0)
        if curr_text != "":
            raise Exception("text did not change")

        template_management.click_element_by_name_or_text("android.widget.EditText",0)
        new_text="new text"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
        curr_text = template_management.get_text_from_element("android.widget.EditText",0)
        if curr_text != new_text:
            raise Exception("text did not change")

        new_text="new 123@gmai\n.com"

        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
        others.go_back()

        curr_date = template_management.get_the_date_from_print_page()
        if curr_date!="11/11/2021":
            raise Exception("initial date is not matching")

        now_date = template_management.get_current_date_in_mm_dd_yy_format()
        cur_d = now_date.split("/")
        template_management.set_new_date_in_print_page(int(cur_d[1]))

        curr_date = template_management.get_the_date_from_print_page()
        changing_date=str(template_management.get_in_proper_dd_mm_yy_format())
        if curr_date!=changing_date:
            raise Exception("changed date is not matching")

        template_management.scroll_till_print_enabled_button()
        prev_count = template_management.get_no_of_labels_left_in_print_page()
        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print")
        try:
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
        except:
            pass

        curr_count = template_management.get_no_of_labels_left_in_print_page()

        if not int(prev_count) == int(curr_count)+1:
            raise Exception("no of labels not updated")

        sleep(2)
        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45913(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        name="45913"
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            sleep(3)
        except:
            raise Exception("print page not displayed")

        template_management.check_element_exists("android.widget.EditText",0)
        template_management.check_element_exists("android.widget.EditText",1)
        template_management.check_element_exists("Picture\nicon\nChoose an option",0)

        initial_text = template_management.get_text_from_element("android.widget.EditText",1)
        if initial_text!="123":
            raise Exception("initial_text not matching")
        template_management.click_element_by_name_or_text("android.widget.EditText",1)
        template_management.input_text_in_element_by_name("android.widget.EditText","",1)
        curr_text = template_management.get_text_from_element("android.widget.EditText",1)
        if curr_text:
            raise Exception("blank value not accepted")
        new_text="4567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,1)
        curr_text = template_management.get_text_from_element("android.widget.EditText",1)
        if curr_text!=new_text:
            raise Exception("new text not updated")
        others.go_back()

        initial_text = template_management.get_text_from_element("android.widget.EditText",0)
        if initial_text!="123456789012":
            raise Exception("initial_text not matching")
        template_management.click_element_by_name_or_text("android.widget.EditText",0)
        template_management.input_text_in_element_by_name("android.widget.EditText","",0)
        curr_text = template_management.get_text_from_element("android.widget.EditText",0)
        if curr_text:
            raise Exception("blank value not accepted")
        new_text="1234567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)
        curr_text = template_management.get_text_from_element("android.widget.EditText",0)
        if curr_text!=new_text:
            raise Exception("new text not updated")
        others.go_back()

        template_management.click_on_image_input_in_print_page()
        template_management.upload_image_in_print_page()

        sleep(8)

        template_management.scroll_till_print_enabled_button()
        prev_count = template_management.get_no_of_labels_left_in_print_page()

        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button_enabled()
        common_method.wait_for_element_appearance_enabled("Print",20)
        try:
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
        except:
            pass

        curr_count = template_management.get_no_of_labels_left_in_print_page()

        if not int(prev_count) == int(curr_count)+1:
            raise Exception("no of labels not updated")

        sleep(5)
        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

    def test_Template_Management_TestcaseID_45914(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        name="45914"
        common_method.wait_for_element_appearance_namematches("Showing")
        full_name = template_management.select_design_in_my_design_by_name_and_return(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            sleep(3)
        except:
            raise Exception("print page not displayed")

        template_management.click_on_copies()
        try:
            template_management.wait_for_element_appearance_name_matches_all("keyboard")
        except:
            raise Exception("key board is not present")
        prev_copies=template_management.get_no_of_copies()
        prev_labels = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_element_by_name_or_text("android.widget.EditText",0)

        template_management.input_text_in_element_by_name("android.widget.EditText","2",0)
        others.go_back()

        curr_copies=template_management.get_no_of_copies()
        if str(curr_copies)!='2':
            raise Exception("curr copies not updated")

        template_management.click_print_button_enabled()
        try:
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
        except:
            pass
        common_method.wait_for_element_appearance_enabled("Print")
        curr_labels = template_management.get_no_of_labels_left_in_print_page()
        temp=curr_labels
        if int(prev_labels)!=int(curr_labels)+2:
            raise Exception("no of labels left not updated")
        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()


        template_management.check_element_exists("My Designs")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,1)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        try:
            template_management.click_print_button()
        except:
            others.scroll_down()
            template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)
            template_management.click_print_button()

        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")
        curr_labels=template_management.get_no_of_labels_left_in_print_page()

        if curr_labels!=temp:
            raise Exception("count not same after re selecting the design")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()

        if str(labels_left) != str(curr_labels):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45915(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        template_management.wait_for_element_appearance_name_matches_all("Showing")
        name = "45913"
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")


        template_management.click_element_by_name_or_text("android.widget.EditText",1)

        new_text="4567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,1)

        others.go_back()
        template_management.click_element_by_name_or_text("android.widget.EditText",0)

        new_text="1234567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)

        others.go_back()
        template_management.click_on_image_input_in_print_page()
        template_management.upload_image_in_print_page()
        sleep(8)

        prev_labels = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_on_copies()
        if not template_management.check_copies_focused():
            raise Exception("cursor is not in copies")
        template_management.enter_no_of_copies(3)
        others.go_back()

        curr_copies=template_management.get_no_of_copies()

        if str(curr_copies)!='3':
            raise Exception("curr copies not updated")

        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button_enabled()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")

        common_method.wait_for_element_appearance_enabled("Print")
        curr_labels = template_management.get_no_of_labels_left_in_print_page()
        temp=curr_labels
        if int(prev_labels)!=int(curr_labels)+3:
            raise Exception("no of labels left not updated")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        template_management.check_element_exists("My Designs")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        full_name = template_management.select_design_in_my_design_by_name_and_return(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        template_management.get_the_full_name_of_design_and_click_in_my_design(name)
        try:
            template_management.click_print_button()
        except:
            others.scroll_down()
            template_management.get_the_full_name_of_design_and_click_in_my_design(name,1)
            template_management.click_print_button()

        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")
        curr_labels=template_management.get_no_of_labels_left_in_print_page()
        if curr_labels!=temp:
            raise Exception("count not same after reselecting the design")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            login_page.click_Menu_HamburgerICN()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()

        if str(labels_left) != str(curr_labels):
            raise Exception("labels left not updated")

        """For recently printed Labels"""

        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            sleep(3)
        except:
            raise Exception("print page not displayed")

        template_management.click_element_by_name_or_text("android.widget.EditText",1)

        new_text="4567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,1)

        others.go_back()
        template_management.click_element_by_name_or_text("android.widget.EditText",0)

        new_text="1234567890"
        template_management.input_text_in_element_by_name("android.widget.EditText",new_text,0)

        others.go_back()
        template_management.click_on_image_input_in_print_page()
        template_management.upload_image_in_print_page()
        sleep(8)

        prev_labels = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_on_copies()
        if not template_management.check_copies_focused():
            raise Exception("cursor is not in copies")
        template_management.enter_no_of_copies(3)
        others.go_back()

        curr_copies=template_management.get_no_of_copies()

        if str(curr_copies)!='3':
            raise Exception("curr copies not updated")

        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button_enabled()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")

        common_method.wait_for_element_appearance_enabled("Print")
        curr_labels = template_management.get_no_of_labels_left_in_print_page()
        temp=curr_labels
        if int(prev_labels)!=int(curr_labels)+3:
            raise Exception("no of labels left not updated")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("Home")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        common_method.wait_for_element_appearance_namematches("Recently")
        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,1)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        try:
            template_management.click_print_button()
        except:
            others.scroll_down()
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")
        curr_labels=template_management.get_no_of_labels_left_in_print_page()
        if curr_labels!=temp:
            raise Exception("count not same after reselecting the design")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("Home")
        except:
            login_page.click_Menu_HamburgerICN()

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        common_method.wait_for_element_appearance_namematches("Recently")

        labels_left = template_management.get_no_of_left_cartridge()

        if str(labels_left) != str(curr_labels):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45916(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('2.25" x 0.5"')
        a = template_management.get_names_of_design_in_search_designs([full_name])[0]

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        if not template_management.check_prompt_for_smaller_label_than_current():
            raise Exception("Prompt for smaller page is not displayed or may have wrong words")

        prev_labels = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_on_copies()

        template_management.enter_no_of_copies(1)
        others.go_back()
        template_management.click_print_button_enabled()

        curr_copies=template_management.get_no_of_copies()
        if int(curr_copies) != int('1'):
            raise Exception("current copies are not one")

        common_method.wait_for_element_appearance_enabled("Print")
        curr_labels = template_management.get_no_of_labels_left_in_print_page()
        temp=curr_labels
        if int(prev_labels)!=int(curr_labels)+1:
            raise Exception("no of labels left not updated")
        sleep(5)

        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        template_management.check_element_exists("My Designs")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(a,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()

        if str(labels_left) != str(curr_labels):
            raise Exception("labels left not updated")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('3.5" x 1.25"')

        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        if template_management.check_prompt_for_smaller_label_than_current():
            raise Exception("Prompt for smaller page is  displayed or may have wrong words")

        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print")
        template_management.click_print_button_enabled()

    def test_Template_Management_TestcaseID_45917(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('4" x 6"')
        a = template_management.get_names_of_design_in_search_designs([full_name])[0]
        template_management.click_print_button()

        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            sleep(3)
        except:
            raise Exception("print page not displayed")

        if not template_management.check_prompt_for_smaller_label_than_current():
            raise Exception("Prompt for smaller page is not displayed or may have wrong words")

        template_management.scroll_till_print_enabled_button()
        prev_labels = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_on_copies()

        template_management.enter_no_of_copies(1)
        others.go_back()
        template_management.click_print_button_enabled()
        try:
            template_management.wait_for_element_appearance_name_matches_all("Labels")
            sleep(2)
        except:
            pass
        curr_copies=template_management.get_no_of_copies()
        if str(curr_copies)!='1':
            raise Exception("current copies are not one")

        common_method.wait_for_element_appearance_enabled("Print")
        curr_labels = template_management.get_no_of_labels_left_in_print_page()
        temp=curr_labels
        if int(prev_labels)!=int(curr_labels)+1:
            raise Exception("no of labels left not updated")
        sleep(5)

        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        template_management.check_element_exists("My Designs")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(a,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()

        if str(labels_left) != str(curr_labels):
            raise Exception("labels left not updated")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('3.5" x 1.25"')
        template_management.click_print_button_enabled()
        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            sleep(3)
        except:
            raise Exception("print page not displayed")

        if template_management.check_prompt_for_smaller_label_than_current():
            raise Exception("Prompt for smaller page is  displayed or may have wrong words")
        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print")
        template_management.click_print_button_enabled()

    def test_Template_Management_TestcaseID_45918(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        all_printer_left_count = template_management.get_no_of_cartridge_left_in_all_printer()
        printer_1_prev_count = all_printer_left_count[0]
        printer_2_prev_count = all_printer_left_count[1]

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        all_names = template_management.get_ith_design_by_index_in_my_designs(2)
        name=all_names

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label",15)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed")

        """Printer 1 """
        printers = template_management.select_the_printer_in_print_preview_page_by_index(0,1)
        print("printers", printers)
        if len(printers) != 2:
            raise Exception("Check only 2 printers in the precondition are available for selection fails")

        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        prev_labels_1=template_management.get_no_of_labels_left_in_print_page()

        if not template_management.check_element_exists_name_or_text_matches("labels left"):
            raise Exception("labels left not displayed")

        if not template_management.check_element_exists_name_or_text_matches("Total of 1 label"):
            raise Exception("c. Verify total number of labels for printing (Total of 1 Labels) is correct this step fails")

        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print")

        curr_labels_1 = template_management.get_no_of_labels_left_in_print_page()

        if prev_labels_1 - 1 != curr_labels_1:
            raise Exception("prev and curr labels are not updated")

        """Printer 2"""

        printers = template_management.select_the_printer_in_print_preview_page_by_index(1,0)
        template_management.scroll_till_print_enabled_button()

        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        prev_labels_2=template_management.get_no_of_labels_left_in_print_page()

        try:
            template_management.check_element_exists_name_or_text_matches("labels left")
        except:
            raise Exception("labels left not displayed")

        try:
            template_management.check_element_exists_name_or_text_matches("Total of 1 label")
        except:
            raise Exception("c. Verify total number of labels for printing (Total of 1 Labels) is correct this step fails")

        template_management.click_print_button()
        common_method.wait_for_element_appearance_enabled("Print")

        curr_labels_2 = template_management.get_no_of_labels_left_in_print_page()

        if prev_labels_2 -1 != curr_labels_2:
            raise Exception("prev and curr labels are not updated")

        sleep(3)
        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        all_printer_left_count = template_management.get_no_of_cartridge_left_in_all_printer()
        printer_1_curr_count = all_printer_left_count[0]
        printer_2_curr_count = all_printer_left_count[1]

        if int(printer_1_curr_count)+1 != int(printer_1_prev_count):
            raise Exception("labels left not updated in printer 1")

        if int(printer_2_curr_count)+1 != int(printer_2_prev_count):
            raise Exception("labels left not updated in printer 2")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        name = template_management.get_ith_design_by_index_in_my_designs(4)
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label", 15)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed")

        curr_labels_1_a = template_management.get_no_of_labels_left_in_print_page()

        if curr_labels_1 != curr_labels_1_a:
            raise Exception("curr labels are not updated after selecting other designs")

        printers = template_management.select_the_printer_in_print_preview_page_by_index(1,0)

        curr_labels_2_a = template_management.get_no_of_labels_left_in_print_page()

        if curr_labels_2 != curr_labels_2_a:
            raise Exception("curr labels are not updated after selecting other designs")

    def test_Template_Management_TestcaseID_45919(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        t= template_management.get_first_design_in_my_designs()
        original_name = template_management.get_names_of_design_in_search_designs([t])[0]
        template_management.get_the_full_name_of_design_and_click_in_my_design(original_name)

        duplicate_name = template_management.duplicate_the_design_and_get_the_name()
        common_method.wait_for_element_appearance_namematches("successfully")
        if original_name+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not changing")

        duplicate_name=original_name+" copy"
        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        try:
            common_method.wait_for_element_appearance_namematches(duplicate_name)
        except:
            raise Exception("name does not match")

        if not template_management.check_element_exists("Label 1 of 1"):
            raise Exception("Label 1 of 1 not displayed")

        try:
            template_management.check_element_exists("android.widget.EditText",1)
        except:
            pass

        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button()
        try:
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
        except:
            pass

        prev_copies=template_management.get_no_of_copies()

        if not template_management.check_element_exists_name_or_text_matches("labels left"):
            raise Exception("labels left not displayed")

        curr_copies = template_management.get_no_of_copies()

        if prev_copies!=curr_copies:
            raise Exception("prev and curr copies are not same")

        template_management.check_element_exists("Total of 1 label")

        prev_count = template_management.get_no_of_labels_left_in_print_page()
        if not template_management.check_print_button_clickable:
            raise Exception("print option is not clickable")

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_namematches("Label")
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("Print page dint shown up")

        curr_count = template_management.get_no_of_labels_left_in_print_page()

        if not int(prev_count) == int(curr_count)+1:
            raise Exception("no of labels not updated")

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()
        print(labels_left,curr_count)
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45920(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        name="45912"
        template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        try:
            template_management.click_element_by_name_or_text("Cancel")
        except:
            pass

        template_management.click_element_by_name_or_text("android.widget.EditText",0)
        template_management.enter_the_special_characters_in_print_page("C31:C43'<>,.?£€)")
        a=template_management.get_text_from_element("android.widget.EditText",0)
        if a!="C31:C43'<>,.?£€)":
            raise Exception("special characters are not being accepted properly")

        try:
            template_management.click_element_by_name_or_text("Cancel")
        except:
            pass
        others.go_back()

        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button()


        if not template_management.check_element_exists_name_or_text_matches("labels left"):
            raise Exception("labels left not displayed")
        try:
            template_management.click_on_continue()
        except:
            pass
        template_management.check_element_exists("Total of 1 label")

        prev_count = template_management.get_no_of_labels_left_in_print_page()

        template_management.click_print_button()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")

        try:
            common_method.wait_for_element_appearance_namematches("Label",10)
            template_management.scroll_till_print_enabled_button()
        except:
            raise Exception("print page not displayed properly")

        curr_count = template_management.get_no_of_labels_left_in_print_page()

        if not int(prev_count) == int(curr_count)+1:
            raise Exception("no of labels not updated")

        sleep(1)
        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(2)

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        pd,pm,py=template_management.get_design_last_print_date(full_name)

        cd,cm,cy=template_management.get_current_date()
        if pd != cd or pm != cm or py != cy:
            raise Exception("dates are not matching")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()
        print(labels_left,curr_count)
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45923(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]

        template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        prev_count = template_management.get_no_of_labels_left_in_print_page()
        template_management.click_left_arrow()
        if not template_management.check_element_exists("My Designs"):
            template_management.click_left_arrow()

        template_management.check_element_exists("My Designs")

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name,0)

        try:
            template_management.get_design_last_print_date(full_name)
            raise Exception("last print updated")
        except:
            pass

        template_management.get_the_full_name_of_design_and_click_in_my_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        curr_count=template_management.get_no_of_labels_left_in_print_page()
        if prev_count!=curr_count:
            raise Exception("print label updated without printing")

        template_management.click_print_button_enabled()
        common_method.wait_for_element_appearance_enabled("Print")

        curr_count=template_management.get_no_of_labels_left_in_print_page()

        sleep(5)

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("My Designs")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        sleep(1)

        labels_left = template_management.get_no_of_left_cartridge()
        print(labels_left,curr_count)
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45924(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]

        template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        prev_count = template_management.get_no_of_labels_left_in_print_page()
        template_management.click_left_arrow()
        if not template_management.check_element_exists("Home"):
            template_management.click_left_arrow()

        template_management.check_element_exists("Home")

        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,0)

        try:
            template_management.get_design_last_print_date(full_name)
            raise Exception("last print updated")
        except:
            pass

        template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

        template_management.click_print_button()
        try:
            common_method.wait_for_element_appearance_enabled("Print",15)
        except:
            raise Exception("print page not displayed")

        curr_count=template_management.get_no_of_labels_left_in_print_page()
        if prev_count!=curr_count:
            raise Exception("print label updated without printing")

        template_management.scroll_till_print_enabled_button()
        template_management.click_print_button_enabled()
        template_management.wait_for_element_appearance_name_matches_all("Print complete")
        common_method.wait_for_element_appearance_enabled("Print")

        curr_count=template_management.get_no_of_labels_left_in_print_page()

        template_management.click_left_arrow()
        try:
            template_management.check_element_exists("Home")
        except:
            template_management.click_left_arrow()

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        labels_left = template_management.get_no_of_left_cartridge()
        print(labels_left,curr_count)
        if str(labels_left) != str(curr_count):
            raise Exception("labels left not updated")

    def test_Template_Management_TestcaseID_45926(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """a. Verify "Edit name" window is displayed not in mobile app"""
        """Save" button is NOT clickable (is clickable in mobile)"""

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        """need to automate a. Verify "Edit name" window is displayed
        b. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed"""
        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("default value not matches the design's name")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        template_management.enter_text_in_rename_design("\/")
        sleep(2)
        if not template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for invalid characters")

        new_name = "somenamemyown"

        template_management.enter_text_in_rename_design(new_name)
        sleep(1)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            sleep(1)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("design not found after updating")

        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45927(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("default value not matches the design's name")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is clickable")

        new_name = "ownname"

        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)

        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("design not found after updating")

        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45928(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)

        template_management.click_on_rename_button()

        new_name = "Address"

        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        try:
            full_name = template_management.select_design_in_my_design_by_name_and_return(new_name+" (1)", 0)
        except:
            raise Exception("design not found after updating")

        template_management.select_design_in_my_design_by_name_and_return(new_name+" (1)",1)
        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=new_name+" (1)":
            raise Exception("default value not updated to new value")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")
        template_management.click_on_cancel_button_in_rename_popup()

    def test_Template_Management_TestcaseID_45929(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """Give the name of existing design here"""
        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name,1)
        template_management.click_on_rename_button()
        new_name = "Address"

        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        try:
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name+" (1)", 0)
        except:
            raise Exception("design not found after updating")

        template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(new_name+" (1)",1)
        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=new_name+" (1)":
            raise Exception("default value not updated to new value")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")
        template_management.click_on_cancel_button_in_rename_popup()

    def test_Template_Management_TestcaseID_45930(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]

        names = template_management.get_ith_design_by_index_in_my_designs(1)
        names = template_management.get_names_of_design_in_search_designs([names])[0]
        full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(names,1)
        template_management.click_on_rename_button()
        template_management.enter_text_in_rename_design(name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")
        template_management.click_on_save_button_in_rename_design()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(name+" (1)", 0)
        except:
            raise Exception("design not found after updating")

        template_management.get_the_full_name_of_design_and_click_in_common_design_search(name+" (1)",1)
        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name+" (1)":
            raise Exception("default value not updated to new value")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")
        template_management.click_on_cancel_button_in_rename_popup()

    def test_Template_Management_TestcaseID_45931(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """Give the name of existing design here"""
        name = template_management.get_second_design_in_recently_printed_design()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,1)
        template_management.click_on_rename_button()
        template_management.click_on_save_button_in_rename_design()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name+" (1)", 0)
        except:
            raise Exception("design not found after updating")

        template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name+" (1)",1)
        template_management.click_on_rename_button()

        default_value = template_management.get_the_default_rename_text()
        if default_value != name+" (1)":
            raise Exception("default value not updated to new value")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")
        template_management.click_on_cancel_button_in_rename_popup()

    def test_Template_Management_TestcaseID_45932(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In",5)
        except:
            raise Exception("Did not redirect to the login page")

        """Sign in with email"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google",10)
        social_login.click_on_sign_in_with_email()

        """Provide the email and password"""
        email = "zebratest852@gmail.com"
        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email,password)

        try:
            social_login.wait_for_element_appearance("Home",20)
        except:
            raise Exception("home page dint show up")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        user2_name = template_management.get_first_design_in_my_designs()

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In",5)
        except:
            raise Exception("Did not redirect to the login page")
        """Google sign in"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google",10)
        login_page.click_Loginwith_Google()
        try:
            """Enter the email"""
            email = "zebratest850@gmail.com"
            social_login.choose_a_google_account(email)
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Recently")

        user2_name = "user2"

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
        prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("default value not matches the design's name")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")
        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        template_management.enter_text_in_rename_design(user2_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            sleep(2)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.select_design_in_my_design_by_name_and_return(user2_name, 0)
        except:
            raise Exception("design not found after updating")

        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size != prev_size or curr_date != prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45933(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """Note: the design should be printed if not design rename will not be shown in recently printed labels"""
        name = template_management.get_all_designs_in_recently_printed_labels()
        name = template_management.get_names_of_design_in_search_designs(name)[0]
        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,1)
        prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("default value not matches the design's name")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")
        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        """Enter design which is present in user2"""
        user2_name = "user2"

        template_management.enter_text_in_rename_design(user2_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            sleep(2)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(user2_name, 1)
        except:
            raise Exception("design not found after updating")

        template_management.click_on_rename_button()
        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

        invalid_name = "&*%"

        template_management.enter_text_in_rename_design(invalid_name)
        sleep(2)
        if not template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not  displayed for invalid characters")

        template_management.click_on_cancel_button_in_rename_popup()

        try:
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(user2_name, 0)
        except:
            raise Exception("design not found after canceling rename")

    def test_Template_Management_TestcaseID_45934(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        name = template_management.get_first_design_in_recently_printed_labels()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        template_management.enter_text_in_rename_design("")
        sleep(1)
        if not template_management.check_error_for_blank_value_in_rename_design():
            raise Exception("error not displayed for blank field")

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(1)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            template_management.click_on_rename_button()
        except:
            raise Exception("design name not found after blank value cancellation")

        default_value = template_management.get_the_default_rename_text()
        if default_value != name:
            raise Exception("default value not matches with original name")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        new_name="A_1"
        template_management.enter_text_in_rename_design(new_name)
        sleep(1)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error  displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(new_name, 1)
        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

        template_management.click_on_rename_button()

        template_management.enter_text_in_rename_design("&*%")
        sleep(2)
        if not template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for invalid characters")

        if template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is enabled for invalid characters")

        """. Input only one or several spaces
        Check spaces should be auto cleared and provide the message "Name must be at least 1 character…”  fails"""
        template_management.enter_text_in_rename_design("   ")
        sleep(1)
        if not template_management.check_error_for_blank_value_in_rename_design():
            raise Exception("error not displayed for blank field")

    def test_Template_Management_TestcaseID_45935(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(name,1)
        template_management.click_on_rename_button()
        new_name="A_1"
        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error  displayed for valid characters")

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(2)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
        except:
            raise Exception("design not found after cancelling")
        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("original name changed even after cancellation")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

    def test_Template_Management_TestcaseID_45936(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,1)
        template_management.click_on_rename_button()

        new_name="A_1"
        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error  displayed for valid characters")

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(2)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
        except:
            raise Exception("design not found after cancelling")
        template_management.click_on_rename_button()

        default_value= template_management.get_the_default_rename_text()
        if default_value!=name:
            raise Exception("original name changed even after cancellation")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

    def test_Template_Management_TestcaseID_45937(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]
        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)

            try:
                template_management.click_on_rename_button()
                raise Exception("rename button is present")
            except:
                pass

            template_management.click_left_arrow()
            sleep(1)
            template_management.click_left_arrow()

    def test_Template_Management_TestcaseID_45938(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""

        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)
        prev_size,prev_date= template_management.get_the_size_and_lastprint_of_design(full_name)
        template_management.click_on_rename_button()

        default_value = template_management.get_the_default_rename_text()
        if default_value != name:
            raise Exception("default value not matches with original name")

        template_management.enter_text_in_rename_design("Abc123+")
        if not template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for invalid characters")

        if template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is enabled for invalid characters")

        template_management.enter_text_in_rename_design("! @ $ ^ - ~ ( ) _  ` = { } | [ ] ; '")
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for allowed special characters ")

        new_name="new@_name"
        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for allowed special characters ")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is disabled for valid special characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(new_name, 0)
        except:
            raise Exception("updated name not found")
        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45940(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        name = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
        prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        template_management.click_on_rename_button()

        new_name="new@_name"
        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for allowed special characters ")

        template_management.turn_off_wifi()
        sleep(2)
        template_management.click_on_save_button_in_rename_design()
        """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error"""
        template_management.turn_on_wifi()
        sleep(5)
        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        try:
            full_name=template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("updated name not found")
        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45941(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """Give the name of existing design here"""
        name=template_management.get_first_design_in_recently_printed_labels()
        name=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
        prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        template_management.click_on_rename_button()

        new_name="ne@_name"
        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for allowed special characters ")

        template_management.turn_off_wifi()
        sleep(2)
        template_management.click_on_save_button_in_rename_design()
        """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error"""
        template_management.turn_on_wifi()
        sleep(5)
        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        try:
            full_name=template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("updated name not found")
        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

    def test_Template_Management_TestcaseID_45976(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
        template_management.check_search_icon()
        template_management.check_search_designs_text()

        template_management.click_on_search_design()
        """input value that does not match with our current designs"""

        not_exists_design="noexists"
        template_management.search_designs(not_exists_design,0)
        template_management.wait_for_element_appearance_name_matches_all("results")
        if not template_management.check_text_for_wrong_design_name():
            raise Exception("Proper message is not displayed for wrong design")

        """3. Type in text that does not have a match any of the user's designs
        a. Verify Suggestions dropdown is displayed
        b. Verify "No results for "searched text"" text is displayed (this step has error id SMBUI-1305)
        c. Verify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then."""

        template_management.search_designs("",1)
        common_method.wait_for_element_appearance_namematches("Showing")

        """a. Verify Suggestions dropdown is no longer displayed (but suggestions dropdown is displayed)"""

        my_designs_curr=template_management.get_all_designs_in_my_designs()

        n_designs = template_management.get_showing_n_designs_number()
        print(n_designs,len(my_designs_curr))
        if str(len(my_designs_curr))!=str(n_designs):
            raise Exception("total number of designs present , and showing n designs are not same count")

    def test_Template_Management_TestcaseID_45977(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        my_designs_prev=template_management.get_all_designs_in_my_designs()
        exists_design = template_management.get_names_of_design_in_search_designs(my_designs_prev)[0]
        """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()
        """input value that does not match with our current designs"""
        template_management.search_designs(exists_design,0)
        sleep(2)
        template_management.wait_for_suggestions_to_appear()
        if template_management.check_text_for_wrong_design_name():
            raise Exception("Proper message is displayed for correct design")

        res = template_management.get_all_search_results_in_search_designs()
        first_design_suggested=res[0]
        try:
            common_method.wait_for_element_appearance_enabled(first_design_suggested)
        except:
            raise Exception("element is not present or not clickable")
        sleep(2)
        template_management.click_element_by_name_or_text(first_design_suggested)

        common_method.wait_for_element_appearance_namematches("Showing")

        try:
            template_management.check_element_exists(first_design_suggested)
            raise Exception("suggestion is shown even after clicking the suggested design")
        except:
            pass

        n=template_management.get_showing_n_designs_number()
        if int(n)!=1:
            raise Exception("showing more than one design")

        template_management.search_designs("",1)
        common_method.wait_for_element_appearance_namematches("Showing")

        my_designs_curr=template_management.get_all_designs_in_my_designs()

        if my_designs_curr!=my_designs_prev:
            raise Exception("before and after searching results are not same")

        n_designs = template_management.get_showing_n_designs_number()
        print(n_designs,len(my_designs_curr))
        if str(len(my_designs_curr))!=str(n_designs):
            raise Exception("total number of designs present , and showing n designs are not same count")

    def test_Template_Management_TestcaseID_45978(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        my_designs_prev=template_management.get_all_designs_in_my_designs()

        """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()
        """input value that does not match with our current designs"""
        exists_design="test"
        template_management.search_designs(exists_design,0)
        sleep(2)
        template_management.wait_for_suggestions_to_appear()

        resu = template_management.get_all_search_results_in_search_designs()

        res=template_management.get_names_of_design_in_search_designs(resu)

        temp=["AddressTest","AssetTest","GiftTestLabel","IconGiftTestLabel","TestStatic","TestVariable"]

        print(res,temp)
        for i in temp:
            if i not in res:
                raise Exception(i,"not present in suggestions")

        try:
            common_method.wait_for_element_appearance_enabled(resu[-1])
        except:
            raise Exception("element is not present or not clickable")

        keyevent("enter")
        common_method.wait_for_element_appearance_namematches("Showing")

        n=template_management.get_showing_n_designs_number()
        if int(n)!=6:
            raise Exception("not showing 6 design")

        template_management.search_designs("",1)
        common_method.wait_for_element_appearance_namematches("Showing")

        my_designs_curr=template_management.get_all_designs_in_my_designs()

        print("here",my_designs_curr,my_designs_prev)
        if my_designs_curr!=my_designs_prev:
            raise Exception("before and after searching results are not same")

        n_designs = template_management.get_showing_n_designs_number()
        print(n_designs,len(my_designs_curr))
        if str(len(my_designs_curr))!=str(n_designs):
            raise Exception("total number of designs present , and showing n designs are not same count")

    def test_Template_Management_TestcaseID_45980(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        prev_all_designs=template_management.get_all_designs_in_my_designs()

        n_prev=template_management.get_showing_n_designs_number()

        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()

        """Enter the text here"""
        text="_SG"
        template_management.search_designs(text,0)

        template_management.wait_for_suggestions_to_appear()

        resu = template_management.get_all_search_results_in_search_designs()
        if len(resu)!=3:
            raise Exception("more than 3 design is displayed for _SG search")

        for i in resu:
            try:
                common_method.wait_for_element_appearance_enabled(i)
            except:
                raise Exception(i,"element is not present or not clickable")

        selected_design=resu[0]
        design = template_management.get_names_of_design_in_search_designs(resu)[0]
        template_management.click_element_by_name_or_text(selected_design)

        try:
            template_management.check_for_suggestion_drop_down_in_search_designs()
            raise Exception("suggestion window displayed after clicking an element")
        except:
            pass

        common_method.wait_for_element_appearance_namematches("Showing")

        temp = template_management.get_all_designs_in_my_designs()
        if len(temp) != 1:
            raise Exception("more or less designs is displayed after selecting in suggestion")
        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=1:
            raise Exception("Verify the count in the Showing 1 designs is not correct.")

        text=""
        template_management.search_designs(text,1)
        common_method.wait_for_element_appearance_namematches("Showing")

        curr_all_designs=template_management.get_all_designs_in_my_designs()

        if prev_all_designs!=curr_all_designs:
            raise Exception("prev all designs and curr all designs are not same")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev):
            raise Exception("Showing designs count changed")

        text="~`!@#$%^&*()_-+={}[]|/\:;\"'<>,.?"
        template_management.search_designs(text,0)
        social_login.wait_for_element_appearance_namematches_all("No results found.")

        if not template_management.check_text_for_wrong_design_name():
            raise Exception("Proper message is not displayed for wrong design")

        text=""
        template_management.search_designs(text,1)
        common_method.wait_for_element_appearance_namematches("Showing")

        curr_all_designs=template_management.get_all_designs_in_my_designs()

        if prev_all_designs!=curr_all_designs:
            raise Exception("prev all designs and curr all designs are not same")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev):
            raise Exception("Showing designs count changed")

    def test_Template_Management_TestcaseID_46006(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()

        text="no_text_match"
        template_management.search_designs(text,0)
        social_login.wait_for_element_appearance_namematches_all("No results")

        if not template_management.check_text_for_wrong_design_name():
            raise Exception("Proper message is not displayed for wrong design")

        text=""
        template_management.search_designs(text,1)

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering blank value")

    def test_Template_Management_TestcaseID_46007(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()

        text="Address"
        template_management.search_designs(text,0)
        template_management.wait_for_element_appearance_name_matches_all("CATEGORIES")

        if not template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion not displayed or not clickable")
        if not template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion not displayed or not clickable")

        if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("Verify on the designs section, the number of designs that matches is displayed on the right side (not meeting this step)")

        others.click_enter()

        common_method.wait_for_element_appearance_namematches("Search")

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering search")

        try:
            search_count = template_management.get_total_count_search_results_in_common_designs()
        except:
            raise Exception("Search count is not displayed properly")
        template_management.wait_for_element_appearance_name_matches_all("Categories")
        try:
            categories_count = template_management.get_total_count_categories_results_in_common_designs()
        except:
            raise Exception("Categories count is not displayed properly")

        temp=template_management.get_all_categories_in_search_designs()
        if not template_management.check_element_present_in_array("Address",temp):
            raise Exception("categories displayed which is not matching to search value")

        try:
            design_count = template_management.get_total_count_designs_results_in_common_designs()
        except:
            raise Exception("Design count is not displayed properly")


        temp=template_management.get_all_designs_in_search_designs()
        if not template_management.check_element_present_in_array("Address",temp):
            raise Exception("designs displayed which is not matching to search value")

        text=""
        template_management.search_designs(text,1)

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering blank value")

    def test_Template_Management_TestcaseID_46008(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()

        text="File Folder"
        template_management.search_designs(text,0)
        template_management.wait_for_element_appearance_name_matches_all("CATEGORIES")

        if not template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion not displayed or not clickable")
        if  template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion displayed ")

        others.click_enter()

        common_method.wait_for_element_appearance_namematches("Search")

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering search")

        try:
            search_count = template_management.get_total_count_search_results_in_common_designs()
        except:
            raise Exception("Search count is not displayed properly")
        template_management.wait_for_element_appearance_name_matches_all("Categories")
        try:
            categories_count = template_management.get_total_count_categories_results_in_common_designs()
        except:
            raise Exception("Categories count is not displayed properly")

        temp=template_management.get_all_categories_in_common_designs()
        if not template_management.check_element_present_in_array("Address",temp):
            raise Exception("categories displayed which is not matching to search value")

        """e. Verify designs section is displayed with zero(0) results and "No designs were found with current filters." text.
        this step cannt be done"""

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        a = template_management.get_the_search_bar_text()
        if a:
            raise Exception("search designs text bar is not empty")

    def test_Template_Management_TestcaseID_46009(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()

        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()

        text="Asset"
        template_management.search_designs(text,0)
        template_management.wait_for_element_appearance_name_matches_all("DESIGNS")

        if template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion Displayed or not clickable")
        if not template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion not displayed ")

        others.click_enter()

        common_method.wait_for_element_appearance_namematches("Search")

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering search")

        try:
            search_count = template_management.get_total_count_search_results_in_common_designs()
        except:
            raise Exception("Search count is not displayed properly")

        try:
            categories_count = template_management.get_total_count_categories_results_in_common_designs()
            raise Exception("Categories count is displayed ")
        except:
            pass

        temp=template_management.get_all_designs_in_search_designs()
        if not template_management.check_element_present_in_array(text,temp):
            raise Exception("categories displayed which is not matching to search value")

        text=""
        template_management.search_designs(text,1)

        if template_management.check_suggestion_window_in_common_design():
            raise Exception("suggestion window is displayed after entering blank value")

    def test_Template_Management_TestcaseID_46011(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_for_element_appearance_name_matches_all("Address")
        prev=template_management.get_all_categories_in_common_designs()

        """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
        template_management.check_search_icon()
        template_management.check_search_designs_text()
        template_management.click_on_search_design()
        """input value that does not match with our current designs"""

        not_exists_design="noexistsaddress"
        template_management.search_designs(not_exists_design,0)
        template_management.wait_for_element_appearance_name_matches_all("results")
        if not template_management.check_text_for_wrong_design_name():
            raise Exception("Proper message is not displayed for wrong design")

        template_management.search_designs("",1)
        if template_management.check_suggestion_window_in_common_design() or template_management.check_text_for_wrong_design_name():
            raise Exception("suggestion window is displayed after entering search")

        template_management.wait_for_element_appearance_name_matches_all("Address")
        curr=template_management.get_all_categories_in_common_designs()
        if prev!=curr:
            raise Exception("all categories are not displayed after and before search")

    def test_Template_Management_TestcaseID_46012(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]
        for text in temp[1:]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()

            all_designs = template_management.get_all_designs_in_my_designs()
            all_names = template_management.get_names_of_design_in_search_designs(all_designs)

            t = max(all_names, key=lambda x: len(x))
            template_management.check_search_icon()
            template_management.check_search_designs_text()

            template_management.search_designs(t, 0)
            template_management.wait_for_element_appearance_name_matches_all("1 result")
            a = template_management.get_all_search_results_in_search_designs()
            print(a)
            if len(a)!=1:
                raise Exception("More than one design is displayed")
            if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("design name is not clickable")
            template_management.click_element_name_matches_all(t)
            if template_management.check_for_suggestion_drop_down_in_search_designs():
                raise Exception("suggestion drop down is displayed after clicking the element")

            searched_elements = template_management.get_all_designs_in_my_designs()
            template_management.check_element_present_in_array(t,searched_elements)
            template_management.search_designs("", 1)
            template_management.wait_for_element_appearance_name_matches_all(all_names[1])
            curr_designs = template_management.get_all_designs_in_my_designs()
            if all_designs!=curr_designs:
                raise Exception("-Verify all designs are displayed in the Category. is failing")

            template_management.click_left_arrow()

    def test_Template_Management_TestcaseID_46013(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Address","Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address", "Shipping", "Small Multipurpose"]
        for text in temp[1:]:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()

            all_designs = template_management.get_all_designs_in_my_designs()
            all_names = template_management.get_names_of_design_in_search_designs(all_designs)

            t = 'a'
            template_management.check_search_icon()
            template_management.check_search_designs_text()

            template_management.search_designs(t, 0)
            template_management.wait_for_element_appearance_name_matches_all("1 result")
            a = template_management.get_all_search_results_in_search_designs()
            print(a)
            matched_names=template_management.get_names_of_design_in_search_designs(a)

            if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("design name is not clickable")
            others.click_enter()
            if template_management.check_for_suggestion_drop_down_in_search_designs():
                raise Exception("suggestion drop down is displayed after clicking the element")
            template_management.wait_for_element_appearance_name_matches_all(matched_names[1])

            tem = template_management.get_all_designs_in_my_designs()
            searched_elements = template_management.get_names_of_design_in_search_designs(tem)

            print("searched",searched_elements)
            print("matched_names", matched_names)
            if searched_elements != matched_names:
                raise Exception("suggestion designs and results designs are not same")

            template_management.search_designs("", 1)
            template_management.wait_for_element_appearance_name_matches_all(all_names[1])
            curr_designs = template_management.get_all_designs_in_my_designs()
            if all_designs!=curr_designs:
                raise Exception("-Verify all designs are displayed in the Category. is failing")

            template_management.click_left_arrow()

    def test_Template_Management_TestcaseID_46004(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")

        temp=["Jewelry"]
        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name = names[0]
            template_management.click_on_copy_to_my_designs()

            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()
            #
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev=template_management.get_showing_n_designs_number()

            original_copy = name+" copy"
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy,1)

            template_management.click_print_button_enabled()
            common_method.wait_for_element_appearance_enabled("Print")
            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Complete",10)
            except:
                pass

            template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            social_login.wait_for_element_appearance("Sign In",10)
            login_page.click_loginBtn()
            login_page.click_Loginwith_Google()

            """Enter the email"""
            email = "zebratest850@gmail.com"
            social_login.choose_a_google_account(email)
            social_login.wait_for_element_appearance("Home",15)

            try:
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy)
                raise Exception("copied design found in another account")
            except:
                pass

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            template_management.wait_for_element_appearance_name_matches_all("Showing")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy)
                raise Exception("copied design found in another account")
            except:
                pass

    def test_Template_Management_TestcaseID_45942(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        """Give the name of existing design here"""
        t = template_management.get_first_design_in_my_designs()
        original_copy = template_management.get_names_of_design_in_search_designs([t])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name = template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev)+1:
            raise Exception("Showing designs count not updated")

        template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
        if not template_management.verify_options_clickable_in_design():
            raise Exception("some options are not clickable")
        template_management.click_on_delete_button_in_designs()
        sleep(1)
        template_management.click_on_delete_button_in_designs()

    def test_Template_Management_TestcaseID_45943(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """f. Verify the count in the "Showing x designs" is correct will not be present in home page"""

        """Give the name of existing design here"""
        name=template_management.get_first_design_in_recently_printed_labels()
        original_copy=template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
        if not template_management.verify_options_clickable_in_design():
            raise Exception("some options are not clickable")
        template_management.click_on_delete_button_in_designs()
        sleep(1)
        template_management.click_on_delete_button_in_designs()

    def test_Template_Management_TestcaseID_45944(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        """Give the name of existing design here"""
        name = template_management.get_first_design_in_my_designs()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter unique name here"""

        unique_name="uniquename"
        template_management.enter_name_in_duplicate_designs(unique_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=template_management.get_the_default_duplicate_name()

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev)+1:
            raise Exception("Showing designs count not updated")

        template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
        if not template_management.verify_options_clickable_in_design():
            raise Exception("some options are not clickable")
        template_management.click_on_delete_button_in_designs()
        sleep(1)
        template_management.click_on_delete_button_in_designs()

    def test_Template_Management_TestcaseID_45945(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Give the name of existing design here"""
        name=template_management.get_first_design_in_recently_printed_labels()
        original_copy=template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter unique name here"""

        unique_name="unique_name"
        template_management.enter_name_in_duplicate_designs(unique_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=template_management.get_the_default_duplicate_name()

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
        if not template_management.verify_options_clickable_in_design():
            raise Exception("some options are not clickable")
        template_management.click_on_delete_button_in_designs()
        sleep(1)
        template_management.click_on_delete_button_in_designs()

    def test_Template_Management_TestcaseID_45946(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        """Give the name of existing design here"""

        name = template_management.get_first_design_in_my_designs()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter unique name here"""

        template_management.enter_name_in_duplicate_designs(original_copy)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=original_copy+" (1)"

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        print("duplicate",duplicate_name)
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 1)
        except:
            raise Exception("duplicate name not found")

        template_management.click_the_duplicate_button()

        duplicate_name_after=template_management.get_the_default_duplicate_name()
        if duplicate_name_after!=duplicate_name+" copy":
            raise Exception(" not meeting condition Verify default value matches the updated design's name with appended text copy")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

    def test_Template_Management_TestcaseID_45947(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Give the name of existing design here"""

        name=template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
        original_copy=template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter unique name here"""

        template_management.enter_name_in_duplicate_designs(original_copy)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=original_copy+" (1)"

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        print("duplicate",duplicate_name)
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 1)
        except:
            raise Exception("duplicate name not found")

        template_management.click_the_duplicate_button()

        duplicate_name_after=template_management.get_the_default_duplicate_name()
        if duplicate_name_after!=duplicate_name+" copy":
            raise Exception(" not meeting condition Verify default value matches the updated design's name with appended text copy")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

    def test_Template_Management_TestcaseID_45948(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        """Give the name of existing design here"""

        name = template_management.get_normal_design_if_there_in_first_screen_my_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter Zebra defined name here"""

        enter_name="Address"
        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=enter_name+" (1)"

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        print("duplicate",duplicate_name)
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 1)
        except:
            raise Exception("duplicate name not found")

        template_management.click_the_duplicate_button()

        duplicate_name_after=template_management.get_the_default_duplicate_name()
        if duplicate_name_after!=duplicate_name+" copy":
            raise Exception(" not meeting condition Verify default value matches the updated design's name with appended text copy")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

    def test_Template_Management_TestcaseID_45949(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Give the name of existing design here"""

        name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()
        """Enter unique name here"""

        enter_name="Asset"
        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for proper unique name")

        duplicate_name=enter_name+" (1)"
        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        print("duplicate",duplicate_name)
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 1)
        except:
            raise Exception("duplicate name not found")

        template_management.click_the_duplicate_button()

        duplicate_name_after=template_management.get_the_default_duplicate_name()
        if duplicate_name_after!=duplicate_name+" copy":
            raise Exception(" not meeting condition Verify default value matches the updated design's name with appended text copy")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

    def test_Template_Management_TestcaseID_45950(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        """Give the name of existing design here"""

        name = template_management.get_normal_design_if_there_in_first_screen_my_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        n_curr=template_management.get_showing_n_designs_number()
        if int(n_curr)!=int(n_prev)+1:
            raise Exception("Showing designs count not updated")

    def test_Template_Management_TestcaseID_45951(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """f. Verify the count in the "Showing x designs" is correct will not be present in home page"""

        """Give the name of existing design here"""

        name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
        template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy,1)
        template_management.click_the_duplicate_button()
        template_management.click_on_save_button()
        duplicate_copy_name = original_copy+" copy"

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy,0)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(duplicate_copy_name,1)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if duplicate_copy_name+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 0)
        except:
            raise Exception("duplicate name not found")

        duplicate_size,duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=original_size or duplicate_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy,0)
        except:
            raise Exception("original name not found")
        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
        if original_date!=curr_date or original_size!=curr_size:
            raise Exception("original copy date or size has been changed")

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        my_design_dup_size,my_design_dup_date=template_management.get_the_size_and_lastprint_of_design(d_full_name)

        if duplicate_size!=my_design_dup_size or duplicate_date!=my_design_dup_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

    def test_Template_Management_TestcaseID_45952(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Gets the name of existing first design here"""

        name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy,1)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        enter_name=""
        template_management.enter_name_in_duplicate_designs(enter_name)
        sleep(2)
        if not template_management.check_for_blank_value_error_in_duplicate_design():
            raise Exception("error not displayed for blank name")

        enter_name="a1! "

        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error  displayed for valid  name")

        """Verify no error message is displayed except inputing space key (for inputting space also no error is displayed)"""

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(2)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy,1)
        except:
            raise Exception("original name not found")

        template_management.click_the_duplicate_button()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

        enter_name="abc"

        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error  displayed for valid  name")

        duplicate_name=template_management.get_the_default_duplicate_name()

        template_management.click_on_save_button()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name,1)
        except:
            raise Exception("original name not found")

        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!= original_size or curr_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")

        template_management.click_the_duplicate_button()
        enter_name="&*%"

        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error  displayed for valid  name")

        if template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable for invalid characters")

    def test_Template_Management_TestcaseID_45953(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        """Give the name of existing design here as per setup"""

        original_copy = "Abc123~`!@"

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy,1)
        original_size,original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        enter_name="!Special_123"
        template_management.enter_name_in_duplicate_designs(enter_name)
        if template_management.check_for_invalid_character_error_in_duplicate_design():
            raise Exception("error displayed for valid name")
        duplicate_name=template_management.get_the_default_duplicate_name()

        """Has a bug SMBM-2206 so cannot automate step 4 in his test case"""

        template_management.click_on_save_button()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name,0)
        except:
            raise Exception("duplicate name not found")

        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!= original_size or curr_date!=original_date:
            raise Exception("duplicate copy and original copy dates or sizes not matching")
        sleep(5)
        try:
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy,0)
        except:
            raise Exception("original name not found")

        curr_size,curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!= original_size or curr_date!=original_date:
            raise Exception("original copy before and after original copy dates or sizes not matching")

        """Verify the count in the "Showing x designs" is correct this step is not applicable for recently printed labels"""

        template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
        if not template_management.verify_options_clickable_in_design():
            raise Exception("some options are not clickable")

    def test_Template_Management_TestcaseID_45955(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        name = template_management.get_normal_design_if_there_in_first_screen_my_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(2)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        duplicate_name=original_copy+" copy"
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            raise Exception("duplicate name not found")
        except:
            pass

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
        except:
            raise Exception("original name not found")

        template_management.click_the_duplicate_button()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

    def test_Template_Management_TestcaseID_45956(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Recently")
        name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

        template_management.click_the_duplicate_button()

        template_management.verify_duplicate_design_window()

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(2)
        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("duplicate design window not closed")

        duplicate_name=original_copy+" copy"
        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(duplicate_name, 0)
            raise Exception("duplicate name not found")
        except:
            pass

        try:
            d_full_name=template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
        except:
            raise Exception("original name not found")

        template_management.click_the_duplicate_button()

        duplicate_name=template_management.get_the_default_duplicate_name()
        if original_copy+" copy"!=duplicate_name:
            raise Exception("default duplicate name is not matching as expected")

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")

    def test_Template_Management_TestcaseID_45957(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        """input an existing design name"""
        original_copy=template_management.get_first_design_in_my_designs()
        original_copy = template_management.get_names_of_design_in_search_designs([original_copy])[0]

        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_on_delete_button_in_designs()
        template_management.check_delete_design_window_message()

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_delete_button_clickable_in_design_window():
            raise Exception("delete button is not clickable")

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(1)

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
        except:
            raise Exception("original name not found")

        template_management.click_on_delete_button_in_designs()

        template_management.click_on_delete_button_in_designs()

        try:
            common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=int(n_prev)-1:
            raise Exception("Showing designs count not updated")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        try:
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
            raise Exception("original name not found after deleting in recently printed design")
        except:
            pass

    def test_Template_Management_TestcaseID_45958(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        common_method.wait_for_element_appearance_namematches("Recently")

        name=template_management.get_first_design_in_recently_printed_labels()
        original_copy=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

        template_management.click_on_delete_button_in_designs()
        template_management.check_delete_design_window_message()

        if not template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management.check_delete_button_clickable_in_design_window():
            raise Exception("delete button is not clickable")

        template_management.click_on_cancel_button_in_rename_popup()
        sleep(1)

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
        except:
            raise Exception("original name not found")

        template_management.click_on_delete_button_in_designs()

        template_management.click_on_delete_button_in_designs()

        try:
            common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass
        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=int(n_prev)-1:
            raise Exception("Showing designs count not updated")

    def test_Template_Management_TestcaseID_45959(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """Add more categories as required"""
        temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Badge", "Return Address",
                "Shipping", "Small Multipurpose"]

        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)

            try:
                template_management.click_on_delete_button_in_designs()
                raise Exception("rename button is present")
            except:
                pass

            template_management.click_left_arrow()
            sleep(1)
            template_management.click_left_arrow()

    def test_Template_Management_TestcaseID_45961(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        """input an existing design name"""
        original_copy = "Barcode copy"
        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_on_delete_button_in_designs()
        template_management.check_delete_design_window_message()

        template_management.click_on_delete_button_in_designs()

        try:
            common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=int(n_prev)-1:
            raise Exception("Showing designs count not updated")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        try:
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

    def test_Template_Management_TestcaseID_45962(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """ has this error still SMBM-1902"""
        """5. Go to web portal and other mobile app client to have a check that the template is not deleted
         pending """

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        name = template_management.get_first_design_in_my_designs()
        original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

        template_management.click_on_delete_button_in_designs()
        template_management.check_delete_design_window_message()

        template_management.turn_off_wifi()
        sleep(2)
        template_management.click_on_delete_button_in_designs()

        template_management.turn_on_wifi()
        common_method.wait_for_element_appearance_enabled("Delete")
        sleep(5)
        template_management.click_on_delete_button_in_designs()

        try:
            common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=int(n_prev)-1:
            raise Exception("Showing designs count not updated")

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        common_method.wait_for_element_appearance_namematches("Recently")

        try:
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

    def test_Template_Management_TestcaseID_45963(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        """ has this error still SMBM-1902"""
        """5. Go to web portal and other mobile app client to have a check that the template is not deleted
         pending """
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_prev=template_management.get_showing_n_designs_number()

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        common_method.wait_for_element_appearance_namematches("Recently")

        """input an existing design name"""
        name=template_management.get_first_design_in_recently_printed_labels()
        original_copy=template_management.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

        template_management.click_on_delete_button_in_designs()
        template_management.check_delete_design_window_message()

        template_management.turn_off_wifi()
        sleep(2)
        template_management.click_on_delete_button_in_designs()

        template_management.turn_on_wifi()
        common_method.wait_for_element_appearance_enabled("Delete")
        sleep(5)
        template_management.click_on_delete_button_in_designs()

        try:
            common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
        except:
            raise Exception("Design has been successfully duplicated. is not displayed")

        if template_management.check_cancel_button_clickable_in_rename_popup():
            raise Exception("delete design window not closed")

        try:
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
            raise Exception("original name found after deleting")
        except:
            pass

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        n_curr=template_management.get_showing_n_designs_number()

        if int(n_curr)!=int(n_prev)-1:
            raise Exception("Showing designs count not updated")

        try:
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            raise Exception("original name not found after deleting")
        except:
            pass

    def test_Template_Management_TestcaseID_45964(self):
        pass

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        sleep(1)

        try:
            template_management.get_all_designs_in_my_designs()
            raise Exception("designs are present")
        except:
            pass

        if not template_management.check_no_designs_present_text():
            raise Exception("proper message not displayed for empty designs in my designs")

    def test_Template_Management_TestcaseID_45967(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        strings = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping", "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose", "XL Shipping"]

        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        curr_categories = template_management.get_all_categories_in_common_designs()
        categories = template_management.get_names_of_design_in_search_designs(curr_categories)

        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management.click_common_designs_button()
        template_management.wait_in_common_designs_until_load()

        for i in strings:
            if i not in categories:
                raise Exception(i,"this category is not present in common designs")

        try:
            template_management.verify_zebra_icon_in_the_categories(curr_categories)
        except:
            raise Exception("zebra icon not present for some category")

        if not template_management.verify_description_present_in_the_categories(curr_categories):
            raise Exception("description not present for some category")

    def test_Template_Management_TestcaseID_45968(self):
        pass

        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping", "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose"]
        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            try:
                template_management.wait_for_element_appearance_name_matches_all(text)
            except:
                raise Exception(text,"this category text not displayed")
            if not template_management.check_left_arrow_exists():
                raise Exception("left arrow is not present")

            all_complete_designs = template_management.get_all_designs_in_my_designs()
            all_designs = template_management.get_names_of_design_in_search_designs(all_complete_designs)
            all_designs = template_management.make_everything_lower_case(all_designs)
            sorted_design = all_designs
            sorted_design = sorted(sorted_design)

            """Commented code currently cannot be verified since labels are not sorted properly"""
            # if all_designs != sorted_design:
            #     raise Exception("designs are not in sorted order")

            for i in all_complete_designs:
                name,size,lastprint = template_management.get_the_name_size_and_lastprint_of_design(i)
                if int(lastprint)!=0:
                    raise Exception("last print displayed for",i,"design")

            template_management.scroll_till_element(all_designs[0],1)

            for i in all_complete_designs[:2]:
                template_management.click_on_the_element_in_categories(i)
                try:
                    common_method.wait_for_element_appearance_enabled("Print")
                except:
                    raise Exception("Print button not clickable in common design")
                try:
                    common_method.wait_for_element_appearance_enabled("Copy to My Designs")
                except:
                    raise Exception("Copy to My design button not clickable in common design")

                template_management.click_left_arrow()

            template_management.click_left_arrow()

            if not template_management.check_element_exists("Common Designs"):
                raise Exception("common designs page is not displayed after clicking left arrow")

    def test_Template_Management_TestcaseID_46000(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        temp=["Jewelry"]
        for text in temp:

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text,1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text,0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t=template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names,size=template_management.get_names_and_sizes_in_recently_printed_labels([t])
            name=names[0]
            print("t",t)
            d_size,d_last_print = template_management.get_the_size_and_lastprint_of_design(t)

            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")
            sleep(2)
            template_management.click_left_arrow()
            try:
                login_page.click_Menu_HamburgerICN()
            except:
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()

            template_management.click_home_button()

            name="BOGO copy"
            start_app("com.google.android.googlequicksearchbox")
            sleep(1)
            others.click_google_search_bar()
            others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
            others.click_enter()
            others.wait_for_element_appearance("Continue with Google",10)
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            """pass your email below for the same account"""
            email = "zebratest850@gmail.com"
            template_management.select_and_click_an_google_account(email)

            common_method.wait_for_element_appearance_text("Home",20)
            others.click_hamburger_button_in_Google()
            try:
                template_management.click_on_click_on_my_designs_in_google()
            except:
                others.click_hamburger_button_in_Google()
                template_management.click_on_click_on_my_designs_in_google()
            others.click_hamburger_button_in_Google()

            designs_present = template_management.search_design_in_google_present(name)
            g_size, g_last_print = template_management.get_size_and_lastprint_of_design_in_google(name)
            if not designs_present:
                raise Exception("copied design is not present in the google")
            if g_size != d_size:
                raise Exception("sizes are different for same design in app and web")
            if int(d_last_print)!=0:
                raise Exception("last print date displayed without printing for the copy")

            """3. Go to Home > Recently Printed Designs.
        -Verify copied design is NOT displayed. this step fails due to bug id: SMBM-1372"""
            # start_app("com.zebra.soho_app")
            #
            # others.wait_for_element_appearance_text("Home",20)
            #
            # others.scroll_down()
            #
            # common_method.wait_for_element_appearance_namematches("Recently")
            # try:
            #     template_management.get_the_full_name_of_design_and_click_in_my_design(name+" copy",0)
            #     raise Exception("copied name found in recently printed label without printing ")
            # except:
            #     pass

    def test_Template_Management_TestcaseID_45939(self):
        pass
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        common_method.wait_for_element_appearance_namematches("Home")
        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name=template_management.get_first_design_in_my_designs()
        full_name = name
        template_management.click_element_by_name_or_text(name)
        prev_size,prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

        template_management.click_on_rename_button()

        new_name = "somenamemyown"

        template_management.enter_text_in_rename_design(new_name)
        if template_management.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)

        except:
            raise Exception("design has been successfully renamed. is not displayed")
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        template_management.click_home_button()

        start_app("com.google.android.googlequicksearchbox")

        others.click_google_search_bar()
        others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
        others.click_enter()
        others.wait_for_element_appearance("Continue with Google",20)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account",20)
        """pass your email below for the same account"""
        email = "zebratest850@gmail.com"
        template_management.select_and_click_an_google_account(email)

        common_method.wait_for_element_appearance_text("Home",20)
        others.click_hamburger_button_in_Google()
        template_management.click_on_click_on_my_designs_in_google()
        others.click_hamburger_button_in_Google()

        designs_present = template_management.search_design_in_google_present(new_name)
        g_size, g_last_print = template_management.get_size_and_lastprint_of_design_in_google(new_name)
        if not designs_present:
            raise Exception("renamed design is not present in the google")
        # """size in mobile and app should be same ,this step fails due to SMBM : 1749"""
        # if g_size != prev_size:
        #     raise Exception("sizes are different for same design in app and web")
        if int(g_last_print)!=0:
            raise Exception("last print date displayed without printing for the copy")

        start_app("com.zebra.soho_app")

        common_method.wait_for_element_appearance_namematches("Home",30)

        login_page.click_Menu_HamburgerICN()
        template_management.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")

        try:
            full_name = template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("design not found after updating")

        curr_size,curr_date= template_management.get_the_size_and_lastprint_of_design(full_name)

        if curr_size!=prev_size or curr_date!=prev_date:
            raise Exception("size or date is not matching after renaming the design")

