import os
import re
import subprocess
import time
import datetime
import random
import string
import fnmatch
from datetime import time, datetime
from airtest.core.api import *
import pytest
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
import subprocess
import platform

if platform.system() == "Windows":

    file_path = "C:\\Users\JD4936\OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\ADB_logs\Logs.txt"
    logcat_file_path = "C:\\Users\JD4936\OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\ADB_logs"

else:
    file_path = "/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/ADB_logs/logs.txt"
    logcat_file_path = "/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/ADB_logs"
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

    def fetch_lines_between_words(self, filepath=file_path, start_word='exchangeCode:body:', end_word='3599'):
        with open(filepath, 'r') as file:
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

    def wildcard_search(self, wildcard="exchangeCode", filepath=file_path):
        if wildcard == "exchangeCode":
            wildcard_query = '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*"'
        elif wildcard == "getLocalTokens":
            wildcard_query = '.*flutter :.*getLocalTokens : access_token:.*'
        with open(filepath, 'r') as file:
            file_content = file.read()
            if re.search(wildcard_query, file_content, re.DOTALL):
                return True
        return False

    def check_if_exchangeCode_message_present(self):
        if self.wildcard_search("exchangeCode"):
            pass
        else:
            raise Exception(
                "There is no message about \"exchangeCode:body:{access_token.. refresh_token...expires_in: 3599s..}\" in the adb log.")

    def check_if_getLocalTokens_information_present(self):
        if self.wildcard_search("getLocalTokens"):
            pass
        else:
            raise Exception(
                "There is no token information about \" : flutter: getLocalTokens : access_token: \" in the adb log.")

    def clear_previous_adb_logs(self):
        sleep(4)
        command = "adb logcat -c"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

    def runBatchFileToFetchLogs(self, filepath=logcat_file_path, batch_file_name="Logcat.bat"):
        sleep(3)
        os.chdir(filepath)
        process = subprocess.Popen(batch_file_name, shell=True)
        sleep(3)

    def terminateBatchFileProcess(self, process, wait_time=None):
        if wait_time is not None:
            sleep(wait_time)
        sleep(10)
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
        return first_name + last_name

    def noErrorOccurredAfterPrinting(self):
        try:
            self.poco("Label").wait_for_appearance(timeout=20)
        except:
            try:
                self.poco("Sign In").wait_for_appearance(timeout=20)
            except:
                raise Exception("Reached sign in page after printing(Error occurred after printing).")

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

    def Change_Darkness_Level_Bar(self, newvalue=50):
        seekbar = self.poco(type="android.widget.SeekBar")
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage
        seekbar.click([click_x, seekbar_size[1] / 2])

    def checkThemeChanged(self):
        try:
            self.poco("Modern").child("android.widget.RadioButton", checked=True).wait_for_appearance(timeout=10)
            x = 1 / 0
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

    def get_token(self, filepath=file_path):
        with open(filepath, 'r') as file:
            file_content = file.read()
        access_tokens = re.findall(r'access_token:\s*(\S+)', file_content)
        print(access_tokens, "access tokens")
        if access_tokens:
            return access_tokens[-1]
        else:
            raise Exception("No access tokens found.")

    def checkTokenRefreshed(self, old_token):
        new_token = self.get_token()
        if new_token != old_token:
            return new_token
        else:
            print(new_token, "->new token\n")
            print(old_token, "old token")
            raise Exception("Token not refreshed.")

    def check_bluetooth_connection_required_popup(self):
        sleep(2)
        if self.poco(nameMatches=".*Bluetooth Connection Required.*").exists():
            self.poco("Continue").click()
        if self.poco("Allow").exists():
            self.poco("Allow").click()
        elif self.poco(text="Allow").exists():
            self.poco(text="Allow").click()
        sleep(4)

    def check_if_error_displayed_when_clicking_logout_when_offline(self):
        sleep(5)
        try:
            self.poco(nameMatches="(?s).*Log out failed.*").wait_for_appearance(timeout=20)
        except:
            raise Exception("No error message displayed when trying to logout after turning off wi-fi(SMBM-2178)")

    def clear_old_logs(self):
        # Clear any existing logcat processes
        subprocess.run(["adb", "logcat", "-c"], shell=False, check=True)

    def start_adb_log_capture(self):
        self.clear_old_logs()
        path = "C:\\Users\\JD4936\\OneDrive - Zebra Technologies\\Documents\\AirTest_ZSB_Mobile_Automation\\ZSB_Mobile\\ADB_logs"
        ADB_LOG_FILE = os.path.join(path, "Logs.txt")
        subprocess.Popen(["adb", "logcat", "-v", "time", ">", {ADB_LOG_FILE}], shell=True)

    def stop_adb_log_capture(self):
        sleep(2)
        result = subprocess.run(["adb", "shell", "killall", "-2", "logcat"],
                                shell=False,
                                check=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("ADB log capture stopped successfully.")
        else:
            print(f"Failed to stop ADB log capture: {result.stderr.decode()}")
        sleep(3)
