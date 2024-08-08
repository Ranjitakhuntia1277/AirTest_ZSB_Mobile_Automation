import inspect

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Login_Screen import *

from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...PageObject.Others_Screen.Others_Screen import Others
import pytest
from ...TestSuite.api_call import *
from ...TestSuite.store import *


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



def test_DataSources_TestcaseID_45729():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Sign in the account and click My Data option.'],
        2: [2, 'Click + button at bottom and select Link File.'],
        3: [3, 'Google Drive will be opened and let user select file to link.'],
        4: [4,
            'Select the file with Special character from Google Drive. Check the selected file is linked. Check the details of the File name, Source and Date added (Today) of the linked file are shown correctly.'],
        5: [5,
            'Select the file with long file name from Google Drive. Check the selected file is linked. Check the details of the File name, Source and Date added (Today) of the linked file are shown correctly.'],
        6: [6, 'Remove these 2 files. Check these 2 files are able to remove.'],
        7: [7, 'Repeat this test case for OneDrive.'],
        8: [8, 'Also check Account Settings page should provide user management of Google and OneDrive accounts.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Sign in the account and click My Data option.
        start_time = time.time()

        """Google Login"""
        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        account = "zebra03.swdvt@gmail.com"
        if template_management_page.checkIfAccPresent(account):
            help_page.chooseAcc(account)
        else:
            count = 5
            while not poco(text="Use another account").exists() and count != 0:
                poco.scroll()
                count -= 1
            login_page.click_GooglemailId()
            if poco(text="Signed in to Google as").exists():
                count = 5
                while not poco(text="Add account to device").exists() and count != 0:
                    poco.scroll()
                    count -= 1
                registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra03.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File.
        start_time = time.time()

        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ google drive """
        registration_page.click_Google_Icon()
        help_page.chooseAcc("zebra03.swdvt@gmail.com")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Google Drive will be opened and let user select file to link.
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance("NAME")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select the file with Special character from Google Drive. Check the selected file is linked. Check the details of the File name, Source and Date added (Today) of the linked file are shown correctly.
        start_time = time.time()

        """Select file with special characters"""
        special_char_file = "A_!@#$%^^&(().xlsx"
        data_sources_page.selectFileDrive(special_char_file)
        sleep(5)
        data_sources_page.searchName(special_char_file)
        data_sources_page.verify_File_Data(special_char_file, "Google Drive")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select the file with long file name from Google Drive. Check the selected file is linked. Check the details of the File name, Source and Date added (Today) of the linked file are shown correctly.
        start_time = time.time()

        data_sources_page.searchName("")
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Remove these 2 files. Check these 2 files are able to remove.
        start_time = time.time()

        data_sources_page.searchName("")
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

        # Step 7: Repeat this test case for OneDrive.
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
        sleep(2)
        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
        common_method.wait_for_element_appearance("NAME")
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Also check Account Settings page should provide user management of Google and OneDrive accounts.
        start_time = time.time()

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



# def test_DataSources_TestcaseID_45733():
#     """test"""
#
#
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
        3: [3, 'Select Google drive'],
        4: [4, 'Google Drive page will open and let user select file to link'],
        5: [5, 'Select a not-supported file types to link (Check only supported files are listed)'],
        6: [6,
            'Select a supported file type but file size exceed maximum allowed size (Max file size is 28.4 MB) Check there is a prompt message for telling user the file is too big'],
        7: [7,
            'Select a same file name which already existed in app to upload Check there is a prompt message for telling user the file is existed, like "file name is already linked"'],
        8: [8, 'Repeat this test case for OneDrive, check it works same for OneDrive file']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom and select Link File
        start_time = time.time()

        sleep(3)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select Google drive
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Google Drive page will open and let user select file to link
        start_time = time.time()

        """Test for Google Drive"""
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select a not-supported file types to link (Check only supported files are listed)
        start_time = time.time()

        """Cannot select unsupported file"""
        data_sources_page.checkFilesShownAreSupported()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Select a supported file type but file size exceed maximum allowed size (Max file size is 28.4 MB) Check there is a prompt message for telling user the file is too big
        start_time = time.time()

        large_file = "large_unsupported_file(50mb).png"
        data_sources_page.selectFileDrive(large_file)
        raise Exception("No prompt message on uploading file greater than 28.4mb")
        """No prompt message on uploading file greater than 28.4mb"""
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Select a same file name which already existed in app to upload Check there is a prompt message for telling user the file is existed, like "file name is already linked"
        start_time = time.time()

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

        # Step 8: Repeat this test case for OneDrive, check it works same for OneDrive file
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
        data_sources_page.checkFilesShownAreSupported()
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
        data_sources_page.searchName("")
        sleep(2)
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
        10: [10, 'Check mobile app return to My Data page and file is linked'],
        11: [11, 'Check the details of file icon, file name, Date added and Data source field (One Drive) are correct'],
        12: [12, 'Repeat for another 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

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
        """ One drive """
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select File page will open
        start_time = time.time()

        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select One Drive
        start_time = time.time()

        data_sources_page.clickMicrosoftOneDrive()
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
        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)

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

        # Step 10: Check mobile app return to My Data page and file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the details of file icon, file name, Date added and Data source field (One Drive) are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for another 2 to 3 supported file types
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
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


def test_DataSources_TestcaseID_45736():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click the 3 dot menu from a file which linked from Google Drive'],
        3: [3, 'Select Remove option'],
        4: [4,
            'A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will need to be reconnected to a data source."'],
        5: [5, 'Select Cancel button'],
        6: [6, 'Check the linked file is not removed'],
        7: [7, 'Click the 3 dot menu from a file which linked from Google Drive'],
        8: [8, 'Select Remove button'],
        9: [9, 'Check the linked file is removed.'],
        10: [10, 'Log into web portal and check the linked file is removed'],
        11: [11, 'Repeat the test case and remove linked file from One Drive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click the 3 dot menu from a file which linked from Google Drive
        start_time = time.time()

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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
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
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select Remove option
        start_time = time.time()

        """Google Drive"""
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file, True, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will need to be reconnected to a data source."
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select Cancel button
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the linked file is not removed
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(txt_file)
        data_sources_page.checkFileNotRemovedAfterClickingCancel(txt_file, "Google Drive")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click the 3 dot menu from a file which linked from Google Drive
        start_time = time.time()

        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select Remove button
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(txt_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check the linked file is removed
        start_time = time.time()

        data_sources_page.checkFileRemovedSuccessfully(txt_file, "Google Drive")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Log into web portal and check the linked file is removed
        start_time = time.time()

        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Repeat the test case and remove linked file from One Drive
        start_time = time.time()

        """One Drive"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file, True, True)
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.checkFileNotRemovedAfterClickingCancel(png_file, "OneDrive")
        sleep(2)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.checkFileRemovedSuccessfully(png_file, "OneDrive")
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


def test_DataSources_TestcaseID_45737():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click the 3 dot menu from a file which linked from Google Drive'],
        3: [3, 'Select Remove option'],
        4: [4,
            'A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will convert to manual input fields."'],
        5: [5, 'Select Remove button'],
        6: [6, 'Check the linked file is removed.'],
        7: [7, 'Print the label design, mobile app will prompt user to Update Data Connections'],
        8: [8, 'Choose the linked excel file in precondition step 4, click next'],
        9: [9,
            'Choose the new column, click next. Check that preview dialog shown. Navigate to check different preview images are correct'],
        10: [10,
             'Click print, then click label range field, just select some rows, click confirm. Check that only the selected row number are shown in the label range field. Navigate to check that only the select rows can be previewed. Check that the total number is correct and the same as your selected row amount'],
        11: [11, 'Click print. Check that only the selected row data are printed out'],
        12: [12, 'Repeat the test case and remove linked file in step 2 from One Drive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        account = "zebra02.swdvt@gmail.com"
        if template_management_page.checkIfAccPresent(account):
            help_page.chooseAcc(account)
        else:
            count = 5
            while not poco(text="Use another account").exists() and count != 0:
                poco.scroll()
                count -= 1
            login_page.click_GooglemailId()
            if poco(text="Signed in to Google as").exists():
                count = 5
                while not poco(text="Add account to device").exists() and count != 0:
                    poco.scroll()
                    count -= 1
                registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra03.swdvt@gmail.com")
        try:
            registration_page.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("home page dint show up")
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click the 3 dot menu from a file which linked from Google Drive
        start_time = time.time()

        removed_file_name = "45737_original.xlsx"
        data_sources_page.searchName(removed_file_name)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select Remove option
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Google Drive", removed_file_name, False, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: A confirmation pop up "Remove linked file - Are you sure you want to remove the linked file? All fields using this data source will convert to manual input fields."
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select Remove button
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the linked file is removed.
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(removed_file_name)
        data_sources_page.checkFileRemovedSuccessfully(removed_file_name, "Google Drive")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Print the label design, mobile app will prompt user to Update Data Connections
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        common_method.wait_for_element_appearance_namematches("Showing", 15)
        data_sources_page.searchMyDesigns("45737")
        common_method.wait_for_element_appearance_namematches("Showing", 15)
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        data_sources_page.chooseAccToLinkFile()
        try:
            common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
            data_sources_page.clickBackArrow()
        except:
            pass

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Choose the linked excel file in precondition step 4, click next
        start_time = time.time()

        template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (Google Drive)")
        data_sources_page.clickContinue()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Choose the new column, click next. Check that preview dialog shown. Navigate to check different preview images are correct
        start_time = time.time()

        template_management_page.selectChooseAnOption(1)
        data_sources_page.clickContinue()
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        """Cannot automate - navigate to check different preview images are correct-has to be verified manually"""
        data_sources_page.scroll_till_print()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click print, then click label range field, just select some rows, click confirm. Check that only the selected row number are shown in the label range field. Navigate to check that only the select rows can be previewed. Check that the total number is correct and the same as your selected row amount
        start_time = time.time()

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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Click print. Check that only the selected row data are printed out
        start_time = time.time()

        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat the test case and remove linked file in step 2 from One Drive
        start_time = time.time()

        data_sources_page.clickBackArrow()
        data_sources_page.checkIfDesignsLoaded()
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        try:
            common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
            data_sources_page.clickBackArrow()
        except:
            pass
        template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (OneDrive)")
        account = "zebra03.swdvt@gmail.com"
        data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
        sleep(5)
        if template_management_page.continueDisabled() and not template_management_page.checkIfOnRelinkDataSourcesPage:
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
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
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
        sleep(5)
        if data_sources_page.verifySignInWithGoogle():
            registration_page.click_Google_Icon()
            account = "zebra03.swdvt@gmail.com"
            if data_sources_page.checkIfAccPresentLink(account):
                help_page.chooseAcc(account)
            else:
                poco("com.google.android.gms:id/add_account_chip_title").click()
                registration_page.sign_In_With_Google("Zebra#123456789", account)
                sleep(2)
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_DataSources_TestcaseID_45739():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4, 'Click back button to return to mobile app. Check no file is uploaded'],
        5: [5, 'Click + button at bottom and select Upload File'],
        6: [6,
            'Select any of the following supported file types to upload. Check File is uploaded with correct icon, name, data source type and create date. Note: Data files should use file icons, images files should use image icons. Check there is notification " has been successfully uploaded"'],
        7: [7,
            'Login to web portal->Data Sources page. Check the uploaded files from mobile app display in the my data page in web portal. Check switch to different menu or press F5 should be able to refresh the file list.'],
        8: [8, 'Repeat for all supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        sleep(3)
        if poco("My Data").exists():
            raise Exception("Page to select file to upload not opened.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click back button to return to mobile app. Check no file is uploaded
        start_time = time.time()

        while not poco("My Data").exists():
            keyevent("back")
            sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click + button at bottom and select Upload File
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

        # Step 6: Select any of the following supported file types to upload. Check File is uploaded with correct icon, name, data source type and create date. Note: Data files should use file icons, images files should use image icons. Check there is notification " has been successfully uploaded"
        start_time = time.time()

        data_sources_page.searchFileInLocalStorage("Supported Files", "Downloads")
        sleep(2)
        uploaded_file_list = ["bmp_file.bmp", "jpg_file.jpg", "png_file.png", "csv_file.csv", "text_file.txt"]
        data_sources_page.selectFilesInLocal()
        """No notification after uploading file"""
        keyevent("back")
        keyevent("back")
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            sleep(7)
            data_sources_page.verifyFilePresentInList(name, "Local File", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Login to web portal->Data Sources page. Check the uploaded files from mobile app display in the my data page in web portal. Check switch to different menu or press F5 should be able to refresh the file list.
        start_time = time.time()

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
        data_sources_page.checkIfOnHomePageWeb()
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
        stepId += 1

        # Step 8: Repeat for all supported file types
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


def test_DataSources_TestcaseID_45744():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4,
            'Select a file which name is same as the file existing uploaded from local. Check it allow user to upload same file and add suffix(1) to the later upload file name'],
        5: [5,
            'Select a file which name is same as the file existing uploaded from cloud. Check the file can be uploaded successfully']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select a file which name is same as the file existing uploaded from local. Check it allow user to upload same file and add suffix(1) to the later upload file name
        start_time = time.time()

        """Select File to upload"""
        file_name = "drive_file.jpg"
        data_sources_page.searchFileInLocalStorage(file_name, "Downloads")
        sleep(5)
        """Upload the same file again"""
        """Click Add File"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload file"""
        data_sources_page.click_Upload_File()
        sleep(5)
        data_sources_page.searchFileInLocalStorage(file_name, "Downloads")
        sleep(5)
        search_name = file_name.split(".")[0]
        extension = file_name.split(".")[1]
        data_sources_page.searchName(search_name)
        file_list = data_sources_page.fileListDisplayed()
        if (search_name + "." + extension in file_list) and (search_name + " (1)" + "." + extension in file_list):
            pass
        else:
            raise Exception("Re-uploading not appended '(1)' to file name")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        "remove file for next execution"
        data_sources_page.searchName("")
        removing_files = [search_name + " (1)", search_name]
        for i in removing_files:
            data_sources_page.searchName(i)
            data_sources_page.remove_File()

        # Step 5: Select a file which name is same as the file existing uploaded from cloud. Check the file can be uploaded successfully
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Upload File"""
        data_sources_page.click_Upload_File()
        sleep(5)
        data_sources_page.searchFileInLocalStorage(file_name)
        sleep(7)
        data_sources_page.searchName(file_name)
        data_sources_page.verifyFilePresentInList(file_name, "Local File", True)
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link file"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        data_sources_page.selectFileDrive(file_name)
        sleep(5)
        """Remove files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(file_name)
        data_sources_page.remove_File_Based_On_DataSource("Local File", file_name)
        data_sources_page.searchName("")
        data_sources_page.searchName(file_name)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", file_name)
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


def test_DataSources_TestcaseID_45740():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at bottom and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4, 'Select any of the following supported file types to upload'],
        5: [5,
            'Upload more than 20 files. Check all files can be uploaded successfully. Check File is uploaded with correct icon, name, data source type and create date. Note: Data files should use file icons, images files should use image icons.'],
        6: [6,
            'Login to web portal->Data Sources page. Check the uploaded files from mobile app display in the my data page in web portal.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: A page will be opened and let user select file to upload
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select any of the following supported file types to upload
        start_time = time.time()

        data_sources_page.searchFileInLocalStorage("20 Files", "Downloads")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Upload more than 20 files. Check all files can be uploaded successfully. Check File is uploaded with correct icon, name, data source type and create date. Note: Data files should use file icons, images files should use image icons.
        start_time = time.time()

        uploaded_file_list = data_sources_page.selectFilesInLocal()
        """No notification after uploading file"""
        keyevent("back")
        keyevent("back")
        for name in uploaded_file_list:
            data_sources_page.searchName(name)
            sleep(7)
            data_sources_page.verifyFilePresentInList(name, "Local File", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Login to web portal->Data Sources page. Check the uploaded files from mobile app display in the my data page in web portal.
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_DataSources_TestcaseID_45741():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click 3 dots menu for a local file'],
        3: [3, 'Click Remove'],
        4: [4, 'Message prompt "Remove local file" to let user to confirm'],
        5: [5, 'Click Cancel'],
        6: [6, 'Check the selected file is not been deleted'],
        7: [7, 'Click 3 dots menu for selected file again'],
        8: [8, 'Click Remove'],
        9: [9, 'Message prompt "Remove local file" to let user to confirm'],
        10: [10,
             'Click Delete button. Check the selected file is deleted from the list (no need to refresh the page manually)'],
        11: [11, 'Go to web portal to check if the file is removed from web portal as well.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        """setup - Upload a file from local to execute"""

        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click 3 dots menu for a local file
        start_time = time.time()

        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select File to upload"""
        selected_file_name = "shubham-unsplash.jpg"
        data_sources_page.searchFileInLocalStorage(selected_file_name, "Downloads")
        sleep(10)
        data_sources_page.searchName(selected_file_name)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click Remove
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Message prompt "Remove local file" to let user to confirm
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Cancel
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the selected file has not been deleted
        start_time = time.time()

        data_sources_page.checkFileNotRemovedAfterClickingCancel(selected_file_name, "Local File")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click 3 dots menu for selected file again
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click Remove
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Message prompt "Remove local file" to let user to confirm
        start_time = time.time()

        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click Delete button. Check the selected file is deleted from the list (no need to refresh the page manually)
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(selected_file_name)
        data_sources_page.checkFileRemovedSuccessfully(selected_file_name, "Local File")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Go to web portal to check if the file is removed from web portal as well.
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_DataSources_TestcaseID_45742():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click 3 dots menu for a local file'],
        3: [3, 'Click Remove'],
        4: [4, 'Message prompt "Remove local file" to let user to confirm'],
        5: [5, 'Click Cancel'],
        6: [6, 'Check the selected file is not been deleted'],
        7: [7, 'Click 3 dots menu for selected file again'],
        8: [8, 'Click Remove'],
        9: [9, 'Message prompt "Remove local file" to let user to confirm'],
        10: [10,
             'Click Delete button. Check the selected file is deleted from the list (no need to refresh the page manually)'],
        11: [11, 'Go to web portal to check if the file is removed from web portal as well.'],
        12: [12, 'Print the template and check it should prompt user to link or input data manually.'],
        13: [13,
             'Try to link a new file or input data manually when print the template. Check user can link a new file or input data manually and print out successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()
        login_page.click_Menu_HamburgerICN()
        sleep(5)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)

        # Step 2: Click 3 dots menu for a local file
        start_time = time.time()

        remove_file_name = "ferry.xlsx"
        data_sources_page.searchName(remove_file_name)
        data_sources_page.remove_File_Based_On_DataSource("Local File", remove_file_name, True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click Remove
        start_time = time.time()
        # Implement step 3
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Message prompt "Remove local file" to let user to confirm
        start_time = time.time()
        # Implement step 4
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Cancel
        start_time = time.time()
        # Implement step 5
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the selected file is not been deleted
        start_time = time.time()

        data_sources_page.checkFileNotRemovedAfterClickingCancel(remove_file_name, "Local File")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click 3 dots menu for selected file again
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", remove_file_name)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click Remove
        start_time = time.time()
        # Implement step 8
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Message prompt "Remove local file" to let user to confirm
        start_time = time.time()
        # Implement step 9
        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Click Delete button. Check the selected file is deleted from the list (no need to refresh the page manually)
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(remove_file_name)
        data_sources_page.checkFileRemovedSuccessfully(remove_file_name, "Local File")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Go to web portal to check if the file is removed from web portal as well.
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

        # Step 12: Print the template and check it should prompt user to link or input data manually.
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
        data_sources_page.clickContinueWeb()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Try to link a new file or input data manually when print the template. Check user can link a new file or input data manually and print out successfully.
        start_time = time.time()

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
        """Re-upload the file for next execution"""
        login_page.click_Menu_HamburgerICN()
        data_sources_page.click_My_Data()
        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        data_sources_page.searchFileInLocalStorage(remove_file_name, "Downloads")
        sleep(10)
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


def test_DataSources_TestcaseID_45743():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Goto Mobile app -> My Data page'],
        2: [2,
            'Click + button at bottom. For iOS: Check only the supported file types can be selectable. For Android: In Android, if you selects a third party file browser, eg. Files in huawei, or ES, then you will be able to select those unsupported files types, then select an unsupported file. If you open the default file browser then only the supported file types can be selectable.'],
        3: [3, 'click or double click on the grey out files. Check the file is not able to selected.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Goto Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click + button at bottom. For iOS: Check only the supported file types can be selectable. For Android: In Android, if you selects a third party file browser, eg. Files in huawei, or ES, then you will be able to select those unsupported files types, then select an unsupported file. If you open the default file browser then only the supported file types can be selectable.
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

        # Step 3: click or double click on the grey out files. Check the file is not able to selected.
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_DataSources_TestcaseID_45745():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Goto Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4,
            'Select a file with below special characters to upload @ & () $ ! ^ = ~ {} [] ; "" _ - # % and Chinese. [Vicky] there will be no error for invalid characters, and those characters are just ignored in the name. Check the file can be uploaded successfully without error'],
        5: [5, 'Repeat to upload files to cover all above special characters.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Goto Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
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

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select a file with below special characters to upload @ & () $ ! ^ = ~ {} [] ; "" _ - # % and Chinese. [Vicky] there will be no error for invalid characters, and those characters are just ignored in the name. Check the file can be uploaded successfully without error
        start_time = time.time()

        ignored_char = '&""#%'
        special_char_file1 = "M@xi!mum_#Power%.jpg"
        special_char_file2 = "un$et_{&}_D@zzle.jpg"
        """Select File to upload"""
        data_sources_page.searchFileInLocalStorage(special_char_file1, "Downloads")
        sleep(7)
        for char in ignored_char:
            special_char_file1 = special_char_file1.replace(char, '')
        data_sources_page.searchName(special_char_file1)
        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(special_char_file1)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Repeat to upload files to cover all above special characters.
        start_time = time.time()

        """Select File to upload"""
        sleep(2)
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        data_sources_page.searchFileInLocalStorage(special_char_file2, "Downloads")
        sleep(7)
        for char in ignored_char:
            special_char_file2 = special_char_file2.replace(char, '')
        data_sources_page.searchName(special_char_file2)
        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(special_char_file2)
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


def test_DataSources_TestcaseID_45746():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click + button at the bottom, and select Upload File'],
        3: [3, 'A page will be opened and let user select file to upload'],
        4: [4, 'Select a file with 64 characters in the file name'],
        5: [5, 'Check it can be uploaded successfully.'],
        6: [6, 'Check the file icon, file name, Date added and Data source field are correct']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
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

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select a file with 64 characters in the file name
        start_time = time.time()

        long_name_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
        """Select File to upload"""
        data_sources_page.searchFileInLocalStorage(long_name_file, "Downloads")
        sleep(7)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check it can be uploaded successfully.
        start_time = time.time()

        data_sources_page.searchName(long_name_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        """Verify If File Uploaded Successfully"""
        data_sources_page.verifyFilePresentInList(long_name_file)
        """Remove file for next execution"""
        data_sources_page.remove_File_Based_On_DataSource("Local File", long_name_file)
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
        6: [6, 'Check the file can be uploaded successfully.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        common_method.tearDown()
        """Click hamburger icon to expand menu"""
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        """Large file"""
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
        large_file = "large_unsupported_file(50mb).png"
        data_sources_page.searchFileInLocalStorage(large_file, "Downloads")
        sleep(20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Check the file can not be uploaded.
        start_time = time.time()

        data_sources_page.searchName(large_file)
        try:
            data_sources_page.verifyFilePresentInList(large_file, "Local File", True)
            x = 1 / 0
        except ZeroDivisionError:
            data_sources_page.remove_File_Based_On_DataSource("Local File", large_file)
            raise Exception("We are able to upload file larger than 28.4 MB.")
        except Exception as e:
            pass
        """unable to verify error as there is no error popping up if file exceeds 28.4mb"""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Repeat the test with file size 28.3MB and 28.4MB.
        start_time = time.time()

        """28.3mb file"""
        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select File of size 28.3mb to upload"""
        data_sources_page.searchFileInLocalStorage("28.3M.png", "Downloads")
        sleep(5)
        """Click Add File"""
        data_sources_page.click_Add_File()
        """Click Upload file"""
        sleep(2)
        data_sources_page.click_Upload_File()
        """Select File of size 28.4 to upload"""
        data_sources_page.searchFileInLocalStorage("29.4M.png", "Downloads")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the file can be uploaded successfully.
        start_time = time.time()
        data_sources_page.searchName("28.3M.png")
        data_sources_page.verifyFilePresentInList("28.3M.png", "Local File", True)
        data_sources_page.searchName("")
        data_sources_page.searchName("29.4m.png")
        data_sources_page.verifyFilePresentInList("29.4m.png", "Local File", True)
        """Remove uploaded files for next execution"""
        data_sources_page.remove_File_Based_On_DataSource("Local File", "29.4m.png")
        data_sources_page.searchName("28.3M.png")
        data_sources_page.remove_File_Based_On_DataSource("Local File", "28.3M.png")
        data_sources_page.searchName(large_file)
        data_sources_page.remove_File_Based_On_DataSource("Local File", large_file)
        common_method.tearDown()
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


# def test_DataSources_TestcaseID_45748():
#     """test"""
#
#     common_method.tearDown()
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
        7: [7, 'Mobile app return to My Data page'],
        8: [8, 'Check no file is uploaded'],
        9: [9, 'Click + button at bottom and select Link File'],
        10: [10, 'Click Microsoft One Drive'],
        11: [11, 'Select any of the supported file types to link'],
        12: [12, 'Check the selected file is linked'],
        13: [13, 'Check the file icon, file name, Date added and Data source field are correct'],
        14: [14, 'Repeat for other 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Google account in Mobile app and go to My Data page
        start_time = time.time()

        """Google Login"""
        common_method.tearDown()
        try:
            registration_page.wait_for_element_appearance("Home", 30)
        except:
            raise Exception("Home page dint show up")
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open and let user select which service to login
        start_time = time.time()

        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Sign in with Microsoft account
        start_time = time.time()

        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Microsoft account, check supported files are listed in One Drive
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
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

        # Step 7: Mobile app return to My Data page
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Check no file is uploaded
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click + button at bottom and select Link File
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

        # Step 10: Click Microsoft One Drive
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Select any of the supported file types to link
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check the selected file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Check the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Repeat for other 2 to 3 supported file types
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
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
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
#     data_sources_page.scroll_till_print()
#     """Set the label range accordingly"""
#     selection_range = 4
#     data_sources_page.labelRangeSelection(selection_range)
#     """Verify if preview label range is according to the label range set"""
#     template_management_page.verify_label_navigation()
#     data_sources_page.scroll_till_print()
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
        3: [3, 'Click the print button, check there is an option for choosing a picture object'],
        4: [4, 'Choose Camera option, take a photo and upload it, check the preview is correct'],
        5: [5, 'Click the print button, check the printed label is correct']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Designs
        start_time = time.time()

        common_method.tearDown()
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

        # Step 3: Click the print button, check there is an option for choosing a picture object
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

        # Step 4: Choose Camera option, take a photo and upload it, check the preview is correct
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click the print button, check the printed label is correct

        start_time = time.time()
        """Print the photo"""
        data_sources_page.scroll_till_print()
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
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


def test_DataSources_TestcaseID_45759():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login to Mobile App'],
        2: [2, 'Go to My Data page'],
        3: [3, "Click on the 'link file' button and follow the link to the Google Drive file"],
        4: [4, 'Click on Google drive login on with prepared google account'],
        5: [5, 'Select one file from Google Drive file list, check file shows in My Data list'],
        6: [6, 'Repeat step 3-4, select the same file to link, validate message "xxx(file name) is already linked"'],
        7: [7, 'Repeat step 3 to 6 to cover OneDrive, check it works well']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login to Mobile App
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Go to My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on the 'link file' button and follow the link to the Google Drive file
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

        # Step 4: Click on Google drive login on with prepared google account
        start_time = time.time()

        """ google drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Select one file from Google Drive file list, check file shows in My Data list
        start_time = time.time()

        existing_file = data_sources_page.selectExistingFile()
        sleep(5)
        data_sources_page.searchName(existing_file)
        data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Repeat step 3-4, select the same file to link, validate message "xxx(file name) is already linked"
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
        data_sources_page.selectExistingFile()
        sleep(2)
        """Verify if 'filename' is already linked pop up appears"""
        data_sources_page.checkIsAlreadyLinkedPopUp()
        sleep(3)
        """remove file for next execution"""
        data_sources_page.searchName(existing_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", existing_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Repeat step 3 to 6 to cover OneDrive, check it works well
        start_time = time.time()

        """ One Drive """
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        data_sources_page.clickMicrosoftOneDrive()
        sleep(2)
        if data_sources_page.verifySignInWithMicrosoft():
            data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
            sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        common_method.wait_for_element_appearance("NAME")
        sleep(3)
        existing_file = data_sources_page.selectExistingFile()
        sleep(3)
        data_sources_page.searchName(existing_file)
        data_sources_page.verifyFilePresentInList(existing_file, "OneDrive", True)
        """Re upload same file"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """CLick Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        data_sources_page.clickMicrosoftOneDrive()
        sleep(2)
        data_sources_page.selectExistingFile()
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


def test_DataSources_TestcaseID_47830():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login in mobile app'],
        2: [2, 'Go to My Design Page'],
        3: [3, 'Login to Web Portal with same test account, create a new design'],
        4: [4, 'Go back to Mobile App'],
        5: [5, 'In My Design page, the newly created design in Step 4 does not show in the list'],
        6: [6, 'Open My Data page'],
        7: [7, 'In Web Portal, upload or link a new file in My Data page'],
        8: [8,
            'Go back to Mobile App, My Data page file list does not update. Check screen pull-down to refresh/update on My Design/My File Page works']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login in mobile app
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Go to My Design Page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Designs in menu"""
        data_sources_page.clickMyDesigns()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Login to Web Portal with same test account, create a new design
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

        # Step 4: Go back to Mobile App
        start_time = time.time()

        stop_app("com.android.chrome")
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: In My Design page, the newly created design in Step 4 does not show in the list
        start_time = time.time()

        raise Exception("No pull down to refresh option due to bug SMBM-1710")
        """No pull down to refresh option due to bug SMBM-1710"""
        data_sources_page.searchMyDesigns(label_name)
        try:
            common_method.wait_for_element_appearance_namematches(
                "There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.")
        except:
            data_sources_page.selectDesignCreatedAtSetUp()
            template_management_page.clickDeleteDesign()
            template_management_page.clickDeleteDesign()
            raise Exception("New Design created in web is present without the need to refresh.")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Open My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data in menu"""
        data_sources_page.click_My_Data()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: In Web Portal, upload or link a new file in My Data page
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Go back to Mobile App, My Data page file list does not update.Check screen pull-down to refresh/update on My Design/My File Page works
        start_time = time.time()

        stop_app("com.android.chrome")
        raise Exception("No pull down to refresh option due to bug SMBM-1710")
        """No pull down to refresh option due to bug SMBM-1710"""
        sleep(5)
        data_sources_page.searchName(selected_file_name)
        try:
            common_method.wait_for_element_appearance_namematches("List is empty")
        except:
            data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name)
            raise Exception("New File updated in web is present without the need to refresh.")
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
            'Check that on My Data page, the selected file should be reflected along with a notification updated for the same.'],
        6: [6, 'Go to My Data page again'],
        7: [7, 'Click on 3 dots corresponding to any file'],
        8: [8, 'Click Remove'],
        9: [9, 'Confirm the same'],
        10: [10, 'File should be removed along with a notification updated for the same.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go To My Data
        start_time = time.time()

        common_method.tearDown()
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

        """Select supported File to upload"""
        selected_file = "Demo.jpg"
        data_sources_page.searchFileInLocalStorage(selected_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check that on My Data page, the selected file should be reflected along with a notification updated for the same.
        start_time = time.time()

        """Notification on file upload"""
        """Unable to verify due to BUG SMBM-712"""
        print(selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Go to My Data page again
        start_time = time.time()

        data_sources_page.searchName(selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click on 3 dots corresponding to any file
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Click Remove
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Confirm the same
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: File should be removed along with a notification updated for the same.
        start_time = time.time()

        """Notification on file removal"""
        """Unable to verify due to BUG SMBM-712"""
        raise Exception("No notification on uploading and removing file")
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


def test_DataSources_TestcaseID_47942():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open the app and login'],
        2: [2, 'Slide the left slide page to choose "Data Sources" item'],
        3: [3, 'Click the "+" button at the bottom, and choose "upload file"'],
        4: [4, 'Choose the file (about 1 MB) to upload'],
        5: [5,
            'It should pop up the progress indicator, and dismiss until the file appears at the "Data Sources" page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Open the app and login
        start_time = time.time()

        common_method.tearDown()
        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Slide the left slide page to choose "Data Sources" item
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

        # Step 3: Click the "+" button at the bottom, and choose "upload file"
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: It should pop up the progress indicator, and dismiss until the file appears at the "Data Sources" page.
        start_time = time.time()

        """Verify Progress Indicator"""
        data_sources_page.verifyProgressIndicator()
        sleep(5)
        """Verify if file uploaded successfully"""
        data_sources_page.searchName(selected_file)
        data_sources_page.verifyFilePresentInList(selected_file)
        """remove file for next execution"""
        data_sources_page.searchName(selected_file)
        data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file)
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


def test_DataSources_TestcaseID_47944():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Open the app and login'],
        2: [2, 'Slide left slide page and click My Data'],
        3: [3, 'Click the + button to choose Upload File'],
        4: [4, 'Choose the file "4-BMP.BMP" which is mentioned in the precondition'],
        5: [5,
            'It should pop up the error dialog saying the file you uploaded has some issue, uploading this file failed. The file should not appear in My Data.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Open the app and login
        start_time = time.time()

        """Click hamburger icon to expand menu"""
        common_method.tearDown()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Slide left slide page and click My Data
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click the + button to choose Upload File
        start_time = time.time()

        data_sources_page.click_Add_File()
        sleep(2)
        data_sources_page.click_Upload_File()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Choose the file "4-BMP.BMP" which is mentioned in the precondition
        start_time = time.time()

        template_management_page.wait_for_appearance_enabled("Show roots")
        """select 4-BMP.BMP"""
        data_sources_page.searchFileInLocalStorage("4-BMP.BMP", "Downloads")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: It should pop up the error dialog saying the file you uploaded has some issue, uploading this file failed. The file should not appear in My Data.
        start_time = time.time()

        raise Exception("No error pop up form uploading broken file")
        """Step 5 pending as no error pop up"""
        data_sources_page.searchName("4-BMP.BMP")
        """check list empty"""
        data_sources_page.checkIfListIsEmpty()
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


def test_DataSources_TestcaseID_45758():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Data page'],
        2: [2, 'Click Link File button and Select a Data Source window opened'],
        3: [3, 'Select Open Google Drive / Open OneDrive'],
        4: [4, 'Google Drive / OneDrive explorer is opened'],
        5: [5, 'Check there is no file listed and "No documents" shown'],
        6: [6, 'Check the Select button is disabled'],
        7: [7, 'Repeat for OneDrive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Data page
        start_time = time.time()

        data_sources_page.clearAppData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.clickSignIn()
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        account = "zebra02.swdvt@gmail.com"
        if template_management_page.checkIfAccPresent(account):
            help_page.chooseAcc(account)
        else:
            count = 5
            while not poco(text="Use another account").exists() and count != 0:
                poco.scroll()
                count -= 1
            login_page.click_GooglemailId()
            if poco(text="Signed in to Google as").exists():
                count = 5
                while not poco(text="Add account to device").exists() and count != 0:
                    poco.scroll()
                    count -= 1
                registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
        """Click hamburger icon to expand menu"""
        try:
            registration_page.wait_for_element_appearance("Home", 30)
        except:
            raise Exception("home page dint show up")
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

        # Step 3: Select Open Google Drive / Open OneDrive
        start_time = time.time()

        """ google drive """
        if data_sources_page.verifySignInWithGoogle():
            registration_page.click_Google_Icon()
        account = "zebratest850@gmail.com"
        if data_sources_page.checkIfAccPresentLink(account):
            help_page.chooseAcc(account)
        else:
            poco("com.google.android.gms:id/add_account_chip_title").click()
            registration_page.sign_In_With_Google("Zebra#123456789", account)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Google Drive / OneDrive explorer is opened
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check there is no file listed and "No documents" shown
        start_time = time.time()

        data_sources_page.checkDriveEmpty()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Check the Select button is disabled
        start_time = time.time()

        raise Exception("There is no select button to verify it is disabled.")
        """Cannot automate - Check the Select button is disabled. as select button not displayed"""
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Repeat for OneDrive
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
        data_sources_page.clickMicrosoftOneDrive()
        if data_sources_page.verifySignInWithMicrosoft():
            data_sources_page.signInWithMicrosoft(account, "Zebra#123456789")
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
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


"""zebraloginzsb@gmail"""


def test_DataSources_TestcaseID_47937():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Launch ZSB Series App.'],
        2: [2, 'Click "Sign In/Register" button.'],
        3: [3, 'Check user is navigated to "Login with username" page.'],
        4: [4,
            'Enter login name (E.g MW12345) with correct password and click Sign in button. This time sign in with Zebra account.'],
        5: [5, 'Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page.'],
        6: [6, 'Go to My Data page'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'Cloud Service Sign in page will open and let user select which service to login'],
        9: [9, 'Click Sign in with Microsoft'],
        10: [10, 'Select two or three supported files to upload'],
        11: [11, 'Check File is linked without issue'],
        12: [12, 'Select the file linked from OneDrive and Remove'],
        13: [13, 'Check the linked file removed from My Data page'],
        14: [14, 'Repeat step 7 to step 13 but to link Google Drive file'],
        15: [15, 'Click on the hamburger icon follow by Settings and click Log out button'],
        16: [16,
             'Check user is successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Launch ZSB Series App.
        start_time = time.time()

        data_sources_page.clearAppData()
        # data_sources_page.clearBrowsingData()
        common_method.tearDown()
        data_sources_page.allowPermissions()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click "Sign In/Register" button.
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

        # Step 4: Enter login name (E.g MW12345) with correct password and click Sign in button. This time sign in with Zebra account.
        start_time = time.time()

        registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0, False)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Check user is successfully login to Money Badger Home Page and is navigated to Overview landing page.
        start_time = time.time()

        data_sources_page.checkIfOnHomePage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Go to My Data page
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Click + button at bottom and select Link File
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

        # Step 8: Cloud Service Sign in page will open and let user select which service to login
        start_time = time.time()

        """ One drive """
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click Sign in with Microsoft
        start_time = time.time()

        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Select two or three supported files to upload
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
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
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check File is linked without issue
        start_time = time.time()

        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Select the file linked from OneDrive and Remove
        start_time = time.time()

        data_sources_page.remove_File_Based_On_DataSource("OneDrive", csv_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Check the linked file removed from My Data page
        start_time = time.time()

        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        data_sources_page.checkFileRemovedSuccessfully(csv_file, "OneDrive")
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Repeat step 7 to step 13 but to link Google Drive file
        start_time = time.time()

        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(5)
        if data_sources_page.verifySignInWithGoogle():
            registration_page.click_Google_Icon()
        account = "zebra03.swdvt@gmail.com"
        if data_sources_page.checkIfAccPresentLink(account):
            help_page.chooseAcc(account)
        else:
            poco("com.google.android.gms:id/add_account_chip_title").click()
            registration_page.sign_In_With_Google("Zebra#123456789", account)
            sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(5)
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
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
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", csv_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        data_sources_page.checkFileRemovedSuccessfully(csv_file, "Google Drive")
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        data_sources_page.searchName("")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 15: Click on the hamburger icon follow by Settings and click Log out button
        start_time = time.time()

        """Non-Zebra login"""
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        registration_page.scroll_till_log_out()
        registration_page.click_log_out_button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 16: Check user is successfully log out of Money Badger Home Page and is being navigate to the ZSB Login Page.
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


def test_DataSources_TestcaseID_45752():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Cloud Service Sign in page will open and let user select which service to login'],
        4: [4, 'Click Sign in with Microsoft account'],
        5: [5, 'After signed in Microsoft account, check supported files are listed in One Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Mobile app return to My Data page'],
        8: [8, 'Check no file is uploaded'],
        9: [9, 'Click + button at bottom and select Link File'],
        10: [10, 'Click Microsoft One Drive'],
        11: [11, 'Select any of the supported file types to link'],
        12: [12, 'Check the selected file is linked'],
        13: [13, 'Check the file icon, file name, Date added and Data source field are correct'],
        14: [14, 'Repeat for other 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Zebra account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.tearDown()
        try:
            registration_page.wait_for_element_appearance("Home", 20)
        except:
            raise Exception("home page dint show up")
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open and let user select which service to login
        start_time = time.time()

        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Sign in with Microsoft account
        start_time = time.time()

        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Microsoft account, check supported files are listed in One Drive
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
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

        # Step 7: Mobile app return to My Data page
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Check no file is uploaded
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click + button at bottom and select Link File
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

        # Step 10: Click Microsoft One Drive
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Select any of the supported file types to link
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check the selected file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Check the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Repeat for other 2 to 3 supported file types
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
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
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


def test_DataSources_TestcaseID_45730():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select File page will open'],
        4: [4, 'Select Google Drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Check mobile app return back to My Data page and no file is linked'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8,
            'On Google Drive page select file page. Check the Google Drive title is shown completely. Check only supported file types are listed'],
        9: [9, 'Select a file and click Select'],
        10: [10, 'Check mobile app return to My Data page and file is linked'],
        11: [11,
             'Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        12: [12, 'Repeat for another 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

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

        # Step 3: Select File page will open
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select Google Drive
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
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: On Google Drive page select file page. Check the Google Drive title is shown completely. Check only supported file types are listed
        start_time = time.time()

        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)

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

        # Step 10: Check mobile app return to My Data page and file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for another 2 to 3 supported file types
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
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


def test_DataSources_TestcaseID_45749():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'At Cloud service sign in page, click Sign in with Google'],
        4: [4, 'Sign in Google account'],
        5: [5, 'After signed in Google account, check supported files are listed in Google Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Check mobile app return back to My Data page and no file is linked'],
        8: [8, 'Click + button at bottom and select Link File'],
        9: [9, 'Click any supported file and click Select button to link'],
        10: [10, 'Check mobile app return to My Data page and file is linked'],
        11: [11,
             'Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        12: [12, 'Repeat for all supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

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

        # Step 3: At Cloud service sign in page, click Sign in with Google
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Sign in Google account
        start_time = time.time()

        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Google account, check supported files are listed in Google Drive
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

        # Step 7: Check mobile app return back to My Data page and no file is linked
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
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click any supported file and click Select button to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check mobile app return to My Data page and file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for all supported file types
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
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
        data_sources_page.searchName("")
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


"""Facebook"""


def test_DataSources_TestcaseID_45750():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Facebook account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'At Cloud service sign in page, click Sign in with Google'],
        4: [4, 'Sign in Google account'],
        5: [5, 'After signed in Google account, check supported files are listed in Google Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Check mobile app return back to My Data page and no file is linked'],
        8: [8, 'Click + button at bottom and select Link File'],
        9: [9, 'Click any supported file and click Select button to link'],
        10: [10, 'Check mobile app return to My Data page and file is linked'],
        11: [11,
             'Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        12: [12, 'Repeat for all supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Facebook account in Mobile app and go to My Data page
        start_time = time.time()

        """FB login"""
        data_sources_page.clearAppData()
        data_sources_page.clearBrowsingData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        registration_page.wait_for_element_appearance("Sign In", 10)
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        registration_page.login_Facebook("Zebra#123456789", "zebra03.swdvt@gmail.com")
        try:
            registration_page.wait_for_element_appearance("Home", 30)
        except:
            raise Exception("home page dint show up")
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
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: At Cloud service sign in page, click Sign in with Google
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Sign in Google account
        start_time = time.time()

        data_sources_page.signInWithGoogle("zebra06.swdvt@gmail.com", "Zebra#123456789")
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Google account, check supported files are listed in Google Drive
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

        # Step 7: Check mobile app return back to My Data page and no file is linked
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
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click any supported file and click Select button to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check mobile app return to My Data page and file is linked
        start_time = time.time()

        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 11: Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct
        start_time = time.time()

        data_sources_page.searchName(png_file)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat for all supported file types
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
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        """Remove Files for next execution"""
        data_sources_page.searchName("")
        data_sources_page.searchName(png_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", png_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(jpg_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", jpg_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", bmp_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        data_sources_page.remove_File_Based_On_DataSource("Google Drive", csv_file)
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


def test_DataSources_TestcaseID_45753():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Facebook account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Cloud Service Sign in page will open and let user select which service to login'],
        4: [4, 'Click Sign in with Microsoft account'],
        5: [5, 'After signed in Microsoft account, check supported files are listed in One Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Mobile app return to My Data page'],
        8: [8, 'Check no file is uploaded'],
        9: [9, 'Click + button at bottom and select Link File'],
        10: [10, 'Click Microsoft One Drive'],
        11: [11, 'Select any of the supported file types to link'],
        12: [12, 'Check the selected file is linked'],
        13: [13, 'Check the file icon, file name, Date added and Data source field are correct'],
        14: [14, 'Repeat for other 2 to 3 supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Cloud Service Sign in page will open and let user select which service to login
        start_time = time.time()

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Click Sign in with Microsoft account
        start_time = time.time()

        """ One drive """
        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: After signed in Microsoft account, check supported files are listed in One Drive
        start_time = time.time()

        common_method.wait_for_element_appearance("NAME")
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

        # Step 7: Mobile app return to My Data page
        start_time = time.time()

        sleep(4)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Check no file is uploaded
        start_time = time.time()

        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click + button at bottom and select Link File
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

        # Step 10: Click Microsoft One Drive
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

        # Step 11: Select any of the supported file types to link
        start_time = time.time()

        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Check the selected file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Check the file icon, file name, Date added and Data source field are correct
        start_time = time.time()

        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Repeat for other 2 to 3 supported file types
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
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
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
        txt_file = "text_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
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
        data_sources_page.searchName(txt_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", txt_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(bmp_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
        data_sources_page.searchName("")
        data_sources_page.searchName(csv_file)
        data_sources_page.remove_File_Based_On_DataSource("OneDrive", csv_file)
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
