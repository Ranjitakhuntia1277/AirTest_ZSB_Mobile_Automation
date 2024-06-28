from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

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

def test_DataSources_TestcaseID_45729():
    pass

    """Google Login"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra03.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    """Google Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    """ google drive """
    registration_page.click_Google_Icon()
    help_page.chooseAcc("zebra03.swdvt@gmail.com")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    common_method.wait_for_element_appearance("NAME")
    sleep(5)
    """Select file with special characters"""
    special_char_file = "A_!@#$%^^&(().xlsx"
    data_sources_page.selectFileDrive(special_char_file)
    sleep(5)
    data_sources_page.searchName(special_char_file)
    data_sources_page.verify_File_Data(special_char_file, "Google Drive")
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
    common_method.Stop_The_App()


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
    """test"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.click_My_Data()
    sleep(3)
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    """Test for Google Drive"""
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    common_method.wait_for_element_appearance_namematches("NAME", 20)
    sleep(2)
    """Cannot select unsupported file"""
    data_sources_page.checkFilesShownAreSupported()
    sleep(2)
    large_file = "large_unsupported_file(50mb).png"
    data_sources_page.selectFileDrive(large_file)
    """No prompt message on uploading file greater than 28.4mb"""
    sleep(5)
    data_sources_page.click_Add_File()
    sleep(2)
    data_sources_page.click_Link_File()
    sleep(3)
    """Re upload same file"""
    data_sources_page.select_file_link_drive(large_file)
    sleep(5)
    data_sources_page.checkIsAlreadyLinkedPopUp()
    """Remove for next execution"""
    data_sources_page.searchName(large_file)
    data_sources_page.remove_File_Based_On_DataSource("Google Drive", large_file)
    data_sources_page.searchName("")
    sleep(2)
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
    data_sources_page.select_file_link_drive(large_file)
    sleep(5)
    sleep(7)
    data_sources_page.click_Add_File()
    sleep(2)
    data_sources_page.click_Link_File()
    sleep(3)
    data_sources_page.clickMicrosoftOneDrive()
    sleep(2)
    """Re upload the same file"""
    data_sources_page.select_file_link_drive(large_file)
    sleep(5)
    data_sources_page.checkIsAlreadyLinkedPopUp()
    """Remove files for next execution"""
    data_sources_page.searchName(large_file)
    data_sources_page.remove_File_Based_On_DataSource("OneDrive", large_file)
    data_sources_page.searchName("")
    sleep(2)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45735():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
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
    sleep(2)
    """ One drive """
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    common_method.wait_for_element_appearance("NAME")
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
    """ One drive """
    data_sources_page.clickMicrosoftOneDrive()
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


def test_DataSources_TestcaseID_45736():
    pass
    common_method.tearDown()
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
    """Google Drive"""
    data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file, True, True)
    data_sources_page.searchName("")
    data_sources_page.searchName(txt_file)
    try:
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
    except:
        raise Exception("File removed even after clicking cancel")
    sleep(2)
    data_sources_page.remove_File_Based_On_DataSource("Google Drive", txt_file)
    data_sources_page.searchName("")
    data_sources_page.searchName(txt_file)
    try:
        data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("File not removed")
    except Exception as e:
        pass
    """One Drive"""
    data_sources_page.searchName("")
    data_sources_page.searchName(png_file)
    data_sources_page.remove_File_Based_On_DataSource("OneDrive", None, True, True)
    data_sources_page.searchName("")
    data_sources_page.searchName(png_file)
    try:
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
    except:
        raise Exception("File not removed")
    sleep(2)
    data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
    data_sources_page.searchName("")
    data_sources_page.searchName(png_file)
    try:
        data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
        raise Exception("File not removed")
    except:
        pass
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45737():
    pass

    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra02.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    sleep(2)
    removed_file_name = "45737_original.xlsx"
    data_sources_page.searchName(removed_file_name)
    data_sources_page.remove_File_Based_On_DataSource("Google Drive", removed_file_name, False, True)
    sleep(3)
    data_sources_page.searchName("")
    data_sources_page.searchName(removed_file_name)
    try:
        data_sources_page.verifyFilePresentInList(removed_file_name, "Google Drive", True)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("File not removed")
    except Exception as e:
        pass
    sleep(2)
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
    template_management_page.selectChooseAnOption(1, "45737_replacement.xlsx (Google Drive)")
    data_sources_page.clickContinue()
    template_management_page.selectChooseAnOption(1)
    data_sources_page.clickContinue()
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    """Cannot automate - navigate to check different preview images are correct-has to be verified manually"""
    count=5
    while not poco("Print").exists() and count!=0:
        poco.scroll()
        count-=1
    data_sources_page.labelRangeSelection(4)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
    """Cannot automate - navigate to check that only the select rows can be previewed-has to be verified manually"""
    template_management_page.verify_label_navigation()
    count=5
    while not poco("Print").exists() and count!=0:
        poco.scroll()
        count-=1
    if template_management_page.get_total_labels_printing() == "4":
        pass
    else:
        raise Exception("The total number is not the same as your selected row amount")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    sleep(3)
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
    count=5
    while not poco("Print").exists() and count!=0:
        poco.scroll()
        count-=1
    data_sources_page.labelRangeSelection(4)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
    """Cannot automate - navigate to check that only the select rows can be previewed-has to be verified manually"""
    template_management_page.verify_label_navigation()
    count=5
    while not poco("Print").exists() and count!=0:
        poco.scroll()
        count-=1
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


def test_DataSources_TestcaseID_45739():
    pass

    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload File"""
    data_sources_page.click_Upload_File()
    sleep(3)
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


def test_DataSources_TestcaseID_45744():
    pass

    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
    """Click Add File"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(5)
    """Select File to upload"""
    file_name = data_sources_page.select_File_To_Upload(True)
    sleep(5)
    """Upload the same file again"""
    """Click Add File"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(5)
    data_sources_page.select_File_To_Upload()
    sleep(5)
    search_name = file_name.split(".")[0]
    extension = file_name.split(".")[1]
    data_sources_page.searchName(search_name)
    file_list = data_sources_page.fileListDisplayed()
    if (search_name + "." + extension in file_list) and (search_name + " (1)" + "." + extension in file_list):
        pass
    else:
        raise Exception("Re-uploading not appended '(1)' to file name")
    drive_file = "drive_file.jpg"
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    common_method.wait_for_element_appearance_namematches("NAME", 20)
    sleep(2)
    data_sources_page.selectFileDrive(drive_file)
    sleep(5)
    data_sources_page.verifyFilePresentInList(drive_file, "Google Drive", True)
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(5)
    data_sources_page.searchFileInLocalStorage(drive_file)
    sleep(7)
    data_sources_page.searchName(drive_file)
    data_sources_page.verifyFilePresentInList(drive_file, "Local File", True)
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


def test_DataSources_TestcaseID_45740():
    """""""""test"""""

    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload File"""
    data_sources_page.click_Upload_File()
    sleep(3)
    data_sources_page.searchFileInLocalStorage("20 Files", "Downloads")
    sleep(2)
    uploaded_file_list = data_sources_page.selectFilesInLocal()
    """No notification after uploading file"""
    keyevent("back")
    keyevent("back")
    for name in uploaded_file_list:
        data_sources_page.searchName(name)
        sleep(7)
        data_sources_page.verifyFilePresentInList(name, "Local File", True)
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


def test_DataSources_TestcaseID_45741():
    pass

    common_method.tearDown()
    """setup - Upload a file from local to execute"""

    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
    """Select Very large File to upload"""
    selected_file_name = data_sources_page.selectFileInLocalStorage()
    sleep(10)
    data_sources_page.searchName(selected_file_name)
    data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name, True)
    file_list = data_sources_page.fileListDisplayed()
    if len(file_list) >= 1:
        pass
    else:
        raise Exception("File list empty")
    data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file_name)
    data_sources_page.searchName("")
    data_sources_page.searchName(selected_file_name)
    try:
        data_sources_page.verifyFilePresentInList(selected_file_name, "Local File", True)
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("File present even after removing it.")
    except Exception as e:
        pass
    selected_file_name = "png_file.png"
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


def test_DataSources_TestcaseID_45742():
    pass

    """Click hamburger icon to expand menu"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    sleep(5)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(5)
    remove_file_name = "ferry.xlsx"
    data_sources_page.searchName(remove_file_name)
    data_sources_page.remove_File_Based_On_DataSource("Local File", remove_file_name, True)
    file_list = data_sources_page.fileListDisplayed()
    if len(file_list) >= 1:
        pass
    else:
        raise Exception("File list empty")
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
    """Select Very large File to upload"""
    data_sources_page.searchFileInLocalStorage(remove_file_name, "Downloads")
    sleep(10)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45743():
    pass

    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
    """Click Add File"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(5)
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


def test_DataSources_TestcaseID_45745():
    """""""""test"""""

    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
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


def test_DataSources_TestcaseID_45746():
    pass

    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
    long_name_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
    """Select File to upload"""
    data_sources_page.searchFileInLocalStorage(long_name_file, "Downloads")
    sleep(7)
    data_sources_page.searchName(long_name_file)
    """Verify If File Uploaded Successfully"""
    data_sources_page.verifyFilePresentInList(long_name_file)
    """Remove file for next execution"""
    data_sources_page.remove_File_Based_On_DataSource("Local File", long_name_file)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45747():
    pass
    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Data"""
    data_sources_page.click_My_Data()
    """Large file"""
    large_file = "large_unsupported_file(50mb).png"
    """Click Add File"""
    sleep(2)
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
    """Select Very large File to upload"""
    data_sources_page.searchFileInLocalStorage(large_file, "Downloads")
    sleep(20)
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
    """28.3mb file"""
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
    """Select File of size 28.3mb to upload"""
    data_sources_page.searchFileInLocalStorage("28.3M.png", "Downloads")
    sleep(5)
    data_sources_page.searchName("28.3M.png")
    data_sources_page.verifyFilePresentInList("28.3M.png", "Local File", True)
    sleep(5)
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    sleep(2)
    data_sources_page.click_Upload_File()
    """Select File of size 28.4 to upload"""
    data_sources_page.searchFileInLocalStorage("29.4M.png", "Downloads")
    sleep(5)
    data_sources_page.searchName("29.4m.png")
    data_sources_page.verifyFilePresentInList("29.4m.png", "Local File", True)
    """Remove uploaded files for next execution"""
    data_sources_page.remove_File_Based_On_DataSource("Local File", "29.4m.png")
    data_sources_page.searchName("28.3M.png")
    data_sources_page.remove_File_Based_On_DataSource("Local File", "28.3M.png")
    data_sources_page.searchName(large_file)
    data_sources_page.remove_File_Based_On_DataSource("Local File", large_file)
    common_method.tearDown()


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
    """One Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    sleep(2)
    """ One drive """
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    common_method.wait_for_element_appearance("NAME")
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
    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Designs in menu"""
    data_sources_page.clickMyDesigns()
    sleep(2)
    """Choose the design created at setup"""
    data_sources_page.searchMyDesigns("45757")
    sleep(3)
    data_sources_page.selectDesignCreatedAtSetUp()
    sleep(3)
    """Click the print option"""
    data_sources_page.clickPrint()
    sleep(5)
    """Verify if there is option to choose picture"""
    data_sources_page.verifyPhotoOptions()
    poco.scroll()
    """Expand to see different options to choose picture"""
    data_sources_page.expandPhotoOptions()
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
    while not poco("Print", enabled=True).exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45759():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    sleep(2)
    """ google drive """
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    sleep(2)
    existing_file = data_sources_page.selectExistingFile()
    sleep(5)
    data_sources_page.searchName(existing_file)
    data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True)
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


def test_DataSources_TestcaseID_47830():
    pass
    """Click hamburger icon to expand menu"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Designs in menu"""
    data_sources_page.clickMyDesigns()
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
    stop_app("com.android.chrome")
    sleep(2)
    """No pull down to refresh option due to bug SMBM-1710"""
    data_sources_page.searchMyDesigns(label_name)
    try:
        common_method.wait_for_element_appearance_namematches(
            "There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.")
    except:
        raise Exception("New Design created in web is present without the need to refresh.")
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Data in menu"""
    data_sources_page.click_My_Data()
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
    """No pull down to refresh option due to bug SMBM-1710"""
    sleep(5)
    data_sources_page.searchName(selected_file_name)
    try:
        common_method.wait_for_element_appearance_namematches("List is empty")
    except:
        raise Exception("New File updated in web is present without the need to refresh.")
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_47936():
    pass
    common_method.tearDown()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    """Click Add File"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(2)
    """Select File to upload"""
    selected_file = "Demo.jpg"
    data_sources_page.searchFileInLocalStorage(selected_file)
    sleep(5)
    """Notification on file upload"""
    """Unable to verify due to BUG SMBM-712"""
    print(selected_file)
    data_sources_page.searchName(selected_file)
    data_sources_page.remove_File()
    """Notification on file removal"""
    """Unable to verify due to BUG SMBM-712"""
    raise Exception("No notification on uploading and removing file")
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_47942():
    """""""""test"""""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    sleep(5)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(5)
    """Click Add File"""
    data_sources_page.click_Add_File()
    sleep(5)
    """Click Upload file"""
    data_sources_page.click_Upload_File()
    sleep(5)
    """Select File to upload"""
    selected_file = "Demo.jpg"
    data_sources_page.searchFileInLocalStorage(selected_file)
    sleep(5)
    """Verify Progress Indicator"""
    data_sources_page.verifyProgressIndicator()
    """Verify if file uploaded successfully"""
    data_sources_page.searchName(selected_file)
    data_sources_page.verifyFilePresentInList(selected_file)
    """remove file for next execution"""
    data_sources_page.searchName(selected_file)
    data_sources_page.remove_File_Based_On_DataSource("Local File", selected_file)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_47944():
    """""""test"""

    """Click hamburger icon to expand menu"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(2)
    data_sources_page.click_Add_File()
    sleep(2)
    data_sources_page.click_Upload_File()
    template_management_page.wait_for_appearance_enabled("Show roots")
    """select 4-BMP.BMP"""
    data_sources_page.searchFileInLocalStorage("4-BMP.BMP", "Downloads")
    sleep(5)
    """Step 5 pending as no error pop up"""
    data_sources_page.searchName("4-BMP.BMP")
    """check list empty"""
    data_sources_page.checkIfListIsEmpty()
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45758():
    """""""""test"""""

    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra02.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
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
    account = "zebratest850@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("Zebra#123456789", account)
    sleep(2)
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    sleep(2)
    data_sources_page.checkDriveEmpty()
    """Cannot automate - Check the Select button is disabled. as select button not displayed"""
    data_sources_page.clickBackArrow()

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


"""zebraloginzsb@gmail"""


def test_DataSources_TestcaseID_47937():
    pass

    data_sources_page.clearAppData()
    # data_sources_page.clearBrowsingData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0, False)
    try:
        registration_page.wait_for_element_appearance_text("Continue", 30)
        data_sources_page.clickContinueWeb()
    except:
        pass
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.click_My_Data()
    sleep(5)
    """One Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    """ One drive """
    sleep(2)
    data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
    sleep(2)
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
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
    """Non-Zebra login"""
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    while not poco("Log Out").exists():
        poco.scroll()
    registration_page.click_log_out_button()
    """Login pending"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebra06.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        count = 5
        while not poco(text="Use another account").exists() and count!=0:
            poco.scroll()
            count-=1
        login_page.click_GooglemailId()
        if poco(text="Signed in to Google as").exists():
            count = 5
            while not poco(text="Add account to device").exists() and count!=0:
                poco.scroll()
                count-=1
            registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", "zebra06.swdvt@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.click_My_Data()
    sleep(5)
    """One Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    """ One drive """
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    common_method.wait_for_element_appearance("NAME")
    sleep(5)
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
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
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
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45752():
    """test"""

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
    """One Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    sleep(2)
    """ One drive """
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    common_method.wait_for_element_appearance("NAME")
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


def test_DataSources_TestcaseID_45730():
    """""""""test"""""

    common_method.tearDown()
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
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
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
    sleep(2)
    """ google drive """
    data_sources_page.clickGoogleDrive()
    sleep(5)
    png_file = "png_file.png"
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


def test_DataSources_TestcaseID_45749():
    pass

    common_method.tearDown()
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
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
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    sleep(2)
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
    sleep(2)
    """ google drive """
    data_sources_page.clickGoogleDrive()
    sleep(5)
    png_file = "png_file.png"
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


"""Facebook"""


def test_DataSources_TestcaseID_45750():
    pass
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
    """Google Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    sleep(2)
    data_sources_page.signInWithGoogle("zebra06.swdvt@gmail.com", "Zebra#123456789")
    sleep(5)
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
    common_method.wait_for_element_appearance_namematches("NAME", 20)
    sleep(2)
    """ google drive """
    data_sources_page.clickGoogleDrive()
    sleep(5)
    png_file = "png_file.png"
    data_sources_page.selectFileDrive(png_file)
    sleep(5)
    data_sources_page.searchName(png_file)
    data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
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


def test_DataSources_TestcaseID_45753():
    pass
    """FB login"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
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
    sleep(2)
    """ One drive """
    data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    common_method.wait_for_element_appearance("NAME")
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
    common_method.wait_for_element_appearance("NAME")
    sleep(5)
    png_file = "png_file.png"
    data_sources_page.selectFileDrive(png_file)
    # sleep(5)
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

# ####"""""""""""""""""""""""""""""""END"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45878():
    """	Verify sign in as zebra, check link and delete one/google drive file works well"""

    common_method.tearDown()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    login_page.click_Menu_HamburgerICN()
    smoke_test_android.click_MyData_Tab()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_LinkFile()
    smoke_test_android.click_Microsoft_OneDrive_Tab()
    smoke_test_android.click_SignIn_With_Microsoft()
    smoke_test_android.click_Email_Text_Field()
    smoke_test_android.click_Next_Button()
    smoke_test_android.click_Microsoft_Password_Field()
    smoke_test_android.click_Sign_In_Button()
    smoke_test_android.click_Microsoft_OneDrive_Tab()
    smoke_test_android.click_Microsoft_Email_Field()
    smoke_test_android.click_Next_Button()
    smoke_test_android.click_On_Microsoft_Password_Textfield()
    smoke_test_android.click_SignIn_Button()
    smoke_test_android.click_Microsoft_OneDrive_Tab()
    smoke_test_android.click_On_Jpg_File()
    smoke_test_android.click_On_Select_Btn()
    app_settings_page.Scroll_Till_Next_Tab()
    smoke_test_android.click_Three_Dot_On_MyData()
    smoke_test_android.Click_Delete_File()
    smoke_test_android.Click_Delete_File()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Logout_Btn()
    common_method.Stop_The_App()
# #     ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #
def test_Smoke_Test_TestcaseID_45879():
    """Verify sign in as non-zebra, check link and delete one/google drive file works well"""


    common_method.tearDown()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    login_page.click_Menu_HamburgerICN()
    smoke_test_android.click_MyData_Tab()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_Upload_icon()
    smoke_test_android.Upload_First_Image()
    smoke_test_android.click_Plus_icon()
    smoke_test_android.click_LinkFile()
    smoke_test_android.click_SignIn_With_Google_Drive()
    login_page.Loginwith_Added_Email_Id()
    smoke_test_android.click_Google_Drive_Password_Field()
    smoke_test_android.click_Sign_In_Button()
    smoke_test_android.click_On_PNG_File()
    smoke_test_android.click_On_Select_Btn()
    app_settings_page.Scroll_Till_Next_Tab()
    smoke_test_android.click_Three_Dot_On_MyData()
    smoke_test_android.Click_Delete_File()
    smoke_test_android.Click_Delete_File()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Logout_Btn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
#
# #     ## """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

