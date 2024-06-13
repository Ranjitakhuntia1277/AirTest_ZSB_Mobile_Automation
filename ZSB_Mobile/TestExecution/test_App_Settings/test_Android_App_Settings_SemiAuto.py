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

"""""""""""""""""""""""Change Password part needs to be verified manually"""""""""""""""""""""""""""""


# #### bug id-SMBM-2773
def test_AppSettings_TestcaseID_47913():
    """Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""

    common_method.tearDown()
    # test_robo_finger()
    # sleep(6)
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
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
    sleep(120)
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
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    """"Verify Printed successfully text"""
    app_settings_page.Verify_Printed_Successfully_Text()
    """"Open the printer cover manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
    """click test print button"""
    app_settings_page.click_Test_Print_Button()
    """""verify error message of cover open"""
    app_settings_page.Verify_ErrorMessage_Text()
    """""Cover close on the printer manually"""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
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
    """"Verify The error message manually if it is displaying"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""
    common_method.Show_popup_For_Error_Message_Manually()
    ### app_settings_page.Verify_The_Invalid_Network_Error_Message()
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

def test_AppSettings_TestcaseID_45688():
    """""""""Verify Wifi Settings"""""

    """""Install the latest production app on the phone & printer should be added and it should be connected to wifi"""""""""
    """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
    #
    # :
    """""Check whether App is installed or not"""
    common_method.tearDown()
    """" Allow pop up before login for the fresh installation"""""
    login_page.click_LoginAllow_Popup()
    """""for the first installation click on the zsb series popup"""
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    """""click on the printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """""click on the printer tab"""
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_General_Tab()
    """"Verify the Test print button text & tab"""
    app_settings_page.Test_Print_button_is_present_on_printer_settings_page()
    """""""""" click on the wifi tab option"""""""""""
    app_settings_page.click_wifi_tab()
    """""""""validate the Current network text"""""
    app_settings_page.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
    """""""Validate the Network status text is present on the printer settings screen"""""""
    app_settings_page.test_Network_Status_Txt_is_present_on_printer_settings_page()
    """"validate network status result text on the printer settings screen"""
    app_settings_page.get_text_Network_Status_Result_Txt()
    """"""""" Verify IP address text is present on the printer settings screen"""""""""
    app_settings_page.get_text_IPAddress_Txt()
    """""""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
    app_settings_page.IS_Present_Save_Network_Message_Txt()
    """""""verify manage networks text is present & clickable"""""""
    app_settings_page.click_Manage_Networks_Btn()
    """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
    app_settings_page.accept_Continue_popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""""""Verify the Cancel button on the Bluetooth_Connection_Failed_Popup"""""
    app_settings_page.Cancel_is_present_on_Bluetooth_Connection_Failed_Popup()
    """"""""""verify the continue button and click on that"""""
    app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    """"""""""Verify the red remove icon next to the network name"""""
    app_settings_page.click_Red_Icon_to_remove_network()
    sleep(5)
    """"""""""Verify the Add Network text & button & click on that"""""""""""
    app_settings_page.click_Add_Network()
    sleep(3)
    """""""""""""Verify Add network page is opening and verify the text"""""""
    app_settings_page.get_text_Add_Network()
    app_settings_page.click_Enter_Network_Manually()
    app_settings_page.click_Network_UserName()
    app_settings_page.click_Join_Btn_On_Other_Network_Popup()
    """""test case 7 to 10 need to check on Web portal manually"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Web_Portal_Verification_Manually()
    """stop the app"""
    common_method.Stop_The_App()

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45876():
    """	Check basic functions work well after upgrading"""


    """"Setup:
    1. The previous version has already been installed in test device
    2. Sign in the test account, with 1 printer added
    3. There is at least one design in My designs"""""

    """start the app"""""
    common_method.tearDown()
    common_method.Stop_The_App()
    # ##common_method.uninstall_app()
    # ##common_method.install_Older_app()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    app_settings_page.Home_text_is_present_on_homepage()
    """""""Verify the Already added Printer"""
    app_settings_page.Verify_Printer_is_already_added()
    common_method.Stop_The_App()
    #### common_method.uninstall_app()
    # ####common_method.install_app()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    app_settings_page.Home_text_is_present_on_homepage()
    app_settings_page.Verify_Printer_is_already_added()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
    add_a_printer_screen.click_FirstOne_In_Common_Design()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.Update_PrinterName_With_Different_Valid_Name()
    app_settings_page.verify_Printer_Name_Updated_Message()
    app_settings_page.click_Printer_Name_Text_Field()
    app_settings_page.Update_PrinterName()
    common_method.Stop_The_App()
    aps_notification.Stop_Android_App()
    aps_notification.click_Mobile_SearchBar()
    aps_notification.click_On_Searchbar2()
    aps_notification.Enter_Files_Text_On_SearchBar()
    aps_notification.click_Files_Folder()
    aps_notification.click_Drive_Searchbar()
    aps_notification.click_Drive_Searchbar2()
    aps_notification.click_PDF_File_From_The_List()
    aps_notification.click_Suggestion_PDF_File()
    aps_notification.click_PDF_ON_Result()
    aps_notification.click_ON_Three_Dot()
    aps_notification.click_Print_Option()
    aps_notification.Verify_Print_Review_Page()
    aps_notification.click_Save_AS_PDF()
    aps_notification.click_All_Printers()
    aps_notification.Verify_Print_job_sent_successfully_Message()
    aps_notification.Stop_Android_App()
    common_method.Start_The_App()
    common_method.Stop_The_App()
    """""The below steps need to be verified manually""""""""""""""
    7. Open printer cover
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
    """Check the status on home page is shown as "Cover Open"""""
    aps_notification.Verify_Printer_Status_AS_HeadOpen()
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
    aps_notification.Verify_Printer_Status_Is_Present()
#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45901():
    """Update Auto label feed setting(disable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.Check_toggle_button()
    """click on the toggle button"""
    app_settings_page.click_toggle_button()
    """stop the app"""
    common_method.Stop_The_App()
    """""""web portal part needs to be verified Manually"""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Web_Portal_Verification_Manually()
# ## #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45882():
    """Verify sign in with non-Zebra account, check the design linked different format file from One Drive can be printed out successfully"""

    common_method.tearDown()
    common_method.Clear_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Loginwith_Google()
    login_page.Loginwith_Added_Email_Id()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.Verify_Design_Preview_Screen_With_Details()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    add_a_printer_screen.click_SecondOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_To_Verify_Printout_Manually()
    common_method.Stop_The_App()
    """""The below step needs to be verified manually"""
    """"""""""2. Sign in the same account on Web portal, create design1, add text object, and link One Drive file with xlsx format. Create design2, add text object, and link One Drive file with csv format"""""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Design_Verification_On_Web_Portal_Manually()

# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#

def test_Smoke_Test_TestcaseID_45885():
    """Add a printer- use a printer which has ever been registered before and require a decommission."""


    """Step 1 needs to be verifiedManually """
    """""1.Turn on the testing printer, wait about 1 min, use a toothpick to press the button on the printer back for about 30s to do a decommission
    Check during this process, the power button is flashing yellow light and then white light, finally turn to blue flashing light and will auto feed the barcode info label. """

    """"decommission the added printer and then execute"""
    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
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
    """"click on finish setup button"""
    add_a_printer_screen.click_Finish_Setup_Button()
    common_method.Stop_The_App()
    common_method.Start_The_App()
    app_settings_page.Verify_Printer_is_already_added()
    """stop the app"""
    common_method.Stop_The_App()
# # ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #

def test_Smoke_Test_TestcaseID_45900():
    """Update Auto label feed setting(enable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """"verify printer is already added"""
    app_settings_page.Verify_Printer_is_already_added()
    """click on the hamburger icon"""
    login_page.click_Menu_HamburgerICN()
    """"click on Printer settings tab"""
    app_settings_page.click_Printer_Settings()
    """"click on printer name on the printer settings page"""
    app_settings_page.click_PrinterName_On_Printersettings()
    """verify general tab text"""
    app_settings_page.Verify_General_Tab_Text()
    """"verify printer name text"""
    app_settings_page.Verify_Printer_Name_Text()
    """verify darkness level bar is present & change the darkness level"""
    app_settings_page.Verify_Darkness_Level_Bar()
    """"change the darkness level"""
    app_settings_page.Change_Darkness_Level_Bar()
    """verify the darkness updated message"""
    app_settings_page.Verify_Darkness_Updated_Message()
    """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
    app_settings_page.Check_toggle_button()
    """click on the toggle button"""
    app_settings_page.click_toggle_button()
    """stop the app"""
    common_method.Stop_The_App()
    """""""web portal part needs to be verified Manually"""""""
    """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
    common_method.Show_popup_For_Darkness_Level_Verification_On_Web_Portal_Manually()
# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""