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
from ZSB_Mobile.PageObject.Template_Management_Sceen_JK.Template_Management_Sceen_JK import Template_Management_Screen


class Android_App_Registration:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
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


def test_Template_Management_TestcaseID_45981():
    pass


#
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if template_management_page.verify_default_sort_my_designs():
#     pass
# else:
#     raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
# template_management_page.click_sort_my_designs()
# template_management_page.verify_sort_options_my_designs()
# poco("Scrim").click()
# design_names = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_design_names_follow_order(design_names)
# expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel", "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
# for design in expected_designs:
#     if design in design_names:
#         pass
#     else:
#         error = "Design " + design + " not present."
#         raise Exception(error)
# if template_management_page.check_design_count_title(len(design_names)):
#     pass
# else:
#     raise Exception("Count of number of designs in the tile doesnt match with actual count.")
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if template_management_page.verify_default_sort_my_designs():
#     pass
# else:
#     raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
# template_management_page.click_sort_my_designs()
# template_management_page.verify_sort_options_my_designs()
# poco("Scrim").click()
# design_names = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_design_names_follow_order(design_names)
# expected_designs = ["IconGiftLabel", "1_Asset", "2_Asset", "3_Address", "4_Address", "5_Barcode", "6_IconGiftLabel", "$Address", "$Asset", "$Barcode", "$IconGiftLabel"]
# for design in expected_designs:
#     if design in design_names:
#         pass
#     else:
#         error = "Design" + design + "not present."
#         raise Exception(error)
# if template_management_page.check_design_count_title(len(design_names)):
#     pass
# else:
#     raise Exception("Count of number of designs in the tile doesn't match with actual count.")


def test_Template_Management_TestcaseID_45984():
    pass


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if template_management_page.verify_default_filter_my_designs():
#     pass
# else:
#     raise Exception("Default filter is not \"All sizes\" in my designs.")
# template_management_page.click_filter_my_designs("All sizes")
# if template_management_page.filter_options(True) > 1:
#     pass
# else:
#     raise Exception("No other filter option present other than All sizes.")
# poco("Scrim").click()
# label_sizes_present = template_management_page.get_all_designs_size_in_my_designs()
# template_management_page.click_filter_my_designs("All sizes")
# filter_options = template_management_page.filter_options()
# poco("Scrim").click()
# for label_sizes in filter_options:
#     if label_sizes in label_sizes_present:
#         pass
#     else:
#         raise Exception(f"label with {label_sizes} not present.")
# if template_management_page.verify_sort_order_my_designs("A-Z"):
#     pass
# else:
#     raise Exception("Designs not sorted in A-Z order.")
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if template_management_page.verify_default_filter_my_designs():
#     pass
# else:
#     raise Exception("Default filter is not \"All sizes\" in my designs.")
# template_management_page.click_filter_my_designs("All sizes")
# if template_management_page.filter_options(True) > 1:
#     pass
# else:
#     raise Exception("No other filter option present other than All sizes.")
# poco("Scrim").click()
# label_sizes_present = template_management_page.get_all_designs_size_in_my_designs()
# template_management_page.click_filter_my_designs("All sizes")
# filter_options = template_management_page.filter_options()
# poco("Scrim").click()
# for label_sizes in filter_options:
#     if label_sizes in label_sizes_present:
#         pass
#     else:
#         raise Exception(f"label with {label_sizes} not present.")
# if template_management_page.verify_sort_order_my_designs("A-Z"):
#     pass
# else:
#     raise Exception("Designs not sorted in A-Z order.")


def test_Template_Management_TestcaseID_45987():
    pass


"""Login"""


# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# common_method.wait_for_element_appearance_namematches("Address")
# template_management_page.search_design_common_designs("Address")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Categories")
# template_management_page.select_design_common_designs()
# if template_management_page.verify_default_sort_my_designs():
#     pass
# else:
#     raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
# template_management_page.click_sort_common_designs()
# template_management_page.verify_sort_options_my_designs()
# poco("Scrim").click()
# if template_management_page.verify_default_filter_my_designs():
#     pass
# else:
#     raise Exception("Default filter is not \"All sizes\"")
# template_management_page.click_filter_common_designs()
# if template_management_page.filter_options(True) > 1:
#     pass
# else:
#     raise Exception("No other filter option present other than All sizes.")
# poco("Scrim").click()
# template_management_page.click_sort_common_designs()
# sleep(3)
# template_management_page.select_sort_order("Z-A")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# template_management_page.click_filter_common_designs()
# label_size = template_management_page.select_label_size()
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_size = template_management_page.get_all_designs_size_in_my_designs()
# try:
#     if len(design_size) == 1:
#         if design_size[0] == label_size:
#             pass
# except:
#     raise Exception("Label size chosen in filter doesnt match the filtered result label size")
# template_management_page.click_sort_common_designs()
# template_management_page.select_sort_order("A-Z")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# template_management_page.click_sort_common_designs()
# template_management_page.select_sort_order("Z-A")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)


def test_Template_Management_TestcaseID_45992():
    pass


"""Login"""


# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# common_method.wait_for_element_appearance_namematches("Address")
# template_management_page.search_design_common_designs("Name")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Categories")
# template_management_page.select_design_common_designs()
# if template_management_page.verify_default_sort_my_designs():
#     pass
# else:
#     raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
# template_management_page.click_sort_common_designs()
# template_management_page.verify_sort_options_my_designs()
# poco("Scrim").click()
# if template_management_page.verify_default_filter_my_designs():
#     pass
# else:
#     raise Exception("Default filter is not \"All sizes\"")
# template_management_page.click_filter_common_designs()
# if template_management_page.filter_options(True) > 1:
#     pass
# else:
#     raise Exception("No other filter option present other than All sizes.")
# poco("Scrim").click()
# template_management_page.click_sort_common_designs()
# sleep(3)
# template_management_page.select_sort_order("Z-A")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# template_management_page.click_filter_common_designs()
# label_size = template_management_page.select_label_size()
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_size = template_management_page.get_all_designs_size_in_my_designs()
# if len(design_size) == 1:
#     if design_size[0] == label_size:
#         pass
#     else:
#         raise Exception("Label size chosen in filter doesnt match the filtered result label size")
# else:
#     raise Exception("More than 1 label size is present after filtering.")
#
# template_management_page.click_sort_common_designs()
# template_management_page.select_sort_order("A-Z")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# template_management_page.click_sort_common_designs()
# template_management_page.select_sort_order("Z-A")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)


def test_Template_Management_TestcaseID_45994():
    pass


"""Login"""


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# template_management_page.turn_off_wifi()
# template_management_page.click_filter_my_designs()
# label_size = template_management_page.select_label_size()
# sleep(3)
# poco("Scrim").click()
# if template_management_page.verify_connection_error_app():
#     pass
# else:
#     raise Exception("Connection lost error not displayed.")
# template_management_page.turn_on_wifi()
# template_management_page.click_filter_my_designs()
# label_size = template_management_page.select_label_size()
# sleep(3)
# design_name = template_management_page.get_first_design_name_my_designs()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# title_count = template_management_page.get_showing_n_designs_number()
# if len(design_list) == int(title_count):
#     pass
# else:
#     raise Exception("Count in title doesn't match the number of designs.")
# template_management_page.turn_off_wifi()
# template_management_page.search_design_common_designs(design_name)
# template_management_page.verify_connection_error_app()
# template_management_page.turn_on_wifi()
# template_management_page.search_design_common_designs(design_name)
# try:
#     template_management_page.wait_for_suggestions_to_appear()
# except:
#     raise Exception("dropdown did not appear.")
# template_management_page.check_dropdown_options_Are_clickable()
# template_management_page.click_drop_down_result_1()
# try:
#     template_management_page.wait_for_suggestions_to_appear()
#     raise Exception("dropdown is present.")
# except:
#     pass
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# if len(design_list) == 1:
#     if design_list[0] == design_name:
#         pass
#     else:
#         raise Exception("The resulting design name doesn't match search name")
# else:
#     raise Exception("There are more than 1 result.")
# title_count = template_management_page.get_showing_n_designs_number()
# if int(title_count) == 1:
#     pass
# else:
#     raise Exception("Title is not 'Showing 1 Design'.")


def test_Template_Management_TestcaseID_46010():
    pass


# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# common_method.wait_for_element_appearance_namematches("Address")
# """"""
# initial_categories_list = template_management_page.get_all_designs_in_my_designs()
# if template_management_page.verify_search_placeholder():
#     pass
# else:
#     raise Exception("Search design placeholder not present.")
# if template_management_page.verifySearchIcon():
#     pass
# else:
#     raise Exception("Search icon not present")
# template_management_page.search_design_common_designs("/")
# common_method.wait_for_element_appearance_namematches("/", 20)
# category_list_drop_down = template_management_page.get_drop_down_list_my_designs(True)
# keyevent("Enter")
# category_list = template_management_page.get_all_categories_in_common_designs(True)
# if category_list == category_list_drop_down:
#     pass
# else:
#     raise Exception("All Categories not displayed in drop down.")
# search_text = "/"
# template_management_page.search_design_common_designs(search_text)
# common_method.wait_for_element_appearance_namematches(search_text, 20)
# design_list_drop_down = template_management_page.get_all_search_results_in_search_designs()
# # designs_list = template_management_page.get_all_designs_in_search_designs(True)
# search_text = "-"
# template_management_page.search_design_common_designs(search_text)
# common_method.wait_for_element_appearance_namematches(search_text, 20)
# sleep(3)
# try:
#     template_management_page.wait_for_suggestions_to_appear()
# except:
#     raise Exception("dropdown did not appear.")
# name_dropdown = template_management_page.click_drop_down_result_1(True)
# if template_management_page.verifySearchResults_n(1):
#     pass
# else:
#     raise Exception("Search results(1) not present.")
# names_result = template_management_page.get_all_designs_in_search_designs(True)
# if name_dropdown == names_result[0]:
#     pass
# else:
#     raise Exception("Selected design not displayed.")
# template_management_page.search_design_common_designs("")
# keyevent("Enter")
# # common_method.wait_for_element_appearance_namematches("Address")
# new_categories_list = template_management_page.get_all_designs_in_my_designs()
# if initial_categories_list == new_categories_list:
#     pass
# template_management_page.search_design_common_designs("~`!@#$%^&*()_-+={}[]|/\:;"'<>,.?'"")
# if template_management_page.verifyNoResultsDropDown():
#     pass
# else:
#     raise Exception("No results for \"searched text\" text not displayed.")
# template_management_page.search_design_common_designs("")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Address")
# new_categories_list = template_management_page.get_all_designs_in_my_designs()
# if initial_categories_list == new_categories_list:
#     pass


def test_Template_Management_TestcaseID_46014():
    pass


"""Login"""
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
"""ask tarun"""
# common_method.wait_for_element_appearance_namematches("Address")
""""""
# template_management_page.select_design_common_designs()
# if template_management_page.verify_search_placeholder():
#     pass
# else:
#     raise Exception("Search design place holder doesnt have 'Search Design'.")
# template_management_page.search_design_common_designs("Address")
# if poco(nameMatches="Categories.*").exists():
#     raise Exception("Drop down not present.")
# else:
#     pass
# template_management_page.verify_search_drop_down_results("Address")
"""Step -5 pending yet to do"""


# keyevent("Enter")
# try:
#     common_method.wait_for_element_appearance_namematches("Categories")
# except:
#     raise Exception("Drop down present even after clicking search on keyboard.")
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# search_text = "Address"
# for i in design_list:
#     if search_text.lower() in i.lower():
#         pass
#     else:
#         raise Exception("search text not present in one of the results.")
# template_management_page.click_filter_common_designs()
# label_size = template_management_page.select_label_size()
# sleep(3)
# design_size = template_management_page.get_all_designs_size_in_my_designs()
# try:
#     if len(design_size) == 1:
#         if design_size[0] == label_size:
#             pass
# except:
#     raise Exception("Label size chosen in filter doesnt match the filtered result label size")
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# init_no_of_designs = len(design_list)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# template_management_page.click_sort_common_designs()
# sleep(3)
# template_management_page.select_sort_order("Z-A")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# no_of_designs = len(design_list)
# if no_of_designs == init_no_of_designs:
#     pass
# else:
#     raise Exception("The number of designs are not same before and after sorting.")
# template_management_page.click_sort_common_designs()
# sleep(3)
# template_management_page.select_sort_order("A-Z")
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# no_of_designs = len(design_list)
# if no_of_designs == init_no_of_designs:
#     pass
# else:
#     raise Exception("The number of designs are not same before and after sorting.")
# help_page.clickBackArrow()
# template_management_page.select_design_common_designs()
# if template_management_page.verify_search_placeholder():
#     pass
# else:
#     raise Exception("Search box not cleared.")


def test_Template_Management_TestcaseID_46016():
    pass


# start_app("com.android.chrome")
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
"""Step -3"""
# template_management_page.click_from_data_file()
# data_sources_page.clickAddBarcode()
# data_sources_page.placeBarcode()
# keyevent("Back")
""""""


# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# data_sources_page.searchName("csv_file.csv")
# sleep(2)
# data_sources_page.remove_File()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns("46016")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.checkManualInput_checkbox()
# data_sources_page.clickContinue()
# data_sources_page.verifyIfPreviewIsPresent()
# try:
#     template_management_page.verify_print_preview("blank")
# except:
#     raise Exception("Preview is not blank as expected.")
# if template_management_page.verify_label_range_navigation_unavailable():
#     pass
# else:
#     raise Exception("Label range navigation is present.")
# template_management_page.fillOrganizationId("abcd")
# keyevent("back")
# template_management_page.fillIndex("xyz")
# keyevent("back")
# scroll_view = poco("android.view.View")
# scroll_view.swipe("down")
# try:
#     template_management_page.verify_print_preview("46016")
# except:
#     raise Exception("Preview is not blank as expected.")
# scroll_view.swipe("up")
# data_sources_page.clickPrint()


def test_Template_Management_TestcaseID_46019():
    pass


# common_method.Start_The_App()
# """Step 1-4 pending due to web inconsistency"""
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("UnevenC|R")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# data_sources_page.clickPrint()
# """Select column"""
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header()
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# """check that only the selected column values shown in the table - pending"""
# """Check and uncheck select all"""
# template_management_page.select_All()
# template_management_page.select_All(False)
# """check select all"""
# template_management_page.select_All()
# """Step 10 -15 blocked due to BUG ID - SMBM-1134"""
# data_sources_page.clickConfirm()
# """Check"""
# scroll_view = poco("android.view.View")
# scroll_view.swipe("down")
# template_management_page.verify_label_navigation()
# data_sources_page.clickPrint()
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46020():
    pass


# common_method.Start_The_App()
# """Step 1-4 pending due to web inconsistency"""
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("UnevenC|R")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# data_sources_page.clickPrint()
# """Select column"""
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header(True)
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# """Step 7 pending"""
# try:
#     registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
# except:
#     raise Exception("Print preview not present.")
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.verify_label_range_is_All()
# """check that only the selected column values shown in the table - pending"""
# """select arbitrary number of columns"""
# count_checked_boxes = 4
# actual_checked_box_count = data_sources_page.labelRangeSelection(count_checked_boxes, False)
# checkbox = poco("android.widget.CheckBox")
# """Check first row is greyed out"""
# attribute = common_method.getAttr(checkbox[2], "enabled")
# if attribute == False:
#     pass
# else:
#     raise Exception("First row is not greyed out")
# data_sources_page.clickConfirm()
# """Check"""
# template_management_page.check_total_label_for_print_count(actual_checked_box_count)
# while not poco(nameMatches="Label.*").exists():
#     scroll_view = poco("android.view.View")
#     scroll_view.swipe("down")
# template_management_page.verify_label_navigation()
# data_sources_page.clickPrint()
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46022():
    pass


# start_app("com.android.chrome")
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
# # data_sources_page.setLabelName(label_name)
# # data_sources_page.exitDesigner()
# start_app("com.zebra.soho_app")
# poco("Open navigation menu").wait_for_appearance(timeout=10)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns(label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
"""Step -6 continue"""


def test_Template_Management_TestcaseID_47791():
    pass


# start_app("com.android.chrome")
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
# poco(text="Exit Designer").wait_for_appearance(timeout=10)
# common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
# data_sources_page.lock_phone()
# wake()
"""ask Tarun"""
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


# start_app("com.zebra.soho_app")
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns("47791")
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# if template_management_page.verify_if_on_relink_data_source_page():
#     pass
# else:
#     raise Exception("Not on Relink data source page.")
# if template_management_page.verify_duplicate_previous_next_button():
#     raise Exception("Duplicate Previous and Next button exists.")
# else:
#     pass


def test_Template_Management_TestcaseID_47792():
    pass


# "Step 1-3 pending due to web inconsistency"
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing", 10)
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("CurrencyGBP")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# initial_print_value = template_management_page.get_print_value()
# template_management_page.click_print_value()
# keyevent("keyword del")
# keyevent("Enter")
# modified_print_value = template_management_page.get_print_value()
# if initial_print_value == modified_print_value:
#     raise Exception("Print value not modified on clicking backspace.")
# else:
#     pass


def test_Template_Management_TestcaseID_47824():
    pass


# "I am here"
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing", 10)
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("Blank")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# registration_page.wait_for_element_appearance("Print")
# sleep(3)
# data_sources_page.verifyIfPreviewIsPresent()
# registration_page.wait_for_element_appearance("Print")
# data_sources_page.clickPrint()
# """cannot verify - Check ZSB app should not show pint complete popup or the print button is disabled"""
# "No pop up and Print is enabled."


def test_Template_Management_TestcaseID_47947():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing", 10)
# initial_count = int(template_management_page.get_showing_n_designs_number())
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("47947")
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDeleteDesign()
# template_management_page.turn_off_wifi()
# template_management_page.clickDeleteDesign()
"""Design delete pop up is still present"""


# template_management_page.turn_on_wifi()
# data_sources_page.searchMyDesigns("")
# common_method.wait_for_element_appearance_namematches("Showing", 10)
# final_count = int(template_management_page.get_showing_n_designs_number())


def test_Template_Management_TestcaseID_48266():
    pass


# start_app("com.android.chrome")
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://zsbportal.zebra.com/")
# sleep(2)
# data_sources_page.clickEnter()
# data_sources_page.lock_phone()
# wake()
# # data_sources_page.signInWithGoogle("zsbswdvt@gmail.com", "zsbswdvt@1234")
# # data_sources_page.lock_phone()
# # wake()
# data_sources_page.clickGotItWeb()
# registration_page.wait_for_element_appearance_text("Home", 10)
# data_sources_page.click_Menu_HamburgerICNWeb()
# template_management_page.clickCommonDesigns()
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.lock_phone()
# wake()
# template_management_page.search_design_common_designs("Round")
# keyevent("Enter")
# keyevent("back")
# poco.scroll()
# template_management_page.select_design_common_designs_Web()
# while poco("android.widget.EditText").exists():
#     poco.scroll()
# template_management_page.select_label_common_designs_Web()
# selected_design_name = template_management_page.get_name_of_selected_design()
# template_management_page.click_copy_to_My_Designs()
# copied_design_name = selected_design_name + " copy"
# template_management_page.select_label_common_designs_Web()
# data_sources_page.clickPrint()
# data_sources_page.clickPrint()
# common_method.Start_The_App()
# registration_page.wait_for_element_appearance("Open navigation menu", 10)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns(copied_design_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# if copied_design_name in design_list:
#     pass
# else:
#     raise Exception("Copied design from web not present in app.")
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page.search_design_common_designs("Round")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Categories")
# template_management_page.select_design_common_designs()
# if template_management_page.verifyLabelsShown():
#     pass
# else:
#     raise Exception("Error in displaying round labels.")


def test_Template_Management_TestcaseID_48548():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# design_created = "Round"
# data_sources_page.searchMyDesigns(design_created)
# data_sources_page.selectDesignCreatedAtSetUp()
# """Rename pending"""
# renamed_design = "Round@22"
# sleep(20)
# """"""
# data_sources_page.searchMyDesigns(renamed_design)
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDuplicateDesign()
# data_sources_page.searchMyDesigns(renamed_design + " copy")
# duplicated_design_name = renamed_design + " copy"
"""check all try and except"""
# try:
#     common_method.wait_for_element_appearance_namematches(poco(duplicated_design_name), 20)
# except:
#     raise Exception("Duplicated design not present.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# try:
#     common_method.wait_for_element_appearance_namematches(poco("Address"), 20)
# except:
#     raise Exception("Error displayed in common designs page")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns(renamed_design)
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDeleteDesign()
# template_management_page.clickDeleteDesign()
# try:
#     common_method.wait_for_element_appearance_namematches(poco("has been successfully removed"), 20)
# except:
#     raise Exception("Design not deleted.")
# data_sources_page.searchMyDesigns(renamed_design + " copy")
"""Check this"""
# try:
#     common_method.wait_for_element_appearance_namematches(poco(duplicated_design_name), 20)
# except:
#     raise Exception("Duplicated design not present after deleting original design.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# try:
#     common_method.wait_for_element_appearance_namematches(poco("Address"), 20)
# except:
#     raise Exception("Error displayed in common designs page")


def test_Template_Management_TestcaseID_45979():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# template_management_page.verify_search_placeholder()
# template_management_page.verifySearchIcon()
# initial_design_list = template_management_page.get_all_designs_in_my_designs(True)
# initial_count = template_management_page.get_showing_n_designs_number()
# search_keyword = "LDA"
# data_sources_page.searchMyDesigns(search_keyword, False)
# sleep(5)
# if template_management_page.check_suggestion_window_in_common_design():
#     pass
# else:
#     raise Exception("Drop down list did not appear.")
# drop_down_list = template_management_page.get_all_search_results_in_search_designs()
# for i in drop_down_list:
#     if search_keyword in i:
#         pass
#     else:
#         raise Exception("Drop down list contains results that do not contain the search keyword")
# template_management_page.check_dropdown_options_Are_clickable()
# selected_design = template_management_page.click_drop_down_result_1(True)
# if template_management_page.check_suggestion_window_in_common_design():
#     raise Exception("Drop down list did not appear.")
# else:
#     pass
# common_method.wait_for_element_appearance_namematches("Showing")
# displayed_list = template_management_page.get_all_designs_in_my_designs()
# if len(displayed_list) == 1:
#     if displayed_list[0] == selected_design:
#         pass
#     else:
#         "Selected result not present."
# else:
#     raise Exception("Showing more than one design.")
# if int(template_management_page.get_showing_n_designs_number()) == 1:
#     pass
# else:
#     raise Exception("Showing 1 Design not present.")
# data_sources_page.searchMyDesigns("")
# common_method.wait_for_element_appearance_namematches("Showing")
# new_file_list = template_management_page.get_all_designs_in_my_designs(True)
# if initial_design_list == new_file_list:
#     pass
# else:
#     raise Exception("All designs not present after clearing keywords.")
# new_count = template_management_page.get_showing_n_designs_number()
# if initial_count == new_count:
#     pass
# else:
#     raise Exception("initial count not matching after clearing count.")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45922():
    pass


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# search_label_name = "11Elements"
# data_sources_page.searchMyDesigns(search_label_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.verify_print_preview("11Elements")
# field_count = len(template_management_page.get_all_fields_print_page())
# if field_count == 11:
#     pass
# else:
#     raise Exception("The number of fields are not 11.")
# while not poco(nameMatches=".*Label.*").exists():
#     scroll_view = poco("android.widget.ScrollView")
#     scroll_view.swipe("down")
"""ask supported special characters."""
# template_management_page.fill_all_print_fields()
# initial_label_count = template_management_page.get_remaining_label_count()
# data_sources_page.clickPrint()
# template_management_page.wait_for_appearance_disabled("Print")
# template_management_page.wait_for_appearance_enabled("Print")
# new_label_count = template_management_page.get_remaining_label_count()
# if new_label_count == initial_label_count - 1:
#     pass
# else:
#     raise Exception("Label count not updated i.e., not decremented by 1.")
# data_sources_page.clickBackArrow()
# design = template_management_page.get_all_designs_in_my_designs()
# design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
# if design_last_print_date == data_sources_page.get_current_date():
#     pass
# else:
#     raise Exception("Last printed date is not up to date.")
"""step 7a,8 yet to do"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()


def test_Template_Management_TestcaseID_45965():
    pass


# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# while not poco("Log Out").exists():
#     poco.scroll()
# registration_page.click_log_out_button()
"""Login pending"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if poco(nameMatches="Showing.*Designs").exists():
#     pass
# else:
#     raise Exception("\"Showing x designs\" text is not displayed.")
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# """Step 5,6 and 7 should be verified manually cannot be automated."""
# """Step 8, 9 yet to do"""
# template_management_page.verify_design_manipulation_for_all_designs()
# data_sources_page.selectDesignCreatedAtSetUp()
# try:
#     template_management_page.verify_design_manipulation_options()
# except:
#     raise Exception("Design manipulation options \"Print, Rename, Duplicate, Delete\" not present.")
# template_management_page.click_scrim()
# try:
#     template_management_page.verify_design_manipulation_options()
#     raise Exception("Design manipulation options \"Print, Rename, Duplicate, Delete\" not present.")
# except:
#     pass
# """Step 12 pending"""


def test_Template_Management_TestcaseID_45966():
    pass


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if poco(nameMatches="Showing 100 Designs").exists():
#     pass
# else:
#     raise Exception("\"Showing 100 designs\" text is not displayed.")
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# if len(design_list)<=100:
#     pass
# else:
#     raise Exception("There are more than 100 designs.")
# template_management_page.scroll_my_designs("down")
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# """Step 5, 6 yet to do"""
# template_management_page.scroll_my_designs()
# template_management_page.scroll_my_designs("down")
"Delete design"
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDeleteDesign()
# template_management_page.clickDeleteDesign()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# if len(design_list)<=100:
#     pass
# else:
#     raise Exception("There are more than 100 designs.")
# template_management_page.scroll_my_designs("down")
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# """Step 5, 6 yet to do"""
# template_management_page.scroll_my_designs()
# template_management_page.scroll_my_designs("down")
"""Duplicate design"""
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDuplicateDesign()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# if len(design_list)<=100:
#     pass
# else:
#     raise Exception("There are more than 100 designs.")
# template_management_page.scroll_my_designs("down")
# template_management_page.verify_designs_are_according_to_sort_order(design_list)
# """Step 5, 6 yet to do"""
# template_management_page.scroll_my_designs()
# template_management_page.scroll_my_designs("down")


def test_Template_Management_TestcaseID_45925():
    pass


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(5)
# try:
#     common_method.wait_for_element_appearance_namematches("Label")
# except:
#     raise Exception("Print page did not pop up.")
# while not poco("Print").exists():
#     poco.scroll()
# remaining_label_count = template_management_page.get_remaining_label_count()
# template_management_page.changeCopiesCount(remaining_label_count+1)
# keyevent("Enter")
# data_sources_page.clickPrint()


def test_Template_Management_TestcaseID_45921():
    pass


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



