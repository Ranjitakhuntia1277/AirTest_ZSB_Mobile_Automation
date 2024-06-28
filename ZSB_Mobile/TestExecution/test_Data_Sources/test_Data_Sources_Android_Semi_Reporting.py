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


def test_DataSources_TestcaseID_45731():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Facebook account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select File page will open'],
        4: [4, 'Select Google drive'],
        5: [5, 'Click Back button'],
        6: [6, 'Check mobile app return back to My Data page and no file is linked'],
        7: [7, 'Click + button at bottom and select Link File'],
        8: [8, 'On Google Drive page, check only supported file types are listed'],
        9: [9, 'Select a file and click Select'],
        10: [10, 'Check mobile app return to My Data page and file is linked'],
        11: [11,
             'Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        12: [12, 'Repeat for another 2 to 3 supported file types'],
        13: [13, 'Repeat this test case, at step 1 login as Apple account user'],
        14: [14, 'Repeat this test case, at step 1 login as Google account user']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Facebook account in Mobile app and go to My Data page
        start_time = time.time()

        common_method.Start_The_App()
        try:
            common_method.wait_for_element_appearance("Sign In", 20)
        except:
            login_page.click_Menu_HamburgerICN()
            registration_page.click_on_profile_edit()
            poco.scroll()
            registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()
        """Facebook Login"""
        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        registration_page.login_Facebook("Zebra#123456789", "zebra03.swdvt@gmail.com")
        """Click hamburger icon to expand menu"""
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

        """Google Drive"""
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select Google drive
        start_time = time.time()

        common_method.wait_for_element_appearance_namematches("NAME", 20)
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

        # Step 8: On Google Drive page, check only supported file types are listed
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
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
        sleep(5)

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
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
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
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Repeat this test case, at step 1 login as Apple account user
        start_time = time.time()

        """Apple Login"""

        common_method.Start_The_App()
        data_sources_page.checkIfInLoginPage()
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        username = "zebra03.swdvt@gmail.com"
        registration_page.login_Apple("Zebra#123456789", username)
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ google drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(3)
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)
        data_sources_page.clickBackArrow()
        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)
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
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
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
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
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
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 14: Repeat this test case, at step 1 login as Google account user
        start_time = time.time()

        """Google Login"""
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
            while not poco(text="Use another account").exists():
                poco.scroll()
            login_page.click_GooglemailId()
            while not poco(text="Add account to device").exists():
                poco.scroll()
            registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra03.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ google drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(3)
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)
        data_sources_page.clickBackArrow()
        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)
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
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
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
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
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
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
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


def test_DataSources_TestcaseID_45732():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Google account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'Select File page will open and click Microsoft tap. Check only supported files are listed'],
        4: [4, 'Click Back button'],
        5: [5, 'Check mobile app return back to My Data page and no file is linked'],
        6: [6, 'Click + button at bottom and select Link File'],
        7: [7, 'Select Microsoft tap'],
        8: [8, 'Select a file and click Select'],
        9: [9, 'Check mobile app return to My Data page and file is linked'],
        10: [10, 'Check the details of file icon, file name, Date added and Data source field are correct'],
        11: [11, 'Repeat for another 2 to 3 supported file types'],
        12: [12, 'Repeat this test case, at step 1 login as Facebook account user'],
        13: [13, 'Repeat this test case, at step 1 login as Apple account user']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Google account in Mobile app and go to My Data page
        start_time = time.time()

        """Google Login"""
        common_method.Start_The_App()
        try:
            common_method.wait_for_element_appearance("Sign In", 20)
        except:
            login_page.click_Menu_HamburgerICN()
            registration_page.click_on_profile_edit()
            poco.scroll()
            registration_page.click_log_out_button()
            data_sources_page.checkIfInLoginPage()
        """Google Login"""
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
            while not poco(text="Use another account").exists():
                poco.scroll()
            login_page.click_GooglemailId()
            while not poco(text="Add account to device").exists():
                poco.scroll()
            registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
        """Click hamburger icon to expand menu"""
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select File page will open and click Microsoft tap. Check only supported files are listed
        start_time = time.time()

        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        data_sources_page.checkFilesShownAreSupported()
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Select Microsoft tap
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
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

        # Step 9: Check mobile app return to My Data page and file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check the details of file icon, file name, Date added and Data source field are correct
        start_time = time.time()

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
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 12: Repeat this test case, at step 1 login as Facebook account user
        start_time = time.time()

        """Facebook Login"""

        registration_page.clickSignIn()
        registration_page.click_Facebook_Icon()
        registration_page.login_Facebook("Zebra#123456789", "zebra03.swdvt@gmail.com")
        try:
            registration_page.wait_for_element_appearance("Home", 30)
        except:
            raise Exception("home page dint show up")
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)
        data_sources_page.clickBackArrow()
        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        data_sources_page.checkIfInLoginPage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 13: Repeat this test case, at step 1 login as Apple account user
        start_time = time.time()

        """Apple Login"""

        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        """Enter OTP manually"""
        registration_page.login_Apple("Zebra#123456789", "zebra03.swdvt@gmail.com")
        try:
            registration_page.wait_for_element_appearance("Home", 30)
        except:
            raise Exception("home page dint show up")
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.click_My_Data()
        sleep(5)
        initial_file_count = len(data_sources_page.fileListDisplayed())
        """One Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        """ One drive """
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        data_sources_page.checkFilesShownAreSupported()
        sleep(3)
        data_sources_page.clickBackArrow()
        """Check no file linked"""
        data_sources_page.checkNoChangeInFileCount(initial_file_count)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        png_file = "png_file.png"
        data_sources_page.selectFileDrive(png_file)
        sleep(5)
        data_sources_page.searchName(png_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
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


def test_DataSources_TestcaseID_45738():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Go to Mobile app -> My Designs page'],
        2: [2, 'Select the label design in precondition and print'],
        3: [3, 'Check the print preview of the label and the data contents are shown correctly'],
        4: [4, 'Close the print preview'],
        5: [5, 'Go to Google Drive and update the file, add or remove the data entry'],
        6: [6, 'After update, print the same label design again'],
        7: [7, 'Check the print preview, the data has been added or removed'],
        8: [8, 'Select one or several rows to print. Check the printed-out labels are correct'],
        9: [9, 'Repeat this test case for OneDrive']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to Mobile app -> My Designs page
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
            while not poco(text="Use another account").exists():
                poco.scroll()
            login_page.click_GooglemailId()
            while not poco(text="Add account to device").exists():
                poco.scroll()
            registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
        data_sources_page.checkIfOnHomePage()
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        """Click My Data"""
        data_sources_page.click_My_Data()
        sleep(5)
        """Google Drive"""
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        sleep(2)
        """ google drive """
        if data_sources_page.verifySignInWithGoogle():
            registration_page.click_Google_Icon()
        account = "zebra03.swdvt@gmail.com"
        if data_sources_page.checkIfAccPresentLink(account):
            help_page.chooseAcc(account)
        else:
            poco("com.google.android.gms:id/add_account_chip_title").click()
            registration_page.sign_In_With_Google("Zebra#123456789", account)
            sleep(2)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        data_sources_page.clickBackArrow()
        sleep(2)
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
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()
        data_sources_page.clickBackArrow()
        sleep(3)
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        data_sources_page.clickMyDesigns()
        common_method.wait_for_element_appearance_namematches("Showing", 15)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Select the label design in precondition and print
        start_time = time.time()

        """Google Drive"""
        data_sources_page.searchMyDesigns("45738_0")
        common_method.wait_for_element_appearance_namematches("Showing", 15)
        data_sources_page.selectDesignCreatedAtSetUp()
        sleep(2)
        data_sources_page.clickPrint()
        common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
        template_management_page.selectChooseAnOption(1)
        sleep(2)
        data_sources_page.clickContinue()
        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Check the print preview of the label and the data contents are shown correctly
        start_time = time.time()

        data_sources_page.verifyIfPreviewIsPresent()
        sleep(2)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Close the print preview
        start_time = time.time()

        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to Google Drive and update the file, add or remove the data entry
        start_time = time.time()

        """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
        common_method.show_message(
            "Go to Google Drive and update the file, add or remove the data entry.\n Filename = 45738.xlsx account = zebra03.swdvt@gmail.com, password = Zebra#123456789. Keep the app in the same page for continuing execution")

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: After update, print the same label design again
        start_time = time.time()

        common_method.wait_for_element_appearance_namematches("Showing")
        data_sources_page.selectDesignCreatedAtSetUp()
        sleep(2)
        data_sources_page.clickPrint()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Check the print preview, the data has been added or removed
        start_time = time.time()

        common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
        template_management_page.selectChooseAnOption(1)
        sleep(2)
        data_sources_page.clickContinue()
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        """Check the print preview, the data has been  added or removed-has to be done manually"""
        common_method.show_message("Check the print preview, the data has been  added or removed")
        sleep(2)
        data_sources_page.scroll_till_print()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Select one or several rows to print. Check the printed-out labels are correct
        start_time = time.time()

        data_sources_page.labelRangeSelection(4)
        data_sources_page.clickPrint()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        data_sources_page.clickBackArrow()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Repeat this test case for OneDrive
        start_time = time.time()

        """One Drive"""
        common_method.wait_for_element_appearance_namematches("Showing")
        data_sources_page.searchMyDesigns("45738_1")
        common_method.wait_for_element_appearance_namematches("Showing")
        data_sources_page.selectDesignCreatedAtSetUp()
        sleep(2)
        data_sources_page.clickPrint()
        common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
        template_management_page.selectChooseAnOption(1)
        sleep(2)
        data_sources_page.clickContinue()
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        sleep(2)
        data_sources_page.clickBackArrow()
        """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
        common_method.show_message(
            "Go to One Drive and update the file, add or remove the data entry.\n Filename = 45738_1.xlsx account = zebra03.swdvt@gmail.com, password = Zebra#123456789. Keep the app in the same page for continuing execution")
        common_method.wait_for_element_appearance_namematches("Showing")
        data_sources_page.selectDesignCreatedAtSetUp()
        sleep(2)
        data_sources_page.clickPrint()
        common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
        template_management_page.selectChooseAnOption(1)
        sleep(2)
        data_sources_page.clickContinue()
        sleep(10)
        data_sources_page.verifyIfPreviewIsPresent()
        """Check the print preview, the data has been  added or removed-has to be done manually"""
        common_method.show_message("Check the print preview, the data has been  added or removed")
        sleep(2)
        data_sources_page.scroll_till_print()
        data_sources_page.labelRangeSelection(4)
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


def test_DataSources_TestcaseID_45751():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Apple account in Mobile app and go to My Data page'],
        2: [2, 'Click + button at bottom and select Link File'],
        3: [3, 'At Cloud service sign in page, click Sign in with Google'],
        4: [4, 'Sign in with Google account'],
        5: [5, 'After signed in Google account, check supported files are listed in Google Drive'],
        6: [6, 'Click Back button'],
        7: [7, 'Check mobile app returns back to My Data page and no file is linked'],
        8: [8, 'Click + button at bottom and select Link File'],
        9: [9, 'Click any supported file and click Select button to link'],
        10: [10, 'Check mobile app returns to My Data page and file is linked'],
        11: [11,
             'Check the details of file icon, file name, Date added and Data source field (Google Drive) are correct'],
        12: [12, 'Repeat for all supported file types']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Login Apple account in Mobile app and go to My Data page
        start_time = time.time()

        """apple login"""
        data_sources_page.clearAppData()
        data_sources_page.clearBrowsingData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        data_sources_page.checkIfInLoginPage()
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        """Enter OTP manually"""
        registration_page.login_Apple("Zebra#123456789", "zebra03.swdvt@gmail.com")
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

        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Sign in with Google account
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

        # Step 7: Check mobile app returns back to My Data page and no file is linked
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

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Click any supported file and click Select button to link
        start_time = time.time()

        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
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

        # Step 10: Check mobile app returns to My Data page and file is linked
        start_time = time.time()

        data_sources_page.searchName(png_file)
        sleep(5)

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
        common_method.wait_for_element_appearance_namematches("NAME", 20)
        sleep(2)
        """ google drive """
        data_sources_page.clickGoogleDrive()
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
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
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
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
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
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
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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


def test_DataSources_TestcaseID_45754():
    pass
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Apple account in Mobile app and go to My Data page'],
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
        # Step 1: Login Apple account in Mobile app and go to My Data page
        start_time = time.time()

        """apple login"""
        data_sources_page.clearAppData()
        data_sources_page.clearBrowsingData()
        common_method.tearDown()
        data_sources_page.allowPermissions()
        data_sources_page.checkIfInLoginPage()
        registration_page.clickSignIn()
        registration_page.click_Apple_Icon()
        """Enter OTP manually"""
        registration_page.login_Apple("Zebra#123456789", "zebra03.swdvt@gmail.com")
        try:
            registration_page.wait_for_element_appearance("Home", 30)
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
        """ One drive """

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

        data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        data_sources_page.clickMicrosoftOneDrive()

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
        sleep(5)

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
        sleep(5)
        jpg_file = "jpg_file.jpg"
        data_sources_page.selectFileDrive(jpg_file)
        sleep(5)
        data_sources_page.searchName(jpg_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        csv_file = "csv_file.csv"
        data_sources_page.selectFileDrive(csv_file)
        sleep(5)
        data_sources_page.searchName(csv_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        txt_file = "txt_file.txt"
        data_sources_page.selectFileDrive(txt_file)
        sleep(5)
        data_sources_page.searchName(txt_file)
        sleep(5)
        data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
        """Click Add file"""
        data_sources_page.click_Add_File()
        sleep(2)
        """Click Link File"""
        data_sources_page.click_Link_File()
        template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
        """ One drive """
        data_sources_page.clickMicrosoftOneDrive()
        sleep(5)
        bmp_file = "bmp_file.bmp"
        data_sources_page.selectFileDrive(bmp_file)
        sleep(5)
        data_sources_page.searchName(bmp_file)
        sleep(5)
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
