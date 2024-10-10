"""New merged Code"""
import inspect

# import sys
# sys.path.append(r'C:\Users\tr5927\Desktop\ZSB_Automation')

import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Social_Login.Social_Login import Social_Login
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId
from ZSB_Mobile.login_information import *


class Test_Android_Template_Management:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
# start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
social_login = Social_Login(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
aps_notification = APS_Notification(poco)

ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()

start_execution_loop(execID)


def test_Template_Management_TestcaseID_46006():
    test_steps = {
        1: [1, 'Login to the Mobile App.'],
        2: [2, 'Navigate to Common Designs.'],
        3: [3, 'Go to the "Search" box and verify that "Search designs" text and the Search icon are displayed.'],
        4: [4,
            'Type in text that does not match any of the Zebra categories and designs. Verify Suggestions dropdown is displayed. Verify that "No results found." text is displayed. Verify Search tips.'],
        5: [5,
            'Clear the text in the "Search" box. Verify that the Suggestions dropdown is no longer displayed. Verify that all categories are displayed in Common Designs.'],
        6: [6,
            'Input another non-matched keyword and click the search button. Check that the prompt message is correct.']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        user = zebra901
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        registration_page.check_if_user_navigated_to_sign_in_page()
        account, password = common_method.get_credentials_from_user(user)
        help_page.chooseAcc(account)
        registration_page.BugFix_For_Google(account)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        template_management_page_1.click_on_search_design()
        text = "no_text_match"
        template_management_page_1.search_designs(text, 0)
        social_login.check_if_no_results_displayed_when_searching_for_design()
        template_management_page_1.check_expected_message_displayed_when_searching_for_design_that_is_not_present()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        blank_value = ""
        template_management_page_1.search_designs(blank_value, 1)
        template_management_page_1.check_if_suggestion_window_is_displayed_when_search_blank_value_in_common_designs()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        template_management_page_1.search_designs(text, 0)
        social_login.check_if_no_results_displayed_when_searching_for_design()

        template_management_page_1.check_expected_message_displayed_when_searching_for_design_that_is_not_present()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Template_Management_TestcaseID_46007():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        template_management_page_1.click_on_search_design()
        text = "Address"
        categories = "CATEGORIES"
        template_management_page_1.search_designs(text, 0)
        template_management_page_1.wait_for_element_appearance_name_matches_all(categories)

        if not template_management_page_1.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion not displayed or not clickable")
        if not template_management_page_1.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion not displayed or not clickable")

        if not template_management_page_1.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
            raise Exception(
                "Verify on the designs section, the number of designs that matches is displayed on the right side (not meeting this step)")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        others_page.click_enter()
        template_management_page_1.check_suggestion_window_displayed_even_after_clicking_search()
        try:
            template_management_page_1.get_total_count_search_results_in_common_designs()
        except:
            raise Exception("Search count is not displayed properly")
        template_management_page_1.wait_for_element_appearance_name_matches_all("Categories")
        try:
            template_management_page_1.get_total_count_categories_results_in_common_designs()
        except:
            raise Exception("Categories count is not displayed properly")
        temp = template_management_page_1.get_all_categories_in_search_designs()
        if not template_management_page_1.check_element_present_in_array("Address", temp):
            raise Exception("categories displayed which is not matching to search value")
        try:
            template_management_page_1.get_total_count_designs_results_in_common_designs()
        except:
            raise Exception("Design count is not displayed properly")
        temp = template_management_page_1.get_all_designs_in_search_designs()
        if not template_management_page_1.check_element_present_in_array("Address", temp):
            raise Exception("designs displayed which is not matching to search value")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        text = ""
        template_management_page_1.search_designs(text, 1)
        template_management_page_1.check_if_suggestion_window_is_displayed_when_search_blank_value_in_common_designs()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""Reduce step size - debug lines test cases"""


def test_Template_Management_TestcaseID_46008():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        template_management_page_1.click_on_search_design()
        text = "File Folder"
        template_management_page_1.search_designs(text, 0)
        template_management_page_1.wait_for_element_appearance_name_matches_all("CATEGORIES")

        if not template_management_page_1.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion not displayed or not clickable")
        if template_management_page_1.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion displayed ")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        others_page.click_enter()
        template_management_page_1.check_suggestion_window_displayed_even_after_clicking_search()

        try:
            template_management_page_1.get_total_count_search_results_in_common_designs()
        except:
            raise Exception("Search count is not displayed properly")
        template_management_page_1.wait_for_element_appearance_name_matches_all("Categories")
        try:
            template_management_page_1.get_total_count_categories_results_in_common_designs()
        except:
            raise Exception("Categories count is not displayed properly")

        temp = template_management_page_1.get_all_categories_in_common_designs()
        if not template_management_page_1.check_element_present_in_array("Address", temp):
            raise Exception("categories displayed which is not matching to search value")

        """e. Verify designs section is displayed with zero(0) results and "No designs were found with current filters." text.
        this step cannot be done"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        a = template_management_page_1.get_the_search_bar_text()
        if a:
            raise Exception("search designs text bar is not empty")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Template_Management_TestcaseID_46009():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        template_management_page_1.click_on_search_design()
        text = "Asset"
        template_management_page_1.search_designs(text, 0)
        template_management_page_1.wait_for_element_appearance_name_matches_all("DESIGNS")

        if template_management_page_1.check_categories_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("categories suggestion Displayed or not clickable")
        if not template_management_page_1.check_designs_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("designs suggestion not displayed ")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        others_page.click_enter()
        template_management_page_1.check_suggestion_window_displayed_even_after_clicking_search()
        template_management_page_1.get_total_count_search_results_in_common_designs()
        try:
            categories_count = template_management_page_1.get_total_count_categories_results_in_common_designs()
            raise Exception("Categories count is displayed ")
        except:
            pass
        temp = template_management_page_1.get_all_designs_in_search_designs()
        if not template_management_page_1.check_element_present_in_array(text, temp):
            raise Exception("categories displayed which is not matching to search value")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        text = ""
        template_management_page_1.search_designs(text, 1)
        template_management_page_1.check_if_suggestion_window_is_displayed_when_search_blank_value_in_common_designs()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Template_Management_TestcaseID_46011():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        design_category = "Address"
        template_management_page_1.wait_for_element_appearance_name_matches_all(design_category)
        template_management_page_1.click_element_name_matches_all(design_category, 0)
        template_management_page_1.wait_until_designs_load_after_clicking_categories()
        prev = template_management_page_1.get_all_designs_in_my_designs()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        """Search your designs" (for this search designs is prompt text) prompt text and Search icon are displayed"""
        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        template_management_page_1.click_on_search_design()
        """input value that does not match with our current designs"""
        not_exists_design = "non_existing_design"
        template_management_page_1.search_designs(not_exists_design, 0)
        template_management_page_1.wait_for_element_appearance_name_matches_all("results")
        if not template_management_page_1.check_text_for_wrong_design_name():
            raise Exception("Proper message is not displayed for wrong design")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        template_management_page_1.search_designs("", 1)
        if template_management_page_1.check_suggestion_window_in_common_design() or template_management_page_1.check_text_for_wrong_design_name():
            raise Exception("suggestion window is displayed after entering search")

        template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
        curr = template_management_page_1.get_all_designs_in_my_designs()
        if prev != curr:
            raise Exception("all categories are not displayed after and before search")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""AEMS pending"""
"-------------------"


def test_Template_Management_TestcaseID_46012():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
                "Shipping", "Small Multipurpose"]
        for text in temp[:2]:

            login_page.click_Menu_HamburgerICN()
            social_login.click_home_button()
            login_page.click_Menu_HamburgerICN()
            template_management_page_1.click_common_designs_button()
            template_management_page_1.wait_in_common_designs_until_load()

            template_management_page_1.search_designs(text, 1)
            template_management_page_1.wait_for_element_appearance_name_matches_all(text)
            template_management_page_1.click_element_name_matches_all(text, 0)

            template_management_page_1.wait_until_designs_load_after_clicking_categories()

            all_designs = template_management_page_1.get_all_designs_in_my_designs()
            all_names = template_management_page_1.get_names_of_design_in_search_designs(all_designs)

            t = max(all_names, key=lambda x: len(x))
            template_management_page_1.check_search_icon()
            template_management_page_1.check_search_designs_text()

            template_management_page_1.search_designs(t, 0)
            template_management_page_1.check_if_search_results_appear()
            a = template_management_page_1.get_all_search_results_in_search_designs()
            print(a)
            if len(a) != 1:
                raise Exception("More than one design is displayed")
            if not template_management_page_1.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
                raise Exception("design name is not clickable")
            template_management_page_1.click_element_name_matches_all(t)
            if template_management_page_1.check_for_suggestion_drop_down_in_search_designs():
                raise Exception("suggestion drop down is displayed after clicking the element")

            searched_elements = template_management_page_1.get_all_designs_in_my_designs()
            template_management_page_1.check_element_present_in_array(t, searched_elements)
            template_management_page_1.search_designs("", 1)
            template_management_page_1.wait_for_element_appearance_name_matches_all(all_names[1])
            curr_designs = template_management_page_1.get_all_designs_in_my_designs()
            if all_designs != curr_designs:
                raise Exception("-Verify all designs are displayed in the Category. is failing")

            template_management_page_1.click_left_arrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Template_Management_TestcaseID_46013():
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
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    temp = ["Address", "Barcode", "File Folder", "Jewelry", "Multipurpose", "Name Tag", "Return Address",
            "Shipping", "Small Multipurpose"]
    for text in temp[::2]:

        login_page.click_Menu_HamburgerICN()
        social_login.click_home_button()
        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_common_designs_button()
        template_management_page_1.wait_in_common_designs_until_load()

        template_management_page_1.search_designs(text, 1)
        template_management_page_1.wait_for_element_appearance_name_matches_all(text)
        template_management_page_1.click_element_name_matches_all(text, 0)

        template_management_page_1.wait_until_designs_load_after_clicking_categories()

        all_designs = template_management_page_1.get_all_designs_in_my_designs()
        all_names = template_management_page_1.get_names_of_design_in_search_designs(all_designs)

        t = 'a'
        template_management_page_1.check_search_icon()
        template_management_page_1.check_search_designs_text()

        template_management_page_1.search_designs(t, 0)
        template_management_page_1.check_if_search_results_appear()
        a = template_management_page_1.get_all_search_results_in_search_designs()
        print(a)
        matched_names = template_management_page_1.get_names_of_design_in_search_designs(a)

        if not template_management_page_1.check_results_in_design_subarea_in_suggestion_window_and_check_clickable():
            raise Exception("design name is not clickable")
        others_page.click_enter()
        if template_management_page_1.check_for_suggestion_drop_down_in_search_designs():
            raise Exception("suggestion drop down is displayed after clicking the element")
        template_management_page_1.wait_for_element_appearance_name_matches_all(matched_names[1])

        tem = template_management_page_1.get_all_designs_in_my_designs()
        searched_elements = template_management_page_1.get_names_of_design_in_search_designs(tem)

        print("searched", searched_elements)
        print("matched_names", matched_names)
        if searched_elements != matched_names:
            raise Exception("suggestion designs and results designs are not same")

        template_management_page_1.search_designs("", 1)
        template_management_page_1.wait_for_element_appearance_name_matches_all(all_names[1])
        curr_designs = template_management_page_1.get_all_designs_in_my_designs()
        if all_designs != curr_designs:
            raise Exception("-Verify all designs are displayed in the Category. is failing")

        template_management_page_1.click_left_arrow()


"-------------------"


def test_Template_Management_TestcaseID_45964():
    test_steps = {
        1: [1, 'Go to My Designs'],
        2: [2,
            'Check below items\nVerify there are no designs shown\nVerify there is a prompt message like "There are currently no designs saved to your My Designs. To get started Create New design or go to the our Common Designs to see more premade designs"']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_my_designs_button()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        designs = template_management_page_1.get_all_designs_in_my_designs()
        if len(designs) > 0:
            raise Exception("designs are present in this account.")
        if not template_management_page_1.check_no_designs_present_text():
            raise Exception("proper message not displayed for empty designs in my designs")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""AEMS pending"""
"-------------------"
# def test_Template_Management_TestcaseID_45969(self):
#         pass
#
#         common_method.tearDown()
#         data_sources_page.checkIfOnHomePage()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         text = "Address"
#         template_management.search_designs(text, 1)
#         template_management.wait_for_element_appearance_name_matches_all(text)
#         template_management.click_element_name_matches_all(text, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#         all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#
#         for text in all_names[:1]:
#             login_page.click_Menu_HamburgerICN()
#             template_management.click_common_designs_button()
#             template_management.wait_in_common_designs_until_load()
#
#             texts = "Address"
#             template_management.search_designs(texts, 1)
#             template_management.wait_for_element_appearance_name_matches_all(texts)
#             template_management.click_element_name_matches_all(texts, 0)
#
#             template_management.wait_until_designs_load_after_clicking_categories()
#             template_management.search_designs(text, 1)
#             template_management.wait_for_designs_in_comm_design()
#             full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#             original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#             """4. Type in unique name for the design. Click "Save"
#             this step is not applicable """
#
#             template_management.click_on_copy_to_my_designs()
#             try:
#                 common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#             except:
#                 raise Exception("design copied successfully is not displayed. is not displayed")
#             sleep(3)
#             template_management.click_left_arrow()
#             login_page.click_Menu_HamburgerICN()
#             template_management.click_my_designs_button()
#             common_method.wait_for_element_appearance_namematches("Showing")
#
#             try:
#                 full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#                 copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#             except:
#                 raise Exception("copied template not shown or is incorrect name")
#
#             if original_size != copy_size:
#                 raise Exception("copyied and original design sizes are not same")
#             try:
#                 if int(copy_lastdate) != 0:
#                     raise Exception("last printed date displayed for copied design without printing")
#             except:
#                 raise Exception("last printed date displayed for copied design without printing")
#
#             template_management.click_print_button_enabled()
#             try:
#                 template_management.wait_for_element_appearance_name_matches_all(text)
#                 template_management.scroll_till_print_enabled()
#             except:
#                 raise Exception("print page is not displayed properly")
#
#             prev_count = template_management.get_no_of_labels_left_in_print_page()
#             if not template_management.check_print_button_clickable:
#                 raise Exception("print option is not clickable")
#
#             template_management.click_print_button_enabled()
#
#             try:
#                 template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#                 sleep(3)
#             except:
#                 pass
#
#             common_method.wait_for_element_appearance_enabled("Print")
#
#             curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#             if not int(prev_count) == int(curr_count) + 1:
#                 raise Exception("no of labels not updated")
#
#             sleep(3)
#             template_management.click_left_arrow()
#             if not template_management.check_element_exists("My Designs"):
#                 template_management.click_left_arrow()
#
#             login_page.click_Menu_HamburgerICN()
#             template_management.click_home_button()
#             login_page.click_Menu_HamburgerICN()
#             template_management.click_my_designs_button()
#             sleep(2)
#
#             template_management.check_element_exists("My Designs")
#
#             full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#             pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#             cd, cm, cy = template_management.get_current_date()
#             if pd != cd or pm != cm or py != cy:
#                 raise Exception("dates are not matching")
#
#             login_page.click_Menu_HamburgerICN()
#             template_management.click_home_button()
#             sleep(1)
#
#             labels_left = template_management.get_no_of_left_cartridge()
#             if str(labels_left) != str(curr_count):
#                 raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45970(self):
#     pass
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "Barcodes"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#
#     for text in all_names[:1]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "Barcodes"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if int(copy_lastdate) != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#             template_management.scroll_till_print_enabled()
#         except:
#             raise Exception("print page is not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#             sleep(3)
#         except:
#             pass
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#         pm, pd, py = template_management.get_design_last_print_date(full_name)
#
#         cm, cd, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45971(self):
#     pass
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "File Folder"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#
#     for text in all_names[:1]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "File Folder"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if int(copy_lastdate) != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#             template_management.scroll_till_print_enabled()
#         except:
#             raise Exception("print page is not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#             sleep(3)
#         except:
#             pass
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#         pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#         cd, cm, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45972(self):
#     pass
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "Jewelry"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#
#     for text in all_names[:1]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "Jewelry"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if int(copy_lastdate) != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#             template_management.scroll_till_print_enabled()
#         except:
#             raise Exception("print page is not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#             sleep(3)
#         except:
#             pass
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#         pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#         cd, cm, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45973(self):
#     pass
#
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "Small Multipurpose"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#
#     for text in all_names[:1]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "Small Multipurpose"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if copy_lastdate != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#             template_management.scroll_till_print_enabled()
#         except:
#             raise Exception("print page is not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#             sleep(3)
#         except:
#             pass
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#         pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#         cd, cm, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45974(self):
#     pass
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "Multipurpose"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#     print(all_names)
#     for text in all_names[7:8]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "Multipurpose"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if int(copy_lastdate) != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             common_method.wait_for_element_appearance_namematches("Label")
#             template_management.scroll_till_print_enabled_button()
#         except:
#             raise Exception("print page not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete")
#             sleep(3)
#         except:
#             raise Exception("print notification not displayed after print")
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 1)
#         template_management.click_on_delete_button_in_designs()
#         template_management.click_on_delete_button_in_designs()
#         common_method.wait_for_element_appearance_namematches("removed")
#         sleep(2)
#         pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#         cd, cm, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
#
#
# def test_Template_Management_TestcaseID_45975(self):
#     pass
#
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_common_designs_button()
#     template_management.wait_in_common_designs_until_load()
#
#     text = "Shipping"
#     template_management.search_designs(text, 1)
#     template_management.wait_for_element_appearance_name_matches_all(text)
#     template_management.click_element_name_matches_all(text, 0)
#
#     template_management.wait_until_designs_load_after_clicking_categories()
#     all_designs_in_categories = template_management.get_all_designs_in_my_designs()
#     all_names = template_management.get_names_of_design_in_search_designs(all_designs_in_categories)
#
#     template_management.click_left_arrow()
#     login_page.click_Menu_HamburgerICN()
#     template_management.click_home_button()
#
#     for text in all_names[:1]:
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         texts = "Shipping"
#         template_management.search_designs(texts, 1)
#         template_management.wait_for_element_appearance_name_matches_all(texts)
#         template_management.click_element_name_matches_all(texts, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         template_management.search_designs(text, 1)
#         template_management.wait_for_designs_in_comm_design()
#         full_name = template_management.get_the_full_name_of_design_and_click_in_common_design_search(text, 1)
#         original_size, original_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         """4. Type in unique name for the design. Click "Save"
#         this step is not applicable """
#
#         template_management.click_on_copy_to_my_designs()
#         try:
#             common_method.wait_for_element_appearance_namematches("successfully copied to your workspace", 15)
#         except:
#             raise Exception("design copied successfully is not displayed. is not displayed")
#         sleep(3)
#         template_management.click_left_arrow()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         common_method.wait_for_element_appearance_namematches("Showing")
#
#         try:
#             full_name = template_management.get_the_full_name_of_design_and_click_in_my_design(text + " copy", 1)
#             copy_size, copy_lastdate = template_management.get_the_size_and_lastprint_of_design(full_name)
#
#         except:
#             raise Exception("copied template not shown or is incorrect name")
#
#         if original_size != copy_size:
#             raise Exception("copyied and original design sizes are not same")
#         if int(copy_lastdate) != 0:
#             raise Exception("last printed date displayed for copied design without printing")
#
#         template_management.click_print_button_enabled()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#             template_management.scroll_till_print_enabled()
#         except:
#             raise Exception("print page is not displayed properly")
#
#         prev_count = template_management.get_no_of_labels_left_in_print_page()
#         if not template_management.check_print_button_clickable:
#             raise Exception("print option is not clickable")
#
#         template_management.click_print_button_enabled()
#         common_method.wait_for_element_appearance_namematches("Label")
#         template_management.scroll_till_print_enabled_button()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all("Print complete", 10)
#             sleep(3)
#         except:
#             pass
#
#         common_method.wait_for_element_appearance_enabled("Print")
#
#         curr_count = template_management.get_no_of_labels_left_in_print_page()
#
#         if not int(prev_count) == int(curr_count) + 1:
#             raise Exception("no of labels not updated")
#
#         sleep(3)
#         template_management.click_left_arrow()
#         if not template_management.check_element_exists("My Designs"):
#             template_management.click_left_arrow()
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_my_designs_button()
#         sleep(2)
#
#         template_management.check_element_exists("My Designs")
#
#         full_name = template_management.select_design_in_my_design_by_name_and_return(text + " copy", 0)
#
#         pd, pm, py = template_management.get_design_last_print_date(full_name)
#
#         cd, cm, cy = template_management.get_current_date()
#         if pd != cd or pm != cm or py != cy:
#             raise Exception("dates are not matching")
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_home_button()
#         sleep(1)
#
#         labels_left = template_management.get_no_of_left_cartridge()
#         if str(labels_left) != str(curr_count):
#             raise Exception("labels left not updated")
"-------------------"


def test_Template_Management_TestcaseID_45930():
    test_steps = {
        1: [1, 'Go to My Designs'],
        2: [2, 'Select the design in the precondition, click Rename option\nCheck "Edit name" window is displayed'],
        3: [3, 'Input value of an existing design name in user\'s account\nVerify no error message is displayed.'],
        4: [4,
            'Click "Save" button\na. Verify "Edit name" window is closed.\nb. Verify notification alert "Design successfully renamed to <name>" is displayed. Click "x" button.\nc. Verify design\'s name is updated (Name used in step 3 appended with number (1)).'],
        5: [5,
            'Select again the design and click Rename option\na. Verify updated name is displayed\nb. Verify "Cancel" and "Save" buttons are clickable. Click "Cancel"']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_my_designs_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management_page_1.get_first_design_in_my_designs()
        print("1", name)
        name = template_management_page_1.get_names_of_design_in_search_designs([name])[0]
        print("2", name)
        names = template_management_page_1.get_ith_design_by_index_in_my_designs(2)
        print("3", names)
        names = template_management_page_1.get_names_of_design_in_search_designs([names])[0]
        print("4", names)
        data_sources_page.searchName(names)
        full_name = template_management_page_1.get_the_full_name_of_design_and_click_in_common_design_search(names, 1)
        print("5", full_name)
        template_management_page_1.click_on_rename_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        template_management_page_1.enter_text_in_rename_design(name)
        if template_management_page_1.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()
        template_management_page_1.click_on_save_button_in_rename_design()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management_page_1.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        data_sources_page.searchName("")
        try:
            full_name = template_management_page_1.get_the_full_name_of_design_and_click_in_common_design_search(
                name + " (1)",
                0)
        except:
            raise Exception("design not found after updating")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        template_management_page_1.get_the_full_name_of_design_and_click_in_common_design_search(name + " (1)", 1)
        template_management_page_1.click_on_rename_button()

        default_value = template_management_page_1.get_the_default_rename_text()
        if default_value != name + " (1)":
            raise Exception("default value not updated to new value")

        if not template_management_page_1.check_cancel_button_clickable_in_rename_popup():
            raise Exception("cancel button is not clickable")

        if not template_management_page_1.check_save_button_clickable_in_rename_popup():
            raise Exception("save button is not clickable")
        template_management_page_1.click_on_cancel_button_in_rename_popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_Template_Management_TestcaseID_45933():
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
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1
    try:
        # Step 1
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        common_method.wait_for_element_appearance_namematches("Recently")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2
        start_time = time.time()

        """Note: the design should be printed if not design rename will not be shown in recently printed labels"""
        name = template_management_page_1.get_all_designs_in_recently_printed_labels()
        name = template_management_page_1.get_names_of_design_in_search_designs(name)[0]
        full_name = template_management_page_1.get_the_full_name_of_design_and_click_in_recently_printed_design(name, 1)
        prev_size, prev_date = template_management_page_1.get_the_size_and_lastprint_of_design(full_name)
        template_management_page_1.click_on_rename_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3
        start_time = time.time()

        default_value = template_management_page_1.get_the_default_rename_text()
        if default_value != name:
            raise Exception("default value not matches the design's name")
        template_management_page_1.check_cancel_button_clickable()
        template_management_page_1.check_save_button_clickable()
        """Enter design which is present in user2"""
        user2_name = "user2"
        template_management_page_1.enter_text_in_rename_design(user2_name)
        if template_management_page_1.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4
        start_time = time.time()

        template_management_page_1.click_on_save_button_in_rename_design()
        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            sleep(2)
        except:
            raise Exception("design has been successfully renamed. is not displayed")
        if template_management_page_1.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")
        try:
            full_name = template_management_page_1.select_design_in_recetly_printed_design_by_name_and_return(
                user2_name, 1)
        except:
            raise Exception("design not found after updating")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5
        start_time = time.time()

        template_management_page_1.click_on_rename_button()
        curr_size, curr_date = template_management_page_1.get_the_size_and_lastprint_of_design(full_name)
        if curr_size != prev_size or curr_date != prev_date:
            raise Exception("size or date is not matching after renaming the design")
        invalid_name = "&*%"
        template_management_page_1.enter_text_in_rename_design(invalid_name)
        sleep(2)
        if not template_management_page_1.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not  displayed for invalid characters")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6
        start_time = time.time()

        template_management_page_1.click_on_cancel_button_in_rename_popup()
        try:
            full_name = template_management_page_1.select_design_in_recetly_printed_design_by_name_and_return(
                user2_name, 0)
        except:
            raise Exception("design not found after canceling rename")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

def test_Template_Management_TestcaseID_45967():
    test_steps = {
        1: [1, 'Go to Common Designs'],
        2: [2,
            'Scroll through the category list\na. Verify the following categories are displayed:\n- Address\n- Barcode\n- Jewelry\n- Multipurpose/Name Tag\n- Postage/Shipping\n- Return Address/File Folder\n- Round\n- Shipping\n- Small Multipurpose\n- XL Shipping\nb. Verify each category has description\nc. Verify each category has Zebra icon on the top left']
    }

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    strings = ["Address", "Barcodes", "Jewelry", "Shipping", "Return Address/File Folder", "Round", "Shipping",
               "Small Multipurpose", "XL Shipping"]
    login_page.click_Menu_HamburgerICN()
    template_management_page_1.click_common_designs_button()
    template_management_page_1.wait_in_common_designs_until_load()
    curr_categories = template_management_page_1.get_all_categories_in_common_designs()
    categories = template_management_page_1.get_names_of_design_in_search_designs(curr_categories)
    template_management_page_1.verify_if_categories_are_sorted(categories)
    print(categories)
    for i in strings:
        if i not in categories:
            error = i + " this category is not present in common designs"
            raise Exception(error)
    try:
        template_management_page_1.verify_zebra_icon_in_the_categories(curr_categories)
    except:
        raise Exception("zebra icon not present for some category")

    if not template_management_page_1.verify_description_present_in_the_categories(curr_categories):
        raise Exception("description not present for some category")

"""AEMS pending"""
"-------------------"
# def test_Template_Management_TestcaseID_45968():
#     test_steps = {
#         1: [1, 'Go to Common Designs'],
#         2: [2,
#             'Select Address category\na. Verify "Address" category text is displayed\nb. Verify arrow back button is displayed'],
#         3: [3,
#             'Scroll through the design list\na. Verify only the designs belonging to the category are displayed\nb. Verify designs are sorted from A to Z\nc. Verify designs information (Name, Size, Thumbnail) are displayed\nd. Verify "Last Print" information is NOT displayed\ne. Verify 3-dot menu on the top left of the designs are clickable'],
#         4: [4,
#             'Click on each design\nVerify only the following option is displayed and clickable: Print, Copy to My Designs'],
#         5: [5, 'Click Category\'s arrow back button\nVerify Common Designs view is displayed']
#     }
#
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#     temp = ["Address", "Barcodes", "Jewelry", "Multipurpose", "Shipping", "File Folder", "Round", "Shipping",
#             "Small Multipurpose"]
#     for text in temp[0:2]:
#
#         login_page.click_Menu_HamburgerICN()
#         template_management.click_common_designs_button()
#         template_management.wait_in_common_designs_until_load()
#
#         template_management.search_designs(text, 1)
#         template_management.wait_for_element_appearance_name_matches_all(text)
#         template_management.click_element_name_matches_all(text, 0)
#
#         template_management.wait_until_designs_load_after_clicking_categories()
#         try:
#             template_management.wait_for_element_appearance_name_matches_all(text)
#         except:
#             raise Exception(text, "this category text not displayed")
#         if not template_management.check_left_arrow_exists():
#             raise Exception("left arrow is not present")
#
#         all_complete_designs = template_management.get_all_designs_in_my_designs()
#         all_designs = template_management.get_names_of_design_in_search_designs(all_complete_designs)
#         all_designs = template_management.make_everything_lower_case(all_designs)
#         sorted_design = all_designs
#         sorted_design = sorted(sorted_design)
#         print(all_designs)
#         print("\n", sorted_design)
#         """Commented code currently cannot be verified since labels are not sorted properly"""
#         if all_designs != sorted_design:
#             raise Exception("designs are not in sorted order")
#
#         for i in all_complete_designs:
#             name, size, lastprint = template_management.get_the_name_size_and_lastprint_of_design(i)
#             if int(lastprint) != 0:
#                 raise Exception("last print displayed for", i, "design")
#
#         template_management.scroll_till_element(all_designs[0], 1)
#
#         for i in all_complete_designs[:2]:
#             template_management.click_on_the_element_in_categories(i)
#             try:
#                 common_method.wait_for_element_appearance_enabled("Print")
#             except:
#                 raise Exception("Print button not clickable in common design")
#             try:
#                 common_method.wait_for_element_appearance_enabled("Copy to My Designs")
#             except:
#                 raise Exception("Copy to My design button not clickable in common design")
#
#             template_management.click_left_arrow()
#
#         template_management.click_left_arrow()
#
#         if not template_management.check_element_exists("Common Designs"):
#             raise Exception("common designs page is not displayed after clicking left arrow")


def test_Template_Management_TestcaseID_45926():
    pass
    test_steps = {
        1: [1, 'Go to My Designs'],
        2: [2,
            'Select the design in the precondition, click Rename option\na. Verify "Edit name" window is displayed\nb. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed\nc. Verify default value matches the design\'s name\nd. Verify "Cancel" button is clickable and "Save" button is clickable'],
        3: [3, 'Input unique name\nVerify no error message is displayed'],
        4: [4,
            'Click "Save" button\na. Verify "Edit name" window is closed\nb. Verify toast alert "design has been successfully renamed." is displayed\nc. Verify design\'s name is updated\nd. Verify design\'s information (Size, Thumbnail, Last Print) are NOT updated'],
        5: [5, 'Also check entering special characters \\ / can\'t work for rename feature in My design']
    }
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]
    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1
    try:
        # Step 1
        start_time = time.time()
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """a. Verify "Edit name" window is displayed not in mobile app"""
        """Save" button is NOT clickable (is clickable in mobile)"""

        login_page.click_Menu_HamburgerICN()
        template_management_page_1.click_my_designs_button()
        common_method.wait_for_element_appearance_namematches("Showing")
        """Give the name of existing design here"""
        name = template_management_page_1.get_first_design_in_my_designs()
        name = template_management_page_1.get_names_of_design_in_search_designs([name])[0]
        full_name = template_management_page_1.select_design_in_my_design_by_name_and_return(name, 1)
        prev_size, prev_date = template_management_page_1.get_the_size_and_lastprint_of_design(full_name)

        template_management_page_1.click_on_rename_button()

        """need to automate a. Verify "Edit name" window is displayed
        b. Verify "Organize your designs by giving it a name to help you find it faster." text is displayed"""
        default_value = template_management_page_1.get_the_default_rename_text()
        if default_value != name:
            raise Exception("default value not matches the design's name")

        template_management_page_1.check_cancel_button_clickable()

        template_management_page_1.check_save_button_clickable()

        template_management_page_1.enter_text_in_rename_design("\/")
        sleep(2)
        if not template_management_page_1.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error not displayed for invalid characters")

        new_name = "somenamemyown_45926"

        template_management_page_1.enter_text_in_rename_design(new_name)
        sleep(1)
        if template_management_page_1.check_error_for_invalid_characters_in_rename_design():
            raise Exception("error displayed for valid characters")

        template_management_page_1.click_on_save_button_in_rename_design()

        try:
            common_method.wait_for_element_appearance_namematches("Design has been successfully rename", 15)
            sleep(1)
        except:
            raise Exception("design has been successfully renamed. is not displayed")

        if template_management_page_1.check_cancel_button_clickable_in_rename_popup():
            raise Exception("rename popup not closed")

        try:
            full_name = template_management_page_1.select_design_in_my_design_by_name_and_return(new_name, 0)
        except:
            raise Exception("design not found after updating")

        curr_size, curr_date = template_management_page_1.get_the_size_and_lastprint_of_design(full_name)

        if curr_size != prev_size or curr_date != prev_date:
            raise Exception("size or date is not matching after renaming the design")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        if screenshot_path not in uploaded_files:
            upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time, uploaded_files)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
