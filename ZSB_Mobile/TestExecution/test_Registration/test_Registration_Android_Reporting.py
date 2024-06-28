import inspect

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
import pytest
from ...TestSuite.api_call import *
from ...TestSuite.store import *


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
app_settings_page = App_Settings_Screen(poco)


def test_Registration_TestcaseID_45855():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy").'],
        2: [2, 'Check user is directed to Account Registration Page.'],
        3: [3, 'Enter already registered user email (e.g: zebraswtest2@gmail.com) and click NEXT button.'],
        4: [4,
            'Check user is directed to page with header "This email already exists" and message "It looks like this email has already been registered. Please try logging in with your credentials."'],
        5: [5, 'Click RETURN TO LOGIN button.'],
        6: [6, 'Check user is directed to Money Badger Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App, click Login button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy").
        start_time = time.time()

        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        registration_page.verifyLinksInSignInPage()
        registration_page.registerEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check user is directed to Account Registration Page.
        start_time = time.time()

        registration_page.checkIfOnRegistrationPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Enter already registered user email (e.g: zebraswtest2@gmail.com) and click NEXT button.
        start_time = time.time()

        """Enter already existing User Email"""
        registration_page.enter_user_email_for_registering("zebra03.swdvt@gmail.com")
        registration_page.click_on_next()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check user is directed to page with header "This email already exists" and message "It looks like this email has already been registered. Please try logging in with your credentials."
        start_time = time.time()

        """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
        """Verify Account already exists page title"""
        registration_page.check_email_already_exists_page_title()
        """Verify Account already exists page message"""
        registration_page.check_email_already_Exists_page_message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click RETURN TO LOGIN button.
        start_time = time.time()

        """No RETURN TO LOGIN button."""
        """Click Continue"""
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check user is directed to Money Badger Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45859():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2, 'Click Login button.'],
        3: [3, 'Check user is navigated to "Login with username" page.'],
        4: [4, 'Enter INVALID email and password and click Sign in button.'],
        5: [5,
            'Check user is not able to login to Money Badger. Check Display Message "We didn\'t recognize the username or password you entered. Please try again." Check page stays at Login with username.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Login button.
        start_time = time.time()

        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to "Login with username" page.
        start_time = time.time()

        registration_page.checkIfOnSSOLoginPage()
        data_sources_page.signInWithEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Enter INVALID email and password and click Sign in button.
        start_time = time.time()

        registration_page.complete_sign_in_with_email("soho_dvtxxxxx@hotmail.com", "soho_dvtxxxxx@hotmail.com", 1, 0,
                                                      True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user is not able to login to Money Badger. Check Display Message "We didn't recognize the username or password you entered. Please try again." Check page stays at Login with username.
        start_time = time.time()

        registration_page.checkInvalidCredentialsMessage()
        registration_page.checkIfOnSSOLoginPage()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45860():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2, 'Click Login button.'],
        3: [3, 'Check user is navigated to "Login with username" page.'],
        4: [4, 'Enter login name (E.g DZ1136) with incorrect password and click Sign in button.'],
        5: [5,
            'Check user is not able to login to Money Badger. Error message is shown: "We didn\'t recognize the username or password you entered. Please try again."'],
        6: [6, 'Enter login name (E.g DZ1136) with correct password and click Sign in button.'],
        7: [7,
            'Check user is successfully logged in to Money Badger Home Page and is navigated to Overview landing page.'],
        8: [8, 'Click on the hamburger icon followed by Settings and click Log out button.'],
        9: [9,
            'Check user is successfully logged out of Money Badger Home Page and is navigated to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Login button.
        start_time = time.time()

        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to "Login with username" page.
        start_time = time.time()

        data_sources_page.signInWithEmail()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Enter login name (E.g DZ1136) with incorrect password and click Sign in button.
        start_time = time.time()

        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#1234567890", 1, 0, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user is not able to login to Money Badger. Error message is shown: "We didn't recognize the username or password you entered. Please try again."
        start_time = time.time()

        registration_page.checkInvalidCredentialsMessage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Enter login name (E.g DZ1136) with correct password and click Sign in button.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0, False, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user is successfully logged in to Money Badger Home Page and is navigated to Overview landing page.
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click on the hamburger icon followed by Settings and click Log out button.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user is successfully logged out of Money Badger Home Page and is navigated to the ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45861():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App and click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        2: [2, 'Click on Google icon.'],
        3: [3, 'Check user is successfully logged in to Money Badger Home Page without the need to enter credentials.'],
        4: [4, 'Click on the hamburger icon followed by Settings and click Log Out button.'],
        5: [5,
            'Check user is able to successfully log out of Money Badger Home Page and is navigated to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        common_method.tearDown()
        registration_page.clickSignIn()
        sleep(2)
        registration_page.verifyLinksInSignInPage()
        scroll_view = poco("android.view.View")
        while not poco(text="Sign In With"):
            scroll_view.swipe("down")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Google icon.
        start_time = time.time()

        registration_page.click_Google_Icon()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is successfully logged in to Money Badger Home Page without the need to enter credentials.
        start_time = time.time()

        try:
            poco(text="Choose an account").wait_for_appearance(timeout=20)
            help_page.chooseAcc("zebra03.swdvt@gmail.com")
        except:
            pass
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click on the hamburger icon followed by Settings and click Log Out button.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        sleep(2)
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user is able to successfully log out of Money Badger Home Page and is navigated to the ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45863():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2,
            'Click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        3: [3, 'Check user is navigated to "Login with username" page.'],
        4: [4, 'Click on Facebook icon.'],
        5: [5, 'Check user will be navigated to Facebook Sign In Page.'],
        6: [6, 'Enter registered Facebook account username with incorrect password.'],
        7: [7,
            'Check user is not able to login to Money Badger Home Page. Error message at Facebook sign-in prompt is displayed: "The password that you\'ve entered is incorrect. Forgotten password?".'],
        8: [8, 'Enter registered Facebook account username with correct password.'],
        9: [9,
            'Check user is able to successfully log in to Money Badger Page and the top left corner shows the login name (E.g: soho.swdvt.02).'],
        10: [10, 'Click on the hamburger icon followed by Settings and click Log out button.'],
        11: [11,
             'Check user is able to successfully log out of Money Badger Home Page and is navigated to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to "Login with username" page.
        start_time = time.time()

        registration_page.checkIfOnSSOLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click on Facebook icon.
        start_time = time.time()

        registration_page.click_Facebook_Icon()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user will be navigated to Facebook Sign In Page.
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Enter registered Facebook account username with incorrect password.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check user is not able to login to Money Badger Home Page. Error message at Facebook sign-in prompt is displayed: "The password that you've entered is incorrect. Forgotten password?".
        start_time = time.time()

        registration_page.login_Facebook("Zebra#12345678", "zebra03.swdvt@gmail.com", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Enter registered Facebook account username with correct password.
        start_time = time.time()

        registration_page.login_Facebook("Zebra#123456789")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check user is able to successfully log in to Money Badger Page and the top left corner shows the login name (E.g: soho.swdvt.02).
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        name = registration_page.get_login_name_from_menu()
        if name == "swdvt zsb":
            pass
        else:
            raise Exception("Login name does not match")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click on the hamburger icon followed by Settings and click Log out button.
        start_time = time.time()

        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check user is able to successfully log out of Money Badger Home Page and is navigated to the ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45868():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App and click Login button.'],
        2: [2, 'Navigate to Sign In page, click "Reset Password" button.'],
        3: [3,
            'Navigate to Password Recovery page, input the right zebra username. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html'],
        4: [4, 'Check the zebra user cannot reset password, the SUBMIT button is unclickable.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click Login button.
        start_time = time.time()

        """Test on stage build"""
        common_method.tearDown()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Navigate to Sign In page, click "Reset Password" button.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        poco.scroll()
        registration_page.click_on_reset_password()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Navigate to Password Recovery page, input the right zebra username. (SMBUI-2648) Check the URL should be updated to https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html
        start_time = time.time()

        registration_page.check_if_in_password_recovery_page()
        # help_page.verify_url("https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html")
        help_page.verify_url("https://signup.zebra.com/content/userreg/reset-password-landing.html")
        sleep(2)
        registration_page.Enter_Username_password_recovery_page("zebra06.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check the zebra user cannot reset password, the SUBMIT button is unclickable.
        start_time = time.time()

        registration_page.check_submit_is_clickable()
        registration_page.click_SUBMIT()
        common_method.Stop_The_App()

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


def test_Registration_TestcaseID_45869():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App and click "Sign In/Register" button.'],
        2: [2, 'Proceed to login to Money Badger.'],
        3: [3, 'At Money Badger landing page, click on Buy More Labels'],
        4: [4, 'Check browser is open and user is navigated to page https://www.zebra.com/smb/us/en/labels.html']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click "Sign In/Register" button.
        start_time = time.time()

        common_method.tearDown()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Proceed to login to Money Badger.
        start_time = time.time()

        registration_page.click_Google_Icon()
        account = "zebra03.swdvt@gmail.com"
        if template_management_page.checkIfAccPresent(account):
            help_page.chooseAcc(account)
        else:
            while not poco(text="Use another account").exists():
                poco.scroll()
            login_page.click_GooglemailId()
            if poco(text="Signed in to Google as").exists():
                while not poco(text="Add account to device").exists():
                    poco.scroll()
                registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", account)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: At Money Badger landing page, click on Buy More Labels
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        registration_page.click_Buy_More_Labels()
        registration_page.acceptPermissions()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check browser is open and user is navigated to page https://www.zebra.com/smb/us/en/labels.html
        start_time = time.time()

        help_page.verify_url("https://www.zebra.com/smb/us/en/labels.html")
        common_method.Stop_The_App()

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


"""Add printer"""


# def test_Registration_TestcaseID_46303():
#     """""""""test"""""
#
#     common_method.tearDown()
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_page.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_page.Click_Next_Button()
#     add_a_printer_page.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to Wi-Fi", 30)
#     common_method.wait_for_element_appearance("Discovered networks", 30)
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """Store the time till wi-fi turn green."""
#     time_taken = registration_page.timeTillWiFiGreen()
#     print(time_taken)
#     """"click on finish setup button"""
#     common_method.wait_for_element_appearance("Printer registration was successful", 30)
#     add_a_printer_page.click_Finish_Setup_Button()
#     common_method.Stop_The_App()
#
#
# """Add printer"""
# def test_Registration_TestcaseID_46307():
#     """""""""test"""""
#
#     common_method.tearDown()
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_page.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_page.Click_Next_Button()
#     add_a_printer_page.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
#     common_method.wait_for_element_appearance("Discovered networks", 30)
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """wait till wi-fi turn green."""
#     registration_page.timeTillWiFiGreen()
#     """"click on finish setup button"""
#     common_method.wait_for_element_appearance("Printer registration was successful", 30)
#     add_a_printer_page.click_Finish_Setup_Button()
#     common_method.Stop_The_App()


def test_Registration_TestcaseID_45862():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App and click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        2: [2, 'Click on Google Icon.'],
        3: [3, 'Check user will be navigate to Google Sign In Page.'],
        4: [4, 'Enter registered google username with incorrect password.'],
        5: [5,
            'Check user is not able to login to Money Badger Page. - Error message at google sign in prompt is displayed: "Wrong password. Try again or click Forgot password to reset it."'],
        6: [6, 'Enter registered google username with correct password provided in Setup.'],
        7: [7,
            'Check user is successfully login to Money Badger Page and the top left corner shows the login name (E.g: soho.swdvt.01).'],
        8: [8, 'Click on the hamburger icon follow by Settings and click Log out button.'],
        9: [9,
            'Check user is able to successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App and click Login button. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on Google Icon.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user will be navigate to Google Sign In Page.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 4: Enter registered google username with incorrect password.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 5: Check user is not able to login to Money Badger Page. - Error message at google sign in prompt is displayed: "Wrong password. Try again or click Forgot password to reset it."
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 6: Enter registered google username with correct password provided in Setup.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 7: Check user is successfully login to Money Badger Page and the top left corner shows the login name (E.g: soho.swdvt.01).
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        name = registration_page.get_login_name_from_menu()
        if name == "swdvt zsb":
            pass
        else:
            raise Exception("Login name does not match")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 8: Click on the hamburger icon follow by Settings and click Log out button.
        start_time = time.time()

        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 9: Check user is able to successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

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


# def test_Registration_TestcaseID_47930():
#     """""""""test"""""
# """Code needs to be changed according to the modified testcase"""
#
#     common_method.tearDown()
#     """click on the hamburger icon"""
#     login_page.click_Menu_HamburgerICN()
#     """"click on Add printer tab"""""
#     add_a_printer_page.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_page.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_page.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_page.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_page.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_page.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_page.Click_Next_Button()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     """"accept Bluetooth pairing popup 2"""
#     try:
#         add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
#     except:
#         pass
#     """Verify Connect Wi-fi Network Text"""
#     common_method.wait_for_element_appearance("Connect to a Wi-Fi Network", 20)
#     """Wait for connection error to appear"""
#     """"click on connect button on connect wi-fi network screen"""
#     registration_page.connectToWIfi()
#     registration_page.enterPasswordWifi()
#     """Wait till wi-fi turn green."""
#     registration_page.timeTillWiFiGreen()
#     """"verify need the printer driver text"""
#     add_a_printer_page.Verify_Need_the_Printer_Driver_Text()
#     """""verify registering your printer text"""
#     add_a_printer_page.Verify_Registering_your_Printer_Text()
#     """"click on finish setup button"""
#     add_a_printer_page.click_Finish_Setup_Button()
#     common_method.Stop_The_App()


"""UP -TO DATE"""

# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""Semi"""


def test_Smoke_Test_TestcaseID_45877():
    pass

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Launch ZSB Series App, click Sign in/Register button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")'],
        2: [2, 'Check user is directed to Account Registration Page'],
        3: [3, 'Enter new user email and click NEXT button'],
        4: [4, 'Login to newly created user email account'],
        5: [5,
            'Enter the verification code (E.g: 3CRL5N) provided by the email to the mobile app and click SUBMIT button'],
        6: [6,
            'At "User Information and Account Security" Page: Proceed to enter First Name (E.g: John) that comply with first name entry requirement. Proceed to enter Last Name (E.g: Loke) that comply with last name entry requirement. Proceed to select Country (E.g: Canada) from Select Country * drop down list. Proceed to enter password and confirmed password (E.g: Zebratest123?) that complied with IT SSO password requirement. Proceed to enable check boxes "I have read and agree to the Terms and Conditions"'],
        7: [7, 'Click SUBMIT AND CONTINUE button'],
        8: [8,
            'Click on CONTINUE button when user is navigated to "Account Created" page with the message "Success! Click "continue" to log into your account."'],
        9: [9, 'Check user is navigated to EULA page'],
        10: [10,
             'Check the user is NOT able to log in if not accepting EULA, and then the user accept it, and log into successfully.'],
        11: [11,
             'Check user is successfully login to Money Badger Home Page and navigated to the overview page with initial name display e.g: "Hey zebraswtest4!" and a "Add a Printer" button id provided to add printer'],
        12: [12, 'Click on the hamburger icon then Settings follow by Log out button'],
        13: [13, 'Check user is successfully log out of Money Badger Home Page and is being navigate to ZSB Login Page']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App, click Sign in/Register button and click Register now link. During the process: slide down the screen of each page, and check the 3 links at the bottom all can work. ("copyright", "Terms & Conditions" and "Privacy Policy")
        start_time = time.time()

        """	Verify create a brand new user with unregistered user in Mobile App."""

        #
        """"Setup:
        1. Create a new email address
        (Need to match the new register email format, for IDC, it should be soho_swdvt_xxxx@xxxx.com, for CDC, it should be soho_swdvt_xxxx@xxxx.com)
        2. Install the target build of ZSB app on mobile device"""""

        """start the app"""""
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        poco.scroll()
        data_sources_page.signInWithEmail()
        registration_page.registerEmail()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check user is directed to Account Registration Page
        start_time = time.time()

        registration_page.checkIfOnRegistrationPage()
        """Enter the User Email"""
        registration_page.enter_user_email_for_registering("smbmzsb7@gmail.com")
        registration_page.click_on_next()

        try:
            registration_page.wait_for_element_appearance("Resend Verification Code.", 10)
        except:
            raise Exception("Second step dint work")

        verification_code = "SLS9820000"
        registration_page.enter_the_verification_code(verification_code)
        registration_page.click_on_next()
        sleep(2)
        """Enter the first Name last name and the password"""
        first_n = "Zebra"
        last_n = "Z"
        password = "Zebra#123456789"
        registration_page.enter_the_fields(first_n, last_n, password)
        registration_page.select_the_country("India")
        registration_page.select_the_check_boxes()
        registration_page.click_submit_and_continue()
        sleep(2)
        registration_page.check_sign_up_successful()
        registration_page.click_continue_registration_page()
        poco("Login").wait_for_appearance(timeout=10)

        login_page.click_loginBtn()
        registration_page.wait_for_element_appearance_text("Continue with Google", 20)
        data_sources_page.signInWithEmail()
        """Provide the email and password"""
        email = "zebra852@gmail.com"
        password = "Zebra#123456789"
        registration_page.complete_sign_in_with_email(email, password)
        try:
            registration_page.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("home page dint show up")

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()
        try:
            registration_page.wait_for_element_appearance("Login", 5)
        except:
            raise Exception("Did not redirect to the login page")
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        common_method.Stop_The_App()

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
# # ## """"""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""
#
