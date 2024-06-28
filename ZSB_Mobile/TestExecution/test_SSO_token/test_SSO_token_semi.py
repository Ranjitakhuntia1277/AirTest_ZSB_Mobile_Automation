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


def test_SSO_Token_Renewal_TestcaseID_49906():
    pass
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Login"""
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zsbtestsso@gmail.com"
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
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
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
    account = "zsbtestsso@gmail.com"
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
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Apple login"""
    registration_page.clickSignIn()
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
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
    registration_page.click_Apple_Icon()
    registration_page.login_Apple("DLpwhvr@JCQ5Gkx", "zsbswdvt@gmail.com")
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
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    help_page.checkIfOnSignInPage()
    """Facebook Login"""
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
    """verify if logged in successfully"""
    data_sources_page.checkIfOnHomePage()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sso_token_renewal_page.terminateBatchFileProcess(process)
    """Check that there is a message about "exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}" in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_exchangeCode_message_present()
    """Check that there is a token information about " : flutter: getLocalTokens : access_token: " in the adb log or tidevice syslog"""
    sso_token_renewal_page.check_if_getLocalTokens_information_present()
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
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("zsbswdvt@1234", "zsbswdvt@gmail.com")
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


def test_SSO_Token_Renewal_TestcaseID_49919():
    pass
    """device 1"""
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zsbtestsso@gmail.com", "Zebra#123456789", 1, 0)
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
    old_token_1 = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    new_token_1 = sso_token_renewal_page.checkTokenRefreshed(old_token_1)
    """Check if still on logged in page"""
    """cannot automate - Check the bottom of the screen when the token is about to renew, there is no error message popping up (Like "** STOP Error 500\** ", for covering SMBM-2557)"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    common_method.Stop_The_App()
    """device 2"""
    """clear app data"""
    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    """Sign in"""
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("zsbtestsso@gmail.com", "Zebra#123456789", 1, 0)
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
    old_token_2 = sso_token_renewal_page.get_token()
    process = sso_token_renewal_page.runBatchFileToFetchLogs()
    sleep(3120)
    sso_token_renewal_page.terminateBatchFileProcess(process)
    new_token_2 = sso_token_renewal_page.checkTokenRefreshed(old_token_2)
    """Check if still on logged in page"""
    """cannot automate - Check the bottom of the screen when the token is about to renew, there is no error message popping up (Like "** STOP Error 500\** ", for covering SMBM-2557)"""
    sso_token_renewal_page.check_if_user_is_logged_in()
    common_method.Stop_The_App()
    if new_token_1 != new_token_2:
        pass
    else:
        raise Exception("Tokens of this account in the different devices are not different and individual.")
