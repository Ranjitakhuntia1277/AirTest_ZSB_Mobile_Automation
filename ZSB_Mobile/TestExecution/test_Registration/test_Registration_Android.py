from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen


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
    """""""""test"""""

    data_sources_page.clearAppData()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    if poco("com.android.chrome:id/coordinator").exists():
        poco("com.android.chrome:id/coordinator").click()
    keyevent("back")
    registration_page.verifyLinksInSignInPage()
    registration_page.registerEmail()
    try:
        registration_page.wait_for_element_appearance_text("ZSB Printer Account Registration", 20)
    except:
        raise Exception("register user page dint show")

    """Enter the User Email"""
    registration_page.enter_user_email_for_registering("zsbswdvt@gmail.com")
    registration_page.click_on_next()
    """header \"This email already exist\" and message \"It looks like this email has already been registered. Please try logging in with your credentials. not matching with displayed text"""
    """Verify Account already exists page title"""
    registration_page.check_email_already_exists_page_title()
    """Verify Account already exists page message"""
    registration_page.check_email_already_Exists_page_message()
    """No RETURN TO LOGIN button."""
    """Click Continue"""
    data_sources_page.clickContinue()
    try:
        registration_page.wait_for_element_appearance("Sign In", 10)
    except:
        raise Exception("Did not return to login page.")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45859():
    """""""""test"""""

    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("soho_dvtxxxxx@hotmail.com", "soho_dvtxxxxx@hotmail.com", 1, 0, True)
    try:
        registration_page.wait_for_element_appearance_text(
            "We didn't recognize the username or password you entered. Please try again.")
    except:
        raise Exception(
            "\"We didn't recognize the username or password you entered. Please try again.\" message did not appear.")
    try:
        registration_page.wait_for_element_appearance_text("Sign In With")
    except:
        raise Exception("Page not at Login with username.")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45860():
    """""""""test"""""

    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("jd4936", "Zebra#1234567890", 1, 0, True)
    try:
        registration_page.wait_for_element_appearance_text(
            "We didn't recognize the username or password you entered. Please try again.")
    except:
        raise Exception(
            "Error message : \"We didn't recognize the username or password you entered. Please try again.\" not shown")
    data_sources_page.signInWithEmail()
    registration_page.complete_sign_in_with_email("jd4936", "Vl@d#vost0k008", 1, 0, False, True)
    try:
        registration_page.wait_for_element_appearance_text("Continue", 70)
        data_sources_page.clickContinue()
    except:
        pass
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45861():
    """""""""test"""""

    common_method.tearDown()
    registration_page.clickSignIn()
    sleep(2)
    registration_page.verifyLinksInSignInPage()
    scroll_view = poco("android.view.View")
    while not poco(text="Sign In With"):
        scroll_view.swipe("down")
    registration_page.click_Google_Icon()
    try:
        poco(text="Choose an account").wait_for_appearance(timeout=20)
        help_page.chooseAcc("zsbswdvt@gmail.com")
    except:
        pass
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    sleep(2)
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 10)
    except:
        raise Exception("Did not redirect to the login page")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45863():
    """""""""test"""""

    common_method.tearDown()
    registration_page.clickSignIn()
    registration_page.click_Facebook_Icon()
    registration_page.login_Facebook("zsbswdvt@123", "zsbswdvt@gmail.com", True)
    registration_page.login_Facebook("zsbswdvt@1234")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    name = registration_page.get_login_name_from_menu()
    if name == "swdvt zsb":
        pass
    else:
        raise Exception("Login name does not match")
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45868():
    """""""""test"""""

    """Test on stage build"""
    common_method.tearDown()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    if poco("com.android.chrome:id/coordinator").exists():
        poco("com.android.chrome:id/coordinator").click()
    keyevent("back")
    poco.scroll()
    registration_page.click_on_reset_password()
    try:
        registration_page.check_if_in_password_recovery_page()
    except:
        raise Exception("Did not navigate to 'Password Recovery' Page")
    # help_page.verify_url("https://stagec-signup.zebra.com/content/userreg/reset-password-landing.html")
    help_page.verify_url("https://signup.zebra.com/content/userreg/reset-password-landing.html")
    sleep(2)
    registration_page.Enter_Username_password_recovery_page("zsbswdvt1@gmail.com")
    if registration_page.check_submit_is_clickable():
        pass
    else:
        raise Exception("Submit is not clickable.")
    registration_page.click_SUBMIT()
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45869():
    """""""""test"""""

    common_method.tearDown()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    poco(text="Choose an account").wait_for_appearance(timeout=20)
    help_page.chooseAcc("zsbswdvt@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    registration_page.click_Buy_More_Labels()
    try:
        poco(text="Allow").wait_for_appearance(timeout=20)
        poco(text="Allow").click()
    except:
        pass
    help_page.verify_url("https://www.zebra.com/smb/us/en/labels.html")
    common_method.Stop_The_App()


def test_Registration_TestcaseID_46303():
    """""""""test"""""

    common_method.tearDown()
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
    common_method.wait_for_element_appearance("Connect to Wi-Fi", 30)
    common_method.wait_for_element_appearance("Discovered networks", 30)
    """"click on connect button on connect wi-fi network screen"""
    registration_page.connectToWIfi()
    registration_page.enterPasswordWifi()
    """Store the time till wi-fi turn green."""
    time_taken = registration_page.timeTillWiFiGreen()
    print(time_taken)
    """"click on finish setup button"""
    common_method.wait_for_element_appearance("Printer registration was successful", 30)
    add_a_printer_page.click_Finish_Setup_Button()
    common_method.Stop_The_App()
#
#
def test_Registration_TestcaseID_46306():
    """""""""test"""""
#
    common_method.tearDown()
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
    try:
        registration_page.wait_for_element_appearance("Connect to Wi-Fi", 50)
    except:
        raise Exception("Bluetooth connection unsuccessful")
    common_method.wait_for_element_appearance("Discovered networks", 30)
    registration_page.connectToWIfi("POCO M3")
    registration_page.enterPasswordWifi("123456789")
    try:
        registration_page.wait_for_element_appearance("Incorrect Wi-Fi password entered", 60)
        x=1/0
    except ZeroDivisionError:
        raise Exception("Internet access blocked message did not show up.")
    except Exception as e:
        pass
    common_method.Stop_The_App()


def test_Registration_TestcaseID_46307():
    """""""""test"""""

    common_method.tearDown()
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
    common_method.Stop_The_App()


def test_Registration_TestcaseID_47786():
    """""""""test"""""

    common_method.tearDown()
    others_page.uninstall_and_install_zsb_series_on_google_play(True)
    sleep(2)
    registration_page.clickSignIn()
    if poco(text="Allow").exists():
        poco(text="Allow").click()
    poco("Continue with Google").wait_for_appearance(timeout=10)
    registration_page.click_Google_Icon()
    sleep(2)
    help_page.chooseAcc("zsbswdvt@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    others_page.uninstall_and_install_zsb_series_on_google_play(True, True)
    sleep(2)
    registration_page.clickSignIn()
    if poco(text="Allow").exists():
        poco(text="Allow").click()
    poco("Continue with Google").wait_for_appearance(timeout=10)
    registration_page.click_Google_Icon()
    sleep(2)
    help_page.chooseAcc("zsbswdvt@gmail.com")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    """Token verification pending"""
    common_method.Stop_The_App()


def test_Registration_TestcaseID_45862():
    """""""""test"""""


    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    while not poco(text="Use another account").exists():
        poco.scroll()
    login_page.click_GooglemailId()
    while not poco(text="Add account to device").exists():
        poco.scroll()
    registration_page.addAccountToDevice()
    registration_page.sign_In_With_Google("wrongloginzsb@123", "wrongloginzsb@gmail.com", True)
    registration_page.sign_In_With_Google("wrongloginzsb@1234")
    try:
        common_method.wait_for_element_appearance_text("For the best experience, we need a couple of things from you.",
                                                       20)
        poco(text="For the best experience, we need a couple of things from you.").parent().child()[1].focus(
            [0.5, 0.2]).click()
        text("ZSB")
        data_sources_page.clickContinue()
    except:
        pass
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    name = registration_page.get_login_name_from_menu()
    if name == "wrongLoginZsb ZSB":
        pass
    else:
        raise Exception("Login name does not match")
    registration_page.click_on_profile_edit()
    poco.scroll()
    registration_page.click_log_out_button()
    try:
        registration_page.wait_for_element_appearance("Sign In", 5)
    except:
        raise Exception("Did not redirect to the login page")
    common_method.Stop_The_App()

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