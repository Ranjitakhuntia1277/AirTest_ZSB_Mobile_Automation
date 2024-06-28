import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Social_Login.Social_Login import Social_Login
from ...Common_Method import *
import os
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Others.Others import Others

import tkinter as tk
from tkinter import simpledialog
from ...TestSuite.api_calls import *
from ...TestSuite.store import *
import inspect
from ...TestSuite.store import *


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring("Input", "Please enter your value:")
    return user_input


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
# sleep(3.0)

login_page = Login_Screen(poco)
social_login = Social_Login(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
others = Others(poco)
data_sources_page = Data_Sources_Screen(poco)


class test_Android_Social_Login():
    pass

    def setup_logout(self):
        stop_app("com.zebra.soho_app")
        start_app("com.zebra.soho_app")
        sleep(5)

        try:
            others.wait_for_element_appearance("Sign In", 20)
        except:
            pass

        try:
            common_method.wait_for_element_appearance_namematches("Home", 20)
            login_page.click_Menu_HamburgerICN()
            others.click_on_profile_edit()
            others.scroll_down()
            others.click_log_out_button()
        except:
            pass

    def test_Social_Login_TestcaseID_48464(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button'],
            2: [2, 'When the login page shows up, check below items:\n'
                   '- Check there is a Zebra icon on the top of the page\n'
                   '- Check under the Sign in With option, there are Google/Apple/Facebook login options\n'
                   '- Check under the "-OR-" option, there is a "Sign in with your email" option\n'
                   '- Check under the "Sign in with your email" option, there is a "Learn more about the Benefits of Creating a Free ZSB Account", and the "Benefits of Creating a Free Account" is highlighted in blue\n'
                   '- Check there is a paragraph to clarify the user cookies, the wording like "This site uses cookies to manage user authentication, analytics, and to provide an improved digital experience. You can learn more about the cookies we use as well as how you can change your cookie settings by clicking here. By continuing to use this site without changing your settings, you are agreeing to our use of cookies. Review Zebra\'s Privacy Statement to learn more."\n'
                   '- Check under the wording, there are three options highlighted in blue, Zebra.com, Legal Notice and Privacy Statement'],
            3: [3, 'Check the whole login page looks coordinated']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1

        try:
            # Step 1: Launch the ZSB Series app, click on Login button
            start_time = time.time()
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
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: When the login page shows up, check below items
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            res = social_login.check_zebra_logo()
            if not res:
                raise Exception("Zebra logo not present")

            res = social_login.check_login_with_google()
            if not res:
                raise Exception("Login with google not present")

            res = social_login.check_login_with_apple()
            if not res:
                raise Exception("Login with Apple not present")

            res = social_login.check_login_with_facebook()
            if not res:
                raise Exception("Login with Facebook not present")

            res = social_login.check_sign_in_with_email()
            if not res:
                raise Exception("Sign in with email not present")

            res = social_login.check_text_of_free_benifits()
            if not res:
                raise Exception(
                    "Check under the Sign in with your email option, there is a Learn more about the Benefits of Creating a Free ZSB Account, and the Benefits of Creating a Free Account is highlighted in blue")

            social_login.scroll_down(1)

            social_login.check_the_cookie_text()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check the whole login page looks coordinated
            start_time = time.time()
            res = social_login.check_options_under_cookie_text()
            if not res:
                raise Exception("options are not proper or missing")

            common_method.tearDown()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            # If an error occurs, mark the step as "Fail" and include the error message
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48465(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   'Check the login page shows up correctly'],
            2: [2, 'Click on the "Benefits of Creating a ZSB Account" option\n'
                   'Check the page pops up'],
            3: [3, 'Check there are two parts on the page\n'
                   '- Part 1 is "Create, design and print labels from your PC or Mac.", the detailed description is "Design custom labels from scratch and print using the ZSB Label Designer on your PC or Mac."\n'
                   '- Part 2 is "Create a free Zebra account and register your printer for access to:", the detailed description is like below:\n'
                   '  - Create and design labels in your own web-based custom workspace.\n'
                   '  - Thousands of pre-made design templates with high-quality artwork perfect for home or business use.\n'
                   '  - Automatic software updates with the latest features and bug fixes.\n'
                   '  - And much more!'],
            4: [4, 'Check there is a related picture beside both parts'],
            5: [5, 'Check there is a back button on the "Benefits of Creating a ZSB Account" page'],
            6: [6, 'Click on the back button\n'
                   'Check it will back to sign in page']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app, click on Login button, check the login page shows up correctly
            start_time = time.time()
            common_method.tearDown()
            self.setup_logout()
            try:
                social_login.click_on_allow_for_notification()
            except:
                pass
            login_page.click_loginBtn()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on the "Benefits of Creating a ZSB Account" option, check the page pops up
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            social_login.click_on_benefits_of_zebra_account()
            sleep(2)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check there are two parts on the page
            start_time = time.time()
            res = social_login.check_the_text_of_benefits_of_free_account_page()
            if not res:
                raise Exception("the page text dint match")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Check there is a related picture beside both parts
            start_time = time.time()
            social_login.scroll_up(1)
            social_login.check_both_images_in_benefits_of_free_account_page()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Check there is a back button on the "Benefits of Creating a ZSB Account" page
            start_time = time.time()
            res = social_login.check_the_back_button()
            if not res:
                raise Exception("No back button")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Click on the back button, check it will back to sign in page
            start_time = time.time()
            social_login.click_on_the_back_button()
            res = social_login.check_login_with_google()
            if not res:
                raise Exception("6. Click on the back button Check it will back to sign in page fails")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48466(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   'Check the login page shows up correctly'],
            2: [2, 'Click on the "Zebra.com" link\n'
                   'Check it will open the correct page "https://www.zebra.com"'],
            3: [3, 'Click on the "Legal Notice" link\n'
                   'Check it will open the correct page "https://www.zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html"'],
            4: [4, 'Click on the "Privacy Statement" link\n'
                   'Check it will open the correct page "https://www.zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html"']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app, click on Login button, check the login page shows up correctly
            start_time = time.time()
            self.setup_logout()

            login_page.click_loginBtn()
            data_sources_page.lock_phone()
            wake()
            sleep(2)
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on the "Zebra.com" link, check it will open the correct page
            start_time = time.time()
            try:
                social_login.open_in_chrome()
            except:
                pass
            social_login.swith_back_the_app()
            sleep(1)
            social_login.scroll_down(1)
            data_sources_page.lock_phone()
            wake()
            sleep(2)
            social_login.click_on_zebra_link()
            if not social_login.verify_the_url("zebra.com"):
                raise Exception("zebra.com url not present")
            social_login.go_back()
            social_login.swith_back_the_app()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Click on the "Legal Notice" link, check it will open the correct page
            start_time = time.time()
            social_login.click_on_legal_notice_link()
            if not social_login.verify_the_url(
                    "zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html"):
                raise Exception(
                    "\"zebra.com/us/en/about-zebra/company-information/legal/terms-of-use.html\" url not present")
            social_login.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click on the "Privacy Statement" link, check it will open the correct page
            start_time = time.time()
            social_login.swith_back_the_app()
            sleep(1)
            social_login.click_on_privacy_statement_link()
            if not social_login.verify_the_url(
                    "zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html"):
                raise Exception(
                    "\"zebra.com/us/en/about-zebra/company-information/legal/privacy-statement.html\" url not present")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            # If an error occurs, mark the step as "Fail" and include the error message
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48475(self):
        pass
        common_method.tearDown()
        self.setup_logout()
        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        social_login.click_on_sign_in_with_email()
        keyevent("back")
        sleep(1)
        social_login.scroll_down(1)

        """Reset The password"""
        social_login.click_on_reset_password()
        social_login.wait_for_element_appearance_text("Password Recovery", 20)
        sleep(1)
        username = common_method.get_user_input("enter the user email here")
        social_login.enter_user_name_to_change_password(username)
        social_login.click_on_submit_button()

        common_method.wait_for_element_appearance_namematches("Click here")
        social_login.click_here_button_click()
        """Cant Automate this step 3. Input the prepare email address, follow the steps to finish reseting pw
        Check the pw can be reset successfully without any error"""
        """Enter the temp_pass was temporary password which is got through Mail and enter new password"""

        """Semi automated here pass temp password"""

        """Part2"""

        common_method.wait_for_element_appearance_textmatches("Reset Password", 30)
        sleep(3)

        common_method.show_message("enter the temp password and new password here")

        social_login.click_on_submit_button()

        try:
            social_login.wait_for_element_appearance_text("Password changed successfully.", 20)
        except:
            raise Exception("password changed confirmation dint receive")

        try:
            common_method.wait_for_element_appearance_namematches("Click here")
            social_login.click_here_button_click()
        except:
            pass
        common_method.wait_for_element_appearance_namematches("Continue with Google", 15)
        social_login.click_on_sign_in_with_email()
        common_method.show_message("enter the email and password and continue till home page")

        try:
            social_login.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("dint sign in properly")

    def test_Others_TestcaseID_45802(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Open Mobile app'],
            2: [2, 'Click Sign in button'],
            3: [3, 'Input valid username and password (Note: DO NOT click Sign In button)'],
            4: [4, 'Keep this login page open for 29 mins'],
            5: [5, 'Click Sign In button, check user login Mobile App successfully'],
            6: [6, 'Check user can navigate to other pages, check basic operation on Mobile App work as expected']
        }

        start_time_main = time.time()
        stepId = 1
        start_main(execID, leftId[test_case_id])


        try:

            # Step 1: Open Mobile app
            start_time = time.time()
            common_method.tearDown()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Sign in button
            start_time = time.time()
            try:
                social_login.click_on_allow_for_notification()
            except:
                pass
            self.setup_logout()
            common_method.wait_for_element_appearance_namematches("Sign In")

            login_page.click_loginBtn()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",exec_time)
            stepId += 1

            # Step 3: Input valid username and password (Note: DO NOT click Sign In button)
            start_time = time.time()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            others.click_on_sign_in_with_email()
            common_method.wait_for_element_appearance_textmatches("Sign In")

            email = "zebratest851@gmail.com"
            password = "Zebra#85185180"
            social_login.complete_sign_in_with_email(email, password, 0)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Keep this login page open for 29 mins
            start_time = time.time()
            sleep_time = 60 * 29
            sleep(sleep_time)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click Sign In button, check user login Mobile App successfully
            start_time = time.time()
            others.click_on_sign_in()
            common_method.wait_for_element_appearance_namematches("Home", 30)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Check user can navigate to other pages, check basic operation on Mobile App work as expected
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            others.click_Printer_Settings()
            login_page.click_Menu_HamburgerICN()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Others_TestcaseID_45872(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Open Mobile App'],
            2: [2, 'Click Sign in button'],
            3: [3, 'Input valid username and password (Note: DO NOT click Sign In button)'],
            4: [4, 'Keep this login page open for 31 mins'],
            5: [5,
                'Click Sign In button, check user not login in Mobile App and current page shows: The page you are trying to access is no longer available'],
            6: [6,
                'When ZSB app presents the Cancel button, click on the Cancel button immediately. Check pressing Cancel button in the login view cancels the login']
        }

        start_time_main = time.time()
        stepId = 1
        start_main(execID, leftId[test_case_id])


        try:

            # Step 1: Open Mobile App
            start_time = time.time()

            common_method.tearDown()
            self.setup_logout()
            common_method.wait_for_element_appearance_namematches("Sign In")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Sign in button
            start_time = time.time()
            login_page.click_loginBtn()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            others.click_on_sign_in_with_email()
            sleep(1)
            others.go_back()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input valid username and password (Note: DO NOT click Sign In button)
            start_time = time.time()
            others.enter_user_name_in_sign_with_email("zebratest851@gmail.com")

            others.enter_password_in_sign_with_email("Zebra#85185180")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Keep this login page open for 31 mins
            start_time = time.time()
            sleep_time = 60 * 31
            sleep(sleep_time)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click Sign In button, check user not login in Mobile App and current page shows: The page you are trying to access is no longer available
            start_time = time.time()
            others.click_on_sign_in()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: When ZSB app presents the Cancel button, click on the Cancel button immediately. Check pressing Cancel button in the login view cancels the login
            start_time = time.time()
            try:
                others.wait_for_element_appearance("Home", 10)
                raise Exception("The page does not timeout")
            except ZeroDivisionError:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Social_Login_TestcaseID_48473(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   'Check the login page shows up correctly'],
            2: [2, 'Click on the Sign in with your email option\n'
                   'Check the Zebra account login page pops up'],
            3: [3, 'Check the UI of Zebra account login page\n'
                   '3-1. Under the Sign In option, there are USERNAME and PASSWORD two input boxes\n'
                   '3-2. The Sign In and Close buttons are enabled and highlighted\n'
                   '3-3. Check there are two options:\n'
                   ' - Don\'t have an account? Register Your Email Now\n'
                   ' - Forgot your password? Reset Password'],
            4: [4, 'Click Close button\n'
                   'Check the Zebra login page is closed']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1

        try:
            # Step 1: Launch the ZSB Series app, click on Login button, check the login page shows up correctly
            start_time = time.time()
            common_method.tearDown()
            self.setup_logout()
            login_page.click_loginBtn()
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click on the Sign in with your email option, check Zebra account login page pops up
            start_time = time.time()
            social_login.click_on_sign_in_with_email()
            try:
                social_login.check_element_present_name_matches("keyboard")
                keyevent("back")
            except:
                pass
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check the UI of Zebra account login page
            start_time = time.time()
            if not social_login.check_zebra_logo():
                raise Exception("Zebra Logo not present")

            if not social_login.check_username_and_password_feilds():
                raise Exception("user name or password fields not present ")

            if not social_login.check_sign_in_button():
                raise Exception("sign in button not present")

            social_login.swipe_down_half(1)

            if not social_login.check_close_button():
                raise Exception("close button not present")

            if not social_login.check_text_of_register_your_email():
                raise Exception("text not matching for register your email now")

            if not social_login.check_reset_password_text():
                raise Exception("text not matching for reset password feild")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click Close button, check Zebra login page is closed
            start_time = time.time()
            social_login.click_on_close_button()

            if social_login.check_close_button():
                raise Exception("page dint close")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            # If an error occurs, mark the step as "Fail" and include the error message
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48474(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_on_sign_in_with_email()
        try:
            social_login.click_register_your_email()
        except:
            social_login.go_back()
            social_login.click_register_your_email()

        sleep(2)
        common_method.wait_for_element_appearance_textmatches("ZSB Printer", 20)
        a = social_login.check_registration_of_email()
        if not a:
            raise Exception("register user page dint show")

        """Enter the User Email"""
        email = "testzebra141@gmail.com"
        social_login.enter_user_email_for_registering(email)
        social_login.click_on_next()

        try:
            social_login.wait_for_element_appearance("Resend Verification Code.", 30)
        except:
            raise Exception("Second step dint work")

        """Semi automated """
        """Enter Verification code"""
        verification_code = common_method.get_user_input("enter the code which is got through testzebra141@gmail.com")
        social_login.enter_the_verification_code(verification_code)
        social_login.scroll_down(1)
        social_login.click_on_next()

        """Enter the first Name last name and the password"""
        common_method.wait_for_element_appearance_textmatches("ZSB Printer User Information and Account Security")
        sleep(2)
        first_n = "Zebra"
        last_n = "Z"
        password = "Zebra#123456789"
        social_login.enter_the_fields(first_n, last_n, password)
        social_login.select_the_country("India")
        try:
            social_login.select_the_check_boxes()
            social_login.select_the_check_boxes()
        except:
            try:
                social_login.scroll_down(1)
                social_login.select_the_check_boxes()
                social_login.select_the_check_boxes()
            except:
                pass
        social_login.click_submit_and_continue()
        sleep(2)
        social_login.check_sign_up_successful()
        social_login.click_on_continue()

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide the email and password"""
        social_login.complete_sign_in_with_email(email, password)

        try:
            social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement")
        except:
            raise Exception("EULA page dint show up")

        social_login.click_on_cancel_button_in_eula()
        social_login.click_on_exit_in_eula()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48482(self):
        pass

        common_method.show_message(
            "Prepare an external account which hasn't been signed in once in ZSB series app (new registered)")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide new_user name and password which is not registered"""
        email = common_method.get_user_input("enter the new email")
        password = common_method.get_user_input("enter the password")

        social_login.complete_sign_in_with_email(email, password)
        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""

        common_method.show_message("check the user first name and last name")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()
        sleep(2)
        social_login.complete_sign_in_with_email(email, password)
        common_method.wait_for_element_appearance_namematches("Home")
        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_50646(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Open ZSB app and click Login button'],
            2: [2, 'Click "Sign In with your email"'],
            3: [2, 'Check Input focus should be in username textbox first and keyboard should show up']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1

        try:

            # Step 1: Open ZSB app and click Login button
            start_time = time.time()
            self.setup_logout()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance_text("Continue with Google", 10)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click "Sign In with your email"
            start_time = time.time()
            social_login.click_on_sign_in_with_email()

            if not social_login.check_focused_of_user_name():
                raise Exception("user name is not focused")
            if not social_login.check_key_board():
                raise Exception("No key board displayed")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Check Input focus should be in username textbox first and keyboard should show up
            start_time = time.time()
            if not social_login.check_key_board():
                raise Exception("keyboard dint show up")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Social_Login_TestcaseID_48467(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   'Check the login page shows up correctly'],
            2: [2, 'Under the Sign in With option, click Google option\n'
                   'Check the Google sign in page will be opened'],
            3: [3, 'Input the Google account mentioned in setup 2, then click Sign in\n'
                   'Check the Google account can be signed in successfully'],
            4: [4,
                'On the home page, click the hamburger button and then click on the pen icon to open user settings page\n'
                'Check the user information is correct comparing to the account you signed in'],
            5: [5, 'Click Log Out button\n'
                   'Check the user is being signed out and back to the start logging page']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app, click on Login button, check the login page shows up correctly
            start_time = time.time()
            self.setup_logout()
            """Login with an existing account"""
            login_page.click_loginBtn()
            data_sources_page.lock_phone()
            wake()
            sleep(2)
            common_method.wait_for_element_appearance_namematches("Continue with Google")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Google option under the Sign in With option, check Google sign in page opens
            start_time = time.time()
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            """Enter the email"""
            email = "zebra850.swdvt@gmail.com"
            password = "Zebra#123456789"
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input Google account and sign in
            start_time = time.time()
            social_login.choose_a_google_account(email)
            social_login.wait_for_element_appearance("Home", 30)

            """Check whether logged in to same account as email"""
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Click hamburger button, then pen icon for user settings, verify user information
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            if not social_login.check_the_email_in_profile_page(email):
                raise Exception("the email is not matching")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click Log Out button, verify user is signed out and back to start login page
            start_time = time.time()

            """Log out"""
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            try:
                social_login.wait_for_element_appearance("Sign In", 10)
            except:
                raise Exception("Did not redirect to the login page")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_50643(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the Zebra login page'],
            2: [2, 'Sign in with Google / Facebook'],
            3: [3, 'Once logged in, Logout again'],
            4: [4, 'Launch Zebra login page and again select Google (same platform as Step 2)']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:

            # Step 1: Launch the Zebra login page
            start_time = time.time()
            self.setup_logout()
            login_page.click_loginBtn()
            common_method.wait_for_element_appearance_namematches("Continue with Google")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Sign in with Google / Facebook
            start_time = time.time()
            login_page.click_Loginwith_Google()
            common_method.wait_for_element_appearance_textmatches("Choose an account")

            """Enter the email"""
            email = "zebra850.swdvt@gmail.com"
            social_login.choose_a_google_account(email)
            social_login.wait_for_element_appearance("Home", 20)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Once logged in, Logout again
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()

            social_login.scroll_down(1)
            social_login.click_log_out_button()
            try:
                social_login.wait_for_element_appearance("Sign In", 10)
            except:
                raise Exception("Did not redirect to the login page")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Launch Zebra login page and again select Google (same platform as Step 2)
            start_time = time.time()
            login_page.click_loginBtn()

            login_page.click_Loginwith_Google()

            if not social_login.verify_choose_an_account_text():
                raise Exception("did not redirect to the choose an acoount page")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Social_Login_TestcaseID_50612(self):
        pass
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app'],
            2: [2, 'Check the login page shows up correctly'],
            3: [3, 'Under the Sign in Option, enter User name and password']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:

            # Step 1: Launch the ZSB Series app
            start_time = time.time()

            common_method.tearDown()
            self.setup_logout()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Check the login page shows up correctly
            start_time = time.time()

            login_page.click_loginBtn()

            common_method.wait_for_element_appearance_namematches("Continue with Google")
            """Enter the email and password"""
            email = "zebra850.swdvt@gmail.com"
            password = 'Zebra#123456789'

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Under the Sign in Option, enter User name and password
            start_time = time.time()

            social_login.click_on_sign_in_with_email()
            social_login.complete_sign_in_with_email(email, password, 0)
            social_login.show_the_password()
            sleep(4)
            res = social_login.get_the_password()
            print(res)
            if str(res) != str(password):
                raise Exception("password is not matching")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Social_Login_TestcaseID_48486(self):
        pass
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1,
                'Launch the ZSB Series app, when the start page shows up, click on Login button. Check the login page shows up correctly'],
            2: [2,
                'Under the Sign in With option, click Sign in with your email option. Check the Zebra sign in page will be opened'],
            3: [3,
                'Keep the username and password input box empty, click sign in. Check the prompt message "Please fill out username/password field" shows up under the username/password input boxes'],
            4: [4,
                'Input username but keep password field empty, click sign in. Check the prompt message "Please fill out password field" shows up under the password input box'],
            5: [5,
                'Input password, click sign in. Check no error message pops up this time, user can login in successfully']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app and verify login page
            start_time = time.time()

            self.setup_logout()
            login_page.click_loginBtn()

            """Enter the email and password"""
            email = ""
            password = ''
            common_method.wait_for_element_appearance_namematches("Continue with Google")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Sign in with your email option and verify Zebra sign in page
            start_time = time.time()

            social_login.click_on_sign_in_with_email()

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Keep username and password fields empty, click sign in
            start_time = time.time()

            social_login.complete_sign_in_with_email(email, password, 1)
            sleep(3)
            if not social_login.check_for_blank_value_error_of_both():
                raise Exception("Error not displayed for blank values")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Input username but keep password field empty, click sign in
            start_time = time.time()

            email = "zebratest852@gmail.com"
            social_login.complete_sign_in_with_email(email, password, 1, 0)
            if not social_login.check_for_blank_value_error_of_password():
                raise Exception("Error not displayed for blank values")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Input password, click sign in
            start_time = time.time()

            password = "Zebra#123456789"
            social_login.complete_sign_in_with_email(email, password, 1, 0)
            try:
                social_login.wait_for_element_appearance("Home", 20)
            except:
                raise Exception('did not sign in properly')

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)

    def test_Social_Login_TestcaseID_48483(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   '- Check the login page shows up correctly'],
            2: [2, 'Under the Sign in With option, click Sign in with your email option\n'
                   '- Check the Zebra sign in page will be opened'],
            3: [3, 'Input the inter account mentioned in setup 2, then click Sign in\n'
                   '- Check the EULA will be displayed if it is the first time signing in, if not, skip step 4'],
            4: [4, 'Accept the EULA\n'
                   '- Check the account is signed in and home page is opened successfully'],
            5: [5,
                'On the home page, click the hamburger button and then click on the pen icon to open user settings page\n'
                '- Check the user information is correct comparing to the account you signed in'],
            6: [6, 'Click Log Out button\n'
                   '- Check the user is being signed out and back to the start logging page']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app and verify login page
            start_time = time.time()
            self.setup_logout()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance_text("Continue with Google", 10)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Sign in with your email option and verify Zebra sign in page
            start_time = time.time()
            social_login.click_on_sign_in_with_email()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input the account mentioned in setup 2 and sign in
            start_time = time.time()
            """Provide new_user name and password which is registered"""
            email = "zebratest852@gmail.com"
            password = "Zebra#123456789"
            social_login.complete_sign_in_with_email(email, password)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Accept the EULA if displayed
            start_time = time.time()
            if social_login.check_EULA():
                social_login.accept_EULA_agreement()

            social_login.wait_for_element_appearance("Home", 20)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Navigate to user settings page and verify user information
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            """Pass the first name last name and email to be expected"""
            first_name = "Zebra"
            last_name = "Zebra"
            social_login.validate_the_details_of_account(first_name, last_name, email)
            if not social_login.check_the_email_in_profile_page(email):
                raise Exception("Email are not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 6: Click Log Out button and verify logout
            start_time = time.time()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            try:
                social_login.wait_for_element_appearance("Sign In", 5)
            except:
                raise Exception("Did not redirect to the login page")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48485(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   '- Check the login page shows up correctly'],
            2: [2, 'Under the Sign in With option, click Sign in with your email option\n'
                   '- Check the Zebra sign in page will be opened'],
            3: [3, 'Input the prepare account with correct username but wrong pw, click sign in\n'
                   '- Check the error prompt message shows up to inform user the credential is incorrect'],
            4: [4, 'Clear the username and pw, input wrong username name but correct pw, click sign in\n'
                   '- Check the error prompt message shows up to inform user the credential is incorrect'],
            5: [5, 'Clear the username and pw, input correct username name and correct pw, click sign in\n'
                   '- Check no error message pops up this time, user can login in successfully']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1

        try:
            # Step 1: Launch the ZSB Series app and verify login page
            start_time = time.time()
            common_method.tearDown()
            self.setup_logout()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance("Continue with Google")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Sign in with your email option and verify Zebra sign in page
            start_time = time.time()
            social_login.click_on_sign_in_with_email()
            """Incorrect password but correct email"""
            """Enter the email and password"""
            email = "zebratest852@gmail.com"
            password = 'Zebra#1234567890'
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input correct username but wrong password, click sign in
            start_time = time.time()
            # social_login.click_on_sign_in_with_email()
            social_login.complete_sign_in_with_email(email, password, 1)
            if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
                raise Exception("Error not displayed for incorrect password values")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Clear username and password, input wrong username but correct password, click sign in
            start_time = time.time()
            sleep(1)
            """Incorrect Email but correct password"""
            email = "zebratest85@gmail.com"
            password = 'Zebra#123456789'

            social_login.click_on_sign_in_with_email()

            social_login.complete_sign_in_with_email(email, password, 1, 1)
            sleep(2)
            if not social_login.check_for_incorrect_user_name_or_password_sign_in_with_email():
                raise Exception("Error not displayed for incorrect email")

            sleep(1)
            social_login.click_on_sign_in_with_email()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Clear username and password, input correct username and password, click sign in
            start_time = time.time()
            """Correct password and email"""
            email = "zebratest852@gmail.com"
            password = "Zebra#123456789"
            social_login.complete_sign_in_with_email(email, password, 1, 1)
            if social_login.wait_for_element_appearance("Home", 20):
                raise Exception('did not sign in properly')
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48479(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   '- Check the login page shows up correctly'],
            2: [2,
                'Click Google option, input invalid Google account (wrong username or password) mentioned in setup 2, then click Sign in\n'
                '- Check there is a prompt message for telling user the username or password is wrong'],
            3: [3, 'Clear the wrong user credentials, input valid Google account, click sign in\n'
                   '- Check this time the Google account can be signed in successfully'],
            4: [4,
                'On the home page, click the hamburger button and then click on the pen icon to open user settings page\n'
                '- Check the user information is correct comparing to the account you signed in'],
            5: [5, 'Click Log Out button\n'
                   '- Check the user is being signed out and back to the start logging page']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app and verify login page
            start_time = time.time()
            common_method.tearDown()
            self.setup_logout()
            """Enter invalid user name in google id feild"""
            login_page.click_loginBtn()
            data_sources_page.lock_phone()
            wake()
            sleep(2)
            social_login.wait_for_element_appearance("Continue with Google")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Google option, input invalid credentials, and verify error message
            start_time = time.time()
            login_page.click_Loginwith_Google()

            common_method.wait_for_element_appearance_textmatches("Choose an account")
            social_login.sign_in_with_google()
            common_method.wait_for_element_appearance_textmatches("ext")
            social_login.enter_user_name_in_google("zsb@gmail.com")
            social_login.click_on_next_in_google_sing_in()
            sleep(1)

            if not social_login.check_for_incorrect_username_in_google():
                raise Exception("error not found for incorrect email")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input valid Google account, click sign in, and verify successful login
            start_time = time.time()
            """Select a proper gmail account"""
            social_login.go_back()
            social_login.go_back()
            login_page.click_loginBtn()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance("Continue with Google")
            login_page.click_Loginwith_Google()

            t = social_login.get_one_of_the_gmail_accounts()
            social_login.choose_a_google_account(t)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Navigate to user settings page, verify user information
            start_time = time.time()
            social_login.wait_for_element_appearance("Home", 20)
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click Log Out button and verify logout
            start_time = time.time()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            social_login.wait_for_element_appearance("Sign In", 10)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            # If an error occurs, mark the step as "Fail" and include the error message
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48470(self):
        pass

        common_method.show_message("add a new google account to the phone")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        email = common_method.get_user_input("enter the new gmail account")
        social_login.choose_a_google_account(email)
        sleep(3)
        try:
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
            sleep(2)
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        common_method.show_message("check the first name last name and email are matching as provided")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 10)

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_48472(self):
        pass

        common_method.show_message("create a new facebook account")
        self.setup_logout()
        email = common_method.get_user_input("enter the new facebook email here")
        password = common_method.get_user_input("enter the new password here")
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
        except:
            pass

        social_login.continue_in_facebook()
        social_login.wait_for_element_appearance_text("Submit", 10)

        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_in_facebook()
            social_login.wait_for_element_appearance_text("Continue", 10)
            social_login.click_on_continue()
        except:
            pass

        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        """Semi automated"""
        common_method.show_message("check the email, first name and last name is as expected")

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()
        try:

            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 10)

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")


    def test_Social_Login_TestcaseID_48481(self):
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app, when the start page shows up, click on Login button\n'
                   '- Check the login page shows up correctly'],
            2: [2,
                'Click Facebook option, input invalid Facebook account (wrong username or password) mentioned in setup 2, then click Sign in\n'
                '- Check there is a prompt message for telling user the username or password is wrong'],
            3: [3, 'Clear the wrong user credentials, input valid Facebook account, click sign in\n'
                   '- Check this time the Facebook account can be signed in successfully'],
            4: [4,
                'On the home page, click the hamburger button and then click on the pen icon to open user settings page\n'
                '- Check the user information is correct comparing to the account you signed in'],
            5: [5, 'Click Log Out button\n'
                   '- Check the user is being signed out and back to the start logging page']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:
            # Step 1: Launch the ZSB Series app and verify login page
            start_time = time.time()
            self.setup_logout()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance_text("Continue with Google", 10)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Click Facebook option, input invalid credentials, and verify error message
            start_time = time.time()
            social_login.click_login_with_facebook()
            social_login.wait_for_element_appearance_text(
                "Log in to your Facebook account to connect to Zebra Technologies")

            email = "wrongemail.com"
            password = "Zebra#123456"
            social_login.enter_username_and_password_in_facebook(email, password)
            try:
                social_login.click_element_by_text("Log In")
            except:
                social_login.click_element_by_text("Log in")
            sleep(3)

            if not social_login.check_wrong_user_name_error_in_facebook():
                raise Exception("error not shown for wrong user name")

            email = "testswdvt@gmail.com"
            password = "Zebra#1234567"
            social_login.enter_username_and_password_in_facebook(email, password)
            try:
                social_login.click_element_by_text("Log In")
            except:
                social_login.click_element_by_text("Log in")
            sleep(3)

            if not social_login.check_wrong_password_error_in_facebook():
                raise Exception("error not shown for wrong password")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Input valid Facebook account, click sign in, and verify successful login
            start_time = time.time()
            try:
                email = "testswdvt@gmail.com"
                password = "Zebra#123456789"
                social_login.enter_username_and_password_in_facebook(email, password)
                social_login.click_element_by_text("Log in")
                sleep(3)

            except:
                try:
                    social_login.click_element_by_text("Log In")
                except:
                    pass

            social_login.continue_in_facebook()

            social_login.wait_for_element_appearance("Home", 20)
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 4: Navigate to user settings page, verify user information
            start_time = time.time()
            login_page.click_Menu_HamburgerICN()
            social_login.click_on_profile_edit()
            """Pass the first name last name and email to be expected"""
            first_name = "Zebra"
            last_name = "Zebra"
            # social_login.validate_the_details_of_account(first_name, last_name, email)
            email = "testswdvt@gmail.com"
            if not social_login.check_the_email_in_profile_page(email):
                raise Exception("email not matching")
            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 5: Click Log Out button and verify logout
            start_time = time.time()
            social_login.scroll_down(1)
            social_login.click_log_out_button()
            try:
                social_login.wait_for_element_appearance("Sign In", 5)
            except:
                raise Exception("Did not redirect to the login page")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            # If an error occurs, mark the step as "Fail" and include the error message
            exec_time = 0
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)

    def test_Social_Login_TestcaseID_48469(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log in", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log in")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        try:
            common_method.wait_for_element_appearance_namematches(
                "For the best experience, we need a couple things from you.", 3)
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
        except:
            pass

        common_method.show_message("if the page ask for otp or code provide that and continue till the homr page")

        try:
            social_login.continue_in_facebook()
        except:
            pass

        social_login.wait_for_element_appearance("Home", 30)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Pass the first name last name and email to be expected"""
        first_name = "Zebra"
        last_name = "Zebra"
        # social_login.validate_the_details_of_account(first_name, last_name, email)
        email = "testswdvt@gmail.com"
        if not social_login.check_the_email_in_profile_page(email):
            raise Exception("email not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48478(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        common_method.show_message("if not signed in , then sign in")

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        common_method.show_message("add a printer to this account")
        """Semi automated"""
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        social_login.click_Printer_Settings()
        social_login.click_on_first_printer()
        social_login.click_test_print()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        social_login.click_home_button()
        social_login.click_three_dots_in_printer()
        social_login.click_delete_button()
        social_login.click_delete_button()

        social_login.confirm_delete_printer()
        add_a_printer_page.disable_bluetooth()

        try:
            social_login.click_element_by_text("ALLOW")
        except:
            try:
                social_login.click_element_by_text("Allow")
            except:
                pass
        sleep(2)

        social_login.click_done_enabled()
        sleep(5)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 10)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_48480(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        try:
            social_login.wait_for_element_appearance_text("Forgot", 10)
        except:
            pass

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#12345678"
        social_login.enter_apple_id_and_password(apple_id, password)

        social_login.click_element_by_text("Apple\xa0ID")
        sleep(2)

        if not social_login.check_for_incorrect_error_in_apple():
            raise Exception("No error raised for wrong password or username")

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """Enter two factor authentication if required"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-", 4)
            # social_login.go_back()
            code = "661850"
            social_login.two_factor_authentication_for_apple(code)
            sleep(2)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass
        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home")

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48471(self):
        pass

        common_method.show_message("Create a new apple account")
        self.setup_logout()
        """Need to create a new apple account"""
        apple_id = common_method.get_user_input("Enter the new apple account")
        password = common_method.get_user_input("Enter the password for the apple account")
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)
        try:
            social_login.enter_apple_id_and_password(apple_id, password)
        except:
            pass

        try:
            social_login.click_on_continue()
        except:
            pass

        """Enter the two factor authentication code sent in phone """
        a = common_method.get_user_input("enter the code")
        try:
            social_login.two_factor_authentication_for_apple(a)
        except:
            pass

        social_login.apple_trust_this_browser()
        social_login.continue_steps_in_apple()

        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            sleep(1)
            social_login.click_on_submit_button()
            sleep(2)
        except:
            pass

        social_login.click_on_continue()

        social_login.wait_for_element_appearance_namematches_all("ZSB Terms of Use and License Agreement", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.click_on_cancel_button()
        social_login.click_on_exit_in_eula()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        """Semi automated check manually"""
        """Pass the first name last name and email to be expected"""
        common_method.show_message("check the email , first name and last name are as expected")

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)
        try:

            social_login.enter_apple_id_and_password(apple_id, password)
        except:
            pass

        try:
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance("Home")

        if social_login.check_EULA():
            raise Exception("Eula is dispayed")

    def test_Social_Login_TestcaseID_48468(self):
        pass
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 15)

        social_login.click_login_with_apple()
        common_method.wait_for_element_appearance_textmatches("Forgot", 15)

        """Sign in"""
        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """IF two factor authentication requires"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-factor authentication", 4)
            # social_login.go_back()
            code = common_method.get_user_input("Enter the apple id code")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass
        try:
            common_method.wait_for_element_appearance_textmatches("Trust", 6)
            social_login.apple_trust_this_browser()
        except:
            pass
        sleep(1)

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        """Log out"""
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        first_name = "swdvt"
        last_name = "test"
        if not social_login.validate_the_details_of_account(first_name, last_name):
            raise Exception("credentials not matching")
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48477(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)

        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        try:
            code = common_method.show_message("enter the code")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        common_method.show_message("add a printer to this account")
        """Semi automated"""
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()

        login_page.click_Menu_HamburgerICN()
        social_login.click_Printer_Settings()
        social_login.click_on_first_printer()
        social_login.click_test_print()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        social_login.click_home_button()
        social_login.click_three_dots_in_printer()
        social_login.click_delete_button()
        social_login.click_delete_button()

        social_login.confirm_delete_printer()
        add_a_printer_page.disable_bluetooth()

        try:
            social_login.click_element_by_text("ALLOW")
        except:
            try:
                social_login.click_element_by_text("Allow")
            except:
                pass
        sleep(2)

        social_login.click_done_enabled()
        sleep(5)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 10)

        social_login.enter_apple_id_and_password(apple_id, password)

        try:
            code = common_method.get_user_input("enter the code here")
            social_login.two_factor_authentication_for_apple(code)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home", 30)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_50223(self):
        pass

        common_method.show_message("create a new google account")
        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        email = common_method.get_user_input("enter the new email account")
        social_login.choose_a_google_account(email)
        sleep(3)
        try:
            social_login.click_on_continue()
        except:
            pass
        try:
            social_login.click_on_both_check_boxes_in_google_first_time_login()
            social_login.click_on_submit_button()
            sleep(2)
            social_login.click_on_continue()
        except:
            pass
        social_login.wait_for_element_appearance_namematches_all("End User", 20)
        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.decline_EULA_agreement()
        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        common_method.wait_for_element_appearance_namematches("Continue with Google")

        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")

        social_login.choose_a_google_account("zebra850.swdvt@gmail.com")
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()

        try:
            social_login.wait_for_element_appearance("Sign In", 5)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance("Continue with Google", 10)

        login_page.click_Loginwith_Google()
        social_login.choose_a_google_account(email)

        social_login.wait_for_element_appearance_namematches_all("End User", 20)

        if not social_login.check_EULA():
            raise Exception("EULA Not displayed")

        social_login.accept_EULA_agreement()
        social_login.wait_for_element_appearance("Home", 10)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance("Continue with Google", 10)

        login_page.click_Loginwith_Google()
        social_login.choose_a_google_account(email)
        sleep(5)
        if social_login.check_EULA():
            raise Exception("EULA  displayed")

    def test_Social_Login_TestcaseID_48484(self):
        pass
        self.setup_logout()
        """Sign in with email"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        social_login.click_on_sign_in_with_email()

        """Provide the email and password"""
        email = "zebratest852@gmail.com"
        password = "Zebra#123456789"
        social_login.complete_sign_in_with_email(email, password)

        try:
            social_login.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("home page dint show up")

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()
        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 15)
        except:
            raise Exception("Did not redirect to the login page")

        """Google sign in"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()

        """Enter the email"""
        email = "zebra850.swdvt@gmail.com"
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 20)
        except:
            raise Exception("Did not redirect to the login page")

        """Apple sign in"""
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_login_with_apple()
        social_login.wait_for_element_appearance_text("Forgot ", 20)

        """Sign in"""
        apple_id = "testzebra101@gmail.com"
        password = "Zebra#123456789"
        social_login.enter_apple_id_and_password(apple_id, password)

        """semi automated"""
        try:
            common_method.wait_for_element_appearance_textmatches("Two-", 4)
            social_login.go_back()
            code = "666773"
            social_login.two_factor_authentication_for_apple(code)
            sleep(1)
        except:
            pass

        try:
            social_login.apple_trust_this_browser()
            sleep(2)
        except:
            pass

        social_login.click_on_continue()
        social_login.wait_for_element_appearance("Home")

        """Log out"""
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

        """Facebook Sign in"""

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)

        social_login.click_login_with_facebook()

        try:
            social_login.wait_for_element_appearance_text("Log In", 15)

            email = "testswdvt@gmail.com"
            password = "Zebra#123456789"
            social_login.enter_username_and_password_in_facebook(email, password)
            social_login.click_element_by_text("Log In")
            sleep(3)

        except:
            pass

        social_login.continue_in_facebook()

        social_login.wait_for_element_appearance("Home", 20)

        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

    def test_Social_Login_TestcaseID_48476(self):
        pass

        self.setup_logout()
        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 20)
        login_page.click_Loginwith_Google()

        """Enter the email"""
        email = "zebra850.swdvt@gmail.com"
        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)

        common_method.show_message("add a printer to this account")
        # sleep(60 * 5)
        # login_page.click_Menu_HamburgerICN()
        # add_a_printer_page.click_Add_A_Printer()
        #
        # add_a_printer_page.click_Start_Button()
        # add_a_printer_page.click_Show_All_Printers()
        # sleep(4)
        #
        # social_login.selectPrinter("ZSB-DP12\n6CC28F")
        # social_login.clickSelect()
        # try:
        #     add_a_printer_page.click_Bluetooth_pairing_Popup1()
        # except:
        #     pass
        # try:
        #     social_login.click_Bluetooth_pairing_Popup2()
        # except:
        #     pass
        #
        # social_login.clickConnect()
        # sleep(2)
        # social_login.Enter_Password_Join_Network("123456789")
        # sleep(2)
        # poco(text("123456789"))
        # #
        # common_method.wait_for_element_appearance("Submit")
        #
        # social_login.clickSubmit()
        # social_login.clickFinishSetup()
        #
        # login_page.click_Menu_HamburgerICN()
        # social_login.click_Printer_Settings()
        # social_login.click_on_first_printer()
        # social_login.click_test_print()
        # sleep(3)
        # login_page.click_Menu_HamburgerICN()
        # social_login.click_home_button()
        # social_login.click_three_dots_in_printer()
        # social_login.click_delete_button()
        # social_login.click_delete_button()
        #
        # social_login.confirm_delete_printer()
        # add_a_printer_page.disable_bluetooth()
        #
        # try:
        #     social_login.click_element_by_text("ALLOW")
        # except:
        #     try:
        #         social_login.click_element_by_text("Allow")
        #     except:
        #         pass
        # sleep(2)
        #
        # social_login.click_done_enabled()
        # sleep(5)
        login_page.click_Menu_HamburgerICN()
        social_login.click_on_profile_edit()

        social_login.scroll_down(1)
        social_login.click_log_out_button()
        try:
            social_login.wait_for_element_appearance("Sign In", 10)
        except:
            raise Exception("Did not redirect to the login page")

        login_page.click_loginBtn()
        social_login.wait_for_element_appearance_text("Continue with Google", 10)
        login_page.click_Loginwith_Google()

        social_login.choose_a_google_account(email)
        social_login.wait_for_element_appearance("Home", 20)

        if not social_login.check_printer_not_there_in_home_page():
            raise Exception("printer found in home page")

    def test_Social_Login_TestcaseID_50613(self):
        pass
        current_function_name = inspect.currentframe().f_code.co_name
        test_case_id = current_function_name.split("_")[-1]

        test_steps = {
            1: [1, 'Launch the ZSB Series app or browse the web portal URL to open the login page'],
            2: [2, 'Under the Sign in with option, select the Google option'],
            3: [3, 'Enter the non-Google account, but a valid Zebra email account']
        }

        start_time_main = time.time()
        start_main(execID, leftId[test_case_id])

        stepId = 1  # Initialize stepId before the try-except block

        try:

            # Step 1: Launch the ZSB Series app or browse the web portal URL to open the login page
            start_time = time.time()

            common_method.tearDown()
            self.setup_logout()
            login_page.click_loginBtn()
            social_login.wait_for_element_appearance("Continue with Google")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 2: Under the Sign in with option, select the Google option
            start_time = time.time()

            login_page.click_Loginwith_Google()
            social_login.sign_in_with_google()
            sleep(5)

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)
            stepId += 1

            # Step 3: Enter the non-Google account, but a valid Zebra email account
            start_time = time.time()

            social_login.enter_user_name_in_google("zebratest_o1@outlook.com")
            social_login.click_on_next_in_google_sing_in()
            if not social_login.check_for_incorrect_username_in_google():
                raise Exception("error not found for incorrect email")

            exec_time = (time.time() - start_time) / 60
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                        exec_time)

        except Exception as e:
            insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
            insert_stepDetails(execID, leftId[test_case_id],test_steps[stepId][0] ,str(e) , "")
            insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
            raise Exception(str(e))

        finally:
            exec_time = (time.time() - start_time_main) / 60
            end_main(execID, leftId[test_case_id], exec_time)
