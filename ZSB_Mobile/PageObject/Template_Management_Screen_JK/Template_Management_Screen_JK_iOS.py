import datetime
import time
import random
import string
import fnmatch

from airtest.core.api import *
import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen

import subprocess

common_method = Common_Method(poco)


class Template_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco

    def checkIfAccPresent(self, account):
        while True:
            accounts_len = len(self.poco("Sign in – Google accounts").child()[6].child())
            for i in range(accounts_len):
                account_displayed = self.poco("Sign in – Google accounts").child()[6].child()[i].child().child()[
                    -1].get_name()
                if account_displayed == account:
                    return True
                elif account == "Use another account":
                    return False

    """ios"""

    def choose_file_update_data_connections(self, filename):
        parent = self.poco("Upload File").parent()
        for child in parent.child():
            if child.get_name() == filename:
                child.click()
                return
        raise Exception("Did not find file")

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

    def wait_for_element_appearance_name_matches_all(self, element, time_out=20):
        self.poco(nameMatches="(?s).*" + element + ".*").wait_for_appearance(timeout=time_out)

    """ios"""

    def selectChooseAnOption(self, option_count=1, option_name=None, click=True):
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
                    self.poco("ScrollView").parent().child()[option_count - i].click()
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
        scroll_view = self.poco("ScrollView")
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

    def click_scrim(self):
        self.poco("Scrim").click()

    def get_remaining_label_count(self):
        labels_left = int(self.poco(nameMatches=".*Printer.*").get_name().split(" ")[1][1:])
        return labels_left

    def wait_for_appearance_enabled(self, element, time_out=20):
        self.poco(element, enabled=True).wait_for_appearance(timeout=time_out)

    def verify_only_selected_rows_displayed_in_label_range(self, number_of_selected_rows):
        print(self.poco("Print").parent().child()[-7].get_name())
        if self.poco("Print").parent().child()[-7].get_name() == "1-" + str(number_of_selected_rows):
            pass
        else:
            raise Exception("rows displayed on the label range field not matching with the selected number of rows")

    def clickGotIt(self):
        self.poco("Got It").click()
        if self.poco("Welcome to your new ZSB Series Printer").exists():
            self.poco("Button").click()

    def clickDeleteDesign(self):
        self.poco("Delete").click()
