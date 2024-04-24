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


def test_Template_Management_TestcaseID_45981():
    pass


# common_method.Start_The_App()
# registration_page.clickSignIn()
# login_page.click_loginBtn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@gmail.com", "zebraidctest@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45982():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# if template_management_page.verify_default_sort_my_designs():
#     pass
# else:
#     raise Exception("Default sort is not \"Name (A to Z)\" in my designs.")
# template_management_page.click_sort_my_designs()
# template_management_page.verify_sort_options_my_designs()
# template_management_page.select_sort_order("Z-A")
# template_management_page.click_sort_my_designs()
# template_management_page.select_sort_order("A-Z")
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
# template_management_page.select_sort_order("Z-A")
# template_management_page.click_sort_my_designs()
# template_management_page.select_sort_order("A-Z")
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45983():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# template_management_page.click_sort_my_designs()
# template_management_page.select_sort_order("Z-A")
# design_names = template_management_page.get_all_designs_in_my_designs(True)
# template_management_page.verify_design_names_follow_order(design_names, "Z-A")
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
#     raise Exception("Sorting order is not back to default sort order - \"Name (A to Z)\" in my designs.")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45984():
    pass


# common_method.Start_The_App()
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45985():
    pass


"""look here"""


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# template_management_page.click_filter_my_designs("All sizes")
# number_of_filter_options = template_management_page.filter_options(True)
# if number_of_filter_options > 1:
#     pass
# else:
#     raise Exception("No other filter option present other than All sizes.")
# for i in range(1, number_of_filter_options):
#     selectedFilterSize = template_management_page.selectFilter(i)
#     common_method.wait_for_element_appearance_namematches("Showing")
#     label_size_present = template_management_page.get_all_designs_size_in_my_designs()
#     labels = template_management_page.get_all_designs_in_my_designs()
#     if len(label_size_present) == 1:
#         design_size = label_size_present.pop()
#         if design_size == selectedFilterSize:
#             pass
#         else:
#             error_message = f"Designs with size - {label_size_present} displayed when {selectedFilterSize} is selected in filter."
#             raise Exception(error_message)
#     if len(labels) == int(template_management_page.get_showing_n_designs_number()):
#         pass
#     else:
#         print(labels)
#         raise Exception("NUmber of labels displayed not matching the number shown in title.")
#     template_management_page.verify_designs_are_according_to_sort_order(labels)
#     login_page.click_Menu_HamburgerICN()
#     template_management_page.clickCommonDesigns()
#     login_page.click_Menu_HamburgerICN()
#     data_sources_page.clickMyDesigns()
#     common_method.wait_for_element_appearance_namematches("Showing")
#     if template_management_page.verify_default_filter_my_designs():
#         pass
#     else:
#         raise Exception("Sorting order is not back to default sort order - \"Name (A to Z)\" in my designs.")
#     template_management_page.click_filter_my_designs("All sizes")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45987():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
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
# """Step 8 pending"""
# """Cannot verify filter due to bug SMBM-1749"""
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45988():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("Barcodes")
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
# """Step 8 pending"""
# """Cannot verify filter due to bug SMBM-1749"""
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
# common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_45988():
#     pass
#
#
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("Barcodes")
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
# """Step 8 pending"""
# """Cannot verify filter due to bug SMBM-1749"""
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45989():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("File Folder")
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
# """Step 8 pending"""
# """Cannot verify filter due to bug SMBM-1749"""
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45990():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("Jewelry")
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
# displayed_filter_options = template_management_page.filter_options()
# if len(displayed_filter_options) == 1:
#     if displayed_filter_options[0] == "2.25\" x 0.5\"":
#         pass
#     else:
#         raise Exception(f"Filter option {displayed_filter_options[1]} displayed instead of 2.25\" x 0.5\"")
# else:
#     raise Exception(f"Has {len(displayed_filter_options)} instead of just 1 i.e., \"2.25\" x 0.5\"\" ")
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
#         if design_size.pop() == label_size:
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45992():
    pass


"Now here"


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
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
# number_of_filter_options = template_management_page.filter_options(True)
# if number_of_filter_options >= 1:
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
# for i in range(1, number_of_filter_options):
#     selectedFilterSize = template_management_page.selectFilter(i)
#     common_method.wait_for_element_appearance_namematches("Showing")
#     label_size_present = template_management_page.get_all_designs_size_in_my_designs()
#     labels = template_management_page.get_all_designs_in_my_designs()
#     if len(label_size_present) == 1:
#         design_size = label_size_present.pop()
#         if design_size == selectedFilterSize:
#             pass
#         else:
#             error_message = f"Designs with size - {label_size_present} displayed when {selectedFilterSize} is selected in filter."
#             raise Exception(error_message)
#     if len(labels) == int(template_management_page.get_showing_n_designs_number()):
#         pass
#     else:
#         print(labels)
#         raise Exception("Number of labels displayed not matching the number shown in title.")
#     template_management_page.click_sort_common_designs()
#     template_management_page.select_sort_order("A-Z")
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     template_management_page.verify_designs_are_according_to_sort_order(design_list)
#     template_management_page.click_sort_common_designs()
#     template_management_page.select_sort_order("Z-A")
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     template_management_page.verify_designs_are_according_to_sort_order(design_list)
# common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_45994():
#     pass
#
#
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# template_management_page.turn_off_wifi()
# template_management_page.click_filter_my_designs()
# label_size = template_management_page.select_label_size()
# sleep(3)
# if template_management_page.verify_connection_error_app():
#     pass
# else:
#     raise Exception("Connection lost error not displayed.")
# template_management_page.turn_on_wifi()
# sleep(5)
# template_management_page.click_filter_my_designs()
# label_size = template_management_page.select_label_size()
# template_management_page.wait_for_appearance_designs_in_a_particular_category()
# design_name = template_management_page.get_first_design_name_my_designs()
# design_list = template_management_page.get_all_designs_in_my_designs(True)
# title_count = template_management_page.get_showing_n_designs_number()
# if len(design_list) == int(title_count):
#     pass
# else:
#     raise Exception("Count in title doesn't match the number of designs.")
# template_management_page.turn_off_wifi()
# template_management_page.search_design_common_designs(design_name)
# """Step 8-10 pending due to bug SMBM-1774"""
# sleep(3)
# if template_management_page.verify_connection_error_app():
#     pass
# else:
#     raise Exception("Connection lost error not displayed.")
# template_management_page.turn_on_wifi()
# sleep(5)
# template_management_page.search_design_common_designs(design_name)
# try:
#     template_management_page.wait_for_suggestions_to_appear()
# except:
#     raise Exception("dropdown did not appear.")
# template_management_page.check_dropdown_options_Are_clickable()
# template_management_page.click_drop_down_result_1()
# try:
#     template_management_page.wait_for_suggestions_to_appear()
#     x=1/0
# except ZeroDivisionError:
#     raise Exception("dropdown is present.")
# except Exception as e:
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46010():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# initial_categories_list = template_management_page.get_all_categories_in_common_designs()
# if template_management_page.verify_search_placeholder():
#     pass
# else:
#     raise Exception("Search design placeholder not present.")
# if template_management_page.verifySearchIcon():
#     pass
# else:
#     raise Exception("Search icon not present")
# search_text = "/"
# template_management_page.search_design_common_designs(search_text)
# template_management_page_1.wait_for_element_appearance_name_matches_all("CATEGORIES", 20)
# sleep(3)
# category_list_drop_down = template_management_page.get_drop_down_list_common_designs(True)
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Categories")
# category_list = template_management_page.get_all_categories_in_common_designs(True)
# if category_list == category_list_drop_down:
#     pass
# else:
#     raise Exception("All Categories not displayed in drop down.")
# template_management_page.clickCancelSearch()
# search_text = "-"
# template_management_page.search_design_common_designs(search_text)
# template_management_page_1.wait_for_element_appearance_name_matches_all("DESIGNS", 20)
# sleep(3)
# design_list_drop_down = template_management_page.get_drop_down_list_common_designs()
# keyevent("Enter")
# search_text = "-"
# template_management_page.search_design_common_designs(search_text)
# template_management_page_1.wait_for_element_appearance_name_matches_all("DESIGNS", 20)
# sleep(3)
# name_dropdown = template_management_page.click_drop_down_result_1(True)
# print(name_dropdown)
# sleep(3)
# try:
#     common_method.wait_for_element_appearance_namematches("Search results")
# except:
#     raise Exception("dropdown did not close.")
# if template_management_page.verifySearchResults_n(1):
#     pass
# else:
#     raise Exception("Search results(1) not present.")
# names_result = template_management_page.get_all_designs_in_search_designs(True)
# print(names_result)
# if name_dropdown == names_result[0]:
#     pass
# else:
#     raise Exception("Selected design not displayed.")
# template_management_page.search_design_common_designs("")
# keyevent("Enter")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# new_categories_list = template_management_page.get_all_categories_in_common_designs()
# if initial_categories_list == new_categories_list:
#     pass
# template_management_page.search_design_common_designs("~`!@#$%^&*()_-+={}[]|/\:;"'<>,.?'"")
# try:
#     common_method.wait_for_element_appearance_namematches("No results found.\nSearch tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then.")
# except:
#     raise Exception("No results for \"searched text\" text not displayed.")
# template_management_page.search_design_common_designs("")
# keyevent("Enter")
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# new_categories_list = template_management_page.get_all_categories_in_common_designs()
# if initial_categories_list == new_categories_list:
#     pass


def test_Template_Management_TestcaseID_46014():
    pass


"""Login"""


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# """"""
# categories = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping", "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose", "XL Shipping"]
# search_text = ["Address", "Dishes", "Price", "Badge", "Harmful", "TwoLine", "Fragile", "Caution", "Asset", "Checklist"]
# for i in range(len(categories)):
#     template_management_page.search_design_common_designs(categories[i])
#     keyevent("Enter")
#     common_method.wait_for_element_appearance_namematches("Categories")
#     template_management_page.select_design_common_designs()
#     if template_management_page.verify_search_placeholder():
#         pass
#     else:
#         raise Exception("Search design place holder doesnt have 'Search designs'.")
#     template_management_page.search_design_common_designs(search_text[i])
#     try:
#         poco(nameMatches="(?s).*result").wait_for_appearance(timeout=20)
#     except:
#         raise Exception("Drop down not present.")
#     """Step -5b pending yet to do"""
#     drop_down_list = template_management_page.get_all_search_results_in_search_designs()
#     for result in drop_down_list:
#         if search_text[i] in result:
#             pass
#         else:
#             raise Exception("Drop down list contains results that do not contain the search keyword")
#     template_management_page.check_dropdown_options_Are_clickable()
#     template_management_page.checkNumberOfDesignsMatchingDropDown()
#     keyevent("Enter")
#     if poco(nameMatches="(?s).*result").exists():
#         raise Exception("Drop down present even after clicking search on keyboard.")
#     else:
#         pass
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     for result in design_list:
#         if search_text[i].lower() in result.lower():
#             pass
#         else:
#             raise Exception("search text not present in one of the results.")
#     template_management_page.click_filter_common_designs()
#     label_size = template_management_page.select_label_size()
#     print(label_size)
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_size = template_management_page.get_all_designs_size_in_my_designs()
#     try:
#         if len(design_size) == 1:
#             if design_size.pop() == label_size:
#                 pass
#     except:
#         raise Exception("Label size chosen in filter doesnt match the filtered result label size")
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     init_no_of_designs = len(design_list)
#     template_management_page.verify_designs_are_according_to_sort_order(design_list)
#     template_management_page.click_sort_common_designs()
#     template_management_page.select_sort_order("Z-A")
#     sleep(3)
#     if template_management_page.get_filter_value() == label_size:
#         pass
#     else:
#         raise Exception("Filtering selection changed after changing sort order.")
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     template_management_page.verify_designs_are_according_to_sort_order(design_list)
#     no_of_designs = len(design_list)
#     if no_of_designs == init_no_of_designs:
#         pass
#     else:
#         raise Exception("The number of designs are not same before and after sorting.")
#     template_management_page.click_sort_common_designs()
#     sleep(3)
#     template_management_page.select_sort_order("A-Z")
#     sleep(3)
#     if template_management_page.get_filter_value() == label_size:
#         pass
#     else:
#         raise Exception("Filtering selection changed after changing sort order.")
#     template_management_page.wait_for_appearance_designs_in_a_particular_category()
#     design_list = template_management_page.get_all_designs_in_my_designs(True)
#     template_management_page.verify_designs_are_according_to_sort_order(design_list)
#     no_of_designs = len(design_list)
#     if no_of_designs == init_no_of_designs:
#         pass
#     else:
#         raise Exception("The number of designs are not same before and after sorting.")
#     help_page.clickBackArrow()
#     template_management_page.select_design_common_designs()
#     if template_management_page.verify_search_placeholder():
#         pass
#     else:
#         raise Exception("Search box not cleared.")
#     help_page.clickBackArrow()
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46015():
    pass


# """Step 1-4 web portal - pending due to web in consistency"""
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# sleep(3)
# data_sources_page.searchName("Country_capital.xlsx")
# sleep(2)
# data_sources_page.remove_File()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# design_name = "46015"
# "here"
# data_sources_page.searchMyDesigns(design_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("could not be read")
# template_management_page.selectChooseAnOption(1, None, False)
# poco.scroll()
# """Issue in step 7 due to bug SMBM-2202"""
# template_management_page.select_file_update_data_connections("Local File")
# template_management_page.wait_for_appearance_enabled("Continue")
# data_sources_page.clickContinue()
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# try:
#     registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
# except:
#     raise Exception("Print preview not present.")
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# """Reopen print preview"""
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("could not be read")
# template_management_page.selectChooseAnOption(1, None, False)
# poco.scroll()
# """Issue in step 7 due to bug SMBM-2202"""
# selected_file_name = template_management_page.select_file_update_data_connections("Drive")
# template_management_page.wait_for_appearance_enabled("Continue")
# data_sources_page.clickContinue()
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# try:
#     registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
# except:
#     raise Exception("Print preview not present.")
# """Remove the file from web"""
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
# data_sources_page.lock_phone()
# wake()
# registration_page.wait_for_element_appearance_text("Home", 10)
# sleep(3)
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.click_My_Data()
# data_sources_page.click_Menu_HamburgerICNWeb()
# data_sources_page.searchName("Korea.xlsx")
# keyevent("back")
# sleep(3)
# poco.scroll()
# sleep(2)
# data_sources_page.remove_File_Web()
# stop_app("com.android.chrome")
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46016():
    pass


"""Step 1-4 pending due to web inconsistency execute manually"""


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
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Home", 10)
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.clickMyDesigns()
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.lock_phone()
# # wake()
# # data_sources_page.clickCreateDesignBtn()
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Select a label size", 10)
# # data_sources_page.selectLabelSize()
# # data_sources_page.clickContinueWeb()
# # data_sources_page.lock_phone()
# # wake()
# # poco(text="Exit Designer").wait_for_appearance(timeout=10)
# # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
# # sleep(3)
# # template_management_page.click_Connect_Data_File()
# # data_sources_page.lock_phone()
# # wake()
# # file_name = template_management_page.select_file_from_Connect_Data_File()
# # template_management_page.clickAddText()
# # template_management_page.placeText()
# # sleep(3)
# # keyevent("Back")
# """Step -3"""
# # template_management_page.click_from_data_file()
# # data_sources_page.clickAddBarcode()
# # data_sources_page.placeBarcode()
# # keyevent("Back")
# """"""

# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# data_sources_page.searchName("csv_file.csv")
# sleep(2)
# data_sources_page.remove_File()
# sleep(3)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns("46016")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.checkManualInput_checkbox()
# data_sources_page.clickContinue()
# sleep(3)
# data_sources_page.verifyIfPreviewIsPresent()
# """cannot verify this part of step 6"""
# """check that no value shown in the variables in the preview dialog"""
# if template_management_page.verify_label_range_navigation_unavailable():
#     pass
# else:
#     raise Exception("Label range navigation is present.")
# """Step 7 pending"""
# template_management_page.fillOrganizationId("abcd")
# keyevent("back")
# template_management_page.fillIndex("xyz")
# keyevent("back")
# scroll_view = poco("android.view.View")
# scroll_view.swipe("down")
# """cannot verify this part of step 8"""
# """check that preview is shown correctly"""
# scroll_view.swipe("up")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_46019():
#     pass
#
#
# common_method.Start_The_App()
# """Step 1-4 pending due to web inconsistency"""
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("46019")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# data_sources_page.clickPrint()
# """Select column"""
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header(False)
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# """check that only the selected column values shown in the table - pending"""
# """Check and uncheck select all"""
# scroll_view = poco("android.widget.ScrollView")
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# data_sources_page.select_All()
# data_sources_page.select_All(False)
# """check select all"""
# data_sources_page.select_All()
# """Step 10 -15 blocked due to BUG ID - SMBM-1134"""
# data_sources_page.clickConfirm()
# """Check"""
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
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
# if poco(text="Choose an account").exists():
#     help_page.chooseAcc("zsbswdvt@gmail.com")
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header(True)
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# """check the label amount is correct, same as the selected column row number - cannot be automated"""
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
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46022():
    pass


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
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Home", 10)
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.clickMyDesigns()
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.lock_phone()
# # wake()
# # data_sources_page.clickCreateDesignBtn()
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Select a label size", 10)
# # data_sources_page.selectLabelSize()
# # data_sources_page.clickContinueWeb()
# # data_sources_page.lock_phone()
# # wake()
# # poco(text="Exit Designer").wait_for_appearance(timeout=10)
# # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
# # sleep(3)
# # data_sources_page.lock_phone()
# # wake()
# # template_management_page.click_Connect_Data_File()
# # data_sources_page.lock_phone()
# # wake()
# # data_file_name = "columnWithUnequalRows.xlsx"
# # template_management_page.select_file_from_Connect_Data_File(data_file_name)
# # data_sources_page.clickAddBarcode()
# # data_sources_page.placeBarcode()
# # sleep(3)
# # keyevent("Back")
# # data_sources_page.lock_phone()
# # wake()
# # common_method.swipe_screen([0.8407407407407408, 0.5260683760683761], [0.5009259259259259, 0.5260683760683761], 1)
# # template_management_page.click_from_data_file()
# # common_method.swipe_screen([0.5009259259259259, 0.5260683760683761], [0.8407407407407408, 0.5260683760683761], 1)
# # common_method.swipe_screen([0.08055555555555556, 0.25427350427350426], [0.9, 0.25427350427350426], 1)
# # common_method.swipe_screen([0.5, 0.254], [0.5, 0.63], 1)
# # data_sources_page.lock_phone()
# # wake()
# # label_name = "46022"
# # data_sources_page.setLabelName(label_name)
# # data_sources_page.exitDesigner()
# common_method.Start_The_App()
# poco("Open navigation menu").wait_for_appearance(timeout=10)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns("46022")
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# data_sources_page.clickBackArrow()
# common_method.wait_for_element_appearance_namematches("Update Data Connections")
# template_management_page.selectChooseAnOption(1, None, False)
# poco.scroll()
# """Issue in step 7 due to bug SMBM-2202"""
# selected_file_name = template_management_page.select_file_update_data_connections("Drive")
# data_sources_page.clickContinue()
# data_sources_page.first_row_header(True)
# template_management_page.selectChooseAnOption(1)
# data_sources_page.clickContinue()
# """check the label amount is correct, same as the selected column row number - cannot be automated"""
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
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47791():
    pass


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
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Home", 10)
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.clickMyDesigns()
# # data_sources_page.click_Menu_HamburgerICNWeb()
# # data_sources_page.lock_phone()
# # wake()
# # data_sources_page.clickCreateDesignBtn()
# # data_sources_page.lock_phone()
# # wake()
# # registration_page.wait_for_element_appearance_text("Select a label size", 10)
# # data_sources_page.selectLabelSize()
# # data_sources_page.clickContinueWeb()
# # poco(text="Exit Designer").wait_for_appearance(timeout=10)
# # common_method.swipe_screen([0.9, 0.25427350427350426], [0.08055555555555556, 0.25427350427350426], 1)
# # data_sources_page.lock_phone()
# # wake()
# """ask Tarun"""
# # template_management_page.click_Connect_Data_File()
# # data_sources_page.lock_phone()
# # wake()
# # file_name = template_management_page.select_file_from_Connect_Data_File()
# # template_management_page.clickAddText()
# # template_management_page.placeText()
# # sleep(3)
# # keyevent("Back")
# """Step -3"""
# # template_management_page.click_from_data_file()
# # data_sources_page.clickAddBarcode()
# # data_sources_page.placeBarcode()
# # keyevent("Back")
# """"""
# common_method.Start_The_App()
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
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47812():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# data_sources_page.searchName("Label", False)
# """Cannot automate - Check the search result title and the result label should not overlap each other - due to bug SMBM-1886"""
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_47824():
    pass


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
# """Design delete pop up is still present"""
# """No prompt as \"Design XX was not deleted"\""""
# """Blocked due to bug id SMBM-1902"""
# template_management_page.turn_on_wifi()
# data_sources_page.searchMyDesigns("")
# common_method.wait_for_element_appearance_namematches("Showing", 10)
# final_count = int(template_management_page.get_showing_n_designs_number())
# if final_count == initial_count - 1:
#     pass
# else:
#     raise Exception("The count did not reduce by 1.")


def test_Template_Management_TestcaseID_48266():
    pass


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
# data_sources_page.lock_phone()
# wake()
# data_sources_page.signInWithGoogle("zsbswdvt@gmail.com", "zsbswdvt@1234")
# data_sources_page.lock_phone()
# wake()
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
# data_sources_page.lock_phone()
# wake()
# template_management_page.select_design_common_designs_Web()
# while poco("android.widget.EditText").exists():
#     poco.scroll()
# template_management_page.select_label_common_designs_Web()
# data_sources_page.lock_phone()
# wake()
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
# template_management_page.verifyLabelsShown()
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# recently_printed_designs = template_management_page_1.get_all_designs_in_recently_printed_labels()
# for i in recently_printed_designs:
#     if "Last print" in i:
#         pass
#     else:
#         raise Exception("Recently printed labels not loaded successfully.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# try:
#     template_management_page.waitForAppearanceTypeName("android.widget.ImageView", "x")
# except:
#     raise Exception("My Designs did not load properly.")


def test_Template_Management_TestcaseID_48547():
    pass


# """Step 1-6 web portal - pending due to web in consistency"""
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
# data_sources_page.lock_phone()
# wake()
# sleep(2)
# try:
#     poco(text="Sign In With").wait_for_appearance(timeout=15)
#     account = "zebraidctest@gmail.com"
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
#         registration_page.sign_In_With_Google("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
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
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# design_created = "48547"
# data_sources_page.searchMyDesigns(design_created)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print not successful.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print not successful.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# try:
#     common_method.wait_for_element_appearance_namematches("Showing")
# except:
#     raise Exception("My designs did not load load properly")

"""Web objects update pending due to web inconsistency."""


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# design_created = "48547"
# data_sources_page.searchMyDesigns(design_created)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# # data_sources_page.clickPrint()
# # try:
# #     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# # except:
# #     raise Exception("Print not successful.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# # data_sources_page.clickPrint()
# # try:
# #     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# # except:
# #     raise Exception("Print not successful.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# try:
#     common_method.wait_for_element_appearance_namematches("Showing")
# except:
#     raise Exception("My designs did not load load properly")


def test_Template_Management_TestcaseID_48548():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# design_created = "48548"
# data_sources_page.searchMyDesigns(design_created)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Rename pending"""
# renamed_design = "Round@22"
# template_management_page.rename_Design()
# template_management_page.new_design_name(renamed_design)
# template_management_page.clickSave()
# common_method.wait_for_element_appearance_namematches("Design has been successfully renamed")
# data_sources_page.searchMyDesigns(renamed_design)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDuplicateDesign()
# template_management_page.clickSave()
# common_method.wait_for_element_appearance_namematches("Design has been successfully duplicated")
# data_sources_page.searchMyDesigns(renamed_design + " copy")
# common_method.wait_for_element_appearance_namematches("Showing")
# duplicated_design_name = renamed_design + " copy"
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all(duplicated_design_name, 20)
# except:
#     raise Exception("Duplicated design not present.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Address", 20)
# except:
#     raise Exception("Error displayed in common designs page")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns(renamed_design)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectSecondDesign()
# template_management_page.clickDeleteDesign()
# template_management_page.clickDeleteDesign()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("has been successfully removed", 20)
# except:
#     raise Exception("Design not deleted.")
# data_sources_page.searchMyDesigns(duplicated_design_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all(duplicated_design_name, 20)
# except:
#     raise Exception("Duplicated design not present after deleting original design.")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Address", 20)
# except:
#     raise Exception("Error displayed in common designs page")
# """Change back the design name and bring back to default"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns(duplicated_design_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.rename_Design()
# template_management_page.new_design_name(design_created)
# template_management_page.clickSave()
# common_method.Stop_The_App()


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


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# search_label_name = "11Elements"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# """cannot verify - 3a. Verify the design's elements are displayed in the print preview.
# This has to be done manually"""
# common_method.wait_for_element_appearance_textmatches("Text")
# sleep(4)
# field_count = len(template_management_page.get_all_fields_print_page())
# if field_count == 11:
#     pass
# else:
#     raise Exception("The number of fields are not 11.")
# while not poco(nameMatches=".*Label.*").exists():
#     scroll_view = poco("android.widget.ScrollView")
#     scroll_view.swipe("down")
# """ask supported special characters."""
# template_management_page.fill_all_print_fields()
# initial_label_count = template_management_page.get_remaining_label_count()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# new_label_count = template_management_page.get_remaining_label_count()
# if new_label_count == initial_label_count - 1:
#     pass
# else:
#     raise Exception("Label count not updated i.e., not decremented by 1.")
# data_sources_page.clickBackArrow()
# common_method.wait_for_element_appearance_namematches("My Designs")
# design = template_management_page.get_all_designs_in_my_designs()
# try:
#     design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
#     if design_last_print_date == data_sources_page.get_current_date():
#         pass
#     else:
#         raise Exception("Last printed date is not up to date.")
# except:
#     raise Exception("No last print information under the design in My Designs Page")
# """step 7a,8 yet to do"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# label_left_in_printer_info = template_management_page.get_Labels_left_in_printer_info()
# if str(new_label_count) + " of" in label_left_in_printer_info:
#     pass
# else:
#     raise Exception("Labels left in printer info is not updated.")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45965():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# while not poco("Log Out").exists():
#     poco.scroll()
# registration_page.click_log_out_button()
# """Login pending"""
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zsbswdvt1@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zsbswdvt1@gmail.com", "zsbswdvt1@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
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
# design_precondition1 = ["design1", "design2", "design3", "design4"]
# design_precondition2 = ["unprintedDesign1", "unprintedDesign2"]
# design_precondition3 = ["unprintedDesign1 copy", "unprintedDesign2 copy"]
# for design in design_precondition1:
#     data_sources_page.searchMyDesigns(design)
#     common_method.wait_for_element_appearance_namematches("Showing")
#     design_info = template_management_page.getDesignInfo(design)
#     if "Last print" in design_info:
#         pass
#     else:
#         raise Exception("No Last print date in designs from precondition 1.")
# for design in design_precondition2:
#     data_sources_page.searchMyDesigns(design)
#     common_method.wait_for_element_appearance_namematches("Showing")
#     design_info = template_management_page.getDesignInfo(design)
#     if "Last print" in design_info:
#         raise Exception("No Last print date in designs from precondition 1.")
# for design in design_precondition3:
#     data_sources_page.searchMyDesigns(design)
#     common_method.wait_for_element_appearance_namematches("Showing")
#     design_info = template_management_page.getDesignInfo(design)
#     if "Last print" in design_info:
#         raise Exception("No Last print date in designs from precondition 1.")
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


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# while not poco("Log Out").exists():
#     poco.scroll()
# registration_page.click_log_out_button()
# """Login pending"""
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "sohozsb@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("sohozsb@gmail.com", "sohozsb@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
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
# "Delete design"
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDeleteDesign()
# template_management_page.clickDeleteDesign()
# common_method.wait_for_element_appearance_namematches("Showing")
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
# """Duplicate design"""
#
#
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDuplicateDesign()
# template_management_page.clickSave()
# common_method.wait_for_element_appearance_namematches("Showing")
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
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45924():
    pass


# common_method.Start_The_App()
# lastPrintInitial = template_management_page.getLastPrintFromFirstDesignInRecentlyPrintedDesigns()
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# template_management_page.wait_for_appearance_enabled("Print")
# initial_label_count = template_management_page.get_remaining_label_count()
# data_sources_page.clickBackArrow()
# try:
#     common_method.wait_for_element_appearance("Recently Printed Labels")
#     template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
# except:
#     raise Exception("Recently printed label view not present.")
# lastPrintNew = template_management_page.getLastPrintFromFirstDesignInRecentlyPrintedDesigns()
# if lastPrintInitial == lastPrintNew:
#     pass
# else:
#     raise Exception("Last print info updated without printing.")
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# template_management_page.wait_for_appearance_enabled("Print")
# new_label_count = template_management_page.get_remaining_label_count()
# if initial_label_count == new_label_count:
#     pass
# else:
#     raise Exception("Label count updated without printing.")
# data_sources_page.clickPrint()
# data_sources_page.clickBackArrow()
# label_left = template_management_page.get_Labels_left_in_printer_info()
# if str(new_label_count) in label_left:
#     pass
# else:
#     raise Exception("Label count not updated in printer info after printing.")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45925():
    pass


# common_method.Start_The_App()
# initail_prints_left = template_management_page.get_Labels_left_in_printer_info().split(" ")[0]
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
# sleep(5)
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Printer cover closed")
# sleep(20)
# """Load another cartridge in the printer. Resume printing.-has to be done manually"""
# remainingLabels = template_management_page.get_remaining_label_count()
# if remainingLabels > 0:
#     pass
# else:
#     raise Exception("Labels left not updated after changing empty cartridge.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# new_prints_left = template_management_page.get_Labels_left_in_printer_info().split(" ")[0]
# if new_prints_left > initail_prints_left:
#     pass
# else:
#     raise Exception("total number of labels left (x of x prints left) is not updated in the Printer information")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_45921():
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
# data_sources_page.clickPrint()
# new_label_count = template_management_page.get_remaining_label_count()
# if remaining_label_count == new_label_count:
#     pass
# else:
#     raise Exception("Label count changed even when printer is offline.")
# data_sources_page.clickBackArrow()
# try:
#     registration_page.wait_for_element_appearance("My Designs")
# except:
#     raise Exception("Did not return to \"My Designs\" page")


def test_Template_Management_TestcaseID_46005():
    pass


# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46005"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# name, size, lastPrint = template_management_page.get_the_name_size_and_lastprint_of_design(poco(nameMatches=f"(?s).*{search_label_name}.*").get_name())
# "unable to Verify design's information (Name, Size, Last Print) are NOT updated."
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.fill_all_print_fields("0")
# print(1/0)
# """Clear the input box for print preview-unable to set value to blank"""
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# "Verify updated elements are visible in print preview-cannot automate"
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")


def test_Template_Management_TestcaseID_46023():
    pass


# "Step 1- 4 pending due to web inconsistency"
# common_method.Start_The_App()
# """Click hamburger menu"""
# login_page.click_Menu_HamburgerICN()
# """clickMy designs"""
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# "Search label created in web"
# search_label_name = "46023"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# "Select the label"
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# template_management_page_1.check_element_exists_enabled("Print")
# data_sources_page.clickPrint()
# """select column with all alphabets"""
# template_management_page.selectChooseAnOption(1, "Alphabet")
# "click on continue"
# data_sources_page.clickContinue()
# "check if error pops up"
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
# except:
#     raise Exception("No error displayed")
# data_sources_page.clickCancel()
# while not poco("Print").exists():
#     poco.scroll()
# "navigate labels and check for error"
# data_sources_page.clickNext()
# "check if error pops up"
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
# except:
#     raise Exception("No error displayed")
# data_sources_page.clickCancel()
# try:
#     template_management_page.wait_for_appearance_disabled("Print", 5)
# except:
#     raise Exception("Print option is not greyed out")
# data_sources_page.clickPrevious()
# "check if error pops up"
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
# except:
#     raise Exception("No error displayed")
# data_sources_page.clickCancel()
# try:
#     template_management_page.wait_for_appearance_disabled("Print", 5)
# except:
#     raise Exception("Print option is not greyed out")
# "click back arrow"
# data_sources_page.clickBackArrow()
# common_method.wait_for_element_appearance_namematches("Showing")
# "select the design created and click print"
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# "choose column with both numbers and alphabets"
# template_management_page.selectChooseAnOption(1, "Alphabet and Number")
# "click continue"
# data_sources_page.clickContinue()
# "check if error pops up for numeric values"
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
#     x = 1/0
# except ZeroDivisionError:
#     raise Exception("Error message shown for column with numeric values.")
# except Exception as e:
#     pass
# while not poco("Print").exists():
#     poco.scroll()
# "check print option is disabled"
# try:
#     template_management_page.wait_for_appearance_disabled("Print", 5)
# except:
#     raise Exception("Print option is not greyed out")
# "navigate labels and check if error pos up for numeric values"
# data_sources_page.clickNext()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
#     x = 1/0
# except ZeroDivisionError:
#     raise Exception("Error message shown for column with numeric values.")
# except Exception as e:
#     pass
# "check print option is disabled"
# try:
#     template_management_page.wait_for_appearance_disabled("Print", 5)
# except:
#     raise Exception("Print option is not greyed out")
# data_sources_page.clickNext()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
# except:
#     raise Exception("No error displayed")
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Could not fetch the Print Preview")
# except:
#     raise Exception("\"Could not fetch the Print Preview\" not present in popup")
# """uncheck the alphabet rows"""
# data_sources_page.clickCancel()
# "check print option is disabled"
# try:
#     template_management_page.wait_for_appearance_disabled("Print", 5)
# except:
#     raise Exception("Print option is not greyed out")
# data_sources_page.clickLabelRange()
# data_sources_page.clickCheckBox(0)
# data_sources_page.clickCheckBox(3)
# data_sources_page.clickCheckBox(4)
# data_sources_page.clickCheckBox(7)
# data_sources_page.clickConfirm()
# """check that correct label amount shown"""
# if template_management_page.check_total_label_for_print_count(3):
#     pass
# else:
#     raise Exception("Label amount shown is incorrect.")
# sleep(2)
# """check that correct row index shown in label range field"""
# label_range_index = data_sources_page.getRowIndex()
# if label_range_index == "1-2,5":
#     pass
# else:
#     raise Exception("Row index shown in label range field is incorrect.")
# "cannot automate - check that the labels are shown correctly has to be done manually"
# while template_management_page_1.check_element_exists_enabled("Next"):
#     data_sources_page.clickNext()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Error")
#     x = 1/0
# except ZeroDivisionError:
#     raise Exception("Error message shown for column with numeric values.")
# except Exception as e:
#     pass
# if template_management_page_1.check_element_exists_enabled("Print"):
#     pass
# else:
#     raise Exception("Print option is disabled.")
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print complete notification did not appear.")
# common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_46024():
#     pass
#
#
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "Linked_CSV"
# data_sources_page.searchMyDesigns(search_label_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page_1.check_element_exists_enabled("Print")
# data_sources_page.clickPrint()
# data_sources_page.clickBackArrow()
# if template_management_page.verify_if_on_update_connections_page():
#     pass
# else:
#     raise Exception("Not on \"Update data connections\" page.")
# sleep(2)
# template_management_page.checkIfDataSourceIsLinked()
# data_sources_page.clickContinue()
# if template_management_page.verify_if_on_relink_data_source_page():
#     pass
# else:
#     raise Exception("Not on \"Relink data source\" page.")
# data_sources_page.first_row_header(True)
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# while not poco("Print").exists():
#     poco.scroll()
# initial_print_label_count = int(template_management_page.get_total_labels_printing())
# copies = 2
# template_management_page.changeCopiesCount(copies)
# keyevent("Enter")
# new_label_print_count = int(template_management_page.get_total_labels_printing())
# if new_label_print_count == initial_print_label_count * copies:
#     pass
# else:
#     raise Exception("Number of labels printing did not update properly.")
# initial_remaining_label = template_management_page.get_remaining_label_count()
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print complete notification did not appear.")
# template_management_page.closeNotification()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
#     x=1/0
# except ZeroDivisionError:
#     raise Exception("Print complete notification did not close.")
# except Exception as e:
#     pass
# common_method.wait_for_element_appearance_namematches("Label")
# new_remaining_label = template_management_page.get_remaining_label_count()
# print(initial_remaining_label)
# print(new_remaining_label)
# if new_remaining_label == initial_remaining_label - new_label_print_count:
#     pass
# else:
#     raise Exception("Remaining label count not matching expected count.\n Expected label count = initial labels left in printer - number of labels printed.")
# data_sources_page.clickBackArrow()
# try:
#     common_method.wait_for_element_appearance_namematches("My Designs")
# except:
#     raise Exception("Did not return to \"My Designs\" page.")
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.searchName("")
# sleep(7)
# data_sources_page.searchName(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# design = template_management_page.get_all_designs_in_my_designs()
# design_last_print_date = design[0].split("\n")[2].split(":")[1].strip()
# if design_last_print_date == data_sources_page.get_current_date():
#     pass
# else:
#     raise Exception("Last printed date is not up to date.")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# data_sources_page.clickBackArrow()
# if template_management_page.verify_if_on_update_connections_page():
#     pass
# else:
#     raise Exception("Not on \"Update data connections\" page.")
# sleep(2)
# template_management_page.checkIfDataSourceIsLinked()
# data_sources_page.clickContinue()
# if template_management_page.verify_if_on_relink_data_source_page():
#     pass
# else:
#     raise Exception("Not on \"Relink data source\" page.")
# data_sources_page.first_row_header(True)
# template_management_page.selectChooseAnOption(1)
# data_sources_page.clickContinue()
# while not poco("Print").exists():
#     poco.scroll()
# new_remaining_label_1 = template_management_page.get_remaining_label_count()
# if new_remaining_label_1 == new_remaining_label:
#     pass
# else:
#     raise Exception("Number of labels left have changed from the previous time without printing.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# prints_left = template_management_page.get_Labels_left_in_printer_info()
# print(prints_left)
# if str(new_remaining_label_1) in prints_left:
#     pass
# else:
#     raise Exception("Number of labels left (x of x prints left) is not updated in the Printer information.")


def test_Template_Management_TestcaseID_46025():
    pass


# common_method.Start_The_App()
# categories = ["Address", "Barcodes", "Jewelry", "Multipurpose/Name Tag", "Postage/Shipping", "Return Address/File Folder", "Round", "Shipping", "Small Multipurpose", "XL Shipping"]
# for i in range(len(categories)):
#     login_page.click_Menu_HamburgerICN()
#     template_management_page.clickCommonDesigns()
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
#     template_management_page.search_design_common_designs(categories[i])
#     keyevent("Enter")
#     common_method.wait_for_element_appearance_namematches("Categories")
#     template_management_page.select_design_common_designs()
#     template_management_page.select_label_common_designs()
#     data_sources_page.clickPrint()
#     while not poco("Print", enabled=True).exists():
#         poco.scroll()
#     poco.scroll()
#     template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# selected_label = template_management_page.select_label_common_designs() + " copy"
# template_management_page.click_copy_to_My_Designs()
# template_management_page_1.wait_for_element_appearance_name_matches_all("has been successfully copied to your workspace")
# sleep(2)
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns(selected_label)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print", enabled=True).exists():
#     poco.scroll()
# poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# first_recently_printed_label = template_management_page_1.get_first_design_in_recently_printed_labels()
# name_first_recently_printed_label = first_recently_printed_label.split("\n")[0]
# date_first_recently_printed_label = first_recently_printed_label.split("\n")[2].split(":")[1].strip()
# current_date = data_sources_page.get_current_date()
# if name_first_recently_printed_label == selected_label:
#     if date_first_recently_printed_label == current_date:
#         pass
#     else:
#         raise Exception("Recently printed date of the top design in recently printed design is not the current date.")
# else:
#     raise Exception("First shown design in \"Recently pPrinted Labels\" is not the recently printed design.")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46026():
    pass


"""Step 1-6 web portal - pending due to web in consistency"""


# selected_file_name = "test_local.xlsx"
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
# data_sources_page.lock_phone()
# wake()
# registration_page.wait_for_element_appearance_text("Home", 10)
# sleep(3)
# data_sources_page.click_Menu_HamburgerICNWeb()
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
# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# design_name = "46026"
# "here"
# data_sources_page.searchMyDesigns(design_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.verify_update_data_connections_dialog()
# common_method.wait_for_element_appearance_namematches("could not be read")
# template_management_page.selectChooseAnOption(1, None, False)
# """Issue in step 8 due to bug SMBM-2202"""
# template_management_page.select_file_update_data_connections("Upload File")
# data_sources_page.searchFileInLocalStorage(".xlsx")
# template_management_page.wait_for_appearance_enabled("Continue")
# data_sources_page.clickContinue()
# template_management_page.selectChooseAnOption(2)
# """Cannot automate \"Check the column name displayed above the column selection box. Currently it displays in the column selection box\" due to bug BUGID SMBM-2175"""
# data_sources_page.clickContinue()
# try:
#     registration_page.wait_for_element_appearance("android.widget.ImageView", 20)
# except:
#     raise Exception("Print preview not present.")
# while not poco("Print").exists():
#     poco.scroll()
# poco.scroll()
# template_management_page.verify_label_range_is_All()
# data_sources_page.clickLabelRange()
# """Cannot verify \"check that all the columns and rows of the new data source file are shown in the table\""""
# data_sources_page.clickBackArrow()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")


def test_Template_Management_TestcaseID_47941():
    pass


# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.click_My_Data()
# try:
#     common_method.wait_for_element_appearance("My Data")
# except:
#     raise Exception("My Data page did not open.")
# try:
#     common_method.wait_for_element_appearance("Connect files so you can leverage them within your designs.")
# except:
#     raise Exception("\"Connect files so you can leverage them within your designs.\" text not present")
#
# if template_management_page.checkIfElementIsPresent("You don’t have any files"):
#     if template_management_page.checkIfElementIsPresent("Get started by adding files to be used within your workspace and your team."):
#         pass
# elif template_management_page.checkIfElementIsPresent("android.widget.EditText"):
#     if template_management_page.verifySearchIcon():
#         pass
#     else:
#         raise Exception("Search Icon not present.")
#     if template_management_page.verifySearchFiles():
#         pass
#     else:
#         raise Exception("Search Files placeholder not present.")
#     if template_management_page.checkIfElementIsPresent("NAME"):
#         pass
#     else:
#         raise Exception("NAME field not present.")
#     """Cannot automate step 3 due to BUG SMBM-938"""
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46030():
    pass


# """Step 1-5 pending due to web automation"""
# """Select google account
# email-zsbswdvt@gmail.com
# password - zsbswdvt@1234 in while creating template in web"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46030"
# data_sources_page.searchMyDesigns(search_label_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# poco("Accept").wait_for_appearance(timeout=10)
# template_management_page.clickAccept()
# """ google contacts """
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
# label_range = 4
# data_sources_page.labelRangeSelection(label_range)
# "Unable to automate step 9"
# for i in range(label_range):
#     data_sources_page.clickNext()
# template_management_page_1.check_element_exists_enabled("Next")
# poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
"""Step 12 pending due to web automation - has to be executed manually"""


def test_Template_Management_TestcaseID_46031():
    pass


"""Step 1-5 pending due to web automation"""


# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46031"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# poco("Accept").wait_for_appearance(timeout=10)
# template_management_page.clickAccept()
# """ google contacts """
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 12:
#     pass
# else:
#     if number_of_labels > 12:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# while not poco("Print").exists():
#     poco.scroll()
# """cannot automate - check all the link column values are correct, the preview image is correct"""
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.labelRangeSelection(4)
# sleep(3)
# template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# start_app("com.android.chrome")
# sleep(2)
# poco("com.android.chrome:id/tab_switcher_button").click()
# sleep(2)
# poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://contacts.google.com/")
# data_sources_page.clickEnter()
# sleep(2)
# data_sources_page.lock_phone()
# wake()
# sleep(2)
# common_method.wait_for_element_appearance_text("Contacts", 20)
# try:
#     common_method.wait_for_element_appearance_text("Use the Contacts app")
#     if poco(text="Stay on web").exists():
#         poco(text="Stay on web").click()
# except:
#     pass
# template_management_page.changeAccInAddContacts(account)
# common_method.wait_for_element_appearance_text("Contacts")
# try:
#     common_method.wait_for_element_appearance_text("Use the Contacts app")
#     if poco(text="Stay on web").exists():
#         poco(text="Stay on web").click()
# except:
#     pass
# template_management_page.delectContactGoogleContacts()
# template_management_page.createContact("z", "1")
# sleep(2)
# template_management_page.createContact("y", "1")
# stop_app("com.android.chrome")
# registration_page.wait_for_element_appearance("Home", 20)
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# """Yet to execute as recently printed labels has bug"""
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 13:
#     pass
# else:
#     if number_of_labels > 13:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate -
# check all the link column values are correct, the preview image is correct
# check the delete contact is not shown
# check the updated value shown in that contact
# check the newly added contacts are shown
# -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# """cannot automate - check the table info is updated accordingly - has to be checked manually"""
# data_sources_page.clickConfirm()
# sleep(3)
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46032():
    pass


# """Step 1-5 pending due to web automation"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# sleep(2)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46032"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# if poco("Accept").exists():
#     template_management_page.clickAccept()
# """ Office 365 contacts """
# account = "zsbswdvt@gmail.com"
# data_sources_page.signInWithMicrosoft(account, "hmWepX4AUMLa!9E", False)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 27:
#     pass
# else:
#     if number_of_labels > 27:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.clickConfirm()
# sleep(3)
# """Cannot automate  - has to be done manually as unable to enter data for missing fields"""
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46033():
    pass


# """Step 1-5 pending due to web automation"""
# common_method.Start_The_App()
# registration_page.wait_for_element_appearance("Home", 20)
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46033"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# try:
#     common_method.wait_for_element_appearance_namematches("Label", 20)
# except:
#     raise Exception("Microsoft Login dialog popped up even after google account already login")
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 27:
#     pass
# else:
#     if number_of_labels > 27:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
# while not poco("Print").exists():
#     poco.scroll()
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.labelRangeSelection(7)
# sleep(3)
# template_management_page.verify_only_selected_rows_displayed_in_label_range("7")
# template_management_page.verify_label_navigation()
# """Cannot automate step 9 - has to be done manually anda also unable to enter data manually for missing fields"""
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# """Cannot automate-
# check that the labels are printed out with correct data
# check that the manually input values are printed out correctly
# check that the label with empty fields are still printed out with empty fields
# -has to be done manually"""
# """Step 11 pending as unable to enter data manually for missing fields"""
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46034():
    pass


# """Step 1-5 pending due to web automation"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@gmail.com", "zebraidctest@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46034"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# if poco("Accept").exists():
#     template_management_page.clickAccept()
# data_sources_page.checkIfAccPresentLink(account)
# data_sources_page.chooseAccToLinkFile(account)
# try:
#     registration_page.wait_for_element_appearance_text("Sign in to ZSB Series", 20)
#     poco.scroll()
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance_text("ZSB Series wants access to your Google Account", 20)
#     while not poco(text="Continue").exists():
#         poco.scroll()
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance_text(" wants to access your Google Account", 20)
#     while not poco(text="Allow").exists():
#         poco.scroll()
#     data_sources_page.clickAllow_Text()
# except:
#     pass
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 1:
#     pass
# else:
#     error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#     raise Exception(error)
# data_sources_page.clickLabelRange()
# sleep(2)
# if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#     pass
# else:
#     raise Exception("Tabel is not empty.")
# data_sources_page.clickBackArrow()
# """Step - 7 pending as input fields are not editable."""
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()

# """Cannot automate adding new contact to office 365 contacts-has to be done manually"""
# """Manual interruption required to add contacts in office 365"""
# """Account username - zsbswdvt@1234
# password- hmWepX4AUMLa"""


def test_Template_Management_TestcaseID_46034_1():
    pass


# """execute after executing test case 46034 first half"""
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# """Yet to execute as recently printed labels has bug"""
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 1:
#     pass
# else:
#     error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#     raise Exception(error)
# data_sources_page.clickLabelRange()
# sleep(2)
# if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#     raise Exception("Tabel is empty even after adding a contact.")
# data_sources_page.clickBackArrow()
# """Step - 7 pending as input fields are not editable."""
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46035():
    pass


# """Step 1-5 pending due to web automation"""
# """Select Office 365 account
# email-zsbswdvt1@gmail.com
# password - Zebra#123456789 in while creating template in web"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebratest850@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("Zebra#123456789", accounth)
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46035"
# data_sources_page.searchMyDesigns(search_label_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# poco("Accept").wait_for_appearance(timeout=10)
# template_management_page.clickAccept()
# """ google contacts """
# account = "zsbswdvt@gmail.com"
# """ Office 365 contacts """
# account = "zsbswdvt1@gmail.com"
# data_sources_page.signInWithMicrosoft(account, "Zebra#123456789", False)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
# label_range = 4
# data_sources_page.labelRangeSelection(label_range)
# "Unable to automate -check the table info is the same as your Office365 contact info in this different Microsoft account has to be done manually"
# for i in range(label_range):
#     data_sources_page.clickNext()
# template_management_page_1.check_element_exists_enabled("Next")
# poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# """Step 12 pending due to web automation - has to be executed manually"""


def test_Template_Management_TestcaseID_46036():
    pass


"""Step 1-5 pending due to web automation"""

#
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46031"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# poco("Accept").wait_for_appearance(timeout=10)
# template_management_page.clickAccept()
# """ google contacts """
# account = "zsbswdvt@gmail.com"
# data_sources_page.signInWithMicrosoft(account, "hmWepX4AUMLa!9E", False)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 27:
#     pass
# else:
#     if number_of_labels > 27:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# while not poco("Print").exists():
#     poco.scroll()
# """cannot automate - check all the link column values are correct, the preview image is correct"""
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.labelRangeSelection(4)
# sleep(3)
# template_management_page.verify_only_selected_rows_displayed_in_label_range("4")
# template_management_page.verify_label_navigation()
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# """Cannot automate adding new contact to office 365 contacts-has to be done manually"""
# registration_page.wait_for_element_appearance("Home", 20)
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# """Yet to execute as recently printed labels has bug"""
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 28:
#     pass
# else:
#     if number_of_labels > 28:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate -
# check all the link column values are correct, the preview image is correct
# check the delete contact is not shown
# check the updated value shown in that contact
# check the newly added contacts are shown
# -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# """cannot automate - check the table info is updated accordingly - has to be checked manually"""
# data_sources_page.clickConfirm()
# sleep(3)
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46027():
    pass
#
#
# """Step 1-5 pending due to web automation"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@1234", "zebraidctest@gmail.com")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# """Click My Data"""
# data_sources_page.click_My_Data()
# sleep(5)
# """Google Drive"""
# """Click Add file"""
# data_sources_page.click_Add_File()
# sleep(2)
# """Click Link File"""
# data_sources_page.click_Link_File()
# sleep(2)
# """ google drive """
# if data_sources_page.verifySignInWithGoogle():
#     registration_page.click_Google_Icon()
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("NAME", 20)
# data_sources_page.clickBackArrow()
# sleep(5)
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46027"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# if poco("Accept").exists():
#     template_management_page.clickAccept()
# """ google contacts """
# account = "zsbswdvt@gmail.com"
# if data_sources_page.checkIfAccPresentLink(account):
#     help_page.chooseAcc(account)
# else:
#     poco("com.google.android.gms:id/add_account_chip_title").click()
#     registration_page.sign_In_With_Google("zsbswdvt@1234", account)
#     sleep(2)
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 12:
#     pass
# else:
#     if number_of_labels > 12:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.clickConfirm()
# sleep(3)
# """Cannot automate  - has to be done manually as unable to enter data for missing fields"""
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# common_method.Stop_The_App()


# def test_Template_Management_TestcaseID_46028():
#     pass
#
#
# """Step 1-5 pending due to web automation"""
# common_method.Start_The_App()
# registration_page.wait_for_element_appearance("Home", 20)
# login_page.click_Menu_HamburgerICN()
# sleep(2)
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46028"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# try:
#     common_method.wait_for_element_appearance_namematches("Label", 20)
# except:
#     raise Exception("Google Login dialog popped up even after google account already login")
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 12:
#     pass
# else:
#     if number_of_labels > 12:
#         raise Exception("Label amount is more than the number of contacts.")
#     else:
#         raise Exception("Label amount is less than the number of contacts.")
# scroll_view = poco("android.widget.ScrollView")
# """verify label range navigation works"""
# template_management_page.verify_label_navigation()
# """cannot automate - check all the link column values are correct, the preview image is correct -has to be done manually"""
# data_sources_page.clickNext()
# data_sources_page.clickNext()
# data_sources_page.clickNext()
# data_sources_page.clickNext()
# while poco(nameMatches=".*Label . of .*").exists():
#     scroll_view.swipe("up")
# """check that variables with empty value in that contact are available for your to input the value at print time - unable to enter manually"""
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.choose_label_print_range()
# """cannot automate - check the table info is the same as your contact info - has to be checked manually"""
# data_sources_page.select_All(False)
# data_sources_page.clickBackArrow()
# data_sources_page.labelRangeSelection(7)
# sleep(3)
# template_management_page.verify_only_selected_rows_displayed_in_label_range("7")
# template_management_page.verify_label_navigation()
# """Cannot automate step 9 - has to be done manually anda also unable to enter data manually for missing fields"""
# while not poco("Print").exists():
#     poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete", 60)
# """Step 11 pending as unable to enter data manually for missing fields"""
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46029():
    pass


# """Step 1-5 pending due to web automation"""
# data_sources_page.clearAppData()
# common_method.Start_The_App()
# data_sources_page.allowPermissions()
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "zebraidctest@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("zebraidctest@gmail.com", "zebraidctest@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# search_label_name = "46029"
# data_sources_page.searchMyDesigns(search_label_name)
# common_method.wait_for_element_appearance_namematches("Showing")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# sleep(2)
# if poco("Accept").exists():
#     template_management_page.clickAccept()
# data_sources_page.checkIfAccPresentLink(account)
# data_sources_page.chooseAccToLinkFile(account)
# try:
#     registration_page.wait_for_element_appearance_text("Sign in to ZSB Series", 20)
#     poco.scroll()
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance_text("ZSB Series wants access to your Google Account", 20)
#     while not poco(text="Continue").exists():
#         poco.scroll()
#     data_sources_page.clickContinueWeb()
# except:
#     pass
# try:
#     registration_page.wait_for_element_appearance_text(" wants to access your Google Account", 20)
#     while not poco(text="Allow").exists():
#         poco.scroll()
#     data_sources_page.clickAllow_Text()
# except:
#     pass
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 1:
#     pass
# else:
#     error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#     raise Exception(error)
# data_sources_page.clickLabelRange()
# sleep(2)
# if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#     pass
# else:
#     raise Exception("Tabel is not empty.")
# data_sources_page.clickBackArrow()
# """Step - 7 pending as input fields are not editable."""
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# start_app("com.android.chrome")
# sleep(2)
# poco("com.android.chrome:id/tab_switcher_button").click()
# sleep(2)
# poco("com.android.chrome:id/new_tab_view_button").click()
# sleep(2)
# poco(text="Search or type URL").click()
# sleep(2)
# poco(text="Search or type URL").set_text("https://contacts.google.com/")
# data_sources_page.clickEnter()
# sleep(2)
# data_sources_page.lock_phone()
# wake()
# sleep(2)
# common_method.wait_for_element_appearance_text("Contacts", 20)
# try:
#     common_method.wait_for_element_appearance_text("Use the Contacts app")
#     if poco(text="Stay on web").exists():
#         poco(text="Stay on web").click()
# except:
#     pass
# template_management_page.changeAccInAddContacts(account)
# common_method.wait_for_element_appearance_text("Contacts")
# try:
#     common_method.wait_for_element_appearance_text("Use the Contacts app")
#     if poco(text="Stay on web").exists():
#         poco(text="Stay on web").click()
# except:
#     pass
# template_management_page.createContact("a", "1")
# stop_app("com.android.chrome")
# registration_page.wait_for_element_appearance("Home", 20)
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# """Yet to execute as recently printed labels has bug"""
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# common_method.wait_for_element_appearance_namematches("Label", 20)
# sleep(10)
# data_sources_page.verifyIfPreviewIsPresent()
# while not poco("Print").exists():
#     poco.scroll()
# number_of_labels = int(template_management_page.get_total_labels_printing())
# if number_of_labels == 1:
#     pass
# else:
#     error = f"There are {number_of_labels} labels printing even when connected to google account with no contacts."
#     raise Exception(error)
# data_sources_page.clickLabelRange()
# sleep(2)
# if poco("android.widget.CheckBox")[3].parent().child()[1].get_name() == "android.view.View":
#     raise Exception("Tabel is empty even after adding a contact.")
# data_sources_page.clickBackArrow()
# """Step - 7 pending as input fields are not editable."""
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46018():
    pass


# common_method.Start_The_App()
# """Step 1-4 pending due to web inconsistency"""
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("46018")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# data_sources_page.clickPrint()
# sleep(2)
# """Select column"""
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header()
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# scroll_view = poco("android.widget.ScrollView")
# while not poco("Print").exists():
#     scroll_view.swipe("up")
# template_management_page.choose_label_print_range()
# data_sources_page.select_All()
# data_sources_page.select_All(False)
# """Step -8,9 pending as search is not working."""
# """Check select all"""
# data_sources_page.select_All()
# data_sources_page.clickConfirm()
# if template_management_page.check_if_on_print_preview_page():
#     pass
# else:
#     raise Exception("Did not return to print preview page.")
# poco.scroll()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# selected_number_of_rows = "4"
# data_sources_page.labelRangeSelection(int(selected_number_of_rows))
# """Step -8,9 pending as search is not working."""
# if template_management_page.check_if_on_print_preview_page():
#     pass
# else:
#     raise Exception("Did not return to print preview page.")
# sleep(3)
# template_management_page.verify_only_selected_rows_displayed_in_label_range(selected_number_of_rows)
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46017():
    pass


# common_method.Start_The_App()
# """Step 1-4 pending due to web inconsistency"""
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("46017")
# data_sources_page.selectDesignCreatedAtSetUp()
# """Click print"""
# data_sources_page.clickPrint()
# """Select column"""
# data_sources_page.clickBackArrow()
# data_sources_page.clickContinue()
# data_sources_page.first_row_header()
# template_management_page.selectChooseAnOption(2)
# data_sources_page.clickContinue()
# template_management_page.check_if_on_print_preview_page()
# scroll_view = poco("android.widget.ScrollView")
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.verify_label_range_is_All()
# template_management_page.choose_label_print_range()
# try:
#     common_method.wait_for_element_appearance("Select label range")
# except:
#     raise Exception("Did not open print range dialog.")
# data_sources_page.select_All(False)
# data_sources_page.clickBackArrow()
# template_management_page.verify_label_range_is_All()
# data_sources_page.labelRangeSelection(3)
# sleep(2)
# """Cannot automate - check the one selected empty row will be disabled and empty - has to be done manually"""
# """Cannot automate - check that each labels can be previewed correctly - has to be checked manually"""
# template_management_page.verify_label_navigation()
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46037():
    pass


# common_method.Start_The_App()
# """Log out of existing account"""
# login_page.click_Menu_HamburgerICN()
# registration_page.click_on_profile_edit()
# while not poco("Log Out").exists():
#     poco.scroll()
# registration_page.click_log_out_button()
# """Login to account with 100+designs"""
# registration_page.clickSignIn()
# # login_page.click_loginBtn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# account = "sohozsb@gmail.com"
# if template_management_page.checkIfAccPresent(account):
#     help_page.chooseAcc(account)
# else:
#     while not poco(text="Use another account").exists():
#         poco.scroll()
#     login_page.click_GooglemailId()
#     while not poco(text="Add account to device").exists():
#         poco.scroll()
#     registration_page.addAccountToDevice()
#     registration_page.sign_In_With_Google("sohozsb@gmail.com", "sohozst@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     raise Exception("home page dint show up")
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# initial_design_count = template_management_page.get_showing_n_designs_number()
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
# data_sources_page.click_Menu_HamburgerICNWeb()
# scroll_view = poco("android.view.View")
# while poco(text="This is where you can access all of your saved designs.").exists():
#     scroll_view.swipe("up")
# if template_management_page.verify_My_Designs_pagination():
#     pass
# else:
#     raise Exception("All templates did not show up with pagination")
# template_management_page.verify_pagination_shown_is_correct()
# data_sources_page.clickCreateDesignBtn()
# data_sources_page.lock_phone()
# wake()
# """Step 4 pending due to web inconsistency."""
# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# new_design_count = template_management_page.get_showing_n_designs_number()
# if new_design_count == initial_design_count+1:
#     pass
# else:
#     error = f"{new_design_count} is not equal to {initial_design_count}+1"
#     raise Exception(error)
# """Step 5 check template total number add one pending"""
# """Search and select design created in web"""
# data_sources_page.searchMyDesigns("ZZZ_Test")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# common_method.Stop_The_App()

def test_Template_Management_TestcaseID_46038():
    pass


# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# """Step 2, 3 pending as no pagination on mobile app"""
# """Navigating to page 3 pending as no pagination on app"""
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# """Step 5 - Repeat for all pages pending as no pagination on app"""
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46039():
    pass


# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# initial_design_count = int(template_management_page.get_showing_n_designs_number())
# """Step 2 pending as no pagination on mobile app"""
# """Navigating to page 3 pending as no pagination on app"""
# data_sources_page.selectDesignCreatedAtSetUp()
# template_management_page.clickDuplicateDesign()
# new_name = "Duplicate Test"
# template_management_page.new_design_name(new_name)
# template_management_page.clickSave()
# common_method.wait_for_element_appearance_namematches("Showing")
# new_design_count = int(template_management_page.get_showing_n_designs_number())
# if new_design_count == initial_design_count+1:
#     pass
# else:
#     error = f"{new_design_count} is not equal to {initial_design_count}+1({initial_design_count+1})"
#     raise Exception(error)
# data_sources_page.searchMyDesigns(new_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# copies = 2
# template_management_page.changeCopiesCount(copies)
# keyevent("Enter")
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# template_management_page.changeCopiesCount(" ")
# keyevent("Enter")
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page.verifyErrorPopUp_forInvalidCopies()
# data_sources_page.clickContinue()
# template_management_page.changeCopiesCount("$")
# keyevent("Enter")
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page.verifyErrorPopUp_forInvalidCopies()
# data_sources_page.clickContinue()
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46040():
    pass


# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# initial_design_count = int(template_management_page.get_showing_n_designs_number())
# """Step 2 pending as no pagination on mobile app"""
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("Address")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Categories")
# template_management_page.select_design_common_designs()
# template_management_page.select_label_common_designs()
# template_management_page.click_copy_to_My_Designs()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# new_design_count = int(template_management_page.get_showing_n_designs_number())
# if new_design_count == initial_design_count+1:
#     pass
# else:
#     error = f"{new_design_count} is not equal to {initial_design_count}+1({initial_design_count+1})"
#     raise Exception(error)
# data_sources_page.searchMyDesigns("Address copy")
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# copies = 2
# template_management_page.changeCopiesCount(copies)
# keyevent("Enter")
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_46041():
    pass


# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# initial_design_count = template_management_page.get_showing_n_designs_number()
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
# data_sources_page.click_Menu_HamburgerICNWeb()
# scroll_view = poco("android.view.View")
# while poco(text="This is where you can access all of your saved designs.").exists():
#     scroll_view.swipe("up")
# if template_management_page.verify_My_Designs_pagination():
#     pass
# else:
#     raise Exception("All templates did not show up with pagination")
# design_selected = "Sale" + " copy"
# downloaded_design_name = design_selected + ".nlbl"
# template_management_page.clickImport()
# data_sources_page.searchFileInLocalStorage(downloaded_design_name, "Downloads")
# """Step 4 pending due to web inconsistency."""
# common_method.Start_The_App()
# """Open My designs"""
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# common_method.wait_for_element_appearance_namematches("Showing")
# new_design_count = template_management_page.get_showing_n_designs_number()
# if new_design_count == initial_design_count+1:
#     pass
# else:
#     error = f"{new_design_count} is not equal to {initial_design_count}+1"
#     raise Exception(error)
# data_sources_page.searchMyDesigns(design_selected)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# common_method.Stop_The_App()


def test_Template_Management_TestcaseID_50656():
    pass

# common_method.Start_The_App()
# login_page.click_Menu_HamburgerICN()
# template_management_page.clickCommonDesigns()
# template_management_page_1.wait_for_element_appearance_name_matches_all("Address")
# template_management_page.search_design_common_designs("PickImage")
# keyevent("Enter")
# common_method.wait_for_element_appearance_namematches("Designs")
# template_management_page.select_label_common_designs()
# data_sources_page.clickPrint()
# template_management_page.selectChooseAnOption(1, "Zebra Gallery")
# try:
#     template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
# except:
#     raise Exception("Zebra Gallery did not load.")
# all_Icons = template_management_page.get_all_icons_zebra_gallery()
# search_keyword = "Error"
# template_management_page.search_Icons(search_keyword)
# keyevent("Enter")
# search_results = template_management_page.get_all_icons_zebra_gallery()
# for icon in search_results:
#     if search_keyword in icon:
#         pass
#     else:
#         raise Exception("Search results do not contain the search keyword.")
# template_management_page.search_Icons("")
# keyevent("Enter")
# icons_after_clearing_search = template_management_page.get_all_icons_zebra_gallery()
# if all_Icons == icons_after_clearing_search:
#     pass
# else:
#     raise Exception("All Icons did not show up after clearing search text.")
# common_method.Stop_The_App()
# """Sign in same account in web portal, go to my designs, create/edit a design, add an image, set it to prompt at print needs to be executed manually due to web inconsistency """
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
# # a,b = poco(text="Undo last operation. Max of 10 undo steps are supported.").get_position()
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
# design_name = "Pic_PromptAtPrint"
# # data_sources_page.setLabelName(design_name)
# # sleep(5)
# # data_sources_page.exitDesigner()
# """Web pending due to inconsistent behaviour"""
# common_method.Start_The_App()
# registration_page.wait_for_element_appearance("Home")
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickMyDesigns()
# data_sources_page.searchMyDesigns(design_name)
# data_sources_page.selectDesignCreatedAtSetUp()
# data_sources_page.clickPrint()
# template_management_page.selectChooseAnOption(1, "Zebra Gallery")
# try:
#     template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
# except:
#     raise Exception("Zebra Gallery did not load.")
# template_management_page.clickSearchIconTextBox()
# template_management_page.clickSearchIcon()
# keyevent("Enter")
# all_iconsAfterClickingSearch = template_management_page.get_all_icons_zebra_gallery()
# if all_iconsAfterClickingSearch == all_Icons:
#     pass
# else:
#     raise Exception("All Icons did not show up.")
# template_management_page.clickFirstIcon()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print not successful.")
# data_sources_page.clickBackArrow()
# login_page.click_Menu_HamburgerICN()
# data_sources_page.clickHome()
# registration_page.wait_for_element_appearance("Recently Printed Labels", 20)
# """Yet to execute as recently printed labels has bug"""
# template_management_page_1.click_first_design_in_recently_printed_labels()
# data_sources_page.clickPrint()
# template_management_page.selectChooseAnOption(1, "Zebra Gallery")
# try:
#     template_management_page.wait_for_element_appearance_type("android.widget.ImageView")
# except:
#     raise Exception("Zebra Gallery did not load.")
# template_management_page.clickSearchIconTextBox()
# template_management_page.clickSearchIcon()
# keyevent("Enter")
# all_iconsAfterClickingSearch = template_management_page.get_all_icons_zebra_gallery()
# if all_iconsAfterClickingSearch == all_Icons:
#     pass
# else:
#     raise Exception("All Icons did not show up.")
# template_management_page.clickFirstIcon()
# while not poco("Print").exists():
#     poco.scroll()
# template_management_page.wait_for_appearance_enabled("Print")
# data_sources_page.clickPrint()
# try:
#     template_management_page_1.wait_for_element_appearance_name_matches_all("Print complete")
# except:
#     raise Exception("Print not successful.")
# common_method.Stop_The_App()
