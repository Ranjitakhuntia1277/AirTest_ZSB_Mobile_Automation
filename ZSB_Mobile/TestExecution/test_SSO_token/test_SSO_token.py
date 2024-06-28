from ZSB_Mobile.PageObject.SSO_Token_Renewal_Screen.SSO_Token_Renewal_Screen_Android import SSO_Token_Renewal_Screen
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ZSB_Mobile.PageObject.Delete_Account.Delete_Account_Screen import Delete_Account_Screen
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.Device_Networks.Device_Network_Android import Device_Networks_Android
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from poco.exceptions import PocoNoSuchNodeException
import pytest


class SSO_Token_Renewal:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
delete_account_page = Delete_Account_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
device_network_page = Device_Networks_Android(poco)
sso_token_renewal_page = SSO_Token_Renewal_Screen(poco)


def test_SSO_Token_Renewal_TestcaseID_49905():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebra07.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", account)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process, 20)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}"
    in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    x=1/0
    """Check that there is token information about " : flutter: getLocalTokens : access_token: " in the adb log or
    tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    x=1/0
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(30)
    # 3120
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebra07.swdvt@gmail.com"
    template_management_page.checkIfAccPresent(account)
    help_page.chooseAcc(account)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Swipe up"""
    poco.scroll()
    """Click Help dropdown to expand Help options"""
    help_page.click_Help_dropdown_option()
    sso_token_renewal_page.checkIfHelpPagesArePresent()
    template_management_page.click_scrim()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Click hamburger icon to expand menu"""
    login_page.click_Menu_HamburgerICN()
    """Swipe up"""
    poco.scroll()
    """Click Help dropdown to expand Help options"""
    help_page.click_Help_dropdown_option()
    sso_token_renewal_page.checkIfHelpPagesArePresent()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49907():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """wait for 53 min"""
    sleep(3120)
    """Check if user still logged in"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    sso_token_renewal_page.noErrorOccurredAfterPrinting()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49908():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Check if still on logged in page"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49909():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    sleep(3000)
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page.Click_Next_Button()
    add_a_printer_page.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    sleep(120)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """wait till wi-fi turn green."""
    registration_page.timeTillWiFiGreen()
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_page.click_Finish_Setup_Button()
    """Local"""
    login_page.click_Menu_HamburgerICN()
    sleep(5)
    """Click My Data"""
    data_sources_page.click_My_Data()
    """Click Add File"""
    data_sources_page.click_Add_File()
    data_sources_page.click_Upload_File()
    sleep(3)
    selected_file_name = data_sources_page.selectFileInLocalStorage()
    sleep(10)
    data_sources_page.searchName(selected_file_name)
    sleep(7)
    data_sources_page.verifyFilePresentInList(selected_file_name, "Local File")
    data_sources_page.searchName("")
    sleep(7)
    """Google drive"""
    """Click Add File"""
    data_sources_page.click_Add_File()
    """Click Upload file"""
    data_sources_page.click_Link_File()
    """Test for Google Drive"""
    sleep(2)
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
    sleep(2)
    jpg_file = "jpg_file.jpg"
    data_sources_page.selectFileDrive(jpg_file)
    sleep(5)
    data_sources_page.searchName(jpg_file)
    sleep(5)
    data_sources_page.verifyFilePresentInList(jpg_file, "Google Drive", True)
    data_sources_page.searchName("")
    sleep(7)
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    """ One drive """
    data_sources_page.clickMicrosoftOneDrive()
    sleep(5)
    data_sources_page.selectFileDrive(jpg_file)
    sleep(5)
    data_sources_page.searchName(jpg_file)
    sleep(5)
    data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49910():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Open a different app"""
    start_app("com.android.chrome")
    """wait for 52 min"""
    sleep(3120)
    """Close the other app"""
    stop_app("com.android.chrome")
    """Check if still on logged in page"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    sso_token_renewal_page.noErrorOccurredAfterSwitchingApps()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    template_management_page.checkDisplayedCountMatchesExpected("1")
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    printer_management_page.clickPrinter1InPinterSettings()
    app_settings_page.click_Test_Print_Button()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49911():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Open a different app"""
    start_app("com.android.chrome")
    """wait for 52 min"""
    sleep(3120)
    """Close the other app"""
    stop_app("com.android.chrome")
    """Check if still on logged in page"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    sso_token_renewal_page.noErrorOccurredAfterSwitchingApps()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    """"change the darkness level"""
    sso_token_renewal_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    printer_management_page.clickPrinter1InPinterSettings()
    printer_management_page.setPrinterName("ZSB-DP12A")
    """verify the printer name updated message"""
    app_settings_page.verify_Printer_Name_Updated_Message()
    """"""
    """Reset darkness and printer name to default"""
    printer_management_page.setPrinterName("ZSB-DP12")
    app_settings_page.verify_Printer_Name_Updated_Message()
    sso_token_renewal_page.goToCommonTabPrinterSettings()
    app_settings_page.Change_Darkness_Level_Bar()
    app_settings_page.Verify_Darkness_Updated_Message()
    sso_token_renewal_page.Change_Darkness_Level_Bar(100)
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49912():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Open a different app"""
    start_app("com.android.chrome")
    """wait for 60 min"""
    sleep(3600)
    """Close the other app"""
    stop_app("com.android.chrome")
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_page.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page.Click_Next_Button()
    add_a_printer_page.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 20)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """wait till wi-fi turn green."""
    registration_page.timeTillWiFiGreen()
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_page.click_Finish_Setup_Button()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


# def test_SSO_Token_Renewal_TestcaseID_49913():
#     pass
#     """clear app data"""
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     """Sign in"""
#     registration_page.clickSignIn()
#     data_sources_page.signInWithEmail()
#     registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
#     """verify if logged in successfully"""
#     data_sources_page.checkIfOnHomePage()
#     """Open a different app"""
#     start_app("com.android.chrome")
#     """wait for 1 day 5 min"""
#     sleep(86700)
#     """Close the other app"""
#     stop_app("com.android.chrome")
#     """Check if still on logged in page"""
#     sso_token_renewal_page.check_if_user_is_logged_in()
#     login_page.click_Menu_HamburgerICN()
#     """Open printer settings"""
#     app_settings_page.click_Printer_Settings()
#     """Select printer"""
#     printer_management_page.clickPrinter1InPinterSettings()
#     app_settings_page.click_wifi_tab()
#     app_settings_page.click_Manage_Networks_Btn()
#     app_settings_page.click_Add_Network()
#     """Continue"""


def test_SSO_Token_Renewal_TestcaseID_49914():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Force quit the app"""
    common_method.Stop_The_App()
    """wait for 53 min"""
    sleep(3180)
    """Open the app"""
    common_method.Start_The_App()
    """Check if user still logged in"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    sso_token_renewal_page.checkTokenRefreshed(old_token)
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    sso_token_renewal_page.noErrorOccurredAfterPrinting()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49915():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Force quit the app"""
    common_method.Stop_The_App()
    """wait for 65 min"""
    sleep(3900)
    """Open the app"""
    common_method.Start_The_App()
    """Check if user still logged in"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    old_name_first, old_name_last = sso_token_renewal_page.get_name()
    old_name = sso_token_renewal_page.get_name(False)
    """change avatar"""
    """""click on upload photo"""
    app_settings_page.click_User_upload_photo()
    """click on camera option"""
    app_settings_page.click_Mobile_Camera()
    """""click allow if it is present"""
    app_settings_page.Click_Allow_popup()
    """"click on click picture icon"""
    others_page.capture_the_image_button()
    data_sources_page.clickOk()
    """"Verify photo uploaded message"""""
    app_settings_page.Verify_Photo_Uploaded_Message()
    """change name"""
    """Change first name"""
    delete_account_page.change_first_name()
    """Change last name"""
    delete_account_page.change_last_name()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click Home"""
    data_sources_page.clickHome()
    """Click on edit profile"""
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    new_name = sso_token_renewal_page.get_name(False)
    print(old_name, new_name)
    if old_name != new_name:
        pass
    else:
        raise Exception("Name change not successful.")
    """avatar verification pending"""
    """Change everything back to normal for future execution"""
    """Change first name"""
    delete_account_page.change_first_name(old_name_first)
    """Change last name"""
    delete_account_page.change_last_name(old_name_last)
    """Remove avatar photo"""
    app_settings_page.click_User_Photo_Remove_Image()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49916():
    pass
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
    account = "zebra06.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zebra06.swdvt@gmail.com", "Zebra#123456789")
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    new_token = sso_token_renewal_page.checkTokenRefreshed(old_token)
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.select_design_common_designs()
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Login Again"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebra07.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", account)
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check token refreshed after logout and login"""
    sso_token_renewal_page.checkTokenRefreshed(new_token)
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Three_Dot_On_Workspace()
    """Click change theme"""
    app_settings_page.click_Change_Theme()
    """Change default theme to any other theme"""
    app_settings_page.check_Change_Electic_Theme()
    """click on the save & exit"""
    app_settings_page.click_Save_Exit_Btn()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Three_Dot_On_Workspace()
    """Click change theme"""
    app_settings_page.click_Change_Theme()
    """Check theme is changed"""
    sso_token_renewal_page.checkThemeChanged()
    """"""
    """Revert back changes to default for future execution"""
    app_settings_page.check_Change_Modern_Theme()
    """click on the save & exit"""
    app_settings_page.click_Save_Exit_Btn()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49917():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    template_management_page_1.turn_off_wifi()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click on edit profile"""
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    """Blocked"""
    """Cannot verify error due to bug SMBM-2178"""
    """Turn on wi-fi for next execution"""
    template_management_page_1.turn_off_wifi()
    common_method.Stop_The_App()


def test_SSO_Token_Renewal_TestcaseID_49918():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zebra07.swdvt@gmail.com", "Zebra#123456789", 1, 0)
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    """Wait for 50 min"""
    sleep(3000)
    """Disconnect network"""
    template_management_page_1.turn_off_wifi()
    """Wait for 2 min"""
    sleep(120)
    """Connect to network"""
    template_management_page_1.turn_on_wifi()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
    """Check the token is refreshed at 8 minutes prior to expiry time[480 ~420 second]"""
    old_token = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    new_token = sso_token_renewal_page.checkTokenRefreshed(old_token)
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Open Notifications"""
    app_settings_page.click_Notifications_Tab()
    app_settings_page.click_Notification_Settings_Tab()
    sso_token_renewal_page.updateNotificationSettings()
    """Click Hamburger Icon"""
    login_page.click_Menu_HamburgerICN()
    """Click Home"""
    data_sources_page.clickHome()
    """Click on edit profile"""
    login_page.click_Menu_HamburgerICN()
    """Open Notifications"""
    app_settings_page.click_Notifications_Tab()
    app_settings_page.click_Notification_Settings_Tab()
    """Cannot verify - check it can be correctly updated"""
    """ask someone"""
    common_method.Stop_The_App()


def test_Registration_TestcaseID_47786():
    """""""""test"""""

    common_method.tearDown()
    # others_page.uninstall_and_install_zsb_series_on_google_play(True)
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    sleep(2)
    registration_page.clickSignIn()
    if poco(text="Allow").exists():
        poco(text="Allow").click()
    poco("Continue with Google").wait_for_appearance(timeout=10)
    registration_page.click_Google_Icon()
    sleep(2)
    help_page.chooseAcc("zebra03.swdvt@gmail.com")
    data_sources_page.checkIfOnHomePage()
    # others_page.uninstall_and_install_zsb_series_on_google_play(True, True)
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    sleep(2)
    registration_page.clickSignIn()
    if poco(text="Allow").exists():
        poco(text="Allow").click()
    poco("Continue with Google").wait_for_appearance(timeout=10)
    registration_page.click_Google_Icon()
    sleep(2)
    help_page.chooseAcc("zebra03.swdvt@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    """Token verification pending"""
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45870():
    pass
    common_method.tearDown()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    login_page.click_GooglemailId()
    registration_page.wait_for_element_appearance_text("Add account to device")
    registration_page.addAccountToDevice()
    registration_page.sign_In_With_Google("zsbswdvt@123", "zebra03.swdvt@gmail.com", True)
    registration_page.sign_In_With_Google("Zebra#123456789")
    data_sources_page.checkIfOnHomePage()
    sleep(7200)
    data_sources_page.checkIfOnHomePage()
    registration_page.clickConnect()


