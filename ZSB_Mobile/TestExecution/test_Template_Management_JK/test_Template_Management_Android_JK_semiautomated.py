from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# wake()
# start_app("com.zebra.soho_app")
sleep(2.0)
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
template_management_page_1 = Template_Management_Android(poco)


def test_Template_Management_TestcaseID_46021():
    pass

    common_method.Start_The_App()
    """Step 1-4 pending due to web inconsistency - has to be executed manually"""
    """Step 5-6  - has to be executed manually"""
    sleep(600)
    """Open My designs"""
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    data_sources_page.searchMyDesigns("46021")
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    """Select column"""
    if poco(text="Choose an account").exists():
        help_page.chooseAcc("zsbswdvt@gmail.com")
    template_management_page.selectChooseAnOption(3)
    data_sources_page.clickContinue()
    """Step 10 -11  - has to be executed manually"""
    sleep(600)
    """check that the label contents are not updated to the latest data source values - cannot be automated and has to be verified manually"""
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    """check that the labels can be printed out correctly with the values, not the latest one - cannot be automated and has to be verified manually"""
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    sleep(3)
    data_sources_page.clickBackArrow()
    data_sources_page.selectDesignCreatedAtSetUp()
    """Click print"""
    data_sources_page.clickPrint()
    """Select column"""
    template_management_page.selectChooseAnOption(3)
    data_sources_page.clickContinue()
    try:
        common_method.wait_for_element_appearance_namematches("Label")
    except:
        raise Exception("preview dialog did not open.")
    """check that the content is updated with new column data - cannot be automated and has to be verified manually"""
    """check that the labels can be printed out correctly with the latest values - cannot be automated and has to be verified manually"""
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47792():
    pass

    "Step 1-3 pending due to web inconsistency"
    common_method.Start_The_App()
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
        raise Exception("Print value not modified on clicking backspace.")
    else:
        pass
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_48547():
    pass

    """Step 1-6 web portal - pending due to web in consistency"""
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    poco("com.android.chrome:id/new_tab_view_button").click()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
    sleep(2)
    data_sources_page.clickEnter()
    sleep(3)
    try:
        poco(text="Sign In With").wait_for_appearance(timeout=15)
        account = "zebraidctest@gmail.com"
        registration_page.click_Google_Icon()
        try:
            registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
        except:
            raise Exception("Did not navigate to Sign In with google page")
        if template_management_page.checkIfAccPresent(account):
            help_page.chooseAcc(account)
        else:
            while not poco(text="Use another account").exists():
                poco.scroll()
            login_page.click_GooglemailId()
            while not poco(text="Add account to device").exists():
                poco.scroll()
            registration_page.addAccountToDevice()
            registration_page.sign_In_With_Google("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
    except:
        pass
    common_method.wait_for_element_appearance_text("Got It", 20)
    template_management_page.clickGotIt()
    try:
        registration_page.wait_for_element_appearance_text("Home", 30)
    except:
        raise Exception("Home page dint show up")
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.clickMyDesigns()
    data_sources_page.lock_phone()
    wake()
    data_sources_page.click_Menu_HamburgerICNWeb()
    data_sources_page.clickCreateDesignBtn()
    registration_page.wait_for_element_appearance_text("Select a label size", 10)
    """Round label selection pending"""
    for i in range(5):
        poco.scroll()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    scroll_view = poco(text="Return Address/File Folder").parent().parent()
    for i in range(30):
        scroll_view.swipe("left")
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    template_management_page.selectRoundLabelInCreate()
    data_sources_page.clickContinueWeb()
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    poco(text="Exit Designer").wait_for_appearance(timeout=10)
    common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
    sleep(3)
    data_sources_page.lock_phone()
    wake()
    data_sources_page.clickAddBarcode()
    data_sources_page.placeBarcode()
    data_sources_page.exit_pop_up_after_placing_element_in_new_design()
    data_sources_page.clickAddText()
    data_sources_page.placeText()
    data_sources_page.exit_pop_up_after_placing_element_in_new_design()
    data_sources_page.lock_phone()
    wake()
    sleep(5)
    common_method.swipe_screen([0.08055555555555556, 0.25427350427350426], [0.9, 0.25427350427350426], 1)
    sleep(5)
    data_sources_page.lock_phone()
    wake()
    label_name = "48547"
    data_sources_page.setLabelName(label_name)
    sleep(5)
    data_sources_page.exitDesigner()
    common_method.Start_The_App()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    design_created = "48547"
    data_sources_page.searchMyDesigns(design_created)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    try:
        common_method.wait_for_element_appearance_namematches("Showing")
    except:
        raise Exception("My designs did not load load properly")

    """Web objects update pending due to web inconsistency."""

    common_method.Start_The_App()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    """Search and select design created in web"""
    design_created = "48547"
    data_sources_page.searchMyDesigns(design_created)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    try:
        common_method.wait_for_element_appearance_namematches("Showing")
    except:
        raise Exception("My designs did not load load properly")

def test_Template_Management_TestcaseID_45925():
    pass

    common_method.Start_The_App()
    initial_prints_left = template_management_page.get_Labels_left_in_printer_info().split(" ")[0]
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(5)
    try:
        common_method.wait_for_element_appearance_namematches("Label")
    except:
        raise Exception("Print page did not pop up.")
    while not poco("Print").exists():
        poco.scroll()
    remaining_label_count = template_management_page.get_remaining_label_count()
    template_management_page.changeCopiesCount(remaining_label_count + 1)
    keyevent("Enter")
    sleep(5)
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Printer cover closed")
    sleep(20)
    """Load another cartridge in the printer. Resume printing.-has to be done manually"""
    remainingLabels = template_management_page.get_remaining_label_count()
    if remainingLabels > 0:
        pass
    else:
        raise Exception("Labels left not updated after changing empty cartridge.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    new_prints_left = template_management_page.get_Labels_left_in_printer_info().split(" ")[0]
    if new_prints_left > initial_prints_left:
        pass
    else:
        raise Exception("total number of labels left (x of x prints left) is not updated in the Printer information")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46030():
    pass

    """Step 1-5 pending due to web automation"""
    """Select google account
    email-zsbswdvt@gmail.com
    password - zsbswdvt@1234 in while creating template in web"""
    data_sources_page.clearAppData()
    common_method.Start_The_App()
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
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    search_label_name = "46030"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    poco("Accept").wait_for_appearance(timeout=10)
    template_management_page.clickAccept()
    """ google contacts """
    account = "zsbswdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("zsbswdvt@1234", account)
        sleep(2)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    label_range = 4
    data_sources_page.labelRangeSelection(label_range)
    "Unable to automate step 9 - has to be verified manually"
    for i in range(label_range):
        data_sources_page.clickNext()
    template_management_page_1.check_element_exists_enabled("Next")
    poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    """Step 12 pending due to web automation - has to be executed manually"""


def test_Template_Management_TestcaseID_46031():
    pass

    """Step 1-5 pending due to web automation"""

    data_sources_page.clearAppData()
    common_method.Start_The_App()
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
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    search_label_name = "46031"
    data_sources_page.searchMyDesigns(search_label_name)
    common_method.wait_for_element_appearance_namematches("Showing")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(2)
    poco("Accept").wait_for_appearance(timeout=10)
    template_management_page.clickAccept()
    """ google contacts """
    account = "zsbswdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("zsbswdvt@1234", account)
        sleep(2)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
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
    while not poco("Print").exists():
        poco.scroll()
    """cannot automate - check all the link column values are correct, the preview image is correct"""
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.labelRangeSelection(4)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    start_app("com.android.chrome")
    sleep(2)
    poco("com.android.chrome:id/tab_switcher_button").click()
    sleep(2)
    poco("com.android.chrome:id/new_tab_view_button").click()
    sleep(2)
    poco(text="Search or type URL").click()
    sleep(2)
    poco(text="Search or type URL").set_text("https://contacts.google.com/")
    data_sources_page.clickEnter()
    sleep(2)
    data_sources_page.lock_phone()
    wake()
    sleep(2)
    common_method.wait_for_element_appearance_text("Contacts", 20)
    try:
        common_method.wait_for_element_appearance_text("Use the Contacts app")
        if poco(text="Stay on web").exists():
            poco(text="Stay on web").click()
    except:
        pass
    template_management_page.changeAccInAddContacts(account)
    common_method.wait_for_element_appearance_text("Contacts")
    try:
        common_method.wait_for_element_appearance_text("Use the Contacts app")
        if poco(text="Stay on web").exists():
            poco(text="Stay on web").click()
    except:
        pass
    template_management_page.deleteContactGoogleContacts()
    template_management_page.createContact("z", "1")
    sleep(2)
    template_management_page.createContact("y", "1")
    stop_app("com.android.chrome")
    registration_page.wait_for_element_appearance("Home", 20)
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    """Yet to execute as recently printed labels has bug"""
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 13:
        pass
    else:
        if number_of_labels > 13:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate -
    check all the link column values are correct, the preview image is correct
    check the delete contact is not shown
    check the updated value shown in that contact
    check the newly added contacts are shown
    -has to be done manually"""
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.choose_label_print_range()
    """cannot automate - check the table info is updated accordingly - has to be checked manually"""
    data_sources_page.clickConfirm()
    sleep(3)
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46034():
    pass

    """Step 1-5 pending due to web automation"""
    data_sources_page.clearAppData()
    common_method.Start_The_App()
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
        registration_page.sign_In_With_Google("zebraidctest@gmail.com", "zebraidctest@1234")
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    search_label_name = "46034"
    data_sources_page.searchMyDesigns(search_label_name)
    common_method.wait_for_element_appearance_namematches("Showing")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(2)
    if poco("Accept").exists():
        template_management_page.clickAccept()
    data_sources_page.checkIfAccPresentLink(account)
    data_sources_page.chooseAccToLinkFile(account)
    try:
        registration_page.wait_for_element_appearance_text("Sign in to ZSB Series", 20)
        poco.scroll()
        data_sources_page.clickContinueWeb()
    except:
        pass
    try:
        registration_page.wait_for_element_appearance_text("ZSB Series wants access to your Google Account", 20)
        while not poco(text="Continue").exists():
            poco.scroll()
        data_sources_page.clickContinueWeb()
    except:
        pass
    try:
        registration_page.wait_for_element_appearance_text(" wants to access your Google Account", 20)
        while not poco(text="Allow").exists():
            poco.scroll()
        data_sources_page.clickAllow_Text()
    except:
        pass
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 1:
        pass
    else:
        error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
        raise Exception(error)
    data_sources_page.clickLabelRange()
    sleep(2)
    if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
        pass
    else:
        raise Exception("Tabel is not empty.")
    data_sources_page.clickBackArrow()
    """Step - 7 pending as input fields are not editable."""
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()

    """Cannot automate adding new contact to office 365 contacts-has to be done manually"""
    """Manual interruption required to add contacts in office 365"""
    """Account username - zsbswdvt@1234
    password- hmWepX4AUMLa"""


def test_Template_Management_TestcaseID_46034_1():
    pass

    """execute after executing test case 46034 first half"""
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    """Yet to execute as recently printed labels has bug"""
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 1:
        pass
    else:
        error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
        raise Exception(error)
    data_sources_page.clickLabelRange()
    sleep(2)
    if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
        raise Exception("Tabel is empty even after adding a contact.")
    data_sources_page.clickBackArrow()
    """Step - 7 pending as input fields are not editable."""
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46035():
    pass

    """Step 1-5 pending due to web automation"""
    """Select Office 365 account
    email-zsbswdvt1@gmail.com
    password - Zebra#123456789 in while creating template in web"""
    data_sources_page.clearAppData()
    common_method.Start_The_App()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    registration_page.click_Google_Icon()
    try:
        registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    except:
        raise Exception("Did not navigate to Sign In with google page")
    account = "zebratest850@gmail.com"
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
    try:
        registration_page.wait_for_element_appearance("Home", 20)
    except:
        raise Exception("home page dint show up")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    search_label_name = "46035"
    data_sources_page.searchMyDesigns(search_label_name)
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    poco("Accept").wait_for_appearance(timeout=10)
    template_management_page.clickAccept()
    """ google contacts """
    account = "zsbswdvt@gmail.com"
    """ Office 365 contacts """
    account = "zsbswdvt1@gmail.com"
    data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    label_range = 4
    data_sources_page.labelRangeSelection(label_range)
    "Unable to automate -check the table info is the same as your Office365 contact info in this different Microsoft account has to be done manually"
    for i in range(label_range):
        data_sources_page.clickNext()
    template_management_page_1.check_element_exists_enabled("Next")
    poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    """Step 12 pending due to web automation - has to be executed manually"""




def test_Template_Management_TestcaseID_46036():
    pass

    """Step 1-5 pending due to web automation"""

    data_sources_page.clearAppData()
    common_method.Start_The_App()
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
    data_sources_page.clickMyDesigns()
    common_method.wait_for_element_appearance_namematches("Showing")
    search_label_name = "46031"
    data_sources_page.searchMyDesigns(search_label_name)
    common_method.wait_for_element_appearance_namematches("Showing")
    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(2)
    poco("Accept").wait_for_appearance(timeout=10)
    template_management_page.clickAccept()
    """ google contacts """
    account = "zsbswdvt@gmail.com"
    data_sources_page.signInWithMicrosoft(account, "hmWepX4AUMLa!9E", False)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 27:
        pass
    else:
        if number_of_labels > 27:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    while not poco("Print").exists():
        poco.scroll()
    """cannot automate - check all the link column values are correct, the preview image is correct"""
    """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
    data_sources_page.labelRangeSelection(4)
    sleep(3)
    template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    """Cannot automate adding new contact to office 365 contacts-has to be done manually"""
    registration_page.wait_for_element_appearance("Home", 20)
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    """Yet to execute as recently printed labels has bug"""
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 28:
        pass
    else:
        if number_of_labels > 28:
            raise Exception("Label amount is more than the number of contacts.")
        else:
            raise Exception("Label amount is less than the number of contacts.")
    scroll_view = poco("android.widget.ScrollView")
    """verify label range navigation works"""
    template_management_page.verify_label_navigation()
    """cannot automate -
    check all the link column values are correct, the preview image is correct
    check the delete contact is not shown
    check the updated value shown in that contact
    check the newly added contacts are shown
    -has to be done manually"""
    while poco(nameMatches=".*Label . of .*").exists():
        scroll_view.swipe("up")
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.choose_label_print_range()
    """cannot automate - check the table info is updated accordingly - has to be checked manually"""
    data_sources_page.clickConfirm()
    sleep(3)
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    common_method.Stop_The_App()




def test_Template_Management_TestcaseID_50656():
    pass

    common_method.Start_The_App()
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
    common_method.Stop_The_App()
    """Sign in same account in web portal, go to my designs, create/edit a design, add an image, set it to prompt at print needs to be executed manually due to web inconsistency """
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
    # registration_page.wait_for_element_appearance_text("Home", 10)
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickMyDesigns()
    # data_sources_page.lock_phone()
    # wake()
    # sleep(2)
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickCreateDesignBtn()
    # sleep(5)
    # data_sources_page.selectLabelSize()
    # data_sources_page.clickContinueWeb()
    # data_sources_page.lock_phone()
    # wake()
    # common_method.wait_for_element_appearance_text("Exit Designer")
    # a,b = poco(text="Undo last operation. Max of 10 undo steps are supported.").get_position()
    # while not poco(text="Add picture").exists():
    #     common_method.swipe_screen([0.9, b], [0.3, b], 1)
    #     data_sources_page.lock_phone()
    #     wake()
    #     sleep(3)
    # data_sources_page.clickAddPhoto()
    # data_sources_page.placePhoto()
    # while not poco(text="Exit Designer").exists():
    #     common_method.swipe_screen([0.1, b], [0.7, b], 1)
    #     data_sources_page.lock_phone()
    #     wake()
    #     sleep(3)
    design_name = "Pic_PromptAtPrint"
    # data_sources_page.setLabelName(design_name)
    # sleep(5)
    # data_sources_page.exitDesigner()
    """Web pending due to inconsistent behaviour"""
    common_method.Start_The_App()
    registration_page.wait_for_element_appearance("Home")
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
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    data_sources_page.clickBackArrow()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
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
    while not poco("Print").exists():
        poco.scroll()
    template_management_page.wait_for_appearance_enabled("Print")
    data_sources_page.clickPrint()
    try:
        template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    except:
        raise Exception("Print not successful.")
    common_method.Stop_The_App()