import pandas as pd
import sys
import json
from time import sleep
from api_calls import *

# Replace with the path to your Excel file
file_path = '../../AEMS/execution.xlsx'
df = pd.read_excel(file_path)

# Extract values from the specified columns
station_name = df['station_name'].iloc[0]
user_name = df['user_name'].iloc[0]
firmwarename = df['firmwarename'].iloc[0]

exec_id = new_execution(station_name, user_name)
print("Execution ID:", exec_id)

deviceDetails(exec_id, firmwarename)
insert_tool_version(exec_id)

# Step 1: Read the CSV file
df = pd.read_csv('Testcases.csv')  # Ensure 'Testcases.csv' is in the same directory or provide the full path

# Debug: Print the first few rows of the dataframe
print("Testcases DataFrame Head:\n", df.head())

# Step 2: Extract distinct subareas
distinct_subareas = df['Subarea'].unique()

if len(sys.argv) > 1:
    generated_list_json = sys.argv[1]
    generated_list = json.loads(generated_list_json)
else:
    generated_list = []

if len(generated_list) == 0:
    subarea_dict = {}
    subarea_string_list = []
    id_counter = 1
    for subarea in distinct_subareas:
        subarea_string_list.append(f"0,{id_counter},{subarea}")
        subarea_dict[subarea] = id_counter
        id_counter += 1

    subarea_string = "|".join(subarea_string_list)

    print("Subarea String:", subarea_string)
    print("Subarea Dictionary:", subarea_dict)

    test_cases = ""
    # Step 4: Populate the dictionary with test cases
    for index, row in df.iterrows():
        subarea = row['Subarea']
        test_case_id = str(row['Testcase_ID'])  # Ensure test_case_id is treated as a string
        if subarea in subarea_dict:
            test_cases += f"{subarea_dict[subarea]},{test_case_id},{test_case_id}|"

    # Remove the trailing pipe character from test_cases
    if test_cases.endswith("|"):
        test_cases = test_cases[:-1]

    # Combine subarea_string and test_cases with a pipe character if test_cases is not empty
    if test_cases:
        case_names = subarea_string + "|" + test_cases
    else:
        case_names = subarea_string

    print("Case Names:", case_names)
    initialize_cases_hierarchy(exec_id, case_names)

else:
    distinct_subareas = generated_list
    print("Distinct Subareas:", distinct_subareas)

    subarea_dict = {}
    subarea_string_list = []
    id_counter = 1
    for subarea in distinct_subareas:
        subarea_string_list.append(f"0,{id_counter},{subarea}")
        subarea_dict[subarea] = id_counter
        id_counter += 1

    subarea_string = "|".join(subarea_string_list)

    print("Subarea String:", subarea_string)
    print("Subarea Dictionary:", subarea_dict)

    test_cases = ""
    # Step 4: Populate the dictionary with test cases
    for index, row in df.iterrows():
        subarea = row['Subarea']
        test_case_id = str(row['Testcase_ID'])  # Ensure test_case_id is treated as a string
        if subarea in subarea_dict:
            test_cases += f"{subarea_dict[subarea]},{test_case_id},{test_case_id}|"

    # Remove the trailing pipe character from test_cases
    if test_cases.endswith("|"):
        test_cases = test_cases[:-1]

    # Combine subarea_string and test_cases with a pipe character if test_cases is not empty
    if test_cases:
        case_names = subarea_string + "|" + test_cases
    else:
        case_names = subarea_string

    print("Case Names:", case_names)
    initialize_cases_hierarchy(exec_id, case_names)

sleep(1)
json_left_id = get_case_hierarchy(exec_id)
sleep(1)

# Decode the byte string to a regular string
decoded_string = json_left_id.decode('utf-8')

# Parse the JSON string
json_data = json.loads(decoded_string)

# Populate the leftId dictionary, filtering out empty tags
result = {item["tag"]: item["leftID"] for item in json_data if "tag" in item and item["tag"] and "leftID" in item}

print("Execution ID:", exec_id)
print("LeftID Dictionary:", result)

# Verify that all test cases are included in result
for test_case_id in df['Testcase_ID'].astype(str).unique():  # Convert IDs to strings for comparison
    if test_case_id not in result:
        print(f"Test Case ID {test_case_id} not found in result")

# Save results
with open('../../AEMS/store.py', 'w') as f:
    f.write('leftId = ' + repr(result) + '\n')
    f.write('execID = ' + str(exec_id))

print("Done")
