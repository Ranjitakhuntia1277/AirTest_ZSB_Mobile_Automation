import os
import re
import subprocess
import time
import datetime
import random
import string
import fnmatch

from airtest.core.api import *
import pytest
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess

common_method = Common_Method(poco)
data_sources_page = Data_Sources_Screen(poco)


class SSO_Token_Renewal_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.deleteAccount = "Delete Account"
        self.logOut = "Log Out"
        self.delete = "Delete"
        self.first_name = "new_first_name"
        self.last_name = "new_last_name"

    def fetch_lines_between_words(self, file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt", start_word='exchangeCode:body:', end_word='3599'):
        with open(file_path, 'r') as file:
            file_content = file.read()
            start_index = [match.start() for match in re.finditer(start_word, file_content)]
            end_index = [match.start() for match in re.finditer(end_word, file_content)]

            valid_start_index = -1
            valid_end_index = -1
            for recent_start_index in reversed(start_index):
                for recent_end_index in end_index:
                    if recent_end_index > recent_start_index:
                        valid_start_index = recent_start_index
                        valid_end_index = recent_end_index
                        break
                if valid_start_index != -1:
                    break
            if valid_start_index != -1 and valid_end_index != -1:
                end_line = file_content.find("\n", valid_end_index)
                if end_line == -1:
                    end_line = len(file_content)
                else:
                    end_line += 1
                result = file_content[valid_start_index:end_line]
                return result
            else:
                error = f"No valid {start_word} and {end_word} found in the correct order."
                raise Exception(error)

    def wildcard_search(self, wildcard="exchangeCode", file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt"):
        if wildcard == "exchangeCode":
            wildcard_query = '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*"expires_in":"3599"'
        elif wildcard == "getLocalTokens":
            wildcard_query = '.*flutter: getLocalTokens: access_token:.*'
        with open(file_path, 'r') as file:
            file_content = file.read()
            if re.search(wildcard_query, file_content, re.DOTALL):
                return True
        return False

    def check_if_exchangeCode_message_present(self):
        if self.wildcard_search("exchangeCode"):
            pass
        else:
            raise Exception("There is no message about \"exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}\" in the adb log.")

    def check_if_getLocalTokens_information_present(self):
        if self.wildcard_search("getLocalTokens"):
            pass
        else:
            raise Exception("There is a token information about \" : flutter: getLocalTokens : access_token: \" in the adb log.")

    def runBatchFileToFetchLogs(self, file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs", batch_file_name="Logcat.bat"):
        os.chdir(file_path)
        process = subprocess.Popen(batch_file_name, shell=True)
        return process

    def terminateBatchFileProcess(self, process, wait_time=None):
        if wait_time is not None:
            sleep(wait_time)
        sleep(2)
        process.terminate()

    def check_if_user_is_logged_in(self):
        try:
            self.poco("Home").wait_for_appearance(timeout=20)
        except:
            raise Exception("User not Logged In")

    def get_name(self, seperate=True):
        first_name = self.poco("android.widget.EditText").get_text()
        last_name = self.poco("android.widget.EditText")[1].get_text()
        if seperate:
            return first_name, last_name
        return first_name+last_name

    def noErrorOccurredAfterPrinting(self):
        try:
            self.poco("Label").wait_for_appearance(timeout=20)
        except:
            try:
                self.poco("Sign In").wait_for_appearance(timeout=20)
            except:
                raise Exception("Reached sign in page after printing.")
            raise Exception("Error occurred after printing.")

    def noErrorOccurredAfterSwitchingApps(self):
        try:
            self.poco("Buy More Labels").wait_for_appearance(timeout=20)
        except:
            try:
                self.poco("Sign In").wait_for_appearance(timeout=20)
            except:
                raise Exception("Reached sign in page after printing.")
            raise Exception("Error occurred after printing.")

    def updateNotificationSettings(self):
        self.poco("Documents are printed").click()

    def goToCommonTabPrinterSettings(self):
        self.poco(nameMatches="(?s).*Common.*").click()

    def Change_Darkness_Level_Bar(self, newvalue=50 ):
        seekbar = self.poco(type="android.widget.SeekBar")
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage
        seekbar.click([click_x, seekbar_size[1] / 2])

    def checkThemeChanged(self):
        try:
            self.poco("Modern").child("android.widget.RadioButton", checked=True).wait_for_appearance(timeout=10)
            x=1/0
        except ZeroDivisionError:
            raise Exception("Theme not changed")
        except Exception as e:
            pass

    def checkIfHelpPagesArePresent(self):
        try:
            self.poco("Support", enabled=True).exists()
            self.poco("FAQs", enabled=True).exists()
            self.poco("Contact Us", enabled=True).exists()
            try:
                self.poco("Live Chat", enabled=True).exists()
            except:
                self.poco("Chat currently unavailable", enabled=False).exists()
        except:
            raise Exception("Help pages are not available.")

    def get_token(self, file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt"):
        with open(file_path, 'r') as file:
            file_content = file.read()
        access_tokens = re.findall(r'access_token:\s*(\S+)', file_content)
        if access_tokens:
            return access_tokens[-1]
        else:
            raise Exception("No access tokens found.")

    def checkTokenRefreshed(self, old_token):
        new_token = self.get_token()
        if new_token != old_token:
            return new_token
        else:
            raise Exception("Token not refreshed.")
