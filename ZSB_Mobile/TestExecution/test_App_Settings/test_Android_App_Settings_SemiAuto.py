from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others.Others import Others

# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)
others = Others(poco)

"""""""""""""""""""""""Change Password part needs to be verified manually"""""""""""""""""""""""""""""


# #### bug id-SMBM-2773
def test_AppSettings_TestcaseID_47913():
    """Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""


    common_method.tearDown()
    #test_robo_finger()
    sleep(6)
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_screen.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_screen.click_Start_Button()
    login_page.click_Allow_ZSB_Series_Popup()
    add_a_printer_screen.Verify_Lets_Make_Sure_Text()
    add_a_printer_screen.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_screen.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_screen.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_screen.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
    """"verify pairing your printer text"""
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"verify pairing your printer text"""
    add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
    add_a_printer_screen.click_Password_Field_On_Join_Network()
    add_a_printer_screen.click_Submit_Button_ON_Join_Network()
    """"verify need the printer driver text"""
    add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
    """""verify registering your printer text"""
    add_a_printer_screen.Verify_Registering_your_Printer_Text()
    """"Turn OFF the WIFI & Turn on again after some time (approx. 2 min)"""
    aps_notification.disable_wifi()
    aps_notification.enable_wifi()
    sleep(7)
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Setup_Button()
    """stop the app"""
    common_method.Stop_The_App()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


####### bug id---SMBM-2778
def test_AppSettings_TestcaseID_50031():
    """Check the error message prompted when print test page and printer head open or offline"""



    """printer should be online"""
    """start the app"""
    common_method.tearDown()
    sleep(3)
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify home text is displaying on the home screen"""
    app_settings_page.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings tab"""""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """click test print button"""
    app_settings_page.click_Test_Print_Button()
    """"Verify Printed successfully text"""
    app_settings_page.Verify_Printed_Successfully_Text()
    """"Open the printer cover manually"""
    sleep(15)
    """click test print button"""
    app_settings_page.click_Test_Print_Button()
    """""verify error message of cover open"""
    app_settings_page.Verify_ErrorMessage_Text()
    """""Cover close on the printer manually"""""
    """"click on test print"""
    app_settings_page.click_Test_Print_Button()
    """"Verify Printed successfully text"""
    app_settings_page.Verify_Printed_Successfully_Text()
    """stop the app"""
    common_method.Stop_The_App()


## #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id-SMBM-2160
def test_AppSettings_TestcaseID_49709():
    """Manage network- Check able to manage network with long name"""


    """"printer should be online & wifi should be connected"""
    """start the app"""
    common_method.tearDown()
    """click on hamburger menu icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
    app_settings_page.accept_Continue_popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"""""""verify the continue button and click on that"""""
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    sleep(5)
    """"""""""Verify the Add Network text & button & click on that"""""""""""
    app_settings_page.click_Add_Network()
    sleep(3)
    """""""""""""Verify Add network page is opening and verify the text"""""""
    app_settings_page.get_text_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Long_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
    app_settings_page.Verify_Long_Network_UserName()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    """"click on the red icon to delete the added network name"""
    app_settings_page.click_Red_Icon_to_remove_network()
    """stop the app"""
    common_method.Stop_The_App()

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ####bug id-SMBM-2163
def test_AppSettings_TestcaseID_49711():
    """Manage networks- Check there is a prompt message when applying to the network which can't resolve Zebra host"""



    """start the app"""
    common_method.tearDown()
    """click on hamburger menu icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    """"verify bluetooth connection required text"""
    app_settings_page.get_text_Bluetooth_connection_required_Txt()
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page.click_Allow_Btn()
    app_settings_page.click_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Long_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
    app_settings_page.Verify_Long_Network_UserName()
    app_settings_page.click_Apply_Chnages_Button()
    """""Currently there is no error message displaying so Couldnot automate, it is blocked due to SMBM-2163"""""""""""
    app_settings_page.Verify_The_Invalid_Network_Error_Message()
    """stop the app"""
    common_method.Stop_The_App()

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50326():
    """Manage Network- Check able to add/delete/sort network when printer bt paired/unpaired in device""""""
    
    """"App should be in logged in condition & printer should be added """"
    """"""connect with Another wifi Network except NESTWIFI"""



    """"start the app"""
    common_method.tearDown()
    """"click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
    app_settings_page.click_Add_Network()
    app_settings_page.click_ZEBRA_Network()
    app_settings_page.click_Network_Password_Field()
    app_settings_page.click_Network_Submit_Btn()
    app_settings_page.Verify_NestWIFI_Network_Name_In_Network_List()
    app_settings_page.click_Red_Icon_to_remove_network()
    app_settings_page.Verify_NestWIFI_In_Network_List()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    app_settings_page.Verify_Printer_is_already_added()
    """stop the app"""
    common_method.Stop_The_App()
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50325():
    """Manage Network-Check able to add/delete/sort network when printer bt paired/unpaired in device"""


    """"App should be in logged in condition & printer should be added """



    """"start the app"""
    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_wifi_tab()
    app_settings_page.click_Manage_Networks_Btn()
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page.click_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Security_Open()
    app_settings_page.click_WPA_PSK()
    app_settings_page.click_Keyboard_back_Icon()
    app_settings_page.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page.Verify_Added_Network()
    """stop the app"""
    common_method.Stop_The_App()



def test_Others_TestcaseID_51703():
    pass
    common_method.show_message("Install the testing build on device")

    sleep(2)
    common_method.tearDown()

    others.check_allow_permission_for_location()
    login_page.click_loginBtn()
    try:
        others.click_on_allow()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass
    try:
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.click_an_google_account("zebra850.swdvt@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home",30)
    res = others.check_home_page()
    if not res:
        raise Exception("Not in Home page")

    others.uninstall_and_install_zsb_series_on_google_play()
    common_method.wait_for_element_appearance_namematches("Uninstall",30)
    stop_app("com.android.vending")

    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    while(1):
        if others.check_zsb_app_icon():
            t='present'
            break
        else:
            others.scroll_down()

    others.click_zsb_app_icon()
    sleep(5)

    try:
        others.check_allow_permission_for_location()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass

    try:
        login_page.click_loginBtn()
    except:
        pass
    try:
        others.click_on_allow()
    except:
        pass
    try:
        common_method.wait_for_element_appearance_namematches("Continue with Google")
        login_page.click_Loginwith_Google()
        common_method.wait_for_element_appearance_textmatches("Choose an account")
        others.click_an_google_account("zebra850.swdvt@gmail.com")
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Home",30)

    res = others.check_home_page()
    if not res:
        raise Exception("Not in Home page")

def test_Others_TestcaseID_51704(self):
    pass

    common_method.show_message("Install the older build in phone")
    common_method.show_message("now install 1. Install the new build, ")

    sleep(10)

    start_app("com.zebra.soho_app")
    common_method.wait_for_element_appearance_textmatches("location")
    others.check_allow_permission_for_location()
    try:
        others.click_on_allow()
    except:
        pass
    others.click_on_older_login()
    try:
        others.click_on_allow()
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    try:
        others.click_an_google_account("zebra850.swdvt@gmail.com")
        common_method.wait_for_element_appearance_namematches("Home",20)
    except:
        pass
    try:
        others.check_continue_button_and_click_enter()
        others.check_continue_button_and_click_enter()
    except:
        pass
    res = others.check_home_page()

    if not res:
        raise Exception("Not in Home page")

    cmd ='adb uninstall com.zebra.soho_app'
    res = others.run_the_command(cmd)
    print(res)

    common_method.show_message("install older build and new build again")
    sleep(15)
    poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    while(1):
        if others.check_zsb_app_icon():
            t='present'
            break
        else:
            others.scroll_down()

    others.click_zsb_app_icon()
    sleep(5)

    others.check_allow_permission_for_location()
    try:
        others.click_on_allow()
    except:
        pass
    login_page.click_loginBtn()
    try:
        others.click_on_allow()
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Continue with Google")
    login_page.click_Loginwith_Google()
    common_method.wait_for_element_appearance_textmatches("Choose an account")
    try:
        others.click_an_google_account("zebra850.swdvt@gmail.com")
        common_method.wait_for_element_appearance_namematches("Home",20)
    except:
        pass

    try:
        others.check_continue_button_and_click_enter()
        others.check_continue_button_and_click_enter()
    except:
        pass

    res = others.check_home_page()

    if not res:
        raise Exception("Not in Home page")


def test_Others_TestcaseID_45874(self):
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Home")
    except:
        pass

    expected_version_no = common_method.get_user_input("enter the version number to be expected")
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()

    """get the version number of the current device"""
    actual_version_no = others.get_the_version_no()

    """If version number not same generate error"""
    if expected_version_no != actual_version_no:
        raise Exception("Version no did not match")


###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Others_TestcaseID_45799():
    pass

    common_method.show_message("test this manually in android 8.0 device")

    # start_app("com.android.documentsui")
    # t=''
    # others.install_the_zsb_apk_in_files_android_8()
    # sleep(3)
    # res = others.check_app_is_installed_on_android_8()
    # if res:
    #     raise Exception("app is installed but it should not")
    #
    # others.go_back()
    # others.go_back()
    #
    # poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.01)

    # while(1):
    #     if others.check_zsb_app_icon():
    #         t='present'
    #         break
    #     else:
    #         others.scroll_down()
    #
    # if t == 'present':
    #     raise Exception("app present")

