import re

file_path = "C:\\Users\\JD4936\\OneDrive - Zebra Technologies\\Documents\\AirTest_ZSB_Mobile_Automation\\ZSB_Mobile\\ADB_logs\\Logs.txt"


def wildcard_search(wildcard="exchangeCode", filepath=file_path):
    if wildcard == "exchangeCode":
        wildcard_query = '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*"expires_in":"3599"'
    # elif wildcard == "getLocalTokens":
    else:
        wildcard_query = '.*flutter: getLocalTokens: access_token:.*'
    with open(filepath, 'r') as file:
        file_content = file.read()
        if re.search(wildcard_query, file_content, re.DOTALL):
            return True
    return False


print(wildcard_search())

# wildcard_query = '(?s).*exchangeCode:body:.*{.*"access_token".*"refresh_token".*expires_in'
# regex = re.compile(wildcard_query)
# print(regex)
# with open(file_path, 'r') as file:
#     file_content = file.read()
#     if re.search(regex, file_content):
#         print(re.search(regex, file_content))
