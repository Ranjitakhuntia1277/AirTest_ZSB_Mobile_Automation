import datetime
import time
import random
import string

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class Template_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Search_place_holder = Template(r"searchPlaceHolder.png", record_pos=(-0.192, -0.609),
                                            resolution=(1080, 2280))
        self.Search_icon = Template(r"search_Icon.png", record_pos=(-0.398, -0.605), resolution=(1080, 2280))

    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        common_method.run_the_command(cmd)

    def get_showing_n_designs_number(self):
        a = self.poco(nameMatches=".*Showing.*").get_name()
        a = a.split(" ")
        return a[1]

    def turn_off_wifi(self):
        command = "adb shell svc wifi disable"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)

    def verify_default_sort_my_designs(self):
        return self.poco("Name (A to Z)").exists()

    def click_sort_my_designs(self):
        self.poco("android.view.View")[4].child()[4].click()

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
        return self.poco("All sizes").exists()

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
            self.poco("android.view.View")[4].child()[3].click()

    def click_sort_common_designs(self):
        self.poco("android.view.View")[5].child()[3].click()

    def click_filter_common_designs(self):
        self.poco("android.view.View")[5].child()[2].click()

    def verify_connection_error_app(self):
        return self.poco("An error occurred when loading your designs. Please tap to try again").exists()

    def wait_for_appearance_designs_in_a_particular_category(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=10)

    def get_all_designs_in_my_designs(self, name=False):
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

            self.poco.scroll()
            prev = curr

        return total

    def get_all_designs_size_in_my_designs(self):
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

            self.poco.scroll()
            prev = curr
        for i in total:
            label_sizes.add(i.split("\n")[1])
        return label_sizes

    def filter_options(self, length=False):

        filter_option_list = []
        if length:
            return len(self.poco("android.view.View")[6].child())
        else:
            for i in range(1, len(self.poco("android.view.View")[6].child())):
                filter_option_list.append(self.poco("android.view.View")[6].child()[i].get_name())
            return filter_option_list

    def verify_design_names_follow_order(self, design_names):
        start_with_special_character = False
        start_with_number = False
        start_with_alphabet = False
        for name in design_names:
            if name[0].isalpha():
                if not start_with_number and not start_with_special_character:
                    print(name)
                    raise Exception(
                        "Design name starting with alphabets found before design names starting with number and special characters... ")
                start_with_alphabet = True
            elif name[0].isdigit():
                if start_with_alphabet:
                    print(name)
                    raise Exception(
                        "Design name starting with number found after design names starting with alphabets... ")
                start_with_number = True
            else:
                if start_with_number or start_with_alphabet:
                    print(name)
                    raise Exception(
                        "Design name starting with special characters found after design names starting with number or alphabets...")
                start_with_special_character = True

    def check_design_count_title(self, length):
        return self.poco(f"Showing {length} Designs").exists()

    def clickCommonDesigns(self):
        self.poco("Common Designs").click()

    def search_design_common_designs(self, design_name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(design_name)

    def select_design_common_designs(self):
        self.poco("android.view.View")[7].child()[1].child().click()

    def select_design_common_designs_Web(self):
        if self.poco("android.widget.Image")[1].exists():
            self.poco("android.widget.Image")[1].click()

    def select_label_common_designs_Web(self):
        if self.poco("android.widget.Image")[2].exists():
            self.poco("android.widget.Image")[2].click()

    def get_name_of_selected_design(self):
        design_name = self.poco("android.widget.TextView").get_text()
        return design_name

    def click_copy_to_My_Designs(self):
        self.poco(text="Copy to My Designs").click()

    def get_first_design_name_my_designs(self):
        return self.poco("android.view.View")[8].child().child().get_name().split("\n")[0]

    def check_for_suggestion_drop_down_in_search_designs(self):
        a = self.poco(nameMatches="(?s).*result.*")[0].exists()
        return a

    def check_dropdown_options_Are_clickable(self):
        drop_down_result_1 = self.poco("android.view.View")[3].child().get_name()
        return self.poco(name=drop_down_result_1, enabled=True).exists()

    def click_drop_down_result_1(self, returnName):
        return_value = self.poco(nameMatches="(?s).*result.*").get_name().split("\n")[0]
        self.poco(nameMatches="(?s).*result.*").click()
        if returnName:
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
        self.poco(nameMatches="(Ws).*result.*").wait_for_appearance(timeout=10)

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

    def clickAddText(self):
        self.poco(text="Add text").click()

    def placeText(self):
        touch(Template(r"tpl1708429167702.png", record_pos=(-0.109, 0.382), resolution=(1080, 2340)))

    def checkManualInput_checkbox(self):
        if self.poco("android.widget.CheckBox", checked=True):
            pass
        else:
            self.poco("android.widget.CheckBox").click()

    def verify_print_preview(self, preview_name):
        assert_exists(Template(rf"{preview_name}.png", record_pos=(-0.001, -0.045), resolution=(1080, 2340)),
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

    def verify_duplicate_previous_next_button(self):
        if self.poco("Previous")[1].exists():
            return True
        if self.poco("Next")[1].exists():
            return True
        return False

    def select_second_colum_from_data_file(self):
        self.poco("android.widget.TextView")[7].focus([0.1, 0.5]).click()
        self.poco("android.widget.TextView")[9].focus([0.1, 0.5]).click()

    def unpair_bluetooth_device(self, device_name):
        while not self.poco(text="AVAILABLE DEVICES"):
            if self.poco(text=device_name).exists():
                connected_device = len(self.poco("com.android.settings:id/recycler_view").child())
                for i in range(connected_device):
                    curr_device = self.poco("android:id/title")[i].get_text()
                    print(self.poco("android:id/title")[i].get_text())

                    if curr_device == device_name:
                        if self.poco("com.android.settings:id/preference_detail")[i].exists():
                            self.poco("com.android.settings:id/preference_detail")[i].click()
                        if self.poco("com.android.settings:id/settings_button")[i].exists():
                            self.poco("com.android.settings:id/settings_button")[i].click()
                break
            self.poco.scroll()
        if self.poco(text="Unpair").exists():
            self.poco(text="Unpair").click()
        if self.poco(text="Forget").exists():
            self.poco(text="Forget").click()

    def selectChooseAnOption(self, option_count=1, option_name=None):
        for i in range(1, option_count + 1):
            self.poco("Choose an option").click()
            if option_name is None:
                self.poco("android.view.View")[6].child()[option_count - i].click()
            else:
                self.poco(option_name).click()

    def verify_label_range_is_All(self):
        if self.poco("All").exists():
            return
        raise Exception("Label Range is not 'All'")

    def verify_label_navigation(self):
        initial = self.poco(nameMatches="Label.*").get_name()
        self.poco("Next").click()
        navigated_next = self.poco(nameMatches="Label.*").get_name()
        self.poco("Previous").click()
        navigated_previous = self.poco(nameMatches="Label.*").get_name()
        if navigated_next != initial:
            if navigated_previous == initial:
                return
        raise Exception("'Previous' and 'Next' navigation buttons are not functioning.")

    def check_total_label_for_print_count(self, n):
        return self.poco(f"Total of {n} labels").exists()

    def choose_label_print_range(self):
        self.poco("All").click()

    def select_All(self, check=True):
        checked_value = common_method.getAttr(self.poco("android.widget.CheckBox"), "checked")
        if checked_value:
            if not check:
                self.poco("android.widget.CheckBox").click()
        else:
            if check:
                self.poco("android.widget.CheckBox").click()

    def rename_Design(self):
        self.poco("Rename").click()

    def clickDuplicateDesign(self):
        self.poco("Duplicate").click()
        self.poco("Save").wait_for_appearance(timeout=10)
        self.poco("Save").click()

    def clickDeleteDesign(self):
        self.poco("Delete").click()

    def verifyLabelsShown(self):
        return self.poco("android.view.View").child(type="android.widget.ImageView").exists()

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

    def get_drop_down_list_common_designs(self, category=False):
        prev = []
        curr = []
        temp = []
        flag = 1
        while flag:
            curr = [child.get_name() for child in self.poco("android.view.View")[4].child()]
            if curr == prev:
                break
            for i in curr:
                if i not in temp:
                    if category:
                        if "DESIGNS" in i:
                            flag = 0
                            break
                    temp.append(i)
            prev = curr
            self.poco.swipe([0.5, 0.5], [0.5, 0.2])
        return temp

    def get_all_categories_in_common_designs(self, name=False):
        temp = []
        prev = []
        self.poco(nameMatches="(?s).*For use with Label Cartridges: .*")
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

    def click_scrim(self):
        self.poco("Scrim").click()

    def verifySearchResults_n(self, n):
        return self.poco(f"Search results ({n})").exists()

    def verifyNoResultsDropDown(self):
        return self.poco(nameMatches="(?s).*No results found..*").exists()

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

    def fill_all_print_fields(self):
        elements = []
        previous = []
        while 1:
            current = []
            for child in self.poco("android.widget.ScrollView").child("android.view.View").child():
                current.append(child.get_text())
            if current == previous:
                break
            for field in current:
                if field not in elements:
                    random_word = data_sources_page.generateRandomWord(8)
                    self.poco(text=field).click()
                    self.poco(text=field).set_text(random_word)
                    keyevent("back")
                    elements.append(random_word)
            previous = current

    def get_remaining_label_count(self):
        labels_left = int(self.poco(nameMatches=".*Printer.*").get_name().split(" ")[1][1:])
        return labels_left

    def wait_for_appearance_enabled(self, element):
        self.poco(element, enabled=True).wait_for_appearance(timeout=20)

    def wait_for_appearance_disabled(self, element):
        self.poco(element, enabled=False).wait_for_appearance(timeout=20)

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
        self.poco("android.widget.ScrollView").child("android.widget.EditText").click()
        self.poco("android.widget.ScrollView").child("android.widget.EditText").set_text(new_copies_count)
