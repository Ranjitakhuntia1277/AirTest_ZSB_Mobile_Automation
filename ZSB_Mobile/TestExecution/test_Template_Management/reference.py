import re
import platform

if platform.system() == "Windows":

    file_path = "C:\\Users\JD4936\OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\ADB_logs\Logs.txt"
    logcat_file_path = "C:\\Users\JD4936\OneDrive - Zebra Technologies\Documents\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\ADB_logs"

else:
    file_path = "/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/ADB_logs/logs.txt"
    logcat_file_path = "/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/ADB_logs"


def get_token(filepath=file_path):
    with open(filepath, 'r') as file:
        file_content = file.read()
    access_tokens = re.findall(r'access_token:\s*(\S+)', file_content)
    print(access_tokens, "access tokens")
    if access_tokens:
        return access_tokens[-1]
    else:
        raise Exception("No access tokens found.")


print(get_token())
