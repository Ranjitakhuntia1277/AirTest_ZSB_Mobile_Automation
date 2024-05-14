import os
import re
import subprocess
import time
import datetime
import time
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

    def fetch_lines_between_words(self, file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt", start_word="exchangeCode:body:", end_word="\"expires_in\":\"3599\""):
        lines = ""
        found_start = False
        found_end = False

        with open(file_path, 'r') as file:
            for line in file:
                if start_word in line:
                    found_start = True

                if found_start:
                    lines += line

                if found_start and end_word in line:
                    found_end = True
                    break
        if not found_end:
            print(f"End word '{end_word}' not found after start word '{start_word}'")

        return lines

    def wildcard_search(self, file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt", wildcard_query= '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*"expires_in":"3599"'):
        with open(file_path, 'r') as file:
            file_content = file.read()
            if re.search(wildcard_query, file_content, re.DOTALL):
                return True
        return False

    def runBatchFileToFetchLogs(self):
        file_path = "C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs"
        batch_file_name = "Logcat.bat"
        os.chdir(file_path)
        process = subprocess.Popen(batch_file_name, shell=True)
        time.sleep(20)
        process.terminate()
