from api_calls import *
import webbrowser
import pandas as pd
import sys
import json
from time import sleep
import sys
import logging
import requests


file_path = 'execution.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Extract values from the specified columns
station_name = df['station_name'].iloc[0]
user_name = df['user_name'].iloc[0]
tool_version = str(df['tool_version'].iloc[0])
hardwarename = df['hardwarename'].iloc[0]
firmwarename = df['firmwarename'].iloc[0]

exec_id = new_execution(station_name, user_name)
print(exec_id)
# exec_id = 938001

insert_tool_version(exec_id, tool_version)
deviceDetails(exec_id, hardwarename, firmwarename)

# Step 1: Read the Excel file
df = pd.read_csv('Testcases.csv')  # Change 'test_cases.xlsx' to your actual file path

# Step 2: Extract distinct subareas
distinct_subareas = df['Subarea'].unique()

generated_list_json = sys.argv[1]
generated_list = json.loads(generated_list_json)

if len(generated_list) == 0:

    subarea_dict = {}
    subarea_string_list = []
    id_counter = 1
    for subarea in distinct_subareas:
        subarea_string_list.append(f"0,{id_counter},{subarea}")
        subarea_dict[subarea] = id_counter
        id_counter += 1

    subarea_string = "|".join(subarea_string_list)

    print(subarea_string)
    print(subarea_dict)

    test_cases = ""
    # Step 4: Populate the dictionary with test cases
    for index, row in df.iterrows():
        subarea = row['Subarea']
        test_case_id = row['Testcase_ID']
        test_description = row['Test_Description']
        test_cases += str(subarea_dict[subarea]) + "," + str(test_case_id) + "," + str(test_case_id) + "|"

    case_names = subarea_string + "|" + test_cases

    print(case_names)
    initialize_cases_hierarchy(exec_id, case_names)

else:
    distinct_subareas = generated_list
    print("distinct subareas", distinct_subareas)

    subarea_dict = {}
    subarea_string_list = []
    id_counter = 1
    for subarea in distinct_subareas:
        subarea_string_list.append(f"0,{id_counter},{subarea}")
        subarea_dict[subarea] = id_counter
        id_counter += 1

    subarea_string = "|".join(subarea_string_list)

    print("subarea string", subarea_string)
    print("subarea dict", subarea_dict)

    test_cases = ""
    # Step 4: Populate the dictionary with test cases
    for index, row in df.iterrows():
        subarea = row['Subarea']
        test_case_id = row['Testcase_ID']
        test_description = row['Test_Description']
        if subarea in subarea_dict:
            test_cases += str(subarea_dict[subarea]) + "," + str(test_case_id) + "," + str(test_case_id) + "|"
        else:
            pass

    case_names = subarea_string + "|" + test_cases

    print(case_names)
    initialize_cases_hierarchy(exec_id, case_names)

sleep(1)
json_left_id = get_case_hierarchy(exec_id)
sleep(1)

# Decode the byte string to a regular string
decoded_string = json_left_id.decode('utf-8')

# Parse the JSON string
json_data = json.loads(decoded_string)

result = {item["tag"]: item["leftID"] for item in json_data}

print(exec_id, result)

with open('store.py', 'w') as f:
    f.write('leftId = ' + repr(result) + '\n')
    f.write('execID = ' + str(exec_id))

print("done")

# url = 'https://aems.us.zebra.lan/Report/Tools?executionID='+str(exec_id)
#
# webbrowser.get('edge').open_new_tab(url)
