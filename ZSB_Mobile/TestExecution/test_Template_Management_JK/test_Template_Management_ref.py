from platform import platform
import datetime
import re
import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import device as current_device
import os
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen_Android
import subprocess


def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",a)

common_method = Common_Method(poco)

class Template_Management_Android:
    pass

    def __init__(self,poco):
        self.poco = poco
        self.my_designs_button = "My Designs"
        self.print_button = "Print"
        self.delete_button = "Delete"
        self.home_button = "Home"
        self.common_designs_button = "Common Designs"
        self.copy_to_my_designs = "Copy to My Designs"
        self.search_icon = Template(Basic_path(r"tpl1708320351770.png"), record_pos=(-0.408, -0.55), resolution=(720, 1280))


    def click_my_designs_button(self):
        self.poco(self.my_designs_button).click()

    def click_home_button(self):
        self.poco(self.home_button).click()

    def click_first_design_in_my_designs(self):
        self.poco("android.view.View").child(type="android.widget.ImageView")[0].click()

    def click_first_design_in_common_design(self):
        self.poco("android.view.View").child(type="android.widget.ImageView")[0].click()

    def click_design_in_my_designs_by_full_name(self,design):

        try:
            self.poco(design).click()
        except:
            self.poco.scroll()
            self.poco(design).click()

    def select_design_in_my_design_by_name_and_return(self,name,click=1):
        total = self.get_all_designs_in_my_designs()
        temp={}

        for i in range(len(total)):
            a = total[i].split("\n")
            temp[a[0]] = total[i]

        while(not self.poco(temp[name]).exists()):
            self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)

        if click:
            try:
                self.click_design_in_my_designs_by_full_name(temp[name])
            except:
                self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)
                self.click_design_in_my_designs_by_full_name(temp[name])

        return temp[name]

    def get_the_full_name_of_design_and_click_in_my_design(self,name,click=1):

        escaped_name = re.escape(name)
        regex_pattern = "(?s).*"+escaped_name+".*"

        temp = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            a = self.poco(nameMatches=regex_pattern).exists()
            if a:
                p = self.poco(nameMatches=regex_pattern).get_name()
                temp.append(p)
                break
            if curr == prev:
                break
            prev = curr
            self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)

        if len(temp) == 0:
            prev = []
            while 1:
                curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
                a = self.poco(nameMatches=regex_pattern).exists()
                if a:
                    p = self.poco(nameMatches=regex_pattern).get_name()
                    temp.append(p)
                    break
                if curr == prev:
                    break
                prev = curr
                self.poco.swipe([0.5, 0.9], [0.5, 0.4], duration=0.5)
        print(temp)
        if click:
            self.poco(temp[0]).click()

        return temp[0]

    def get_the_full_name_of_design_and_click_in_recently_printed_design(self,name,click=1):

        escaped_name = re.escape(name)
        regex_pattern = "(?s).*" + escaped_name + ".*"
        temp = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]

            a = self.poco(nameMatches=regex_pattern).exists()
            if a:
                p = self.poco(nameMatches=regex_pattern).get_name()
                temp.append(p)
                break

            if self.poco(nameMatches=".*Recently.*").exists():
                break
            self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)

        if len(temp) == 0:
            prev = []
            while 1:
                curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]

                a = self.poco(nameMatches=regex_pattern).exists()
                if a:
                    p = self.poco(nameMatches=regex_pattern).get_name()
                    temp.append(p)
                    break

                if curr == prev:
                    break
                prev = curr
                self.poco.scroll()

        if click:
            self.poco(temp[0]).click()

        return temp[0]


    def select_design_in_recetly_printed_design_by_name_and_return(self,name,click=1):
        total = self.get_all_designs_in_recently_printed_labels()
        temp={}

        for i in range(len(total)):
            a = total[i].split("\n")
            temp[a[0]] = total[i]

        while(not self.poco(temp[name]).exists()):
            self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)

        if click:
            try:
                self.click_design_in_my_designs_by_full_name(temp[name])
            except:
                self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)
                self.click_design_in_my_designs_by_full_name(temp[name])

        return temp[name]


    def check_element_exists(self,element,order=0):
        try:
            a=self.poco(element)[order].exists()
            return a
        except:
            a = self.poco(text=element)[order].exists()
            return a

    def click_element_by_name_or_text(self,element,order=0):
        try:
            self.poco(element)[order].click()
        except:
            self.poco(text=element)[order].click()

    def get_the_date_from_print_page(self):
        a = self.poco("android.widget.EditText")[0].parent().child("android.view.View").get_text()
        return a

    def set_new_date_in_print_page(self,date):
        date=str(date)
        self.poco("android.widget.EditText")[0].parent().child("android.view.View").click()
        self.poco(nameMatches=".*" +date+ ".*").click()
        self.poco("OK").click()

    def click_on_image_input_in_print_page(self):
        self.poco("Picture\nicon\nChoose an option")[0].click()

    def wait_for_image_upload_in_print_page(self):
        common_method.wait_for_element_disappearance("Picture\nicon\nChoose an option")

    def upload_image_in_print_page(self):
        self.poco("Upload").click()
        self.poco(text="Camera").click()

        self.poco(nameMatches=".*Photo.*")[0].click()


    def get_text_from_element(self,element,order):
        try:
            a = self.poco(element)[order].get_text()
            return a
        except:
            a = self.poco(text=element)[order].get_text()
            return a



    def check_element_exists_name_or_text_matches(self,element,order=0):
        try:
            a=self.poco(nameMatches=".*"+element+".*")[order].exists
            return a
        except:
            a = self.poco(textMatches=".*"+element+".*")[order].exists
            return a

    def check_print_button_clickable(self):
        return self.poco("Print",enabled=True)

    def get_first_design_in_my_designs(self):
        a = self.poco("android.view.View").child(type="android.widget.ImageView")[0].get_name()
        return a

    def get_no_of_copies(self):
        try:
            return self.poco("Copies").parent().child("android.widget.EditText").get_text()
        except:
            self.poco.scroll()
            self.poco("Copies").parent().child("android.widget.EditText").get_text()

    def click_on_copies(self):
        try:
            self.poco("Copies").parent().child("android.widget.EditText").click()
        except:
            self.poco.scroll()
            self.poco("Copies").parent().child("android.widget.EditText").click()
    def enter_no_of_copies(self,no):
        try:
            self.poco("Copies").parent().child("android.widget.EditText").set_text(no)
        except:
            self.poco.scroll()
            self.poco("Copies").parent().child("android.widget.EditText").set_text(no)

    def check_copies_focused(self):
        return self.poco("Copies").parent().child(name="android.widget.EditText",focused=True).exists()

    def click_print_button(self):
        self.poco(self.print_button).click()

    def click_print_button_enabled(self):
        try:
            self.poco(name=self.print_button,enabled=True).click()
        except:
            self.poco.scroll()
            self.poco(name=self.print_button, enabled=True).click()

    def wait_for_designs_in_comm_design(self):
        self.poco("android.view.View").child(type="android.widget.ImageView").wait_for_appearance(timeout=30)

    def get_all_designs_in_my_designs(self):
        total = []
        prev = []
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

        return total

    def click_first_design_in_recently_printed_labels(self):
        self.poco("android.view.View").child(type="android.widget.ImageView")[1].click()


    def get_first_design_in_recently_printed_labels(self):
        a = self.poco("android.view.View").child(type="android.widget.ImageView")[1].get_name()
        return a

    def get_all_designs_in_recently_printed_labels(self,index=6):
        arr = self.get_all_designs_in_my_designs()
        return arr[-index:]

    def delete_last_design_in_my_design(self):
        self.poco.scroll()
        self.poco("android.view.View").child(type="android.widget.ImageView")[-1].click()
        self.poco(self.delete_button).click()
        self.poco(self.delete_button).click()

    def click_left_arrow(self):
        self.poco("android.widget.Button").click()

    def get_current_date(self):
        current_date = datetime.datetime.now()

        # Extract current year, month, and day
        current_year = current_date.year
        current_month = current_date.strftime("%B")  # %B gives the full month name
        current_day = current_date.day

        return current_month[:3],current_day,current_year

    def get_current_date_in_mm_dd_yy_format(self):
        current_date = datetime.datetime.now()

        # Format date as "mm/dd/yyyy" without leading zeros for month and day
        formatted_date = current_date.strftime("%#m/%#d/%Y")

        return formatted_date

    def get_printer_date_in_google(self):
        a = self.poco(textMatches=".*Last print:.*")[0].get_text()
        temp = a.split(" ")
        print(temp[-1])
        return temp[-1]

    def get_design_last_print_date(self,design):
        a = design.split("Last print:")
        temp = a[-1]
        temp = temp.replace(",", "")
        temp = temp.split(" ")

        return temp[1],int(temp[2]),int(temp[3])

    def verify_print_notification(self):
        a = self.poco(nameMatches=".*Print complete.*").exists()

        return a

    def get_no_of_left_cartridge(self):
        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
                           "android.view.View").child("android.view.View").child("android.view.View").offspring(
                           "android.widget.ScrollView").child("android.view.View")[0].child("android.view.View").child(
                           "android.view.View")[0].children()]

        modified_list = [item.split('\n') for item in child_names]
        modified_list = modified_list[0][4].split(" ")

        return int(modified_list[0])

    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        common_method.run_the_command(cmd)

    def turn_off_wifi(self):
        command = "adb shell svc wifi disable"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)

    def get_no_of_labels_left_in_print_page(self):
        try:
            a = self.poco(nameMatches=".*labels left.*").get_name()
            print(a)

            temp = a.split("(")
            temp = temp[1].split(" ")
            print(temp[0])
            return temp[0]
        except:
            self.poco.scroll()
            a = self.poco(nameMatches=".*labels left.*").get_name()
            print(a)

            temp = a.split("(")
            temp = temp[1].split(" ")
            print(temp[0])
            return temp[0]

    def duplicate_the_design_and_get_the_name(self):
        self.poco("Duplicate").click()

        a = self.poco("android.widget.EditText").get_text()

        self.poco("Save").click()

        return a

    def click_the_duplicate_button(self):
        self.poco("Duplicate").click()

    def get_the_default_duplicate_name(self):
        a = self.poco("android.widget.EditText").get_text()
        return a

    def enter_name_in_duplicate_designs(self,name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(name)

    def check_for_invalid_character_error_in_duplicate_design(self):
        a = self.poco("These characters are not valid.").exists()
        return a
    def click_common_designs_button(self):
        self.poco(self.common_designs_button).click()

    def click_namematches_element(self,element):
        try:
            self.poco(nameMatches=".*"+element+".*").click()
        except:
            self.poco.scroll()
            self.poco(nameMatches=".*" + element + ".*").click()

    def search_designs(self, str,enter=1):
        design = self.poco("android.widget.EditText")
        design.click()
        design.set_text(str)
        if enter:
            keyevent("enter")

    def select_first_design(self):
        first_design = self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
            "android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View")[1].child("android.view.View").child("android.view.View")[0]
        first_design.click()

    def click_on_copy_to_my_designs(self):
        self.poco(self.copy_to_my_designs).click()

    def get_name_of_first_categories(self):
        a = self.poco("android.view.View").child(type="android.widget.ImageView")[0].get_name()
        temp = a.split("\n")
        print(temp[0])
        return temp[0]

    def verify_element_exists_by_name(self,elem):
        a = self.poco(elem).exists()
        return a

    def verify_options_clickable_in_design(self):
        a = self.poco("Print", enabled=True).exists()

        b = self.poco("Rename", enabled=True).exists()

        c = self.poco("Duplicate", enabled=True).exists()

        d = self.poco("Delete", enabled=True).exists()

        return a and b and c and d

    def click_and_close_menu_designs_in_home(self,arr):

        for i in arr:
            try:
                self.poco(i).click()
                self.poco("Scrim").click()
            except:
                self.poco.scroll()
                self.poco(i).click()
                self.poco("Scrim").click()

    def close_menu_of_design_in_home(self):
        self.poco("Scrim").click()

    def check_the_dates_of_last_print_in_recent_print_labels(self,arr):

        curr_mon,curr_date,curr_year = self.get_current_date()

        for i in arr:
            des_mon, des_date, des_year = self.get_design_last_print_date(i)

            if curr_mon!=des_mon or curr_date!=des_date or curr_year!=des_year:
                raise Exception("dates not matching")

    def get_names_and_sizes_in_recently_printed_labels(self,arr):

        names = []
        sizes = []
        for i in arr:
            temp = i.split("\n")
            names.append(temp[0])
            sizes.append(temp[1])

        return names, sizes

    def click_on_design_which_is_not_printed_yet(self,total):
        for i in total[::-1]:
            if "Last Print" not in i:

                try:
                    self.poco(i).click()

                except:
                    self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)
                    self.poco(i).click()
                break
            else:
                continue

    def refresh_the_home_page_till_you_see_error(self):

        while not self.poco("Continue").exists():
            self.poco.swipe([0.5,0.5], [0.5,1.0], duration=0.5)

    def refresh_the_home_page_(self):
        self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)
        self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)
        self.poco.swipe([0.5, 0.5], [0.5, 1.0], duration=0.5)

    def check_the_error_msg_of_turning_off_wifi(self):
        a = self.poco("Continue").parent().get_name()
        temp = a.split("\n")
        assert_equal(temp[1],"The service is currently unavailable.","ok")

    def click_on_continue(self):
        try:
            self.poco("CONTINUE").click()
        except:
            try:
                self.poco(text="Continue").click()
            except:
                self.poco("Continue").click()

    def input_text_in_element_by_name(self,element,text,order=0):
        self.poco(element)[order].set_text(text)

    def check_prompt_for_smaller_label_than_current(self):
        a = self.poco("Label Is Different Size Than Cartridge").exists()

        b = self.poco(
            "Resize the label or insert a different cartridge into the printer.  Otherwise, the label output may not be as expected.").exists()

        return a and b

    def enter_the_special_characters_in_print_page(self,text):
        self.poco("android.widget.EditText")[0].set_text(text)

    def click_on_rename_button(self):
        self.poco("Rename").click()

    def get_the_default_rename_text(self):
        a = self.poco("android.widget.EditText").get_text()
        return a

    def check_cancel_button_clickable_in_rename_popup(self):
        a = self.poco(name="Cancel", enabled=True).exists()
        print(a)
        return a

    def click_on_cancel_button_in_rename_popup(self):
        self.poco(name="Cancel", enabled=True).click()

    def check_save_button_clickable_in_rename_popup(self):
        a = self.poco(name="Save", enabled=True).exists()
        print(a)
        return a

    def check_error_for_invalid_characters_in_rename_design(self):
        a = self.poco("These characters are not valid.").exists()
        return a

    def click_on_save_button_in_rename_design(self):
        self.poco("Save").click()

    def click_on_save_button(self):
        try:
            self.poco("Save").click()
        except:
            self.poco(text="Save").click()

    def check_for_the_popup_for_rename_design_after_save(self):
        common_method.wait_for_element_appearance_namematches("Design has been successfully rename",15)

    def get_the_size_and_lastprint_of_design(self,design):
        a = design.split("\n")
        try:
            return a[1], a[2]
        except:
            return a[1],0

    def enter_text_in_rename_design(self,text):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(text)

    def check_error_for_blank_value_in_rename_design(self):
        return self.poco("Name must be at least 1 character long").exists()

    def check_search_icon(self):
        try:
            assert_exists(self.search_icon)
        except:
            raise Exception("search icon not found")

    def check_search_designs_text(self):
        try:
            temp = Template(Basic_path(r"tpl1708320370860.png"), record_pos=(-0.228, -0.55), resolution=(720, 1280))
            assert_exists(temp)
        except:
            raise Exception("search design text not found")

    def click_on_search_design(self):
        self.poco("android.widget.EditText").click()

    def check_for_suggestion_drop_down_in_search_designs(self):
        a = self.poco(nameMatches="(?s).*result.*")[0].exists()
        return a

    def wait_for_suggestions_to_appear(self):
        self.poco(nameMatches="(?s).*result.*").wait_for_appearance(timeout=10)

    def check_text_for_wrong_design_name(self):
        a = self.poco("No results found.\nSearch tips: try typing exactly what you’re looking for. It may help to simply type 1 word, and search for results then.").exists()
        return a

    def get_showing_n_designs_number(self):
        a=self.poco(nameMatches=".*Showing.*").get_name()
        a=a.split(" ")
        return a[1]

    def get_all_search_results_in_search_designs(self):
        a = len(self.poco(nameMatches="(?s).*result.*"))
        temp=[]
        if a<5:
            for i in range(a):
                temp.append(self.poco(nameMatches="(?s).*result.*")[i].get_name())
        else:

            total = []
            prev = []
            while 1:
                curr = [child.get_name() for child in
                        self.poco(nameMatches="(?s).*result.*")]
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

    def get_names_of_design_in_search_designs(self,arr):
        temp=[]
        for i in arr:
            a=i.split("\n")
            temp.append(a[0])
        return temp

    def verify_duplicate_design_window(self):
        t1=Template(Basic_path(r"tpl1708428872115.png"), record_pos=(-0.106, -0.289), resolution=(1080, 2340))
        t2=Template(Basic_path(r"tpl1708428886221.png"), record_pos=(-0.007, -0.158), resolution=(1080, 2340))
        try:
            assert_exists(t1)
            try:
                assert_exists(t2)
            except:
                pass
        except:
            raise Exception("duplicate_design_window is not displayed properly")


