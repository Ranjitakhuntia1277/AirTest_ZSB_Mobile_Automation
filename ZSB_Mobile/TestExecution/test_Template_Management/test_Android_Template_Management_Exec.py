"""New merged Code"""

# import sys
# sys.path.append(r'C:\Users\tr5927\Desktop\ZSB_Automation')

import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
# from ...PageObject.Login_Screen import *
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.Template_Management.Template_Management_Android import Template_Management_Android

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
# start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
smoke_test_android = Smoke_Test_Android(poco)
aps_notification = APS_Notification(poco)

from ...TestExecution.test_Template_Management.test_Android_Template_Management import test_Android_Template_Management

tm_a = test_Android_Template_Management()


def test_Template_Management_TestcaseID_46006():
    tm_a.test_Template_Management_TestcaseID_46006()


def test_Template_Management_TestcaseID_46007():
    tm_a.test_Template_Management_TestcaseID_46007()


def test_Template_Management_TestcaseID_46008():
    tm_a.test_Template_Management_TestcaseID_46008()


def test_Template_Management_TestcaseID_46009():
    tm_a.test_Template_Management_TestcaseID_46009()


def test_Template_Management_TestcaseID_46011():
    tm_a.test_Template_Management_TestcaseID_46011()


def test_Template_Management_TestcaseID_46012():
    tm_a.test_Template_Management_TestcaseID_46012()


def test_Template_Management_TestcaseID_46013():
    tm_a.test_Template_Management_TestcaseID_46013()


def test_Template_Management_TestcaseID_45964():
    tm_a.test_Template_Management_TestcaseID_45964()


def test_Template_Management_TestcaseID_45969():
    tm_a.test_Template_Management_TestcaseID_45969()


def test_Template_Management_TestcaseID_45970():
    tm_a.test_Template_Management_TestcaseID_45970()


def test_Template_Management_TestcaseID_45971():
    tm_a.test_Template_Management_TestcaseID_45971()


def test_Template_Management_TestcaseID_45972():
    tm_a.test_Template_Management_TestcaseID_45972()


def test_Template_Management_TestcaseID_45973():
    tm_a.test_Template_Management_TestcaseID_45973()


def test_Template_Management_TestcaseID_45974():
    tm_a.test_Template_Management_TestcaseID_45974()


def test_Template_Management_TestcaseID_45975():
    tm_a.test_Template_Management_TestcaseID_45975()


def test_Template_Management_TestcaseID_45930():
    tm_a.test_Template_Management_TestcaseID_45930()


def test_Template_Management_TestcaseID_45933():
    tm_a.test_Template_Management_TestcaseID_45933()


def test_Template_Management_TestcaseID_45967():
    tm_a.test_Template_Management_TestcaseID_45967()


def test_Template_Management_TestcaseID_45968():
    tm_a.test_Template_Management_TestcaseID_45968()


def test_Template_Management_TestcaseID_45926():
    tm_a.test_Template_Management_TestcaseID_45926()


def test_Template_Management_TestcaseID_45927():
    tm_a.test_Template_Management_TestcaseID_45927()


def test_Template_Management_TestcaseID_45929():
    tm_a.test_Template_Management_TestcaseID_45929()


def test_Template_Management_TestcaseID_45931():
    tm_a.test_Template_Management_TestcaseID_45931()


def test_Template_Management_TestcaseID_45934():
    tm_a.test_Template_Management_TestcaseID_45934()


def test_Template_Management_TestcaseID_45935():
    tm_a.test_Template_Management_TestcaseID_45935()


def test_Template_Management_TestcaseID_45936():
    tm_a.test_Template_Management_TestcaseID_45936()


def test_Template_Management_TestcaseID_45928():
    tm_a.test_Template_Management_TestcaseID_45928()


def test_Template_Management_TestcaseID_45937():
    tm_a.test_Template_Management_TestcaseID_45937()


def test_Template_Management_TestcaseID_45938():
    tm_a.test_Template_Management_TestcaseID_45938()


def test_Template_Management_TestcaseID_45939():
    tm_a.test_Template_Management_TestcaseID_45939()


def test_Template_Management_TestcaseID_45940():
    tm_a.test_Template_Management_TestcaseID_45940()


def test_Template_Management_TestcaseID_45941():
    tm_a.test_Template_Management_TestcaseID_45941()


def test_Template_Management_TestcaseID_45957():
    tm_a.test_Template_Management_TestcaseID_45957()


def test_Template_Management_TestcaseID_45958():
    tm_a.test_Template_Management_TestcaseID_45958()


def test_Template_Management_TestcaseID_45959():
    tm_a.test_Template_Management_TestcaseID_45959()


def test_Template_Management_TestcaseID_45961():
    tm_a.test_Template_Management_TestcaseID_45961()


def test_Template_Management_TestcaseID_45995():
    tm_a.test_Template_Management_TestcaseID_45995()


def test_Template_Management_TestcaseID_45996():
    tm_a.test_Template_Management_TestcaseID_45996()


def test_Template_Management_TestcaseID_45997():
    tm_a.test_Template_Management_TestcaseID_45997()


def test_Template_Management_TestcaseID_45998():
    tm_a.test_Template_Management_TestcaseID_45998()


def test_Template_Management_TestcaseID_45999():
    tm_a.test_Template_Management_TestcaseID_45999()


def test_Template_Management_TestcaseID_46000():
    tm_a.test_Template_Management_TestcaseID_46000()


def test_Template_Management_TestcaseID_46001():
    tm_a.test_Template_Management_TestcaseID_46001()


def test_Template_Management_TestcaseID_46002():
    tm_a.test_Template_Management_TestcaseID_46002()


def test_Template_Management_TestcaseID_46003():
    tm_a.test_Template_Management_TestcaseID_46003()


def test_Template_Management_TestcaseID_46004():
    tm_a.test_Template_Management_TestcaseID_46004()


def test_Template_Management_TestcaseID_45976():
    tm_a.test_Template_Management_TestcaseID_45976()


def test_Template_Management_TestcaseID_45977():
    tm_a.test_Template_Management_TestcaseID_45977()


def test_Template_Management_TestcaseID_45942():
    tm_a.test_Template_Management_TestcaseID_45942()


def test_Template_Management_TestcaseID_45943():
    tm_a.test_Template_Management_TestcaseID_45943()


def test_Template_Management_TestcaseID_45944():
    tm_a.test_Template_Management_TestcaseID_45944()


def test_Template_Management_TestcaseID_45945():
    tm_a.test_Template_Management_TestcaseID_45945()


def test_Template_Management_TestcaseID_45946():
    tm_a.test_Template_Management_TestcaseID_45946()


def test_Template_Management_TestcaseID_45947():
    tm_a.test_Template_Management_TestcaseID_45947()


def test_Template_Management_TestcaseID_45948():
    tm_a.test_Template_Management_TestcaseID_45948()


def test_Template_Management_TestcaseID_45949():
    tm_a.test_Template_Management_TestcaseID_45949()


def test_Template_Management_TestcaseID_45950():
    tm_a.test_Template_Management_TestcaseID_45950()


def test_Template_Management_TestcaseID_45951():
    tm_a.test_Template_Management_TestcaseID_45951()


def test_Template_Management_TestcaseID_45952():
    tm_a.test_Template_Management_TestcaseID_45952()


def test_Template_Management_TestcaseID_45955():
    tm_a.test_Template_Management_TestcaseID_45955()


def test_Template_Management_TestcaseID_45956():
    tm_a.test_Template_Management_TestcaseID_45956()


def test_Template_Management_TestcaseID_45902():
    tm_a.test_Template_Management_TestcaseID_45902()


def test_Template_Management_TestcaseID_45903():
    tm_a.test_Template_Management_TestcaseID_45903()


def test_Template_Management_TestcaseID_45905():
    tm_a.test_Template_Management_TestcaseID_45905()


def test_Template_Management_TestcaseID_45906():
    tm_a.test_Template_Management_TestcaseID_45906()


def test_Template_Management_TestcaseID_45907():
    tm_a.test_Template_Management_TestcaseID_45907()


def test_Template_Management_TestcaseID_45909():
    tm_a.test_Template_Management_TestcaseID_45909()


def test_Template_Management_TestcaseID_45910():
    tm_a.test_Template_Management_TestcaseID_45910()


def test_Template_Management_TestcaseID_45911():
    tm_a.test_Template_Management_TestcaseID_45911()


def test_Template_Management_TestcaseID_45912():
    tm_a.test_Template_Management_TestcaseID_45912()


def test_Template_Management_TestcaseID_45913():
    tm_a.test_Template_Management_TestcaseID_45913()


def test_Template_Management_TestcaseID_45914():
    tm_a.test_Template_Management_TestcaseID_45914()


def test_Template_Management_TestcaseID_45915():
    tm_a.test_Template_Management_TestcaseID_45915()


def test_Template_Management_TestcaseID_45916():
    tm_a.test_Template_Management_TestcaseID_45916()


def test_Template_Management_TestcaseID_45919():
    tm_a.test_Template_Management_TestcaseID_45919()


def test_Template_Management_TestcaseID_45920():
    tm_a.test_Template_Management_TestcaseID_45920()


def test_Template_Management_TestcaseID_45923():
    tm_a.test_Template_Management_TestcaseID_45923()


def test_Template_Management_TestcaseID_45924():
    tm_a.test_Template_Management_TestcaseID_45924()


def test_Template_Management_TestcaseID_45904():
    tm_a.test_Template_Management_TestcaseID_45904()


def test_Template_Management_TestcaseID_45932():
    tm_a.test_Template_Management_TestcaseID_45932()


"""Ranjita code"""


def test_Smoke_Test_TestcaseID_45880():
    """Verify sign in with non-zebra account, check the design linked different format file from local can be printed out successfully"""

    #
    """""Sign in the same account on Web portal, create design1, add text object, and link Local file with csv format.
    Create design2, add text object, and link local file with xlsx format"""

    common_method.tearDown()
    data_sources_page.log_out_of_account()
    common_method.Clear_App()
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    registration_page.click_Google_Icon()
    login_page.Loginwith_Added_Email_Id()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    """"Verify manually it should print successfully"""
    sleep(5)
    data_sources_page.clickBackArrow()
    add_a_printer_screen.click_SecondOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


# #
# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45890():
    """	Print template with static information in Recently Printed Template list"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)

    """click on navigation option"""
    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    sleep(2)
    n = 2

    """test the printer to print the label"""
    for i in range(n):
        app_settings_page.click_Test_Print_Button()
        sleep(2)

    sleep(1)
    """Go to the Home Page"""
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)

    """Check wheather the cartridges are updated or not"""
    res = app_settings_page.check_update_cartridge(previous, after, n)
    if res:
        print("success")
    else:
        print("Failed")
    common_method.Stop_The_App()


#
# # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_Smoke_Test_TestcaseID_45891():
    """	Print multiple copies of template with variable data in Workspace"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    app_settings_page.click_Firstone_In_Recently_Prtinted_Label()
    smoke_test_android.click_Print_Button()
    smoke_test_android.click_And_Enter_Copies_Number_Field()
    smoke_test_android.click_Second_Print_Button()
    app_settings_page.click_Keyboard_back_Icon()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)

    """click on navigation option"""
    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    sleep(2)
    n = 2

    """test the printer to print the label"""
    for i in range(n):
        app_settings_page.click_Test_Print_Button()
        sleep(2)

    sleep(1)
    """Go to the Home Page"""
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)

    """Check wheather the cartridges are updated or not"""
    res = app_settings_page.check_update_cartridge(previous, after, n)
    if res:
        print("success")
    else:
        print("Failed")
    common_method.Stop_The_App()


# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_Smoke_Test_TestcaseID_45892():
    """	Delete template in Workspace"""

    """"Setup:
    1. There is an existing template in My Designs."""""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    smoke_test_android.click_Delete_Button_On_MyDesign()
    smoke_test_android.click_Cancel_Button_On_Delete_Popup()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    smoke_test_android.click_Delete_Button_On_MyDesign()
    smoke_test_android.Click_Delete_Button_On_Delete_Popup()
    data_sources_page.verify_design_successfully_removed_message()
    smoke_test_android.Verify_Deleted_Successfully_Message()
    common_method.Stop_The_App()


#
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
def test_Smoke_Test_TestcaseID_45893():
    """	To Verify View Zebra defined categories in Common Designs"""
    #
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    smoke_test_android.Verify_List_Is_Sorted_From_A_TO_Z()
    smoke_test_android.get_all_designs_in_Common_Designs()
    common_method.Stop_The_App()


#
#
# #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
def test_Smoke_Test_TestcaseID_45894():
    """	View list of Zebra templates in Common Designs"""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
    add_a_printer_screen.click_FirstOne_In_Common_Design()
    app_settings_page.click_Keyboard_back_Icon()
    smoke_test_android.click_Back_Icon_On_Address_Screen()
    smoke_test_android.Verify_Common_Design_Page_Is_Displaying()
    smoke_test_android.Verify_List_Is_Sorted_From_A_TO_Z()
    smoke_test_android.get_all_designs_in_Common_Designs()
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
    add_a_printer_screen.click_FirstOne_In_Common_Design()
    smoke_test_android.Verify_Copy_To_My_Design_Text_Is_Present()
    app_settings_page.click_Keyboard_back_Icon()
    smoke_test_android.click_Back_Icon_On_Address_Screen()
    smoke_test_android.Verify_Common_Design_Page_Is_Displaying()
    common_method.Stop_The_App()


# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
def test_Smoke_Test_TestcaseID_45895():
    """Print Zebra templates after Copy the template which needs to upload a picture from Library to Workspace (eg: Address->AddressWithIcon; Small Multipurpose->pickImage)"""

    #
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    previous = app_settings_page.Check_no_of_left_cartridge()
    print(previous)

    """click on navigation option"""
    login_page.click_Menu_HamburgerICN()

    """Select the Printer in the Printer Settings (Note: The printer name should be defined)"""
    app_settings_page.click_Printer_Settings()
    app_settings_page.click_PrinterName_On_Printersettings()
    sleep(2)
    n = 2

    """test the printer to print the label"""
    for i in range(n):
        app_settings_page.click_Test_Print_Button()
        sleep(2)

    sleep(1)
    """Go to the Home Page"""
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_Home_Tab()
    sleep(2)

    """After printing Get the number of cartridges"""
    after = app_settings_page.Check_no_of_left_cartridge()
    print(after)

    """Check wheather the cartridges are updated or not"""
    res = app_settings_page.check_update_cartridge(previous, after, n)
    if res:
        print("success")
    else:
        print("Failed")
    common_method.Stop_The_App()
    #


# # # # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#
#
def test_Smoke_Test_TestcaseID_45896():
    """Print a label from Common Design."""

    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    add_a_printer_screen.click_Common_Design_Tab()
    add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
    add_a_printer_screen.click_FirstOne_In_Common_Design()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Text_Field_To_Edit()
    add_a_printer_screen.click_Print_Button()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    """Verify manually it should print successfully"""
    """"point 4 is blocked due to SMB-1664"""""
    common_method.Stop_The_App()


# hello

"""JayKirans Code"""
"""zebra02.swdvt@gmail.com"""


def test_Template_Management_TestcaseID_46015():
    pass
    """Step 1-4 web portal - pending due to web in consistency"""
    common_method.tearDown()
    data_sources_page.log_out_of_account()
    data_sources_page.clearAppData()
    sleep(2)
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    registration_page.check_if_user_navigated_to_sign_in_page()
    account = "zebra02.swdvt@gmail.com"
    help_page.chooseAcc(account)
    registration_page.BugFix_For_Google(account)
    data_sources_page.checkIfOnHomePage()
    uploaded_file = "Country_capital.xlsx"
    """Upload file for execution"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    data_sources_page.click_Add_File()
    data_sources_page.click_Upload_File()
    data_sources_page.searchFileInLocalStorage(uploaded_file)
    """"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    sleep(3)
    data_sources_page.searchName(uploaded_file)
    sleep(2)
    data_sources_page.remove_File()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    design_name = "46015"
    "here"
    data_sources_page.searchMyDesigns(design_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    common_method.wait_for_element_appearance_namematches("could not be read")
    template_management_page.selectChooseAnOption(1, None, False)
    poco.scroll()
    """Issue in step 7 due to bug SMBM-2202"""
    template_management_page.select_file_update_data_connections("Local File")
    template_management_page.wait_for_appearance_enabled("Continue")
    data_sources_page.clickContinue()
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
    """Reopen print preview"""
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    template_management_page.selectChooseAnOption(1, None, False)
    poco.scroll()
    """Issue in step 7 due to bug SMBM-2202"""
    selected_file_name = template_management_page.select_file_update_data_connections("Google Drive")
    print(selected_file_name)
    if poco(text="Choose an account").exists():
        print("Entered If")
        data_sources_page.chooseAccToLinkFile("zebra03.swdvt@gmail.com")
    template_management_page.wait_for_appearance_enabled("Continue")
    data_sources_page.clickContinue()
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    try:
        registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
    except:
        raise Exception("Print preview not present.")
    """Remove the file from web"""
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    data_sources_page.add_new_tab_in_browser()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    data_sources_page.lock_phone()
    wake()
    registration_page.wait_for_element_appearance_text("Home", 10)
    sleep(3)
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    data_sources_page.click_My_Data()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.searchName("Korea.xlsx")
    keyevent("back")
    sleep(3)
    poco.scroll()
    sleep(2)
    data_sources_page.remove_File_Web()
    sleep(5)
    stop_app("com.android.chrome")
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_45924():
#     pass
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#     lastPrintInitial = template_management_page.getLastPrintFromFirstDesignInRecentlyPrintedDesigns()
#     raise Exception("Recently printed label has a bug SMBM-1748 hence unable to proceed.")
#     template_management_page_1.click_first_design_in_recently_printed_labels()
#     data_sources_page.clickPrint()
#     template_management_page.wait_for_appearance_enabled("Print")
#     initial_label_count = template_management_page.get_remaining_label_count()
#     data_sources_page.clickBackArrow()
#     try:
#         common_method.wait_for_element_appearance("Recently Printed Labels")
#         template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
#     except:
#         raise Exception("Recently printed label view not present.")
#     lastPrintNew = template_management_page.getLastPrintFromFirstDesignInRecentlyPrintedDesigns()
#     if lastPrintInitial == lastPrintNew:
#         pass
#     else:
#         raise Exception("Last print info updated without printing.")
#     raise Exception("Recently printed label has a bug SMBM-1748 hence unable to proceed.")
#     template_management_page_1.click_first_design_in_recently_printed_labels()
#     data_sources_page.clickPrint()
#     template_management_page.wait_for_appearance_enabled("Print")
#     new_label_count = template_management_page.get_remaining_label_count()
#     if initial_label_count == new_label_count:
#         pass
#     else:
#         raise Exception("Label count updated without printing.")
#     data_sources_page.clickPrint()
#     data_sources_page.clickBackArrow()
#     label_left = template_management_page.get_Labels_left_in_printer_info()
#     if str(new_label_count) in label_left:
#         pass
#     else:
#         raise Exception("Label count not updated in printer info after printing.")
#     common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46032():
    pass

    """Step 1-5 pending due to web automation"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "46032"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(4)
    if poco("Accept").exists():
        template_management_page.clickAccept()
    """ Office 365 contacts """
    account = "zebra03.swdvt@gmail.com"
    data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
    template_management_page_1.wait_for_element_appearance_name_matches_all("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 15:
        pass
    else:
        if int(number_of_labels) > 15:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    data_sources_page.scroll_till_print()
    template_management_page.choose_label_print_range()
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.clickConfirm()
    sleep(3)
    """Cannot automate  - has to be done manually as unable to enter data for missing fields"""
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 20)
    except:
        pass


def test_Template_Management_TestcaseID_46016():
    pass

    """Step 1-4 pending due to web inconsistency execute manually"""

    # start_app("com.android.chrome")
    # sleep(2)
    # poco("com.android.chrome:id/tab_switcher_button").click()
    # sleep(2)
    # data_sources_page.add_new_tab_in_browser()
    # sleep(2)
    # poco(text="Search or type URL").click()
    # sleep(2)
    # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    # sleep(2)
    # data_sources_page.clickEnter()
    # data_sources_page.lock_phone()
    # wake()
    # registration_page.wait_for_element_appearance_text("Home", 10)
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickMyDesigns()
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.lock_phone()
    # wake()
    # data_sources_page.clickCreateDesignBtn()
    # data_sources_page.lock_phone()
    # wake()
    # registration_page.wait_for_element_appearance_text("Select a label size", 10)
    # data_sources_page.selectLabelSize()
    # data_sources_page.clickContinueWeb()
    # data_sources_page.lock_phone()
    # wake()
    # poco(text="Exit Designer").wait_for_appearance(timeout=10)
    # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
    # sleep(3)
    # template_management_page.click_Connect_Data_File()
    # data_sources_page.lock_phone()
    # wake()
    # file_name = template_management_page.select_file_from_Connect_Data_File()
    # template_management_page.clickAddText()
    # template_management_page.placeText()
    # sleep(3)
    # keyevent("Back")
    # """Step -3"""
    # template_management_page.click_from_data_file()
    # data_sources_page.clickAddBarcode()
    # data_sources_page.placeBarcode()
    # keyevent("Back")
    """"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    uploaded_file = "csv_file.csv"
    """Upload file for execution"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    data_sources_page.click_Add_File()
    data_sources_page.click_Upload_File()
    data_sources_page.searchFileInLocalStorage(uploaded_file)
    """"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    data_sources_page.searchName(uploaded_file)
    sleep(2)
    data_sources_page.remove_File()
    sleep(3)
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.searchMyDesigns("46016")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    template_management_page.checkManualInput_checkbox()
    data_sources_page.clickContinue()
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    """cannot verify this part of step 6"""
    """check that no value shown in the variables in the preview dialog"""
    if template_management_page.verify_label_range_navigation_unavailable():
        pass
    else:
        raise Exception("Label range navigation is present.")
    """Step 7 pending"""
    template_management_page.fillOrganizationId("abcd")
    keyevent("back")
    template_management_page.fillIndex("xyz")
    keyevent("back")
    scroll_view = poco("android.view.View")
    scroll_view.swipe("down")
    """cannot verify this part of step 8"""
    """check that preview is shown correctly"""
    scroll_view.swipe("up")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        pass
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46019():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Step 1-4 pending due to web inconsistency"""
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("46019")
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    """Select column"""
    data_sources_page.clickBackArrow()
    data_sources_page.clickContinue()
    data_sources_page.first_row_header(False)
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    """check that only the selected column values shown in the table - pending"""
    """Check and uncheck select all"""
    scroll_view = poco("android.widget.ScrollView")
    data_sources_page.scroll_till_print()
    template_management_page.choose_label_print_range()
    data_sources_page.select_All()
    data_sources_page.select_All(False)
    """check select all"""
    data_sources_page.select_All()
    raise Exception("Blocked due to BUG ID - SMBM-1134")
    """Step 10 -15 blocked due to BUG ID - SMBM-1134"""
    data_sources_page.clickConfirm()
    """Check"""
    template_management_page.verify_label_navigation()
    data_sources_page.scroll_till_print()
    # data_sources_page.clickPrint()
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47791():
    pass

    # start_app("com.android.chrome")
    # sleep(2)
    # poco("com.android.chrome:id/tab_switcher_button").click()
    # sleep(2)
    # data_sources_page.add_new_tab_in_browser()
    # sleep(2)
    # poco(text="Search or type URL").click()
    # sleep(2)
    # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    # sleep(2)
    # data_sources_page.clickEnter()
    # registration_page.wait_for_element_appearance_text("Home", 10)
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickMyDesigns()
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.lock_phone()
    # wake()
    # data_sources_page.clickCreateDesignBtn()
    # data_sources_page.lock_phone()
    # wake()
    # registration_page.wait_for_element_appearance_text("Select a label size", 10)
    # data_sources_page.selectLabelSize()
    # data_sources_page.clickContinueWeb()
    # poco(text="Exit Designer").wait_for_appearance(timeout=10)
    # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
    # data_sources_page.lock_phone()
    # wake()
    # template_management_page.click_Connect_Data_File()
    # data_sources_page.lock_phone()
    # wake()
    # file_name = template_management_page.select_file_from_Connect_Data_File()
    # template_management_page.clickAddText()
    # template_management_page.placeText()
    # sleep(3)
    # keyevent("Back")
    # """Step -3"""
    # template_management_page.click_from_data_file()
    # data_sources_page.clickAddBarcode()
    # data_sources_page.placeBarcode()
    # keyevent("Back")
    # """"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.searchMyDesigns("47791")
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    if template_management_page.verify_if_on_relink_data_source_page():
        pass
    else:
        raise Exception("Not on Relink data source page.")
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    if template_management_page.verify_duplicate_previous_next_button():
        raise Exception("Duplicate Previous and Next button exists(SMBM-1818).")
    else:
        pass
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47824():
    """Verify ZSB app doesn't show "Print Complete" popup for empty label printing or printer is in error/offline
    status"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("Blank")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    registration_page.wait_for_element_appearance("Print")
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    registration_page.wait_for_element_appearance("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 20)
        raise ZeroDivisionError()
    except ZeroDivisionError:
        raise Exception("Print complete pop up is present even while printing blank label.(SMBM-1729)")
    except Exception as e:
        pass
    data_sources_page.checkPrintIsDisabled()
    """cannot verify - Check ZSB app should not show pint complete popup or the print button is disabled"""
    "No pop up and Print is enabled."


def test_Template_Management_TestcaseID_47947():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    initial_count = int(template_management_page.get_showing_n_designs_number())
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("47947")
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDeleteDesign()
    template_management_page.Turn_Off_wifi()
    "---------------------------"
    """Remove this after bug is resolved"""
    template_management_page.Turn_ON_wifi()
    raise Exception(
        "No specific or error message display for delete design when device lost its network connection(SMBM-1902)")
    "----------------------------"
    template_management_page.clickDeleteDesign()
    """Design delete pop up is still present"""
    """No prompt as \"Design XX was not deleted"\""""
    """Blocked due to bug id SMBM-1902"""
    template_management_page.Turn_ON_wifi()
    data_sources_page.searchMyDesigns("")
    data_sources_page.checkIfDesignsLoaded()
    final_count = int(template_management_page.get_showing_n_designs_number())
    if final_count == initial_count - 1:
        pass
    else:
        raise Exception("The count did not reduce by 1.")
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDuplicateDesign()
    template_management_page.new_design_name("47947")
    template_management_page.clickSave()


def test_Template_Management_TestcaseID_48548():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    design_created = "48548"
    data_sources_page.searchMyDesigns(design_created)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    """Rename pending"""
    renamed_design = "Round@22"
    template_management_page.rename_Design()
    template_management_page.new_design_name(renamed_design)
    template_management_page.clickSave()
    common_method.wait_for_element_appearance_namematches("Design has been successfully renamed")
    data_sources_page.searchMyDesigns(renamed_design)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDuplicateDesign()
    template_management_page.clickSave()
    common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated")
    data_sources_page.searchMyDesigns(renamed_design + " copy")
    data_sources_page.checkIfDesignsLoaded()
    duplicated_design_name = renamed_design + " copy"
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all(duplicated_design_name, 20)
    except:
        raise Exception("Duplicated design not present.")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Address", 20)
    except:
        raise Exception("Error displayed in common designs page")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns(renamed_design)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectSecondDesign()
    template_management_page.clickDeleteDesign()
    template_management_page.clickDeleteDesign()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("has been successfully removed", 20)
    except:
        raise Exception("Design not deleted.")
    data_sources_page.searchMyDesigns(duplicated_design_name)
    data_sources_page.checkIfDesignsLoaded()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all(duplicated_design_name, 20)
    except:
        raise Exception("Duplicated design not present after deleting original design.")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Address", 20)
    except:
        raise Exception("Error displayed in common designs page")
    """Change back the design name and bring back to default"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.searchMyDesigns(duplicated_design_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.rename_Design()
    template_management_page.new_design_name(design_created)
    template_management_page.clickSave()
    common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_45922():
#     pass
#
#     common_method.tearDown()
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickMyDesigns()
#     search_label_name = "Elements_11"
#     data_sources_page.searchMyDesigns(search_label_name)
#     data_sources_page.checkIfDesignsLoaded()
#     data_sources_page.selectDesignCreatedAtSetUp()
#     data_sources_page.clickPrint()
#     """cannot verify - 3a. Verify the design's elements are displayed in the print preview.
#     This has to be done manually"""
#     common_method.wait_for_element_appearance_textmatches("Text")
#     sleep(4)
#     field_count = len(template_management_page.get_all_fields_print_page())
#     if field_count == 11:
#         pass
#     else:
#         raise Exception("The number of fields are not 11.")
#     while not poco(nameMatches=".*Label.*").exists():
#         scroll_view = poco("android.widget.ScrollView")
#         scroll_view.swipe("down")
#     """ask supported special characters."""
#     template_management_page.fill_all_print_fields()
#     initial_label_count = template_management_page.get_remaining_label_count()
#     data_sources_page.clickPrint()
#     try:
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     except:
#         pass
#     new_label_count = template_management_page.get_remaining_label_count()
#     if new_label_count == initial_label_count - 1:
#         pass
#     else:
#         raise Exception("Label count not updated i.e., not decremented by 1.")
#     data_sources_page.clickBackArrow()
#     try:
#         common_method.wait_for_element_appearance_namematches("My Designs")
#     except:
#         data_sources_page.clickBackArrow()
#         common_method.wait_for_element_appearance_namematches("My Designs")
#     design = template_management_page.get_all_designs_in_my_designs()
#     sleep(3)
#     try:
#         design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
#         print(design_last_print_date, data_sources_page.get_current_date())
#         if str(design_last_print_date) == str(data_sources_page.get_current_date()):
#             pass
#         else:
#             raise Exception("Last printed date is not up to date.")
#     except:
#         raise Exception("No last print information under the design in My Designs Page")
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickHome()
#     label_left_in_printer_info = template_management_page.get_Labels_left_in_printer_info()
#     if str(new_label_count) + " of" in label_left_in_printer_info:
#         pass
#     else:
#         raise Exception("Labels left in printer info is not updated.")


def test_Template_Management_TestcaseID_46005():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "46005"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    name, size, lastPrint = template_management_page.get_the_name_size_and_lastprint_of_design(
        poco(nameMatches=f"(?s).*{search_label_name}.*").get_name())
    "unable to Verify design's information (Name, Size, Last Print) are NOT updated."
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    template_management_page.fill_all_print_fields("0")
    """Clear the input box for print preview-unable to set value to blank"""
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    "Verify updated elements are visible in print preview-cannot automate"
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")


def test_Template_Management_TestcaseID_46023():
    pass

    "Step 1- 4 pending due to web inconsistency"
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Click hamburger menu"""
    login_page.click_Menu_HamburgerICN()
    """clickMy designs"""
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    "Search label created in web"
    search_label_name = "46023"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    "Select the label"
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    template_management_page_1.check_element_exists_enabled("Print")
    data_sources_page.clickPrint()
    """select column with all alphabets"""
    template_management_page.selectChooseAnOption(1, "Alphabet")
    "click on continue"
    data_sources_page.clickContinue()
    "check if error pops up"
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
    except:
        raise Exception("No error displayed")
    data_sources_page.clickCancel()
    data_sources_page.scroll_till_print()
    poco.scroll()
    "navigate labels and check for error"
    data_sources_page.clickNext()
    "check if error pops up"
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
    except:
        raise Exception("No error displayed")
    data_sources_page.clickCancel()
    try:
        template_management_page.wait_for_appearance_disabled("Print", 10)
    except:
        raise Exception("Print option is not greyed out")
    data_sources_page.clickPrevious()
    "check if error pops up"
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
    except:
        raise Exception("No error displayed")
    data_sources_page.clickCancel()
    try:
        template_management_page.wait_for_appearance_disabled("Print", 5)
    except:
        raise Exception("Print option is not greyed out")
    "click back arrow"
    data_sources_page.clickBackArrow()
    data_sources_page.checkIfDesignsLoaded()
    "select the design created and click print"
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    "choose column with both numbers and alphabets"
    template_management_page.selectChooseAnOption(1, "Alphabet and Number")
    "click continue"
    data_sources_page.clickContinue()
    "check if error pops up for numeric values"
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Error message shown for column with numeric values.")
    except Exception as e:
        pass
    data_sources_page.scroll_till_print()
    "check print option is disabled"
    try:
        template_management_page.wait_for_appearance_disabled("Print", 5)
    except:
        raise Exception("Print option is not greyed out")
    "navigate labels and check if error pos up for numeric values"
    data_sources_page.clickNext()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Error message shown for column with numeric values.")
    except Exception as e:
        pass
    "check print option is disabled"
    try:
        template_management_page.wait_for_appearance_disabled("Print", 5)
    except:
        raise Exception("Print option is not greyed out")
    data_sources_page.clickNext()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
    except:
        raise Exception("No error displayed")
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Could not fetch the Print Preview")
    except:
        raise Exception("\"Could not fetch the Print Preview\" not present in popup")
    """uncheck the alphabet rows"""
    data_sources_page.clickCancel()
    "check print option is disabled"
    try:
        template_management_page.wait_for_appearance_disabled("Print", 5)
    except:
        raise Exception("Print option is not greyed out")
    data_sources_page.clickLabelRange()
    data_sources_page.clickCheckBox(0)
    data_sources_page.clickCheckBox(3)
    data_sources_page.clickCheckBox(4)
    data_sources_page.clickCheckBox(7)
    data_sources_page.clickConfirm()
    """check that correct label amount shown"""
    if template_management_page.check_total_label_for_print_count(3):
        pass
    else:
        raise Exception("Label amount shown is incorrect.")
    sleep(2)
    """check that correct row index shown in label range field"""
    label_range_index = data_sources_page.getRowIndex()
    if label_range_index == "1-2,5":
        pass
    else:
        raise Exception("Row index shown in label range field is incorrect.")
    "cannot automate - check that the labels are shown correctly has to be done manually"
    while template_management_page_1.check_element_exists_enabled("Next"):
        data_sources_page.clickNext()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Error message shown for column with numeric values.")
    except Exception as e:
        pass
    if template_management_page_1.check_element_exists_enabled("Print"):
        pass
    else:
        raise Exception("Print option is disabled.")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print complete notification did not appear.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46024():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "Linked_CSV"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page_1.check_element_exists_enabled("Print")
    data_sources_page.clickPrint()
    sleep(5)
    if poco(text="Choose an account").exists():
        data_sources_page.chooseAccToLinkFile("zebra03.swdvt@gmail.com")
    data_sources_page.clickContinue()
    data_sources_page.clickBackArrow()
    if template_management_page.verify_if_on_update_connections_page():
        pass
    else:
        raise Exception("Not on \"Update data connections\" page.")
    sleep(2)
    template_management_page.checkIfDataSourceIsLinked()
    data_sources_page.clickContinue()
    if template_management_page.verify_if_on_relink_data_source_page():
        pass
    else:
        raise Exception("Not on \"Relink data source\" page.")
    data_sources_page.first_row_header(True)
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    data_sources_page.scroll_till_print()
    initial_print_label_count = int(template_management_page.get_total_labels_printing())
    copies = 2
    template_management_page.changeCopiesCount(copies)
    keyevent("Enter")
    new_label_print_count = int(template_management_page.get_total_labels_printing())
    if new_label_print_count == initial_print_label_count * copies:
        pass
    else:
        raise Exception("Number of labels printing did not update properly.")
    initial_remaining_label = template_management_page.get_remaining_label_count()
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print complete notification did not appear.")
    template_management_page.closeNotification()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("Print complete notification did not close.")
    except Exception as e:
        pass
    common_method.wait_for_element_appearance_namematches("Label")
    new_remaining_label = template_management_page.get_remaining_label_count()
    print(initial_remaining_label)
    print(new_remaining_label)
    if new_remaining_label == initial_remaining_label - new_label_print_count:
        pass
    else:
        raise Exception(
            "Remaining label count not matching expected count.\n Expected label count = initial labels left in printer - number of labels printed.")
    data_sources_page.clickBackArrow()
    try:
        common_method.wait_for_element_appearance_namematches("My Designs")
    except:
        raise Exception("Did not return to \"My Designs\" page.")
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.searchName("")
    sleep(7)
    data_sources_page.searchName(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    design = template_management_page.get_all_designs_in_my_designs()
    design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
    if design_last_print_date == data_sources_page.get_current_date():
        pass
    else:
        raise Exception("Last printed date is not up to date.")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.clickBackArrow()
    if template_management_page.verify_if_on_update_connections_page():
        pass
    else:
        raise Exception("Not on \"Update data connections\" page.")
    sleep(2)
    template_management_page.checkIfDataSourceIsLinked()
    data_sources_page.clickContinue()
    if template_management_page.verify_if_on_relink_data_source_page():
        pass
    else:
        raise Exception("Not on \"Relink data source\" page.")
    data_sources_page.first_row_header(True)
    template_management_page.selectChooseAnOption(1)
    data_sources_page.clickContinue()
    data_sources_page.scroll_till_print()
    new_remaining_label_1 = template_management_page.get_remaining_label_count()
    if new_remaining_label_1 == new_remaining_label:
        pass
    else:
        raise Exception("Number of labels left have changed from the previous time without printing.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    data_sources_page.checkIfOnHomePage()
    prints_left = template_management_page.get_Labels_left_in_printer_info()
    print(prints_left)
    if str(new_remaining_label_1) in prints_left:
        pass
    else:
        raise Exception("Number of labels left (x of x prints left) is not updated in the Printer information.")


def test_Template_Management_TestcaseID_46033():
    pass

    """Step 1-5 pending due to web automation"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "46033"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(4)
    if poco("Accept").exists():
        template_management_page.clickAccept()
    """ Office 365 contacts """
    account = "zebra03.swdvt@gmail.com"
    if data_sources_page.check_if_asked_to_login_in_microsoft():
        data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
    try:
        common_method.wait_for_element_appearance_namematches("Label", 20)
    except:
        raise Exception("Microsoft Login dialog popped up even after google account already login")
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 15:
        pass
    else:
        if number_of_labels > 15:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    raise Exception("Unable to enter data to empty values due to bug SMBM-2204")
    """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
    data_sources_page.scroll_till_print()
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.labelRangeSelection(7)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("7")
    template_management_page.verify_label_navigation()
    raise Exception("unable to enter data manually for missing fields")
    """Cannot automate step 9 - has to be done manually anda also unable to enter data manually for missing fields"""
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    """Cannot automate-
    check that the labels are printed out with correct data
    check that the manually input values are printed out correctly
    check that the label with empty fields are still printed out with empty fields
    -has to be done manually"""
    """Step 11 pending as unable to enter data manually for missing fields"""
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46018():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Step 1-4 pending due to web inconsistency"""
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("46018")
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    sleep(2)
    """Select column"""
    data_sources_page.clickBackArrow()
    data_sources_page.clickContinue()
    data_sources_page.first_row_header()
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    scroll_view = poco("android.widget.ScrollView")
    while not poco("Print").exists():
        scroll_view.swipe("up")
    template_management_page.choose_label_print_range()
    data_sources_page.select_All()
    data_sources_page.select_All(False)
    """Step -8,9 pending as search is not working."""
    raise Exception("SMBM-1134: blocked")
    """Check select all"""
    data_sources_page.select_All()
    data_sources_page.clickConfirm()
    if template_management_page.check_if_on_print_preview_page():
        pass
    else:
        raise Exception("Did not return to print preview page.")
    poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    selected_number_of_rows = "4"
    data_sources_page.labelRangeSelection(int(selected_number_of_rows))
    """Step -8,9 pending as search is not working."""
    if template_management_page.check_if_on_print_preview_page():
        pass
    else:
        raise Exception("Did not return to print preview page.")
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range(selected_number_of_rows)
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46017():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Step 1-4 pending due to web inconsistency"""
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("46017")
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    """Select column"""
    data_sources_page.clickBackArrow()
    data_sources_page.clickContinue()
    data_sources_page.first_row_header()
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    template_management_page.check_if_on_print_preview_page()
    scroll_view = poco("android.widget.ScrollView")
    data_sources_page.scroll_till_print()
    template_management_page.verify_label_range_is_All()
    template_management_page.choose_label_print_range()
    try:
        common_method.wait_for_element_appearance("Select label range")
    except:
        raise Exception("Did not open print range dialog.")
    data_sources_page.select_All(False)
    data_sources_page.clickBackArrow()
    template_management_page.verify_label_range_is_All()
    data_sources_page.labelRangeSelection(3)
    sleep(2)
    raise Exception("Blocked due to bug SMBM-2204")
    """Cannot automate - check the one selected empty row will be disabled and empty - has to be done manually"""
    """Cannot automate - check that each labels can be previewed correctly - has to be checked manually"""
    template_management_page.verify_label_navigation()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46027():
    pass

    """Step 1-5 pending due to web automation"""
    common_method.tearDown()
    data_sources_page.log_out_of_account()
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    registration_page.check_if_user_navigated_to_sign_in_page()
    account = "zebra02.swdvt@gmail.com"
    help_page.chooseAcc(account)
    registration_page.BugFix_For_Google(account)
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
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
    account = "zebra03.swdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    # else:
    #     poco("com.google.android.gms:id/add_account_chip_title").click()
    #     registration_page.sign_In_With_Google("Zebra#123456789", account)
    #     sleep(2)
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    common_method.wait_for_element_appearance_namematches("NAME", 20)
    data_sources_page.clickBackArrow()
    sleep(5)
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "46027"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(4)
    if poco("Accept").exists():
        template_management_page.clickAccept()
    """ google contacts """

    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 12:
        pass
    else:
        if number_of_labels > 12:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    data_sources_page.scroll_till_print()
    template_management_page.choose_label_print_range()
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.clickConfirm()
    sleep(3)
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 10)
    except:
        pass


def test_Template_Management_TestcaseID_46028():
    pass

    """Step 1-5 pending due to web automation"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    sleep(2)
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    search_label_name = "46028"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(2)
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Label", 20)
    except:
        raise Exception("Google Login dialog popped up even after google account already login")
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    data_sources_page.scroll_till_print()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 12:
        pass
    else:
        if number_of_labels > 12:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
    data_sources_page.clickNext()
    data_sources_page.clickNext()
    data_sources_page.clickNext()
    data_sources_page.clickNext()
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    raise Exception("Unable to enter data to empty values due to bug SMBM-2204")
    """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
    data_sources_page.scroll_till_print()
    template_management_page.choose_label_print_range()
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.select_All(False)
    data_sources_page.clickBackArrow()
    data_sources_page.labelRangeSelection(7)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("7")
    template_management_page.verify_label_navigation()
    """Cannot automate step 9 - has to be done manually anda also unable to enter data manually for missing fields"""
    data_sources_page.scroll_till_print()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    """Step 11 pending as unable to enter data manually for missing fields"""
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46020():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Step 1-4 pending due to web inconsistency - has to be executed manually"""
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("UnevenC_R")
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    """Select column"""
    if poco(text="Choose an account").exists():
        help_page.chooseAcc("zebra03.swdvt@gmail.com")
    data_sources_page.clickBackArrow()
    data_sources_page.clickContinue()
    data_sources_page.first_row_header(True)
    template_management_page.selectChooseAnOption(2)
    data_sources_page.clickContinue()
    """check the label amount is correct, same as the selected column row number - cannot be automated"""
    try:
        registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
    except:
        raise Exception("Print preview not present.")
    data_sources_page.scroll_till_print()
    template_management_page.verify_label_range_is_All()
    """check that only the selected column values shown in the table - pending"""
    """select arbitrary number of columns"""
    count_checked_boxes = 4
    actual_checked_box_count = data_sources_page.labelRangeSelection(count_checked_boxes, False)
    checkbox = poco("android.widget.CheckBox")
    """Check first row is greyed out"""
    attribute = common_method.getAttr(checkbox[2], "enabled")
    if attribute == False:
        pass
    else:
        raise Exception("First row is not greyed out")
    data_sources_page.clickConfirm()
    """Check"""
    template_management_page.check_total_label_for_print_count(actual_checked_box_count)
    while not poco(nameMatches="Label.*").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")
    template_management_page.verify_label_navigation()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46022():
    pass

    # start_app("com.android.chrome")
    # sleep(2)
    # poco("com.android.chrome:id/tab_switcher_button").click()
    # sleep(2)
    # data_sources_page.add_new_tab_in_browser()
    # sleep(2)
    # poco(text="Search or type URL").click()
    # sleep(2)
    # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    # sleep(2)
    # data_sources_page.clickEnter()
    # data_sources_page.lock_phone()
    # wake()
    # registration_page.wait_for_element_appearance_text("Home", 10)
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickMyDesigns()
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.lock_phone()
    # wake()
    # data_sources_page.clickCreateDesignBtn()
    # data_sources_page.lock_phone()
    # wake()
    # registration_page.wait_for_element_appearance_text("Select a label size", 10)
    # data_sources_page.selectLabelSize()
    # data_sources_page.clickContinueWeb()
    # data_sources_page.lock_phone()
    # wake()
    # poco(text="Exit Designer").wait_for_appearance(timeout=10)
    # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
    # sleep(3)
    # data_sources_page.lock_phone()
    # wake()
    # template_management_page.click_Connect_Data_File()
    # data_sources_page.lock_phone()
    # wake()
    # data_file_name = "columnWithUnequalRows.xlsx"
    # template_management_page.select_file_from_Connect_Data_File(data_file_name)
    # data_sources_page.clickAddBarcode()
    # data_sources_page.placeBarcode()
    # sleep(3)
    # keyevent("Back")
    # data_sources_page.lock_phone()
    # wake()
    # common_method.swipe_screen([0.8407407407407408, 0.5260683760683761], [0.5009259259259259, 0.5260683760683761], 1)
    # template_management_page.click_from_data_file()
    # common_method.swipe_screen([0.5009259259259259, 0.5260683760683761], [0.8407407407407408, 0.5260683760683761], 1)
    # common_method.swipe_screen([0.08055555555555556, 0.25427350427350426], [0.9, 0.25427350427350426], 1)
    # common_method.swipe_screen([0.5, 0.254], [0.5, 0.63], 1)
    # data_sources_page.lock_phone()
    # wake()
    # label_name = "46022"
    # data_sources_page.setLabelName(label_name)
    # data_sources_page.exitDesigner()
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    poco("Open navigation menu").wait_for_appearance(timeout=10)
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.searchMyDesigns("46022")
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.clickBackArrow()
    common_method.wait_for_element_appearance_namematches("Update Data Connections")
    template_management_page.selectChooseAnOption(1, None, False)
    poco.scroll()
    """Issue in step 7 due to bug SMBM-2202"""
    selected_file_name = template_management_page.select_file_update_data_connections("Google Drive")
    if poco(text="Choose an account").exists():
        data_sources_page.chooseAccToLinkFile("zebra03.swdvt@gmail.com")
    data_sources_page.clickContinue()
    data_sources_page.first_row_header(True)
    template_management_page.selectChooseAnOption(1)
    data_sources_page.clickContinue()
    """check the label amount is correct, same as the selected column row number - cannot be automated"""
    try:
        registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
    except:
        raise Exception("Print preview not present.")
    data_sources_page.scroll_till_print()
    template_management_page.verify_label_range_is_All()
    """check that only the selected column values shown in the table - pending"""
    """select arbitrary number of columns"""
    count_checked_boxes = 4
    actual_checked_box_count = data_sources_page.labelRangeSelection(count_checked_boxes, False)
    checkbox = poco("android.widget.CheckBox")
    """Check first row is greyed out"""
    attribute = common_method.getAttr(checkbox[2], "enabled")
    if not attribute:
        pass
    else:
        raise Exception("First row is not greyed out")
    data_sources_page.clickConfirm()
    """Check"""
    template_management_page.check_total_label_for_print_count(actual_checked_box_count)
    while not poco(nameMatches="Label.*").exists():
        scroll_view = poco("android.view.View")
        scroll_view.swipe("down")
    template_management_page.verify_label_navigation()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46026():
    pass

    """Step 1-6 web portal - pending due to web in consistency"""
    selected_file_name = "test_link.xlsx"
    # start_app("com.android.chrome")
    # sleep(2)
    # poco("com.android.chrome:id/tab_switcher_button").click()
    # sleep(2)
    # data_sources_page.add_new_tab_in_browser()
    # sleep(2)
    # poco(text="Search or type URL").click()
    # sleep(2)
    # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    # sleep(2)
    # data_sources_page.clickEnter()
    # sleep(2)
    # registration_page.wait_for_element_appearance_text("Home", 20)
    # sleep(3)
    # sleep(600)
    # """2.in my design page, create a new design or edit an existing design
    # 3. select a data source file, no matter from local or google drive or one drive
    # 4. add text and barcode objects, select the link data source column as source type and select a column
    # 5. exit designer = has to be done manually due to web inconsistency"""
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.lock_phone()
    # wake()
    # sleep(2)
    # data_sources_page.click_My_Data()
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.searchName(selected_file_name)
    # keyevent("back")
    # sleep(3)
    # poco.scroll()
    # sleep(2)
    # data_sources_page.remove_File_Web()
    # stop_app("com.android.chrome")
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    common_method.wait_for_element_appearance_namematches("Open navigation menu")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    design_name = "46026"
    data_sources_page.searchMyDesigns(design_name)
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.clickBackArrow()
    template_management_page.verify_update_data_connections_dialog()
    template_management_page.selectChooseAnOption(1, None, False)
    """Issue in step 8 due to bug SMBM-2202"""
    template_management_page.select_file_update_data_connections("Upload File")
    data_sources_page.searchFileInLocalStorage(".xlsx")
    raise Exception("Blocked due to bug SMBM-2202")
    template_management_page.wait_for_appearance_enabled("Continue")
    data_sources_page.clickContinue()
    raise Exception("Blocked due to bug SMBM-2175")
    template_management_page.selectChooseAnOption(2)
    """Cannot automate \"Check the column name displayed above the column selection box. Currently it displays in the column selection box\" due to bug BUGID SMBM-2175"""
    data_sources_page.clickContinue()
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    """Cannot verify - navigate to check that the preview image is shown correctly- has to be done manually"""
    data_sources_page.scroll_till_print()
    poco.scroll()
    template_management_page.verify_label_range_is_All()
    data_sources_page.clickLabelRange()
    """Cannot verify \"check that all the columns and rows of the new data source file are shown in the table\""""
    data_sources_page.clickBackArrow()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    sleep(3)
    data_sources_page.clickBackArrow()
    """Re-upload file for next execution"""
    login_page.click_Menu_HamburgerICN()
    sleep(3)
    """Click My Data"""
    data_sources_page.click_My_Data()
    sleep(3)
    drive_file = "test_link.xlsx"
    """Click Add file"""
    data_sources_page.click_Add_File()
    sleep(2)
    """Click Link File"""
    data_sources_page.click_Link_File()
    sleep(2)
    """ google drive """
    if data_sources_page.verifySignInWithGoogle():
        registration_page.click_Google_Icon()
    account = "zebra03.swdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    #     else:
    #         poco("com.google.android.gms:id/add_account_chip_title").click()
    #         registration_page.sign_In_With_Google("Zebra#123456789", account)
    #         sleep(2)
    template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
    common_method.wait_for_element_appearance_namematches("NAME", 20)
    sleep(2)
    data_sources_page.selectFileDrive(selected_file_name)
    sleep(7)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_50656():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("PickImage")
    keyevent("Enter")
    common_method.wait_for_element_appearance_namematches("Designs")
    template_management_page.select_label_common_designs()
    data_sources_page.clickPrint()
    template_management_page.selectChooseAnOption(1, "Zebra Gallery")
    try:
        template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
    except:
        raise Exception("Zebra Gallery did not load.")
    all_Icons = template_management_page.get_all_icons_zebra_gallery()
    search_keyword = "Error"
    template_management_page.search_Icons(search_keyword)
    keyevent("Enter")
    search_results = template_management_page.get_all_icons_zebra_gallery()
    for icon in search_results:
        if search_keyword in icon:
            pass
        else:
            raise Exception("Search results do not contain the search keyword.")
    template_management_page.search_Icons("")
    keyevent("Enter")
    icons_after_clearing_search = template_management_page.get_all_icons_zebra_gallery()
    if all_Icons == icons_after_clearing_search:
        pass
    else:
        raise Exception("All Icons did not show up after clearing search text.")
    # # common_method.Stop_The_App()
    # # """Sign in same account in web portal, go to my designs, create/edit a design, add an image, set it to prompt at print needs to be executed manually due to web inconsistency """
    # # start_app("com.android.chrome")
    # # sleep(2)
    # # poco("com.android.chrome:id/tab_switcher_button").click()
    # # sleep(2)
    # # poco("com.android.chrome:id/new_tab_view_button").click()
    # # sleep(2)
    # # poco(text="Search or type URL").click()
    # # sleep(2)
    # # poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    # # sleep(2)
    # # data_sources_page.clickEnter()
    # # registration_page.wait_for_element_appearance_text("Home", 10)
    # # data_sources_page.click_Menu_HamburgerICNWeb()
    # # data_sources_page.clickMyDesigns()
    # # data_sources_page.lock_phone()
    # # wake()
    # # sleep(2)
    # # data_sources_page.click_Menu_HamburgerICNWeb()
    # # data_sources_page.clickCreateDesignBtn()
    # # sleep(5)
    # # data_sources_page.selectLabelSize()
    # # data_sources_page.clickContinueWeb()
    # # data_sources_page.lock_phone()
    # # wake()
    # # common_method.wait_for_element_appearance_text("Exit Designer")
    # # a, b = poco(text="Undo last operation. Max of 10 undo steps are supported.").get_position()
    # # while not poco(text="Add picture").exists():
    # #     common_method.swipe_screen([0.9, b], [0.3, b], 1)
    # #     data_sources_page.lock_phone()
    # #     wake()
    # #     sleep(3)
    # # data_sources_page.clickAddPhoto()
    # # data_sources_page.placePhoto()
    # # while not poco(text="Exit Designer").exists():
    # #     common_method.swipe_screen([0.1, b], [0.7, b], 1)
    # #     data_sources_page.lock_phone()
    # #     wake()
    # #     sleep(3)
    design_name = "Pic_PromptAtPrint"
    # # data_sources_page.setLabelName(design_name)
    # # sleep(5)
    # # data_sources_page.exitDesigner()
    # """Web pending due to inconsistent behaviour"""
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.searchMyDesigns(design_name)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    template_management_page.selectChooseAnOption(1, "Zebra Gallery")
    try:
        template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
    except:
        raise Exception("Zebra Gallery did not load.")
    template_management_page.clickSearchIconTextBox()
    template_management_page.clickSearchIcon()
    keyevent("Enter")
    all_iconsAfterClickingSearch = template_management_page.get_all_icons_zebra_gallery()
    if all_iconsAfterClickingSearch == all_Icons:
        pass
    else:
        raise Exception("All Icons did not show up.")
    template_management_page.clickFirstIcon()
    data_sources_page.scroll_till_print()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    raise Exception("Recently printed label has a bug SMBM-1748 hence unable to proceed.")
    """Yet to execute as recently printed labels has bug"""
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    template_management_page.selectChooseAnOption(1, "Zebra Gallery")
    try:
        template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
    except:
        raise Exception("Zebra Gallery did not load.")
    template_management_page.clickSearchIconTextBox()
    template_management_page.clickSearchIcon()
    keyevent("Enter")
    all_iconsAfterClickingSearch = template_management_page.get_all_icons_zebra_gallery()
    if all_iconsAfterClickingSearch == all_Icons:
        pass
    else:
        raise Exception("All Icons did not show up.")
    template_management_page.clickFirstIcon()
    data_sources_page.scroll_till_print()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47792():
    pass

    "Step 1-3 pending due to web inconsistency"
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing", 10)
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("CurrencyGBP")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    initial_print_value = template_management_page.get_print_value()
    template_management_page.click_print_value()
    keyevent("keyword del")
    keyevent("Enter")
    modified_print_value = template_management_page.get_print_value()
    if initial_print_value == modified_print_value:
        raise Exception("Print value not modified on clicking backspace(SMBM-1817).")
    else:
        pass
    common_method.Stop_The_App()


"""zebra07.swdvt@gmail.com"""


def test_Template_Management_TestcaseID_45981():
    pass
    common_method.tearDown()
    data_sources_page.log_out_of_account()
    sleep(2)
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    account = "zebra07.swdvt@gmail.com"
    registration_page.sign_in_with_mail_zebra07()
    registration_page.BugFix_For_ZebraEmail(account)
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_my_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    design_names = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_design_names_follow_order(design_names)
    expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel",
                        "$Address", "$Asset", "$Barcode", "$IconGiftLabel", "Address", "Asset", "Barcode (1)",
                        "IconGiftLabel"]
    for design in expected_designs:
        if design in design_names:
            pass
        else:
            error = "Design " + design + " not present."
            raise Exception(error)
    if template_management_page.check_design_count_title(len(design_names)):
        pass
    else:
        raise Exception("Count of number of designs in the tile doesnt match with actual count.")
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_my_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    design_names = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_design_names_follow_order(design_names)
    expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel",
                        "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
    for design in expected_designs:
        if design in design_names:
            pass
        else:
            error = "Design" + design + "not present."
            raise Exception(error)
    if template_management_page.check_design_count_title(len(design_names)):
        pass
    else:
        raise Exception("Count of number of designs in the tile doesn't match with actual count.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45982():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_my_designs()
    template_management_page.verify_sort_options_my_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.click_sort_my_designs()
    template_management_page.select_sort_order("A-Z")
    design_names = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_design_names_follow_order(design_names)
    expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel",
                        "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
    for design in expected_designs:
        if design in design_names:
            pass
        else:
            error = "Design " + design + " not present."
            raise Exception(error)
    if template_management_page.check_design_count_title(len(design_names)):
        pass
    else:
        raise Exception("Count of number of designs in the tile doesnt match with actual count.")
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_my_designs()
    template_management_page.verify_sort_options_my_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.click_sort_my_designs()
    template_management_page.select_sort_order("A-Z")
    design_names = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_design_names_follow_order(design_names)
    expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel",
                        "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
    for design in expected_designs:
        if design in design_names:
            pass
        else:
            error = "Design" + design + "not present."
            raise Exception(error)
    if template_management_page.check_design_count_title(len(design_names)):
        pass
    else:
        raise Exception("Count of number of designs in the tile doesn't match with actual count.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45983():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    template_management_page.click_sort_my_designs()
    template_management_page.select_sort_order("Z-A")
    design_names = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_design_names_follow_order(design_names, "Z-A")
    expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel",
                        "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
    for design in expected_designs:
        if design in design_names:
            pass
        else:
            error = "Design " + design + " not present."
            raise Exception(error)
    if template_management_page.check_design_count_title(len(design_names)):
        pass
    else:
        raise Exception("Count of number of designs in the tile doesnt match with actual count.")
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Sorting order is not back to default sort order - \"Name (A to Z)\" in my designs.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45984():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_my_designs("All sizes")
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    poco("Scrim").click()
    label_sizes_present = template_management_page.get_all_designs_size_in_my_designs()
    template_management_page.click_filter_my_designs("All sizes")
    filter_options = template_management_page.filter_options()
    poco("Scrim").click()
    for label_sizes in filter_options:
        if label_sizes in label_sizes_present:
            pass
        else:
            raise Exception(f"label with {label_sizes} not present.")
    if template_management_page.verify_sort_order_my_designs("A-Z"):
        pass
    else:
        raise Exception("Designs not sorted in A-Z order.")
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_my_designs("All sizes")
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    poco("Scrim").click()
    label_sizes_present = template_management_page.get_all_designs_size_in_my_designs()
    template_management_page.click_filter_my_designs("All sizes")
    filter_options = template_management_page.filter_options()
    poco("Scrim").click()
    for label_sizes in filter_options:
        if label_sizes in label_sizes_present:
            pass
        else:
            raise Exception(f"label with {label_sizes} not present.")
    if template_management_page.verify_sort_order_my_designs("A-Z"):
        pass
    else:
        raise Exception("Designs not sorted in A-Z order.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45985():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    template_management_page.click_filter_my_designs("All sizes")
    number_of_filter_options = template_management_page.filter_options(True)
    if number_of_filter_options > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    for i in range(1, number_of_filter_options):
        selectedFilterSize = template_management_page.selectFilter(i)
        data_sources_page.checkIfDesignsLoaded()
        label_size_present = template_management_page.get_all_designs_size_in_my_designs()
        labels = template_management_page.get_all_designs_in_my_designs()
        if len(label_size_present) == 1:
            design_size = label_size_present.pop()
            if design_size == selectedFilterSize:
                pass
            else:
                error_message = f"Designs with size - {label_size_present} displayed when {selectedFilterSize} is selected in filter."
                raise Exception(error_message)
        if len(labels) == int(template_management_page.get_showing_n_designs_number()):
            pass
        else:
            print(len(labels), "\n", int(template_management_page.get_showing_n_designs_number()))
            print(labels)
            raise Exception("Number of labels displayed not matching the number shown in title.")
        template_management_page.verify_designs_are_according_to_sort_order(labels)
        login_page.click_Menu_HamburgerICN()
        template_management_page.clickCommonDesigns()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        data_sources_page.checkIfDesignsLoaded()
        template_management_page.verify_default_sort_order_back_to_normal()
        template_management_page.click_filter_my_designs("All sizes")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45987():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Address")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    template_management_page.selectFilter(1)
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_sizes_displayed = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_sizes_displayed) > 1:
        print(design_sizes_displayed)
        raise Exception(
            "Designs are not filtered i.em designs of different sizes present even after filtering on one size.")
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_size) == 1:
        if design_size.pop() == label_size:
            pass
        else:
            raise Exception("Label size chosen in filter doesnt match the filtered result label size")
    else:
        raise Exception("There is more than 1 label size in the filtered results")
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45988():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Barcodes")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    template_management_page.selectFilter(1)
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_sizes_displayed = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_sizes_displayed) > 1:
        raise Exception(
            "Designs are not filtered i.em designs of different sizes present even after filtering on one size.(SMBM-1749)")
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_size) == 1:
        if design_size.pop() == label_size:
            pass
        else:
            raise Exception("Label size chosen in filter doesnt match the filtered result label size")
    else:
        raise Exception("There is more than 1 label size in the filtered results")
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45989():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("File Folder")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    template_management_page.selectFilter(1)
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_sizes_displayed = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_sizes_displayed) > 1:
        raise Exception(
            "Designs are not filtered i.e, designs of different sizes present even after filtering on one size.")
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45990():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Jewelry")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    displayed_filter_options = template_management_page.filter_options()
    if len(displayed_filter_options) == 1:
        if displayed_filter_options[0] == "2.25\" x 0.5\"":
            pass
        else:
            raise Exception(f"Filter option {displayed_filter_options[1]} displayed instead of 2.25\" x 0.5\"")
    else:
        error = f"Has {len(displayed_filter_options)} filter options i.e., {displayed_filter_options} instead of just 1 i.e., \"2.25\" x 0.5\"\" "
        raise Exception(error)
    poco("Scrim").click()
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_size) == 1:
        if design_size.pop() == label_size:
            pass
        else:
            raise Exception("Label size chosen in filter doesnt match the filtered result label size")
    else:
        raise Exception("There is more than 1 label size in the filtered results")
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45991():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Multipurpose/")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    displayed_filter_options = template_management_page.filter_options()
    if len(displayed_filter_options) == 1:
        if displayed_filter_options[0] == "3.5\" x 2.25\"":
            pass
        else:
            raise Exception(f"Filter option {displayed_filter_options[1]} displayed instead of 3.5\" x 2.25\"")
    else:
        error = f"Has {len(displayed_filter_options)} filter options i.e., {displayed_filter_options} instead of just 1 i.e., \"3.5\" x 2.25\"\" "
        raise Exception(error)
    poco("Scrim").click()
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_size) == 1:
        if design_size.pop() == label_size:
            pass
        else:
            raise Exception("Label size chosen in filter doesnt match the filtered result label size")
    else:
        raise Exception("There is more than 1 label size in the filtered results")
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45992():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Name")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    number_of_filter_options = template_management_page.filter_options(True)
    if number_of_filter_options >= 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    poco("Scrim").click()
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    for i in range(1, number_of_filter_options):
        selectedFilterSize = template_management_page.selectFilter(i)
        sleep(10)
        label_size_present = template_management_page.get_all_designs_size_in_my_designs()
        if len(label_size_present) == 1:
            design_size = label_size_present.pop()
            if design_size == selectedFilterSize:
                pass
            else:
                error_message = f"Designs with size - {label_size_present} displayed when {selectedFilterSize} is selected in filter."
                raise Exception(error_message)
        template_management_page.click_sort_common_designs()
        template_management_page.select_sort_order("A-Z")
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        template_management_page.verify_designs_are_according_to_sort_order(design_list)
        template_management_page.click_sort_common_designs()
        template_management_page.select_sort_order("Z-A")
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        template_management_page.verify_designs_are_according_to_sort_order(design_list)
        template_management_page.click_filter_common_designs()
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45993():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Shipping")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    if template_management_page.verify_default_sort_my_designs():
        pass
    else:
        raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
    template_management_page.click_sort_common_designs()
    template_management_page.verify_sort_options_my_designs()
    poco("Scrim").click()
    template_management_page.verify_default_filter_my_designs()
    template_management_page.click_filter_common_designs()
    if template_management_page.filter_options(True) > 1:
        pass
    else:
        raise Exception("No other filter option present other than All sizes.")
    template_management_page.selectFilter(1)
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_sizes_displayed = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_sizes_displayed) > 1:
        raise Exception(
            "Designs are not filtered i.em designs of different sizes present even after filtering on one size.")
    template_management_page.click_sort_common_designs()
    sleep(3)
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_filter_common_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_size = template_management_page.get_all_designs_size_in_my_designs()
    if len(design_size) == 1:
        if design_size.pop() == label_size:
            pass
        else:
            raise Exception("Label size chosen in filter doesnt match the filtered result label size")
    else:
        raise Exception("There is more than 1 label size in the filtered results")
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("A-Z")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    template_management_page.click_sort_common_designs()
    template_management_page.select_sort_order("Z-A")
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45994():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    template_management_page.Turn_Off_wifi()
    try:
        poco(
            nameMatches="(?s).*An error occurred when loading your designs. Please tap to try again.*").wait_for_appearance(
            timeout=20)
        x = 1 / 0
    except ZeroDivisionError:
        template_management_page.Turn_ON_wifi()
        raise Exception("Blocked due to bug SMBM-1774")
    except Exception as e:
        pass
    template_management_page.click_filter_my_designs()
    label_size = template_management_page.select_label_size()
    sleep(3)
    template_management_page.Turn_ON_wifi()
    sleep(2)
    template_management_page.click_filter_my_designs()
    sleep(5)
    if template_management_page.verify_connection_error_app():
        pass
    else:
        raise Exception("Connection lost error not displayed(SMBM-1774).")
    template_management_page.click_filter_my_designs()
    label_size = template_management_page.select_label_size()
    template_management_page.wait_for_appearance_designs_in_a_particular_category()
    design_name = template_management_page.get_first_design_name_my_designs()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    title_count = template_management_page.get_showing_n_designs_number()
    if len(design_list) == int(title_count):
        pass
    else:
        raise Exception("Count in title doesn't match the number of designs.")
    template_management_page.Turn_Off_wifi()
    template_management_page.search_design_common_designs(design_name)
    """"""
    """Remove after bug is resolved"""
    template_management_page.Turn_ON_wifi()
    """"""
    raise Exception("Blocked due to bug SMBM-1774")
    """Step 8-10 pending due to bug SMBM-1774"""
    sleep(3)
    if template_management_page.verify_connection_error_app():
        pass
    else:
        raise Exception("Connection lost error not displayed.")
    template_management_page.Turn_ON_wifi()
    sleep(5)
    template_management_page.search_design_common_designs(design_name)
    try:
        template_management_page.wait_for_suggestions_to_appear()
    except:
        raise Exception("dropdown did not appear.")
    template_management_page.check_dropdown_options_Are_clickable()
    template_management_page.click_drop_down_result_1()
    try:
        template_management_page.wait_for_suggestions_to_appear()
        x = 1 / 0
    except ZeroDivisionError:
        raise Exception("dropdown is present.")
    except Exception as e:
        pass
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    if len(design_list) == 1:
        if design_list[0] == design_name:
            pass
        else:
            raise Exception("The resulting design name doesn't match search name")
    else:
        raise Exception("There are more than 1 result.")
    title_count = template_management_page.get_showing_n_designs_number()
    if int(title_count) == 1:
        pass
    else:
        raise Exception("Title is not 'Showing 1 Design'.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46010():
    pass
    template_management_page.Turn_ON_wifi()
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    initial_categories_list = template_management_page.get_all_categories_in_common_designs()
    if template_management_page.verify_search_placeholder():
        pass
    else:
        raise Exception("Search design placeholder not present.")
    if template_management_page.verifySearchIcon():
        pass
    else:
        raise Exception("Search icon not present")
    search_text = "/"
    template_management_page.search_design_common_designs(search_text)
    template_management_page_1.wait_for_element_appearance_name_matches_all("CATEGORIES", 20)
    sleep(3)
    category_list_drop_down = template_management_page.get_drop_down_list_common_designs(True)
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    category_list = template_management_page.get_all_categories_in_common_designs(True)
    if category_list == category_list_drop_down:
        pass
    else:
        print(category_list, "\n", category_list_drop_down)
        raise Exception("All Categories not displayed in drop down.")
    template_management_page.clickCancelSearch()
    search_text = "-"
    template_management_page.search_design_common_designs(search_text)
    template_management_page_1.wait_for_element_appearance_name_matches_all("DESIGNS", 20)
    sleep(3)
    design_list_drop_down = template_management_page.get_drop_down_list_common_designs()
    keyevent("Enter")
    search_text = "-"
    template_management_page.search_design_common_designs(search_text)
    template_management_page_1.wait_for_element_appearance_name_matches_all("DESIGNS", 20)
    sleep(3)
    name_dropdown = template_management_page.click_drop_down_result_1(True)
    print(name_dropdown)
    sleep(3)
    try:
        common_method.wait_for_element_appearance_namematches("Search results")
    except:
        raise Exception("dropdown did not close.")
    if template_management_page.verifySearchResults_n(1):
        pass
    else:
        raise Exception("Search results(1) not present.")
    names_result = template_management_page.get_all_designs_in_search_designs(True)
    print(names_result)
    if name_dropdown == names_result[0]:
        pass
    else:
        raise Exception("Selected design not displayed.")
    template_management_page.search_design_common_designs("")
    keyevent("Enter")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    new_categories_list = template_management_page.get_all_categories_in_common_designs()
    if initial_categories_list == new_categories_list:
        pass
    template_management_page.search_design_common_designs("~`!@#$%^&*()_-+={}[]|/\:;"'<>,.?'"")
    try:
        template_management_page.waitForAppearanceOfNoResultsFound()
    except:
        raise Exception("No results for \"searched text\" text not displayed.")
    template_management_page.search_design_common_designs("")
    keyevent("Enter")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    new_categories_list = template_management_page.get_all_categories_in_common_designs()
    if initial_categories_list == new_categories_list:
        pass


def test_Template_Management_TestcaseID_46014():
    pass
    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    """"""
    categories = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping",
                  "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose", "XL Shipping"]
    search_text = ["Product", "Dishes", "Price", "Badge", "Harmful", "TwoLine", "Fragile", "Caution", "Asset",
                   "Checklist"]
    for i in range(2):
        template_management_page.search_design_common_designs(categories[i])
        keyevent("Enter")
        template_management_page.waitForAppearanceOfCategories()
        template_management_page.select_design_common_designs()
        if template_management_page.verify_search_placeholder():
            pass
        else:
            raise Exception("Search design place holder doesnt have 'Search designs'.")
        template_management_page.search_design_common_designs(search_text[i])
        template_management_page.check_if_drop_down_list_open()
        """Cannot automate step 5b.Verify the matched keyword is in blue font. - has to be verified manually"""
        template_management_page.check_if_drop_down_list_contains_results_that_include_search_keyword(search_text[i])
        template_management_page.check_dropdown_options_Are_clickable()
        template_management_page.checkNumberOfDesignsMatchingDropDown()
        keyevent("Enter")
        if poco(nameMatches="(?s).*result").exists():
            raise Exception("Drop down present even after clicking search on keyboard.")
        else:
            pass
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        for result in design_list:
            if search_text[i].lower() in result.lower():
                pass
            else:
                raise Exception("search text not present in one of the results.")
        template_management_page.click_filter_common_designs()
        label_size = template_management_page.select_label_size()
        print(label_size)
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_size = template_management_page.get_all_designs_size_in_my_designs()
        if len(design_size) == 1:
            if design_size.pop() == label_size:
                pass
            else:
                raise Exception("Label size chosen in filter doesnt match the filtered result label size")
        else:
            raise Exception("There is more than 1 label size in the filtered results")
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        init_no_of_designs = len(design_list)
        template_management_page.verify_designs_are_according_to_sort_order(design_list)
        template_management_page.click_sort_common_designs()
        template_management_page.select_sort_order("Z-A")
        sleep(3)
        if template_management_page.get_filter_value() == label_size:
            pass
        else:
            raise Exception("Filtering selection changed after changing sort order.")
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        template_management_page.verify_designs_are_according_to_sort_order(design_list)
        no_of_designs = len(design_list)
        if no_of_designs == init_no_of_designs:
            pass
        else:
            raise Exception("The number of designs are not same before and after sorting.")
        template_management_page.click_sort_common_designs()
        sleep(3)
        template_management_page.select_sort_order("A-Z")
        sleep(3)
        if template_management_page.get_filter_value() == label_size:
            pass
        else:
            raise Exception("Filtering selection changed after changing sort order.")
        template_management_page.wait_for_appearance_designs_in_a_particular_category()
        design_list = template_management_page.get_all_designs_in_my_designs(True)
        template_management_page.verify_designs_are_according_to_sort_order(design_list)
        no_of_designs = len(design_list)
        if no_of_designs == init_no_of_designs:
            pass
        else:
            raise Exception("The number of designs are not same before and after sorting.")
        help_page.clickBackArrow()
        template_management_page.select_design_common_designs()
        if template_management_page.verify_search_placeholder():
            pass
        else:
            raise Exception("Search box not cleared.")
        help_page.clickBackArrow()
    common_method.Stop_The_App()


"""Semi Automated"""
#
#
# def test_Template_Management_TestcaseID_46029():
#     pass
#
#     """Step 1-5 pending due to web automation"""
#     common_method.tearDown()
#     data_sources_page.log_out_of_account()
#     data_sources_page.clearAppData()
#     common_method.tearDown()
#     data_sources_page.allowPermissions()
#     registration_page.clickSignIn()
#     registration_page.click_Google_Icon()
#     registration_page.check_if_user_navigated_to_sign_in_page()
#     account = "zebra02.swdvt@gmail.com"
#     help_page.chooseAcc(account)
#     data_sources_page.checkIfOnHomePage()
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickMyDesigns()
#     data_sources_page.checkIfDesignsLoaded()
#     search_label_name = "46029"
#     data_sources_page.searchMyDesigns(search_label_name)
#     data_sources_page.checkIfDesignsLoaded()
#     data_sources_page.selectDesignCreatedAtSetUp()
#     data_sources_page.clickPrint()
#     sleep(4)
#     if poco("Accept").exists():
#         template_management_page.clickAccept()
#     data_sources_page.chooseAccToLinkFile(account)
#     try:
#         registration_page.wait_for_element_appearance_text("Sign in to ZSB Series", 20)
#         poco.scroll()
#         data_sources_page.clickContinueWeb()
#     except:
#         pass
#     try:
#         registration_page.wait_for_element_appearance_text("ZSB Series wants access to your Google Account", 20)
#         while not poco(text="Continue").exists():
#             poco.scroll()
#         data_sources_page.clickContinueWeb()
#     except:
#         pass
#     try:
#         registration_page.wait_for_element_appearance_text(" wants to access your Google Account", 20)
#         while not poco(text="Allow").exists():
#             poco.scroll()
#         data_sources_page.clickAllow_Text()
#     except:
#         pass
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Label", 20)
#     sleep(10)
#     data_sources_page.verifyIfPreviewIsPresent()
#     data_sources_page.scroll_till_print()
#     number_of_labels = int(template_management_page.get_total_labels_printing())
#     if number_of_labels == 1:
#         pass
#     else:
#         error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#         raise Exception(error)
#     data_sources_page.clickLabelRange()
#     sleep(2)
#     if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#         pass
#     else:
#         raise Exception("Tabel is not empty.")
#     data_sources_page.clickBackArrow()
#     """Step - 7 pending as input fields are not editable."""
#     raise Exception("Unable to enter data to empty values due to bug SMBM-2204")
#     data_sources_page.clickPrint()
#     try:
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     except:
#         pass
#     data_sources_page.clickBackArrow()
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickHome()
#     start_app("com.android.chrome")
#     sleep(2)
#     poco("com.android.chrome:id/tab_switcher_button").click()
#     sleep(2)
#     data_sources_page.add_new_tab_in_browser()
#     sleep(2)
#     poco(text="Search or type URL").click()
#     sleep(2)
#     poco(text="Search or type URL").set_text("https://contacts.google.com/")
#     data_sources_page.clickEnter()
#     sleep(2)
#     data_sources_page.lock_phone()
#     wake()
#     sleep(2)
#     common_method.wait_for_element_appearance_text("Contacts", 20)
#     try:
#         common_method.wait_for_element_appearance_text("Use the Contacts app")
#         if poco(text="Stay on web").exists():
#             poco(text="Stay on web").click()
#     except:
#         pass
#     template_management_page.changeAccInAddContacts(account)
#     common_method.wait_for_element_appearance_text("Contacts")
#     try:
#         common_method.wait_for_element_appearance_text("Use the Contacts app")
#         if poco(text="Stay on web").exists():
#             poco(text="Stay on web").click()
#     except:
#         pass
#     template_management_page.createContact("a", "1")
#     stop_app("com.android.chrome")
#     registration_page.wait_for_element_appearance("Home", 20)
#     registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
#     raise Exception("Recently printed label has a bug SMBM-1748 hence unable to proceed.")
#     """Yet to execute as recently printed labels has bug"""
#     template_management_page_1.click_first_design_in_recently_printed_labels()
#     data_sources_page.clickPrint()
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Label", 20)
#     sleep(10)
#     data_sources_page.verifyIfPreviewIsPresent()
#     data_sources_page.scroll_till_print()
#     number_of_labels = int(template_management_page.get_total_labels_printing())
#     if number_of_labels == 2:
#         pass
#     else:
#         error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#         raise Exception(error)
#     data_sources_page.clickLabelRange()
#     sleep(2)
#     if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#         raise Exception("Tabel is empty even after adding a contact.")
#     data_sources_page.clickBackArrow()
#     """Step - 7 pending as input fields are not editable."""
#     data_sources_page.clickPrint()
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     common_method.Stop_The_App()


"""zebra04.swdvt@gmail.com"""


def test_Template_Management_TestcaseID_45966():
    """Scroll design list in My Designs with more than 100 designs"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    registration_page.check_if_user_navigated_to_sign_in_page()
    account = "zebra04.swdvt@gmail.com"
    help_page.chooseAcc(account)
    registration_page.BugFix_For_Google(account)
    sleep(5)
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    data_sources_page.check_if_showing_100_designs_text()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.check_there_are_less_than_100_designs(design_list)
    template_management_page.scroll_my_designs("down")
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    """Step 5, 6 yet to do"""
    template_management_page.scroll_my_designs()
    template_management_page.scroll_my_designs("down")
    "Delete design"
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDeleteDesign()
    template_management_page.clickDeleteDesign()
    data_sources_page.checkIfDesignsLoaded()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.check_there_are_less_than_100_designs(design_list)
    template_management_page.scroll_my_designs("down")
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    """Step 5, 6 yet to do"""
    template_management_page.scroll_my_designs()
    template_management_page.scroll_my_designs("down")
    """Duplicate design"""

    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDuplicateDesign()
    template_management_page.clickSave()
    data_sources_page.checkIfDesignsLoaded()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.check_there_are_less_than_100_designs(design_list)
    template_management_page.scroll_my_designs("down")
    template_management_page.verify_designs_are_according_to_sort_order(design_list)
    """Step 5, 6 yet to do"""
    template_management_page.scroll_my_designs()
    template_management_page.scroll_my_designs("down")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46037():
    """with 100+ template in my design, create a template save then print out via Mobile"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    initial_design_count = len(template_management_page.get_all_designs_in_my_designs())
    designName = "ZZZ_Test"
    """Step 1-4 pending due to web inconsistency - has to be done manually"""
    sleep(2)
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    data_sources_page.add_new_tab_in_browser()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    sleep(2)
    registration_page.wait_for_element_appearance_text("Home", 10)
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    data_sources_page.clickMyDesigns()
    data_sources_page.click_Menu_HamburgerICNWeb()
    scroll_view = poco("android.view.View")
    while poco(text="This is where you can access all of your saved designs.").exists():
        scroll_view.swipe("up")
    template_management_page.verify_My_Designs_pagination()
    template_management_page.verify_pagination_shown_is_correct()
    data_sources_page.clickCreateDesignBtn()
    data_sources_page.lock_phone()
    wake()
    """Step 4 pending due to web inconsistency."""
    stop_app("com.android.chrome")
    data_sources_page.checkIfDesignsLoaded()
    new_design_count = len(template_management_page.get_all_designs_in_my_designs())
    template_management_page.check_if_design_count_incremented_by_1(new_design_count, initial_design_count)
    """Step 5 check template total number add one pending"""
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns(designName)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    """Delete the design for next execution"""
    data_sources_page.clickBackArrow()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDeleteDesign()
    template_management_page.clickDeleteDesign()


def test_Template_Management_TestcaseID_46038():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    raise Exception("No Pagination on app")
    """Step 2, 3 pending as no pagination on mobile app"""
    """Navigating to page 3 pending as no pagination on app"""
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    """Step 5 - Repeat for all pages pending as no pagination on app"""
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46039():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    initial_design_count = len(template_management_page.get_all_designs_in_my_designs())
    raise Exception("No Pagination on app")
    """Step 2 pending as no pagination on mobile app"""
    """Navigating to page 3 pending as no pagination on app"""
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDuplicateDesign()
    new_name = "Duplicate Test"
    template_management_page.new_design_name(new_name)
    template_management_page.clickSave()
    data_sources_page.checkIfDesignsLoaded()
    new_design_count = len(template_management_page.get_all_designs_in_my_designs())
    template_management_page.check_if_design_count_incremented_by_1(new_design_count, initial_design_count)
    data_sources_page.searchMyDesigns(new_name)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    copies = 2
    template_management_page.changeCopiesCount(copies)
    keyevent("Enter")
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    template_management_page.changeCopiesCount(" ")
    keyevent("Enter")
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page.verifyErrorPopUp_forInvalidCopies()
    data_sources_page.clickContinue()
    template_management_page.changeCopiesCount("$")
    keyevent("Enter")
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page.verifyErrorPopUp_forInvalidCopies()
    data_sources_page.clickContinue()
    """Delete the design for next execution"""
    data_sources_page.clickBackArrow()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDeleteDesign()
    template_management_page.clickDeleteDesign()
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46040():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    initial_design_count = len(template_management_page.get_all_designs_in_my_designs())
    raise Exception("No Pagination on app")
    """Step 2 pending as no pagination on mobile app"""
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
    template_management_page.search_design_common_designs("Address")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    selected_label = template_management_page.select_label_common_designs() + " copy"
    template_management_page.click_copy_to_My_Designs()
    sleep(2)
    data_sources_page.clickBackArrow()
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    new_design_count = len(template_management_page.get_all_designs_in_my_designs())
    template_management_page.check_if_design_count_incremented_by_1(new_design_count, initial_design_count)
    data_sources_page.searchMyDesigns(selected_label)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    copies = 2
    template_management_page.changeCopiesCount(copies)
    keyevent("Enter")
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    """Delete the design for next execution"""
    data_sources_page.clickBackArrow()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.clickDeleteDesign()
    template_management_page.clickDeleteDesign()
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46041():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    initial_design_count = template_management_page.get_showing_n_designs_number()
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    data_sources_page.add_new_tab_in_browser()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    registration_page.wait_for_element_appearance_text("Home", 10)
    sleep(2)
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    data_sources_page.clickMyDesigns()
    data_sources_page.click_Menu_HamburgerICNWeb()
    scroll_view = poco("android.view.View")
    while poco(text="This is where you can access all of your saved designs.").exists():
        scroll_view.swipe("up")
    template_management_page.verify_My_Designs_pagination()
    design_selected = "ImportedTemplate"
    downloaded_design_name = design_selected + ".nlbl"
    template_management_page.clickImport()
    data_sources_page.searchFileInLocalStorage(downloaded_design_name, "Downloads")
    sleep(10)
    stop_app("com.android.chrome")
    data_sources_page.checkIfDesignsLoaded()
    new_design_count = template_management_page.get_showing_n_designs_number()
    template_management_page.check_if_design_count_incremented_by_1(new_design_count, initial_design_count)
    data_sources_page.searchMyDesigns(design_selected)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    data_sources_page.scroll_till_print()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47941():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    try:
        common_method.wait_for_element_appearance("My Data")
    except:
        raise Exception("My Data page did not open.")
    try:
        common_method.wait_for_element_appearance("Connect files so you can leverage them within your designs.")
    except:
        raise Exception("\"Connect files so you can leverage them within your designs.\" text not present")

    if template_management_page.checkIfElementIsPresent("You don’t have any files"):
        if template_management_page.checkIfElementIsPresent(
                "Get started by adding files to be used within your workspace and your team."):
            pass
    elif template_management_page.checkIfElementIsPresent("android.widget.EditText"):
        try:
            template_management_page.verifySearchIcon()
            pass
        except:
            raise Exception("Search Icon not present.")
        if template_management_page.verifySearchFiles():
            pass
        else:
            raise Exception("Search Files placeholder not present.")
        if template_management_page.checkIfElementIsPresent("NAME"):
            pass
        else:
            raise Exception("NAME field not present.")
        """Cannot automate step 3 due to BUG SMBM-938"""
    common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_47812():
#     pass
#
#     common_method.tearDown()
#     data_sources_page.checkIfOnHomePage()
#     login_page.click_Menu_HamburgerICN()
#     template_management_page.clickCommonDesigns()
#     data_sources_page.searchName("Label", False)
#     """Cannot automate - Check the search result title and the result label should not overlap each other - due to bug SMBM-1886"""
#     common_method.Stop_The_App()


""""""


def test_Template_Management_TestcaseID_48266():
    pass

    data_sources_page.clearBrowsingData()
    common_method.tearDown()
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    data_sources_page.add_new_tab_in_browser()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    data_sources_page.lock_phone()
    wake()
    try:
        data_sources_page.signInWithGoogle("zebra03.swdvt@gmail.com", "Zebra#123456789")
        data_sources_page.lock_phone()
    except:
        pass
    wake()
    try:
        data_sources_page.clickGotItWeb()
    except:
        pass
    registration_page.wait_for_element_appearance_text("Home", 10)
    data_sources_page.click_Menu_HamburgerICNWeb()
    template_management_page.clickCommonDesigns()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.lock_phone()
    wake()
    template_management_page.search_design_common_designs("Round")
    keyevent("Enter")
    keyevent("back")
    poco.scroll()
    data_sources_page.lock_phone()
    wake()
    template_management_page.select_design_common_designs_Web()
    while poco("android.widget.EditText").exists():
        poco.scroll()
    template_management_page.select_label_common_designs_Web()
    data_sources_page.lock_phone()
    wake()
    selected_design_name = template_management_page.get_name_of_selected_design()
    template_management_page.click_copy_to_My_Designs()
    copied_design_name = selected_design_name + " copy"
    template_management_page.select_label_common_designs_Web()
    data_sources_page.clickPrint()
    data_sources_page.clickPrint()
    common_method.tearDown()
    registration_page.wait_for_element_appearance("Open navigation menu", 10)
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns(copied_design_name)
    data_sources_page.checkIfDesignsLoaded()
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    if copied_design_name in design_list:
        pass
    else:
        raise Exception("Copied design from web not present in app.")
    login_page.click_Menu_HamburgerICN()
    template_management_page.clickCommonDesigns()
    template_management_page.search_design_common_designs("Round")
    keyevent("Enter")
    template_management_page.waitForAppearanceOfCategories()
    template_management_page.select_design_common_designs()
    template_management_page.verifyLabelsShown()
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    recently_printed_designs = template_management_page_1.get_all_designs_in_recently_printed_labels()
    for i in recently_printed_designs:
        if "Last print" in i:
            pass
        else:
            raise Exception("Recently printed labels not loaded successfully.")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    try:
        template_management_page.waitForAppearanceTypeName("android.widget.ImageView", "x")
    except:
        raise Exception("My Designs did not load properly.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45979():
    """Search designs in My Designs with more than 100 designs in the list"""

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    template_management_page.verify_search_placeholder()
    template_management_page.verifySearchIcon()
    initial_design_list = template_management_page.get_all_designs_in_my_designs(True)
    initial_count = template_management_page.get_showing_n_designs_number()
    search_keyword = "4_Address"
    data_sources_page.searchMyDesigns(search_keyword, False)
    sleep(5)
    template_management_page.check_if_drop_down_list_open()
    template_management_page.check_if_drop_down_list_contains_results_that_include_search_keyword(search_keyword)
    template_management_page.check_dropdown_options_Are_clickable()
    selected_design = template_management_page.click_drop_down_result_1(True)
    template_management_page.check_if_drop_down_list_close()
    data_sources_page.checkIfDesignsLoaded()
    displayed_list = template_management_page.get_all_designs_in_my_designs(True)
    print(displayed_list)
    if len(displayed_list) == 1:
        if displayed_list[0] == selected_design:
            pass
        else:
            raise Exception("Selected result not present.")
    else:
        raise Exception("Showing more than one design.")
    if int(template_management_page.get_showing_n_designs_number()) == 1:
        pass
    else:
        raise Exception("Showing 1 Design not present.")
    data_sources_page.searchMyDesigns("")
    data_sources_page.checkIfDesignsLoaded()
    new_file_list = template_management_page.get_all_designs_in_my_designs(True)
    if initial_design_list == new_file_list:
        pass
    else:
        raise Exception("All designs not present after clearing keywords.")
    new_count = template_management_page.get_showing_n_designs_number()
    if initial_count == new_count:
        pass
    else:
        raise Exception("initial count not matching after clearing count.")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45965():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    registration_page.click_on_profile_edit()
    registration_page.scroll_till_log_out()
    registration_page.click_log_out_button()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    registration_page.check_if_user_navigated_to_sign_in_page()
    account = "zebra06.swdvt@gmail.com"
    help_page.chooseAcc(account)
    registration_page.BugFix_For_Google(account)
    data_sources_page.checkIfOnHomePage()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    if poco(nameMatches="Showing.*Designs").exists():
        pass
    else:
        raise Exception("\"Showing x designs\" text is not displayed.")
    design_list = template_management_page.get_all_designs_in_my_designs(True)
    template_management_page.verify_designs_are_according_to_sort_order(design_list)

    """Step 5,6 and 7 should be verified manually cannot be automated."""

    design_precondition1 = ["design1", "design2", "design3", "design4"]
    design_precondition2 = ["unprintedDesign1", "unprintedDesign2"]
    design_precondition3 = ["unprintedDesign1 copy", "unprintedDesign2 copy"]
    for design in design_precondition1:
        data_sources_page.searchMyDesigns(design)
        data_sources_page.checkIfDesignsLoaded()
        design_info = template_management_page.getDesignInfo(design)
        if "Last print" in design_info:
            pass
        else:
            raise Exception("No Last print date in designs from precondition 1.")
    for design in design_precondition2:
        data_sources_page.searchMyDesigns(design)
        data_sources_page.checkIfDesignsLoaded()
        design_info = template_management_page.getDesignInfo(design)
        if "Last print" in design_info:
            raise Exception("There is last print date in designs from precondition 1.")
    for design in design_precondition3:
        data_sources_page.searchMyDesigns(design)
        data_sources_page.checkIfDesignsLoaded()
        design_info = template_management_page.getDesignInfo(design)
        if "Last print" in design_info:
            raise Exception("There is last print date in designs from precondition 1.")
    template_management_page.verify_design_manipulation_for_all_designs()
    data_sources_page.selectDesignCreatedAtSetUp()
    template_management_page.verify_design_manipulation_options_in_design_menu()
    template_management_page.click_scrim()
    template_management_page.check_design_menu_closed()
    """Step 12 pending"""


"""Semi Automated"""


#
#
# def test_Template_Management_TestcaseID_45921():
#     pass
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickMyDesigns()
#     data_sources_page.checkIfDesignsLoaded()
#     data_sources_page.selectDesignCreatedAtSetUp()
#     data_sources_page.clickPrint()
#     sleep(5)
#     try:
#         common_method.wait_for_element_appearance_namematches("Label")
#     except:
#         raise Exception("Print page did not pop up.")
#     data_sources_page.scroll_till_print()
#     remaining_label_count = template_management_page.get_remaining_label_count()
#     data_sources_page.clickPrint()
#     new_label_count = template_management_page.get_remaining_label_count()
#     if remaining_label_count == new_label_count:
#         pass
#     else:
#         raise Exception("Label count changed even when printer is offline.")
#     data_sources_page.clickBackArrow()
#     try:
#         registration_page.wait_for_element_appearance("My Designs")
#     except:
#         raise Exception("Did not return to \"My Designs\" page")


def test_Template_Management_TestcaseID_46025():
    pass

    common_method.tearDown()
    data_sources_page.checkIfOnHomePage()
    categories = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping",
                  "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose", "XL Shipping"]
    for i in range(2):
        sleep(2)
        login_page.click_Menu_HamburgerICN()
        sleep(2)
        template_management_page.clickCommonDesigns()
        sleep(2)
        template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
        template_management_page.search_design_common_designs(categories[i])
        keyevent("Enter")
        template_management_page.waitForAppearanceOfCategories()
        template_management_page.select_design_common_designs()
        selected_label = template_management_page.select_label_common_designs() + " copy"
        template_management_page.click_copy_to_My_Designs()
        template_management_page_1.wait_for_element_appearance_name_matches_all(
            "has been successfully copied to your workspace")
        sleep(2)
        data_sources_page.clickBackArrow()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickMyDesigns()
        data_sources_page.searchMyDesigns(selected_label)
        data_sources_page.selectDesignCreatedAtSetUp()
        data_sources_page.clickPrint()
        while not poco("Print", enabled=True).exists():
            poco.scroll()
        poco.scroll()
        template_management_page.wait_for_appearance_enabled("Print")
        data_sources_page.clickPrint()
        try:
            template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
        except:
            pass
        sleep(5)
        data_sources_page.clickBackArrow()
        login_page.click_Menu_HamburgerICN()
        data_sources_page.clickHome()
        registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
        first_recently_printed_label = template_management_page_1.get_first_design_in_recently_printed_labels()
        name_first_recently_printed_label = first_recently_printed_label.split("\n")[0]
        date_first_recently_printed_label = first_recently_printed_label.split("\n")[2].split(":")[1].strip()
        current_date = data_sources_page.get_current_date()
        if name_first_recently_printed_label == selected_label:
            if date_first_recently_printed_label == current_date:
                pass
            else:
                raise Exception(
                    "Recently printed date of the top design in recently printed design is not the current date.")
        else:
            raise Exception("First shown design in \"Recently Printed Labels\" is not the recently printed design.")
    common_method.Stop_The_App()


# ###"""""""""""""""""""""""""""""""""""""""""""""""End""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #####""""""""""""""""""""""""""""""""Smoketestcases""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def test_Smoke_Test_TestcaseID_45881():
    """Verify sign in with social account, check the design linked different format file from Google Drive can be printed out successfully"""

    """start the app"""
    common_method.tearDown()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    login_page.click_Menu_HamburgerICN()
    app_settings_page.click_pen_Icon_near_UserName()
    app_settings_page.Scroll_till_Delete_Account()
    app_settings_page.click_Logout_Btn()
    login_page.click_loginBtn()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
    """""""""" check the 3 links at the bottom all can work ("copyright", "Terms & Conditions" and "Privacy Policy")"""""""""""
    smoke_test_android.Verify_SignIn_With_Text_Is_Present()
    smoke_test_android.click_Continue_With_Facebook_Option()
    """""due to some issue, it is directly login to the facebook account without asking for password"""
    login_page.click_Continue_On_Facebbok_Login_Page()
    login_page.click_Menu_HamburgerICN()
    smoke_test_android.Verify_Facebook_UserName_Is_Displaying()
    login_page.click_Continue_On_Facebbok_Login_Page()
    login_page.click_Menu_HamburgerICN()
    smoke_test_android.Verify_Facebook_UserName_Is_Displaying()
    app_settings_page.click_My_Design()
    add_a_printer_screen.click_FirstOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
    add_a_printer_screen.click_SecondOne_In_MyDesign()
    add_a_printer_screen.click_Print_Option()
    add_a_printer_screen.click_Print_Button()
    """"Verify manually it should print successfully"""
    common_method.Stop_The_App()
    common_method.Start_The_App()
    login_page.click_LoginAllow_Popup()
    login_page.click_Allow_ZSB_Series_Popup()
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
# # ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
