import os
import re
import subprocess
import time
import datetime


def fetch_lines_between_words(
        file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt",
        start_word='exchangeCode:body:', end_word='3599'):
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
            print(result)
        else:
            print(f"No valid {start_word} and {end_word} found in the correct order.")


def get_token(file_path="C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs\\logs.txt"):
    with open(file_path, 'r') as file:
        file_content = file.read()
    access_tokens = re.findall(r'access_token:\s*(\S+)', file_content)
    if access_tokens:
        return access_tokens[-1]
    else:
        raise Exception("No access tokens found.")


def runBatchFileToFetchLogs(self):
    file_path = "C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\\\ZSB_Mobile\\ADB_logs"
    batch_file_name = "Logcat.bat"
    os.chdir(file_path)
    process = subprocess.Popen(batch_file_name, shell=True)
    time.sleep(20)
    process.terminate()


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
def test_get_tokens():
    pass
    lines_between_words = wildcard_search("getLocalTokens")
    print("1:\n", lines_between_words)  # Print the lines, removing leading/trailing whitespace
    if wildcard_search():
        print("Wildcard query found in the file")
    else:
        print("Wildcard query not found in the file")
    runBatchFileToFetchLogs()

    lines_between_words = fetch_lines_between_words()
    print("2:\n", lines_between_words)  # Print the lines, removing leading/trailing whitespace
    x=1/0


