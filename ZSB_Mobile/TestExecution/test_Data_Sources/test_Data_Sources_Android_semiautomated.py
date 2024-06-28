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
    common_method.Start_The_App()
    try:
        common_method.wait_for_element_appearance("Sign In", 20)
    except:
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        registration_page.wait_for_element_appearance("Sign In", 10)
    """Google Login"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebraidctest@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
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
    initial_file_count = len(data_sources_page.fileListDisplayed())
    """Google Drive"""
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    """Google Drive"""
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
    registration_page.wait_for_element_appearance("Sign In", 10)

    """Apple Login"""

    common_method.Start_The_App()
    registration_page.wait_for_element_appearance("Sign In", 10)
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    username = "zsbswdvt@gmail.com"
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", username)
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
    """ google drive """
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
    registration_page.wait_for_element_appearance("Sign In", 10)

    """Facebook Login"""

    registration_page.wait_for_element_appearance("Sign In", 10)
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
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
    """ google drive """
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
    registration_page.wait_for_element_appearance("Sign In", 10)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45732():
    """""""""test"""""

    """Google Login"""
    common_method.Start_The_App()
    try:
        common_method.wait_for_element_appearance("Sign In", 20)
    except:
        login_page.click_Menu_HamburgerICN()
        registration_page.click_on_profile_edit()
        poco.scroll()
        registration_page.click_log_out_button()
        registration_page.wait_for_element_appearance("Sign In", 10)
    """Google Login"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebraidctest@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
    """Click hamburger icon to expand menu"""
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
    registration_page.wait_for_element_appearance("Sign In", 10)

    """Apple Login"""

    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    """Enter OTP manually"""
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
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
    registration_page.wait_for_element_appearance("Sign In", 10)

    """Facebook Login"""

    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
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
    registration_page.wait_for_element_appearance("Sign In", 10)
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45738():
    """""""""test"""""

    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebraidctest@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
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
    account = "zsbswdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("zsbswdvt@1234", account)
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
    data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    data_sources_page.clickMicrosoftOneDrive()
    data_sources_page.clickBackArrow()
    sleep(3)
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing", 15)
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
    data_sources_page.verifyIfPreviewIsPresent()
    sleep(2)
    sleep(600)
    """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
    data_sources_page.clickBackArrow()
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
    while not poco("Print").exists():
        poco.scroll()
    """Check the print preview, the data has been  added or removed-has to be done manually"""
    data_sources_page.labelRangeSelection(4)
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
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
    sleep(600)
    """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
    data_sources_page.clickBackArrow()
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
    while not poco("Print").exists():
        poco.scroll()
    """Check the print preview, the data has been  added or removed-has to be done manually"""
    data_sources_page.labelRangeSelection(4)
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_DataSources_TestcaseID_45751():
    """Test"""

    """apple login"""
    data_sources_page.clearAppData()
    data_sources_page.clearBrowsingData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.wait_for_element_appearance("Sign In", 10)
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    """Enter OTP manually"""
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
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
    data_sources_page.signInWithGoogle("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
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
    sleep(5)
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
    sleep(5)
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
    sleep(5)
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


def test_DataSources_TestcaseID_45754():
    """Test"""

    """apple login"""
    data_sources_page.clearAppData()
    data_sources_page.clearBrowsingData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.wait_for_element_appearance("Sign In", 10)
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    """Enter OTP manually"""
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
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
    sleep(2)
    """ One drive """
    data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
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
    common_method.Stop_The_App()