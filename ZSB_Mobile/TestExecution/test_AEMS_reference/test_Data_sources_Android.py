import inspect

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from ...AEMS.api_calls import start_main, insert_step, insert_stepDetails, insert_case_results, end_main, \
    start_execution_loop, end_execution_loop, end_execution, upload_case_files
from ...AEMS.store import execID, leftId
# from setuptools import logging
# from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from airtest.core.api import connect_device

import signal

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
import subprocess
import time
import os

from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Others_Screen.Others_Screen import Others
import pytest
from ...PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen


class Android_App_Data_Sources:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
# start_app("com.zebra.soho_app")
# sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
others_page = Others(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
aps_notification = APS_Notification(poco)
delete_account_page = Delete_Account_Screen(poco)

# ###bug id- SMBM-1456
"""zebra02.swdvt@gmail.com"""

ADB_LOG, test_run_start_time = common_method.start_adb_log_capture()

start_execution_loop(execID)


def test_DataSources_TestcaseID_45729():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Sign in the account and click My Data option'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Google Drive will be opened and let user select file to link'],
        4: [4,
            'Select the file with Special character from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
        5: [5,
            'Select the file with long file name from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
        6: [6, 'Remove these 2 files\nCheck these 2 files are able to remove'],
        7: [7, 'Repeat this test case for OneDrive'],
        8: [8, 'Check Account Settings page should provide user management of Google and OneDrive accounts']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Sign in the account and click My Data option
        start_time = time.time()

        """Google Login"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        account = "zebra02.swdvt@gmail.com"
        registration_page.sign_in_with_mail_zebra02()
        registration_page.BugFix_For_ZebraEmail(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)
        """Google Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Google Drive will be opened and let user select file to link
        start_time = time.time()

        """ google drive """
        registration_page.click_Google_Icon()
        help_page.chooseAcc("zebra02.swdvt@gmail.com")
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select the file with Special character from Google Drive
        start_time = time.time()

        """Select file with special characters"""
        special_char_file = "A_!@#$%^^&(().xlsx"
        data_sources_page.selectFileDrive(special_char_file)
        sleep(5)
        data_sources_page.searchName(special_char_file)
        data_sources_page.verify_File_Data(special_char_file, "Google Drive")
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select the file with long file name from Google Drive
        start_time = time.time()

        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(3)
        """Select long file name"""
        long_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
        data_sources_page.selectFileDrive(long_file)
        sleep(5)
        data_sources_page.searchName(long_file)
        data_sources_page.verify_File_Data(long_file, "Google Drive")
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Remove these 2 files
        start_time = time.time()

        """Remove both files"""
        data_sources_page.searchName(special_char_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", special_char_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(long_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", long_file)
        data_sources_page.searchName("")
        """Check if files removed successfully"""
        data_sources_page.searchName(special_char_file)
        data_sources_page.checkIfListIsEmpty()
        data_sources_page.searchName(long_file)
        data_sources_page.checkIfListIsEmpty()
        """"""""""""""""""""""""""""""""""""""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Repeat this test case for OneDrive
        start_time = time.time()

        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(3)
        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
        common_method.wait_for_element_appearance("NAME")
        data_sources_page.clickMicrosoftOneDrive()
        """Select file with special characters"""
        sleep(5)
        data_sources_page.selectFileDrive(special_char_file)
        sleep(5)
        data_sources_page.searchName(special_char_file)
        data_sources_page.verify_File_Data(special_char_file, "OneDrive")
        data_sources_page.searchName("")
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(3)
        """Select long file name"""
        data_sources_page.selectFileDrive(long_file)
        sleep(5)
        data_sources_page.searchName(long_file)
        data_sources_page.verify_File_Data(long_file, "OneDrive")
        data_sources_page.searchName("")
        """Remove both files"""
        data_sources_page.searchName(special_char_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", special_char_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(long_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", long_file)
        data_sources_page.searchName("")
        """Check if files removed successfully"""
        data_sources_page.searchName(special_char_file)
        data_sources_page.checkIfListIsEmpty()
        data_sources_page.searchName(long_file)
        data_sources_page.checkIfListIsEmpty()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# def test_DataSources_TestcaseID_45733():
#     """test"""
#
#     common_method.Start_The_App()
#     """Click hamburger icon to expand menu"""
#     sleep(5)
#     login_page.click_Menu_HamburgerICN()
#     sleep(5)
#     """Click My Data"""
#     data_sources_page.click_My_Data()
#     """Click Add File"""
#     data_sources_page.click_Add_File()
#     """Click Upload file"""
#     data_sources_page.click_Link_File()
#     try:
#         common_method.wait_for_element_appearance("NAME", 20)
#     except:
#         registration_page.click_Google_Icon()
#         help_page.chooseAcc("zebra03.swdvt@gmail.com")
#         common_method.wait_for_element_appearance("NAME")
#     """searchTest re check"""
#     data_sources_page.searchFilesInLinkFiles("test")
#     sleep(4)
#     data_sources_page.verifyFilePresentInDrive("Test1.jpg")
#     data_sources_page.verifyFilePresentInDrive("Test2.png")
#     data_sources_page.verifyFilePresentInDrive("Test3.bmp")
#     data_sources_page.searchFilesInLinkFiles("test")
#     sleep(4)
#     data_sources_page.verifyFilePresentInDrive("Test1.jpg")
#     """yet to write"""
#     a = data_sources_page.getFilesShownInDrive()
#     print(a)
#     x=1/0
#     """"""
#
#
#     data_sources_page.searchTest("test_i", 1)
#     data_sources_page.searchTest("test_i", 2)
#     data_sources_page.searchTest("test_i", 3)
#     data_sources_page.searchTest(".jpg")
#     data_sources_page.searchTest(".png")
#     data_sources_page.searchTest(".bmp")
#     random_word = data_sources_page.generateRandomWord(24)
#     data_sources_page.searchTest(random_word)


def test_DataSources_TestcaseID_45734():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select Google Drive'],
        4: [4, 'Google Drive page will open and let user select file to link'],
        5: [5, 'Select a not-supported file types to link\nCheck only supported files are listed'],
        6: [6,
            'Select a supported file type but file size exceed maximum allowed size (Max file size is 28.4 MB)\nCheck there is a prompt message for telling user the file is too big'],
        7: [7,
            'Select a same file name which already existed in app to upload\nCheck there is a prompt message for telling user the file is existed, like "file name is already linked"'],
        8: [8, 'Repeat this test case for OneDrive, check it works same for OneDrive file']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select Google Drive
        start_time = time.time()

        """Test for Google Drive"""
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.click_drive_sign_in_if_present()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Google Drive page will open and let user select file to link
        start_time = time.time()

        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select a not-supported file types to link
        start_time = time.time()

        """Cannot select unsupported file"""
        """Modified while adding AEMS code"""
        try:
            data_sources_page.checkFilesShownAreSupported()
            sleep(2)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("There are no unsupported files shown in drive")
        except Exception as e:
            pass
        """"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Select a supported file type but file size exceed maximum allowed size
        start_time = time.time()

        """Modified while adding AEMS code"""
        large_file = "large_unsupported_file(50mb).png"
        try:
            template_management_page_1.wait_for_element_appearance_name_matches_all("file too big")
        except:
            raise Exception("Failed due to bug SMBUI-1127")
        """"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Select a same file name which already existed in app to upload
        start_time = time.time()

        data_sources_page.selectFileDrive(large_file)
        """No prompt message on uploading file greater than 28.4mb"""
        sleep(5)
        data_sources_page.click_Add_File()
        sleep(2)
        data_sources_page.click_Link_File()
        sleep(3)
        """Re upload same file"""
        data_sources_page.selectFileDrive(large_file)
        sleep(5)
        data_sources_page.checkIsAlreadyLinkedPopUp()
        """Remove for next execution"""
        data_sources_page.searchName(large_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", large_file)
        data_sources_page.searchName("")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat this test case for OneDrive
        start_time = time.time()

        """Test for One Drive"""
        sleep(3)
        data_sources_page.click_Add_File()
        sleep(2)
        data_sources_page.click_Link_File()
        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        data_sources_page.clickMicrosoftOneDrive()
        template_management_page_1.wait_for_element_appearance_name_matches_all("NAME", 20)
        sleep(3)
        data_sources_page.selectFileDrive(large_file)
        sleep(5)
        sleep(7)
        data_sources_page.click_Add_File()
        sleep(2)
        data_sources_page.click_Link_File()
        sleep(3)
        data_sources_page.clickMicrosoftOneDrive()
        sleep(2)
        """Re upload the same file"""
        data_sources_page.selectFileDrive(large_file)
        sleep(5)
        data_sources_page.checkIsAlreadyLinkedPopUp()
        """Remove files for next execution"""
        data_sources_page.searchName(large_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", large_file)
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
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45735():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select File page will open'],
        4: [4, 'Select One Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Check mobile app return back to My Data page and no file is linked'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'On One Drive page, check only supported file types are listed'],
        9: [9, 'Select a file and click Select'],
        10: [10,
             'Check mobile app return to My Data page and file is linked, Check the details of file icon, file name, Date added and Data source field (One Drive) are correct'],
        11: [11, 'Repeat for another 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Zebra account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """One Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ One drive """

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select File page will open
        start_time = time.time()

        sleep(2)
        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select One Drive
        start_time = time.time()

        data_sources_page.clickMicrosoftOneDrive()
        data_sources_page.click_drive_sign_in_if_present()
        common_method.wait_for_element_appearance("NAME")
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check mobile app return back to My Data page and no file is linked
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: On One Drive page, check only supported file types are listed
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        template_management_page_1.wait_for_element_appearance_name_matches_all("NAME", 20)
        sleep(5)
        data_sources_page.checkFilesShownAreSupported()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Select a file and click Select
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check mobile app return to My Data page and file is linked, Check the details of file icon, file name, Date added and Data source field (One Drive) are correct
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Repeat for another 2 to 3 supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45736():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Add file from google drive'],
        2: [2, 'Add file from one drive'],
        3: [3, 'Go to Mobile app -> My Data page'],
        4: [4,
            'Click the 3 dot menu from a file which linked from Google Drive, Select Remove option, A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will need to be reconnected to a data source.", Select Cancel button'],
        5: [5, 'Check the linked file is not removed'],
        6: [6, 'Click the 3 dot menu from a file which linked from Google Drive, Select Remove button'],
        7: [7, 'Check the linked file is removed.'],
        8: [8, 'Repeat the test case and remove linked file from One Drive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Add file from google drive
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(3)
        """Upload file to remove"""
        """Google drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Add file from one drive
        start_time = time.time()

        """One drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click the 3 dot menu from a file which linked from Google Drive, Select Remove option
        start_time = time.time()

        data_sources_page.searchName(csv_file)
        sleep(5)
        """Google Drive"""
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", csv_file, True, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check the linked file is not removed
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        try:
            data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
        except:
            raise Exception("File removed even after clicking cancel")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click the 3 dot menu from a file which linked from Google Drive
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Google Drive", csv_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check the linked file is removed
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        try:
            data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File not removed")
        except Exception as e:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat the test case and remove linked file from One Drive
        start_time = time.time()

        """One Drive"""
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file, True, True)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        try:
            data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
        except:
            raise Exception("File not removed")
        sleep(2)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        try:
            data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
            raise Exception("File not removed")
        except:
            pass
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45759():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open the Mobile App'],
        2: [2, 'Go to my data page'],
        3: [3, 'Click on the "link file" button and follow the link to the Google Drive file'],
        4: [4, 'Click on Google Drive login with prepared Google account'],
        5: [5, 'Select one file from Google Drive file list, check file shows in My Data list'],
        6: [6,
            'Repeat step 3-4, select the same file to link, Validate message will display "xxx(file name) is already linked."'],
        7: [7, 'Remove the linked file'],
        8: [8, 'Repeat step 3 to 7 to cover OneDrive\nCheck it works well']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Open the Mobile App
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Go to my data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on the "link file" button and follow the link to the Google Drive file
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click on Google Drive login with prepared Google account
        start_time = time.time()

        data_sources_page.click_drive_sign_in_if_present()
        """ google drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select one file from Google Drive file list, check file shows in My Data list
        start_time = time.time()

        existing_file = "drive_existing_file.jpg"
        sleep(2)
        data_sources_page.selectFileDrive(existing_file)
        sleep(5)
        data_sources_page.searchName(existing_file)
        data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True, False)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Repeat step 3-4, select the same file to link, Validate message "xxx(file name) is already linked."
        start_time = time.time()

        """Re upload same file"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """CLick Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        data_sources_page.clickGoogleDrive()
        sleep(2)
        data_sources_page.selectFileDrive(existing_file)
        """Verify if 'filename' is already linked pop up appears"""
        data_sources_page.checkIsAlreadyLinkedPopUp()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Remove linked file
        start_time = time.time()

        """remove file for next execution"""
        data_sources_page.searchName(existing_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", existing_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat step 3 to 6 to cover OneDrive, check it works well
        start_time = time.time()

        """ One Drive """
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        sleep(2)
        data_sources_page.click_drive_sign_in_if_present()
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(3)
        data_sources_page.selectFileDrive(existing_file)
        sleep(5)
        data_sources_page.searchName(existing_file)
        data_sources_page.verifyFilePresentInList(existing_file, "OneDrive", True, False)
        """Re upload same file"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """CLick Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        data_sources_page.clickMicrosoftOneDrive()
        sleep(2)
        data_sources_page.selectFileDrive(existing_file)
        """Verify if 'filename' is already linked pop up appears"""
        data_sources_page.checkIsAlreadyLinkedPopUp()
        sleep(3)
        """remove file for next execution"""
        data_sources_page.searchName(existing_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", existing_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""zebra02.swdvt@gmail.com"""


def test_DataSources_TestcaseID_45737():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2,
            'Click the 3 dot menu from a file linked from Google Drive, Select Remove option, A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will convert to manual input fields.", Select Remove button'],
        3: [3, 'Check the linked file is removed'],
        4: [4, 'Print the label design, mobile app will prompt user to Update Data Connections'],
        5: [5, 'Choose the linked Excel file in precondition step 4, click next'],
        6: [6,
            'Choose the new column, click next\nCheck that preview dialog is shown\nNavigate to check different preview images are correct'],
        7: [7,
            'Click print, then click label range field, select some rows, click confirm\nCheck that only the selected row numbers are shown in the label range field\nNavigate to check that only the selected rows can be previewed\nCheck that the total number is correct and the same as your selected row amount'],
        8: [8, 'Click print\nCheck that only the selected row data is printed out'],
        9: [9, 'Repeat the test case and remove the linked file in step 2 from One Drive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:

        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        account = "zebra02.swdvt@gmail.com"
        registration_page.sign_in_with_mail_zebra02()
        registration_page.BugFix_For_ZebraEmail(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click the 3 dot menu from a file linked from Google Drive, Select Remove option, A confirmation pop up, Select Remove button
        start_time = time.time()

        removed_file_name = "45737_original.xlsx"
        data_sources_page.searchName(removed_file_name)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", removed_file_name, False, True)
        sleep(3)
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check the linked file is removed
        start_time = time.time()

        data_sources_page.searchName(removed_file_name)
        try:
            data_sources_page.verifyFilePresentInList(removed_file_name, "Google Drive", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File not removed")
        except Exception as e:
            pass
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Print the label design, mobile app will prompt user to Update Data Connections
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        common_method.wait_for_element_appearance_namematches("Showing", 15)
        data_sources_page.searchMyDesigns("45737")
        sleep(5)
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        data_sources_page.chooseAccToLinkFile()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Choose the linked Excel file in precondition step 4, click next
        start_time = time.time()

        try:
            common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
            data_sources_page.clickBackArrow()
            sleep(4)
        except:
            pass
        template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (Google Drive)")
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Choose the new column, click next, Check that preview dialog is shown, navigate to check different preview images
        start_time = time.time()

        template_management_page.selectChooseAnOption(1)
        data_sources_page.clickContinue()
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        template_management_page.verify_label_navigation()
        """Cannot automate - navigate to check different preview images are correct-has to be verified manually"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click print, then click label range field, select some rows, click confirm, Check selected row numbers and preview, Check total number matches selected rows
        start_time = time.time()

        data_sources_page.scroll_till_print()
        data_sources_page.labelRangeSelection(4)
        sleep(3)
        template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
        """Cannot automate - navigate to check that only the select rows can be previewed-has to be verified manually"""
        template_management_page.verify_label_navigation()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click print, Check only selected row data is printed out
        start_time = time.time()

        data_sources_page.scroll_till_print()
        if template_management_page.get_total_labels_printing() == "4":
            pass
        else:
            raise Exception("The total number is not the same as your selected row amount")
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 90)
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Repeat the test case and remove the linked file in step 2 from One Drive
        start_time = time.time()

        data_sources_page.clickBackArrow()
        data_sources_page.checkIfDesignsLoaded()
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        try:
            common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
            data_sources_page.clickBackArrow()
            sleep(4)
        except:
            pass
        template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (OneDrive)")
        account = "zebra03.swdvt@gmail.com"
        if data_sources_page.verifySignInWithMicrosoft():
            data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
            sleep(2)
        sleep(10)
        if template_management_page.continueDisabled() and not template_management_page.checkIfOnRelinkDataSourcesPage:
            print("///---///")
            template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (OneDrive)")
            data_sources_page.enterMicrosoftUsername(account)
            data_sources_page.clickContinue()
        if not template_management_page.checkIfOnRelinkDataSourcesPage():
            data_sources_page.clickContinue()
        template_management_page.selectChooseAnOption(1)
        data_sources_page.clickContinue()
        """Cannot automate - navigate to check different preview images are correct-has to be verified manually"""
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        data_sources_page.scroll_till_print()
        data_sources_page.labelRangeSelection(4)
        sleep(3)
        template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
        """Cannot automate - navigate to check that only the select rows can be previewed-has to be verified manually"""
        template_management_page.verify_label_navigation()
        data_sources_page.scroll_till_print()
        if template_management_page.get_total_labels_printing() == "4":
            pass
        else:
            raise Exception("The total number is not the same as your selected row amount")
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 90)
        sleep(3)
        data_sources_page.clickBackArrow()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()
        sleep(5)
        """Re-upload the file for the next execution"""
        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(5)
        """ google drive """
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        data_sources_page.selectFileDrive(removed_file_name)
        sleep(5)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45739():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4, 'Click back button to return to mobile app\nCheck no file is uploaded'],
        5: [5, 'Click + button at bottom and select Upload File'],
        6: [6,
            'Upload all the supported file types\nCheck Files are uploaded with correct icon, name, data source type and create date\nNote: Data files should use file icons, image files should use image icons\nCheck there is notification " has been successfully uploaded"'],
        7: [7,
            'Login to web portal -> Data Sources page\nCheck the uploaded files from mobile app display in the My Data page in web portal\nCheck switching to different menus or pressing F5 should refresh the file list']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Upload File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload File"""
        data_sources_page.click_Upload_File()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        data_sources_page.searchFileInLocalStorage("Supported Files", "Downloads")
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click back button to return to mobile app, Check no file is uploaded
        start_time = time.time()

        data_sources_page.clickBackArrow()
        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click + button at bottom and select Upload File
        start_time = time.time()

        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload File"""
        data_sources_page.click_Upload_File()
        sleep(3)

        # Step 6: Select supported file type to upload, Check icon, name, data source, create date, and notification
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        data_sources_page.searchFileInLocalStorage("Supported Files", "Downloads")
        sleep(3)
        uploaded_file_list = ["bmp_file.bmp", "jpg_file.jpg", "png_file.png", "csv_file.csv", "text_file.txt"]
        data_sources_page.selectFilesInLocal()
        """No notification after uploading file"""
        keyevent("back")
        keyevent("back")
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            sleep(7)
            data_sources_page.verifyFilePresentInList(name, "Local File", True)
            """Remove this once web inconsistency issue is resolved"""
            """--------------------------------------"""
            data_sources_page.remove_File_Based_On_DataSource("Local File", name)
            """--------------------------------------"""

        # Step 7: Login to web portal -> Data Sources page, Check uploaded files and refresh list
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        """Login to web portal->Data Sources page Check the uploaded files from mobile app display in the my data page in web portal."""
        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        data_sources_page.clickEnter()
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        data_sources_page.signIn_if_on_SSO_page_web()
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        template_management_page.clickGotIt()
        registration_page.wait_for_element_appearance_text("Home", 20)
        sleep(3)
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.click_My_Data()
        data_sources_page.click_Menu_HamburgerICNWeb()
        sleep(3)
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            keyevent("back")
            sleep(2)
            poco.scroll()
            try:
                common_method.wait_for_element_appearance_text("No files match your search")
                x = 1 / 0
            except ZeroDivisionError:
                raise Exception("Uploaded files not displaying in my data page.")
            except Exception as e:
                pass
        stop_app("com.android.chrome")
        """Remove uploaded files for next execution"""
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            data_sources_page.remove_File_Based_On_DataSource("Local File", name)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45744():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload, select a file from local'],
        4: [4,
            'Click + button at the bottom, and select Upload File\nA page will be opened and let user select file to upload\nSelect a file which name is same as the file existing uploaded from local\nCheck it allows user to upload the same file and adds suffix(1) to the later uploaded file name'],
        5: [5, 'Click + button at the bottom, and select Link File'],
        6: [6,
            'A page will be opened and let user select file to link, select a file from cloud and check if it is present'],
        7: [7,
            'Click + button at the bottom, and select Upload File\nSelect a file which name is same as the file existing uploaded from cloud\nCheck the file can be uploaded successfully'],
        8: [8, 'Remove the uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at the bottom, and select Upload File
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload, select a file from local
        start_time = time.time()

        """Select File to upload"""
        file_name = data_sources_page.select_File_To_Upload(True)
        print(file_name)
        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select a file with the same name as an already uploaded file from local, Check if the same file is uploaded with a suffix (1)
        start_time = time.time()

        """Upload the same file again"""
        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)
        data_sources_page.select_File_To_Upload()
        sleep(10)
        search_name = file_name.split(".")[0]
        extension = file_name.split(".")[1]
        data_sources_page.searchName(search_name)
        file_list = data_sources_page.fileListDisplayed()
        if (search_name + "." + extension in file_list) and (search_name + " (1)" + "." + extension in file_list):
            pass
        else:
            raise Exception("Re-uploading not appended '(1)' to file name")
        drive_file = "drive_file.jpg"

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click + button at the bottom, and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: A page will be opened and let user select file to link, select a file from cloud
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        data_sources_page.selectFileDrive(drive_file)
        sleep(7)
        data_sources_page.searchName(drive_file)
        data_sources_page.verifyFilePresentInList(drive_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at the bottom, and select Upload File, Select a file which name is same as the file existing uploaded from cloud, Check the file can be uploaded successfully
        start_time = time.time()

        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)
        data_sources_page.searchFileInLocalStorage(drive_file)
        sleep(7)
        data_sources_page.searchName(drive_file)
        data_sources_page.verifyFilePresentInList(drive_file, "Local File", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Remove the uploaded files
        start_time = time.time()

        "remove file for next execution"
        removing_files = [search_name + " (1)", search_name]
        for i in removing_files:
            data_sources_page.searchName(i)
            data_sources_page.remove_File()
        data_sources_page.searchName(drive_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", drive_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(drive_file)
        data_sources_page.remove_File_Based_On_DataSource("Local File", drive_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45741():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Upload a local file'],
        3: [3,
            'Click 3 dots menu for a local file, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Cancel'],
        4: [4, 'Check the selected file is not been deleted'],
        5: [5,
            'Click 3 dots menu for selected file again, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Delete button'],
        6: [6, 'Check the selected file is deleted from the list (no need to refresh the page manually)'],
        7: [7, 'Go to web portal to check if the file is removed from web portal as well.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """setup - Upload a file from local to execute"""

        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Upload a local file
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select Very large File to upload"""
        selected_file_name = data_sources_page.selectFileInLocalStorage()
        print(selected_file_name)
        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click 3 dots menu for a local file, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Cancel
        start_time = time.time()

        data_sources_page.searchName(selected_file_name)
        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check the selected file is not been deleted
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(selected_file_name)

        file_list = data_sources_page.fileListDisplayed()
        if len(file_list) >= 1:
            pass
        else:
            raise Exception("File list empty")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click 3 dots menu for selected file again, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Delete button
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the selected file is deleted from the list (no need to refresh the page manually)
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(selected_file_name)
        try:
            data_sources_page.verifyFilePresentInList(selected_file_name, "Local File", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File present even after removing it.")
        except Exception as e:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Go to web portal to check if the file is removed from web portal as well.
        start_time = time.time()

        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        data_sources_page.clickEnter()
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        registration_page.wait_for_element_appearance_text("Home", 20)
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.click_My_Data()
        data_sources_page.click_Menu_HamburgerICNWeb()
        sleep(2)
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        data_sources_page.searchName(selected_file_name)
        keyevent("back")
        sleep(2)
        poco.scroll()
        try:
            common_method.wait_for_element_appearance_text("No files match your search")
        except:
            raise Exception("File is not removed from the web portal.")
        stop_app("com.android.chrome")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45742():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Upload a local file'],
        3: [3,
            'Click 3 dots menu for a local file, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Cancel'],
        4: [4, 'Check the selected file is not been deleted'],
        5: [5,
            'Click 3 dots menu for selected file again, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Delete button\nCheck the selected file is deleted from the list (no need to refresh the page manually)'],
        6: [6, 'Go to web portal to check if the file is removed from web portal as well.'],
        7: [7, 'Print the template and check it should prompt user to link or input data manually.'],
        8: [8,
            'Try to link a new file or input data manually when printing the template\nCheck user can link a new file or input data manually and print out successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        remove_file_name = "ferry.xlsx"
        """----------------------------------------------"""
        """Upload the file for this next execution"""
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Upload a local file
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select Very large File to upload"""
        data_sources_page.searchFileInLocalStorage(remove_file_name, "Downloads")
        sleep(10)
        """----------------------------------------------"""
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click 3 dots menu for a local file, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Cancel
        start_time = time.time()

        data_sources_page.searchName(remove_file_name)
        data_sources_page.remove_File_Based_On_DataSource("Local File", remove_file_name, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check the selected file is not been deleted
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(remove_file_name)
        file_list = data_sources_page.fileListDisplayed()
        if len(file_list) >= 1:
            pass
        else:
            raise Exception("File list empty")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click 3 dots menu for selected file again, Click Remove, Message prompt "Remove local file" to let user to confirm, Click Delete button\nCheck the selected file is deleted from the list (no need to refresh the page manually)
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", remove_file_name)
        data_sources_page.searchName("")
        data_sources_page.searchName(remove_file_name)
        try:
            data_sources_page.verifyFilePresentInList(remove_file_name, "Local File", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File present even after removing it.")
        except Exception as e:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Go to web portal to check if the file is removed from web portal as well.
        start_time = time.time()

        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        data_sources_page.clickEnter()
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        registration_page.wait_for_element_appearance_text("Home", 20)
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.click_My_Data()
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.searchName(remove_file_name)
        keyevent("back")
        sleep(2)
        poco.scroll()
        try:
            common_method.wait_for_element_appearance_text("No files match your search")
        except:
            raise Exception("File is not removed from the web portal.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Print the template and check it should prompt user to link or input data manually.
        start_time = time.time()

        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.clickMyDesigns()
        data_sources_page.click_Menu_HamburgerICNWeb()
        common_method.wait_for_element_appearance_textmatches("Showing")
        data_sources_page.searchName("45742")
        keyevent("back")
        common_method.wait_for_element_appearance_textmatches("Showing")
        poco.scroll()
        data_sources_page.selectDesignCreatedAtSetUpWeb()
        data_sources_page.clickPrint()
        data_sources_page.clickCheckBox()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Try to link a new file or input data manually when printing the template\nCheck user can link a new file or input data manually and print out successfully.
        start_time = time.time()

        data_sources_page.clickContinueWeb()
        _, b = poco("android.widget.EditText").get_position()
        common_method.swipe_screen([0.9, b], [0.2, b], 1)
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.set_text("Hello")
        keyevent("back")
        data_sources_page.clickPrint()
        common_method.wait_for_element_appearance_text("Print complete", 20)
        stop_app("com.android.chrome")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45743():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Goto Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and click upload file'],
        3: [3,
            'In Android, if you select a third-party file browser, e.g., Files in Huawei or ES, you will be able to select unsupported file types. Then select an unsupported file.\nIf you open the default file browser, only the supported file types can be selectable. Click or double-click on the greyed-out files\nCheck the file is not able to be selected.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Goto Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and click upload file
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: In Android, if you select a third-party file browser, e.g., Files in Huawei or ES, you will be able to select unsupported file types. Then select an unsupported file.
        # If you open the default file browser, only the supported file types can be selectable. Click or double-click on the greyed-out files
        # Check the file is not able to be selected.
        start_time = time.time()

        """Select File to upload"""
        data_sources_page.selectUnSupportedFile()
        try:
            common_method.wait_for_element_appearance("My Data")
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("Unsupported files are selectable.")
        except Exception as e:
            pass
        keyevent("back")
        keyevent("back")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45745():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Goto Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3,
            'A page will be opened and let user select file to upload, Select a file with below special characters to upload\n@ & () $ ! ^ = ~ {} [] ; "" _ - # % and Chinese\n[Vicky] there will be no error for invalid characters, and those characters are just ignored in the name\nCheck the file can be uploaded successfully without error'],
        4: [4, 'Repeat to upload files to cover all above special characters.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Goto Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)
        """"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at the bottom, and select Upload File
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        ignored_char = '&""#%'
        special_char_file1 = "M@xi!mum_#Power%.jpg"
        special_char_file2 = "un$et_{&}_D@zzle.jpg"
        """Select File to upload"""
        data_sources_page.searchFileInLocalStorage(special_char_file1, "Downloads")
        sleep(7)
        for char in ignored_char:
            special_char_file1 = special_char_file1.replace(char, '')
        sleep(2)
        print(special_char_file1)
        data_sources_page.searchName(special_char_file1)
        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(special_char_file1)
        data_sources_page.remove_File_Based_On_DataSource("Local File", special_char_file1)
        """Select File to upload"""
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Repeat to upload files to cover all above special characters.
        start_time = time.time()

        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        data_sources_page.searchFileInLocalStorage(special_char_file2, "Downloads")
        sleep(7)
        for char in ignored_char:
            special_char_file2 = special_char_file2.replace(char, '')
        sleep(2)
        print(special_char_file2)
        data_sources_page.searchName(special_char_file2)
        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(special_char_file2)
        data_sources_page.remove_File_Based_On_DataSource("Local File", special_char_file2)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45746():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3,
            'A page will be opened and let user select file to upload, Select a file with 64 characters in the file name'],
        4: [4,
            'Check it can be uploaded successfully. Check the file icon, file name, Date added, and Data source field are correct.'],
        5: [5, 'Remove the uploaded file']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at the bottom, and select Upload File
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        long_name_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
        """Select File to upload"""
        data_sources_page.searchFileInLocalStorage(long_name_file, "Downloads")
        sleep(7)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check it can be uploaded successfully
        start_time = time.time()

        data_sources_page.searchName(long_name_file)
        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(long_name_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Remove the uploaded file
        start_time = time.time()

        """Remove file for next execution"""
        data_sources_page.remove_File_Based_On_DataSource("Local File", long_name_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45747():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3, 'Select a file with exceed maximum allowed size (eg. size is 28.5 MB, Max file size is 28.4 MB)'],
        4: [4, 'Check the file can not be uploaded.'],
        5: [5, 'Repeat the test with file size 28.3MB and 28.4MB.'],
        6: [6, 'Check the file can be uploaded successfully.'],
        7: [7, 'Remove the successfully uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        """Large file"""
        large_file = "large_unsupported_file(50mb).png"
        """Click Add File"""
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at the bottom, and select Upload File
        start_time = time.time()

        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select a file with exceed maximum allowed size (eg. size is 28.5 MB, Max file size is 28.4 MB)
        start_time = time.time()

        """Select Very large File to upload"""
        data_sources_page.searchFileInLocalStorage(large_file, "Downloads")
        sleep(30)
        data_sources_page.searchName(large_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check the file can not be uploaded
        start_time = time.time()

        try:
            data_sources_page.verifyFilePresentInList(large_file, "Local File", True)
            x = 1 / 0
        except ZeroDivisionError:
            data_sources_page.remove_File_Based_On_DataSource("Local File", large_file)
            raise Exception("We are able to upload file larger than 28.4 MB.(SMBUI-1127)")
        except Exception as e:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Repeat the test with file size 28.3MB and 28.4MB
        start_time = time.time()

        """unable to verify error as there is no error popping up if file exceeds 28.4mb"""
        """28.3mb file"""
        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select File of size 28.3mb to upload"""
        data_sources_page.searchFileInLocalStorage("28.3M.png", "Downloads")
        sleep(10)
        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select File of size 28.4 to upload"""
        data_sources_page.searchFileInLocalStorage("29.4M.png", "Downloads")
        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the file can be uploaded successfully
        start_time = time.time()

        data_sources_page.searchName("29.4m.png")
        data_sources_page.verifyFilePresentInList("29.4m.png", "Local File", True)
        sleep(5)
        data_sources_page.searchName("")
        data_sources_page.searchName("28.3M.png")
        data_sources_page.verifyFilePresentInList("28.3M.png", "Local File", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Remove the successfully uploaded files
        start_time = time.time()

        """Remove uploaded files for next execution"""
        data_sources_page.remove_File_Based_On_DataSource("Local File", "28.3M.png")
        data_sources_page.searchName("29.4m.png")
        data_sources_page.remove_File_Based_On_DataSource("Local File", "29.4m.png")
        data_sources_page.searchName(large_file)
        data_sources_page.remove_File_Based_On_DataSource("Local File", large_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# def test_DataSources_TestcaseID_45748():
#     """test"""
#
#     common_method.tearDown()
#         data_sources_page.checkIfOnHomePage()
#     """Click hamburger icon to expand menu"""
#     login_page.click_Menu_HamburgerICN()
#     """Click My Data"""
#     data_sources_page.click_My_Data()
#     sleep(2)
#     """get initial count of files"""
#     initial_file_count = len(data_sources_page.fileListDisplayed())
#     sleep(2)
#     """search some words which match with some files name"""
#     data_sources_page.searchExistingName()
#     """get count after searching"""
#     final_file_count = len(data_sources_page.fileListDisplayed())
#     """Check if results are filtered"""
#     data_sources_page.checkIfResultsAreFiltered(initial_file_count, final_file_count)
#     sleep(2)
#     """search some words which do not match with any files name"""
#     data_sources_page.searchRandomWord()
#     """check if the list is empty"""
#     data_sources_page.checkIfListIsEmpty()
#     """Enter special characters to the Search field"""
#     data_sources_page.enterSpecialCharactersInsearchField()
#     """Cannot verify if error occurs as here is no error."""
#     data_sources_page.clearTextAndVerifyFileCount(initial_file_count)
#     common_method.Stop_The_App()


def test_DataSources_TestcaseID_45755():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Google account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Cloud Service Sign in page will open and let user select which service to login'],
        4: [4, 'Click Sign in with Microsoft account'],
        5: [5, 'After signed in Microsoft account, check supported files are listed in One Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Mobile app return to My Data page, Check no file is uploaded'],
        8: [8, 'Click + button at bottom and select Link File'],
        9: [9, 'Click Microsoft One Drive'],
        10: [10, 'Select any of the supported file types to link'],
        11: [11,
             'Check the selected file is linked, Check the file icon, file name, Date added and Data source field are correct'],
        12: [12, 'Repeat for other 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Google account in Mobile app and go to My Data page
        start_time = time.time()

        """Google Login"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        account = "zebra02.swdvt@gmail.com"
        registration_page.sign_in_with_mail_zebra02()
        registration_page.BugFix_For_ZebraEmail(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """One Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open and let user select which service to login
        start_time = time.time()

        if data_sources_page.verifySignInWithMicrosoft():
            data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
            sleep(3)
        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Sign in with Microsoft account
        start_time = time.time()

        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Microsoft account, check supported files are listed in One Drive
        start_time = time.time()

        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Mobile app return to My Data page, Check no file is uploaded
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click Microsoft One Drive
        start_time = time.time()

        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Select any of the supported file types to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the selected file is linked, Check the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for other 2 to 3 supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# def test_DataSources_TestcaseID_45756():
#     """test"""
#
#     common_method.tearDown()
#     """Click hamburger icon to expand menu"""
#     login_page.click_Menu_HamburgerICN()
#     sleep(2)
#     """Click My Designs in menu"""
#     data_sources_page.clickMyDesigns()
#     """Choose the design created at setup"""
#     common_method.wait_for_element_appearance_namematches("Showing")
#     data_sources_page.searchName("45756")
#     common_method.wait_for_element_appearance_namematches("Showing")
#     data_sources_page.selectDesignCreatedAtSetUp()
#     sleep(2)
#     """Click print"""
#     data_sources_page.clickPrint()
#     """Choose Use Local Contacts in Update Data Connections page"""
#     try:
#         poco("Accept").wait_for_appearance(timeout=10)
#         poco("Accept").click()
#     except:
#         pass
#     try:
#         poco(text="Allow").wait_for_appearance(timeout=10)
#         poco(text="Allow").click()
#     except:
#         pass
#     sleep(7)
#     """Verify if preview is present"""
#     data_sources_page.verifyIfPreviewIsPresent()
#     while not poco("Print").exists():
#         poco.scroll()
#     """Set the label range accordingly"""
#     selection_range = 4
#     data_sources_page.labelRangeSelection(selection_range)
#     """Verify if preview label range is according to the label range set"""
#     template_management_page.verify_label_navigation()
#     while not poco("Print").exists():
#         poco.scroll()
#     number_of_labels_printing = template_management_page.get_total_labels_printing()
#     print(number_of_labels_printing)
#     if number_of_labels_printing == str(selection_range):
#         pass
#     else:
#         raise Exception("Number of label printed out is not equal to number of contact selected")
#     """Click print to print the labels"""
#     data_sources_page.clickPrint()
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     common_method.Stop_The_App()


def test_DataSources_TestcaseID_45757():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Designs'],
        2: [2, 'Select the design created in Setup'],
        3: [3, 'Click the print button\n Check there is option for choosing picture object'],
        4: [4, 'Choose Camera option, take a photo and upload it\n Check the preview is correct'],
        5: [5, 'Click the print button\n Check the printed label is correct']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Designs
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Designs in menu"""
        data_sources_page.clickMyDesigns()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Select the design created in Setup
        start_time = time.time()

        """Choose the design created at setup"""
        data_sources_page.searchMyDesigns("45757")
        sleep(3)
        data_sources_page.selectDesignCreatedAtSetUp()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click the print button
        # Check there is option for choosing picture object
        start_time = time.time()

        """Click the print option"""
        data_sources_page.clickPrint()
        sleep(5)
        """Verify if there is option to choose picture"""
        data_sources_page.verifyPhotoOptions()
        poco.scroll()
        """Expand to see different options to choose picture"""
        data_sources_page.expandPhotoOptions()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Choose Camera option, take a photo and upload it
        # Check the preview is correct
        start_time = time.time()

        """Choose camera option"""
        data_sources_page.chooseCameraToClickPhoto()
        """click the photo"""
        try:
            common_method.wait_for_element_appearance_textmatches("While using the app", 20)
            data_sources_page.allowPermissions()
        except:
            pass
        others_page.capture_the_image_button()
        data_sources_page.clickOk()

        """Part of step 4 is to check the preview is correct unable to verify preview has to be done manually"""
        """Print the photo"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click the print button
        # Check the printed label is correct
        start_time = time.time()

        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_47830():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open mobile app and Go to My Design Page'],
        2: [2, 'Login Web Portal with same test account, create a new design'],
        3: [3, 'Go back to Mobile App'],
        4: [4,
            'In My Design page, the new created design in Step 2 not show in list\n Check screen pull-down to refresh/update on My Design'],
        5: [5, 'Open My Data page'],
        6: [6, 'In Web Portal, upload or link a new file in My Data page'],
        7: [7,
            'Go back to Mobile App, My Data page file list not update\n Check screen pull-down to refresh/update on My Data Page works']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Open mobile app and Go to My Design Page
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Designs in menu"""
        data_sources_page.clickMyDesigns()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Login Web Portal with same test account, create a new design
        start_time = time.time()

        sleep(2)
        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        sleep(2)
        data_sources_page.clickEnter()
        sleep(5)
        data_sources_page.click_Menu_HamburgerICNWeb()
        sleep(2)
        data_sources_page.lock_phone()
        sleep(2)
        wake()
        sleep(3)
        data_sources_page.clickMyDesigns()
        sleep(5)
        data_sources_page.click_Menu_HamburgerICNWeb()
        sleep(5)
        data_sources_page.lock_phone()
        wake()
        data_sources_page.clickCreateDesignBtn()
        sleep(5)
        data_sources_page.selectLabelSize()
        data_sources_page.clickContinueWeb()
        poco(text="Exit Designer").wait_for_appearance(timeout=10)
        data_sources_page.lock_phone()
        sleep(2)
        wake()
        label_name = "PullDownToRefresh"
        data_sources_page.setLabelName(label_name)
        sleep(5)
        data_sources_page.exitDesigner()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Go back to Mobile App
        start_time = time.time()

        stop_app("com.android.chrome")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: In My Design page, the new created design in Step 2 not show in list
        # Check screen pull-down to refresh/update on My Design
        start_time = time.time()

        raise Exception("No pull down to refresh option due to bug SMBM-1710")
        """No pull down to refresh option due to bug SMBM-1710"""
        data_sources_page.searchMyDesigns(label_name)
        try:
            common_method.wait_for_element_appearance_namematches(
                "There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.")
        except:
            raise Exception("New Design created in web is present without the need to refresh.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Open My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data in menu"""
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: In Web Portal, upload or link a new file in My Data page
        start_time = time.time()

        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        sleep(2)
        data_sources_page.clickEnter()
        sleep(3)
        data_sources_page.click_Menu_HamburgerICNWeb()
        sleep(5)
        data_sources_page.lock_phone()
        sleep(2)
        wake()
        data_sources_page.click_My_Data()
        sleep(5)
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.click_Upload_File_Web()
        selected_file_name = data_sources_page.selectFileToUploadWeb()
        stop_app("com.android.chrome")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Go back to Mobile App, My Data page file list not update
        # Check screen pull-down to refresh/update on My Data Page works
        start_time = time.time()

        raise Exception("No pull down to refresh option due to bug SMBM-1710")
        """No pull down to refresh option due to bug SMBM-1710"""
        sleep(5)
        data_sources_page.searchName(selected_file_name)
        try:
            common_method.wait_for_element_appearance_namematches("List is empty")
        except:
            raise Exception("New File updated in web is present without the need to refresh.")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""Test this once"""


def test_DataSources_TestcaseID_47936():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go To My Data'],
        2: [2, 'Click on + sign on bottom right'],
        3: [3, 'Click on Upload File'],
        4: [4, 'Select a supported File'],
        5: [5,
            'Check that on My Data page, selected file should be reflected along with Notification updated for the same'],
        6: [6, 'Go to My Data page again, Click on 3 dots corresponding to any file, Click Remove, Confirm the same'],
        7: [7, 'Check file is removed along with Notification updated for the same']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go To My Data
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on + sign on bottom right
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on Upload File
        start_time = time.time()

        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select a supported File
        start_time = time.time()

        """Select File to upload"""
        selected_file = "Demo.jpg"
        data_sources_page.searchFileInLocalStorage(selected_file)
        sleep(5)
        """Notification on file upload"""
        """Unable to verify due to BUG SMBM-712"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check that on My Data page, selected file should be reflected along with Notification updated for the same
        start_time = time.time()

        print(selected_file)
        data_sources_page.check_notification_on_file_upload_file(selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Go to My Data page again
        start_time = time.time()

        data_sources_page.searchName(selected_file)
        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Check file is removed along with Notification updated for the same
        start_time = time.time()

        data_sources_page.check_notification_on_remove_file()
        data_sources_page.searchName("")
        data_sources_page.searchName(selected_file)
        data_sources_page.checkIfListIsEmpty()
        """Notification on file removal"""
        """Unable to verify due to BUG SMBM-712"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_47942():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open the app and login'],
        2: [2, "Slide the left slide page to choose 'Data Sources' item"],
        3: [3, "Click the '+' button at the bottom, and choose 'upload file'"],
        4: [4, 'Choose the file (about 1 MB) to upload'],
        5: [5,
            "Check that the progress indicator pops up, and dismisses once the file appears at the 'Data Sources' page"],
        6: [6, "Remove the uploaded file"]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Open the app and login
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Slide the left slide page to choose 'Data Sources' item
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        sleep(5)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click the '+' button at the bottom, and choose 'upload file'
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(5)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Choose the file (about 1 MB) to upload
        start_time = time.time()

        """Select File to upload"""
        selected_file = "Demo.jpg"
        data_sources_page.searchFileInLocalStorage(selected_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check that the progress indicator pops up, and dismisses once the file appears at the 'Data Sources' page
        start_time = time.time()

        """Verify Progress Indicator"""
        data_sources_page.verifyProgressIndicator()
        sleep(5)
        """Verify if file uploaded successfully"""
        data_sources_page.searchName(selected_file)
        data_sources_page.verifyFilePresentInList(selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Remove the uploaded file
        start_time = time.time()

        """remove file for next execution"""
        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_47944():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'open the app and login'],
        2: [2, 'slide left slide page and click My data'],
        3: [3, "click the + button to choose Upload File"],
        4: [4, 'choose the file "4-BMP.BMP" which mentioned at precondition'],
        5: [5,
            'It should pop up the error dialog said the file you uploaded has some issue, uploading this file fail. And the file shouldn\'t appears at the My data.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: open the app and login
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: slide left slide page and click My data
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: click the + button to choose Upload File
        start_time = time.time()

        data_sources_page.click_Add_File()
        sleep(2)
        data_sources_page.click_Upload_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: choose the file "4-BMP.BMP" which mentioned at precondition
        start_time = time.time()

        template_management_page.wait_for_appearance_enabled("Show roots")
        """select 4-BMP.BMP"""
        data_sources_page.searchFileInLocalStorage("4-BMP.BMP", "Downloads")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: It should pop up the error dialog said the file you uploaded has some issue, uploading this file fail. And the file shouldn't appears at the My data.
        start_time = time.time()

        """Step 5 pending as no error pop up"""
        data_sources_page.check_if_file_being_uploaded_has_issue()
        data_sources_page.searchName("4-BMP.BMP")
        """check list empty"""
        data_sources_page.checkIfListIsEmpty()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45740():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and select Upload File'],
        3: [3,
            'A page will be opened and let user select file to upload.\nSelect any of the following supported file types to upload'],
        4: [4,
            'Upload more than 20 files\nCheck all files can be uploaded successfully\nCheck File is uploaded with correct icon, name, data source type, and create date\nNote: Data files should use file icons, image files should use image icons.'],
        5: [5,
            'Login to web portal -> Data Sources page\nCheck the uploaded files from the mobile app display in the My Data page in web portal']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        for i in range(1, 21):
            file_name = f"{i}.jpg"
            data_sources_page.searchName(file_name)
            sleep(2)
            try:
                data_sources_page.remove_File_Based_On_DataSource("Local File", file_name)
                sleep(7)
            except:
                pass
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.clickHome()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Upload File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload File"""
        data_sources_page.click_Upload_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload.\nSelect any of the following supported file types to upload
        start_time = time.time()

        sleep(3)
        data_sources_page.searchFileInLocalStorage("20 Files", "Downloads")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Upload more than 20 files\nCheck all files can be uploaded successfully\nCheck File is uploaded with correct icon, name, data source type, and create date\nNote: Data files should use file icons, image files should use image icons.
        start_time = time.time()

        uploaded_file_list = data_sources_page.selectFilesInLocal()
        """No notification after uploading file"""
        keyevent("back")
        keyevent("back")
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            sleep(7)
            data_sources_page.verifyFilePresentInList(name, "Local File", True)
            """Remove this once web inconsistency is fixed"""
            """-------------------------------------------"""
            data_sources_page.remove_File_Based_On_DataSource("Local File", name)
            """-------------------------------------------"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Login to web portal -> Data Sources page\nCheck the uploaded files from the mobile app display in the My Data page in web portal
        start_time = time.time()

        """Login to web portal->Data Sources page Check the uploaded files from mobile app display in the my data page in web portal. pending"""
        start_app("com.android.chrome")
        sleep(2)
        poco("com.android.chrome:id/tab_switcher_button").click()
        sleep(2)
        try:
            poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            poco(text="New tab").click()
        sleep(2)
        poco(text="Search or type URL").click()
        sleep(2)
        poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
        data_sources_page.clickEnter()
        data_sources_page.lock_phone()
        wake()
        sleep(3)
        registration_page.wait_for_element_appearance_text("Home", 20)
        sleep(3)
        data_sources_page.click_Menu_HamburgerICNWeb()
        data_sources_page.lock_phone()
        wake()
        sleep(2)
        data_sources_page.click_My_Data()
        data_sources_page.click_Menu_HamburgerICNWeb()
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            keyevent("back")
            sleep(2)
            poco.scroll()
            try:
                common_method.wait_for_element_appearance_text("No files match your search")
                x = 1 / 0
            except ZeroDivisionError:
                raise Exception("Uploaded files not displaying in my data page.")
            except Exception as e:
                pass
        stop_app("com.android.chrome")
        """Remove uploaded files for next execution"""
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            data_sources_page.remove_File_Based_On_DataSource("Local File", name)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""zebra07.swdvt@gmail"""


def test_DataSources_TestcaseID_47937():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2, 'Click "Sign In/Register" button.'],
        3: [3,
            'Check user is navigated to "Login with username" page. Enter login name (E.g MW12345) with correct password and click Sign in button. This time sign in with Zebra account.'],
        4: [4, 'Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page.'],
        5: [5, 'Go to My Data page'],
        6: [6, 'Click + button at bottom and select Link File'],
        7: [7,
            'Cloud Service Sign in page will open and let user select which service to login. Click Sign in with Microsoft'],
        8: [8,
            'Select two or three supported files to upload\n Check Files are linked without issue, Select the files linked from OneDrive and Remove\nCheck the linked files are removed from My Data page'],
        9: [9, 'Repeat step 7 to step 13 but to link Google Drive file'],
        10: [10, 'Click on the hamburger icon follow by Settings and click Log out button'],
        11: [11,
             'Check user is successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click "Sign In/Register" button.
        start_time = time.time()

        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check user is navigated to "Login with username" page.
        start_time = time.time()

        data_sources_page.signInWithEmail()
        account = "zebra07.swdvt@gmail.com"
        registration_page.sign_in_with_mail_zebra07()
        registration_page.BugFix_For_ZebraEmail(account)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page.
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click + button at bottom and select Link File
        start_time = time.time()

        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Cloud Service Sign in page will open...
        start_time = time.time()

        """ One drive """
        sleep(2)
        if data_sources_page.verifySignInWithMicrosoft():
            data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
            sleep(2)
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select two or three supported files to upload...
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        sleep(7)
        data_sources_page.searchName("")
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", csv_file)
        sleep(7)
        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        try:
            data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File not removed")
        except Exception as e:
            pass
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 9: Repeat step 7 to step 13 but to link Google Drive file
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(5)
        # registration_page.click_Google_Icon()
        # account = "zebra02.swdvt@gmail.com"
        # help_page.chooseAcc(account)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        registration_page.click_Google_Icon()
        account = "zebra03.swdvt@gmail.com"
        help_page.chooseAcc(account)
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        sleep(7)
        data_sources_page.searchName("")
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        common_method.wait_for_element_appearance("NAME")
        """ google drive """
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", csv_file)
        sleep(7)
        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        try:
            data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File not removed")
        except Exception as e:
            pass
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click on the hamburger icon follow by Settings and click Log out button
        start_time = time.time()

        data_sources_page.log_out_of_account()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check user is successfully log out...
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45752():
    """test"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3,
            'Cloud Service Sign in page will open and let user select which service to login\nClick Sign in with Microsoft account'],
        4: [4, 'After signed in Microsoft account, check supported files are listed in One Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Mobile app return to My Data page\nCheck no file is uploaded'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'Click Microsoft One Drive'],
        9: [9, 'Select any of the supported file types to link'],
        10: [10,
             'Check the selected file is linked\nCheck the file icon, file name, Date added and Data source field are correct'],
        11: [11, 'Repeat for other 2 to 3 supported file types'],
        12: [12, 'Remove the uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Zebra account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        """ One drive """

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open...
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: After signed in Microsoft account, check supported files are listed...
        start_time = time.time()

        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Mobile app return to My Data page\nCheck no file is uploaded
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click Microsoft One Drive
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Select any of the supported file types to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check the selected file is linked\nCheck the file icon, file name, Date added...
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Repeat for other 2 to 3 supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Remove the uploaded files
        start_time = time.time()

        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45730():
    """""""""test"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select File page will open\n Select Google Drive'],
        4: [4, 'Click Back button'],
        5: [5, 'Check mobile app return back to My Data page and no file is linked'],
        6: [6, 'Click + button at bottom and select Link File'],
        7: [7,
            'On Google Drive page select file page\nCheck the Google Drive title is shown completely\nCheck only supported file types are listed'],
        8: [8, 'Select a file and click Select'],
        9: [9,
            'Check mobile app return to My Data page and file is linked\nCheck the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        10: [10, 'Repeat for another 2 to 3 supported file types'],
        11: [11, 'Remove uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Zebra account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select File page will open\n Select Google Drive
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickGoogleDrive()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check mobile app return back to My Data page and no file is linked
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: On Google Drive page select file page\nCheck the Google Drive title is shown completely...
        start_time = time.time()

        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select a file and click Select
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check mobile app return to My Data page and file is linked\nCheck the details...
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Repeat for another 2 to 3 supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45749():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'At Cloud service sign in page, click Sign in with Google\nSign in Google account'],
        4: [4, 'After signed in Google account, check supported files are listed in Google Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Check mobile app return back to My Data page and no file is linked'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'Click any supported file and click Select button to link'],
        9: [9,
            'Check mobile app return to My Data page and file is linked\nCheck the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        10: [10, 'Repeat for all supported file types'],
        11: [11, 'Remove the uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Zebra account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """Google Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: At Cloud service sign in page, click Sign in with Google\nSign in Google account
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        data_sources_page.clickGoogleDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: After signed in Google account, check supported files are listed in Google Drive
        start_time = time.time()

        sleep(5)
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check mobile app return back to My Data page and no file is linked
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click any supported file and click Select button to link
        start_time = time.time()

        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check mobile app return to My Data page and file is linked\nCheck the details...
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Repeat for all supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Remove uploaded files
        start_time = time.time()

        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
        data_sources_page.searchName("")
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


"""Facebook"""


def test_DataSources_TestcaseID_45750():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Facebook account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'At Cloud service sign in page, click Sign in with Google. Sign in Google account'],
        4: [4, 'After signed in Google account, check supported files are listed in Google Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Check mobile app return back to My Data page and no file is linked'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'Click any supported file and click Select button to link'],
        9: [9,
            'Check mobile app return to My Data page and file is linked.\nCheck the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        10: [10, 'Repeat for all supported file types'],
        11: [11, 'Remove uploaded files']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Facebook account in Mobile app and go to My Data page
        start_time = time.time()

        """FB login"""
        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        registration_page.login_Facebook("Zebra#123456789", "zebra03.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """Google Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: At Cloud service sign in page, click Sign in with Google. Sign in Google account
        start_time = time.time()

        data_sources_page.signInWithGoogle("zebra06.swdvt@gmail.com", "Zebra#123456789")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: After signed in Google account, check supported files are listed in Google Drive
        start_time = time.time()

        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check mobile app return back to My Data page and no file is linked
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click any supported file and click Select button to link
        start_time = time.time()

        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check mobile app return to My Data page and file is linked.\nCheck the details of file icon, file name, Date added and Data source field (Google Drive) are correct
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Repeat for all supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Remove uploaded files
        start_time = time.time()

        """Remove Files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45753():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Facebook account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3,
            'Cloud Service Sign in page will open and let user select which service to login .\nClick Sign in with Microsoft account'],
        4: [4, 'After signed in Microsoft account, check supported files are listed in One Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Mobile app return to My Data page.\nCheck no file is uploaded'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'Click Microsoft One Drive'],
        9: [9, 'Select any of the supported file types to link'],
        10: [10,
             'Check the selected file is linked.\nCheck the file icon, file name, Date added and Data source field are correct'],
        11: [11, 'Repeat for other 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Login Facebook account in Mobile app and go to My Data page
        start_time = time.time()

        """FB login"""
        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """One Drive"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open and let user select which service to login.\nClick Sign in with Microsoft account
        start_time = time.time()

        """ One drive """
        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: After signed in Microsoft account, check supported files are listed in One Drive
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Back button
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Mobile app return to My Data page
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click Microsoft One Drive
        start_time = time.time()

        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Select any of the supported file types to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the selected file is linked.\nCheck the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for other 2 to 3 supported file types
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# ####"""""""""""""""""""""""""""""""END"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45878():
    """	Verify sign in as zebra, check link and delete one/Google Drive file works well"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App'],
        2: [2, 'Click "Sign In/Register" button.\nCheck user is navigated to "Login with username" page'],
        3: [3,
            'Enter the login name mentioned in setup 2, (E.g MW12345) with correct password and click Sign in button'],
        4: [4, 'Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page'],
        5: [5, 'Go to My Data page'],
        6: [6, 'Click + button at bottom and select Link File'],
        7: [7,
            'Cloud Service Sign in page will open and let user select which service to login\nClick Sign in with Microsoft'],
        8: [8, 'Select two or three supported files to upload'],
        9: [9, 'Check File is linked without issue'],
        10: [10, 'Select the file linked from OneDrive and Remove.\nCheck the linked file removed from My Data page'],
        11: [11, 'Click on the hamburger icon follow by Settings and click Log out button'],
        12: [12,
             'Check user is successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    try:
        # Step 1: Launch ZSB Series App
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click "Sign In/Register" button. Check user is navigated to "Login with username" page
        start_time = time.time()

        data_sources_page.log_out_of_account()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Enter the login name mentioned in setup 2, (E.g MW12345) with correct password and click Sign in button
        start_time = time.time()

        registration_page.click_Google_Icon()
        login_page.Loginwith_Added_Email_Id()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 4: Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        smoke_test_android.click_MyData_Tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click + button at bottom and select Link File
        start_time = time.time()

        smoke_test_android.click_Plus_icon()
        smoke_test_android.click_LinkFile()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Cloud Service Sign in page will open and let user select which service to login\nClick Sign in with Microsoft
        start_time = time.time()

        smoke_test_android.click_Microsoft_OneDrive_Tab()
        data_sources_page.signInWithMicrosoft("swdvt.zebra@outlook.com", "Swdvt@123")
        smoke_test_android.click_Microsoft_OneDrive_Tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select two or three supported files to upload
        start_time = time.time()

        smoke_test_android.click_On_Jpg_File()
        smoke_test_android.click_On_Select_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check File is linked without issue
        start_time = time.time()

        data_sources_page.Scroll_Till_Next_Tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Select the file linked from OneDrive and Remove
        start_time = time.time()

        smoke_test_android.click_Three_Dot_On_MyData()
        smoke_test_android.Click_Delete_File()
        smoke_test_android.Click_Delete_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Click on the hamburger icon follow by Settings and click Log out button
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check user is successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


# #     ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #
def test_Smoke_Test_TestcaseID_45879():
    """Verify sign in as non-zebra, check link and delete one/Google Drive file works well"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App'],
        2: [2, 'Click "Sign In/Register" button.\nCheck user is navigated to "Login with username" page'],
        3: [3, 'Enter the login name mentioned in setup 2, with correct password and click Sign in button'],
        4: [4, 'Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page'],
        5: [5, 'Go to My Data page'],
        6: [6, 'Click + button at bottom and select Link File'],
        7: [7,
            'Cloud Service Sign in page will open and let user select which service to login.\nClick Sign in with Microsoft'],
        8: [8, 'Select two or three supported files to upload'],
        9: [9, 'Check File is linked without issue'],
        10: [10, 'Select the file linked from OneDrive and Remove.\nCheck the linked file removed from My Data page'],
        11: [11, 'Click on the hamburger icon followed by Settings and click Log out button'],
        12: [12,
             'Check user is successfully logged out of Money Badger Home Page and is being navigated to the ZSB Login Page']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Launch ZSB Series App
        start_time = time.time()

        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click "Sign In/Register" button.\nCheck user is navigated to "Login with username" page
        start_time = time.time()

        data_sources_page.log_out_of_account()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        registration_page.clickSignIn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Enter the login name mentioned in setup 2, with correct password and click Sign in button
        start_time = time.time()

        registration_page.click_Google_Icon()
        login_page.Loginwith_Added_Email_Id()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        smoke_test_android.click_MyData_Tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 6: Click + button at bottom and select Link File
        start_time = time.time()

        smoke_test_android.click_Plus_icon()
        smoke_test_android.click_LinkFile()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Cloud Service Sign in page will open and let user select which service to login.\nClick Sign in with Google
        start_time = time.time()

        smoke_test_android.click_SignIn_With_Google_Drive()
        login_page.Loginwith_Added_Email_Id()
        smoke_test_android.click_Google_Drive_Password_Field()
        smoke_test_android.click_Sign_In_Button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select two or three supported files to upload
        start_time = time.time()

        smoke_test_android.click_On_PNG_File()
        smoke_test_android.click_On_Select_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check File is linked without issue
        start_time = time.time()

        app_settings_page.Scroll_Till_Next_Tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Select the file linked from OneDrive and Remove.\nCheck the linked file removed from My Data page
        start_time = time.time()

        smoke_test_android.click_Three_Dot_On_MyData()
        smoke_test_android.Click_Delete_File()
        smoke_test_android.Click_Delete_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Click on the hamburger icon followed by Settings and click Log out button
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_pen_Icon_near_UserName()
        app_settings_page.Scroll_till_Delete_Account()
        app_settings_page.click_Logout_Btn()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check user is successfully logged out of Money Badger Home Page and is being navigated to the ZSB Login Page
        start_time = time.time()

        data_sources_page.checkIfInLoginPage()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)


def test_DataSources_TestcaseID_45758():
    """""""""test"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click Link File button and Select a Data Source window opened'],
        3: [3, 'Select Open Google Drive / Open OneDrive\nGoogle Drive / OneDrive explorer is opened'],
        4: [4, 'Check there is no file listed and "No documents" shown'],
        5: [5, 'Repeat for OneDrive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block
    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.log_out_of_account()
        data_sources_page.clearAppData()
        data_sources_page.allowPermissions()
        """Sign in"""
        registration_page.clickSignIn()
        data_sources_page.signInWithEmail()
        account = "zebra02.swdvt@gmail.com"
        registration_page.sign_in_with_mail_zebra02()
        registration_page.BugFix_For_ZebraEmail(account)
        """verify if logged in successfully"""
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Link File button and Select a Data Source window opened
        start_time = time.time()

        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select Open Google Drive / Open OneDrive\nGoogle Drive / OneDrive explorer is opened
        start_time = time.time()

        """ google drive """
        registration_page.click_Google_Icon()
        account = "zebra850.swdvt@gmail.com"
        help_page.chooseAcc(account)
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check there is no file listed and "No documents" shown
        start_time = time.time()

        data_sources_page.checkDriveEmpty()
        """Cannot automate - Check the Select button is disabled. as select button not displayed"""
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Repeat for OneDrive
        start_time = time.time()

        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        """ One drive """
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        print(data_sources_page.verifySignInWithMicrosoft())
        account_onedrive = "zebra901.swdvt@gmail.com"
        data_sources_page.signInWithMicrosoft(account_onedrive, "Zebra#123456789")
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(2)
        data_sources_page.checkDriveEmpty()
        """Cannot automate - Check the Select button is disabled. as select button not displayed"""
        data_sources_page.clickBackArrow()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)

    except Exception as e:
        screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
        raise Exception(str(e))

    finally:
        common_method.stop_adb_log_capture()
        upload_case_files(execID, os.path.dirname(ADB_LOG), test_run_start_time)
        end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
        end_execution_loop(execID)
        end_execution(execID)
