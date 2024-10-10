# from poco import poco
import time
import pytest
# import sys
# sys.path.append(r'C:\Users\tr5927\Desktop\ZSB_Automation')

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...Common_Method import Common_Method
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Others.Others import Others
from ...PageObject.Social_Login.Social_Login import Social_Login
import inspect

import os
from ...TestSuite.api_calls import *
from ...TestSuite.store import *

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)
template_management = Template_Management_Android(poco)
login_page = Login_Screen(poco)
common_method = Common_Method(poco)
others = Others(poco)
social_login = Social_Login(poco)

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def show_message(msg):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Ensure the root window is on top
    messagebox.showinfo("Information", msg)
    root.destroy()


def get_user_input(msg):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)
    user_input = simpledialog.askstring("Input", msg)
    return user_input


class test_Android_Template_Management_Reporting:
    # pass
    def __init__(self):
        pass

    def test_Template_Management_TestcaseID_45902(self):
        test_steps = {
            1: [1, 'Login to Mobile App.'],
            2: [2, 'Verify there are no designs shown in Home > Recently Printed Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
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

            try:
                others.wait_for_element_appearance("Sign In", 10)
                login_page.click_loginBtn()
                common_method.wait_for_element_appearance_namematches("Continue with Google")
                login_page.click_Loginwith_Google()

                """enter email here"""
                email = "zebra850.swdvt@gmail.com"
                common_method.wait_for_element_appearance_textmatches("Choose an account")
                others.choose_google_account(email)
            except:
                pass
            common_method.wait_for_element_appearance_namematches("Recently")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Verify there are no designs shown in Home > Recently Printed Designs
            start_time = time.time()
            total_designs = template_management.get_all_designs_in_recently_printed_labels()
            if len(total_designs) != 0:
                raise Exception("Label found in recently printed design even without printing")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45903(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3, 'Select the design in the precondition'],
            4: [4, 'Click Print option on the list menu'],
            5: [5, 'Print 1 copy\n-Verify toast alert "Print job sent" is displayed.\n-Verify 1 label is printed'],
            6: [6,
                'Click Print "Back" button. Go to Home > Recently Printed Designs.\na. Verify the design is displayed at the top of the list\nb. Verify the design has "Last Print" information which is equal to the current date']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            try:
                common_method.wait_for_element_appearance_namematches("Open navigation menu")
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
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select the design in the precondition
            start_time = time.time()
            prev = template_management.get_first_design_in_my_designs()
            template_management.click_first_design_in_my_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Print option on the list menu
            start_time = time.time()
            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Print 1 copy
            start_time = time.time()
            template_management.click_print_button_enabled()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print "Back" button. Go to Home > Recently Printed Designs
            start_time = time.time()
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(2)
            curr = template_management.get_first_design_in_recently_printed_labels()

            if prev != curr:
                raise Exception("the top of recently printed label is not as expected")

            curr_mon, curr_date, curr_year = template_management.get_current_date()
            des_mon, des_date, des_year = template_management.get_design_last_print_date(curr)
            if curr_mon != des_mon or curr_date != des_date or curr_year != des_year:
                raise Exception("dates not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45904(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3, 'Select one design in the precondition'],
            4: [4, 'Click Print option on the list menu'],
            5: [5, 'Print 1 copy\n-Verify toast alert "Print job sent" is displayed.\n-Verify 1 label is printed'],
            6: [6,
                'Click Print "Back" button. Go to Home > Recently Printed Designs.\na. Verify the design is displayed at the top of the list\nb. Verify the design has "Last Print" information which is equal to the current date'],
            7: [7, 'After printing the 7th design, verify that only the 6 most Recently Printed Designs are displayed'],
            8: [8,
                'Delete one of the designs in the Recently Printed Designs.\n-Verify design is removed from the list.\n-Verify the 6th most recently printed design is added at the bottom of the list. Total of 6 designs are displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Login to Mobile App

            start_time = time.time()
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
            email = "zebra850.swdvt@gmail.com"
            common_method.wait_for_element_appearance_textmatches("Choose an account")
            others.choose_google_account(email)
            common_method.wait_for_element_appearance_namematches("Home")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId["45904"], test_steps[2][0], stepId, test_steps[2][1], "Pass", exec_time)
            stepId += 1

            # Step 3: Select one design in the precondition
            start_time = time.time()
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

            for i in total_my_designs[5:6]:
                common_method.wait_for_element_appearance_namematches("Showing.")
                template_management.click_design_in_my_designs_by_full_name(i)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[3][0], stepId, test_steps[3][1], "Pass", exec_time)
                stepId += 1

                # Step 4: Click Print option on the list menu
                start_time = time.time()
                template_management.click_print_button()
                try:
                    common_method.wait_for_element_appearance_namematches("Label", 10)
                    template_management.scroll_till_print_enabled_button()
                except:
                    raise Exception("print page not displayed properly")
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[4][0], stepId, test_steps[4][1], "Pass", exec_time)
                stepId += 1

                # Step 5: Print 1 copy
                start_time = time.time()
                template_management.click_print_button_enabled()
                try:
                    common_method.wait_for_element_appearance_namematches("Print complete", 10)
                except:
                    raise Exception("print_toast_dint_pop up")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[5][0], stepId, test_steps[5][1], "Pass", exec_time)
                stepId += 1

                # Step 6: Click Print "Back" button. Go to Home > Recently Printed Designs
                start_time = time.time()
                common_method.wait_for_element_appearance_enabled("android.widget.Button", 10)
                template_management.click_left_arrow()
                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(2)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[6][0], stepId, test_steps[6][1], "Pass", exec_time)
                stepId += 1

                # Step 7: Verify only the 6 most Recently Printed Designs are displayed after printing the 7th design
                start_time = time.time()
                # Insert code to verify only the 6 most Recently Printed Designs are displayed
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[7][0], stepId, test_steps[7][1], "Pass", exec_time)
                stepId += 1

                # Step 8: Delete one of the designs in the Recently Printed Designs
                start_time = time.time()
                # Insert code to delete one of the designs in the Recently Printed Designs
                # Insert code to verify design is removed from the list
                # Insert code to verify the 6th most recently printed design is added at the bottom of the list
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45904"], test_steps[8][0], stepId, test_steps[8][1], "Pass", exec_time)


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def logout_and_login(self, email, password):
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
        email = email
        password = password
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.choose_google_account(email)
        common_method.wait_for_element_appearance_namematches("Home", 20)

    def test_Template_Management_TestcaseID_45905(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4,
                'Select any of the available designs that are compatible with the label size of the cartridge installed in the printer. Click "Copy to My Designs" option on the list menu'],
            5: [5, 'Go to My Designs. Select the copied design'],
            6: [6, 'Click Print option on the list menu'],
            7: [7, 'Print 1 copy.\n-Verify toast alert "Print job sent" is displayed.\n-Verify 1 label is printed'],
            8: [8,
                'Click Print "Back" button. Go to Home > Recently Printed Designs.\na. Verify the design is displayed at the top of the list.\nb. Verify the design has "Last Print" information which is equal to the current date']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Login to Mobile App

            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")

            self.logout_and_login("zebra850.swdvt@gmail.com", "Zebra#123456789")

            """Copy design from common design to my design"""

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select Address category
            start_time = time.time()
            text = "Address"
            template_management.search_designs(text, 1)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select a design compatible with the label size of the cartridge installed in the printer. Click "Copy to My Designs" option
            start_time = time.time()
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            curr_design = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(curr_design)
            curr_design = template_management.get_names_of_design_in_search_designs([curr_design])[0]

            template_management.get_the_full_name_of_design_and_click_in_my_design(curr_design, 1)

            template_management.click_on_copy_to_my_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Go to My Designs. Select the copied design
            start_time = time.time()
            template_management.wait_for_element_appearance_name_matches_all("successfully copied")
            sleep(2)
            template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            template_management.search_designs(curr_design)

            common_method.wait_for_element_appearance_namematches("Showing", 20)
            template_management.click_first_design_in_my_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print option on the list menu
            start_time = time.time()
            template_management.click_print_button()
            common_method.wait_for_element_appearance_enabled("Print", 30)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Print 1 copy
            start_time = time.time()
            template_management.click_print_button_enabled()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Click Print "Back" button. Go to Home > Recently Printed Designs
            start_time = time.time()
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            common_method.wait_for_element_appearance("Recently Printed Labels")
            curr = template_management.get_first_design_in_recently_printed_labels()
            curr = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(curr_design, 0)
            curr = template_management.get_first_design_in_recently_printed_labels()

            if curr_design != curr:
                raise Exception("the top of recently printed label is not as expected")
            curr_mon, curr_date, curr_year = template_management.get_current_date()
            des_mon, des_date, des_year = template_management.get_design_last_print_date(curr)
            if curr_mon != des_mon or curr_date != des_date or curr_year != des_year:
                raise Exception("dates not matching")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45906(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4,
                'Select any of the available designs that are compatible with the label size of the cartridge installed in the printer. Click Print option on the list menu'],
            5: [5, 'Print 1 copy.\n-Verify toast alert "Print job sent" is displayed.\n-Verify 1 label is printed'],
            6: [6,
                'Click Print "Back" button. Go to Home > Recently Printed Designs.\na. Verify the design is displayed at the top of the list.\nb. Verify the design has "Last Print" information which is equal to the current date']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App

            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance("Home", 10)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            """Copy design from common design to my design"""

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select Address category
            start_time = time.time()
            template_management.search_designs("Address")
            common_method.wait_for_element_appearance_namematches("Categories")
            template_management.select_first_design()

            template_management.wait_for_designs_in_comm_design()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select a design compatible with the label size of the cartridge installed in the printer. Click Print option
            start_time = time.time()
            template_management.click_first_design_in_common_design()
            sleep(2)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Print 1 copy
            start_time = time.time()
            template_management.click_print_button_enabled()

            """Will fail if the first design is not updated with the recently printed label"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print "Back" button. Go to Home > Recently Printed Designs
            start_time = time.time()
            common_method.wait_for_element_appearance_enabled("android.widget.Button", 10)
            template_management.click_left_arrow()
            common_method.wait_for_element_appearance_enabled("android.widget.Button", 10)
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()

            common_method.wait_for_element_appearance("Recently Printed Labels")
            curr = template_management.get_first_design_in_recently_printed_labels()

            curr_mon, curr_date, curr_year = template_management.get_current_date()
            des_mon, des_date, des_year = template_management.get_design_last_print_date(curr)
            if curr_mon != des_mon or curr_date != des_date or curr_year != des_year:
                raise Exception("dates not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45907(self):
        test_steps = {
            1: [1, 'Go to Home > Recently Printed Designs'],
            2: [2, 'Verify "Recently Printed Labels" text is displayed'],
            3: [3, 'Verify the names of the designs are correct'],
            4: [4, 'Verify the sizes of the designs are correct'],
            5: [5, 'Verify the thumbnail images of the designs are displayed'],
            6: [6, 'Verify the "Last Print" dates of the designs are correct'],
            7: [7,
                'Click on one of the designs and check the following options are clickable: Print, Rename, Duplicate, Delete'],
            8: [8, 'Click outside the design and check the design menu is closed'],
            9: [9, 'Click on each of the designs and verify the design menu is displayed'],
            10: [10, 'Click outside the design and verify the design menu is closed'],
            11: [11, 'Scroll up and down the list and verify the designs are displayed properly']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Go to Home > Recently Printed Designs

            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Verify "Recently Printed Labels" text is displayed
            start_time = time.time()
            if not template_management.verify_element_exists_by_name("Recently Printed Labels"):
                raise Exception("no recently printed label text")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Verify the names of the designs are correct
            start_time = time.time()
            """pass no of designs printed as parameter"""
            all_designs = template_management.get_all_designs_in_recently_printed_labels(6)

            names, sizes = template_management.get_names_and_sizes_in_recently_printed_labels(all_designs)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Verify the sizes of the designs are correct
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Verify the thumbnail images of the designs are displayed
            start_time = time.time()
            common_method.wait_for_element_appearance("Recently Printed Labels")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Verify the "Last Print" dates of the designs are correct
            start_time = time.time()
            template_management.check_the_dates_of_last_print_in_recent_print_labels(all_designs)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Click on one of the designs and check the following options are clickable: Print, Rename, Duplicate, Delete
            start_time = time.time()
            curr = template_management.click_first_design_in_recently_printed_labels()

            a = template_management.verify_options_clickable_in_design()
            if not a:
                raise Exception("some options are not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Click outside the design and check the design menu is closed
            start_time = time.time()
            template_management.close_menu_of_design_in_home()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Click on each of the designs and verify the design menu is displayed
            start_time = time.time()
            template_management.click_and_close_menu_designs_in_home(all_designs)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 10: Click outside the design and verify the design menu is closed
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 11: Scroll up and down the list and verify the designs are displayed properly
            start_time = time.time()
            common_method.wait_for_element_appearance("Recently Printed Labels")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45908(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design mentioned in setup, click Print option'],
            3: [3,
                'Print 1 copy. Check toast alert "Print job sent" is displayed. Note: for mobile app, there is no such toast message. Just check the label is NOT printed out'],
            4: [4,
                'Click Print "Back" button. Go to Home > Recently Printed Designs. Verify the number of prints left is NOT updated'],
            5: [5, 'Changed the condition of Printer to ready for printing'],
            6: [6, 'Verify label is printed'],
            7: [7,
                'Refresh the page. Verify the design is still displayed in Recently Printed Designs. Verify the number of prints left is updated']
        }

        show_message("2. Set printer to offline or error status(Media low/Media out/Cover open)\n3. There is an "
                     "existing design in My Designs but hasn't been printed yet")
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            prev = template_management.get_no_of_left_cartridge()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design mentioned in setup, click Print option
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            total = template_management.get_all_designs_in_my_designs()
            template_management.click_on_design_which_is_not_printed_yet(total)

            template_management.click_print_button()
            common_method.wait_for_element_appearance_enabled("Print", 10)

            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Print 1 copy. Check toast alert "Print job sent" is displayed. Note: for mobile app, there is no such toast message. Just check the label is NOT printed out
            start_time = time.time()
            try:
                template_management.click_print_button_enabled()
            except:
                template_management.scroll_till_print_enabled()
                template_management.click_print_button_enabled()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Print "Back" button. Go to Home > Recently Printed Designs. Verify the number of prints left is NOT updated
            start_time = time.time()
            template_management.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            curr = template_management.get_no_of_left_cartridge()
            if prev != curr:
                raise Exception("number of prints left is updated after printer being turned off")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Changed the condition of Printer to ready for printing
            start_time = time.time()
            show_message("Turn on Printer to be online , wait for 30sec and press ok")
            common_method.swipe_by_positions([0.5, 0.5], [0.5, 1.0])
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Verify label is printed
            start_time = time.time()
            common_method.show_message("Verify label is printed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Refresh the page. Verify the design is still displayed in Recently Printed Designs. Verify the number of prints left is updated
            start_time = time.time()
            after = template_management.get_no_of_left_cartridge()

            if after - 1 != curr:
                raise Exception("number of prints left is not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45910(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Turn off the WiFi connection on the mobile device settings'],
            3: [3,
                'Go to Home > Recently Printed Designs. Check there is a dialog popping up, with prompt message "The service is currently unavailable", click Continue button on the dialog. Check the dialog is closed and there is no design shown'],
            4: [4, 'Turn on the WiFi connection on the mobile device settings'],
            5: [5, 'Go back to the Mobile App. Verify there are designs shown in Recently Printed Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Turn off the WiFi connection on the mobile device settings
            start_time = time.time()
            prev_designs = template_management.get_all_designs_in_recently_printed_labels()
            template_management.turn_off_wifi()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Go to Home > Recently Printed Designs
            start_time = time.time()
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
            if len(curr_designs) > 0:
                raise Exception("designs are displayed after turning off the wifi  ")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Turn on the WiFi connection on the mobile device settings
            start_time = time.time()
            template_management.turn_on_wifi()
            sleep(5)
            template_management.refresh_the_home_page_()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Go back to the Mobile App
            start_time = time.time()

            common_method.wait_for_element_appearance("Recently Printed Labels")

            after_designs = template_management.get_all_designs_in_recently_printed_labels()

            if prev_designs != after_designs:
                raise Exception("designs are not matching before and after turning on wifi")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45909(self):
        test_steps = {
            1: [1, 'Go to web portal and sign in the same account'],
            2: [2,
                'Go to Home > Recently Printed Designs. Verify the design in the precondition is displayed at the top of the list. Verify the design has "Last Print" information which is equal to the current date, and the date is shown completely']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to web portal and sign in the same account

            start_time = time.time()
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
                others.wait_for_element_appearance("Continue with Google", 10)
                login_page.click_Loginwith_Google()
                sleep(2)
                email = "zebra850.swdvt@gmail.com"
                social_login.choose_a_google_account(email)
            except:
                pass

            others.wait_for_element_appearance_text("Home", 20)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Home > Recently Printed Designs
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45911(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3,
                'Select the design in the setup 2, and click Print option. Verify Print page is displayed. Verify the design\'s name is displayed at the top of the page with "Back" button. Verify the design\'s elements are displayed in the print preview. Verify label count (Label 1 of 1) is displayed below the image. Verify there are no controls to input data. Verify "Print" button is clickable'],
            4: [4,
                'Click "Print" button. Verify the number of labels left (x labels left) is displayed. Verify only the printers registered to the user are displayed in the Printer\'s list options. Verify number of copies to be printed is the same as in previous step. Verify total number of labels for printing (Total of 1 Labels) is correct. Verify "Print" button is clickable'],
            5: [5,
                'Click "Print" button. Verify 1 label with correct output is printed. Verify toast alert "Print job sent" is displayed'],
            6: [6, 'In Print window, verify the number of labels left (x labels left) is updated'],
            7: [7,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date'],
            8: [8,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")

            self.logout_and_login("zebra850.swdvt@gmail.com", "Zebra#123456789")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select the design and click Print option, verify print page
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            name = "45911"

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click "Print" button, verify print options and details
            start_time = time.time()
            try:
                common_method.wait_for_element_appearance_namematches(name)
            except:
                raise Exception("name does not match")

            if not template_management.check_element_exists("Label 1 of 1"):
                raise Exception("Label 1 of 1 not displayed")

            try:
                template_management.check_element_exists("android.widget.EditText", 1)
            except:
                pass

            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            template_management.click_print_button()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
            sleep(2)

            prev_copies = template_management.get_no_of_copies()

            if not template_management.check_element_exists_name_or_text_matches("labels left"):
                raise Exception("labels left not displayed")
            curr_copies = template_management.get_no_of_copies()

            if prev_copies != curr_copies:
                raise Exception("prev and curr copies are not same")

            template_management.check_element_exists("Total of 1 label")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click "Print" button, verify print job and toast alert
            start_time = time.time()

            template_management.click_print_button()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
            sleep(2)
            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Verify number of labels left is updated
            start_time = time.time()
            if not int(prev_count) == int(curr_count) + 1:
                raise Exception("no of labels not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Click Print "Back" button, verify My Designs view and Last Print information
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Go to Home > Recently Printed Designs, verify total number of labels left
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45995(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Select and click any of the design\n-Verify "Copy to My Designs" option is clickable'],
            5: [5, 'Click "Copy to My Designs"\nCheck toast message is shown']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select Address category
            start_time = time.time()
            text = "Address"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select and click any of the design
            start_time = time.time()
            template_management.click_element_name_matches_all(text, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            all_designs_in_categories = template_management.get_all_designs_in_my_designs()

            template_management.click_element_by_name_or_text(all_designs_in_categories[-1])
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click "Copy to My Designs"
            start_time = time.time()
            template_management.click_on_copy_to_my_designs()
            try:
                common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
            except:
                raise Exception("design copied successfully is not displayed. is not displayed")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45996(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4,
                'Select any of the design. Click on the 3-dot menu.\n-Verify "Copy to My Designs" option is clickable'],
            5: [5,
                'Click "Copy to My Designs".\na. Verify notification alert " has been successfully copied to your workspace." is displayed and dismiss after few seconds'],
            6: [6, 'Go to My Designs.\na. Verify the copied design is displayed with correct name (copy)'],
            7: [7,
                'Select the copied design and click Duplicate\na. Verify "Duplicate design" window is displayed.\nb. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)'],
            8: [8,
                'Input value of an existing design name in user\'s account.\na. Verify no error message is displayed'],
            9: [9,
                'Click "Save" button.\na. Verify "Duplicate Design" window is closed.\nb. Verify notification alert "Design has been successfully duplicated." is displayed. Click "x" button.\nc. Verify the copied design is displayed with correct name (Name used in step 8 appended with number (1))']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            name = template_management.get_normal_design_if_there_in_first_screen_my_design()
            existing_design = template_management.get_names_of_design_in_search_designs([name])[0]

            temp = ["Address", "Barcode"]
            for text in temp[1:]:
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select Address category
                start_time = time.time()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Select any design and click 3-dot menu
                start_time = time.time()
                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
                name = names[0]
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Click "Copy to My Designs" and verify notification alert
                start_time = time.time()
                template_management.click_on_copy_to_my_designs()
                try:
                    common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
                except:
                    raise Exception("design copied successfully is not displayed. is not displayed")
                sleep(2)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Go to My Designs and verify copied design
                start_time = time.time()
                template_management.click_left_arrow()
                try:
                    login_page.click_Menu_HamburgerICN()
                except:
                    template_management.click_left_arrow()
                    login_page.click_Menu_HamburgerICN()

                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing", 30)
                try:
                    template_management.get_the_full_name_of_design_and_click_in_my_design(name + " copy", 1)
                except:
                    raise Exception("copied name not found")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 7: Select copied design and click Duplicate
                start_time = time.time()
                try:
                    template_management.click_the_duplicate_button()
                except:
                    social_login.scroll_down(1)
                    try:
                        template_management.get_the_full_name_of_design_and_click_in_my_design(name + " copy", 1)
                    except:
                        raise Exception("copied name not found")
                    template_management.click_the_duplicate_button()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 8: Input value of an existing design name
                start_time = time.time()
                template_management.verify_duplicate_design_window()

                existing_name = existing_design
                template_management.enter_name_in_duplicate_designs(existing_name)
                if template_management.check_for_invalid_character_error_in_duplicate_design():
                    raise Exception("error displayed for proper unique name")

                duplicate_name = template_management.get_the_default_duplicate_name()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 9: Click "Save" button and verify
                start_time = time.time()
                template_management.click_on_save_button()

                try:
                    common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
                except:
                    raise Exception("Design has been successfully duplicated. is not displayed")
                sleep(1)
                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("duplicate design window not closed")
                print("duplicate name", duplicate_name)
                try:
                    d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(
                        duplicate_name + " (1)", 1)
                except:
                    raise Exception(
                        "c. Verify the copied design is displayed with correct name  (Name used in step 8 appended with number (1)). this step fails")

                template_management.click_on_delete_button_in_designs()
                template_management.click_on_delete_button_in_designs()
                common_method.wait_for_element_appearance_namematches("successfully removed")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45997(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3, 'Select and click any of the design.\n-Verify "Duplicate" option is clickable'],
            4: [4,
                'Click "Duplicate".\na. Verify "Duplicate design" window is displayed.\nb. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)'],
            5: [5,
                'Input name of an existing Zebra design in Common Designs (ie:Address).\n-Verify no error message is displayed'],
            6: [6,
                'Click "Save" button.\na. Verify "Duplicate Design" window is closed.\nb. Verify notification alert "Design has been successfully duplicated." is displayed. Click "x" button.\nc. Verify the Duplicate Design is displayed with correct name (Name used in step 6 appended with number (1))']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            for text in temp[2:3]:

                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
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
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select and click any design, verify "Duplicate" option
                start_time = time.time()
                common_method.wait_for_element_appearance_namematches("Showing")

                """Give the name of existing design here"""

                original_copy = name + " copy"
                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

                template_management.click_the_duplicate_button()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Click "Duplicate" and verify "Duplicate design" window
                start_time = time.time()
                template_management.verify_duplicate_design_window()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Input name of an existing Zebra design in Common Designs
                start_time = time.time()
                enter_name = name
                template_management.enter_name_in_duplicate_designs(enter_name)
                if template_management.check_for_invalid_character_error_in_duplicate_design():
                    raise Exception("error displayed for proper unique name")

                duplicate_name = enter_name + " (1)"
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Click "Save" button and verify duplication
                start_time = time.time()
                template_management.click_on_save_button()

                try:
                    common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
                except:
                    raise Exception("Design has been successfully duplicated. is not displayed")

                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("duplicate design window not closed")

                print("duplicate", duplicate_name)
                try:
                    sleep(3)
                    d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name,
                                                                                                         0)
                except:
                    raise Exception("failing this step:",
                                    "c. Verify the Duplicate Design is displayed with correct name (Name used in step 6 appended with number (1)).")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45998(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3, 'Select and click any of the design.\n-Verify "Duplicate" option is clickable'],
            4: [4,
                'Click "Duplicate".\na. Verify "Duplicate design" window is displayed.\nb. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)'],
            5: [5, 'Clear the default value in the input box control'],
            6: [6, 'Input the following values.\na. ab\nb. 12\nc. c3\nd. !#'],
            7: [7,
                'Click "Cancel" button.\na. Verify "Duplicate design" window is closed.\nb. Verify design is NOT copied in the My Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            for text in temp[5:6]:

                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
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
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select and click any design, verify "Duplicate" option
                start_time = time.time()
                common_method.wait_for_element_appearance_namematches("Showing")

                original_copy = name + " copy"

                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Click "Duplicate" and verify "Duplicate design" window
                start_time = time.time()
                template_management.click_the_duplicate_button()

                template_management.verify_duplicate_design_window()
                duplicate_name = template_management.get_the_default_duplicate_name()
                if original_copy + " copy" != duplicate_name:
                    raise Exception("default duplicate name is not matching as expected")

                enter_name = "ab12c3!#"

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Clear the default value in the input box control
                start_time = time.time()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Input the following values: ab, 12, c3, !#
                start_time = time.time()
                values_to_test = ["ab", "12", "c3", "!#"]
                for value in values_to_test:
                    template_management.enter_name_in_duplicate_designs(enter_name)
                    sleep(3)
                    if not template_management.check_for_invalid_character_error_in_duplicate_design():
                        raise Exception("error not displayed for invalid name")
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 7: Click "Cancel" button and verify design is NOT copied
                start_time = time.time()
                template_management.click_on_cancel_button_in_rename_popup()
                sleep(2)

                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("duplicate design window not closed")

                try:
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(enter_name, 0)
                    raise Exception("duplicate name found after cancelling")
                except:
                    pass
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45999(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3, 'Select and click any of the design.\n-Verify "Duplicate" option is clickable'],
            4: [4,
                'Click "Duplicate".\na. Verify "Duplicate design" window is displayed.\nb. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)'],
            5: [5, 'Input name !Special_123\n-Verify no error message is displayed'],
            6: [6,
                'Click "Save" button.\na. Verify "Duplicate design" window is closed.\nb. Verify toast alert "design has been successfully duplicated." is displayed'],
            7: [7,
                'Go to My Designs.\na. Verify the copied design is displayed with correct name.\nb. Verify the copied design\'s elements and information (Size, Thumbnail, no Last Print) matches the Zebra design.\nc. Verify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            for text in temp[6:7]:

                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing")
                prev_designs = template_management.get_showing_n_designs_number()

                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
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
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select and click any design, verify "Duplicate" option
                start_time = time.time()
                common_method.wait_for_element_appearance_namematches("Showing")

                """Give the name of existing design here"""
                curr_designs = template_management.get_showing_n_designs_number()

                original_copy = name + " copy"

                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)
                original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Click "Duplicate" and verify "Duplicate design" window
                start_time = time.time()
                template_management.click_the_duplicate_button()

                template_management.verify_duplicate_design_window()

                duplicate_name = template_management.get_the_default_duplicate_name()
                if original_copy + " copy" != duplicate_name:
                    raise Exception("default duplicate name is not matching as expected")
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Input name !Special_123 and verify no error message
                start_time = time.time()
                enter_name = "!Special_123"
                template_management.enter_name_in_duplicate_designs(enter_name)
                if template_management.check_for_invalid_character_error_in_duplicate_design():
                    raise Exception("error displayed for valid name")
                duplicate_name = template_management.get_the_default_duplicate_name()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Click "Save" button and verify success
                start_time = time.time()
                template_management.click_on_save_button()
                try:
                    common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
                except:
                    raise Exception("Design has been successfully duplicated. is not displayed")
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 7: Verify copied design in My Designs
                start_time = time.time()
                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("duplicate design window not closed")

                try:
                    full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                        duplicate_name, 1)
                except:
                    raise Exception("duplicate name not found")

                curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

                if int(original_date) != 0:
                    raise Exception("last date displayed for not printed label ")

                if curr_size != original_size or curr_date != original_date:
                    raise Exception("duplicate copy and original copy sizes not matching")

                if int(prev_designs) + 1 != int(curr_designs):
                    raise Exception("showing n designs not updated after copying a design")

                template_management.click_on_delete_button_in_designs()
                template_management.click_on_delete_button_in_designs()
                sleep(2)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46001(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Select and click any of the design.\n-Verify "Copy to My Designs" option is clickable'],
            5: [5, 'Click "Copy to My Designs"'],
            6: [6, 'Verify toast alert "(design name) has been successfully copied to your workspace." is displayed'],
            7: [7, 'Go to My Designs. Select and click the copied design'],
            8: [8,
                'Click "Rename"\na. Verify "Edit name" window is displayed\nb. Verify default value matches the design\'s name'],
            9: [9, 'Input unique name.\n-Verify no error message is displayed'],
            10: [10,
                 'Click "Save" button.\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, no Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            for text in temp[1::4]:
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing")
                prev_designs = template_management.get_showing_n_designs_number()
                #
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select Address category
                start_time = time.time()
                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Select and click any of the design, verify "Copy to My Designs" option is clickable
                start_time = time.time()
                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
                name = names[0]
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Click "Copy to My Designs"
                start_time = time.time()
                template_management.click_on_copy_to_my_designs()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Verify toast alert is displayed
                start_time = time.time()
                try:
                    common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
                except:
                    raise Exception("design copied successfully is not displayed. is not displayed")
                sleep(2)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 7: Go to My Designs and select the copied design
                start_time = time.time()
                template_management.click_left_arrow()
                try:
                    login_page.click_Menu_HamburgerICN()
                except:
                    template_management.click_left_arrow()
                    login_page.click_Menu_HamburgerICN()
                #
                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing")

                original_copy = name + " copy"

                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 8: Click "Rename" and verify "Edit name" window is displayed with default value
                start_time = time.time()
                prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

                template_management.click_on_rename_button()

                default_value = template_management.get_the_default_rename_text()
                if default_value != original_copy:
                    raise Exception("default value not matches the design's name")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 9: Input unique name and verify no error message is displayed
                start_time = time.time()
                new_name = "somenamemyown45941"

                template_management.enter_text_in_rename_design(new_name)
                if template_management.check_error_for_invalid_characters_in_rename_design():
                    raise Exception("error displayed for valid characters")
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 10: Click "Save" button and verify changes
                start_time = time.time()
                template_management.click_on_save_button_in_rename_design()

                try:
                    common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
                except:
                    raise Exception("design has been successfully renamed. is not displayed")

                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("rename popup not closed")
                sleep(1)
                try:
                    sleep(2)
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(new_name, 1)
                except:
                    raise Exception("design not found after updating")
                print("full name", full_name)
                curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

                if curr_size != prev_size:
                    raise Exception("size is not matching after renaming the design")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46002(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Select and click any of the design.\n-Verify "Copy to My Designs" option is clickable'],
            5: [5, 'Click "Copy to My Designs"'],
            6: [6, 'Verify toast alert "(design name) has been successfully copied to your workspace." is displayed'],
            7: [7, 'Go to My Designs. Select and click the copied design'],
            8: [8,
                'Click "Duplicate"\na. Verify "Duplicate design" window is displayed\nb. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)'],
            9: [9, 'Input unique name.\n-Verify no error message is displayed'],
            10: [10,
                 'Click "Save" button.\na. Verify "Duplicate name" window is closed\nb. Verify toast alert "design has been successfully duplicated." is displayed\nc. Verify the duplicate design is displayed with correct name (Name used in step 9)\nd. Verify the duplicate design\'s elements and information (Size, Thumbnail, no Last Print) matches the original design\ne. Verify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nf. Verify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Common Designs
            start_time = time.time()
            for text in temp:
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing")
                prev_designs = template_management.get_showing_n_designs_number()
                #
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Select  category
                start_time = time.time()
                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 4: Select and click any of the design, verify "Copy to My Designs" option is clickable
                start_time = time.time()
                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
                name = names[0]
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 5: Click "Copy to My Designs"
                start_time = time.time()
                template_management.click_on_copy_to_my_designs()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 6: Verify toast alert is displayed
                start_time = time.time()
                try:
                    common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
                except:
                    raise Exception("design copied successfully is not displayed. is not displayed")
                sleep(2)
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 7: Go to My Designs and select the copied design
                start_time = time.time()
                template_management.click_left_arrow()
                try:
                    login_page.click_Menu_HamburgerICN()
                except:
                    template_management.click_left_arrow()
                    login_page.click_Menu_HamburgerICN()
                #
                template_management.click_my_designs_button()
                common_method.wait_for_element_appearance_namematches("Showing")

                n_prev = template_management.get_showing_n_designs_number()

                original_copy = name + " copy"
                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)
                prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 8: Click "Duplicate" and verify "Duplicate design" window is displayed with default value
                start_time = time.time()
                template_management.click_the_duplicate_button()

                template_management.verify_duplicate_design_window()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 9: Input unique name and verify no error message is displayed
                start_time = time.time()
                """Enter unique name here"""

                unique_name = "uniquename_46002"
                template_management.enter_name_in_duplicate_designs(unique_name)
                if template_management.check_for_invalid_character_error_in_duplicate_design():
                    raise Exception("error displayed for proper unique name")

                duplicate_name = unique_name
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 10: Click "Save" button and verify changes
                start_time = time.time()
                template_management.click_on_save_button()

                try:
                    common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
                except:
                    raise Exception("Design has been successfully duplicated. is not displayed")

                if template_management.check_cancel_button_clickable_in_rename_popup():
                    raise Exception("duplicate design window not closed")
                sleep(1)
                try:
                    d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name,
                                                                                                         0)
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
                if prev_size != curr_size:
                    raise Exception("original copy date or size has been changed")

                n_curr = template_management.get_showing_n_designs_number()
                if int(n_curr) != int(n_prev) + 1:
                    raise Exception("Showing designs count not updated")

                template_management.select_design_in_my_design_by_name_and_return(duplicate_name, 1)
                if not template_management.verify_options_clickable_in_design():
                    raise Exception("some options are not clickable")

                template_management.click_on_delete_button_in_designs()
                template_management.click_on_delete_button_in_designs()
                sleep(2)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46003(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3,
                'Select and click the design in Setup 1. then click "Duplicate"\na. Verify "Duplicate design" window is displayed\nb. Verify "Keep your designs organized by adding a name to your copy below." text is displayed\nc. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nd. Verify "Cancel" and "Save" buttons are clickable'],
            4: [4,
                'Click "Save" button\na. Verify "Duplicate design" window is closed\nb. Verify notification alert "design has been successfully duplicated." is displayed. Click "x" button\nc. Verify the duplicate design is displayed with correct name (ie. design Name copy)\nd. Verify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\ne. Verify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nf. Verify the count in the "Showing x designs" is correct'],
            5: [5,
                'Select and click again the design in Setup 1. then click "Duplicate"\na. Verify "Duplicate design" window is displayed\nb. Verify "Keep your designs organized by adding a name to your copy below." text is displayed\nc. Verify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nd. Verify "Cancel" and "Save" buttons are clickable'],
            6: [6,
                'Click "Save" button\na. Verify toast message show duplicate success\nb. Verify the duplicate label name is : design Name copy(1)'],
            7: [7,
                'Go to Common Designs. Select and click category and the design in Setup 2.\nthen click "Copy to My Designs"\na. Verify "Duplicate design" window is displayed\nb. Verify "Keep your designs organized by adding a name to your copy below." text is displayed\nc. Verify default value matches the design\'s name with appended text "copy". (ie. Address copy)\nd. Verify "Cancel" and "Save" buttons are clickable'],
            8: [8,
                'Click "Save" button\na. Verify "Duplicate design" window is closed\nb. Verify notification alert "design has been successfully duplicated." is displayed. Click "x" button\nc. Verify the duplicate design is displayed with correct name (ie. Address copy)\nd. Verify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\ne. Verify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nf. Verify the count in the "Showing x designs" is correct'],
            9: [9,
                'Select and click again the design in Setup 2. then click "Duplicate"\na. Verify "Duplicate design" window is displayed\nb. Verify "Keep your designs organized by adding a name to your copy below." text is displayed\nc. Verify default value matches the design\'s name with appended text "copy". (ie. Address copy)\nd. Verify "Cancel" and "Save" buttons are clickable'],
            10: [10,
                 'Click "Save" button\na. check toast message show that label has been successfully copied to your workspace\nb. go to the my design, check the copied name :Address copy(1)']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select and click the design in Setup 1. then click "Duplicate"
            start_time = time.time()
            n_prev = template_management.get_showing_n_designs_number()
            """Pass the existing name design here"""
            name = template_management.get_normal_design_if_there_in_first_screen_my_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click "Save" button
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select and click again the design in Setup 1. then click "Duplicate"
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click "Save" button
            start_time = time.time()
            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            sleep(1)

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(
                    duplicate_name + " (1)", 0)
            except:
                raise Exception("duplicate name not found after duplicating again")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Go to Common Designs. Select and click category and the design in Setup 2. then click "Copy to My Designs"
            start_time = time.time()
            text = "Address"
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            prev_designs = template_management.get_showing_n_designs_number()
            #
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)
            template_management.click_element_name_matches_all(text, 0)

            template_management.wait_until_designs_load_after_clicking_categories()
            t = template_management.get_first_design_in_my_designs()
            template_management.click_element_by_name_or_text(t)
            names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
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

            n_prev = template_management.get_showing_n_designs_number()

            original_copy = name + " copy"
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

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Click "Save" button
            start_time = time.time()
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

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Select and click again the design in Setup 2. then click "Duplicate"
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 10: Click "Save" button
            start_time = time.time()
            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            sleep(1)

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(
                    duplicate_name + " (1)", 0)
            except:
                raise Exception("duplicate name not found after duplicating again")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45969(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Address category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Address category"
            start_time = time.time()

            text = "Address"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45970(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Barcode category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Barcode category"
            start_time = time.time()

            text = "Barcode"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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

                texts = "Barcode"
                template_management.search_designs(texts, 1)
                template_management.wait_for_element_appearance_name_matches_all(texts)
                template_management.click_element_name_matches_all(texts, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45971(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select File Folder category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select File Folder category"
            start_time = time.time()

            text = "File Folder"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45972(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Jewelry category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Jewelry category"
            start_time = time.time()

            text = "Jewelry"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45973(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Multipurpose category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Multipurpose category"
            start_time = time.time()

            text = "Multipurpose"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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

                texts = "Multipurpose"
                template_management.search_designs(texts, 1)
                template_management.wait_for_element_appearance_name_matches_all(texts)
                template_management.click_element_name_matches_all(texts, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45974(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Name tag category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Name tag category"
            start_time = time.time()

            text = "Name tag"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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

                texts = "Name tag"
                template_management.search_designs(texts, 1)
                template_management.wait_for_element_appearance_name_matches_all(texts)
                template_management.click_element_name_matches_all(texts, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45975(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Shipping category'],
            3: [3, 'Select any of the design then click "Copy to My Designs"'],
            4: [4,
                'Type in unique name for the design. Click "Save"\nVerify toast alert "design name has been successfully copied to your workspace." is displayed'],
            5: [5,
                'Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design\'s elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no "Last Print" date information displayed'],
            6: [6,
                'Select the design. Click "Print"\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)'],
            7: [7,
                'Click "Print" button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated'],
            8: [8,
                'Click Print "Back" button\na. Verify My Designs view is visible\nb. Verify the design\'s "Last Print" information is updated to the current date'],
            9: [9,
                'Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to Common Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select Shipping category"
            start_time = time.time()

            text = "Shipping"
            template_management.search_designs(text, 1)
            template_management.wait_for_element_appearance_name_matches_all(text)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select any of the design then click 'Copy to My Designs'"
            start_time = time.time()

            template_management.click_element_name_matches_all(text, 0)

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
                template_management.search_designs(text, 1)
                template_management.wait_for_designs_in_comm_design()
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
                original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Type in unique name for the design. Click 'Save'\nVerify toast alert 'design name has been successfully copied to your workspace.' is displayed"
                start_time = time.time()
                """4. Type in unique name for the design. Click "Save"
                           this step is not applicable """
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Go to My Designs\na. Verify the copied design is displayed with correct name (ie. design Name copy)\nb. Verify the copied design's elements and information (Size, Thumbnail) matches the Zebra design\nc. Verify there is no 'Last Print' date information displayed"
                start_time = time.time()

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
                    full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy",
                                                                                                       1)
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

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Select the design. Click 'Print'\nVerify Print page is displayed\nTake a note of number of labels left (x labels left)"
                start_time = time.time()

                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                    template_management.scroll_till_print_enabled()
                except:
                    raise Exception("print page is not displayed properly")

                prev_count = template_management.get_no_of_labels_left_in_print_page()
                if not template_management.check_print_button_clickable:
                    raise Exception("print option is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Click 'Print' button\na. Verify 1 label with correct output is printed\nb. Verify the number of labels left (x labels left) is updated"
                start_time = time.time()

                template_management.click_print_button_enabled()

                try:
                    template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
                    sleep(3)
                except:
                    pass

                common_method.wait_for_element_appearance_enabled("Print")

                curr_count = template_management.get_no_of_labels_left_in_print_page()

                if not int(prev_count) == int(curr_count) + 1:
                    raise Exception("no of labels not updated")

                sleep(3)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step8: "Click Print 'Back' button\na. Verify My Designs view is visible\nb. Verify the design's 'Last Print' information is updated to the current date"
                start_time = time.time()

                template_management.click_left_arrow()
                if not template_management.check_element_exists("My Designs"):
                    template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                sleep(2)

                template_management.check_element_exists("My Designs")

                full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)

                pd, pm, py = template_management.get_design_last_print_date(full_name)

                cd, cm, cy = template_management.get_current_date()
                if pd != cd or pm != cm or py != cy:
                    raise Exception("dates are not matching")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step9: "Go to Home > Recently Printed Designs\nVerify the total number of labels left (x of x prints left) is updated in the Printer information"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                sleep(1)

                labels_left = template_management.get_no_of_left_cartridge()
                if str(labels_left) != str(curr_count):
                    raise Exception("labels left not updated")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45912(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to My Designs'],
            3: [3,
                'Select the design mentioned in setup 2, click on Print option. Check Print page is displayed. Check the design\'s elements are displayed in the print preview. Check there are 2 input controls (Text, Date)'],
            4: [4, 'Go to the text input control. Check the text initial value is displayed as the default.'],
            5: [5,
                'Clear the value on the text input control. Verify the cleared text is no longer displayed in the print preview. Verify the text prompt value is displayed in the input control'],
            6: [6,
                'Type in new text in the input control. Verify the prompt value is automatically cleared upon typing the first character of the new text. Verify the new text is displayed in the print preview. Verify letters, numbers, special characters can be entered. Verify next line can be entered'],
            7: [7, 'Go to the date input control. Verify the date initial value is displayed as the default'],
            8: [8,
                'Clear the value on the input control. Verify the cleared date is no longer displayed in the print preview. Verify the date prompt value is displayed in the input control'],
            9: [9,
                'Type in new date in the input control. Verify the prompt value is automatically cleared upon typing the first character of the new date. Verify the new date is displayed in the print preview. Verify only correct date format can be entered'],
            10: [10,
                 'Select date from the date picker. Verify the selected date is displayed in the input control. Verify the selected date is displayed in the print preview'],
            11: [11, 'Check only the printers registered to the user are displayed in the Printer\'s list options'],
            12: [12, 'Click "Print" button. Verify 1 label with correct output is printed'],
            13: [13, 'In Print window, verify the number of labels left (x labels left) is updated'],
            14: [14,
                 'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date'],
            15: [15,
                 'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated on Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to My Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select the design and click Print option, verify print page and elements
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            name = "45912"
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                sleep(3)
            except:
                raise Exception("print page not displayed properly")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Check text input control initial value
            start_time = time.time()
            initial_text = "Sample123"

            curr_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if initial_text != curr_text:
                raise Exception("initial text not matching")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Clear text input control value and verify
            start_time = time.time()
            template_management.input_text_in_element_by_name("android.widget.EditText", "", 0)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if curr_text != "":
                raise Exception("text did not change")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Type in new text in the input control and verify
            start_time = time.time()
            template_management.click_element_by_name_or_text("android.widget.EditText", 0)
            new_text = "new text"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 0)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if curr_text != new_text:
                raise Exception("text did not change")

            new_text = "new 123@gmai\n.com"

            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 0)
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Verify date input control initial value
            start_time = time.time()
            curr_date = template_management.get_the_date_from_print_page()
            if curr_date != "11/11/2021":
                raise Exception("initial date is not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Clear date input control value and verify
            start_time = time.time()
            now_date = template_management.get_current_date_in_mm_dd_yy_format()
            cur_d = now_date.split("/")
            print(cur_d)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Type in new date in the input control and verify
            start_time = time.time()
            template_management.set_new_date_in_print_page(int(cur_d[1]))
            sleep(1)
            try:
                template_management.click_on_cancel_button_in_rename_popup()
            except:
                pass

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 10: Select date from date picker and verify
            start_time = time.time()
            curr_date = template_management.get_the_date_from_print_page()
            changing_date = str(template_management.get_in_proper_dd_mm_yy_format())
            if curr_date != changing_date:
                raise Exception("changed date is not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 11: Check only registered printers are displayed in Printer's list
            start_time = time.time()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 12: Click "Print" button and verify print output
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 13: Verify number of labels left is updated
            start_time = time.time()
            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count) + 1:
                raise Exception("no of labels not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 14: Click Print "Back" button, verify My Designs view and Last Print information
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 15: Go to Home > Recently Printed Designs, verify total number of labels left
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45913(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Recently Printed labels'],
            3: [3,
                'Select the design mentioned in setup 2, click on Print option. Check Print page is displayed. Check the design\'s elements are displayed in the print preview. Check there are 3 input controls (Number, Barcode, Image)'],
            4: [4, 'Go to the number input control. Verify the number initial value is displayed as the default.'],
            5: [5,
                'Clear the value on the number input control. Verify the cleared number is no longer displayed in the print preview. Verify the number prompt value is displayed in the input control'],
            6: [6,
                'Type in new number in the input control. Verify the prompt value is automatically cleared upon typing the first character of the new number. Verify the new number is displayed in the print preview. Verify only numbers can be entered'],
            7: [7, 'Go to the barcode input control. Verify the barcode initial value is displayed as the default'],
            8: [8,
                'Clear the value on the barcode input control. Verify the cleared barcode is no longer displayed in the print preview. Verify the barcode prompt value is displayed in the input control'],
            9: [9,
                'Input new barcode in the input control. Verify the prompt value is automatically cleared. Verify the new barcode is displayed in the print preview'],
            10: [10, 'Go to the image input control. Check the default placeholder is "Choose an option"'],
            11: [11, 'Upload one picture from local. Check the image shows correctly on preview'],
            12: [12, 'Click "Print" button. Verify 1 label with correct output is printed and the labels left minus 1'],
            13: [13,
                 'Click Print "Back" button. Verify Recently Printed Labels view is visible. Verify the design\'s "Last Print" information is updated to the current date']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])
        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to Recently Printed labels
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Select the design and click Print option, verify print page and elements
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            name = "45913"
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                sleep(3)
            except:
                raise Exception("print page not displayed")

            template_management.check_element_exists("android.widget.EditText", 0)
            template_management.check_element_exists("android.widget.EditText", 1)
            template_management.check_element_exists("Picture\nicon\nChoose an option", 0)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Check number input control initial value
            start_time = time.time()
            initial_text = template_management.get_text_from_element("android.widget.EditText", 1)
            if initial_text != "123":
                raise Exception("initial_text not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Clear number input control value and verify
            start_time = time.time()
            template_management.click_element_by_name_or_text("android.widget.EditText", 1)
            template_management.input_text_in_element_by_name("android.widget.EditText", "", 1)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 1)
            if curr_text:
                raise Exception("blank value not accepted")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Type in new number in the input control and verify
            start_time = time.time()
            new_text = "4567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 1)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 1)
            if curr_text != new_text:
                raise Exception("new text not updated")
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Verify barcode input control initial value
            start_time = time.time()
            initial_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if initial_text != "123456789012":
                raise Exception("initial_text not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Clear barcode input control value and verify
            start_time = time.time()
            template_management.click_element_by_name_or_text("android.widget.EditText", 0)
            template_management.input_text_in_element_by_name("android.widget.EditText", "", 0)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if curr_text:
                raise Exception("blank value not accepted")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Input new barcode in the input control and verify
            start_time = time.time()
            new_text = "1234567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 0)
            curr_text = template_management.get_text_from_element("android.widget.EditText", 0)
            if curr_text != new_text:
                raise Exception("new text not updated")
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 10: Go to the image input control, check default placeholder
            start_time = time.time()
            template_management.click_on_image_input_in_print_page()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 11: Upload one picture from local, check image in preview
            start_time = time.time()
            template_management.upload_image_in_print_page()

            sleep(8)

            template_management.scroll_till_print_enabled_button()
            prev_count = template_management.get_no_of_labels_left_in_print_page()

            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 12: Click "Print" button, verify output and labels left
            start_time = time.time()
            template_management.click_print_button_enabled()
            common_method.wait_for_element_appearance_enabled("Print", 20)
            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete")
            except:
                pass

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count) + 1:
                raise Exception("no of labels not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 13: Click Print "Back" button, verify Recently Printed Labels view and Last Print information
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45914(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design mentioned in setup 2, click Print option. Verify Print page is displayed.'],
            3: [3,
                'Click on the Copies option, check the numeric keypad shows up instead of full keypad. Input 2 in the "Copies" input control. Verify total number of labels for printing (Total of 2 Labels) is correct. Take note of the number of labels left'],
            4: [4, 'Click "Print" button. Verify 2 labels with correct output are printed'],
            5: [5, 'In Print window, verify the number of labels left (x labels left) is updated'],
            6: [6,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date'],
            7: [7,
                'Select again the design and select print option. Verify the number of labels left (x labels left) (same count in step 5)'],
            8: [8,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information (same count in step 5).']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design mentioned in setup 2, click Print option. Verify Print page is displayed.
            start_time = time.time()
            name = "45914"
            common_method.wait_for_element_appearance_namematches("Showing")
            full_name = template_management.select_design_in_my_design_by_name_and_return(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                sleep(3)
            except:
                raise Exception("print page not displayed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click on the Copies option, check the numeric keypad shows up instead of full keypad. Input 2 in the "Copies" input control. Verify total number of labels for printing (Total of 2 Labels) is correct. Take note of the number of labels left
            start_time = time.time()
            template_management.click_on_copies()
            try:
                template_management.wait_for_element_appearance_name_matches_all("keyboard")
            except:
                raise Exception("key board is not present")
            prev_copies = template_management.get_no_of_copies()
            prev_labels = template_management.get_no_of_labels_left_in_print_page()
            template_management.click_element_by_name_or_text("android.widget.EditText", 0)

            template_management.input_text_in_element_by_name("android.widget.EditText", "2", 0)
            others.go_back()

            curr_copies = template_management.get_no_of_copies()
            if str(curr_copies) != '2':
                raise Exception("curr copies not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click "Print" button. Verify 2 labels with correct output are printed
            start_time = time.time()
            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: In Print window, verify the number of labels left (x labels left) is updated
            start_time = time.time()
            common_method.wait_for_element_appearance_enabled("Print")
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            temp = curr_labels
            if int(prev_labels) != int(curr_labels) + 2:
                raise Exception("no of labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Select again the design and select print option. Verify the number of labels left (x labels left) (same count in step 5)
            start_time = time.time()
            try:
                template_management.click_print_button()
            except:
                others.scroll_down()
                template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)
                template_management.click_print_button()

            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")
            sleep(2)
            curr_labels = template_management.get_no_of_labels_left_in_print_page()

            if curr_labels != temp:
                raise Exception("count not same after re selecting the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information (same count in step 5)
            start_time = time.time()
            template_management.click_left_arrow()
            try:
                template_management.check_element_exists("My Designs")
            except:
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()

            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()

            if str(labels_left) != str(curr_labels):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45915(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design mentioned on setup 2, and click Print option. Verify Print page is displayed.'],
            3: [3, 'Input data to each element'],
            4: [4,
                'Input 3 in the "Copies" input control. Check the cursor is located at "Copies" input box after clicking it, will not locate on the element input box. Verify total number of labels for printing (Total of 3 Labels) is correct. Take note of the number of labels left.'],
            5: [5,
                'Click "Print" button. Verify 3 labels with correct output are printed. Verify toast alert "Print job sent" is displayed.'],
            6: [6, 'In Print window, verify the number of labels left (x labels left) is updated.'],
            7: [7,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date.'],
            8: [8,
                'Select again the design and click print option. Verify the number of labels left (x labels left) (same count in step 6).'],
            9: [9,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information (same count in step 6).'],
            10: [10, 'Repeat steps for design in Recently Printed Designs section']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design mentioned on setup 2, and click Print option. Verify Print page is displayed.
            start_time = time.time()
            template_management.wait_for_element_appearance_name_matches_all("Showing")
            name = "45913"
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                pass

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input data to each element
            start_time = time.time()
            template_management.click_element_by_name_or_text("android.widget.EditText", 1)

            new_text = "4567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 1)

            others.go_back()
            template_management.click_element_by_name_or_text("android.widget.EditText", 0)

            new_text = "1234567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 0)

            others.go_back()
            template_management.click_on_image_input_in_print_page()
            template_management.upload_image_in_print_page()
            sleep(8)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Input 3 in the "Copies" input control. Check the cursor is located at "Copies" input box after clicking it, will not locate on the element input box. Verify total number of labels for printing (Total of 3 Labels) is correct. Take note of the number of labels left.
            start_time = time.time()
            prev_labels = template_management.get_no_of_labels_left_in_print_page()

            template_management.click_on_copies()
            if not template_management.check_copies_focused():
                raise Exception("cursor is not in copies")
            template_management.enter_no_of_copies(3)
            others.go_back()

            curr_copies = template_management.get_no_of_copies()

            if str(curr_copies) != '3':
                raise Exception("curr copies not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click "Print" button. Verify 3 labels with correct output are printed. Verify toast alert "Print job sent" is displayed.
            start_time = time.time()
            template_management.scroll_till_print_enabled_button()
            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete")
            except:
                pass

            common_method.wait_for_element_appearance_enabled("Print")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: In Print window, verify the number of labels left (x labels left) is updated.
            start_time = time.time()
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            temp = curr_labels
            if int(prev_labels) != int(curr_labels) + 3:
                raise Exception("no of labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date.
            start_time = time.time()
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
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Select again the design and click print option. Verify the number of labels left (x labels left) (same count in step 6).
            start_time = time.time()
            template_management.get_the_full_name_of_design_and_click_in_my_design(name)
            try:
                template_management.click_print_button()
            except:
                others.scroll_down()
                template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)
                template_management.click_print_button()

            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                pass
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            if curr_labels != temp:
                raise Exception("count not same after reselecting the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information (same count in step 6).
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            #step 10:
            start_time = time.time()

            """For recently printed Labels"""

            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                sleep(3)
            except:
                raise Exception("print page not displayed")

            template_management.click_element_by_name_or_text("android.widget.EditText", 1)

            new_text = "4567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 1)

            others.go_back()
            template_management.click_element_by_name_or_text("android.widget.EditText", 0)

            new_text = "1234567890"
            template_management.input_text_in_element_by_name("android.widget.EditText", new_text, 0)

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

            curr_copies = template_management.get_no_of_copies()

            if str(curr_copies) != '3':
                raise Exception("curr copies not updated")

            template_management.scroll_till_print_enabled_button()
            template_management.click_print_button_enabled()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")

            common_method.wait_for_element_appearance_enabled("Print")
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            temp = curr_labels
            if int(prev_labels) != int(curr_labels) + 3:
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
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            try:
                template_management.click_print_button()
            except:
                others.scroll_down()
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
                template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            if curr_labels != temp:
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

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45916(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design and click Print option. Check Print page is displayed. Check there is a prompt message like "! Label Is Different Size Than Cartridge Resize the label or insert a different cartridge into the printer. Otherwise, the label output may not be as expected"'],
            3: [3,
                'Input 1 in the "Copies" input control. Verify total number of labels for printing (Total of 1 Labels) is correct. Take note of the number of labels left.'],
            4: [4, 'Click "Print" button. Verify 1 label with correct output is printed.'],
            5: [5, 'In Print window, verify the number of labels left (x labels left) is updated.'],
            6: [6,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date.'],
            7: [7,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information.'],
            8: [8,
                'Go to My designs, select the design mentioned on setup 3. Click Print option. Check the Print page pops up. Check there is no prompt message for telling different size.'],
            9: [9, 'Click Print option. Check the label printed out correctly.']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Print option. Check Print page is displayed. Check there is a prompt message like "! Label Is Different Size Than Cartridge Resize the label or insert a different cartridge into the printer. Otherwise, the label output may not be as expected"
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('2.25" x 0.5"')
            a = template_management.get_names_of_design_in_search_designs([full_name])[0]

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")
            if not template_management.check_prompt_for_smaller_label_than_current():
                raise Exception("Prompt for smaller page is not displayed or may have wrong words")

            prev_labels = template_management.get_no_of_labels_left_in_print_page()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input 1 in the "Copies" input control. Verify total number of labels for printing (Total of 1 Labels) is correct. Take note of the number of labels left.
            start_time = time.time()
            template_management.click_on_copies()

            template_management.enter_no_of_copies(1)
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click "Print" button. Verify 1 label with correct output is printed.
            start_time = time.time()
            template_management.click_print_button_enabled()

            curr_copies = template_management.get_no_of_copies()
            if int(curr_copies) != int('1'):
                raise Exception("current copies are not one")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: In Print window, verify the number of labels left (x labels left) is updated.
            start_time = time.time()
            common_method.wait_for_element_appearance_enabled("Print")
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            temp = curr_labels
            if int(prev_labels) != int(curr_labels) + 1:
                raise Exception("no of labels left not updated")
            sleep(5)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date.
            start_time = time.time()
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            template_management.check_element_exists("My Designs")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(a, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()

            if str(labels_left) != str(curr_labels):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Go to My designs, select the design mentioned on setup 3. Click Print option. Check the Print page pops up. Check there is no prompt message for telling different size.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('3.5" x 1.25"')

            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")

            if template_management.check_prompt_for_smaller_label_than_current():
                raise Exception("Prompt for smaller page is  displayed or may have wrong words")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 9: Click Print option. Check the label printed out correctly.
            start_time = time.time()
            template_management.click_print_button()
            common_method.wait_for_element_appearance_enabled("Print")
            template_management.click_print_button_enabled()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45917(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to My Designs.'],
            2: [2,
                'Select the design and click Print option. Check Print page is displayed. Check there is a prompt message like "! Label Is Different Size Than Cartridge Resize the label or insert a different cartridge into the printer. Otherwise, the label output may not be as expected."'],
            3: [3,
                'Input 1 in the "Copies" input control. Verify total number of labels for printing (Total of 1 Labels) is correct. Take note of the number of labels left.'],
            4: [4, 'Click "Print" button. Verify 1 label with correct output is printed.'],
            5: [5, 'In Print window, verify the number of labels left (x labels left) is updated.'],
            6: [6,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date.'],
            7: [7,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information.'],
            8: [8,
                'Go to My designs, select the design mentioned on setup 3. Click Print option. Check the Print page pops up. Check there is no prompt message for telling different size.'],
            9: [9, 'Click Print option. Check the label printed out correctly.']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs.
            start_time = time.time()
            show_message("Connect Dp14 Printer")
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Select the design and click Print option. Check Print page is displayed. Check there is a prompt message about label size.
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('4" x 6"')
            a = template_management.get_names_of_design_in_search_designs([full_name])[0]
            template_management.click_print_button()

            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                sleep(3)
            except:
                raise Exception("print page not displayed")

            if not template_management.check_prompt_for_smaller_label_than_current():
                raise Exception("Prompt for smaller page is not displayed or may have wrong words")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input 1 in the "Copies" input control. Verify total number of labels for printing (Total of 1 Labels) is correct. Take note of the number of labels left.
            start_time = time.time()
            template_management.scroll_till_print_enabled_button()
            prev_labels = template_management.get_no_of_labels_left_in_print_page()

            template_management.click_on_copies()

            template_management.enter_no_of_copies(1)
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click "Print" button. Verify 1 label with correct output is printed.
            start_time = time.time()
            template_management.click_print_button_enabled()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Labels")
                sleep(2)
            except:
                pass
            curr_copies = template_management.get_no_of_copies()
            if str(curr_copies) != '1':
                raise Exception("current copies are not one")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: In Print window, verify the number of labels left (x labels left) is updated.
            start_time = time.time()
            common_method.wait_for_element_appearance_enabled("Print")
            curr_labels = template_management.get_no_of_labels_left_in_print_page()
            temp = curr_labels
            if int(prev_labels) != int(curr_labels) + 1:
                raise Exception("no of labels left not updated")
            sleep(5)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date.
            start_time = time.time()
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            template_management.check_element_exists("My Designs")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(a, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()

            if str(labels_left) != str(curr_labels):
                raise Exception("labels left not updated")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 8: Go to My designs, select the design mentioned on setup 3. Click Print option. Check the Print page pops up. Check there is no prompt message for telling different size.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design('3.5" x 1.25"')
            template_management.click_print_button_enabled()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                sleep(3)
            except:
                raise Exception("print page not displayed")

            if template_management.check_prompt_for_smaller_label_than_current():
                raise Exception("Prompt for smaller page is  displayed or may have wrong words")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 9: Click Print option. Check the label printed out correctly.
            start_time = time.time()
            template_management.scroll_till_print_enabled_button()
            template_management.click_print_button()
            common_method.wait_for_element_appearance_enabled("Print")
            template_management.click_print_button_enabled()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))
        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45918(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to My Designs.'],
            2: [2, 'Select the design and click Print option. Check Print page is displayed.'],
            3: [3, 'Check the printer list. Check only 2 printers in the precondition are available for selection.'],
            4: [4,
                'Select Printer 1. Verify "Print" button is clickable. Verify the number of labels left (x labels left) is correct. Verify total number of labels for printing (Total of 1 Labels) is correct.'],
            5: [5, 'Click "Print" button. Verify 1 label with correct output is printed.'],
            6: [6, 'In Print window, verify the number of labels left (x labels left) is updated.'],
            7: [7,
                'Select Printer 2. Verify "Print" button is clickable. Verify the number of labels left (x labels left) is correct. Verify total number of labels for printing (Total of 1 Labels) is correct.'],
            8: [8, 'Click "Print" button. Verify 1 label with correct output is printed.'],
            9: [9, 'In Print window, verify the number of labels left (x labels left) is updated.'],
            10: [10,
                 'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date.'],
            11: [11,
                 'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer 1 information. Verify the total number of labels left (x of x prints left) is updated in the Printer 2 information.'],
            12: [12,
                 'Select another design and click Print option. Select Printer 1. Verify the total number of labels left (x of x prints left) is correct (matches the number in step 6). Select Printer 2. Verify the total number of labels left (x of x prints left) is correct (matches the number in step 9).']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs.
            start_time = time.time()
            show_message("connect 2 printers DP12 and DP14")
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            all_printer_left_count = template_management.get_no_of_cartridge_left_in_all_printer()
            printer_1_prev_count = all_printer_left_count[0]
            printer_2_prev_count = all_printer_left_count[1]

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Select the design and click Print option. Check Print page is displayed.
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            all_names = template_management.get_ith_design_by_index_in_my_designs(2)
            name = all_names

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label", 15)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check the printer list. Check only 2 printers in the precondition are available for selection.
            start_time = time.time()
            """Printer 1 """
            printers = template_management.select_the_printer_in_print_preview_page_by_index(0, 1)
            print("printers", printers)
            if len(printers) != 2:
                raise Exception("Check only 2 printers in the precondition are available for selection fails")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Select Printer 1 and verify details
            start_time = time.time()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            prev_labels_1 = template_management.get_no_of_labels_left_in_print_page()

            if not template_management.check_element_exists_name_or_text_matches("labels left"):
                raise Exception("labels left not displayed")

            if not template_management.check_element_exists_name_or_text_matches("Total of 1 label"):
                raise Exception(
                    "c. Verify total number of labels for printing (Total of 1 Labels) is correct this step fails")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click "Print" button and verify 1 label with correct output is printed
            start_time = time.time()
            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: In Print window, verify the number of labels left is updated
            start_time = time.time()
            curr_labels_1 = template_management.get_no_of_labels_left_in_print_page()

            if prev_labels_1 - 1 != curr_labels_1:
                raise Exception("prev and curr labels are not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7: Select Printer 2 and verify details
            start_time = time.time()
            """Printer 2"""

            printers = template_management.select_the_printer_in_print_preview_page_by_index(1, 0)
            template_management.scroll_till_print_enabled_button()

            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            prev_labels_2 = template_management.get_no_of_labels_left_in_print_page()

            try:
                template_management.check_element_exists_name_or_text_matches("labels left")
            except:
                raise Exception("labels left not displayed")

            try:
                template_management.check_element_exists_name_or_text_matches("Total of 1 label")
            except:
                raise Exception(
                    "c. Verify total number of labels for printing (Total of 1 Labels) is correct this step fails")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 8: Click "Print" button and verify 1 label with correct output is printed
            start_time = time.time()
            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 9: In Print window, verify the number of labels left is updated
            start_time = time.time()
            curr_labels_2 = template_management.get_no_of_labels_left_in_print_page()

            if prev_labels_2 - 1 != curr_labels_2:
                raise Exception("prev and curr labels are not updated")

            sleep(3)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 10: Click Print "Back" button and verify My Designs view
            start_time = time.time()
            template_management.click_left_arrow()
            try:
                template_management.check_element_exists("My Designs")
            except:
                template_management.click_left_arrow()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 11: Go to Home > Recently Printed Designs and verify updates for both printers
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(2)

            template_management.check_element_exists("My Designs")

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            all_printer_left_count = template_management.get_no_of_cartridge_left_in_all_printer()
            printer_1_curr_count = all_printer_left_count[0]
            printer_2_curr_count = all_printer_left_count[1]

            if int(printer_1_curr_count) + 1 != int(printer_1_prev_count):
                raise Exception("labels left not updated in printer 1")

            if int(printer_2_curr_count) + 1 != int(printer_2_prev_count):
                raise Exception("labels left not updated in printer 2")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 12: Select another design and verify printer details
            start_time = time.time()
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

            printers = template_management.select_the_printer_in_print_preview_page_by_index(1, 0)

            curr_labels_2_a = template_management.get_no_of_labels_left_in_print_page()

            if curr_labels_2 != curr_labels_2_a:
                raise Exception("curr labels are not updated after selecting other designs")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45919(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click Duplicate option'],
            3: [3, 'Check the "Duplicate Design" dialog pops up. Check the default name is "design name copy"'],
            4: [4, 'Click save with the default name. Check the duplicated design shows in My Designs'],
            5: [5,
                'Select the duplicated design and click Print option. Verify the design\'s name is displayed at the top of the page with "Back" button. Verify the design\'s elements are displayed in the print preview. Verify label count (Label 1 of 1) is displayed below the image. Verify there are no controls to input data. Verify number of copies to be printed can be entered. Default quantity is 1. Take a note of current prints left'],
            6: [6,
                'Click "Print" button. Verify 1 label with correct output is printed. In Print window, verify the number of labels left (x labels left) is updated'],
            7: [7,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date'],
            8: [8,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition, click Duplicate option
            start_time = time.time()
            t = template_management.get_first_design_in_my_designs()
            original_name = template_management.get_names_of_design_in_search_designs([t])[0]
            template_management.get_the_full_name_of_design_and_click_in_my_design(original_name)

            duplicate_name = template_management.duplicate_the_design_and_get_the_name()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Check the "Duplicate Design" dialog pops up. Check the default name is "design name copy"
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("successfully")
            if original_name + " copy" != duplicate_name:
                raise Exception("default duplicate name is not changing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click save with the default name. Check the duplicated design shows in My Designs
            start_time = time.time()
            duplicate_name = original_name + " copy"
            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")

            try:
                common_method.wait_for_element_appearance_namematches(duplicate_name)
            except:
                raise Exception("name does not match")

            if not template_management.check_element_exists("Label 1 of 1"):
                raise Exception("Label 1 of 1 not displayed")

            try:
                template_management.check_element_exists("android.widget.EditText", 1)
            except:
                pass

            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the duplicated design and click Print option. Verify various elements on Print page
            start_time = time.time()
            template_management.click_print_button()
            try:
                template_management.wait_for_element_appearance_name_matches_all("Print complete")
            except:
                pass

            prev_copies = template_management.get_no_of_copies()

            if not template_management.check_element_exists_name_or_text_matches("labels left"):
                raise Exception("labels left not displayed")

            curr_copies = template_management.get_no_of_copies()

            if prev_copies != curr_copies:
                raise Exception("prev and curr copies are not same")

            template_management.check_element_exists("Total of 1 label")

            prev_count = template_management.get_no_of_labels_left_in_print_page()
            if not template_management.check_print_button_clickable:
                raise Exception("print option is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click "Print" button. Verify 1 label with correct output is printed. In Print window, verify the number of labels left (x labels left) is updated
            start_time = time.time()
            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_namematches("Label")
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("Print page dint shown up")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count) + 1:
                raise Exception("no of labels not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            print(labels_left, curr_count)
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45920(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click print option. Check the print page pops up'],
            3: [3,
                'Input "C31:C43\'<>,.?£€)" to the input control. Verify the value entered is displayed in the print preview'],
            4: [4, 'Take a note of current number of labels left (x labels left)'],
            5: [5,
                'Click "Print" button. Verify 1 label with correct output is printed. In Print window, verify the number of labels left (x labels left) is updated'],
            6: [6,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is updated to the current date'],
            7: [7,
                'Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition, click print option. Check the print page pops up
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            name = "45912"
            template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input "C31:C43'<>,.?£€)" to the input control. Verify the value entered is displayed in the print preview
            start_time = time.time()
            try:
                template_management.click_element_by_name_or_text("Cancel")
            except:
                pass

            template_management.click_element_by_name_or_text("android.widget.EditText", 0)
            template_management.enter_the_special_characters_in_print_page("C31:C43'<>,.?£€)")
            a = template_management.get_text_from_element("android.widget.EditText", 0)
            if a != "C31:C43'<>,.?£€)":
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Take a note of current number of labels left (x labels left)
            start_time = time.time()
            prev_count = template_management.get_no_of_labels_left_in_print_page()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click "Print" button. Verify 1 label with correct output is printed. In Print window, verify the number of labels left (x labels left) is updated
            start_time = time.time()
            template_management.click_print_button()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")

            try:
                common_method.wait_for_element_appearance_namematches("Label", 10)
                template_management.scroll_till_print_enabled_button()
            except:
                raise Exception("print page not displayed properly")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            if not int(prev_count) == int(curr_count) + 1:
                raise Exception("no of labels not updated")

            sleep(1)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is updated to the current date
            start_time = time.time()
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

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            pd, pm, py = template_management.get_design_last_print_date(full_name)

            cd, cm, cy = template_management.get_current_date()
            if pd != cd or pm != cm or py != cy:
                raise Exception("dates are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Go to Home > Recently Printed Designs. Verify the total number of labels left (x of x prints left) is updated in the Printer information
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            print(labels_left, curr_count)
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45923(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click print option. Check the print page pops up'],
            3: [3, 'Take note of the number of labels left'],
            4: [4,
                'Click Print "Back" button. Verify My Designs view is visible. Verify the design\'s "Last Print" information is NOT updated'],
            5: [5,
                'Select again the design and click Print option. Verify Print page is displayed. Click "Print" button. Verify the number of labels left (x labels left) is the same as in step 3'],
            6: [6,
                'Go to Home page. Verify the total number of labels left (x of x prints left) is NOT updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition, click print option. Check the print page pops up
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]

            template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Take note of the number of labels left
            start_time = time.time()
            prev_count = template_management.get_no_of_labels_left_in_print_page()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Print "Back" button. Verify My Designs view is visible. Verify the design's "Last Print" information is NOT updated
            start_time = time.time()
            template_management.click_left_arrow()
            if not template_management.check_element_exists("My Designs"):
                template_management.click_left_arrow()

            template_management.check_element_exists("My Designs")

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 0)

            try:
                template_management.get_design_last_print_date(full_name)
                raise Exception("last print updated")
            except ZeroDivisionError:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select again the design and click Print option. Verify Print page is displayed. Click "Print" button. Verify the number of labels left (x labels left) is the same as in step 3
            start_time = time.time()
            template_management.get_the_full_name_of_design_and_click_in_my_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")

            curr_count = template_management.get_no_of_labels_left_in_print_page()
            if prev_count != curr_count:
                raise Exception("print label updated without printing")

            template_management.click_print_button_enabled()
            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()

            sleep(5)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to Home page. Verify the total number of labels left (x of x prints left) is NOT updated in the Printer information
            start_time = time.time()
            template_management.click_left_arrow()
            try:
                template_management.check_element_exists("My Designs")
            except:
                template_management.click_left_arrow()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            sleep(1)

            labels_left = template_management.get_no_of_left_cartridge()
            print(labels_left, curr_count)
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45924(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click print option. Check the print page pops up'],
            3: [3, 'Take note of the number of labels left'],
            4: [4,
                'Click Print "Back" button. Verify Recently Printed Labels view is visible. Verify the design\'s "Last Print" information is NOT updated'],
            5: [5,
                'Select again the design and click Print option. Verify Print page is displayed. Click "Print" button. Verify the number of labels left (x labels left) is the same as in step 3'],
            6: [6,
                'Go to Home page. Verify the total number of labels left (x of x prints left) is NOT updated in the Printer information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition, click print option. Check the print page pops up
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]

            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Take note of the number of labels left
            start_time = time.time()
            prev_count = template_management.get_no_of_labels_left_in_print_page()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Print "Back" button. Verify Recently Printed Labels view is visible. Verify the design's "Last Print" information is NOT updated
            start_time = time.time()
            template_management.click_left_arrow()
            if not template_management.check_element_exists("Home"):
                template_management.click_left_arrow()

            template_management.check_element_exists("Home")

            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 0)

            try:
                template_management.get_design_last_print_date(full_name)
                raise Exception("last print updated")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select again the design and click Print option. Verify Print page is displayed. Click "Print" button. Verify the number of labels left (x labels left) is the same as in step 3
            start_time = time.time()
            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name)

            template_management.click_print_button()
            try:
                common_method.wait_for_element_appearance_enabled("Print", 15)
            except:
                raise Exception("print page not displayed")

            curr_count = template_management.get_no_of_labels_left_in_print_page()
            if prev_count != curr_count:
                raise Exception("print label updated without printing")

            template_management.scroll_till_print_enabled_button()
            template_management.click_print_button_enabled()
            template_management.wait_for_element_appearance_name_matches_all("Print complete")
            common_method.wait_for_element_appearance_enabled("Print")

            curr_count = template_management.get_no_of_labels_left_in_print_page()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to Home page. Verify the total number of labels left (x of x prints left) is NOT updated in the Printer information
            start_time = time.time()
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
            print(labels_left, curr_count)
            if str(labels_left) != str(curr_count):
                raise Exception("labels left not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45926(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Rename option\na. Verify "Edit name" window is displayed\nb. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed\nc. Verify default value matches the design\'s name\nd. Verify "Cancel" button is clickable and "Save" button is clickable'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'],
            5: [5, 'Also check entering special characters \\ / can\'t work for rename feature in My design']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to My Designs"
            start_time = time.time()
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """a. Verify "Edit name" window is displayed not in mobile app"""
            """Save" button is NOT clickable (is clickable in mobile)"""

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\na. Verify "Edit name" window is displayed\nb. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed\nc. Verify default value matches the design's name\nd. Verify "Cancel" button is clickable and "Save" button is clickable"
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            """need to automate a. Verify "Edit name" window is displayed
            b. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed"""
            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches the design's name")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            template_management.enter_text_in_rename_design("\/")
            sleep(2)
            if not template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for invalid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Input unique name\nVerify no error message is displayed"
            start_time = time.time()
            new_name = "somenamemyown_45926"

            template_management.enter_text_in_rename_design(new_name)
            sleep(1)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()

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

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Also check entering special characters \\ / can\'t work for rename feature in My design'
            start_time = time.time()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45927(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2,
                'Select the design in the precondition, click Rename option\na. Verify "Edit name" window is displayed\nb. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed\nc. Verify default value matches the design\'s name\nd. Verify "Cancel" button is clickable and "Save" button is clickable'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently", 20)
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\na. Verify "Edit name" window is displayed\nb. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed\nc. Verify default value matches the design's name\nd. Verify "Cancel" button is clickable and "Save" button is clickable"
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches the design's name")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Input unique name\nVerify no error message is displayed"
            start_time = time.time()

            new_name = "ownname"

            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()

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

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45928(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Input name of an existing Zebra design in Common Designs (ie:Address)\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button\nc. Verify design\'s name is updated (Name used in step 3 appended with number (ie: Address(1))'],
            5: [5,
                'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to My Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)

            template_management.click_on_rename_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input name of an existing Zebra design in Common Designs (ie:Address)\nVerify no error message is displayed'
            start_time = time.time()
            new_name = "EAN"

            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button\nc. Verify design\'s name is updated (Name used in step 3 appended with number (ie: Address(1))'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            try:
                full_name = template_management.select_design_in_my_design_by_name_and_return(new_name + " (1)", 0)
            except:
                raise Exception("design not found after updating")

            template_management.select_design_in_my_design_by_name_and_return(new_name + " (1)", 1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"'
            start_time = time.time()
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != new_name + " (1)":
                raise Exception("default value not updated to new value")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            template_management.click_on_cancel_button_in_rename_popup()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45929(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Input name of an existing Zebra design in Common Designs (ie: Basic)\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button\nc. Verify design\'s name is updated (Name used in step 3 appended with number (ie: Basic (1))'],
            5: [5,
                'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed"
            start_time = time.time()
            sleep(2)
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input name of an existing Zebra design in Common Designs (ie: Basic)\nVerify no error message is displayed'
            start_time = time.time()
            new_name = "Basic"

            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button\nc. Verify design\'s name is updated (Name used in step 3 appended with number (ie: Basic (1))'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            try:
                full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(
                    new_name + " (1)", 0)
            except:
                raise Exception("design not found after updating")

            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(new_name + " (1)", 1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"'
            start_time = time.time()
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != new_name + " (1)":
                raise Exception("default value not updated to new value")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            template_management.click_on_cancel_button_in_rename_popup()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45930(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3, 'Input value of an existing design name in user\'s account\nVerify no error message is displayed.'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed.\nb. Verify notification alert "Design successfully renamed to <name>" is displayed. Click "x" button.\nc. Verify design\'s name is updated (Name used in step 3 appended with number (1)).'],
            5: [5,
                'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to My Designs"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\nCheck 'Edit name' window is displayed"
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]

            names = template_management.get_ith_design_by_index_in_my_designs(2)
            names = template_management.get_names_of_design_in_search_designs([names])[0]
            full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(names, 1)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Input value of an existing design name in user's account\nVerify no error message is displayed."
            start_time = time.time()
            template_management.enter_text_in_rename_design(name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Click 'Save' button\na. Verify 'Edit name' window is closed.\nb. Verify notification alert 'Design successfully renamed to <name>' is displayed. Click 'x' button.\nc. Verify design's name is updated (Name used in step 3 appended with number (1))."
            start_time = time.time()

            template_management.click_on_save_button_in_rename_design()
            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(
                    name + " (1)", 0)
            except:
                raise Exception("design not found after updating")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify 'Cancel' and 'Save' buttons are clickable. Click 'Cancel'"
            start_time = time.time()

            template_management.get_the_full_name_of_design_and_click_in_common_design_search(name + " (1)", 1)
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name + " (1)":
                raise Exception("default value not updated to new value")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            template_management.click_on_cancel_button_in_rename_popup()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45931(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3, 'Input value of an existing design name in user\'s account\nVerify no error message is displayed.'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed.\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button.\nc. Verify design\'s name is updated (Name used in step 3 appended with number (1)).'],
            5: [5,
                'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """Give the name of existing design here"""
            sleep(2)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed"
            start_time = time.time()
            name = template_management.get_second_design_in_recently_printed_design()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input value of an existing design name in user\'s account\nVerify no error message is displayed.'
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\na. Verify "Edit name" window is closed.\nb. Verify notification alert "Design successfully renamed to is displayed. Click "x" button.\nc. Verify design\'s name is updated (Name used in step 3 appended with number (1)).'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()
            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    name + " (1)", 0)
            except:
                raise Exception("design not found after updating")

            template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name + " (1)", 1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"'
            start_time = time.time()
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name + " (1)":
                raise Exception("default value not updated to new value")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            template_management.click_on_cancel_button_in_rename_popup()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45932(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option. Check "Edit name" window is displayed'],
            3: [3,
                'Input value of the design name in the precondition from user 2. Verify no error message is displayed'],
            4: [4,
                'Click "Save" button. Verify "Edit name" window is closed. Verify toast alert "design has been successfully renamed." is displayed'],
            5: [5,
                'Verify design\'s name is updated. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            user2_name = template_management.get_first_design_in_my_designs()
            user2_name = template_management.get_names_of_design_in_search_designs([user2_name])[0]

            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            try:
                social_login.wait_for_element_appearance("Sign In", 5)
            except:
                raise Exception("Did not redirect to the login page")
            """Google sign in"""

            login_page.click_loginBtn()
            social_login.wait_for_element_appearance_text("Continue with Google", 10)
            login_page.click_Loginwith_Google()
            try:
                """Enter the email"""
                email = "zebra901.swdvt@gmail.com"
                social_login.choose_a_google_account(email)
            except:
                pass
            common_method.wait_for_element_appearance_namematches("Recently")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition, click Rename option. Check "Edit name" window is displayed
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input value of the design name in the precondition from user 2. Verify no error message is displayed
            start_time = time.time()
            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches the design's name")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")
            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            template_management.enter_text_in_rename_design(user2_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click "Save" button. Verify "Edit name" window is closed. Verify toast alert "design has been successfully renamed." is displayed
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
                sleep(2)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Verify design's name is updated. Verify design's information (Size, Thumbnail, Last Print) are NOT updated
            start_time = time.time()
            try:
                full_name = template_management.select_design_in_my_design_by_name_and_return(user2_name, 0)
            except:
                raise Exception("design not found after updating")

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45933(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Input value of the design name in the precondition from user 2\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'],
            5: [5,
                'Click rename option again, input name with special characters, like "&*%"\nCheck the save button is disabled and there is a prompt message "These characters are not valid."'],
            6: [6, 'Cancel rename\nCheck the name is same as step 3']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            """Note: the design should be printed if not design rename will not be shown in recently printed labels"""

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\nCheck 'Edit name' window is displayed"
            start_time = time.time()

            name = template_management.get_all_designs_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs(name)[0]
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches the design's name")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")
            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Input value of the design name in the precondition from user 2\nVerify no error message is displayed"
            start_time = time.time()

            user2_name = "user2"

            template_management.enter_text_in_rename_design(user2_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error displayed for valid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Click 'Save' button\na. Verify 'Edit name' window is closed\nb. Verify toast alert 'design has been successfully renamed.' is displayed\nc. Verify design's name is updated\nd. Verify design's information (Size, Thumbnail, Last Print) are NOT updated"
            start_time = time.time()

            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
                sleep(2)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")

            try:
                full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(user2_name,
                                                                                                           1)
            except:
                raise Exception("design not found after updating")

            template_management.click_on_rename_button()
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Click rename option again, input name with special characters, like '&*%'\nCheck the save button is disabled and there is a prompt message 'These characters are not valid.'"
            start_time = time.time()

            invalid_name = "&*%"

            template_management.enter_text_in_rename_design(invalid_name)
            sleep(2)
            if not template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not  displayed for invalid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Cancel rename\nCheck the name is same as step 3"
            start_time = time.time()

            template_management.click_on_cancel_button_in_rename_popup()
            try:
                full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(user2_name,
                                                                                                           0)
            except:
                raise Exception("design not found after canceling rename")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45934(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Clear the default value in the input box control\nVerify error message "design name must be at least 1 characters long" is displayed'],
            4: [4,
                'Click "Cancel" button.\na. Verify "Edit name" window is closed.\nb. Verify design\'s name is NOT updated'],
            5: [5,
                'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is NOT clickable'],
            6: [6, 'Input 3 characters (ie.A_1)'],
            7: [7,
                'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "design has been successfully renamed." is displayed. Click "x" button\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'],
            8: [8,
                'Click rename option again, input name with special characters, like "&*%"\nCheck the save button is disabled and there is a prompt message "These characters are not valid."'],
            9: [9,
                'Input only one or several spaces\nCheck spaces should be auto cleared and provide the message "Name must be at least 1 character…"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed"
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Clear the default value in the input box control\nVerify error message "design name must be at least 1 characters long" is displayed'
            start_time = time.time()
            template_management.enter_text_in_rename_design("")
            sleep(2)
            if not template_management.check_error_for_blank_value_in_rename_design():
                raise Exception("error not displayed for blank field")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Cancel" button.\na. Verify "Edit name" window is closed.\nb. Verify design\'s name is NOT updated'
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")

            try:
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
                template_management.click_on_rename_button()
            except:
                raise Exception("design name not found after blank value cancellation")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is NOT clickable'
            start_time = time.time()
            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches with original name")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: 'Input 3 characters (ie.A_1)'
            start_time = time.time()
            new_name = "A_1"
            template_management.enter_text_in_rename_design(new_name)
            sleep(1)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error  displayed for valid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step7: 'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify notification alert "design has been successfully renamed." is displayed. Click "x" button\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")

            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(new_name,
                                                                                                             1)
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step8: 'Click rename option again, input name with special characters, like "&*%"\nCheck the save button is disabled and there is a prompt message "These characters are not valid."'
            start_time = time.time()
            template_management.click_on_rename_button()

            template_management.enter_text_in_rename_design("&*%")
            sleep(2)
            if not template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for invalid characters")

            if template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is enabled for invalid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step9: 'Input only one or several spaces\nCheck spaces should be auto cleared and provide the message "Name must be at least 1 character…"'
            start_time = time.time()

            """. Input only one or several spaces
            Check spaces should be auto cleared and provide the message "Name must be at least 1 character…”  fails"""
            template_management.enter_text_in_rename_design(" ")
            sleep(2)
            if not template_management.check_error_for_blank_value_in_rename_design():
                raise Exception("error not displayed for blank field")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45935(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Input a unique name, click "Cancel" button\na. Verify "Edit name" window is closed\nb. Verify design\'s name is NOT updated'],
            4: [4,
                'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is NOT clickable']
        }

        start_main(execID, leftId["45935"])

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to My Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input a unique name, click "Cancel" button\na. Verify "Edit name" window is closed\nb. Verify design\'s name is NOT updated'
            start_time = time.time()
            new_name = "A_1_1"
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is NOT clickable'
            start_time = time.time()
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("original name changed even after cancellation")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45936(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
            3: [3,
                'Input a unique name, click "Cancel" button\na. Verify "Edit name" window is closed\nb. Verify design\'s name is NOT updated'],
            4: [4,
                'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is clickable']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Recently Printed Labels"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            sleep(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input a unique name, click "Cancel" button\na. Verify "Edit name" window is closed\nb. Verify design\'s name is NOT updated'
            start_time = time.time()
            new_name = "A_1"
            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error  displayed for valid characters")

            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(name,
                                                                                                                 1)
            except:
                raise Exception("design not found after cancelling")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Select again the design and click Rename option\na. Verify default value matches the design\'s name\nb. Verify "Cancel" button is clickable and "Save" button is clickable'
            start_time = time.time()
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("original name changed even after cancellation")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45937(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Address category'],
            3: [3, 'Select any of designs\nVerify "Rename" option is NOT displayed'],

        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        categories_to_check = [
            "Address", "Barcode", "File Folder", "Jewelry", "Multipurpose",
            "Name Badge", "Return Address", "Shipping", "Small Multipurpose"
        ]

        try:
            for text in categories_to_check[4:5]:
                # step1: "Go to Common Designs"
                start_time = time.time()
                stop_app("com.zebra.soho_app")
                start_app("com.zebra.soho_app")
                common_method.wait_for_element_appearance_namematches("Home")

                login_page.click_Menu_HamburgerICN()
                social_login.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step2: 'Select {category} category'
                start_time = time.time()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId["45937"], test_steps[stepId][0], stepId,
                            test_steps[stepId][1], "Pass", exec_time)
                stepId += 1

                # step3: 'Select any of designs\nVerify "Rename" option is NOT displayed'
                start_time = time.time()
                try:
                    template_management.click_on_rename_button()
                    raise Exception("rename button is present")
                except:
                    pass

                template_management.click_left_arrow()
                sleep(1)
                template_management.click_left_arrow()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45938(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Rename option\nVerify "Edit name" window is displayed\nVerify default value matches the design\'s name'],
            3: [3,
                'Input name with special characters (ie: Abc123 + "special characters")\na. Not Allowed special characters: # % & * ? + \\ : / < >\nCheck the Save button is disabled\nVerify error message "These characters are not valid" is displayed and template name is NOT updated\nb. Allowed special characters:  ! @ $ ^ - ~ ( ) _ ` = { } | [ ] ; \' " , . \nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Edit name" window is closed\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to My Designs"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option\nVerify "Edit name" window is displayed\nVerify default value matches the design's name'
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""

            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            template_management.click_on_rename_button()

            default_value = template_management.get_the_default_rename_text()
            if default_value != name:
                raise Exception("default value not matches with original name")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input name with special characters (ie: Abc123 + "special characters")\na. Not Allowed special characters: # % & * ? + \ : / < >\nCheck the Save button is disabled\nVerify error message "These characters are not valid" is displayed and template name is NOT updated\nb. Allowed special characters:  ! @ $ ^ - ~ ( ) _ ` = { } | [ ] ; \' " , . \nVerify no error message is displayed'
            start_time = time.time()
            template_management.enter_text_in_rename_design("Abc123+")
            sleep(2)
            if not template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for invalid characters")

            if template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is enabled for invalid characters")

            template_management.enter_text_in_rename_design("! @ $ ^ - ~ ( ) _  ` = { } | [ ] ; '")
            sleep(2)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for allowed special characters ")

            new_name = "new@_name"
            template_management.enter_text_in_rename_design(new_name)
            sleep(2)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for allowed special characters ")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is disabled for valid special characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Click "Save" button\nVerify "Edit name" window is closed\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design's name is updated\nVerify design's information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("rename popup not closed")

            sleep(3)
            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(new_name, 0)
            except:
                raise Exception("updated name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45940(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Select the design in the precondition, click Rename option'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4, 'Turn off the WiFi connection on the mobile device settings'],
            5: [5,
                'Go back to the Mobile App. Click "Save" button\nVerify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed'],
            6: [6, 'Turn on the WiFi connection on the mobile device settings'],
            7: [7,
                'Go back to the Mobile App. Click "Save" button\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: 'Go to My Designs'
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option'
            start_time = time.time()
            try:
                common_method.wait_for_element_appearance_namematches("Showing")
            except:
                pass
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            name = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            template_management.click_on_rename_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input unique name\nVerify no error message is displayed'
            start_time = time.time()
            new_name = "new@_name_45940"
            template_management.enter_text_in_rename_design(new_name)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for allowed special characters ")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Turn off the WiFi connection on the mobile device settings'
            start_time = time.time()
            template_management.turn_off_wifi()
            sleep(3)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Go back to the Mobile App. Click "Save" button\nVerify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()
            """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error  SMBM-1771"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: 'Turn on the WiFi connection on the mobile device settings'
            start_time = time.time()
            template_management.turn_on_wifi()
            sleep(5)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step7: 'Go back to the Mobile App. Click "Save" button\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            try:
                sleep(3)
                full_name = template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
            except:
                raise Exception("updated name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45941(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2, 'Select the design in the precondition, click Rename option'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4, 'Turn off the WiFi connection on the mobile device settings'],
            5: [5,
                'Go back to the Mobile App. Click "Save" button\nVerify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed'],
            6: [6, 'Turn on the WiFi connection on the mobile device settings'],
            7: [7,
                'Go back to the Mobile App. Click "Save" button\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: 'Go to Recently Printed Labels'
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """Give the name of existing design here"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition, click Rename option'
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            name = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(name, 1)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            template_management.click_on_rename_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Input unique name\nVerify no error message is displayed'
            start_time = time.time()
            new_name = "ne@_name_45941"
            template_management.enter_text_in_rename_design(new_name)
            sleep(2)
            if template_management.check_error_for_invalid_characters_in_rename_design():
                raise Exception("error not displayed for allowed special characters ")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Turn off the WiFi connection on the mobile device settings'
            start_time = time.time()
            template_management.turn_off_wifi()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Go back to the Mobile App. Click "Save" button\nVerify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()
            """Verify connection lost alert "Error communicating with server" with "Cancel" and "Save" buttons is displayed this step has error"""
            common_method.wait_for_element_appearance_namematches("Error communicating with server")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: 'Turn on the WiFi connection on the mobile device settings'
            start_time = time.time()
            template_management.turn_on_wifi()
            sleep(5)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step7: 'Go back to the Mobile App. Click "Save" button\nVerify toast alert "design has been successfully renamed." is displayed\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated'
            start_time = time.time()
            template_management.click_on_save_button_in_rename_design()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            except:
                raise Exception("design has been successfully renamed. is not displayed")

            try:
                full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(new_name, 0)
            except:
                raise Exception("updated name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45976(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Go to "Search" box\nVerify "Search your designs" prompt text and Search icon are displayed'],
            3: [3,
                'Type in text that does not have a match any of the user\'s designs\nVerify Suggestions dropdown is displayed\nVerify "No results for "searched text"" text is displayed\nVerify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then." text is displayed'],
            4: [4,
                'Clear the text in the "Search" box\nVerify Suggestions dropdown is no longer displayed\nVerify all designs are displayed in My Designs\nVerify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to "Search" box and verify "Search your designs" prompt text and Search icon are displayed
            start_time = time.time()
            """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
            template_management.check_search_icon()
            template_management.check_search_designs_text()

            template_management.click_on_search_design()
            """input value that does not match with our current designs"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Type in text that does not match any of the user's designs and verify suggestions
            start_time = time.time()
            not_exists_design = "noexists"
            template_management.search_designs(not_exists_design, 0)
            template_management.wait_for_element_appearance_name_matches_all("results")
            if not template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is not displayed for wrong design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Clear the text in the "Search" box and verify all designs are displayed
            start_time = time.time()
            template_management.search_designs("", 1)
            common_method.wait_for_element_appearance_namematches("Showing")

            """a. Verify Suggestions dropdown is no longer displayed (but suggestions dropdown is displayed)"""

            my_designs_curr = template_management.get_all_designs_in_my_designs()

            n_designs = template_management.get_showing_n_designs_number()
            print(n_designs, len(my_designs_curr))
            if str(len(my_designs_curr)) != str(n_designs):
                raise Exception("total number of designs present , and showing n designs are not same count")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45977(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2, 'Go to "Search" box\nVerify "Search your designs" prompt text and Search icon are displayed'],
            3: [3,
                'Type in text that matches one of the user\'s designs (ie:Address 1)\nVerify Suggestions dropdown is displayed with one design name\nVerify the matched text is in blue font\nVerify the design name is clickable'],
            4: [4,
                'Click the design name\nVerify Suggestions dropdown is no longer displayed\nVerify only the design that matches the search is displayed in the My Designs\nVerify the count in the "Showing 1 designs" is correct'],
            5: [5,
                'Clear the text in the "Search" box\nVerify all designs are displayed in My Designs\nVerify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Go to "Search" box and verify "Search your designs" prompt text and Search icon are displayed
            start_time = time.time()
            my_designs_prev = template_management.get_all_designs_in_my_designs()
            exists_design = template_management.get_names_of_design_in_search_designs(my_designs_prev)[0]
            """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
            template_management.check_search_icon()
            template_management.check_search_designs_text()
            template_management.click_on_search_design()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Type in text that matches one of the user's designs and verify suggestions
            start_time = time.time()
            """input value that does not match with our current designs"""
            template_management.search_designs(exists_design, 0)
            sleep(2)
            template_management.wait_for_suggestions_to_appear()
            if template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is displayed for correct design")

            res = template_management.get_all_search_results_in_search_designs()
            first_design_suggested = res[0]
            try:
                common_method.wait_for_element_appearance_enabled(first_design_suggested)
            except:
                raise Exception("element is not present or not clickable")
            sleep(2)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click the design name and verify only the matched design is displayed
            start_time = time.time()
            template_management.click_element_by_name_or_text(first_design_suggested)

            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                template_management.check_element_exists(first_design_suggested)
                raise Exception("suggestion is shown even after clicking the suggested design")
            except:
                pass

            n = template_management.get_showing_n_designs_number()
            if int(n) != 1:
                raise Exception("showing more than one design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Clear the text in the "Search" box and verify all designs are displayed
            start_time = time.time()
            template_management.search_designs("", 1)
            common_method.wait_for_element_appearance_namematches("Showing")

            my_designs_curr = template_management.get_all_designs_in_my_designs()

            if my_designs_curr != my_designs_prev:
                raise Exception("before and after searching results are not same")

            n_designs = template_management.get_showing_n_designs_number()
            print(n_designs, len(my_designs_curr))
            if str(len(my_designs_curr)) != str(n_designs):
                raise Exception("total number of designs present , and showing n designs are not same count")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45978(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to My Designs.'],
            2: [2, 'Go to "Search" box. Verify "Search your designs" prompt text and Search icon are displayed.'],
            3: [3,
                'Type in keyword in the precondition. Verify Suggestions dropdown is displayed with 6 design names. Verify the matched keyword is in blue font. Verify the design names are clickable.'],
            4: [4,
                'Press keyboard "Search". Verify Suggestions dropdown is no longer displayed. Verify only the designs with names that matches the keyword in step 4 are displayed. Verify the count in the "Showing 6 designs" is correct.'],
            5: [5,
                'Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs.
            start_time = time.time()
            show_message("Add this 6 designs to my designs\n design 1: AddressTest\ndesign 2: AssetTest\ndesign 3: "
                         "GiftTestLabel\ndesign 4: IconGiftTestLabel\ndesign 5: TestStatic\ndesign 6: TestVariable")
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Go to "Search" box. Verify "Search your designs" prompt text and Search icon are displayed.
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            my_designs_prev = template_management.get_all_designs_in_my_designs()

            """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
            template_management.check_search_icon()
            template_management.check_search_designs_text()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Type in keyword in the precondition. Verify Suggestions dropdown is displayed with 6 design names. Verify the matched keyword is in blue font. Verify the design names are clickable.
            start_time = time.time()
            template_management.click_on_search_design()
            """input value that does not match with our current designs"""
            exists_design = "test"
            template_management.search_designs(exists_design, 0)
            sleep(2)
            template_management.wait_for_suggestions_to_appear()

            resu = template_management.get_all_search_results_in_search_designs()

            res = template_management.get_names_of_design_in_search_designs(resu)
            temp = ["AddressTest", "AssetTest", "GiftTestLabel", "IconGiftTestLabel", "TestStatic", "TestVariable"]

            print(res, temp)
            for i in temp:
                if i not in res:
                    raise Exception(i, "not present in suggestions")

            try:
                common_method.wait_for_element_appearance_enabled(resu[-1])
            except:
                raise Exception("element is not present or not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Press keyboard "Search". Verify Suggestions dropdown is no longer displayed. Verify only the designs with names that matches the keyword in step 4 are displayed. Verify the count in the "Showing 6 designs" is correct.
            start_time = time.time()
            keyevent("enter")
            common_method.wait_for_element_appearance_namematches("Showing")

            n = template_management.get_showing_n_designs_number()
            if int(n) != 6:
                raise Exception("not showing 6 design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.
            start_time = time.time()
            template_management.search_designs("", 1)
            common_method.wait_for_element_appearance_namematches("Showing")

            my_designs_curr = template_management.get_all_designs_in_my_designs()

            print("here", my_designs_curr, my_designs_prev)
            if my_designs_curr != my_designs_prev:
                raise Exception("before and after searching results are not same")

            n_designs = template_management.get_showing_n_designs_number()
            print(n_designs, len(my_designs_curr))
            if str(len(my_designs_curr)) != str(n_designs):
                raise Exception("total number of designs present , and showing n designs are not same count")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))
        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45980(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to My Designs.'],
            2: [2, 'Go to "Search" box. Verify "Search your designs" prompt text and Search icon are displayed.'],
            3: [3,
                'Type in "_SG". Verify Suggestions dropdown is displayed with 3 design names. Verify the matched keyword is in blue font. Verify the design names are clickable.'],
            4: [4,
                'Click one of the design in the suggestion list. Verify Suggestions dropdown is no longer displayed. Verify only the selected design is displayed in the My Designs. Verify the count in the "Showing 1 designs" is correct.'],
            5: [5,
                'Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.'],
            6: [6,
                'Type in "~`!@#$%^&*()_-+={}[]|/\\:;\"\'<>,.?" Verify Suggestions window is displayed. Verify "No results for "searched text"" text is displayed. Verify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then." text is displayed.'],
            7: [7,
                'Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs.
            start_time = time.time()
            show_message(
                "There are design names in My Designs with special characters.(ie:Address_SG, Asset_SG, IconGiftLabel_SG)")
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Go to "Search" box. Verify "Search your designs" prompt text and Search icon are displayed.
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            prev_all_designs = template_management.get_all_designs_in_my_designs()

            n_prev = template_management.get_showing_n_designs_number()

            template_management.check_search_icon()
            template_management.check_search_designs_text()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Type in "_SG". Verify Suggestions dropdown is displayed with 3 design names. Verify the matched keyword is in blue font. Verify the design names are clickable.
            start_time = time.time()
            template_management.click_on_search_design()

            """Enter the text here"""
            text = "_SG"
            template_management.search_designs(text, 0)

            template_management.wait_for_suggestions_to_appear()

            resu = template_management.get_all_search_results_in_search_designs()
            if len(resu) != 3:
                raise Exception("more than 3 design is displayed for _SG search")

            for i in resu:
                try:
                    common_method.wait_for_element_appearance_enabled(i)
                except:
                    raise Exception(i, "element is not present or not clickable")

            selected_design = resu[0]
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click one of the design in the suggestion list. Verify Suggestions dropdown is no longer displayed. Verify only the selected design is displayed in the My Designs. Verify the count in the "Showing 1 designs" is correct.
            start_time = time.time()
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
            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != 1:
                raise Exception("Verify the count in the Showing 1 designs is not correct.")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.
            start_time = time.time()
            text = ""
            template_management.search_designs(text, 1)
            common_method.wait_for_element_appearance_namematches("Showing")

            curr_all_designs = template_management.get_all_designs_in_my_designs()

            if prev_all_designs != curr_all_designs:
                raise Exception("prev all designs and curr all designs are not same")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev):
                raise Exception("Showing designs count changed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Type in "~`!@#$%^&*()_-+={}[]|/\\:;\"\'<>,.?" Verify Suggestions window is displayed. Verify "No results for "searched text"" text is displayed. Verify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then." text is displayed.
            start_time = time.time()
            text = "~`!@#$%^&*()_-+={}[]|/\:;\"'<>,.?"
            template_management.search_designs(text, 0)
            social_login.wait_for_element_appearance_namematches_all("No results found.")

            if not template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is not displayed for wrong design")

            text = ""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7: Clear the text in the "Search" box. Verify all designs are displayed in My Designs. Verify the count in the "Showing x designs" is correct.
            start_time = time.time()
            template_management.search_designs(text, 1)
            common_method.wait_for_element_appearance_namematches("Showing")

            curr_all_designs = template_management.get_all_designs_in_my_designs()

            if prev_all_designs != curr_all_designs:
                raise Exception("prev all designs and curr all designs are not same")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev):
                raise Exception("Showing designs count changed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))
        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46006(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Go to the "Search" box.\nVerify "Search designs" text and Search icon are displayed'],
            4: [4,
                'Type in text that does not match any of the Zebra categories and designs.\nVerify the Suggestions dropdown is displayed.\nVerify "No results found." text is displayed.\nVerify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then." text is displayed'],
            5: [5,
                'Clear the text in the "Search" box.\nVerify the Suggestions dropdown is no longer displayed.\nVerify all categories are displayed in Common Designs'],
            6: [6,
                'Input another non-matched keyword, click search button.\nCheck the prompt message is correct:\n"Categories (0)\nNo Categories were found with current filter.\nDesigns (0)\nNo Designs were found with current filter."']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Go to Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Go to the 'Search' box.\nVerify 'Search designs' text and Search icon are displayed"
            start_time = time.time()

            template_management.check_search_icon()
            template_management.check_search_designs_text()
            template_management.click_on_search_design()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Type in text that does not match any of the Zebra categories and designs.\nVerify the Suggestions dropdown is displayed.\nVerify 'No results found.' text is displayed.\nVerify 'Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then.' text is displayed"
            start_time = time.time()

            text = "no_text_match"
            template_management.search_designs(text, 0)
            social_login.wait_for_element_appearance_namematches_all("No results")

            if not template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is not displayed for wrong design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Clear the text in the 'Search' box.\nVerify the Suggestions dropdown is no longer displayed.\nVerify all categories are displayed in Common Designs"
            start_time = time.time()

            text = ""
            template_management.search_designs(text, 1)
            if template_management.check_suggestion_window_in_common_design():
                raise Exception("suggestion window is displayed after entering blank value")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Input another non-matched keyword, click search button.\nCheck the prompt message is correct:\n'Categories (0)\nNo Categories were found with current filter.\nDesigns (0)\nNo Designs were found with current filter.'"
            start_time = time.time()

            template_management.click_on_search_design()
            text = "no_text_matches"
            template_management.search_designs(text, 0)
            social_login.wait_for_element_appearance_namematches_all("No results")

            if not template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is not displayed for wrong design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46007(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Go to the "Search" box.\nVerify "Search common designs" prompt text and Search icon are displayed'],
            4: [4,
                'Enter text matching Zebra category or design. Verify that the dropdown displays two sections: Categories and Designs. Ensure the matched text is in blue, both categories and designs are clickable, and the number of matching designs is shown on the right'],
            5: [5,
                'Press \'Search\'. Verify the Suggestions dropdown disappears and \'Search results (x)\' is shown, where (x) is the total matches. Check \'Categories (x)\' and \'Designs (x)\' are displayed with their respective counts, and ensure matching categories and designs are listed.'],
            6: [6, 'Clear the text in the "Search" box.\nVerify all categories are displayed in Common Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()

            common_method.tearDown()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Go to Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Go to the 'Search' box.\nVerify 'Search common designs' prompt text and Search icon are displayed"
            start_time = time.time()

            template_management.check_search_icon()
            template_management.check_search_designs_text()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Type in text that matches Zebra category and design (i.e., Address)\nVerify Suggestions dropdown displayed the results in 2 sections: Categories and designs\nVerify the matched text is in blue font\nVerify the category and designs are clickable\nVerify on the designs section, the number of designs that matches is displayed on the right side (i.e., Address 1 result)"
            start_time = time.time()

            template_management.click_on_search_design()

            text = "Address"
            template_management.search_designs(text, 0)
            template_management.wait_for_element_appearance_name_matches_all("CATEGORIES")

            if not template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("categories suggestion not displayed or not clickable")
            if not template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("designs suggestion not displayed or not clickable")

            if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                raise Exception(
                    "Verify on the designs section, the number of designs that matches is displayed on the right side (not meeting this step)")

            others.click_enter()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Press keyboard 'Search'\nVerify Suggestions dropdown is no longer displayed\nVerify 'Search results (x)' text is displayed. Count (x) is the total number of categories and designs that match the searched text\nVerify 'Categories (x)' text is displayed. Count (x) is the total number of categories that match the searched text\nVerify the categories that match the searched text are displayed\nVerify 'Designs (x)' text is displayed. Count (x) is the total number of designs that match the searched text\nVerify the designs that match the searched text are displayed"
            start_time = time.time()

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

            temp = template_management.get_all_categories_in_search_designs()
            if not template_management.check_element_present_in_array("Address", temp):
                raise Exception("categories displayed which is not matching to search value")

            try:
                design_count = template_management.get_total_count_designs_results_in_common_designs()
            except:
                raise Exception("Design count is not displayed properly")

            temp = template_management.get_all_designs_in_search_designs()
            if not template_management.check_element_present_in_array("Address", temp):
                raise Exception("designs displayed which is not matching to search value")

            text = ""

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Clear the text in the 'Search' box.\nVerify all categories are displayed in Common Designs"
            start_time = time.time()

            template_management.search_designs(text, 1)

            if template_management.check_suggestion_window_in_common_design():
                raise Exception("suggestion window is displayed after entering blank value")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46008(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Go to the "Search" box.\nVerify "Search common designs" prompt text and Search icon are displayed'],
            4: [4,
                'Type in text that matches Zebra category and does not match any of the Zebra designs (i.e., File Folder)\nVerify Suggestions dropdown displayed the results in 2 sections: Categories and designs\nVerify only the Categories section has displayed results'],
            5: [5,
                'Press keyboard "Search"\nVerify Suggestions dropdown is no longer displayed\nVerify "Search results (x)" text is displayed. Count (x) is the total number of categories that match the searched text\nVerify "Categories (x)" text is displayed. Count (x) is the total number of categories that match the searched text\nVerify the categories that match the searched text are displayed\nVerify designs section is displayed with zero (0) results and "No designs were found with current filters." text'],
            6: [6,
                'Go to My Designs and back to Common Designs\nVerify Search box is cleared\nVerify all categories are displayed in Common Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Go to Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Go to the 'Search' box.\nVerify 'Search common designs' prompt text and Search icon are displayed"
            start_time = time.time()

            template_management.check_search_icon()
            template_management.check_search_designs_text()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Type in text that matches Zebra category and does not match any of the Zebra designs (i.e., File Folder)\nVerify Suggestions dropdown displayed the results in 2 sections: Categories and designs\nVerify only the Categories section has displayed results"
            start_time = time.time()

            template_management.click_on_search_design()

            text = "File Folder"
            template_management.search_designs(text, 0)
            template_management.wait_for_element_appearance_name_matches_all("CATEGORIES")

            if not template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("categories suggestion not displayed or not clickable")
            if template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("designs suggestion displayed ")

            others.click_enter()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Press keyboard 'Search'\nVerify Suggestions dropdown is no longer displayed\nVerify 'Search results (x)' text is displayed. Count (x) is the total number of categories that match the searched text\nVerify 'Categories (x)' text is displayed. Count (x) is the total number of categories that match the searched text\nVerify the categories that match the searched text are displayed\nVerify designs section is displayed with zero (0) results and 'No designs were found with current filters.' text"
            start_time = time.time()

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

            temp = template_management.get_all_categories_in_common_designs()
            if not template_management.check_element_present_in_array("Address", temp):
                raise Exception("categories displayed which is not matching to search value")

            """e. Verify designs section is displayed with zero(0) results and "No designs were found with current filters." text.
            this step cannt be done"""

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Go to My Designs and back to Common Designs\nVerify Search box is cleared\nVerify all categories are displayed in Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            a = template_management.get_the_search_bar_text()
            if a:
                raise Exception("search designs text bar is not empty")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46009(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Go to "Search" box.\n-Verify "Search common designs" prompt text and Search icon are displayed'],
            4: [4,
                'Type in text that matches Zebra design and does not match any of the Zebra categories (i.e., Asset)\nVerify Suggestions dropdown displayed the results in 2 sections: Categories and designs\nVerify only the designs section has displayed results'],
            5: [5,
                'Click the design in the Suggestions dropdown\nVerify Suggestions dropdown is no longer displayed\nVerify "Search results (1)" text is displayed\nVerify "designs (1)" text is displayed\nVerify only the selected design is displayed\nVerify Categories section is NOT displayed'],
            6: [6, 'Clear the text in the "Search" box\n-Verify all categories are displayed in Common Designs']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Go to Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Go to 'Search' box.\n-Verify 'Search common designs' prompt text and Search icon are displayed"
            start_time = time.time()

            template_management.check_search_icon()
            template_management.check_search_designs_text()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Type in text that matches Zebra design and does not match any of the Zebra categories (i.e., Asset)\nVerify Suggestions dropdown displayed the results in 2 sections: Categories and designs\nVerify only the designs section has displayed results"
            start_time = time.time()

            template_management.click_on_search_design()

            text = "Asset"
            template_management.search_designs(text, 0)
            template_management.wait_for_element_appearance_name_matches_all("DESIGNS")

            if template_management.check_categories_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("categories suggestion Displayed or not clickable")
            if not template_management.check_designs_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("designs suggestion not displayed ")

            others.click_enter()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Click the design in the Suggestions dropdown\nVerify Suggestions dropdown is no longer displayed\nVerify 'Search results (1)' text is displayed\nVerify 'designs (1)' text is displayed\nVerify only the selected design is displayed\nVerify Categories section is NOT displayed"
            start_time = time.time()

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

            temp = template_management.get_all_designs_in_search_designs()
            if not template_management.check_element_present_in_array(text, temp):
                raise Exception("categories displayed which is not matching to search value")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Clear the text in the 'Search' box\n-Verify all categories are displayed in Common Designs"
            start_time = time.time()

            text = ""
            template_management.search_designs(text, 1)

            if template_management.check_suggestion_window_in_common_design():
                raise Exception("suggestion window is displayed after entering blank value")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46011(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Go to "Search" box\n-Verify "Search common designs" prompt text and Search icon are displayed'],
            5: [5,
                'Type in text that does not have a match any of the Zebra designs in the category. Try also entering design name from the other category\nVerify Suggestions dropdown is displayed\nVerify "No results for "searched text"" text is displayed\nVerify "Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then." text is displayed'],
            6: [6,
                'Clear the text in the Search box\n-Verify Suggestions dropdown is no longer displayed\nVerify all designs are displayed in the Category']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Go to Common Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: "Select Address category"
            start_time = time.time()

            template_management.wait_for_element_appearance_name_matches_all("Address")
            prev = template_management.get_all_categories_in_common_designs()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: "Go to 'Search' box\n-Verify 'Search common designs' prompt text and Search icon are displayed"
            start_time = time.time()

            template_management.check_search_icon()
            template_management.check_search_designs_text()
            template_management.click_on_search_design()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: "Type in text that does not have a match any of the Zebra designs in the category. Try also entering design name from the other category\nVerify Suggestions dropdown is displayed\nVerify 'No results for 'searched text'' text is displayed\nVerify 'Search tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then.' text is displayed"
            start_time = time.time()

            not_exists_design = "noexistsaddress"
            template_management.search_designs(not_exists_design, 0)
            template_management.wait_for_element_appearance_name_matches_all("results")
            if not template_management.check_text_for_wrong_design_name():
                raise Exception("Proper message is not displayed for wrong design")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: "Clear the text in the Search box\n-Verify Suggestions dropdown is no longer displayed\nVerify all designs are displayed in the Category"
            start_time = time.time()
            template_management.search_designs("", 1)
            if template_management.check_suggestion_window_in_common_design() or template_management.check_text_for_wrong_design_name():
                raise Exception("suggestion window is displayed after entering search")

            template_management.wait_for_element_appearance_name_matches_all("Address")
            curr = template_management.get_all_categories_in_common_designs()
            if prev != curr:
                raise Exception("all categories are not displayed after and before search")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46012(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Go to "Search" box\n-Verify "Search common designs" prompt text and Search icon are displayed'],
            5: [5,
                'Type in keyword that matches one of the Zebra designs in the category\nVerify Suggestions dropdown is displayed with one design name\nVerify the matched text is in blue font\nVerify the design name is clickable'],
            6: [6,
                'Click the design name\nVerify Suggestions dropdown is no longer displayed\nVerify only the design that matches the search is displayed in the Category'],
            7: [7, 'Clear the text in the "Search" box\n-Verify all designs are displayed in the Category']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            for text in temp[3:4]:

                # step2: "Go to Common Designs"
                start_time = time.time()

                login_page.click_Menu_HamburgerICN()
                social_login.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step3: "Select Address category"
                start_time = time.time()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Go to 'Search' box\n-Verify 'Search common designs' prompt text and Search icon are displayed"
                start_time = time.time()

                all_designs = template_management.get_all_designs_in_my_designs()
                all_names = template_management.get_names_of_design_in_search_designs(all_designs)

                t = max(all_names, key=lambda x: len(x))
                template_management.check_search_icon()
                template_management.check_search_designs_text()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Type in keyword that matches one of the Zebra designs in the category\nVerify Suggestions dropdown is displayed with one design name\nVerify the matched text is in blue font\nVerify the design name is clickable"
                start_time = time.time()
                template_management.search_designs(t, 0)
                template_management.wait_for_element_appearance_name_matches_all("1 result")
                a = template_management.get_all_search_results_in_search_designs()
                print(a)
                if len(a) != 1:
                    raise Exception("More than one design is displayed")
                if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                    raise Exception("design name is not clickable")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Click the design name\nVerify Suggestions dropdown is no longer displayed\nVerify only the design that matches the search is displayed in the Category"
                start_time = time.time()
                template_management.click_element_name_matches_all(t)
                if template_management.check_for_suggestion_drop_down_in_search_designs():
                    raise Exception("suggestion drop down is displayed after clicking the element")

                searched_elements = template_management.get_all_designs_in_my_designs()
                template_management.check_element_present_in_array(t, searched_elements)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Clear the text in the 'Search' box\n-Verify all designs are displayed in the Category"
                start_time = time.time()
                template_management.search_designs("", 1)
                template_management.wait_for_element_appearance_name_matches_all(all_names[1])
                curr_designs = template_management.get_all_designs_in_my_designs()
                if all_designs != curr_designs:
                    raise Exception("-Verify all designs are displayed in the Category. is failing")

                template_management.click_left_arrow()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46013(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Common Designs'],
            3: [3, 'Select Address category'],
            4: [4, 'Go to "Search" box\n-Verify "Search common designs" prompt text and Search icon are displayed'],
            5: [5,
                'Type in text that matches more than one of the Zebra designs in the category\nVerify Suggestions dropdown is displayed with the matching design names\nVerify the matched text is in blue font\nVerify the design names are clickable'],
            6: [6,
                'Press keyboard "Search"\nVerify Suggestions dropdown is no longer displayed\nVerify only the designs with names that matches the keyword in step 5 are displayed\nVerify the count in the "Search results (x)" is correct'],
            7: [7, 'Clear the text in the "Search" box\n-Verify all designs are displayed in the Category']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Login to Mobile App"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]
            for text in temp[4:5]:

                # step2: "Go to Common Designs"
                start_time = time.time()
                login_page.click_Menu_HamburgerICN()
                social_login.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step3: "Select Address category"
                start_time = time.time()
                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Go to 'Search' box\n-Verify 'Search common designs' prompt text and Search icon are displayed"
                start_time = time.time()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Type in text that matches more than one of the Zebra designs in the category\nVerify Suggestions dropdown is displayed with the matching design names\nVerify the matched text is in blue font\nVerify the design names are clickable"
                start_time = time.time()
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
                matched_names = template_management.get_names_of_design_in_search_designs(a)

                if not template_management.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                    raise Exception("design name is not clickable")
                others.click_enter()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step6: "Press keyboard 'Search'\nVerify Suggestions dropdown is no longer displayed\nVerify only the designs with names that matches the keyword in step 5 are displayed\nVerify the count in the 'Search results (x)' is correct"
                start_time = time.time()
                if template_management.check_for_suggestion_drop_down_in_search_designs():
                    raise Exception("suggestion drop down is displayed after clicking the element")
                template_management.wait_for_element_appearance_name_matches_all(matched_names[1])

                tem = template_management.get_all_designs_in_my_designs()
                searched_elements = template_management.get_names_of_design_in_search_designs(tem)

                print("searched", searched_elements)
                print("matched_names", matched_names)
                if searched_elements != matched_names:
                    raise Exception("suggestion designs and results designs are not same")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step7: "Clear the text in the 'Search' box\n-Verify all designs are displayed in the Category"
                start_time = time.time()
                template_management.search_designs("", 1)
                template_management.wait_for_element_appearance_name_matches_all(all_names[1])
                curr_designs = template_management.get_all_designs_in_my_designs()
                if all_designs != curr_designs:
                    raise Exception("-Verify all designs are displayed in the Category. is failing")

                template_management.click_left_arrow()

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46004(self):
        test_steps = {
            1: [1, 'Login to Mobile App'],
            2: [2, 'Go to Home > Recently Printed Designs\n-Verify the designs in the Setup are NOT displayed'],
            3: [3, 'Go to My Designs\n-Verify the designs in the Setup are NOT displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Mobile App
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")

            temp = ["Jewelry"]
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
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
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

                n_prev = template_management.get_showing_n_designs_number()

                original_copy = name + " copy"
                full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy, 1)

                template_management.click_print_button_enabled()
                common_method.wait_for_element_appearance_enabled("Print")
                template_management.click_print_button_enabled()
                try:
                    template_management.wait_for_element_appearance_name_matches_all("Complete", 10)
                except:
                    pass

                template_management.click_left_arrow()

                login_page.click_Menu_HamburgerICN()
                social_login.click_on_profile_edit()
                social_login.scroll_down(1)
                social_login.click_log_out_button()

                social_login.wait_for_element_appearance("Sign In", 10)
                login_page.click_loginBtn()
                login_page.click_Loginwith_Google()

                """Enter the email"""
                email = "zebra850.swdvt@gmail.com"
                social_login.choose_a_google_account(email)
                social_login.wait_for_element_appearance("Home", 15)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 2: Go to Home > Recently Printed Designs and verify designs in the Setup are NOT displayed
                start_time = time.time()
                try:
                    template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy)
                    raise Exception("copied design found in another account")
                except:
                    pass

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Go to My Designs and verify designs in the Setup are NOT displayed
                start_time = time.time()
                login_page.click_Menu_HamburgerICN()
                template_management.click_my_designs_button()
                template_management.wait_for_element_appearance_name_matches_all("Showing")
                try:
                    template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy)
                    raise Exception("copied design found in another account")
                except:
                    pass
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45942(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed\nVerify "Keep your designs organized by adding a name to your copy below." text is displayed\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nVerify "Cancel" and "Save" buttons are clickable'],
            3: [3,
                'Click "Save" button\nVerify "Duplicate design" window is closed\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (ie. design Name copy)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nVerify the count in the "Showing x designs" is correct'],
            4: [4, 'Select the duplicate design\nCheck there are options clickable: Print, Rename, Duplicate, Delete']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window elements
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev = template_management.get_showing_n_designs_number()

            """Give the name of existing design here"""
            t = template_management.get_first_design_in_my_designs()
            original_copy = template_management.get_names_of_design_in_search_designs([t])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click Save button and verify duplication process
            start_time = time.time()

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) + 1:
                raise Exception("Showing designs count not updated")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select the duplicate design and verify options
            start_time = time.time()
            template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")
            template_management.click_on_delete_button_in_designs()
            sleep(1)
            template_management.click_on_delete_button_in_designs()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45943(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed\nVerify "Keep your designs organized by adding a name to your copy below." text is displayed\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nVerify "Cancel" and "Save" buttons are clickable'],
            3: [3,
                'Click "Save" button\nVerify "Duplicate design" window is closed\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (ie. design Name copy)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nVerify the count in the "Showing x designs" is correct'],
            4: [4, 'Select the duplicate design\nCheck there are options clickable: Print, Rename, Duplicate, Delete'],
            5: [5,
                'Go to My Designs\nVerify duplicate design is displayed\nVerify design\'s information (Name, Size, Thumbnail, Last Print) are correct\nVerify the count in the "Showing x designs" is correct'],
            6: [6,
                'Select the duplicate design\nCheck the following options are clickable: Print, Rename, Duplicate, Delete']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            """f. Verify the count in the "Showing x designs" is correct will not be present in home page"""

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window elements
            start_time = time.time()
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_recently_printed_labels()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                original_copy)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click Save button and verify duplication process
            start_time = time.time()
            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select the duplicate design and verify options
            start_time = time.time()
            template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Go to My Designs and verify duplicate design
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Select the duplicate design and verify options
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45944(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Duplicate design" window is closed\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (Name used in step 3)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nVerify the count in the "Showing x designs" is correct'],
            5: [5,
                'Select the duplicate design\nVerify the following options are clickable: Print, Rename, Duplicate, Delete']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev = template_management.get_showing_n_designs_number()

            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            """Enter unique name here"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input unique name and verify no error message
            start_time = time.time()
            unique_name = "uniquename_45944"
            template_management.enter_name_in_duplicate_designs(unique_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = template_management.get_the_default_duplicate_name()

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) + 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the duplicate design and verify options are clickable
            start_time = time.time()
            template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")
            template_management.click_on_delete_button_in_designs()
            sleep(1)
            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45945(self):
        test_steps = {
            1: [1, 'Go to Recently Printed Labels'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3, 'Input unique name\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Duplicate design" window is closed\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (Name used in step 3)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print)\nVerify the count in the "Showing x designs" is correct'],
            5: [5,
                'Select the duplicate design\nVerify the following options are clickable: Print, Rename, Duplicate, Delete'],
            6: [6,
                'Go to My Designs\nCheck the duplicated design shows on My Designs with correct Size, Thumbnail, Last Print\nCheck the count in the "Showing x designs" is correct'],
            7: [7, 'Click the design\nCheck the following options are clickable: Print, Rename, Duplicate, Delete']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_recently_printed_labels()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input unique name and verify no error message
            start_time = time.time()
            """Enter unique name here"""

            unique_name = "unique_name"
            template_management.enter_name_in_duplicate_designs(unique_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = template_management.get_the_default_duplicate_name()

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the duplicate design and verify options are clickable
            start_time = time.time()
            template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")
            template_management.click_on_delete_button_in_designs()
            sleep(1)
            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to My Designs and check duplicated design information
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Click the duplicated design and verify options are clickable
            start_time = time.time()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45946(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3, 'Input value of an existing design name in user\'s account.\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Duplicate Design" window is closed\nVerify notification alert "Design has been successfully duplicated." is displayed. Click "x" button\nVerify the Duplicate Design is displayed with correct name (Name used in step 3 appended with number (1))'],
            5: [5,
                'Select again the design, click the Duplicate option\nVerify default value matches the updated design\'s name with appended text "copy". (ie. design Name (1) copy)\nVerify "Cancel" and "Save" buttons are clickable']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            """Give the name of existing design here"""

            name = template_management.get_first_design_in_my_designs()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input value of an existing design name and verify no error message
            start_time = time.time()
            """Enter unique name here"""

            template_management.enter_name_in_duplicate_designs(original_copy)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = original_copy + " (1)"

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            print("duplicate", duplicate_name)
            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 1)
            except:
                raise Exception("duplicate name not found")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the design again, verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name_after = template_management.get_the_default_duplicate_name()
            if duplicate_name_after != duplicate_name + " copy":
                raise Exception(
                    " not meeting condition Verify default value matches the updated design's name with appended text copy")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45947(self):
        test_steps = {
            1: [1, 'Go to Recently Printed'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3, 'Input value of an existing design name in user\'s account.\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Duplicate Design" window is closed\nVerify notification alert "Design has been successfully duplicated." is displayed. Click "x" button\nVerify the Duplicate Design is displayed with correct name (Name used in step 3 appended with number (1))'],
            5: [5,
                'Select again the design, click the Duplicate option\nVerify default value matches the updated design\'s name with appended text "copy". (ie. design Name (1) copy)\nVerify "Cancel" and "Save" buttons are clickable'],
            6: [6, 'Go to My Designs\nCheck the duplicated design is displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently", 30)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            """Give the name of existing design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input value of an existing design name and verify no error message
            start_time = time.time()
            """Enter unique name here"""

            template_management.enter_name_in_duplicate_designs(original_copy)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = original_copy + " (1)"

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            # print("duplicate",duplicate_name)
            try:
                sleep(2)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 1)
            except:
                raise Exception("duplicate name not found")

            template_management.click_the_duplicate_button()

            duplicate_name_after = template_management.get_the_default_duplicate_name()
            if duplicate_name_after != duplicate_name + " copy":
                raise Exception(
                    " not meeting condition Verify default value matches the updated design's name with appended text copy")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to My Designs and verify duplicated design
            start_time = time.time()
            # Insert code to go to My Designs and verify the duplicated design is displayed
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45948(self):
        test_steps = {
            1: [0, 'Go to My Designs'],
            2: [1,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [2,
                'Input name of an existing Zebra design in Common Designs (ie:Address)\nVerify no error message is displayed'],
            4: [3,
                'Click "Save" button\nVerify "Duplicate Design" window is closed\nVerify notification alert "Design has been successfully duplicated." is displayed. Click "x" button\nVerify the Duplicate Design is displayed with correct name (Name used in step 3 appended with number (1))'],
            5: [4,
                'Select again the design, click Duplicate option\nVerify default value matches the updated design\'s name with appended text "copy". (ie. Address (1) copy)\nVerify "Cancel" and "Save" buttons are clickable']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Open navigation menu")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            """Give the name of existing design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_my_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input name of an existing Zebra design and verify no error message
            start_time = time.time()
            """Enter Zebra defined name here"""

            enter_name = "Address"
            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = enter_name + " (1)"

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            print("duplicate", duplicate_name)
            try:
                sleep(2)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 1)
            except:
                raise Exception("duplicate name not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the design again, verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name_after = template_management.get_the_default_duplicate_name()
            if duplicate_name_after != duplicate_name + " copy":
                raise Exception(
                    " not meeting condition Verify default value matches the updated design's name with appended text copy")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45949(self):
        test_steps = {
            1: [1, 'Go to Recently Printed'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3, 'Input name of an existing Zebra design in Common Designs\nVerify no error message is displayed'],
            4: [4,
                'Click "Save" button\nVerify "Duplicate Design" window is closed\nVerify notification alert "Design has been successfully duplicated." is displayed. Click "x" button\nVerify the Duplicate Design is displayed with correct name (Name used in step 3 appended with number (1))'],
            5: [5,
                'Select again the design, click Duplicate option\nVerify default value matches the updated design\'s name with appended text "copy".\nVerify "Cancel" and "Save" buttons are clickable'],
            6: [6, 'Go to My Designs\nCheck the duplicated design is displayed with correct information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            """Give the name of existing design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Input name of an existing Zebra design and verify no error message
            start_time = time.time()
            """Enter unique name here"""

            enter_name = "Asset"
            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for proper unique name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = enter_name + " (1)"
            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            print("duplicate", duplicate_name)
            try:
                sleep(3)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 1)
            except:
                raise Exception("duplicate name not found")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Select the design again, verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name_after = template_management.get_the_default_duplicate_name()
            if duplicate_name_after != duplicate_name + " copy":
                raise Exception(
                    " not meeting condition Verify default value matches the updated design's name with appended text copy")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to My Designs and verify duplicated design
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Open navigation menu")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                sleep(2)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 1)
            except:
                raise Exception("duplicate name not found")

            template_management.click_the_duplicate_button()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45950(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy copy)'],
            3: [3,
                'Click "Save" button\nVerify "Duplicate design" window is closed.\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (ie. design Name copy copy)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print).\nVerify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            n_prev = template_management.get_showing_n_designs_number()

            """Give the name of existing design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_my_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")

            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) + 1:
                raise Exception("Showing designs count not updated")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45951(self):
        test_steps = {
            1: [1, 'Go to Recently Printed'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy copy)'],
            3: [3,
                'Click "Save" button\nVerify "Duplicate design" window is closed.\nVerify toast alert "design has been successfully duplicated." is displayed\nVerify the duplicate design is displayed with correct name (ie. design Name copy copy)\nVerify the duplicate design\'s elements and information (Size, Thumbnail, Last Print) matches the original design\nVerify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print).\nVerify the count in the "Showing x designs" is correct'],
            4: [4, 'Go to My Designs\nCheck the duplicated design is displayed with correct information']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            """f. Verify the count in the "Showing x designs" is correct will not be present in home page"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            """Give the name of existing design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy, 1)
            template_management.click_the_duplicate_button()
            template_management.click_on_save_button()
            duplicate_copy_name = original_copy + " copy"

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy, 0)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(
                duplicate_copy_name, 1)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click Save button and verify duplication process
            start_time = time.time()
            duplicate_name = template_management.get_the_default_duplicate_name()
            if duplicate_copy_name + " copy" != duplicate_name:
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
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            duplicate_size, duplicate_date = template_management.get_the_size_and_lastprint_of_design(d_full_name)

            if duplicate_size != original_size or duplicate_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 0)
            except:
                raise Exception("original name not found")
            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)
            if original_date != curr_date or original_size != curr_size:
                raise Exception("original copy date or size has been changed")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Go to My Designs and check duplicated design
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            my_design_dup_size, my_design_dup_date = template_management.get_the_size_and_lastprint_of_design(
                d_full_name)

            if duplicate_size != my_design_dup_size or duplicate_date != my_design_dup_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45952(self):
        test_steps = {
            1: [1, 'Go to Recently Printed'],
            2: [2,
                'Select the design in the precondition, click Duplicate option\nVerify "Duplicate design" window is displayed\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy copy)'],
            3: [3,
                'Clear the default value in the input box control\nVerify error message "Name must be at least 1 charact..." is displayed'],
            4: [4,
                'Input the following characters\na. a\nb. 1\nc. !\nd. space\nVerify no error message is displayed except for inputting space key'],
            5: [5,
                'Click "Cancel" button\nVerify "Duplicate design" window is closed\nVerify design is NOT duplicated'],
            6: [6,
                'Select again the design and click Duplicate option\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nVerify "Cancel" and "Save" buttons are clickable'],
            7: [7,
                'Input at least 1 character\nClick "Save" button\nVerify "Duplicate design" window is closed\nVerify notification alert "design has been successfully duplicated." is displayed. Click "x" button\nVerify design\'s name is updated\nVerify design\'s information (Size, Thumbnail, Last Print) are NOT updated'],
            8: [8,
                'Click duplicate option again, input name with special characters, like "&*%"\nCheck the save button is disabled and there is a prompt message "These characters are not valid."']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            """Gets the name of existing first design here"""

            name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy, 1)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Clear the default value and verify error message
            start_time = time.time()
            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            enter_name = ""
            template_management.enter_name_in_duplicate_designs(enter_name)
            sleep(2)
            if not template_management.check_for_blank_value_error_in_duplicate_design():
                raise Exception("error not displayed for blank name")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Input characters and verify no error message except for space
            start_time = time.time()
            enter_name = "a1! "

            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error  displayed for valid  name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click Cancel and verify no duplication
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")
            try:
                sleep(3)
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 1)
            except:
                raise Exception("original name not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Select again and verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Input at least 1 character, click Save, and verify duplication
            start_time = time.time()
            enter_name = "abc"

            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error  displayed for valid  name")

            duplicate_name = template_management.get_the_default_duplicate_name()

            template_management.click_on_save_button()

            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                sleep(3)
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 1)
            except:
                raise Exception("original name not found")

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != original_size or curr_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Input special characters, verify disabled Save button and prompt message
            start_time = time.time()
            template_management.click_the_duplicate_button()
            enter_name = "&*%"

            template_management.enter_name_in_duplicate_designs(enter_name)
            sleep(2)
            if not template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error not displayed for valid  name")

            if template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable for invalid characters")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45953(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to Recently Printed.'],
            2: [2,
                'Select the design in the precondition, click Duplicate option. Verify "Duplicate design" window is displayed. Verify default value matches the design\'s name with appended text "copy". (ie. Abc123~`!@ copy)'],
            3: [3,
                'Input name !Special_123. Allowed special characters: ! @ $ ^ - ~ ( ) _ ` = { } | [ ] ; \' " , . Not Allowed special characters: # % & * ? + \\ : / < >. Verify no error message is displayed.'],
            4: [4,
                'Input only spaces as name. Check Spaces should be auto cleared and provide the message "Name must be at least 1 character…"  (Due to SMBM-2206, currently it is able to save).'],
            5: [5,
                'Click "Save" button. Verify "Duplicate design" window is closed. Verify toast alert "design has been successfully duplicated." is displayed. Verify the duplicate design is displayed with correct name (ie. !Special_123). Verify the duplicate design\'s elements and information (Name, Size, Thumbnail, Last Print) matches the original design. Verify the original design is displayed and there are no changes in design\'s information (Name, Size, Thumbnail, Last Print). Verify the count in the "Showing x designs" is correct.'],
            6: [6,
                'Select the duplicate design. Verify the following options are clickable: Print, Rename, Duplicate, Delete.']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed.
            start_time = time.time()
            show_message(
                "2. There is an existing design with special characters in the name (ie:Abc123~`!@) in My Designs")
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            """Give the name of existing design here as per setup"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Select the design in the precondition, click Duplicate option.
            start_time = time.time()
            """Give the name of existing design here as per setup"""

            original_copy = "Abc123~`!@"

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy, 1)
            original_size, original_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input name !Special_123. Verify no error message is displayed.
            start_time = time.time()
            enter_name = "!Special_123"
            template_management.enter_name_in_duplicate_designs(enter_name)
            if template_management.check_for_invalid_character_error_in_duplicate_design():
                raise Exception("error displayed for valid name")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Input only spaces as name. Check Spaces should be auto cleared and provide the message.
            start_time = time.time()
            raise Exception("Has a bug SMBM-2206 so cannot automate step 4 in his test case")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click "Save" button. Verify all required conditions.
            start_time = time.time()
            template_management.click_on_save_button()
            try:
                common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated", 15)
            except:
                raise Exception("Design has been successfully duplicated. is not displayed")

            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 0)
            except:
                raise Exception("duplicate name not found")

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != original_size or curr_date != original_date:
                raise Exception("duplicate copy and original copy dates or sizes not matching")
            sleep(5)
            try:
                full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 0)
            except:
                raise Exception("original name not found")

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != original_size or curr_date != original_date:
                raise Exception("original copy before and after original copy dates or sizes not matching")

            """Verify the count in the "Showing x designs" is correct this step is not applicable for recently printed labels"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Select the duplicate design. Verify all options are clickable.
            start_time = time.time()
            template_management.select_design_in_my_design_by_name_and_return(duplicate_name)
            if not template_management.verify_options_clickable_in_design():
                raise Exception("some options are not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))
        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45955(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition and click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3,
                'Click "Cancel" button\nVerify "Duplicate design" window is closed\nVerify design\'s name is NOT updated'],
            4: [4,
                'Click the design again, select Duplicate option\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nVerify "Cancel" and "Save" buttons are clickable']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            name = template_management.get_normal_design_if_there_in_first_screen_my_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click "Cancel" button and verify window closure and no name update
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            duplicate_name = original_copy + " copy"
            try:
                sleep(3)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(duplicate_name, 0)
                raise Exception("duplicate name not found")
            except:
                pass

            try:
                sleep(3)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            except:
                raise Exception("original name not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select the design again, verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45956(self):
        test_steps = {
            1: [1, 'Go to Recently Printed'],
            2: [2,
                'Select the design in the precondition and click Duplicate option\nVerify "Duplicate design" window is displayed'],
            3: [3,
                'Click "Cancel" button\nVerify "Duplicate design" window is closed\nVerify design\'s name is NOT updated'],
            4: [4,
                'Click the design again, select Duplicate option\nVerify default value matches the design\'s name with appended text "copy". (ie. design Name copy)\nVerify "Cancel" and "Save" buttons are clickable'],
            5: [5, 'Go to My Designs\nCheck the design is not duplicated']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Recently")
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design and click Duplicate option, verify Duplicate design window
            start_time = time.time()
            name = template_management.get_normal_design_if_there_in_first_screen_recently_printed_design()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]

            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

            template_management.click_the_duplicate_button()

            template_management.verify_duplicate_design_window()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click "Cancel" button and verify window closure and no name update
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(2)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("duplicate design window not closed")

            duplicate_name = original_copy + " copy"
            try:
                sleep(3)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    duplicate_name, 0)
                raise Exception("duplicate name not found")
            except:
                pass

            try:
                sleep(3)
                d_full_name = template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(
                    original_copy, 1)
            except:
                raise Exception("original name not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select the design again, verify default value and buttons
            start_time = time.time()
            template_management.click_the_duplicate_button()

            duplicate_name = template_management.get_the_default_duplicate_name()
            if original_copy + " copy" != duplicate_name:
                raise Exception("default duplicate name is not matching as expected")

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_save_button_clickable_in_rename_popup():
                raise Exception("save button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Go to My Designs and check the design is not duplicated
            start_time = time.time()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45957(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Select the design in the precondition and click Delete option\na. Verify "Delete Design" window is displayed\nb. Verify "Deleting a Design will permanently remove it from your workspace. Are you sure you want to delete?" text is displayed\nc. Verify "Cancel" and "Delete" buttons are clickable'],
            3: [3,
                'Click "Cancel" button\na. Verify "Delete design" window is closed\nb. Verify design is NOT removed'],
            4: [4, 'Select again the design and click Delete option'],
            5: [5,
                'Click "Delete" then confirm deletion\na. Verify "Delete design" window is closed\nb. Verify toast alert "design ("Name") has been successfully removed." is displayed\nc. Verify the design is NO longer displayed\nd. Verify the count in the "Showing x designs" is correct'],
            6: [6, 'Go to Home > Recently Printed Designs\n-Verify the design is NOT displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: 'Go to My Designs'
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Select the design in the precondition and click Delete option'
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev = template_management.get_showing_n_designs_number()

            """input an existing design name"""
            original_copy = template_management.get_first_design_in_my_designs()
            original_copy = template_management.get_names_of_design_in_search_designs([original_copy])[0]

            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_on_delete_button_in_designs()
            template_management.check_delete_design_window_message()

            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("cancel button is not clickable")

            if not template_management.check_delete_button_clickable_in_design_window():
                raise Exception("delete button is not clickable")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Click "Cancel" button'
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(1)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("delete design window not closed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step4: 'Select again the design and click Delete option'
            start_time = time.time()
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            except:
                raise Exception("original name not found")

            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step5: 'Click "Delete" then confirm deletion'
            start_time = time.time()
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

            n_curr = template_management.get_showing_n_designs_number()

            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step6: 'Go to Home > Recently Printed Designs'
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()

            try:
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
                raise Exception("original name not found after deleting in recently printed design")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45958(self):
        test_steps = {
            1: [0, 'Go to Recently Printed Labels'],
            2: [1,
                'Select the design in the precondition and click Delete option a. Verify "Delete design" window is displayed b. Verify "Deleting a design will permanently remove it from your workspace. Are you sure you want to delete?" text is displayed'],
            3: [2, 'Click "Cancel" button \a. Verify "Delete design" window is closed b. Verify design is NOT removed'],
            4: [3, 'Select again the design and click Delete option'],
            5: [4,
                'Click "Delete" then confirm deletion a. Verify "Delete design" window is closedb. Verify toast alert "design ("Name") has been successfully removed." is displayed c. Verify the design is NO longer displayed'],
            6: [5,
                'Go to My Designs and verify the design is not displayed and the count is correct Verify the design is NOT displayed Verify the count in the "Showing x designs" is correct']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            n_prev = template_management.get_showing_n_designs_number()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition and click Delete option
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            common_method.wait_for_element_appearance_namematches("Recently")
            name = template_management.get_first_design_in_recently_printed_labels()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)
            template_management.click_on_delete_button_in_designs()
            if not template_management.check_delete_design_window_message():
                raise Exception("Delete design window message not displayed")
            if not template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("Cancel button is not clickable")
            if not template_management.check_delete_button_clickable_in_design_window():
                raise Exception("Delete button is not clickable")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click "Cancel" button
            start_time = time.time()
            template_management.click_on_cancel_button_in_rename_popup()
            sleep(1)
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("Delete design window not closed")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
            except:
                raise Exception("Original name not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Select again the design and click Delete option
            start_time = time.time()
            template_management.click_on_delete_button_in_designs()
            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: Click "Delete" then confirm deletion
            start_time = time.time()
            try:
                common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
            except:
                raise Exception("Design has been successfully duplicated message not displayed")
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("Delete design window not closed")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
                raise Exception("Original name found after deleting")
            except:
                pass
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
                raise Exception("Original name found after deleting")
            except:
                pass
            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Go to My Designs and verify the design is not displayed and the count is correct
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
                raise Exception("Original name found after deleting")
            except:
                pass
            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45959(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2, 'Select Address category'],
            3: [3, 'Select the available designs\nVerify "Delete" option is NOT displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: 'Go to Common Designs'
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """Add more categories as required"""
            temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                    "Shipping", "Small Multipurpose"]

            for text in temp[0:1]:
                login_page.click_Menu_HamburgerICN()
                template_management.click_home_button()
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step2: 'Select Address category'
                start_time = time.time()
                template_management.wait_in_common_designs_until_load()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                t = template_management.get_first_design_in_my_designs()
                template_management.click_element_by_name_or_text(t)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step3: 'Select the available designs'
                start_time = time.time()
                try:
                    template_management.click_on_delete_button_in_designs()
                    raise Exception("rename button is present")
                except:
                    pass

                template_management.click_left_arrow()
                sleep(1)
                template_management.click_left_arrow()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45961(self):
        test_steps = {
            1: [0, 'Go to My Designs'],
            2: [1,
                'Select the design in the precondition and click Delete option a. Verify "Delete design" window is displayed'],
            3: [2,
                'Click "Delete" button a. Verify "Delete design" window is closed b. Verify notification alert "design ("Name") has been successfully removed." is displayed. Click "x" button c. Verify the design is NO longer displayed d. Verify the count in the "Showing x designs" is correct'],
            4: [3, 'Go to Home > Recently Printed Designs Verify the design is NOT displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            n_prev = template_management.get_showing_n_designs_number()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Select the design in the precondition and click Delete option
            start_time = time.time()
            name = template_management.get_first_design_in_recently_printed_labels()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)
            template_management.click_on_delete_button_in_designs()
            if not template_management.check_delete_design_window_message():
                raise Exception("Delete design window message not displayed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Click "Delete" button
            start_time = time.time()
            template_management.click_on_delete_button_in_designs()
            try:
                common_method.wait_for_element_appearance_namematches("has been successfully removed", 15)
            except:
                raise Exception("Design has been successfully removed message not displayed")
            if template_management.check_cancel_button_clickable_in_rename_popup():
                raise Exception("delete design window not closed")
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
                raise Exception("Original name found after deleting")
            except:
                pass
            n_curr = template_management.get_showing_n_designs_number()
            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Go to Home > Recently Printed Designs
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            try:
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
                raise Exception("Original name found in recently printed designs after deleting")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45962(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to My Designs.'],
            2: [2,
                'Select the design in the precondition and click Delete option. Verify "Delete design" window is displayed.'],
            3: [3, 'Turn off the WiFi connection on the mobile device settings.'],
            4: [4,
                'Go back to the Mobile App. Click "Delete" button on the confirm dialog. Verify it would display a toast that says the template wasn\'t deleted successfully.'],
            5: [5, 'Go to web portal and other mobile app client to have a check that the template is not deleted.'],
            6: [6,
                'Turn on the WiFi connection on the mobile device settings, and delete the template again. Verify toast alert "design ("Name") has been successfully removed." is displayed. Verify the design is NO longer displayed. Verify the count in the "Showing x designs" is correct.'],
            7: [7, 'Go to Home > Recently Printed Designs. Verify the design is NOT displayed.']
        }

        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to My Designs.
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """ has this error still SMBM-1902"""

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Select the design in the precondition and click Delete option. Verify "Delete design" window is displayed.
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev = template_management.get_showing_n_designs_number()

            name = template_management.get_first_design_in_my_designs()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_my_design_by_name_and_return(original_copy)

            template_management.click_on_delete_button_in_designs()
            template_management.check_delete_design_window_message()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Turn off the WiFi connection on the mobile device settings.
            start_time = time.time()
            template_management.turn_off_wifi()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Go back to the Mobile App. Click "Delete" button on the confirm dialog. Verify it would display a toast that says the template wasn't deleted successfully.
            start_time = time.time()
            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Go to web portal and other mobile app client to have a check that the template is not deleted.
            start_time = time.time()
            show_message(
                "5. Go to web portal and other mobile app client to have a check that the template is not deleted")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Turn on the WiFi connection on the mobile device settings, and delete the template again. Verify toast alert "design ("Name") has been successfully removed." is displayed. Verify the design is NO longer displayed. Verify the count in the "Showing x designs" is correct.
            start_time = time.time()
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

            n_curr = template_management.get_showing_n_designs_number()

            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7: Go to Home > Recently Printed Designs. Verify the design is NOT displayed.
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            common_method.wait_for_element_appearance_namematches("Recently")

            try:
                template_management.get_the_full_name_of_design_and_click_in_recently_printed_design(original_copy, 1)
                raise Exception("original name not found after deleting")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45963(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Go to Recently Printed Labels.'],
            2: [2,
                'Select the design in the precondition and click Delete option. Verify "Delete design" window is displayed.'],
            3: [3, 'Turn off the WiFi connection on the mobile device settings.'],
            4: [4,
                'Go back to the Mobile App. Click "Delete" button on the confirm dialog. Verify it would display a toast that says the template wasn\'t deleted successfully.'],
            5: [5, 'Go to web portal and other mobile app client to have a check that the template is not deleted.'],
            6: [6,
                'Turn on the WiFi connection on the mobile device settings, and delete the template again. Verify toast alert "design ("Name") has been successfully removed." is displayed. Verify the design is NO longer displayed. Verify the count in the "Showing x designs" is correct.'],
            7: [7, 'Go to My Designs. Verify the design is NOT displayed.']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])
        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Go to Recently Printed Labels.
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            """ has this error still SMBM-1902"""

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            n_prev = template_management.get_showing_n_designs_number()

            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            common_method.wait_for_element_appearance_namematches("Recently")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Select the design in the precondition and click Delete option. Verify "Delete design" window is displayed.
            start_time = time.time()
            """input an existing design name"""
            name = template_management.get_first_design_in_recently_printed_labels()
            original_copy = template_management.get_names_of_design_in_search_designs([name])[0]
            full_name = template_management.select_design_in_recetly_printed_design_by_name_and_return(original_copy)

            template_management.click_on_delete_button_in_designs()
            template_management.check_delete_design_window_message()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Turn off the WiFi connection on the mobile device settings.
            start_time = time.time()
            template_management.turn_off_wifi()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Go back to the Mobile App. Click "Delete" button on the confirm dialog. Verify it would display a toast that says the template wasn't deleted successfully.
            start_time = time.time()
            template_management.click_on_delete_button_in_designs()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Go to web portal and other mobile app client to have a check that the template is not deleted.
            start_time = time.time()
            show_message(
                "5. Go to web portal and other mobile app client to have a check that the template is not deleted")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Turn on the WiFi connection on the mobile device settings, and delete the template again. Verify toast alert "design ("Name") has been successfully removed." is displayed. Verify the design is NO longer displayed. Verify the count in the "Showing x designs" is correct.
            start_time = time.time()
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

            n_curr = template_management.get_showing_n_designs_number()

            if int(n_curr) != int(n_prev) - 1:
                raise Exception("Showing designs count not updated")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 7: Go to My Designs. Verify the design is NOT displayed.
            start_time = time.time()
            try:
                template_management.get_the_full_name_of_design_and_click_in_my_design(original_copy, 1)
                raise Exception("original name not found after deleting")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45964(self):
        test_steps = {
            1: [1, 'Go to My Designs'],
            2: [2,
                'Check below items\nVerify there are no designs shown\nVerify there is a prompt message like "There are currently no designs saved to your My Designs. To get started Create New design or go to the our Common Designs to see more premade designs"']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:

            # step1: "Go to My Designs"
            start_time = time.time()

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            sleep(1)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Check below items\nVerify there are no designs shown\nVerify there is a prompt message like 'There are currently no designs saved to your My Designs. To get started Create New design or go to the our Common Designs to see more premade designs'"
            start_time = time.time()

            try:
                template_management.get_all_designs_in_my_designs()
                raise Exception("designs are present")
            except:
                pass

            if not template_management.check_no_designs_present_text():
                raise Exception("proper message not displayed for empty designs in my designs")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45967(self):
        test_steps = {
            1: [1, 'Go to Common Designs\nVerify the categories are sorted from A to Z'],
            2: [2,
                'Scroll through the category list\na. Verify the following categories are displayed:\n- Address\n- Barcode\n- Jewelry\n- Multipurpose/Name Tag\n- Postage/Shipping\n- Return Address/File Folder\n- Round\n- Shipping\n- Small Multipurpose\n- XL Shipping\nb. Verify each category has description\nc. Verify each category has Zebra icon on the top left']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Common Designs\nVerify the categories are sorted from A to Z"
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            strings = ["Address", "Barcodes", "Jewelry", "Shipping", "Return Address/File Folder", "Round", "Shipping",
                       "Small Multipurpose", "XL Shipping"]

            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: "Scroll through the category list\na. Verify the following categories are displayed:\n- Address\n- Barcode\n- Jewelry\n- Multipurpose/Name Tag\n- Postage/Shipping\n- Return Address/File Folder\n- Round\n- Shipping\n- Small Multipurpose\n- XL Shipping\nb. Verify each category has description\nc. Verify each category has Zebra icon on the top left"
            start_time = time.time()

            curr_categories = template_management.get_all_categories_in_common_designs()
            categories = template_management.get_names_of_design_in_search_designs(curr_categories)
            print(categories)
            login_page.click_Menu_HamburgerICN()
            template_management.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management.click_common_designs_button()
            template_management.wait_in_common_designs_until_load()

            for i in strings:
                if i not in categories:
                    raise Exception(i, "this category is not present in common designs")

            try:
                template_management.verify_zebra_icon_in_the_categories(curr_categories)
            except:
                raise Exception("zebra icon not present for some category")

            if not template_management.verify_description_present_in_the_categories(curr_categories):
                raise Exception("description not present for some category")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45968(self):
        test_steps = {
            1: [1, 'Go to Common Designs'],
            2: [2,
                'Select Address category\na. Verify "Address" category text is displayed\nb. Verify arrow back button is displayed'],
            3: [3,
                'Scroll through the design list\na. Verify only the designs belonging to the category are displayed\nb. Verify designs are sorted from A to Z\nc. Verify designs information (Name, Size, Thumbnail) are displayed\nd. Verify "Last Print" information is NOT displayed\ne. Verify 3-dot menu on the top left of the designs are clickable'],
            4: [4,
                'Click on each design\nVerify only the following option is displayed and clickable: Print, Copy to My Designs'],
            5: [5, 'Click Category\'s arrow back button\nVerify Common Designs view is displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: "Go to Common Designs"
            start_time = time.time()

            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Address", "Barcodes", "Jewelry", "Multipurpose", "Shipping", "File Folder", "Round", "Shipping",
                    "Small Multipurpose"]
            for text in temp[0:1]:
                login_page.click_Menu_HamburgerICN()
                template_management.click_common_designs_button()
                template_management.wait_in_common_designs_until_load()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step2: "Select Address category\na. Verify "Address" category text is displayed\nb. Verify arrow back button is displayed"
                start_time = time.time()

                template_management.search_designs(text, 1)
                template_management.wait_for_element_appearance_name_matches_all(text)
                template_management.click_element_name_matches_all(text, 0)

                template_management.wait_until_designs_load_after_clicking_categories()
                try:
                    template_management.wait_for_element_appearance_name_matches_all(text)
                except:
                    raise Exception(text, "this category text not displayed")
                if not template_management.check_left_arrow_exists():
                    raise Exception("left arrow is not present")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step3: "Scroll through the design list\na. Verify only the designs belonging to the category are displayed\nb. Verify designs are sorted from A to Z\nc. Verify designs information (Name, Size, Thumbnail) are displayed\nd. Verify "Last Print" information is NOT displayed\ne. Verify 3-dot menu on the top left of the designs are clickable"
                start_time = time.time()
                all_complete_designs = template_management.get_all_designs_in_my_designs()
                all_designs = template_management.get_names_of_design_in_search_designs(all_complete_designs)
                all_designs = template_management.make_everything_lower_case(all_designs)
                sorted_design = all_designs
                sorted_design = sorted(sorted_design)

                """Commented code currently cannot be verified since labels are not sorted properly"""
                if all_designs != sorted_design:
                    raise Exception("designs are not in sorted order")

                for i in all_complete_designs:
                    name, size, lastprint = template_management.get_the_name_size_and_lastprint_of_design(i)
                    if int(lastprint) != 0:
                        raise Exception("last print displayed for", i, "design")

                template_management.scroll_till_element(all_designs[0], 1)

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step4: "Click on each design\nVerify only the following option is displayed and clickable: Print, Copy to My Designs"
                start_time = time.time()
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
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # step5: "Click Category's arrow back button\nVerify Common Designs view is displayed"
                start_time = time.time()
                template_management.click_left_arrow()

                if not template_management.check_element_exists("Common Designs"):
                    raise Exception("common designs page is not displayed after clicking left arrow")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_46000(self):
        test_steps = {
            1: [1, 'Login to Web Portal'],
            2: [2,
                'Go to My Designs.\na. Verify copied design is displayed.\nb. Verify design\'s information (Name, Size, Thumbnail, no Last Print) matches the values in the Mobile App'],
            3: [3, 'Go to Home > Recently Printed Designs.\n-Verify copied design is NOT displayed']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Login to Web Portal
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            temp = ["Jewelry"]
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
                names, size = template_management.get_names_and_sizes_in_recently_printed_labels([t])
                name = names[0]
                print("t", t)
                d_size, d_last_print = template_management.get_the_size_and_lastprint_of_design(t)

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

                name = "BOGO copy"
                start_app("com.google.android.googlequicksearchbox")
                sleep(1)
                others.click_google_search_bar()
                others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
                others.click_enter()
                others.wait_for_element_appearance("Continue with Google", 10)
                login_page.click_Loginwith_Google()
                common_method.wait_for_element_appearance_textmatches("Choose an account")
                """pass your email below for the same account"""
                email = "zebra901.swdvt@gmail.com"
                template_management.select_and_click_an_google_account(email)

                common_method.wait_for_element_appearance_text("Home", 20)
                others.click_hamburger_button_in_Google()
                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 2: Go to My Designs, verify copied design and its information
                start_time = time.time()
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
                if int(d_last_print) != 0:
                    raise Exception("last print date displayed without printing for the copy")

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1

                # Step 3: Go to Home > Recently Printed Designs, verify copied design is NOT displayed
                start_time = time.time()
                """3. Go to Home > Recently Printed Designs.
                       -Verify copied design is NOT displayed. this step fails due to bug id: SMBM-1372"""
                start_app("com.zebra.soho_app")

                others.wait_for_element_appearance_text("Home", 20)

                others.scroll_down()

                common_method.wait_for_element_appearance_namematches("Recently")
                try:
                    template_management.get_the_full_name_of_design_and_click_in_my_design(name + " copy", 0)
                    raise Exception("copied name found in recently printed label without printing ")
                except:
                    pass

                exec_time = (time.time() - start_time) / 60
                insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                            exec_time)

                stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Template_Management_TestcaseID_45939(self):
        test_steps = {
            1: [1, 'Login to Web Portal with same account'],
            2: [2,
                'Go to My Designs\nVerify renamed design is displayed\nVerify design\'s information (Name, Size, Thumbnail, Last Print) matches the values in Mobile App'],
            3: [3,
                'Go to Home > Recently Printed Designs\nVerify renamed design is displayed\nVerify design\'s information (Name, Size, Thumbnail, Last Print) matches the values in Mobile App']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # step1: 'Login to Web Portal with same account'
            start_time = time.time()
            stop_app("com.zebra.soho_app")
            start_app("com.zebra.soho_app")
            common_method.wait_for_element_appearance_namematches("Home")
            login_page.click_Menu_HamburgerICN()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step2: 'Go to My Designs\nVerify renamed design is displayed\nVerify design\'s information (Name, Size, Thumbnail, Last Print) matches the values in Mobile App'
            start_time = time.time()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")
            """Give the name of existing design here"""
            name = template_management.get_first_design_in_my_designs()
            full_name = name
            template_management.click_element_by_name_or_text(name)
            prev_size, prev_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            template_management.click_on_rename_button()

            new_name = "somenamemyown_45939"

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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # step3: 'Go to Home > Recently Printed Designs\nVerify renamed design is displayed\nVerify design\'s information (Name, Size, Thumbnail, Last Print) matches the values in Mobile App'
            start_time = time.time()
            start_app("com.google.android.googlequicksearchbox")

            others.click_google_search_bar()
            others.enter_the_text_in_goole("https://zsbportal.zebra.com/")
            others.click_enter()
            others.wait_for_element_appearance("Continue with Google", 20)
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account", 20)
            """pass your email below for the same account"""
            email = "zebra850.swdvt@gmail.com"
            template_management.select_and_click_an_google_account(email)

            common_method.wait_for_element_appearance_text("Home", 20)
            others.click_hamburger_button_in_Google()
            template_management.click_on_click_on_my_designs_in_google()
            others.click_hamburger_button_in_Google()

            designs_present = template_management.search_design_in_google_present(new_name)
            g_size, g_last_print = template_management.get_size_and_lastprint_of_design_in_google(new_name)
            if not designs_present:
                raise Exception("renamed design is not present in the google")
            """size in mobile and app should be same ,this step fails due to SMBM : 1749"""
            if g_size != prev_size:
                raise Exception("sizes are different for same design in app and web")
            if int(g_last_print) != 0:
                raise Exception("last print date displayed without printing for the copy")

            start_app("com.zebra.soho_app")

            common_method.wait_for_element_appearance_namematches("Home", 30)

            login_page.click_Menu_HamburgerICN()
            template_management.click_my_designs_button()
            common_method.wait_for_element_appearance_namematches("Showing")

            try:
                full_name = template_management.select_design_in_my_design_by_name_and_return(new_name, 0)
            except:
                raise Exception("design not found after updating")

            curr_size, curr_date = template_management.get_the_size_and_lastprint_of_design(full_name)

            if curr_size != prev_size or curr_date != prev_date:
                raise Exception("size or date is not matching after renaming the design")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1


        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Others_TestcaseID_45801(self):
        test_steps = {
            1: [1, 'Open Mobile device'],
            2: [2, 'Login in with existing user already added one printer'],
            3: [3, 'Go to common design, copy one common design into my design. eg: copy Asset in Address category'],
            4: [4, 'Go to My Design, open copied template and click printer'],
            5: [5, 'In Print preview page, there are 2 input boxes: Enter Data, Enter Text'],
            6: [6,
                'Click Enter Data input box, check the input box in focus. Input a value into this input box, stop entering and wait for a while (5 seconds), then check the preview will update and continue input, check the keyboard will not disappear'],
            7: [7, 'Repeat step 6, check while input text and stop for a while, keyboard will keep showing up'],
            8: [8, 'Click print, check the template print out with updated value successfully']
        }

        start_time_main = time.time()

        stepId = 1
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]
        start_main(execID, leftId[test_case_id])

        try:
            # Step 1: Open Mobile device
            start_time = time.time()
            common_method.tearDown()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 2: Login in with existing user already added one printer
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 3: Go to common design, copy one common design into my design. eg: copy Asset in Address category
            start_time = time.time()
            others.click_common_designs_button()
            others.search_designs("Small Multipurpose")
            sleep(4)
            others.select_first_design()
            sleep(4)

            others.search_designs("PriceLabel")
            sleep(3)
            others.select_first_design()

            others.click_on_copy_to_my_designs()
            common_method.wait_for_element_appearance_namematches("successfully")
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 4: Go to My Design, open copied template and click printer
            start_time = time.time()
            others.click_left_arrow()
            login_page.click_Menu_HamburgerICN()
            others.click_on_my_designs()
            others.search_designs("PriceLabel")
            sleep(3)
            others.select_first_design()

            others.click_print_button()
            sleep(4)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 5: In Print preview page, there are 2 input boxes: Enter Data, Enter Text
            start_time = time.time()
            others.click_enter_data_for_design()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 6: Click Enter Data input box, check the input box in focus. Input a value into this input box, stop entering and wait for a while (5 seconds), then check the preview will update and continue input, check the keyboard will not disappear
            start_time = time.time()
            others.enter_data_for_design("123456789")
            others.check_error_print_preview()
            sleep(5)
            res = others.check_for_keyboard()
            if not res:
                raise Exception("Keyboard not found")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 7: Repeat step 6, check while input text and stop for a while, keyboard will keep showing up
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

            stepId += 1

            # Step 8: Click print, check the template print out with updated value successfully
            start_time = time.time()
            others.click_print_button()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)



        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)
