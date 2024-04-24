from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others


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


# def test_DataSources_TestcaseID_45729():
#     pass
#
#
# """Google Login"""
# common_method.Start_The_App()
# registration_page.clickSignIn()
# # login_page.click_loginBtn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zsbswdvt@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zsbswdvt@gmail.com", "zsbswdvt@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ google drive """
# registration_page.click_Google_Icon()
# help_page.chooseAcc("zsbswdvt@gmail.com")
# common_method.wait_for_element_appearance("NAME")
# """Select file with special characters"""
# special_char_file = "A_!@#$%^^&(().xlsx"
# data_sources_page.selectFileDrive(special_char_file)
# sleep(5)
# data_sources_page.searchName(special_char_file)
# data_sources_page.verify_File_Data(special_char_file, "Google Drive")
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """Select long file name"""
# long_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
# data_sources_page.selectFileDrive(long_file)
# sleep(5)
# data_sources_page.searchName(long_file)
# data_sources_page.verify_File_Data(long_file, "Google Drive")
# data_sources_page.searchName("")
# sleep(7)
# """Remove both files"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName(long_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# sleep(7)
# """Check if files removed successfully"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.checkIfListIsEmpty()
# data_sources_page.searchName(long_file)
# data_sources_page.checkIfListIsEmpty()
# """"""""""""""""""""""""""""""""""""""
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """Select file with special characters"""
# data_sources_page.selectFileDrive(special_char_file)
# sleep(5)
# data_sources_page.searchName(special_char_file)
# data_sources_page.verify_File_Data(special_char_file, "OneDrive")
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Select long file name"""
# data_sources_page.selectFileDrive(long_file)
# sleep(5)
# data_sources_page.searchName(long_file)
# data_sources_page.verify_File_Data(long_file, "OneDrive")
# data_sources_page.searchName("")
# sleep(7)
# """Remove both files"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# data_sources_page.searchName(long_file)
# data_sources_page.remove_File()
# data_sources_page.searchName("")
# sleep(7)
# """Check if files removed successfully"""
# data_sources_page.searchName(special_char_file)
# data_sources_page.checkIfListIsEmpty()
# data_sources_page.searchName(long_file)
# data_sources_page.checkIfListIsEmpty()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45730():
    """""""""test"""""


# common_method.Start_The_App()
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("jd4936", "Vl@d#vost0k008", 1, 0, False)
# try:
#     registration_page.wait_for_element_appearance_text("Continue", 30)
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(3)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45731():
    """""""""test"""""


# common_method.Start_The_App()
# try:
#     common_method.wait_for_element_appearance("Sign In", 20)
# except:
#     login_page.click_Menu_HamburgerICN()
#     registration_page.click_on_profile_edit()
#     poco.scroll()
#     registration_page.click_log_out_button()
#     registration_page.wait_for_element_appearance("Sign In", 10)
# """Google Login"""
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """Google Drive"""
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(3)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)

"""Apple Login"""

# common_method.Start_The_App()
# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Apple_Icon()
# """Enter OTP manually"""
# registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ google drive """
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(3)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)

"""Facebook Login"""

# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Facebook_Icon()
# registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ google drive """
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(3)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45732():
    """""""""test"""""


# """Google Login"""
# common_method.Start_The_App()
# try:
#     common_method.wait_for_element_appearance("Sign In", 20)
# except:
#     login_page.click_Menu_HamburgerICN()
#     registration_page.click_on_profile_edit()
#     poco.scroll()
#     registration_page.click_log_out_button()
#     registration_page.wait_for_element_appearance("Sign In", 10)
# """Google Login"""
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ One drive """
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)

"""Apple Login"""

# registration_page.clickSignIn()
# registration_page.click_Apple_Icon()
# """Enter OTP manually"""
# registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ One drive """
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)

"""Facebook Login"""

# registration_page.clickSignIn()
# registration_page.click_Facebook_Icon()
# registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ One drive """
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# poco.scroll()
# registration_page.click_log_out_button()
# registration_page.wait_for_element_appearance("Sign In", 10)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45733():
    """test"""


# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# """Click Add File"""
# data_sources_page.click_Add_File()
# """Click Upload file"""
# data_sources_page.click_Link_File()
# try:
#     common_method.wait_for_element_appearance("NAME", 20)
# except:
#     registration_page.click_Google_Icon()
#     help_page.chooseAcc("zsbswdvt@gmail.com")
#     common_method.wait_for_element_appearance("NAME")
"""searchTest re check"""
# data_sources_page.searchFilesInLinkFiles("test")
# sleep(4)
# data_sources_page.verifyFilePresentInDrive("Test1.jpg")
# data_sources_page.verifyFilePresentInDrive("Test2.png")
# data_sources_page.verifyFilePresentInDrive("Test3.bmp")
# data_sources_page.searchFilesInLinkFiles("test")
# sleep(4)
# data_sources_page.verifyFilePresentInDrive("Test1.jpg")
"""yet to write"""
# a = data_sources_page.getFilesShownInDrive()
# print(a)
# x=1/0
""""""
# data_sources_page.searchTest("test_i", 1)
# data_sources_page.searchTest("test_i", 2)
# data_sources_page.searchTest("test_i", 3)
# data_sources_page.searchTest(".jpg")
# data_sources_page.searchTest(".png")
# data_sources_page.searchTest(".bmp")
# random_word = data_sources_page.generateRandomWord(24)
# data_sources_page.searchTest(random_word)


# def test_DataSources_TestcaseID_45734():
#     """test"""
#
#
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(3)
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """Test for Google Drive"""
# sleep(2)
# if data_sources_page.verifySignInWithGoogle():
#     registration_page.click_Google_Icon()
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """Cannot select unsupported file"""
# data_sources_page.checkFilesShownAreSupported()
# sleep(2)
# large_file = "large_unsupported_file(50mb).png"
# data_sources_page.select_file_link_drive(large_file)
# data_sources_page.clickSelect()
# """No prompt message on uploading file greater than 28.4mb"""
# sleep(5)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# """Re upload same file"""
# data_sources_page.select_file_link_drive(large_file)
# data_sources_page.clickSelect()
# data_sources_page.checkIsAlreadyLinkedPopUp()
# """Test for One Drive"""
# sleep(3)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """ One drive """
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# template_management_page_1.wait_for_element_appearance_name_matches_all("NAME", 20)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.select_file_link_drive(large_file)
# data_sources_page.clickSelect()
# sleep(7)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# """Re upload the same file"""
# data_sources_page.select_file_link_drive(large_file)
# data_sources_page.clickSelect()
# data_sources_page.checkIsAlreadyLinkedPopUp()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45735():
    """test"""


# """Remove if one drive account - zsbswdvt@gmail.com present"""
# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("jd4936", "Vl@d#vost0k008", 1, 0, False)
# try:
#     registration_page.wait_for_element_appearance_text("Continue", 30)
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# """ One drive """
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45736():
#     """""""""test"""""
#
#
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(2)
# """Google Drive"""
# removed_file_name = data_sources_page.remove_File_Based_On_DataSource("Google Drive", None, True, True)
# data_sources_page.searchName(removed_file_name)
# sleep(2)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "Google Drive")
# except:
#     raise Exception("File removed even after clicking cancel")
# sleep(2)
# data_sources_page.remove_File_Based_On_DataSource("Google Drive")
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName(removed_file_name)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "Google Drive")
#     x=1/0
# except ZeroDivisionError:
#     raise Exception("File not removed")
# except Exception as e:
#     pass
# """One Drive"""
# data_sources_page.searchName("")
# sleep(7)
# removed_file_name = data_sources_page.remove_File_Based_On_DataSource("OneDrive", None, True, True)
# data_sources_page.searchName(removed_file_name)
# sleep(2)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "OneDrive")
# except:
#     raise Exception("File not removed")
# sleep(2)
# data_sources_page.remove_File_Based_On_DataSource("OneDrive")
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName(removed_file_name)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "OneDrive")
#     raise Exception("File not removed")
# except:
#     pass
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45737():
    """""""""test"""""


"""Change on mac"""


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# sleep(2)
# removed_file_name = data_sources_page.remove_File_Based_On_DataSource("Google Drive")
# data_sources_page.searchName(removed_file_name)
# sleep(2)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "Google Drive", True)
#     raise Exception("File not removed")
# except:
#     pass
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns("LDA")
# sleep(3)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# data_sources_page.clickBackArrow()
# sleep(2)
# poco(removed_file_name).click()
# sleep(2)
# poco("android.view.View")[6].child()[5].click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# data_sources_page.chooseAnOption1()
# sleep(2)
# poco("android.view.View")[6].child().click()
# sleep(2)
# data_sources_page.clickContinue()
# sleep(2)
# poco.scroll()
# data_sources_page.labelRangeSelection(4)
# data_sources_page.clickPrint()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45738():
    """""""""test"""""


# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# if data_sources_page.verifySignInWithGoogle():
#     registration_page.click_Google_Icon()
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# data_sources_page.clickBackArrow()
# sleep(2)
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(3)
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.clickBackArrow()
# sleep(3)
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing", 15)
# """Google Drive"""
# data_sources_page.searchMyDesigns("45738")
# common_method.wait_for_element_appearance_namematches("Showing", 15)
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
# template_management_page.selectChooseAnOption(1)
# sleep(2)
# data_sources_page.clickContinue()
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# sleep(2)
# """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
# data_sources_page.clickBackArrow()
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
# template_management_page.selectChooseAnOption(1)
# sleep(2)
# data_sources_page.clickContinue()
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# sleep(2)
# while not poco("Print").exists():
#     poco.scroll()
# """Check the print preview, the data has been  added or removed-has to be done manually"""
# data_sources_page.labelRangeSelection(4)
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# """One Drive"""
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.searchMyDesigns("45738_1")
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
# template_management_page.selectChooseAnOption(1)
# sleep(2)
# data_sources_page.clickContinue()
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# sleep(2)
# """Cannot automate - 5. Go to Google Drive and update the file, add or remove the data entry has to be done manually."""
# data_sources_page.clickBackArrow()
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance("Relink Data Source Columns", 20)
# template_management_page.selectChooseAnOption(1)
# sleep(2)
# data_sources_page.clickContinue()
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# sleep(2)
# while not poco("Print").exists():
#     poco.scroll()
# """Check the print preview, the data has been  added or removed-has to be done manually"""
# data_sources_page.labelRangeSelection(4)
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45739():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload File"""
# data_sources_page.click_Upload_File()
# sleep(3)
# data_sources_page.searchFileInLocalStorage("Supported Files", "Downloads")
# sleep(2)
# uploaded_file_list = data_sources_page.selectFilesInLocal()
# """No notification after uploading file"""
# keyevent("back")
# keyevent("back")
# for name in uploaded_file_list:
#     data_sources_page.searchName(name)
#     sleep(7)
#     data_sources_page.verifyFilePresentInList(name, "Local File", True)
"""Login to web portal->Data Sources page Check the uploaded files from mobile app display in the my data page in web portal. pending"""
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45740():
    """""""""test"""""


# """I am here"""
# """Update on mac"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload File"""
# data_sources_page.click_Upload_File()
# sleep(3)
# data_sources_page.searchFileInLocalStorage("20 Files", "Downloads")
# sleep(2)
# file_list_uploaded = data_sources_page.selectFilesInLocal()
# file_list_my_data = data_sources_page.fileListDisplayed()
# for file in file_list_uploaded:
#     if file in file_list_my_data:
#         pass
#     else:
#         error = "File " + file + " not found."
#         raise Exception(error)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45741():
#     pass
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# removed_file_name = data_sources_page.remove_File_Based_On_DataSource("Local File", None, True)
# file_list = data_sources_page.fileListDisplayed()
# if len(file_list) >= 1:
#     pass
# else:
#     raise Exception("File list empty")
# data_sources_page.remove_File_Based_On_DataSource("Local File", removed_file_name)
# sleep(7)
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName(removed_file_name)
# try:
#     data_sources_page.verifyFilePresentInList(removed_file_name, "Local File", True)
#     x=1/0
# except ZeroDivisionError:
#     raise Exception("File present even after removing it.")
# except Exception as e:
#     pass
"""Step -11 cannot automate due to inconsistent web behaviour"""
# # start_app("com.android.chrome")
# # sleep(2)
# # poco("com.android.chrome:id/tab_switcher_button").click()
# # sleep(2)
# # poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# # poco(text="Search or type URL").click()
# # sleep(2)
# # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# # data_sources_page.clickEnter()
# # # data_sources_page.lock_phone()
# # # wake()
# # sleep(3)
# # try:
# #     registration_page.wait_for_element_appearance("Home", 20)
# # except:
# #     if data_sources_page.checkIfElementExists("Continue with Google"):
# #         login_page.click_Loginwith_Google()
# #         sleep(2)
# #         login_page.click_GooglemailId()
# #         sleep(5)
# #         help_page.addAccountToDevice()
# #         sleep(10)
# #         login_page.Enter_Google_UserID("zsbswdvt@gmail.com")
# #         sleep(2)
# #         help_page.clickNext()
# #         sleep(4)
# #         """"To enter password need to use the 2nd method """
# #         help_page.enter_Google_Password("zsbswdvt@1234")
# #         sleep(2)
# #         help_page.clickNext()
# #         sleep(4)
# #         help_page.Agreement_google_login()
# #     else:
# #         raise Exception("ZSB Portal did not open.")
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45742():
#     """""""""test"""""
#
#
#
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# data_sources_page.searchName("ferry.jpg")
# data_sources_page.remove_File_Based_On_DataSource("Local File", "ferry.jpg", True)
# file_list = data_sources_page.fileListDisplayed()
# if len(file_list) >= 1:
#     pass
# else:
#     raise Exception("File list empty")
# data_sources_page.remove_File_Based_On_DataSource("Local File", "ferry.jpg")
# sleep(7)
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName("ferry.jpg")
# try:
#     data_sources_page.verifyFilePresentInList("ferry.jpg", "Local File", True)
#     raise Exception("File present even after removing it.")
# except:
#     pass
"""Step -11 cannot automate due to inconsistent web behaviour"""
# # start_app("com.android.chrome")
# # sleep(2)
# # poco("com.android.chrome:id/tab_switcher_button").click()
# # sleep(2)
# # poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# # poco(text="Search or type URL").click()
# # sleep(2)
# # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# # data_sources_page.clickEnter()
# # # data_sources_page.lock_phone()
# # # wake()
# # sleep(3)
# # try:
# #     registration_page.wait_for_element_appearance("Home", 20)
# # except:
# #     if data_sources_page.checkIfElementExists("Continue with Google"):
# #         login_page.click_Loginwith_Google()
# #         sleep(2)
# #         login_page.click_GooglemailId()
# #         sleep(5)
# #         help_page.addAccountToDevice()
# #         sleep(10)
# #         login_page.Enter_Google_UserID("zsbswdvt@gmail.com")
# #         sleep(2)
# #         help_page.clickNext()
# #         sleep(4)
# #         """"To enter password need to use the 2nd method """
# #         help_page.enter_Google_Password("zsbswdvt@1234")
# #         sleep(2)
# #         help_page.clickNext()
# #         sleep(4)
# #         help_page.Agreement_google_login()
# #     else:
# #         raise Exception("ZSB Portal did not open.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.searchMyDesigns("local_file_linked")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
"""cannot complete step 12, 13 as there is no prompt to user to link or input data manually."""


# data_sources_page.clickPrint()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45743():
    """""""""test"""""


# def test_DataSources_TestcaseID_45744():
#     """""""""test"""""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(3)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# file_name = data_sources_page.select_File_To_Upload(True)
# sleep(5)
# """Upload the same file again"""
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# data_sources_page.select_File_To_Upload()
# sleep(5)
# search_name = file_name.split(".")[1]
# data_sources_page.searchName(search_name)
# file_list = data_sources_page.fileListDisplayed()
# try:
#     if (search_name in file_list) and (search_name + "(1)" in file_list):
#         pass
# except:
#     raise Exception("Re-uploading not appended '(1)' to file name")
# drive_file = "a1.jpg"
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance("NAME")
# data_sources_page.selectFileDrive(drive_file)
# sleep(5)
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# data_sources_page.searchFileInLocalStorage(drive_file)
# data_sources_page.searchName(drive_file)
# data_sources_page.verify_File_Data(drive_file, "Google Drive")
# data_sources_page.verify_File_Data(drive_file, "Google Drive")
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45745():
#     """""""""test"""""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(3)
# """Click Add File"""
# data_sources_page.click_Add_File()
# """Click Upload file"""
# sleep(2)
# data_sources_page.click_Upload_File()
# ignored_char = '&""#%'
# special_char_file1 = "M@xi!mum_#Power%.jpg"
# special_char_file2 = "un$et_{&}_D@zzle.jpg"
# """Select File to upload"""
# data_sources_page.searchFileInLocalStorage(special_char_file1, "Downloads")
# sleep(7)
# for char in ignored_char:
#     special_char_file1 = special_char_file1.replace(char, '')
# data_sources_page.searchName(special_char_file1)
# sleep(7)
# """Verify If File Uploaded Successfully"""
# data_sources_page.verifyFilePresentInList(special_char_file1)
# """Select File to upload"""
# sleep(2)
# data_sources_page.click_Add_File()
# """Click Upload file"""
# sleep(2)
# data_sources_page.click_Upload_File()
# data_sources_page.searchFileInLocalStorage(special_char_file2, "Downloads")
# sleep(7)
# for char in ignored_char:
#     special_char_file2 = special_char_file2.replace(char, '')
# data_sources_page.searchName(special_char_file2)
# sleep(7)
# """Verify If File Uploaded Successfully"""
# data_sources_page.verifyFilePresentInList(special_char_file2)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45746():
    """""""""test"""""


# """""""""click on the login button"""""""""""
# login_page.click_loginBtn()
# sleep(2)
# """""""select the login with google option"""""""""
# login_page.click_Loginwith_Google()
# sleep(2)
# login_page.click_GooglemailId()
# sleep(5)
# login_page.add_Account()
# sleep(2)
# login_page.Enter_Google_UserID()
# sleep(2)
# login_page.click_Emailid_Nextbtn()
# sleep(4)
# """"To enter password need to use the 2nd method """
# login_page.Enter_Google_Password()
# poco(text("Swdvt@#123"))
# sleep(2)
# login_page.click_Password_Nextbtn()
# sleep(7)
# help_page.chooseAcc()
# """Click hamburger icon to expand menu"""
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.select_File_To_Upload()
# sleep(5)
# """Verify Filename date and datasource"""
# common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
# data_sources_page.verify_File_Data()


def test_DataSources_TestcaseID_45747():
    """test"""


# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
"""Large file"""


# """Click Add File"""
# data_sources_page.click_Add_File()
# """Click Upload file"""
# sleep(2)
# data_sources_page.click_Upload_File()
# """Select Very large File to upload"""
# data_sources_page.searchFileInLocalStorage("exceed_maximum_allowed_size.jpg", "Downloads")
# sleep(2)
# data_sources_page.selectFilesInLocal()
# sleep(5)
# """unable to verify error as there is no error popping up if file exceeds 28.4mb"""
# """28.3mb file"""
# """Click Add File"""
# data_sources_page.click_Add_File()
# """Click Upload file"""
# sleep(2)
# data_sources_page.click_Upload_File()
# """Select File of size 28.3mb to upload"""
# data_sources_page.searchFileInLocalStorage("file_28.3.jpg", "Downloads")
# sleep(2)
# data_sources_page.selectFilesInLocal()
# sleep(5)
# data_sources_page.searchName("file_28.3.jpg")
# sleep(5)
# data_sources_page.verifyFilePresentInList("file_28.3.jpg")
# sleep(5)
# data_sources_page.searchName("")
# """Click Add File"""
# data_sources_page.click_Add_File()
# """Click Upload file"""
# sleep(2)
# data_sources_page.click_Upload_File()
# """Select File of size 28.4 to upload"""
# data_sources_page.searchFileInLocalStorage("file_28.4.jpg", "Downloads")
# sleep(2)
# data_sources_page.selectFilesInLocal()
# sleep(5)
# data_sources_page.searchName("file_28.3.jpg")
# sleep(5)
# data_sources_page.verifyFilePresentInList("file_28.3.jpg")


# def test_DataSources_TestcaseID_45748():
#     """test"""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """get initial count of files"""
# initial_file_count = len(data_sources_page.fileListDisplayed())
# sleep(2)
# """search some words which match with some files name"""
# data_sources_page.searchExistingName()
# """get count after searching"""
# final_file_count = len(data_sources_page.fileListDisplayed())
# """Check if results are filtered"""
# data_sources_page.checkIfResultsAreFiltered(initial_file_count, final_file_count)
# sleep(2)
# """search some words which do not match with any files name"""
# data_sources_page.searchRandomWord()
# """check if the list is empty"""
# data_sources_page.checkIfListIsEmpty()
# """nter special characters to the Search field"""
# data_sources_page.enterSpecialCharactersInsearchField()
# """Cannot verify if error occurs as here is no error."""
# data_sources_page.clearTextAndVerifyFileCount(6)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45749():
    pass


# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("jd4936", "Vl@d#vost0k008", 1, 0, False)
# try:
#     registration_page.wait_for_element_appearance_text("Continue", 30)
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithGoogle("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
# sleep(5)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45750():
#     """Test"""
#
#
# """FB login """
# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Facebook_Icon()
# registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithGoogle("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
# sleep(5)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45751():
#     """Test"""
#
#
# """apple login"""
# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Apple_Icon()
# """Enter OTP manually"""
# registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.signInWithGoogle("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
# sleep(5)
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "Google Drive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# """ google drive """
# data_sources_page.clickGoogleDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "Google Drive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45752():
#     """test"""
#
#
# """Remove if one drive account - zsbswdvt@gmail.com present"""
# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# data_sources_page.signInWithEmail()
# registration_page.complete_sign_in_with_email("jd4936", "Vl@d#vost0k008", 1, 0, False)
# try:
#     registration_page.wait_for_element_appearance_text("Continue", 30)
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45753():
    """Test"""


"""FB login """


# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Facebook_Icon()
# registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45754():
#     """Test"""
#
#
# """apple login"""
# data_sources_page.clearAppData()
# data_sources_page.clearBrowsingData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.wait_for_element_appearance("Sign In", 10)
# registration_page.clickSignIn()
# registration_page.click_Apple_Icon()
# """Enter OTP manually"""
# registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45755():
#     """""""""test"""""
#
#
# """Google Login"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.click_My_Data()
# sleep(5)
# initial_file_count = len(data_sources_page.fileListDisplayed())
# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# data_sources_page.checkFilesShownAreSupported()
# sleep(3)
# data_sources_page.clickBackArrow()
# """Check no file linked"""
# data_sources_page.checkNoChangeInFileCount(initial_file_count)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# png_file = "png_file.png"
# data_sources_page.selectFileDrive(png_file)
# sleep(5)
# data_sources_page.searchName(png_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# jpg_file = "jpg_file.jpg"
# data_sources_page.selectFileDrive(jpg_file)
# sleep(5)
# data_sources_page.searchName(jpg_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# csv_file = "csv_file.csv"
# data_sources_page.selectFileDrive(csv_file)
# sleep(5)
# data_sources_page.searchName(csv_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(csv_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# txt_file = "txt_file.txt"
# data_sources_page.selectFileDrive(txt_file)
# sleep(5)
# data_sources_page.searchName(txt_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(txt_file, "OneDrive", True)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# """ One drive """
# data_sources_page.clickMicrosoftOneDrive()
# sleep(5)
# bmp_file = "bmp_file.bmp"
# data_sources_page.selectFileDrive(bmp_file)
# sleep(5)
# data_sources_page.searchName(bmp_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45756():
#     """test"""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# """Choose the design created at setup"""
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.searchName("45756")
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(2)
# """Click print"""
# data_sources_page.clickPrint()
# """Choose Use Local Contacts in Update Data Connections page"""
# try:
#     poco("Accept").wait_for_appearance(timeout=10)
#     poco("Accept").click()
# except:
#     pass
# try:
#     poco(text="Allow").wait_for_appearance(timeout=10)
#     poco(text="Allow").click()
# except:
#     pass
# sleep(7)
# """Verify if preview is present"""
# data_sources_page.verifyIfPreviewIsPresent()
# poco.scroll()
# """Set the label range accordingly"""
# selection_range = 4
# data_sources_page.labelRangeSelection(selection_range)
# """Verify if preview label range is according to the label range set"""
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels_printing = template_management_page.get_total_labels_printing()
# print(number_of_labels_printing)
# if number_of_labels_printing == str(selection_range):
#     pass
# else:
#     raise Exception("Number of label printed out is not equal to number of contact selected")
# """Click print to print the labels"""
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45757():
    """""""""test"""""


# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# sleep(2)
# """Choose the design created at setup"""
# data_sources_page.searchMyDesigns("45757")
# sleep(3)
# data_sources_page.selectDesignCreatedAtSetUp()
# sleep(3)
# """Click the print option"""
# data_sources_page.clickPrint()
# sleep(5)
# """Verify if there is option to choose picture"""
# data_sources_page.verifyPhotoOptions()
# poco.scroll()
# """Expand to see different options to choose picture"""
# data_sources_page.expandPhotoOptions()
# """Choose camera option"""
# data_sources_page.chooseCameraToClickPhoto()
# """click the photo"""
# try:
#     common_method.wait_for_element_appearance_textmatches("While using the app", 20)
#     data_sources_page.allowPermissions()
# except:
#     pass
# others_page.capture_the_image_button()
# data_sources_page.clickOk()
# """Part of step 4 is to check the preview is correct
#     unable to verify preview has to be done manually"""
# """Print the photo"""
# while not poco("Print", enabled=True).exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_45758():
#     """""""""test"""""
#
#
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# if data_sources_page.verifySignInWithGoogle():
#     registration_page.click_Google_Icon()
# account = "zebratest850@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
# registration_page.sign_In_With_Google("Zebra#123456789", account)
# sleep(2)
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# data_sources_page.checkDriveEmpty()
# """Cannot automate - Check the Select button is disabled. as select button not displayed"""
# data_sources_page.clickBackArrow()

# """One Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ One drive """
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# if data_sources_page.verifySignInWithMicrosoft():
#     data_sources_page.signInWithMicrosoft(account, "Zebra#123456789")
#     sleep(2)
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.checkDriveEmpty()
# """Cannot automate - Check the Select button is disabled. as select button not displayed"""
# data_sources_page.clickBackArrow()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_45759():
    """""""""test"""""


# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# """Click hamburger icon to expand menu"""
# try:
#     registration_page.wait_for_element_appearance("Home", 30)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# if data_sources_page.verifySignInWithGoogle():
#     registration_page.click_Google_Icon()
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# sleep(2)
# existing_file = data_sources_page.selectExistingFile()
# sleep(5)
# data_sources_page.searchName(existing_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(existing_file, "Google Drive", True)
# """Re upload same file"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """CLick Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickGoogleDrive()
# sleep(2)
# data_sources_page.selectExistingFile()
# sleep(2)
# """Verify if 'filename' is already linked pop up appears"""
# data_sources_page.checkIsAlreadyLinkedPopUp()
# sleep(3)
# """"""""""""
# """ One Drive """
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# if data_sources_page.verifySignInWithMicrosoft():
#     data_sources_page.signInWithMicrosoft("zsbswdvt@gmail.com", "hmWepX4AUMLa!9E")
#     sleep(2)
# template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(3)
# existing_file = data_sources_page.selectExistingFile()
# sleep(3)
# data_sources_page.searchName(existing_file)
# sleep(5)
# data_sources_page.verifyFilePresentInList(existing_file, "OneDrive", True)
# """Re upload same file"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """CLick Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# data_sources_page.clickMicrosoftOneDrive()
# sleep(2)
# data_sources_page.selectExistingFile()
# """Verify if 'filename' is already linked pop up appears"""
# data_sources_page.checkIsAlreadyLinkedPopUp()
# common_method.Stop_The_App()


def test_DataSources_TestcaseID_47830():
    """""""""test"""""


"""Click hamburger icon to expand menu"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Designs in menu"""
# data_sources_page.clickMyDesigns()
# sleep(2)
# start_app("com.android.chrome")
# sleep(2)
# poco("com.android.chrome:id/tab_switcher_button").click()
# sleep(2)
# poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# sleep(2)
# data_sources_page.clickEnter()
# sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# sleep(2)
# data_sources_page.lock_phone()
# sleep(2)
# wake()
# sleep(3)
# data_sources_page.clickMyDesigns()
# sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# sleep(5)
# data_sources_page.lock_phone()
# wake()
# data_sources_page.clickCreateDesignBtn()
# sleep(5)
# data_sources_page.selectLabelSize()
# data_sources_page.clickContinueWeb()
# poco(text="Exit Designer").wait_for_appearance(timeout=10)
# data_sources_page.lock_phone()
# sleep(2)
# wake()
# label_name = "PullDownToRefresh"
# data_sources_page.setLabelName(label_name)
# sleep(5)
# data_sources_page.exitDesigner()
# stop_app("com.android.chrome")
# sleep(2)
# """No pull down to refresh option due to bug SMBM-1710"""
# data_sources_page.searchMyDesigns(label_name)
# try:
#     common_method.wait_for_element_appearance_namematches("There are currently no designs saved to your workspace. To get started go to our Common Designs to see some premade designs.")
# except:
#     raise Exception("New Design created in web is present without the need to refresh.")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data in menu"""
# data_sources_page.click_My_Data()
# start_app("com.android.chrome")
# sleep(2)
# poco("com.android.chrome:id/tab_switcher_button").click()
# sleep(2)
# poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# sleep(2)
# data_sources_page.clickEnter()
# sleep(3)
# data_sources_page.click_Menu_HamburgerICNWeb()
# sleep(5)
# data_sources_page.lock_phone()
# sleep(2)
# wake()
# data_sources_page.click_My_Data()
# sleep(5)
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.click_Upload_File_Web()
# selected_file_name = data_sources_page.selectFileToUploadWeb()
# stop_app("com.android.chrome")
# """No pull down to refresh option due to bug SMBM-1710"""
# sleep(5)
# data_sources_page.searchName(selected_file_name)
# try:
#     common_method.wait_for_element_appearance_namematches("List is empty")
# except:
#     raise Exception("New File updated in web is present without the need to refresh.")
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_47936():
#     """""""""test"""""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(2)
# """Select File to upload"""
# selected_file = data_sources_page.select_File_To_Upload(True)
# sleep(5)
# """Notification on file upload"""
# """Unable to verify due to BUG SMBM-712"""
# data_sources_page.searchName(selected_file)
# data_sources_page.remove_File()
# """Notification on file removal"""
# """Unable to verify due to BUG SMBM-712"""
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_47942():
#     """""""""test"""""
#
#
# common_method.Start_The_App()
# """Click hamburger icon to expand menu"""
# login_page.click_Menu_HamburgerICN()
# sleep(5)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Click Add File"""
# data_sources_page.click_Add_File()
# sleep(5)
# """Click Upload file"""
# data_sources_page.click_Upload_File()
# sleep(5)
# """Select File to upload"""
# data_sources_page.selectFileInLocalStorage()
# sleep(5)
# """Verify Progress Indicator"""
# data_sources_page.verifyProgressIndicator()
# """Verify if file uploaded succesfully"""
# common_method.Stop_The_App()


# def test_DataSources_TestcaseID_47944():
#     """""""test"""
#
#
# """Click hamburger icon to expand menu"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(2)
# data_sources_page.click_Add_File()
# sleep(2)
# data_sources_page.click_Upload_File()
# template_management_page.wait_for_appearance_enabled("Show roots")
# """select 4-BMP.BMP"""
# data_sources_page.searchFileInLocalStorage("4-BMP.BMP", "Downloads")
# sleep(5)
# """Step 5 pending as no error pop up"""
# data_sources_page.searchName("4-BMP.BMP")
# sleep(5)
# """check list empty"""
# data_sources_page.checkIfListIsEmpty()
# common_method.Stop_The_App()
