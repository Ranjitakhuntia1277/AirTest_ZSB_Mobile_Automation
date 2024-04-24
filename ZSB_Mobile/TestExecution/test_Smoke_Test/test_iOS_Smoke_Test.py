from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
from self import self
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_iOS import App_Settings_Screen_iOS
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_iOS import Login_Screen_iOS
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_iOS import Add_A_Printer_Screen_iOS
from airtest.core.api import *
from poco import poco

from ZSB_Mobile.PageObject.Smoke_Test.Smoke_Test_iOS import Smoke_Test_iOS


class iOS_Smoke_Test:
    pass


# poco = iosPoco()

uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")
sleep(5)

login_screen_ios = Login_Screen_iOS(poco)
app_settings_page_ios = App_Settings_Screen_iOS(poco)
add_a_printer_page_ios = Add_A_Printer_Screen_iOS(poco)
common_method = Common_Method(poco)
smoke_test_ios = Smoke_Test_iOS(poco)

# def test_Smoke_Test_TestcaseID_45875():
#     """	Fresh Install the app with apk/or from Google Store (Android) or from test flight/Apple Store (iOS)."""

# """""Will automate this testcase once we get access to testflight build installation """
# """Freshly install the app"""
# """start the app"""""
# common_method.Start_The_iOSApp()
# common_method.Stop_The_iOSApp()
# common_method.uninstall_iOS_app()
# smoke_test_ios.Open_Test_Flight_App()
# smoke_test_ios.click_New_iOS_Build_In_Test_Flight_App()
# smoke_test_ios.click_Install()
# common_method.Start_The_iOSApp()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Smoke_Test_TestcaseID_45876():
#     """	Check basic functions work well after upgrading"""
#
#
# """"Setup:
# 1. The previous version has already been installed in test device
# 2. Sign in the test account, with 1 printer added
# 3. There is at least one design in My designs"""""
#
# """"Manually verify these below 3 steps as"""
# """start the app"""""
# common_method.Start_The_iOSApp()
# """"Upgrade the app, this needs to be executed manually"""
# """""""Verify the Already added Printer"""
# app_settings_page_ios.Verify_Printer_is_already_added()
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_My_Design()
# add_a_printer_page_ios.click_FirstOne_In_MyDesign()
# add_a_printer_page_ios.click_Print_Option()
# add_a_printer_page_ios.click_Print_Button()
# """"Verify manually it should print successfully"""
# add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
# login_screen_ios.click_Menu_HamburgerICN()
# add_a_printer_page_ios.click_Common_Design_Tab()
# add_a_printer_page_ios.click_FirstOne_Design_In_Common_Design()
# add_a_printer_page_ios.click_FirstOne_In_Common_Design()
# add_a_printer_page_ios.click_Print_Option()
# add_a_printer_page_ios.click_Print_Button()
# """Verify manually it should print successfully"""
# add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
# add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_Printer_Settings()
# app_settings_page_ios.click_PrinterName_On_Printersettings()
# app_settings_page_ios.click_Printer_Name_Text_Field()
# app_settings_page_ios.Update_PrinterName_With_Different_Valid_Name()
# app_settings_page_ios.verify_Printer_Name_Updated_Message()
# app_settings_page_ios.click_PrinterName_On_Printersettings()
# app_settings_page_ios.click_Printer_Name_Text_Field()
# app_settings_page_ios.Update_PrinterName()
# common_method.Stop_The_iOSApp()
# """""The below steps need to be verified manually""""""""""""""
# 6.Open any PDF file, then share to ZSB Series, print the file
# Check the file can be printed out successfully
# 7. Open printer cover
# Check the status on home page is shown as "Cover Open"
# 8. Close the printer cover
# Check the status back to "Online"""""""""
# # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Smoke_Test_TestcaseID_45877():
#     """	Verify create a brand new user with unregistered user in Mobile App."""
#
#
# """"Setup:
# 1. Create a new email address
# (Need to match the new register email format)
# 2. Install the target build of ZSB app on mobile device"""""
#
# """start the app"""""
# common_method.Start_The_iOSApp()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# login_screen_ios.click_Login_With_Email_Tab()
# poco.scroll()
# smoke_test_ios.click_Register_Your_Email_Now_Option()
"""Enter the User Email"""
smoke_test_ios.enter_user_email_for_registering("smbmzsb7@gmail.com")
smoke_test_ios.click_on_next()

try:
    smoke_test_ios.wait_for_element_appearance("Resend Verification Code.", 10)
except:
    raise Exception("Second step dint work")

verification_code = "SLS9820000"
smoke_test_ios.enter_the_verification_code(verification_code)
smoke_test_ios.click_on_next()
sleep(2)
"""Enter the first Name last name and the password"""
first_n = "Zebra"
last_n = "Z"
password = "Zebra#123456789"
smoke_test_ios.enter_the_fields(first_n, last_n, password)
smoke_test_ios.select_the_country("India")
smoke_test_ios.select_the_check_boxes()
smoke_test_ios.click_submit_and_continue()
sleep(2)
smoke_test_ios.check_sign_up_successful()
smoke_test_ios.click_continue_registration_page()
poco("Login").wait_for_appearance(timeout=10)

login_screen_ios.click_loginBtn()
smoke_test_ios.wait_for_element_appearance_text("Continue with Google", 20)
smoke_test_ios.signInWithEmail()
"""Provide the email and password"""
email = "zebra852@gmail.com"
password = "Zebra#123456789"
smoke_test_ios.complete_sign_in_with_email(email, password)
try:
    smoke_test_ios.wait_for_element_appearance("Home", 20)
except:
    raise Exception("home page dint show up")

login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
try:
    smoke_test_ios.wait_for_element_appearance("Login", 5)
except:
    raise Exception("Did not redirect to the login page")
login_screen_ios.click_loginBtn()
login_screen_ios.click_Continue_Btn_To_Login()
login_screen_ios.click_Loginwith_Google()
common_method.Stop_The_iOSApp()


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45878():
    """	Verify sign in as zebra, check link and delete one/google drive file works well"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
smoke_test_ios.click_MyData_Tab()
smoke_test_ios.click_Plus_icon()
smoke_test_ios.click_LinkFile()
smoke_test_ios.click_SignIn_With_Microsoft()
smoke_test_ios.Upload_Files()
smoke_test_ios.Verify_Uploaded_Files()
smoke_test_ios.Click_Delete_File()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
login_screen_ios.click_loginBtn()
login_screen_ios.click_LoginAllow_Popup()
login_screen_ios.click_Loginwith_Google()
common_method.Stop_The_iOSApp()


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45879():
    """Verify sign in as non-zebra, check link and delete one/google drive file works well"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
login_screen_ios.click_loginBtn()
login_screen_ios.click_Login_With_Email_Tab()
login_screen_ios.click_UserName_TextField()
login_screen_ios.Enter_Zebra_UserName()
login_screen_ios.click_Password_TextField()
login_screen_ios.Enter_Zebra_Password()
app_settings_page_ios.click_Keyboard_back_Icon()
login_screen_ios.click_SignIn_Button()
login_screen_ios.click_Menu_HamburgerICN()
smoke_test_ios.click_MyData_Tab()
smoke_test_ios.click_Plus_icon()
smoke_test_ios.click_LinkFile()
smoke_test_ios.click_SignIn_With_Microsoft()
smoke_test_ios.Upload_Files()
smoke_test_ios.Verify_Uploaded_Files()
smoke_test_ios.Click_Delete_File()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
login_screen_ios.click_loginBtn()
login_screen_ios.click_LoginAllow_Popup()
login_screen_ios.click_Loginwith_Google()
common_method.Stop_The_iOSApp()


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45880():
    """Verify sign in with non-zebra account, check the design linked different format file from local can be printed out successfully"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_My_Design()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
add_a_printer_page_ios.click_SecondOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
common_method.Stop_The_iOSApp()


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45881():
    """Verify sign in with social account, check the design linked different format file from Google Drive can be printed out successfully"""


"""start the app"""
common_method.Start_The_iOSApp()
sleep(3)
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
login_screen_ios.click_loginBtn()
login_screen_ios.click_LoginAllow_Popup()
"""""""""" check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy")"""""""""""
smoke_test_ios.Verify_SignIn_With_Text_Is_Present()
smoke_test_ios.click_Continue_With_Facebook_Option()
"""""due to some issue, it is directly login to the facebook account without asking for password"""
login_screen_ios.click_Menu_HamburgerICN()
smoke_test_ios.Verify_Facebook_UserName_Is_Displaying()
app_settings_page_ios.click_My_Design()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
add_a_printer_page_ios.click_SecondOne_In_MyDesign()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
""""Verify manually it should print successfully"""
common_method.Stop_The_App()
common_method.Start_The_App()
sleep(3)
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_pen_Icon_near_UserName()
app_settings_page_ios.Scroll_till_Delete_Account()
app_settings_page_ios.click_Logout_Btn()
login_screen_ios.click_loginBtn()
login_screen_ios.click_LoginAllow_Popup()
login_screen_ios.click_Loginwith_Google()
common_method.Stop_The_iOSApp()


## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# def test_Smoke_Test_TestcaseID_45882():
#     """Verify sign in with non-Zebra account, check the design linked different format file from One Drive can be printed out successfully"""
#
#
# common_method.Start_The_iOSApp()
# login_screen_ios.click_Menu_HamburgerICN()
# app_settings_page_ios.click_My_Design()
# app_settings_page_ios.click_My_Design()
# add_a_printer_page_ios.click_FirstOne_In_MyDesign()
# add_a_printer_page_ios.click_Print_Option()
# add_a_printer_page_ios.Verify_Design_Preview_Screen_With_Details()
# add_a_printer_page_ios.click_Print_Button()
# """"Verify manually it should print successfully"""
# add_a_printer_page_ios.click_The_Back_Icon_Of_Print_Review_Screen()
# add_a_printer_page_ios.click_SecondOne_In_MyDesign()
# add_a_printer_page_ios.click_Print_Option()
# add_a_printer_page_ios.click_Print_Button()
# """"Verify manually it should print successfully"""
# common_method.Stop_The_iOSApp()
# """""The below step needs to be verified manually"""
# """"""""""2. Sign in the same account on Web portal, create design1, add text object, and link One Drive file with xlsx format. Create design2, add text object, and link One Drive file with csv format"""""""""
#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Smoke_Test_TestcaseID_45883():
#     """Verify sign in sign out with registered social accounts in Mobile App."""
#
# """start the app"""
# common_method.Start_The_iOSApp()
# sleep(3)
# # login_screen_ios.click_Menu_HamburgerICN()
# # app_settings_page_ios.click_pen_Icon_near_UserName()
# # app_settings_page_ios.Scroll_till_Delete_Account()
# # app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# """""""""" check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy")"""""""""""
# smoke_test_ios.Verify_SignIn_With_Text_Is_Present()
# smoke_test_ios.click_Continue_With_Facebook_Option()
# """""due to some issue, it is directly login to the facebook account without asking for password"""
# login_screen_ios.click_Menu_HamburgerICN()
# smoke_test_ios.Verify_Facebook_UserName_Is_Displaying()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# smoke_test_ios.click_Continue_With_Apple_Option()
# smoke_test_ios.click_Continue_With_Password_ForApple_Login()
# smoke_test_ios.click_On_Password_Textfield()
# poco(text("Testing@123"))
# smoke_test_ios.click_On_Sign_In_Option()
# login_screen_ios.click_Menu_HamburgerICN()
# smoke_test_ios.Verify_Apple_UserName_Is_Displaying()
# app_settings_page_ios.click_pen_Icon_near_UserName()
# app_settings_page_ios.Scroll_till_Delete_Account()
# app_settings_page_ios.click_Logout_Btn()
# login_screen_ios.click_loginBtn()
# login_screen_ios.click_Continue_Btn_To_Login()
# login_screen_ios.click_Loginwith_Google()
# smoke_test_ios.Verify_Google_UserName_Is_Displaying()
# common_method.Stop_The_iOSApp()

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# def test_Smoke_Test_TestcaseID_45884():
#     """Add a printer- Out of the box user experience"""
#
#
# """""Test steps:
# 1. Turn off the testing printer, then use a toothpick to press the button on the printer back for about 10s, turn on the printer(Keep hold pressing the printer back button for about 20s)
# Check during this process, the power button is flashing white light, then flashing blue light and will auto feed the barcode info label. """""""""""
#
# """start the app"""
# common_method.Start_The_iOSApp()
# sleep(3)
# """"verify home text is displaying on the home screen"""
# app_settings_page_ios.Home_text_is_present_on_homepage()
# """click on the hamburger icon"""
# login_screen_ios.click_Menu_HamburgerICN()
# """"click on Add printer tab"""""
# add_a_printer_page_ios.click_Add_A_Printer()
# """"click on the start button"""
# add_a_printer_page_ios.click_Start_Button()
# """"Verify searching for your printer text"""
# add_a_printer_page_ios.Verify_Searching_for_your_printer_Text()
# """"verify select your printer text"""
# add_a_printer_page_ios.Verify_Select_your_printer_Text()
# """"select 2nd printer which you want to add"""
# add_a_printer_page_ios.click_2nd_Printer_Details_To_Add()
# """""click on select button"""
# add_a_printer_page_ios.click_Select_Button_On_Select_Your_Printer_Screen()
# """"verify pairing your printer text"""
# add_a_printer_page_ios.Verify_Pairing_Your_Printer_Text()
# """"accept Bluetooth pairing popup 1"""
# add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup1()
# """"accept Bluetooth pairing popup 2"""
# add_a_printer_page_ios.Accept_Bluetooth_pairing_Popup2()
# """Verify Connect Wi-fi Network Text"""
# add_a_printer_page_ios.Verify_Connect_Wifi_Network_Text()
# """"click on connect button on connect wifi network screen"""
# add_a_printer_page_ios.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
# """""""click password field on join network"""
# add_a_printer_page_ios.click_Password_Field_On_Join_Network()
# """"click submit button on join network"""
# add_a_printer_page_ios.click_Submit_Button_ON_Join_Network()
# """verify connecting to wifi network text"""
# add_a_printer_page_ios.Verify_Connecting_to_WiFi_Network_Text()
# """"verify need the printer driver text"""
# add_a_printer_page_ios.Verify_Need_the_Printer_Driver_Text()
# """""verify registering your printer text"""
# add_a_printer_page_ios.Verify_Registering_your_Printer_Text()
# """"click on finish setup button"""
# add_a_printer_page_ios.click_Finish_Setup_Button()
# app_settings_page_ios.Verify_Printer_is_already_added()
# """stop the app"""
# common_method.Stop_The_iOSApp()

## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45885():
    """Add a printer- use a printer which has ever been registered before and require a decommission."""


"""Step 1 needs to be verifiedManually """
"""""1.Turn on the testing printer, wait about 1 min, use a toothpick to press the button on the printer back for about 30s to do a decommission
Check during this process, the power button is flashing yellow light and then white light, finally turn to blue flashing light and will auto feed the barcode info label. """

common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Add_A_Printer()
add_a_printer_page_ios.click_Start_Button()
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
"""Verify Connect Wi-fi Network Text"""
add_a_printer_page_ios.Verify_Connect_Wifi_Network_Text()
""""click on connect button on connect wifi network screen"""
add_a_printer_page_ios.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
"""""""click password field on join network"""
add_a_printer_page_ios.click_Password_Field_On_Join_Network()
""""click submit button on join network"""
add_a_printer_page_ios.click_Submit_Button_ON_Join_Network()
"""verify connecting to wifi network text"""
add_a_printer_page_ios.Verify_Connecting_to_WiFi_Network_Text()
""""verify need the printer driver text"""
add_a_printer_page_ios.Verify_Need_the_Printer_Driver_Text()
"""""verify registering your printer text"""
add_a_printer_page_ios.Verify_Registering_your_Printer_Text()
""""click on finish setup button"""
add_a_printer_page_ios.click_Finish_Setup_Button()
app_settings_page_ios.Verify_Printer_is_already_added()
"""stop the app"""
common_method.Stop_The_iOSApp()


## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45886():
    """Check Mobile App can display correct printer status and notifications when printer status updates"""


common_method.Start_The_iOSApp()
res = smoke_test_ios.check_printer_online_status()
if res == "Online":
    print("ok")
else:
    raise Exception("Printer is not in Online state")

smoke_test_ios.select_first_label_from_home()
smoke_test_ios.click_print_button()
sleep(3)
smoke_test_ios.check_error_print_preview()

smoke_test_ios.click_print_button()
sleep(4)
smoke_test_ios.click_left_arrow()

res = smoke_test_ios.check_printer_online_status()
if res == "Cover Open":
    print("ok")
else:
    raise Exception("Printer is not in Cover Open state")
common_method.Start_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45887():
    """	User modify the printer's darkness setting and perform test print"""


"""start the app"""
common_method.Start_The_iOSApp()
sleep(3)
""""verify printer is already added"""
app_settings_page_ios.Verify_Printer_is_already_added()
"""click on the hamburger icon"""
login_screen_ios.click_Menu_HamburgerICN()
""""click on Printer settings tab"""
app_settings_page_ios.click_Printer_Settings()
""""click on printer name on the printer settings page"""
app_settings_page_ios.click_PrinterName_On_Printersettings()
"""verify general tab text"""
app_settings_page_ios.Verify_General_Tab_Text()
""""verify printer name text"""
app_settings_page_ios.Verify_Printer_Name_Text()
"""verify darkness level bar is present & change the darkness level"""
app_settings_page_ios.Verify_Darkness_Level_Bar()
""""change the darkness level"""
app_settings_page_ios.Change_Darkness_Level_Bar()
"""verify the darkness updated message"""
app_settings_page_ios.Verify_Darkness_Updated_Message()
"""Verify auto Label Feed On Printer Cover Close value enable/disable option"""
app_settings_page_ios.Check_toggle_button()
"""click on the toggle button"""
app_settings_page_ios.click_toggle_button()
""""stop the app"""
common_method.Stop_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45888():
    """	Check user can delete a printer from Mobile App"""


"""start the app"""
common_method.Start_The_iOSApp()
""""verify home text is displaying on the home screen"""
app_settings_page_ios.Home_text_is_present_on_homepage()
"""click on three dot on added printer on home page"""
app_settings_page_ios.click_Three_Dot_On_Added_Printer_On_HomePage()
"""""click on delete printer button"""
app_settings_page_ios.click_Delete_Printer_Button()
""""verify final delete printer text"""
app_settings_page_ios.Verify_Final_Delete_Printer_Text()
"""verify delete printer page"""
app_settings_page_ios.Verify_Delete_Printer_Page()
""""click delete printer button"""
app_settings_page_ios.click_Delete_Printer_Button()
""""click yes delete button"""
app_settings_page_ios.click_Yes_Delete_Button()
"""click on unpair bluetooth dropdown list"""""
app_settings_page_ios.Verify_And_click_Unpair_Bluetooth_dropdown_list()
""""verify UI of unpair bluetooth dropdown list """
app_settings_page_ios.Verify_UI_Of_Unpair_Bluetooth_dropdown_list()
""""stop the app"""
common_method.Stop_The_iOSApp()


## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45889():
    """	Check user can upload or link file to My Data"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()

"""Click My Data"""

smoke_test_ios.click_My_Data()
sleep(2)
smoke_test_ios.click_Add_File()
sleep(2)
smoke_test_ios.click_Link_File()
sleep(2)
"""Test for Google Drive"""
smoke_test_ios.clickGoogleDrive()
sleep(2)
smoke_test_ios.checkFilesShownAreSupported()
sleep(2)
large_file = smoke_test_ios.selectLargeFile()
sleep(2)
smoke_test_ios.click_Add_File()
sleep(2)
smoke_test_ios.click_Link_File()
sleep(2)
smoke_test_ios.clickGoogleDrive()
"""Upload a file"""
existing_file = smoke_test_ios.selectExistingFile()
sleep(5)
smoke_test_ios.click_Add_File()
sleep(2)
smoke_test_ios.click_Link_File()
sleep(2)
smoke_test_ios.clickGoogleDrive()
common_method.Stop_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45890():
    """	Print template with static information in Recently Printed Template list"""


common_method.Start_The_iOSApp()
"""take the prvious number of cartridges"""
previous = app_settings_page_ios.Check_no_of_left_cartridge()
print(previous)

"""click on navigation option"""
login_screen_ios.click_Menu_HamburgerICN()

"""Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
app_settings_page_ios.click_Printer_Settings()
app_settings_page_ios.click_PrinterName_On_Printersettings()
sleep(2)
n = 2

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
res = app_settings_page_ios.check_update_cartridge(previous, after, n)
if res:
    print("success")
else:
    print("Failed")
common_method.Stop_The_iOSApp()


# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45891():
    """	Print multiple copies of template with variable data in Workspace"""


common_method.Start_The_iOSApp()
app_settings_page_ios.click_Firstone_In_Recently_Prtinted_Label()
smoke_test_ios.click_Print_Button()
smoke_test_ios.click_On_Copies_Filed()
smoke_test_ios.clear_Copies_Field()
smoke_test_ios.Add_Multiple_Copies_Number()
smoke_test_ios.click_Second_Print_Button()
app_settings_page_ios.click_Keyboard_back_Icon()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_Home_Tab()
previous = app_settings_page_ios.Check_no_of_left_cartridge()
print(previous)

"""click on navigation option"""
login_screen_ios.click_Menu_HamburgerICN()

"""Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
app_settings_page_ios.click_Printer_Settings()
app_settings_page_ios.click_PrinterName_On_Printersettings()
sleep(2)
n = 2

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
res = app_settings_page_ios.check_update_cartridge(previous, after, n)
if res:
    print("success")
else:
    print("Failed")
common_method.Stop_The_iOSApp()


# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45900():
    """Update Auto label feed setting(enable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""


"""start the app"""
common_method.Start_The_iOSApp()
sleep(3)
""""verify printer is already added"""
app_settings_page_ios.Verify_Printer_is_already_added()
"""click on the hamburger icon"""
login_screen_ios.click_Menu_HamburgerICN()
""""click on Printer settings tab"""
app_settings_page_ios.click_Printer_Settings()
""""click on printer name on the printer settings page"""
app_settings_page_ios.click_PrinterName_On_Printersettings()
"""verify general tab text"""
app_settings_page_ios.Verify_General_Tab_Text()
""""verify printer name text"""
app_settings_page_ios.Verify_Printer_Name_Text()
"""verify darkness level bar is present & change the darkness level"""
app_settings_page_ios.Verify_Darkness_Level_Bar()
""""change the darkness level"""
app_settings_page_ios.Change_Darkness_Level_Bar()
"""verify the darkness updated message"""
app_settings_page_ios.Verify_Darkness_Updated_Message()
"""Verify auto Label Feed On Printer Cover Close value enable/disable option"""
app_settings_page_ios.Check_toggle_button()
"""click on the toggle button"""
app_settings_page_ios.click_toggle_button()
""""stop the app"""
common_method.Stop_The_iOSApp()
"""""""web portal part needs to be verified Manually"""""""
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45892():
    """	Delete template in Workspace"""


""""Setup:
1. There is an existing template in My Designs."""""

common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_My_Design()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
smoke_test_ios.click_Delete_Button_On_MyDesign()
smoke_test_ios.click_Cancel_Button_On_Delete_Popup()
add_a_printer_page_ios.click_FirstOne_In_MyDesign()
smoke_test_ios.click_Delete_Button_On_MyDesign()
smoke_test_ios.Click_Delete_Button_On_Delete_Popup()
smoke_test_ios.Verify_Deleted_Successfully_Message()
common_method.Stop_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45893():
    """	To Verify View Zebra defined categories in Common Designs"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Common_Design_Tab()
smoke_test_ios.Verify_List_Is_Sorted_From_A_TO_Z()
smoke_test_ios.Verify_Address_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Barcodes_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Jewelry_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Multipurpose_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Shipping_Header_And_Description_IS_Present()
smoke_test_ios.Verify_ReturnAddress_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Round_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Shipping_Header_And_Description_IS_Present()
smoke_test_ios.Verify_SmallMultipurpose_Header_And_Description_IS_Present()
smoke_test_ios.Verify_XLShipping_Header_And_Description_IS_Present()
common_method.Stop_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45894():
    """	View list of Zebra templates in Common Designs"""


common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Common_Design_Tab()
smoke_test_ios.Verify_Address_Header_And_Description_IS_Present()
add_a_printer_page_ios.click_FirstOne_In_Common_Design()
smoke_test_ios.click_Back_Icon_On_Address_Screen()
smoke_test_ios.Verify_Common_Design_Page_Is_Displaying()
smoke_test_ios.Verify_List_Is_Sorted_From_A_TO_Z()
smoke_test_ios.Verify_Address_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Barcodes_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Jewelry_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Multipurpose_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Postage_Header_And_Description_IS_Present()
smoke_test_ios.Verify_ReturnAddress_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Round_Header_And_Description_IS_Present()
smoke_test_ios.Verify_Shipping_Header_And_Description_IS_Present()
smoke_test_ios.Verify_SmallMultipurpose_Header_And_Description_IS_Present()
smoke_test_ios.Verify_XLShipping_Header_And_Description_IS_Present()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Common_Design_Tab()
add_a_printer_page_ios.click_FirstOne_In_Common_Design()
smoke_test_ios.Verify_Copy_To_My_Design_Text_Is_Present()
smoke_test_ios.click_Back_Icon_On_Address_Screen()
smoke_test_ios.Verify_Common_Design_Page_Is_Displaying()
common_method.Stop_The_iOSApp()


# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45895():
    """Print Zebra templates after Copy the template which needs to upload a picture from Library to Workspace (eg: Address->AddressWithIcon; Small Multipurpose->pickImage)"""


common_method.Start_The_iOSApp()
"""take the prvious number of cartridges"""
previous = app_settings_page_ios.Check_no_of_left_cartridge()
print(previous)

"""click on navigation option"""
login_screen_ios.click_Menu_HamburgerICN()

"""Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
app_settings_page_ios.click_Printer_Settings()
app_settings_page_ios.click_PrinterName_On_Printersettings()
sleep(2)
n = 2

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
res = app_settings_page_ios.check_update_cartridge(previous, after, n)
if res:
    print("success")
else:
    print("Failed")
common_method.Stop_The_iOSApp()

# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45896():
    """Print a label from Common Design."""

common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
add_a_printer_page_ios.click_Common_Design_Tab()
add_a_printer_page_ios.click_FirstOne_Design_In_Common_Design()
add_a_printer_page_ios.click_FirstOne_In_Common_Design()
add_a_printer_page_ios.click_Print_Option()
add_a_printer_page_ios.click_Print_Button()
"""Verify manually it should print successfully"""
""""point 4 is blocked due to SMB-1664"""""
common_method.Stop_The_iOSApp()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45897():
    """Adding New network: Add Essids by using another phone."""

common_method.Start_The_iOSApp()
login_screen_ios.click_Menu_HamburgerICN()
app_settings_page_ios.click_Printer_Settings()
app_settings_page_ios.click_PrinterName_On_Printersettings()
app_settings_page_ios.click_wifi_tab()

"""""""""validate the Current network text"""""
app_settings_page_ios.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
"""""""Validate the Network status text is present on the printer settings screen"""""""
app_settings_page_ios.test_Network_Status_Txt_is_present_on_printer_settings_page()
""""validate network status result text on the printer settings screen"""
app_settings_page_ios.get_text_Network_Status_Result_Txt()
""""" Verify IP address text is present on the printer settings screen"""""
app_settings_page_ios.get_text_IPAddress_Txt()
"""""""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
app_settings_page_ios.IS_Present_Save_Network_Message_Txt()
"""""""verify manage networks text is present & clickable"""""""
sleep(2)
app_settings_page_ios.click_Manage_Networks_Btn()
sleep(2)
app_settings_page_ios.click_Manage_Networks_Btn()
app_settings_page_ios.click_Continue_Btn_on_Bluetooth_Connection_Required()
app_settings_page_ios.click_Add_Network()
app_settings_page_ios.get_text_Add_Network()
app_settings_page_ios.click_Enter_Network_Manually()
app_settings_page_ios.click_Network_UserName()
app_settings_page_ios.click_Cancel_Button_On_Other_Network_Popup()
app_settings_page_ios.click_Enter_Network_Manually()
app_settings_page_ios.click_Network_UserName()
app_settings_page_ios.click_Security_Open()
app_settings_page_ios.click_WPA_PSK()
###app_settings_page_ios.Click_Enter_Password()
app_settings_page_ios.click_Keyboard_back_Icon()
app_settings_page_ios.click_Cancel_Button_On_Other_Network_Popup()
app_settings_page_ios.click_Enter_Network_Manually()
app_settings_page_ios.click_Network_UserName()
app_settings_page_ios.click_Join_Btn_On_Other_Network_Popup()
app_settings_page_ios.Verify_Added_Network()
common_method.Stop_The_iOSApp()
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# # """""" Could not Automate Test casde ID 45898 & 45899, Needs to be verified Manually"""""""""""""""""""""
def test_Smoke_Test_TestcaseID_45901():
    """Update Auto label feed setting(disable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""


"""start the app"""
common_method.Start_The_iOSApp()
sleep(3)
""""verify printer is already added"""
app_settings_page_ios.Verify_Printer_is_already_added()
"""click on the hamburger icon"""
login_screen_ios.click_Menu_HamburgerICN()
""""click on Printer settings tab"""
app_settings_page_ios.click_Printer_Settings()
""""click on printer name on the printer settings page"""
app_settings_page_ios.click_PrinterName_On_Printersettings()
"""verify general tab text"""
app_settings_page_ios.Verify_General_Tab_Text()
""""verify printer name text"""
app_settings_page_ios.Verify_Printer_Name_Text()
"""verify darkness level bar is present & change the darkness level"""
app_settings_page_ios.Verify_Darkness_Level_Bar()
""""change the darkness level"""
app_settings_page_ios.Change_Darkness_Level_Bar()
"""verify the darkness updated message"""
app_settings_page_ios.Verify_Darkness_Updated_Message()
"""Verify auto Label Feed On Printer Cover Close value enable/disable option"""
app_settings_page_ios.Check_toggle_button()
"""click on the toggle button"""
app_settings_page_ios.click_toggle_button()
""""stop the app"""
common_method.Stop_The_iOSApp()
"""""""web portal part needs to be verified Manually"""""""
# #""""""""""""""""""""""""""""""""""End"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

