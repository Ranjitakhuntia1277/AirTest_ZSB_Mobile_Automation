import inspect

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others_Screen.Others_Screen import Others
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ZSB_Mobile.PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ZSB_Mobile.PageObject.Template_Management.Template_Management_Android import Template_Management_Android
from ...TestSuite.api_call import *
from ...TestSuite.store import *


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


def test_Template_Management_TestcaseID_45921():
    pass

    """Turn off printer"""
    common_method.show_message("Turn off printer associated with the account zebra02.swdvt@gmail.com")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()

    data_sources_page.selectDesignCreatedAtSetUp()
    data_sources_page.clickPrint()
    sleep(5)
    try:
        common_method.wait_for_element_appearance_namematches("Label")
    except:
        raise Exception("Print page did not pop up.")

    raise Exception("Blocked due to bug SMBM-884 ")
    data_sources_page.scroll_till_print()
    remaining_label_count = template_management_page.get_remaining_label_count()

    data_sources_page.clickPrint()
    new_label_count = template_management_page.get_remaining_label_count()
    if remaining_label_count == new_label_count:
        pass
    else:
        raise Exception("Label count changed even when printer is offline.")

    data_sources_page.clickBackArrow()
    try:
        registration_page.wait_for_element_appearance("My Designs")
    except:
        raise Exception("Did not return to \"My Designs\" page")

    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickHome()

    no_of_prints_in_printer_info = template_management_page.get_Labels_left_in_printer_info()
    if no_of_prints_in_printer_info == new_label_count:
        pass
    else:
        raise Exception(
            "number of labels left (x of x prints left) is updated in the Printer information even when the printer is offline.")
    common_method.show_message("Turn on printer associated with the account zebra02.swdvt@gmail.com")
    common_method.show_message("Wait until the printer is online")
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    if no_of_prints_in_printer_info == new_label_count - 1:
        pass
    else:
        raise Exception(
            "number of labels left (x of x prints left) is not updated in the Printer information even after turning on the printer.")
    login_page.click_Menu_HamburgerICN()
    data_sources_page.clickMyDesigns()
    data_sources_page.checkIfDesignsLoaded()
    design = template_management_page.get_all_designs_in_my_designs()
    design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
    if design_last_print_date == data_sources_page.get_current_date():
        pass
    else:
        raise Exception("Last printed date is not up to date.")
    common_method.Stop_The_App()


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
    account = "zebra02.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
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
    account = "zebra03.swdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("Zebra#123456789", account)
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
    common_method.show_message("Check all the link column values are correct, the preview image is correct")
    common_method.show_message("Check the table info is the same as your contact info")
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
    raise Exception(
        "Blocked due to bug :SMBM-1748 - Newly copied label/printed label is not getting added under \"Recently printed labels\" in home page.")
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
    """delete the created contacts"""
    common_method.show_message("Delete 2 contacts\n 1st - firstname-z, lastname-1, wnd firstname-y, lastname-1, , account-zebra02.swdvt@gmail.com, Zebra#123456789")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46021():
    pass

    common_method.tearDown()
    """Step 1-4 pending due to web inconsistency - has to be executed manually"""
    """Step 5-6  - has to be executed manually"""
    common_method.show_message(
        "Update the 46021.xlsx file present in google drive by adding more rows or columns. It is present in the account zebra03.swdvt@gmail.com")
    common_method.show_message(
        "Remove the current 46021.xlsx file present in my data and re link the updated file from google drive.zebra03.swdvt@gmail.com")
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
        help_page.chooseAcc("zebra03.swdvt@gmail.com")
    template_management_page.selectChooseAnOption(3)
    data_sources_page.clickContinue()
    """Step 10 -11  - has to be executed manually"""
    common_method.show_message(
        "Again Update the 46021.xlsx file present in google drive by adding more rows or columns. It is present in the account zebra03.swdvt@gmail.com")
    sleep(2)
    common_method.show_message(
        "Remove the current 46021.xlsx file present in my data and re link the updated file from google drive.")
    sleep(2)
    common_method.show_message("check that the contents are not updated with new data added")
    """check that the label contents are not updated to the latest data source values - cannot be automated and has to be verified manually"""
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    sleep(2)
    common_method.show_message(
        "check that the labels can be printed out correctly with the values, not the latest ones")
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
    common_method.show_message("check that the contents are updated with new data added")
    sleep(2)
    common_method.show_message("check that the labels can be printed out correctly with the latest values")
    """check that the labels can be printed out correctly with the latest values - cannot be automated and has to be verified manually"""
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_48547():
    pass

    """Step 1-6 web portal - pending due to web in consistency"""
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
    # try:
    #     poco(text="Sign In With").wait_for_appearance(timeout=15)
    #     account = "zebra02.swdvt@gmail.com"
    #     registration_page.click_Google_Icon()
    #     try:
    #         registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
    #     except:
    #         raise Exception("Did not navigate to Sign In with google page")
    #     if template_management_page.checkIfAccPresent(account):
    #         help_page.chooseAcc(account)
    #     else:
    #         while not poco(text="Use another account").exists():
    #             poco.scroll()
    #         login_page.click_GooglemailId()
    #         while not poco(text="Add account to device").exists():
    #             poco.scroll()
    #         registration_page.addAccountToDevice()
    #         registration_page.sign_In_With_Google("zsbswdvt1@gmail.com", "Zebra#123456789")
    # except:
    #     pass
    # common_method.wait_for_element_appearance_text("Got It", 20)
    # template_management_page.clickGotIt()
    # try:
    #     registration_page.wait_for_element_appearance_text("Home", 30)
    # except:
    #     raise Exception("Home page dint show up")
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickMyDesigns()
    # data_sources_page.lock_phone()
    # wake()
    # data_sources_page.click_Menu_HamburgerICNWeb()
    # data_sources_page.clickCreateDesignBtn()
    # registration_page.wait_for_element_appearance_text("Select a label size", 10)
    # """Round label selection pending"""
    # for i in range(5):
    #     poco.scroll()
    # data_sources_page.lock_phone()
    # wake()
    # sleep(2)
    # scroll_view = poco(text="Return Address/File Folder").parent().parent()
    # for i in range(30):
    #     scroll_view.swipe("left")
    # data_sources_page.lock_phone()
    # wake()
    # sleep(2)
    # template_management_page.selectRoundLabelInCreate()
    # data_sources_page.clickContinueWeb()
    # data_sources_page.lock_phone()
    # wake()
    # sleep(2)
    # poco(text="Exit Designer").wait_for_appearance(timeout=10)
    # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
    # sleep(3)
    # data_sources_page.lock_phone()
    # wake()
    # data_sources_page.clickAddBarcode()
    # data_sources_page.placeBarcode()
    # data_sources_page.exit_pop_up_after_placing_element_in_new_design()
    # data_sources_page.clickAddText()
    # data_sources_page.placeText()
    # data_sources_page.exit_pop_up_after_placing_element_in_new_design()
    # data_sources_page.lock_phone()
    # wake()
    # sleep(5)
    # common_method.swipe_screen([0.08055555555555556, 0.25427350427350426], [0.9, 0.25427350427350426], 1)
    # sleep(5)
    # data_sources_page.lock_phone()
    # wake()
    # label_name = "48547"
    # data_sources_page.setLabelName(label_name)
    # sleep(5)
    # data_sources_page.exitDesigner()
    common_method.tearDown()
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
    raise Exception("Recently printed label has a bug SMBM-1748 hence unable to proceed.")
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
    data_sources_page.checkIfDesignsLoaded()

    common_method.show_message(
        f"Update objects in the design {design_created} on web. Make sure if objects like barcode, textbox, etc are added provide a fixed value instead of prompt on print., account-zebra02.swdvt@gmail.com, Zebra#123456789")

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
    raise Exception(
        "Blocked due to bug :SMBM-1748 - Newly copied label/printed label is not getting added under \"Recently printed labels\" in home page.")
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
    common_method.show_message("Load another cartridge in the printer.-zebra02.swdvt@gmail.com")
    """Load another cartridge in the printer. Resume printing.-has to be done manually"""
    sleep(5)
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


def test_Template_Management_TestcaseID_46016():
    pass

    """Step 1-4 pending due to web inconsistency execute manually"""

    # start_app("com.android.chrome")
    # sleep(2)
    # poco("com.android.chrome:id/tab_switcher_button").click()
    # sleep(2)
    # try:
    #     poco("com.android.chrome:id/new_tab_view_button").click()
    # except:
    #     poco(text="New tab").click()    # sleep(2)
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
    """Step -3"""
    # template_management_page.click_from_data_file()
    # data_sources_page.clickAddBarcode()
    # data_sources_page.placeBarcode()
    # keyevent("Back")
    """"""

    common_method.tearDown()
    login_page.click_Menu_HamburgerICN()
    data_sources_page.click_My_Data()
    data_sources_page.searchName("csv_file.csv")
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
    sleep(3)
    data_sources_page.verifyIfPreviewIsPresent()
    """cannot verify this part of step 6"""
    common_method.show_message("check that no value shown in the variables in the preview dialog")
    if template_management_page.verify_label_range_navigation_unavailable():
        pass
    else:
        raise Exception("Label range navigation is present.")
    """Step 7 pending"""
    common_method.show_message(
        "Click the first text box and try inserting a sticker/GIF and check if there is any error pop up. Then close the keyboard pop up.")
    template_management_page.fillOrganizationId("abcd")
    keyevent("back")
    template_management_page.fillIndex("xyz")
    keyevent("back")
    scroll_view = poco("android.view.View")
    scroll_view.swipe("down")
    common_method.show_message("Check that preview is shown correctly for the entered values")
    """check that preview is shown correctly"""
    scroll_view.swipe("up")
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46030():
    pass

    """Step 1-5 pending due to web automation"""
    """Select google account
    email-zebra03.swdvt@gmail.com
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
    account = "zebra02.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
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
    account = "zebra06.swdvt@gmail.com"
    if data_sources_page.checkIfAccPresentLink(account):
        help_page.chooseAcc(account)
    else:
        poco("com.google.android.gms:id/add_account_chip_title").click()
        registration_page.sign_In_With_Google("Zebra#123456789", account)
        sleep(2)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    label_range = 4
    data_sources_page.labelRangeSelection(label_range)
    "Unable to automate step 9 - has to be verified manually"
    common_method.show_message(
        "check the table info is the same as your google contact info in this different google account\n \"zebra06.swdvt@gmail.com\"")
    for i in range(label_range):
        data_sources_page.clickNext()
    template_management_page_1.check_element_exists_enabled("Next")
    poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    """Step 12 pending due to web automation - has to be executed manually"""
    common_method.show_message(
        "go to web portal, click print at template in my recently printed labels in home page do the similar things as step 8-11 check the contacts info is still the same as the original google account\n\"zebra03.swdvt@gmail.com\"\n at web portal check labels printed out correctly\ntest_id-46030")


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
    account = "zebra02.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("zebra02.swdvt@gmail.com", "Zebra#123456789")
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
    if number_of_labels == 0:
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
    """Account username - Zebra#123456789
    password- Zebra#123456789"""
    common_method.show_message("Create a contact in this Office365 account.zebra02.swdvt@gmail.com")
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    """Yet to execute as recently printed labels has bug"""
    raise Exception(
        "Blocked due to bug :SMBM-1748 - Newly copied label/printed label is not getting added under \"Recently printed labels\" in home page.")
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
    common_method.show_message("Remove the newly added contact in the office 365 account-zebra02.swdvt@gmail.com")
    common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46035():
    pass

    """Step 1-5 pending due to web automation"""
    """Select Office 365 account
    email-zebra06.swdvt@gmail.com
    password - Zebra#123456789 in while creating template in web"""
    common_method.tearDown()
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
    """ Office 365 contacts """
    account = "zebra06.swdvt@gmail.com"
    data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    template_management_page.verify_label_navigation()
    while not poco("Print").exists():
        poco.scroll()
    label_range = 4
    data_sources_page.labelRangeSelection(label_range)
    common_method.show_message(
        "check the table info is the same as your Office365 contact info in this different Microsoft account - zebra06.swdvt@gmail.com")
    "Unable to automate -check the table info is the same as your Office365 contact info in this different Microsoft account has to be done manually"
    for i in range(label_range):
        data_sources_page.clickNext()
    template_management_page_1.check_element_exists_enabled("Next")
    poco.scroll()
    data_sources_page.clickPrint()
    template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
    common_method.show_message(
        "go to web portal, click print at template in my recently printed labels in home page do the similar things as step 8-11 check the contacts info is still the same as the original Microsoft account at web portal check labels printed out correctly\"zebra03.swdvt@gmail.com")
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
    account = "zebra02.swdvt@gmail.com"
    if template_management_page.checkIfAccPresent(account):
        help_page.chooseAcc(account)
    else:
        while not poco(text="Use another account").exists():
            poco.scroll()
        login_page.click_GooglemailId()
        while not poco(text="Add account to device").exists():
            poco.scroll()
        registration_page.addAccountToDevice()
        registration_page.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")
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
    """google contacts """
    account = "zebra03.swdvt@gmail.com"
    data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
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
    common_method.show_message("Create 3 new contacts in this Office365 account., zebra03.swdvt@gmail.com")
    registration_page.wait_for_element_appearance("Home", 20)
    registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
    """Yet to execute as recently printed labels has bug"""
    raise Exception(
        "Blocked due to bug :SMBM-1748 - Newly copied label/printed label is not getting added under \"Recently printed labels\" in home page.")
    template_management_page_1.click_first_design_in_recently_printed_labels()
    data_sources_page.clickPrint()
    common_method.wait_for_element_appearance_namematches("Label", 20)
    sleep(10)
    data_sources_page.verifyIfPreviewIsPresent()
    while not poco("Print").exists():
        poco.scroll()
    number_of_labels = int(template_management_page.get_total_labels_printing())
    if number_of_labels == 18:
        pass
    else:
        if number_of_labels > 18:
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
    common_method.show_message("Remove the 3 newly added contacts in the office 365 account.zebra03.swdvt@gmail.com")
    common_method.Stop_The_App()
