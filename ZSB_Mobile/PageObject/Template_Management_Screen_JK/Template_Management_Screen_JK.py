import datetime
import time
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoTargetTimeout
import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\\templates",
                            a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)

from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen import Login_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class Template_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Search_place_holder = Template(Basic_path(r"search_design_placeholder.png"), record_pos=(-0.192, -0.609),
                                            resolution=(1080, 2280))
        self.Search_icon = Template(Basic_path(r"search_Icon.png"), record_pos=(-0.398, -0.605),
                                    resolution=(1080, 2280))
        self.Search_files_place_holder = Template(Basic_path(r"search_files_place_holder.png"),
                                                  record_pos=(-0.203, -0.584),
                                                  resolution=(1080, 2340))
        self.search_icons_text_box = Template(Basic_path(r"search_Icons_text_box.png"), record_pos=(-0.233, -0.736),
                                              resolution=(1080, 2400))

    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        common_method.run_the_command(cmd)

    def get_showing_n_designs_number(self):
        self.poco(nameMatches=".*Showing.*").wait_for_appearance(timeout=10)
        a = self.poco(nameMatches=".*Showing.*").get_name()
        a = a.split(" ")
        return a[1]

    def Turn_Off_wifi(self):
        command = "adb shell svc wifi disable"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)

    def Turn_ON_wifi(self):
        command = "adb shell svc wifi enable"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)

    def verify_default_sort_my_designs(self):
        return self.poco("Name (A to Z)").exists()

    def click_sort_my_designs(self):
        self.poco(nameMatches="Name(.*)").click()

    def verify_sort_options_my_designs(self):
        if len(self.poco("android.view.View")[6].child()) == 2:
            if self.poco("android.view.View")[6].child()[0].get_name() == "Name (A to Z)":
                if self.poco("android.view.View")[6].child()[1].get_name() == "Name (Z to A)":
                    pass
                else:
                    raise Exception("\"Name (Z to A)\" is not present.")
            else:
                raise Exception("\"Name (A to Z)\" is not present.")
        else:
            raise Exception(f"There are {len(self.poco("android.view.View")[6].child())} options present.")

    def verify_default_filter_my_designs(self):
        if not self.poco("All sizes").exists():
            raise Exception("Default filter is not \"All sizes\"")

    def verify_default_sort_order_back_to_normal(self):
        if self.verify_default_filter_my_designs():
            pass
        else:
            raise Exception("Sorting order is not back to default sort order - \"Name (A to Z)\" in my designs.")

    def verify_sort_order_my_designs(self, sort_order):
        if sort_order == "A-Z":
            return self.poco("Name (A to Z)").exists()
        elif sort_order == "Z-A":
            return self.poco("Name (Z to A)").exists()

    def click_filter_my_designs(self, name=None):
        if name is not None:
            if name == "All sizes":
                self.poco("All sizes").click()
        else:
            self.poco(nameMatches="Name(.*)").parent().child()[3].click()

    def waitForAppearanceOfCategories(self):
        sleep(10)
        if self.poco(nameMatches=".*Categories.*").exists():
            pass
        else:
            raise Exception("Categories not shown.")

    def waitForAppearanceOfNoResultsFound(self):
        sleep(10)
        if self.poco(
                nameMatches=".*No results found.\nSearch tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then.*").exists():
            pass
        else:
            raise Exception("\"No results found\" message not displayed.")

    def selectFilter(self, filterOptionNumber):
        selected_option = self.poco("android.view.View")[6].child()[filterOptionNumber].get_name()
        self.poco("android.view.View")[6].child()[filterOptionNumber].click()
        return selected_option

    def click_sort_common_designs(self):
        self.poco(nameMatches="Name(.*)").click()

    def click_filter_common_designs(self):
        self.poco(nameMatches="Name(.*)").parent().child()[2].click()

    def get_filter_value(self):
        return self.poco("android.view.View")[5].child()[2].get_name()

    def verify_connection_error_app(self):
        return self.poco("An error occurred when loading your designs. Please tap to try again").exists()

    def wait_for_appearance_designs_in_a_particular_category(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=10)

    def get_all_designs_in_my_designs(self, name=False):
        first_design = self.poco("android.view.View").child(type="android.widget.ImageView").get_name()
        total = []
        prev = []
        while 1:
            if name:
                curr = [child.get_name().split("\n")[0] for child in
                        self.poco("android.view.View").child(type="android.widget.ImageView")]
            else:
                curr = [child.get_name() for child in
                        self.poco("android.view.View").child(type="android.widget.ImageView")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)
            if curr == prev:
                break
            self.poco.swipe([0.5, 0.9], [0.5, 0.5])
            prev = curr
        while not self.poco(first_design).exists():
            self.poco.swipe([0.5, 0.5], [0.5, 0.9])
        return total

    def get_all_designs_size_in_my_designs(self):
        first_design = self.poco("android.view.View").child(type="android.widget.ImageView").get_name()
        total = []
        prev = []
        label_sizes = set()
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)

            if curr == prev:
                break

            self.poco.swipe([0.5, 0.9], [0.5, 0.5])
            prev = curr
        for i in total:
            label_sizes.add(i.split("\n")[1])
        while not self.poco(first_design).exists():
            self.poco.swipe([0.5, 0.5], [0.5, 0.9])
        return label_sizes

    def check_there_are_less_than_100_designs(self, design_list):
        if len(design_list) <= 100:
            pass
        else:
            raise Exception("There are more than 100 designs.")

    def check_if_design_count_incremented_by_1(self, new_design_count, initial_design_count):
        if new_design_count == initial_design_count + 1:
            pass
        else:
            error = f"{new_design_count} is not equal to {initial_design_count}+1"
            raise Exception(error)

    def filter_options(self, length=False):

        filter_option_list = []
        if length:
            return len(self.poco("android.view.View")[6].child())
        else:
            for i in range(1, len(self.poco("android.view.View")[6].child())):
                filter_option_list.append(self.poco("android.view.View")[6].child()[i].get_name())
            return filter_option_list

    def verify_design_names_follow_order(self, design_names, sort_order="A-Z"):
        start_with_special_character = False
        start_with_number = False
        start_with_alphabet = False
        previous_design_name = None
        previous_design_num = None
        if sort_order == "A-Z":
            for name in design_names:
                if name[0].isalpha():
                    if not start_with_number and not start_with_special_character:
                        raise Exception(
                            "Design name starting with alphabets found before design names starting with number and special characters... ")
                    start_with_alphabet = True
                    if previous_design_name is not None and name <= previous_design_name:
                        raise Exception(f"Design {name} not following sort order:{sort_order}.")
                    previous_design_name = name
                elif name[0].isdigit():
                    if start_with_alphabet:
                        raise Exception(
                            "Design name starting with number found after design names starting with alphabets... ")
                    start_with_number = True
                    if previous_design_num is not None and name <= previous_design_num:
                        raise Exception(f"Design {name} not following order 0-9 for designs starting with numbers..")
                    previous_design_num = name
                else:
                    if start_with_number or start_with_alphabet:
                        raise Exception(
                            "Design name starting with special characters found after design names starting with number or alphabets...")
                    start_with_special_character = True
        elif sort_order == "Z-A":
            for name in design_names:
                if name[0].isalpha():
                    if start_with_number or start_with_special_character:
                        raise Exception(
                            "Design name starting with alphabets found after design names starting with number or special characters... ")
                    start_with_alphabet = True
                    if previous_design_name is not None and name >= previous_design_name:
                        raise Exception(f"Design {name} not following sort order:{sort_order}.")
                    previous_design_name = name
                elif name[0].isdigit():
                    if start_with_special_character:
                        raise Exception(
                            "Design name starting with number found after design names starting with special characters... ")
                    start_with_number = True
                    if previous_design_num is not None and name >= previous_design_num:
                        raise Exception(f"Design {name} not following order 9-0 for designs starting with numbers..")
                else:
                    if not start_with_number and not start_with_alphabet:
                        raise Exception(
                            "Design name starting with special characters found before design names starting with number and alphabets...")
                    start_with_special_character = True

    def check_design_count_title(self, length):
        return self.poco(f"Showing {length} Designs").exists()

    def clickCommonDesigns(self):
        self.poco("Common Designs").click()

    def checkIfAccPresentGoogleContacts(self, account):
        self.poco(textMatches="Hide more account").parent()
        parent = self.poco(textMatches=".*Hide more accounts.*").parent()
        while 1:
            for i in range(len(parent.child())):
                if parent.child()[i].get_name() == "Add another account (opens a new tab)":
                    return False
                elif account in parent.child()[i].get_name():
                    return True
            self.poco.scroll()
            keyevent('adb shell input keyevent 26')
            wake()
            sleep(2)
            if self.poco(text="Contacts").exists():
                self.poco(textMatches=".*Google Account:.*").click()
            sleep(2)
            parent = self.poco(nameMatches=".*Add another account.*").parent()

    def checkIfAccPresent(self, account):
        start = 0
        end = 1
        while True:
            for i in range(start, len(self.poco("android.widget.ListView").child()) - end):
                if self.poco("android.widget.ListView").child()[i].child().child()[
                    0].get_text() == "Use another account":
                    return False
                elif self.poco("android.widget.ListView").child()[i].child().child()[1].get_text() == account:
                    return True
            start = 1
            end = 0
            self.poco.scroll()

    def search_design_common_designs(self, design_name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(design_name)

    def select_design_common_designs(self):
        sleep(3)
        self.poco("android.view.View")[7].child()[1].child().click()

    def select_design_common_designs_Web(self):
        sleep(3)
        if self.poco("android.widget.Image")[1].exists():
            self.poco("android.widget.Image")[1].click()

    def select_label_common_designs_Web(self):
        if self.poco("android.widget.Image")[2].exists():
            self.poco("android.widget.Image")[2].click()

    def select_label_common_designs(self):
        sleep(2)

        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=10)
        label_name = self.poco("android.view.View").child(type="android.widget.ImageView").get_name().split("\n")[0]
        self.poco("android.view.View").child(type="android.widget.ImageView").click()
        return label_name

    def get_name_of_selected_design(self):
        design_name = self.poco(textMatches="Edit").parent().parent().parent().parent().child()[0].child()[1].get_text()
        return design_name

    def click_copy_to_My_Designs(self):
        try:
            self.poco("Copy to My Designs").click()
        except:
            self.poco(text="Copy to My Designs").click()

    def get_first_design_name_my_designs(self):
        return self.poco("android.view.View")[8].child().child().get_name().split("\n")[0]

    def check_for_suggestion_drop_down_in_search_designs(self):
        a = self.poco(nameMatches="(?s).*result.*")[0].exists()
        return a

    def checkNumberOfDesignsMatchingDropDown(self):
        drop_down_results = len(self.poco("android.view.View")[3].child())
        for i in range(drop_down_results):
            print(self.poco("android.view.View")[3].child()[i].get_name().split("\n")[1])
            if fnmatch.fnmatch(self.poco("android.view.View")[3].child()[i].get_name().split("\n")[1], "? result"):
                pass
            else:
                raise Exception(
                    "Number of design that matches the list in the suggestion dropdown is not displayed on the right side of each.")

    def check_dropdown_options_Are_clickable(self):
        drop_down_result_1 = self.poco("android.view.View")[3].child().get_name()
        return self.poco(name=drop_down_result_1, enabled=True).exists()

    def click_drop_down_result_1(self, returnName=None):
        if self.poco(nameMatches="(?s).*DESIGNS.*").exists():
            return_value = self.poco(nameMatches="(?s).*DESIGNS.*").get_name().split("\n")[1]
            self.poco(nameMatches="(?s).*DESIGNS.*").click()
        elif self.poco(nameMatches="(?s).*result.*").exists():
            return_value = self.poco(nameMatches="(?s).*result.*").get_name().split("\n")[0]
            self.poco(nameMatches="(?s).*result.*").click()
        elif self.poco(nameMatches="(?s).*CATEGORIES.*").exists():
            return_value = self.poco(nameMatches="(?s).*CATEGORIES.*").get_name().split("\n")[1]
            self.poco(nameMatches="(?s).*CATEGORIES.*").click()
        if returnName is not None:
            return return_value

    def select_sort_order(self, sort_order):
        if sort_order == "A-Z":
            self.poco("Name (A to Z)").click()
        elif sort_order == "Z-A":
            self.poco("Name (Z to A)").click()

    def verify_designs_are_according_to_sort_order(self, design_list):
        if self.poco("android.view.View")[6].child()[0].get_name() == "Name (A to Z)":
            for i in range(len(design_list) - 1):
                if design_list[i] > design_list[i + 1]:
                    return False
            return True
        elif self.poco("android.view.View")[6].child()[0].get_name() == "Name (Z to A)":
            for i in range(1, len(design_list)):
                if design_list[i - 1] < design_list[i]:
                    return False
            return True

    def select_label_size(self):
        size = self.poco("android.view.View")[6].child()[1].get_name()
        self.poco("android.view.View")[6].child()[1].click()
        return size

    def verify_search_placeholder(self):
        return assert_exists(self.Search_place_holder, "Search design place holder present.")

    def verify_search_drop_down_results(self, search_text):
        for i in range(len(self.poco("android.view.View")[3].child())):
            result = self.poco("android.view.View")[3].child()[i].get_name().split("\n")[0]
            if search_text.lower() in result.lower():
                pass
            else:
                raise Exception("search text not present in one of the dropdown result.")

    def wait_for_suggestions_to_appear(self):
        self.poco(nameMatches="(?s).*result.*").wait_for_appearance(timeout=10)

    def click_Connect_Data_File(self):
        self.poco(text="Connect Data File").wait_for_appearance(timeout=10)
        self.poco(text="Connect Data File").focus([0.1, 0.5]).click()

    def select_file_from_Connect_Data_File(self, name=None):
        if name is not None:
            self.poco(textMatches="columnWithUnequalRows.xlsx.*").click()
        else:
            self.poco("android.widget.TextView")[3].click()
            return self.poco("android.widget.TextView")[3].get_text().split(" ")[0]

    def click_from_data_file(self):
        self.poco(text="   From Data File").focus([0.0, 0.5]).click()

    def checkIfZebraGalleryLoaded(self):
        try:
            self.wait_for_element_appearance_type("android.widget.ImageView")
        except:
            raise Exception("Zebra Gallery did not load.")

    def checkIfAllIconsShowedUp(self, iconsAfterClickingSearch, defaultIcons):
        if iconsAfterClickingSearch == defaultIcons:
            pass
        else:
            raise Exception("All Icons did not show up after clearing search text.")

    def clickAddText(self):
        self.poco(text="Add text").click()

    def placeText(self):
        touch(Template(Basic_path(r"tpl1708429167702.png"), record_pos=(-0.109, 0.382), resolution=(1080, 2340)))

    def checkManualInput_checkbox(self):
        if self.poco("android.widget.CheckBox", checked=True):
            pass
        else:
            self.poco("android.widget.CheckBox").click()

    def verify_print_preview(self, preview_name):
        assert_exists(
            Template(Basic_path(rf"{preview_name}.png"), record_pos=(-0.001, -0.045), resolution=(1080, 2340)),
            "Preview is present.")

    def verify_label_range_navigation_unavailable(self):
        return self.poco("Label 1 of 1").exists()

    def fillOrganizationId(self, Id):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(Id)

    def fillIndex(self, index):
        self.poco("android.widget.EditText")[1].click()
        self.poco("android.widget.EditText")[1].set_text(index)

    def verify_if_on_relink_data_source_page(self):
        return self.poco(nameMatches=".*Relink.*").exists()

    def verify_if_on_update_connections_page(self):
        return self.poco(nameMatches="Update Data Connections").exists()

    def verify_duplicate_previous_next_button(self):
        if self.poco("Previous")[1].exists():
            return True
        if self.poco("Next")[1].exists():
            return True
        return False

    def select_second_colum_from_data_file(self):
        self.poco("android.widget.TextView")[7].focus([0.1, 0.5]).click()
        self.poco("android.widget.TextView")[9].focus([0.1, 0.5]).click()

    def get_child_count_file_update_data_connections(self):
        if self.poco(type="android.view.View", nameMatches=".*(Local File).*").exists():
            child_count = len(self.poco(type="android.view.View", nameMatches=".*(Local File).*").parent().child())
        elif self.poco(type="android.view.View", nameMatches=".*(OneDrive).*").exists():
            child_count = len(self.poco(type="android.view.View", nameMatches=".*(OneDrive).*").parent().child())
        else:
            child_count = len(self.poco(type="android.view.View", nameMatches=".*(Google Drive).*").parent().child())
        return child_count

    def get_child_file_update_data_connections(self, index):
        try:
            child = self.poco(type="android.view.View", nameMatches=".*(Local File).*").parent().child()[
                index].get_name()
        except:
            try:
                child = self.poco(type="android.view.View", nameMatches=".*(OneDrive).*").parent().child()[
                    index].get_name()
            except:
                child = self.poco(type="android.view.View", nameMatches=".*(Google Drive).*").parent().child()[
                    index].get_name()
        return child

    def select_child_file_update_data_connections(self, index):
        try:
            self.poco(type="android.view.View", nameMatches=".*(Local File).*").parent().child()[index].click()
        except:
            try:
                self.poco(type="android.view.View", nameMatches=".*(OneDrive).*").parent().child()[index].click()
            except:
                self.poco(type="android.view.View", nameMatches=".*(Google Drive).*").parent().child()[index].click()

    def choose_file_update_data_connections(self, filename):
        child_count = self.get_child_count_file_update_data_connections()
        last_child = self.get_child_file_update_data_connections(child_count - 1)
        while 1:
            for i in range(child_count):
                if self.get_child_file_update_data_connections(i) == filename:
                    self.select_child_file_update_data_connections(i)
                    return
            self.poco.scroll()
            new_child_count = self.get_child_count_file_update_data_connections()
            new_last_child = self.get_child_file_update_data_connections(new_child_count - 1)
            if new_last_child == last_child:
                raise Exception("Did not find file")
            last_child = new_last_child
            child_count = new_child_count

    def continueDisabled(self):
        if self.poco("Continue", enabled=False).exists():
            return True

    def choose_file_relink_data_sources(self, option_name):
        self.poco(option_name).click()

    def checkIfOnRelinkDataSourcesPage(self):
        if self.poco("Relink Data Source Columns").exists():
            return True

    def checkIfOnPrintPage(self):
        return self.poco(nameMatches=".*Label.*").exists()

    def selectChooseAnOption(self, option_count=1, option_name=None, click=True):
        sleep(2)
        choice_name = False
        try:
            self.poco(nameMatches="(?s).*Choose an option.*").wait_for_appearance(timeout=20)
        except:
            sleep(3)

        for i in range(1, option_count + 1):
            if self.checkIfOnRelinkDataSourcesPage() or self.checkIfOnPrintPage():
                choice_name = True
            try:
                self.poco(nameMatches="(?s).*Choose an option.*").click()
            except:
                self.poco(nameMatches="(?s).*Continue.*").parent().child()[2].click()
            if click:
                if option_name is None:
                    self.poco("android.view.View")[6].child()[option_count - i].click()
                else:
                    if choice_name:
                        self.choose_file_relink_data_sources(option_name)
                    else:
                        self.choose_file_update_data_connections(option_name)

    def verify_label_range_is_All(self):
        if self.poco("All").exists():
            return
        raise Exception("Label Range is not 'All'")

    def verify_label_navigation(self):
        scroll_view = self.poco("android.widget.ScrollView")
        while not self.poco(nameMatches=".*Label . of .*").exists():
            scroll_view.swipe("down")
        for i in range(5):
            scroll_view.swipe("down")
        initial = self.poco(nameMatches=".*Label . of .*").get_name()
        print(initial)
        self.poco("Next").click()
        navigated_next = self.poco(nameMatches=".*Label . of .*").get_name()
        print(navigated_next)
        self.poco("Previous").click()
        navigated_previous = self.poco(nameMatches=".*Label . of .*").get_name()
        print(navigated_previous)
        if navigated_next != initial:
            if navigated_previous == initial:
                return
        raise Exception("'Previous' and 'Next' navigation buttons are not functioning.")

    def check_total_label_for_print_count(self, n):
        return self.poco(f"Total of {n} labels").exists()

    def get_total_labels_printing(self):
        return self.poco(nameMatches=".*Total.*").get_name().split(" ")[2]

    def get_total_contacts(self):
        return self.poco(nameMatches=".*Label 1 of.*").get_name().split(" ")[3]

    def choose_label_print_range(self):
        self.poco("android.widget.ScrollView").child()[-7].click()

    def rename_Design(self):
        self.poco("Rename").click()

    def new_design_name(self, name):
        self.poco("android.widget.EditText").focus([0.5, 0.45]).click()
        self.poco("android.widget.EditText").set_text(name)

    def clickDuplicateDesign(self):
        self.poco("Duplicate").click()

    def clickDeleteDesign(self):
        self.poco("Delete").click()

    def verifyLabelsShown(self):
        try:
            self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=20)
        except:
            raise Exception("Error in displaying round labels.")

    def change_print_value(self, value):
        self.poco("android.widget.EditText").set_value(value)

    def click_print_value(self):
        self.poco("android.widget.EditText").click()

    def get_print_value(self):
        return self.poco("android.widget.EditText").get_text()

    def compare_element_text(self, element, expected_text):
        element_text = element.get_text()
        print(f"Text from the element: {element_text}")
        if element_text == expected_text:
            print("Text matches the expected value.")
            assert False

    def verifySearchCommonDesignPlaceHolder(self):
        return assert_exists(self.Search_place_holder, "Search placeholder is present")

    def verifySearchIcon(self):
        return assert_exists(self.Search_icon, "Search icon is present")

    def checkIfElementIsPresent(self, element):
        try:
            a = self.poco(element).exists()
            return a
        except:
            a = self.poco(text=element).exists()
            return a

    def verifySearchFiles(self):
        return assert_exists(self.Search_files_place_holder, "Search placeholder is present")

    def clickSearchIconTextBox(self):
        touch(self.search_icons_text_box)

    def clickSearchIcon(self):
        touch(self.Search_icon)

    def clickFirstIcon(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").click()

    def get_drop_down_list_common_designs(self, category=False):
        prev = []
        temp = []
        flag = 1
        while flag:
            curr = [child.get_name() for child in
                    self.poco("android:id/content").child("android.widget.FrameLayout").child().child().child()[
                        0].child().child().child()]
            if curr == prev:
                break
            for i in curr:
                if i not in temp:
                    if "CATEGORIES" in i or "DESIGNS" in i:
                        i = i.split("\n")[1]
                    if category:
                        if "DESIGNS" in i:
                            flag = 0
                            break
                    temp.append(i)
            prev = curr
            self.poco.swipe([0.5, 0.5], [0.5, 0.2])
        return temp

    def clickCancelSearch(self):
        self.poco("android.widget.Button")[-1].click()

    def get_all_categories_in_common_designs(self, name=False):
        temp = []
        prev = []
        while 1:
            if name:
                curr = [child.get_name().split('\n')[0] for child in
                        self.poco(nameMatches="(?s).*For use with Label Cartridges:.*")]
            else:
                curr = [child.get_name() for child in self.poco(nameMatches="(?s).*For use with Label Cartridges:.*")]
            for i in curr:
                if i not in temp:
                    temp.append(i)
            if prev == curr:
                break
            prev = curr
            self.poco.scroll()
        return temp

    def get_all_designs_in_search_designs(self, name=False):
        while not self.poco(nameMatches=".*Designs .*", enabled=True).exists():
            self.poco.scroll()

        temp = self.get_all_designs_in_my_designs(name)
        return temp

    def waitForAppearanceTypeName(self, elementType, elementName, time_out=20):
        self.poco(type=elementType, nameMatches="(?s).*" + elementName + ".*").wait_for_appearance(timeout=time_out)

    def get_all_search_results_in_search_designs(self, name=False):
        a = len(self.poco(nameMatches="(?s).*result.*"))
        temp = []
        if a < 5:
            for i in range(a):
                if name:
                    temp.append(self.poco(nameMatches="(?s).*result.*")[i].get_name().split("\n")[0])
                else:
                    temp.append(self.poco(nameMatches="(?s).*result.*")[i].get_name())
        else:
            total = []
            prev = []
            while 1:
                if name:
                    curr = [child.get_name().split("\n")[0] for child in self.poco(nameMatches="(?s).*result.*")]
                else:
                    curr = [child.get_name() for child in self.poco(nameMatches="(?s).*result.*")]
                if curr != prev:
                    for i in curr:
                        if i not in total:
                            total.append(i)

                if curr == prev:
                    break

                self.poco.swipe([0.5, 0.5], [0.5, 0.2])
                prev = curr

            return total
        return temp

    def check_if_drop_down_list_contains_results_that_include_search_keyword(self, search_keyword):
        drop_down_list = self.get_all_search_results_in_search_designs()
        for result in drop_down_list:
            if search_keyword in result:
                pass
            else:
                raise Exception("Drop down list contains results that do not include the search keyword")

    def click_scrim(self):
        self.poco("Scrim").click()

    def verifySearchResults_n(self, n):
        return self.poco(f"Search results ({n})").exists()

    def check_suggestion_window_in_common_design(self):
        regex_pattern = "(?s).*CATEGORIES.*"
        a = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*DESIGNS.*"
        b = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*No results found..*"
        c = self.poco(nameMatches=regex_pattern).exists()

        regex_pattern = "(?s).*result.*"
        d = self.poco(nameMatches=regex_pattern).exists()

        return a or b or c or d

    def check_if_drop_down_list_open(self):
        sleep(2)
        if self.check_suggestion_window_in_common_design():
            pass
        else:
            raise Exception("Drop down list did not appear.")
        sleep(2)

    def check_if_drop_down_list_close(self):
        if self.check_suggestion_window_in_common_design():
            raise Exception("Drop down list did not close.")
        else:
            pass

    def get_all_fields_print_page(self):
        elements = set()
        previous = set()
        while 1:
            current = set()
            for child in self.poco("android.widget.ScrollView").child("android.view.View").child():
                current.add(child.get_text())
            if current == previous:
                break
            elements = elements.union(current)
            previous = current.copy()
            self.poco.scroll()
        return elements

    def fill_all_print_fields(self, value=None):
        elements = []
        previous = []
        while 1:
            current = []
            for child in self.poco("android.widget.ScrollView").child("android.view.View").child():
                current.append(child.get_text())
            if current == previous:
                break
            for field in current:
                print(field)
                if field is not None and field not in elements:
                    print("selection " + field)
                    if value is None:
                        random_word = data_sources_page.generateRandomWordLetters(8)
                    else:
                        random_word = value
                    print(random_word)
                    self.poco(text=field).click()
                    self.poco(text=field).set_text(random_word)
                    keyevent("back")
                    sleep(2)
                    elements.append(random_word)
            previous = current

    def getLastPrintFromFirstDesignInRecentlyPrintedDesigns(self):
        return \
            self.poco("android.view.View").child(type="android.widget.ImageView")[1].get_name().split("\n")[-1].split(
                ":")[
                -1].strip()

    def get_remaining_label_count(self):
        labels_left = int(self.poco(nameMatches=".*Printer.*").get_name().split(" ")[1][1:])
        return labels_left

    def wait_for_appearance_enabled(self, element, time_out=20):
        self.poco(element, enabled=True).wait_for_appearance(timeout=time_out)

    def wait_for_appearance_disabled(self, element, time_out=20):
        self.poco(element, enabled=False).wait_for_appearance(timeout=time_out)

    def wait_for_appearance_disabled(self, element, time_out=20):
        self.poco(element, enabled=False).wait_for_appearance(timeout=time_out)

    def verify_design_manipulation_for_all_designs(self):
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            for name in curr:
                if name not in total:
                    self.poco(name).click()
                    self.verify_design_manipulation_options()
                    self.click_scrim()
                    total.append(name)
            if curr == prev:
                break
            self.poco.scroll()
            prev = curr

    def verify_design_manipulation_options(self):
        if self.poco("Print").exists():
            pass
        else:
            raise Exception("Print option not present")
        if self.poco("Rename").exists():
            pass
        else:
            raise Exception("Rename option not present")
        if self.poco("Duplicate").exists():
            pass
        else:
            raise Exception("Duplicate option not present")
        if self.poco("Delete").exists():
            pass
        else:
            raise Exception("Delete option not present")

    def verify_design_manipulation_options_in_design_menu(self):
        try:
            self.verify_design_manipulation_options()
        except:
            raise Exception("Design manipulation options \"Print, Rename, Duplicate, Delete\" not present.")

    def check_design_menu_closed(self):
        try:
            self.verify_design_manipulation_options()
            raise Exception("Design menu still open after clicking outside design menu.")
        except:
            pass

    def scroll_my_designs(self, direction="up"):
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            for name in curr:
                if name not in total:
                    total.append(name)
            if curr == prev:
                break
            scroll_view = self.poco("android.view.View")
            scroll_view.swipe(direction)
            scroll_view.swipe(direction)
            prev = curr

    def changeCopiesCount(self, new_copies_count):
        self.poco("Copies").parent().child("android.widget.EditText").click()
        self.poco("Copies").parent().child("android.widget.EditText").set_text(new_copies_count)

    def get_the_name_size_and_lastprint_of_design(self, design):
        a = design.split("\n")
        try:
            return a[0], a[1], a[2].split(":")[1].strip()
        except:
            return a[0], a[1], 0

    def checkIfDataSourceIsLinked(self):
        if self.poco("Choose an option").exists():
            raise Exception("Data Source not linked.")
        else:
            pass

    def closeNotification(self):
        touch(Template(Basic_path(r"close_notification.png"), record_pos=(0.415, -0.896), resolution=(1080, 2280)))

    def clickAccept(self):
        self.poco("Accept").click()

    def check_if_on_print_preview_page(self):
        return self.poco(nameMatches=".*Label.*").exists()

    def get_label_print_range(self):
        return self.poco("android.widget.ScrollView").child()[6].get_name()

    def get_first_row_first_column_value(self):
        return self.poco("android.widget.CheckBox")[3].parent().child()[1].get_name()

    def verify_only_selected_rows_displayed_in_label_range(self, number_of_selected_rows):
        print(self.poco("Print").parent().child()[-7].get_name())
        if self.poco("Print").parent().child()[-7].get_name() == "1-" + str(number_of_selected_rows):
            pass
        else:
            raise Exception("rows displayed on the label range field not matching with the selected number of rows")

    def verify_My_Designs_pagination(self):
        if self.poco("android.widget.ListView").exists():
            pass
        else:
            raise Exception("All templates did not show up with pagination")

    def verify_pagination_shown_is_correct(self):
        total_designs = int(self.poco(textMatches=".*Showing.*").get_text().split(" ")[3])
        number_of_pages = len(self.poco("android.widget.ListView").child()) - 2
        items_per_page = int(self.poco(textMatches=".*items.*").get_text().split(" ")[1])
        print(total_designs, number_of_pages, items_per_page)
        if items_per_page * number_of_pages >= total_designs > items_per_page * (number_of_pages - 1):
            pass
        else:
            raise Exception(
                "Number of pages not satisfying formula\n \"Items per page * Number of pages >= Total nuber of designs > Items per page * Number of pages -1\" ")

    def clickSave(self):
        try:
            self.poco("Save").click()
        except:
            self.poco(text="Save").click()

    def verifyErrorPopUp_forInvalidCopies(self):
        try:
            self.poco(nameMatches="(?s).*Error.*").wait_for_appearance(timeout=10)
            if self.poco(nameMatches="(?s).*Error.*").get_name().split("\n")[1] == "An Unknown Error has Occured.":
                pass
            else:
                error = f"Error shown as {self.poco(nameMatches="(?s).*Error.*").get_name().split("\n")[1]} instead of \"An Unknown Error has Occured.\"."
                raise Exception(error)

        except:
            raise Exception("No Error Pop Up.")

    def wait_for_element_appearance_type(self, element, time_out=15):
        self.poco(type=element).wait_for_appearance(timeout=time_out)

    def clickImport(self):
        self.poco(text="Import").wait_for_appearance(timeout=10)
        self.poco(text="Import").click()

    def get_all_icons_zebra_gallery(self):
        elements = set()
        previous = set()
        while 1:
            current = set()
            for child in self.poco("android.view.View").child(type="android.widget.ImageView"):
                current.add(child.get_name())
            if current == previous:
                break
            elements = elements.union(current)
            previous = current.copy()
            self.poco.scroll()
        scroll_view = self.poco("android.widget.ScrollView")
        if scroll_view.exists():
            while not self.poco(type="android.view.View", name="Alert").exists():
                scroll_view.swipe("down")
        return elements

    def search_Icons(self, icon_name):
        self.poco("android.widget.EditText").wait_for_appearance(timeout=15)
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(icon_name)

    def select_file_update_data_connections(self, filename):
        selected_file_name = self.poco(nameMatches=f"(?s).*{filename}.*").get_name().split("(")[0].strip()
        self.poco(nameMatches=f"(?s).*{filename}.*").click()
        try:
            self.poco(nameMatches="(?s).*could not be read.*").wait_for_appearance(timeout=10)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File could not be read pops up while trying to link google drive file.")
        except Exception as e:
            return selected_file_name

    def verify_update_data_connections_dialog(self):
        sleep(2)
        try:
            self.poco(
                nameMatches="The below data sources are missing for the .* label. They must be updated in order to print.")
        except:
            raise Exception(
                "\"The below data sources are missing for the label. They must be updated in order to print.\" dialog did not appear")

    def selectDesign(self, design_name):
        self.poco(name=design_name).click()

    def get_Labels_left_in_printer_info(self):
        printer_info = self.poco(nameMatches="(?s).*prints left.*").get_name()
        label_info = printer_info.split("\n")[4]
        return label_info

    def search_label_range(self):
        self.poco("android.widget.EditText").set_text("1.01")

    def getDesignInfo(self, design_name):
        return self.poco(nameMatches="(?s).*" + design_name + ".*").get_name()

    def changeAccInAddContacts(self, account):
        self.poco(textMatches=".*Google Account:.*").click()
        self.checkIfAccPresentGoogleContacts(account)
        self.poco(text=account).click()
        if self.poco(text="Close menu").exists():
            self.poco(text="Close menu").click()

    def generateRandomPhoneNumber(self):
        areaCode = random.randint(100, 999)
        prefix = random.randint(100, 999)
        lineNumber = random.randint(1000, 9999)
        return f"{areaCode}{prefix}{lineNumber}"

    def createContact(self, firstName, lastName):
        streets = ["Main St", "Oak St", "Elm St", "Maple Ave", "Cedar Ln", "High Street", "Market Square",
                   "Park Avenue", "Broadway", "Abbey Road"]
        po_boxes = ["PO Box 123", "PO Box 456", "PO Box 789", "PO Box 1011", "PO Box 1212"]
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "London", "Manchester", "Edinburgh",
                  "Toronto", "Sydney"]
        zip_codes = ["10001", "90001", "60601", "77001", "85001", "SW1A 1AA", "M1 1AB", "EH1 1AA", "M5V 2G9", "2000"]
        prefix = ["Mr", "Ms", "Mrs"]
        suffix = ["Sr", "Jr"]
        address = ["66", "1", "74"]
        department = ["IT", "Testing", "SDE", "SDE-1", "SDET", "Firmware Test", "Frontend", "App Dev", "Devops",
                      "Cloud Technician", "CloudDB"]

        self.poco(text="Add new contact").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Create a contact").click()
        sleep(3)
        keyevent("back")
        sleep(3)
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="First name").parent().child()[1].set_text(firstName.upper())
        self.poco(text="Show more").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        Prefix = random.choice(prefix)
        self.poco(text="Prefix").parent().parent().child()[1].set_text(Prefix)
        self.poco(text="Middle name").parent().parent().child()[1].set_text(firstName)
        try:
            self.poco(text="Last name").parent().parent().child()[1].set_text("1")
        except:
            self.poco(text="Surname").parent().parent().child()[1].set_text("1")
        Suffix = random.choice(suffix)
        self.poco(text="Suffix").parent().parent().child()[1].set_text(Suffix)
        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        nick_name = firstName.upper() + firstName
        self.poco(text="Nickname").parent().parent().child()[1].set_text(nick_name)
        self.poco(text="Company").parent().parent().child()[1].set_text("Zebra")
        self.poco(text="Job title").parent().parent().child()[1].set_text("SDE")
        self.poco(text="Show more").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        dept = random.choice(department)
        self.poco(text="Department").parent().parent().child()[1].set_text(dept)
        email = firstName + lastName + "@gmail.com"
        self.poco(text="Email")[0].parent().parent().child()[1].set_text(email)
        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Label").parent().parent().child()[1].set_text("work")
        phone_no = self.generateRandomPhoneNumber()
        self.poco(text="Phone")[0].parent().child()[1].set_text(phone_no)
        keyevent("back")
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("mobile")
        self.poco(text="Add phone").click()
        phone_no = self.generateRandomPhoneNumber()
        self.poco(text="Phone")[-1].parent().child()[1].set_text(phone_no)
        keyevent("back")
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("work")
        self.poco(text="Add phone").click()
        phone_no = self.generateRandomPhoneNumber()
        self.poco(text="Phone")[-1].parent().child()[1].set_text(phone_no)
        keyevent("back")
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("home")
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Add phone").click()
        phone_no = self.generateRandomPhoneNumber()
        self.poco(text="Phone")[-1].parent().child()[1].set_text(phone_no)
        keyevent("back")
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("main")
        self.poco(text="Add address").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        address1, address2, address3 = random.choices(address, k=3)
        self.poco(text="Street address").parent().parent().child()[1].click()
        self.poco(text="Street address").parent().child()[1].set_text(address1)
        keyevent("back")
        self.poco(textMatches=f".*{address1}.*")[-1].click()
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        # pincode1, pincode2, pincode3 = random.choices(zip_codes, k=3)
        # self.poco(text="Pincode").parent().parent().child()[1].set_text(pincode1)
        po_box1, po_box2, po_box3 = random.choices(po_boxes, k=3)
        try:
            self.poco(text="PO Box").parent().parent().child()[1].set_text(po_box1)
        except:
            self.poco(text="PO box").parent().parent().child()[1].set_text(po_box1)
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("home")

        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Add address").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Street address").parent().parent().child()[1].click()
        self.poco(text="Street address").parent().child()[1].set_text(address2)
        keyevent("back")
        self.poco(textMatches=f".*{address2}.*")[-1].click()
        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        # self.poco(text="Pincode").parent().parent().child()[1].set_text(pincode2)
        try:
            self.poco(text="PO Box").parent().parent().child()[1].set_text(po_box2)
        except:
            self.poco(text="PO box").parent().parent().child()[1].set_text(po_box2)
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("work")
        self.poco(text="Add address").click()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Street address").parent().parent().child()[1].click()
        self.poco(text="Street address").parent().child()[1].set_text(address3)
        keyevent("back")
        self.poco(textMatches=f".*{address3}.*")[-1].click()
        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        # self.poco(text="Pincode").parent().parent().child()[1].set_text(pincode3)
        try:
            self.poco(text="PO Box").parent().parent().child()[1].set_text(po_box3)
        except:
            self.poco(text="PO box").parent().parent().child()[1].set_text(po_box3)
        self.poco(text="Label")[-1].parent().parent().child()[1].set_text("other")
        self.poco("android.widget.Spinner")[-1].click()
        self.poco.swipe([0.9, 0.9], [0.9, 0.1])
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        choices = len(self.poco(text="July").parent().child()) // 2
        i = random.randint(0, choices)
        print(i, choices)
        self.poco(text="July").parent().child()[i].click()
        self.poco(text="Day").parent().parent().child()[1].set_text(random.randint(0, 29))
        self.poco(text="Year (optional)").parent().parent().child()[1].set_text(random.randint(1990, 2003))
        self.poco(text="Notes")[1].parent().parent().child()[1].set_text("Hi I am " + firstName + lastName)
        self.poco(text="Save").click()
        sleep(3)
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Contact details").wait_for_appearance(timeout=20)
        keyevent("back")

    def createContactOffice365(self, first_name, last_name):
        streets = ["Main St", "Oak St", "Elm St", "Maple Ave", "Cedar Ln", "High Street", "Market Square",
                   "Park Avenue", "Broadway", "Abbey Road"]
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "London", "Manchester", "Edinburgh",
                  "Toronto", "Sydney"]
        states = ["NY", "CA", "IL", "TX", "Ontario", "New South Wales", "Scotland", "Queensland"]
        zip_codes = ["10001", "90001", "60601", "77001", "85001", "SW1A 1AA", "M1 1AB", "EH1 1AA", "M5V 2G9", "2000"]
        countries = ["United States", "United Kingdom", "Canada", "Australia", "Germany", "France", "Japan", "India",
                     "Brazil", "Italy"]
        prefix = ["Mr", "Ms", "Mrs"]
        suffix = ["Sr", "Jr"]

        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        pin_code = random.choice(zip_codes)
        country = random.choice(countries)
        Prefix = random.choice(prefix)
        Suffix = random.choice(suffix)
        nick_name = first_name.upper() + first_name
        email = first_name + last_name + "@gmail.com"
        phone_no = self.generateRandomPhoneNumber()
        self.poco(text="Create new contact").click()
        self.poco(text="Add name")[1].click()
        self.poco("android.widget.EditText")[0].set_text(Prefix)
        self.poco("android.widget.EditText")[1].set_text(first_name.upper())
        self.poco("android.widget.EditText")[2].set_text(first_name)
        self.poco("android.widget.EditText")[3].set_text(last_name)
        self.poco("android.widget.EditText")[4].set_text(Suffix)
        self.poco("android.widget.EditText")[5].set_text(nick_name)
        self.poco(text="Back").click()
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        sleep(2)
        self.poco(text="Contact")[0].parent().child()[1].child()[1].child().set_text(email)
        self.poco(text="Contact")[0].parent().child()[2].child()[1].child().set_text(phone_no)
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        self.poco(text="Work")[0].parent().child()[1].child()[1].child().set_text("Zebra")
        self.poco.scroll()
        keyevent('adb shell input keyevent 26')
        wake()
        self.poco("android.widget.Spinner").click()
        self.poco(text="SET").click()
        self.poco("android.widget.EditText")[-1].set_text("Hi I am " + first_name + last_name)
        self.poco(text="Add address").click()
        self.poco(text="Business address")[0].parent().child()[1].child()[1].child().set_text(street)
        self.poco(text="Business address")[0].parent().child()[2].child()[1].child().set_text(city)
        self.poco(text="Business address")[0].parent().child()[3].child()[1].child().set_text(state)
        self.poco(text="Business address")[0].parent().child()[4].child()[1].child().set_text(pin_code)
        self.poco(text="Business address")[0].parent().child()[5].child()[1].child().set_text(country)
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        pin_code = random.choice(zip_codes)
        country = random.choice(countries)
        self.poco(text="Home address")[0].parent().child()[1].child()[1].child().set_text(street)
        self.poco(text="Home address")[0].parent().child()[2].child()[1].child().set_text(city)
        self.poco(text="Home address")[0].parent().child()[3].child()[1].child().set_text(state)
        self.poco(text="Home address")[0].parent().child()[4].child()[1].child().set_text(pin_code)
        self.poco(text="Home address")[0].parent().child()[5].child()[1].child().set_text(country)
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        pin_code = random.choice(zip_codes)
        country = random.choice(countries)
        self.poco(text="Other address")[0].parent().child()[1].child()[1].child().set_text(street)
        self.poco(text="Other address")[0].parent().child()[2].child()[1].child().set_text(city)
        self.poco(text="Other address")[0].parent().child()[3].child()[1].child().set_text(state)
        self.poco(text="Other address")[0].parent().child()[4].child()[1].child().set_text(pin_code)
        self.poco(text="Other address")[0].parent().child()[5].child()[1].child().set_text(country)
        self.poco.swipe([0.5, 0.9], [0.5, 0.5])
        keyevent('adb shell input keyevent 26')
        wake()
        self.poco(text="Back").click()
        self.poco(text="Save contact").click()

    def deleteOffice365Contact(self):
        self.poco("android.widget.Button")[-5].click()
        self.poco.scroll()
        self.poco(text="Delete contact").click()

    def deleteContactGoogleContacts(self):
        keyevent('adb shell input keyevent 26')
        wake()
        self.poco("android.widget.CheckBox").click()
        self.poco(text="List settings").click()
        keyevent('adb shell input keyevent 26')
        wake()
        self.poco(text="Delete").click()
        keyevent('adb shell input keyevent 26')
        wake()
        try:
            self.poco(text="Move to trash").click()
        except:
            self.poco(text="Move to the bin").click()

    def clickGotIt(self):
        if self.poco(text="Got It").exists():
            self.poco(text="Got It").click()
        if self.poco(text="Welcome to your new ZSB Series Printer").exists():
            self.poco(text="Welcome to your new ZSB Series Printer").parent().child()[0].click()

    def selectRoundLabelInCreate(self):
        self.poco(text="Round").click()

    def checkDisplayedCountMatchesExpected(self, expected_count):
        count_displayed = self.get_showing_n_designs_number()
        print("cc", count_displayed)
        if count_displayed == expected_count:
            pass
        else:
            # error = f"Displayed count({count_displayed}) does not match expected count({expected_count})"
            raise Exception("Design not loaded properly.")
