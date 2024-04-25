from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
from self import self

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from poco import poco
from ZSB_Mobile.Conftest import Conftest
from ZSB_Mobile.PageObject.Robofinger import test_robo_finger
import pytest

class iOS_App_Settings:
    pass




uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")
sleep(5)

# conftest = Conftest(poco)
# conftest.test_conftest()
login_screen_ios = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)


def test_AppSettings_TestcaseID_47913():
    """""Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""
    """start the app"""
    common_method.tearDown_iOS()
    #test_robo_finger()
    sleep(6)
    """"verify home text is displaying on the home screen"""
    app_settings_page_ios.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page_ios.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page_ios.click_Start_Button()
    login_screen_ios.click_Allow_Login_Popup()
    add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
    add_a_printer_page_ios.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page_ios.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page_ios.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page_ios.click_Select_Button_On_Select_Your_Printer_Screen()
    """"verify pairing your printer text"""
    add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    """"verify pairing your printer text"""
    add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_page_ios.Verify_Connect_Wifi_Network_Text()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_page_ios.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
    add_a_printer_page_ios.click_Password_Field_On_Join_Network()
    add_a_printer_page_ios.click_Submit_Button_ON_Join_Network()
    """"verify need the printer driver text"""
    add_a_printer_page_ios.Verify_Need_the_Printer_Driver_Text()
    """""verify registering your printer text"""
    add_a_printer_page_ios.Verify_Registering_your_Printer_Text()
    """"Turn OFF the WIFI & Turn on again after some time (approx. 2 min)"""
    common_method.disable_wifi()
    common_method.enable_wifi()
    sleep(7)
    """"click on finish setup button"""
    add_a_printer_page_ios.click_Finish_Setup_Button()
    """stop the app"""
    common_method.Stop_The_iOSApp()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47924():
    """Verify Should not allow same printer name in all the clients.."""
    """"Account should be having 2 printers"""
#

    """start the app"""
    common_method.tearDown_iOS()
    test_robo_finger()
    sleep(6)
    """"verify home text is displaying on the home screen"""
    app_settings_page_ios.Home_text_is_present_on_homepage()
    """click on the hamburger icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    """"click on Add printer tab"""""
    add_a_printer_page_ios.click_Add_A_Printer()
    """"click on the start button"""
    add_a_printer_page_ios.click_Start_Button()
    login_screen_ios.click_Allow_Login_Popup()
    add_a_printer_page_ios.Verify_Lets_Make_Sure_Text()
    add_a_printer_page_ios.Click_Next_Button()
    """"Verify searching for your printer text"""
    add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
    """"verify select your printer text"""
    add_a_printer_page_ios.Verify_Select_your_printer_Text()
    """"select 2nd printer which you want to add"""
    add_a_printer_page_ios.click_2nd_Printer_Details_To_Add()
    """""click on select button"""
    add_a_printer_page_ios.click_Select_Button_On_Select_Your_Printer_Screen()
    """"verify pairing your printer text"""
    add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    """"verify pairing your printer text"""
    add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    """Verify Connect Wi-fi Network Text"""
    add_a_printer_page_ios.Verify_Connect_Wifi_Network_Text()
    """"click on connect button on connect wifi network screen"""
    add_a_printer_page_ios.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
    add_a_printer_page_ios.click_Password_Field_On_Join_Network()
    add_a_printer_page_ios.click_Submit_Button_ON_Join_Network()
    """"verify need the printer driver text"""
    add_a_printer_page_ios.Verify_Need_the_Printer_Driver_Text()
    """""verify registering your printer text"""
    add_a_printer_page_ios.Verify_Registering_your_Printer_Text()
    """"click on finish setup button"""
    add_a_printer_page_ios.click_Finish_Setup_Button()
    """click on hamburger icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    """click on printer settings tab"""
    app_settings_page_ios.click_Printer_Settings()
    """"scroll till the 3rd printer"""
    app_settings_page_ios.Scroll_Till_Next_Tab()
    """click on printer name on the printer settings page"""""
    app_settings_page_ios.click_PrinterName2_On_Printersettings()
    """click on printr name"""
    app_settings_page_ios.click_Printer_Name_Text_Field()
    """click on printer name text field"""
    app_settings_page_ios.clear_Printer_Name()
    """Rename the Printer Name with a long text (more than 30 characters)"""
    app_settings_page_ios.Rename_PrinterName_With_Same_Name()
    """"click on back icon"""
    app_settings_page_ios.click_Back_Icon()
    """verify printer name update failed message"""
    app_settings_page_ios.Verify_Printer_Name_Update_Failed_Message()
    """click continue button"""""
    app_settings_page_ios.click_Continue_Button_On_Printer_Update_Failed_Popup()
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Printer_Settings()
    """"verify previous printer name is displaying"""
    app_settings_page_ios.click_PrinterName2_On_Printersettings()
    """stop the app"""
    common_method.Stop_The_iOSApp()
### """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_AppSettings_TestcaseID_49709():
    """Manage network- Check able to manage network with long name"""
    """"printer should be online & wifi should be connected"""

    """start the app"""
    common_method.tearDown_iOS()
    """click on hamburger menu icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page_ios.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page_ios.click_wifi_tab()
    app_settings_page_ios.click_Manage_Networks_Btn()
    """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
    app_settings_page_ios.accept_Continue_popup()
    login_screen_ios.click_Allow_Login_Popup()
    """"""""""verify the continue button and click on that"""""
    app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
    sleep(5)
    """"""""""Verify the Add Network text & button & click on that"""""""""""
    app_settings_page_ios.click_Add_Network()
    sleep(3)
    """""""""""""Verify Add network page is opening and verify the text"""""""
    app_settings_page_ios.get_text_Add_Network()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Long_Network_UserName()
    app_settings_page_ios.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page_ios.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
    app_settings_page_ios.Verify_Long_Network_UserName()
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Printer_Settings()
    """"click on the red icon to delete the added network name"""
    app_settings_page_ios.click_Red_Icon_to_remove_network()
    """stop the app"""
    common_method.Stop_The_iOSApp()

##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_49711():
    """Manage networks- Check there is a prompt message when applying to the network which can't resolve Zebra host"""



    """start the app"""
    common_method.tearDown_iOS()
    """click on hamburger menu icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    """"click on printer settings"""
    app_settings_page_ios.click_Printer_Settings()
    """"click on printer name on  printer settings"""
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    """click on wifi tab"""
    app_settings_page_ios.click_wifi_tab()
    app_settings_page_ios.click_Manage_Networks_Btn()
    """"verify bluetooth connection required text"""
    app_settings_page_ios.get_text_Bluetooth_connection_required_Txt()
    app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page_ios.click_Allow_Btn()
    app_settings_page_ios.click_Add_Network()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Long_Network_UserName()
    app_settings_page_ios.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page_ios.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
    app_settings_page_ios.Verify_Long_Network_UserName()
    app_settings_page_ios.click_Apply_Chnages_Button()
    """""Currently there is no error message displaying so Couldnot automate, it is blocked due to SMBM-2163"""""""""""
    app_settings_page_ios.Verify_The_Invalid_Network_Error_Message()
    """stop the app"""
    common_method.Stop_The_iOSApp()

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50326():
    """Manage Network- Check able to add/delete/sort network when printer bt paired/unpaired in device""""""
    
    """"App should be in logged in condition & printer should be added """"
    """"""connect with Another wifi Network except NESTWIFI"""


    """"start the app"""
    common_method.tearDown_iOS()
    """"click on the hamburger icon"""
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Printer_Settings()
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    app_settings_page_ios.click_wifi_tab()
    app_settings_page_ios.click_Manage_Networks_Btn()
    app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    """"accept Bluetooth pairing popup 1"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
    """"accept Bluetooth pairing popup 2"""
    add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
    app_settings_page_ios.click_Add_Network()
    app_settings_page_ios.click_ZEBRA_Network()
    app_settings_page_ios.click_Network_Password_Field()
    app_settings_page_ios.click_Network_Submit_Btn()
    app_settings_page_ios.Verify_NestWIFI_Network_Name_In_Network_List()
    app_settings_page_ios.click_Red_Icon_to_remove_network()
    app_settings_page_ios.Verify_NestWIFI_In_Network_List()
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Home_Tab()
    app_settings_page_ios.Verify_Printer_is_already_added()
    """stop the app"""
    common_method.Stop_The_iOSApp()

# ##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50325():
    """Manage Network-Check able to add/delete/sort network when printer bt paired/unpaired in device"""


    """"App should be in logged in condition & printer should be added """


    """"start the app"""
    common_method.tearDown_iOS()
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Printer_Settings()
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    app_settings_page_ios.click_wifi_tab()
    app_settings_page_ios.click_Manage_Networks_Btn()
    app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
    app_settings_page_ios.click_Add_Network()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Network_UserName()
    app_settings_page_ios.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Network_UserName()
    app_settings_page_ios.click_Security_Open()
    app_settings_page_ios.click_WPA_PSK()
    app_settings_page_ios.click_Keyboard_back_Icon()
    app_settings_page_ios.click_Cancel_Button_On_Other_Network_Popup()
    app_settings_page_ios.click_Enter_Network_Manually()
    app_settings_page_ios.click_Network_UserName()
    app_settings_page_ios.click_Join_Btn_On_Other_Network_Popup()
    app_settings_page_ios.Verify_Added_Network()
    """stop the app"""
    common_method.Stop_The_iOSApp()

###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_47910():
    """""Verify pull-down screen twice then the prints left value can refresh success in home page."""""


    """start the app"""
    common_method.tearDown_iOS()
    sleep(3)
    ### add_a_printer_screen.click_Add_A_Printer()
    app_settings_page_ios.Verify_Printer_is_already_added()
    """take the prvious number of cartridges"""
    previous = app_settings_page_ios.Check_no_of_left_cartridge()
    print(previous)

    """click on navigation option"""
    login_screen_ios.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    app_settings_page_ios.click_Printer_Settings()
    app_settings_page_ios.click_PrinterName_On_Printersettings()
    sleep(2)
    n=2

    """test the printer to print the label"""
    for i in range(n):
        app_settings_page_ios.click_Test_Print_Button()
        sleep(2)

    sleep(1)
    """Go to the Home Page"""
    login_screen_ios.click_Menu_HamburgerICN()
    app_settings_page_ios.click_Home_Tab()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = app_settings_page_ios.Check_no_of_left_cartridge()
    print(after)

    """Check wheather the cartridges are updated or not"""
    res = app_settings_page_ios.check_update_cartridge(previous,after,n)
    if res:
        print("success")
    else:
        print("Failed")
    """stop the app"""
    common_method.Stop_The_iOSApp()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

