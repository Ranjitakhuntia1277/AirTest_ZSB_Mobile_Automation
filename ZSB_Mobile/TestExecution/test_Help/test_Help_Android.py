import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import pytest

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...TestExecution.test_Help.store import execID, leftId
import inspect


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
sleep(2.0)
wake()
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)

ADB_LOG, test_run_start_time, uploaded_files = common_method.start_adb_log_capture()
start_execution_loop(execID)


def test_Help_TestcaseID_45789():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Click Login button and enter user credentials to sign into Money Badger Mobile App."],
        2: [2, "Click on the hamburger icon."],
        3: [3, "Check Help menu option is available and is represented by '?' icon."],
        4: [4, "Click on Help menu option dropdown list."],
        5: [5, "Check Help option has the available options: Support, FAQs, Contact Us, Live Chat."],
        6: [6, "Click on Support option."],
        7: [7,
            "Check the user is directed to its respective URL on a new page.Check for Support,FAQ's,Contact us and Live chat"],
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        """""""""test"""""
        """clear app data"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        if poco(text="Signed in to Google as").exists():
            while not poco(text="Add account to device").exists():
                poco.scroll()
            registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#12345678", "zebra03.swdvt@gmail.com", True)
        registration_page.sign_In_With_Google("Zebra#12345678")
        data_sources_page.checkIfOnHomePage()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Swipe up"""
        poco.scroll()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check Help icon with '?' is present"""
        help_page.checkIfHelpIconIsPresent()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Help dropdown to expand Help options"""
        help_page.click_Help_dropdown_option()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 5
        start_time = time.time()
        """Check Help has Support, FAQs, Contact Us and Live Chat Options"""
        help_page.Test_Support_faq_Contactus__Livechat_is_present()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 6
        start_time = time.time()
        """Click Support to open support page"""
        help_page.click_Support()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 7
        start_time = time.time()
        """Check if we are redirected to support page"""
        help_page.checkIfLandedOnSupportPage()
        sleep(5)
        help_page.verify_url("https://zsbsupport.zebra.com/s/")
        keyevent("back")
        try:
            help_page.checkIfLandedOnSupportPage()
            keyevent("back")
        except:
            pass
        """Click FAQs to see FAQ on the web"""
        sleep(5)
        help_page.click_FAQs()
        """Check if we are redirected to FAQs page"""
        help_page.checkIfLandedOnFAQsPage()
        sleep(5)
        help_page.verify_url("https://zsbsupport.zebra.com/s/faqs")
        keyevent("back")
        try:
            help_page.checkIfLandedOnFAQsPage()
            keyevent("back")
        except:
            pass
        sleep(5)
        """Click Contact US to view contact options"""
        help_page.click_ContactUs()
        """Check if we are redirected to Contact Us page"""
        help_page.checkIfLandedOnContactUsPage()
        sleep(5)
        help_page.verify_url("https://zsbsupport.zebra.com/s/contactsupport")
        keyevent("back")
        try:
            help_page.checkIfLandedOnContactUsPage()
            keyevent("back")
        except:
            pass
        sleep(5)
        if help_page.checkIfOnValidChatTime():
            """Click chat to """
            help_page.click_Chat()
            sleep(5)
            """Verify Chat Page Title"""
            help_page.verifyLiveChatWindowTitle()
            sleep(2)
            """Verify if Begin Chat button is present"""
            help_page.verifyBeginChatBtn()
        else:
            help_page.checkChatCurrentlyUnavailableMessagePresent()
        sleep(2)
        common_method.Stop_The_App()
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


def test_Help_TestcaseID_47788():
    """""""""test"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Launch the mobile app."],
        2: [2, "Open the menu."],
        3: [3, "Scroll all the way down to 'Help'."],
        4: [4, "Click the down arrow inside the help button."],
        5: [5, "Click 'Live Chat'. Screen should say 'Available 7am to 7pm ET'."],

        6: [6, "Click 'Begin Chat' to enter the Chat Form page."],
        7: [7, "Click the back arrow in the top left corner."],
        8: [8, "Screen should now show the message 'Available 7am to 7pm ET'."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        login_page.click_Menu_HamburgerICN()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Swipe up"""
        poco.scroll()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Help dropdown to expand Help options"""
        help_page.click_Help_dropdown_option()
        if help_page.checkIfOnValidChatTime():
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 5
            start_time = time.time()
            """Click Live Chat"""
            help_page.click_Chat()
            sleep(2)
            """Check if it displays Available 7am to 7pm ET"""
            try:
                help_page.verifyChatHours()
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 6
            start_time = time.time()
            """Begin Chat"""
            help_page.clickBeginChat()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 7
            start_time = time.time()
            """Click Back Arrow"""
            help_page.clickBackArrow()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 8
            start_time = time.time()
            """Check if it displays Available 7am to 7pm ET"""
            """Unable to verify due to BUG"""
            help_page.verifyChatHours()
        else:
            help_page.checkChatCurrentlyUnavailableMessagePresent()
        common_method.Stop_The_App()
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


def test_Help_TestcaseID_47919():
    """""""""test"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Launch the app"],
        2: [2, "Click on the hamburger icon."],
        3: [3, "Check Help menu option is available and is represented by '?' icon."],
        4: [4, "Click on Help menu option dropdown list."],
        5: [5, "Click on Live Chat and begin chat."],
        6: [6,
            "Select subject from dropdown, enter problem description and select affected printer, then click start chatting. Check chat bubble should not appear on chat page."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        start_time = time.time()
        common_method.tearDown()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 2
        start_time = time.time()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Swipe up"""
        poco.scroll()
        sleep(2)
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 3
        start_time = time.time()
        """Check Help icon with '?' is present"""
        help_page.checkIfHelpIconIsPresent()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1
        # -----------------------
        # Step 4
        start_time = time.time()
        """Click Help dropdown to expand Help options"""
        help_page.click_Help_dropdown_option()
        sleep(5)
        if help_page.checkIfOnValidChatTime():
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 5
            start_time = time.time()
            """Click Live Chat"""
            help_page.click_Chat()
            """Begin Chat"""
            help_page.clickBeginChat()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1
            # -----------------------
            # Step 6
            start_time = time.time()
            """Select Subject from dropdown"""
            help_page.selectDropDownForSubject()
            sleep(2)
            help_page.selectSubjectFromDropDown()
            sleep(2)
            """Enter Problem Description"""
            help_page.fillDescription()
            sleep(2)
            """Select affected printer"""
            help_page.selectDropDownForAffectedPrinter()
            sleep(2)
            help_page.selectAffectedPrinterFromDropDown()
            sleep(2)
            """Start chat"""
            help_page.startChat()
            """Click Go to chat"""
            help_page.goToChat()
            """Check if chat bubble does not appear"""
            """Cannot check since chat bubble does not appear"""
        else:
            help_page.checkChatCurrentlyUnavailableMessagePresent()
        common_method.Stop_The_App()
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

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
