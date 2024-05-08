import os
import re
import subprocess
import time


def fetch_lines_between_words(file_path, start_word, end_word):
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


def wildcard_search(file_path, wildcard_query):
    with open(file_path, 'r') as file:
        file_content = file.read()
        if re.search(wildcard_query, file_content, re.DOTALL):
            return True
    return False


file_path = os.path.join(os.path.expanduser('~'), "Documents\\New_ZSB_Automation\\ZSB_Mobile\\ADB_logs",
                         "Logs.txt")  # Replace with the path to your text file
batch_file_path = os.path.join(os.path.expanduser('~'), "Documents\\New_ZSB_Automation\\ZSB_Mobile\\ADB_logs",
                               "Logcat.bat")
start_word = "exchangeCode:body:"  # Replace with the starting word
end_word = "\"expires_in\":\"3599\""  # Replace with the ending word

# lines_between_words = fetch_lines_between_words(file_path, start_word, end_word)
# print("1", lines_between_words)  # Print the lines, removing leading/trailing whitespace
temp = rf"{batch_file_path}"
print(batch_file_path)
print(temp)
# print(batch_file_path)
# try:
#     process = subprocess.Popen(temp, shell=True)
#     print(process)
#     time.sleep(20)
#     if process.poll() is None:
#         process.terminate()
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")

os.system(batch_file_path)



# wildcard_query = '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*"expires_in":"3599"'  # Replace with your wildcard query

# if wildcard_search(file_path, wildcard_query):
#     print("Wildcard query found in the file")
# else:
#     print("Wildcard query not found in the file")

# lines_between_words = fetch_lines_between_words(file_path, start_word, end_word)
# print("2", lines_between_words)  # Print the lines, removing leading/trailing whitespace
