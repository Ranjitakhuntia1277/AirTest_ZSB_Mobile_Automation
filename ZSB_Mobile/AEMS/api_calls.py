import gzip
import os
import shutil
import subprocess
import zipfile

import requests

path = "https://tdmsapi.zebra.lan/api/"

session = requests.Session()


def new_execution(station_name, user_name):
    """
    Create a new execution id.
    :param station_name:
    :param user_name:
    :return:
    """
    new_execution_url = path + "CommonExecution/NewExecution"
    new_execution_json = {
        "stationName": station_name,
        "operatorName": user_name,
        "loopCount": 1,
        "duttype": "",
        "testDataSource": "Scoville Mobile Automation",
        "resultsSchema": "InProgress"
    }
    api_response = session.post(new_execution_url, json=new_execution_json, timeout=60, verify=False)
    exec_id = api_response.json()
    print("this is the execution ID:", exec_id)

    return exec_id


def get_android_device_details():
    adb_devices = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    devices = adb_devices.stdout.strip().split('\n')[1:]
    connected_devices = [device.split()[0] for device in devices if device]
    if not connected_devices:
        raise Exception("No Android devices connected")
    device_serial = connected_devices[0]
    adb_model = subprocess.run(['adb', '-s', device_serial, 'shell', 'settings', 'get', 'global', 'device_name'],
                               capture_output=True, text=True)
    device_name = adb_model.stdout.strip()
    return device_name, device_serial


def get_ios_device_details():
    idevice_list = subprocess.run(['idevice_id', '-l'], capture_output=True, text=True)
    connected_devices = idevice_list.stdout.strip().split('\n')
    if not connected_devices or connected_devices == ['']:
        raise Exception("No iOS devices connected")
    device_serial = connected_devices[0]
    idevice_info = subprocess.run(['ideviceinfo', '-u', device_serial], capture_output=True, text=True)
    device_info = idevice_info.stdout.strip().splitlines()
    device_name = ""
    for line in device_info:
        if "DeviceName" in line:
            device_name = line.split(":")[1].strip()
            break
    return device_name, device_serial


def get_device_details():
    try:
        return get_android_device_details()
    except Exception as e:
        print(f"Android device check failed: {e}")

    try:
        return get_ios_device_details()
    except Exception as e:
        print(f"iOS device check failed: {e}")
        raise Exception("No supported devices connected")


def deviceDetails(execID, firmwarename):
    device_name, device_serial = get_device_details()
    device_details_url = path + 'ExecEngineDevice/Insert_Device'
    device_details_json = {
        "executionId": execID,
        "version": "",
        "hardwareID": 0,
        "firmwareID": 0,
        "hardwareName": device_name,
        "firmwareName": firmwarename,
        "serialNumber": device_serial,
        "communicationDetails": "None",
        "project": "ZSB Mobile Automation",
        "timings": "",
        "dependencies": "",
        "learnMode": "",
        "basePath": ""
    }
    session.put(device_details_url, json=device_details_json, timeout=60, verify=False)


def insert_tool_version(execID):
    insert_tool_version_url = path + "CommonExecution/InsertToolVersion"
    insert_tool_version_json = {
        "executionId": execID,
        "appName": 'Airtest',
        "version": "IDE v1.2.17"
    }
    session.put(insert_tool_version_url, json=insert_tool_version_json, timeout=60, verify=False)


def start_set_up(execID, setup_id, setup_name):
    start_set_up_url = path + "ExecEngineSetup/start_set_up"
    start_set_up_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": 1,
        "setupNumber": 0,
        "setupID": setup_id,
        "setupName": setup_name
    }
    session.put(start_set_up_url, json=start_set_up_json, timeout=60)


def end_set_up(execID, exec_time):
    end_set_up_url = path + "ExecEngineSetup/EndSetup"
    end_set_up_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": 1,
        "setupNumber": 0,
        "executionTime": exec_time
    }
    session.put(end_set_up_url, json=end_set_up_json, timeout=60)


def start_main(execID, leftId):
    start_main_loop_url = path + "ExecEngineMain/StartMain"
    start_main_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftId": leftId
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60, verify=False)


def end_main(execID, leftId, exec_time):
    start_main_loop_url = path + "ExecEngineMain/EndMain"
    start_main_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftId": leftId,
        "executionTime": exec_time
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60, verify=False)


def insert_device(execID, hardware_name, firmware_name, serial_number, communication_details):
    """
    Insert the information of printer, station etc.
    :param execID:
    :param hardware_name:
    :param firmware_name:
    :param serial_number:
    :param communication_details:
    :return:
    """
    insert_device_url = path + "ExecEngineDevice/Insert_Device"
    insert_device_json = {
        "executionId": execID,
        "version": "IDE v1.2.17",
        "hardwareID": 0,
        "firmwareID": 0,
        "hardwareName": hardware_name,
        "firmwareName": firmware_name,
        "serialNumber": serial_number,
        "communicationDetails": communication_details,
        "project": "Scoville Mobile Automation",
        "timings": "",
        "dependencies": "",
        "learnMode": "",
        "basePath": ""
    }
    session.put(insert_device_url, json=insert_device_json, timeout=60)


def start_execution_loop(execID):
    """
    Start the execution in loop.
    :return:
    """
    start_execution_loop_url = path + "ExecutionLoop/StartExecutionLoop"
    start_execution_loop_json = {
        "executionId": execID,
        "loopIndex": 1
    }
    session.put(start_execution_loop_url, json=start_execution_loop_json, timeout=60, verify=False)


def insert_case_details(execID, report_text, left_id, errmsg):
    insert_case_details_url = path + "ExecEngineCase/Insert_CaseDetails"

    insert_case_details_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": left_id,
        "reportText": report_text,
        "errorMessage": errmsg
    }
    session.post(insert_case_details_url, json=insert_case_details_json, timeout=60)


def insert_case_results(execID, leftId, result, exec_time, reportext, errormsg):
    """
    Update the execution result for each case.
    :param execID:
    :param errormsg:
    :param reportext:
    :param exec_time:
    :param result:
    :param leftId:
    :return:
    """
    insert_case_results_url = path + "ExecEngineCase/Insert_CaseResult"

    insert_case_results_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": leftId,
        "result": result,
        "executionTime": exec_time,
        "reportText": reportext,
        "errorMessage": errormsg

    }

    session.post(insert_case_results_url, json=insert_case_results_json, timeout=60, verify=False)


def upload_case_files(execID, output_directory, test_run_start_time):
    """
    Upload the files in local, like selenium report, ATF report, etc.
    :param execID: Execution ID for the test case.
    :param output_directory: Directory where the files are located.
    :return: None
    """
    count = 0
    for file in os.listdir(output_directory):
        file_path = os.path.join(output_directory, file)
        file_name, file_extension = os.path.splitext(file)

        if os.path.getmtime(file_path) < test_run_start_time:
            continue

        print(f"Found file: {file}, extension: {file_extension}")

        if file_extension == '.txt':
            gz_filepath = os.path.join(output_directory, file_name)  # Save as original name without .zip extension
            gz_filename = f"{file_name}.gz"

            # Create a zip file with the original name (without double .zip)
            with open(file_path, 'rb') as f_in, gzip.open(gz_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

            # Upload the zip file with the correct name during the upload
            with open(gz_filepath, "rb") as logs:
                files = {"file": logs}
                upload_case_files_url = path + "FileSave/UploadCaseFile"
                params = {
                    "executionId": execID,
                    "caseId": 1,
                    "leftID": count,
                    "fileName": gz_filename  # Add .zip extension here for correct upload
                }
                print(f"Uploading {gz_filename} to {upload_case_files_url} with params {params}")
                requests.post(upload_case_files_url, files=files, timeout=60, params=params, verify=False)

        else:
            # For non-txt files, upload them as they are
            with open(file_path, "rb") as logs:
                files = {"file": logs}
                upload_case_files_url = path + "FileSave/UploadCaseFile"
                params = {
                    "executionId": execID,
                    "caseId": 1,
                    "leftID": count,
                    "fileName": file_name
                }
                print(f"Uploading {file} to {upload_case_files_url} with params {params}")
                requests.post(upload_case_files_url, files=files, timeout=60, params=params, verify=False)

        count += 2

# def upload_case_files(execID, output_directory):
#     """
#     Upload the files in local, like selenium report, ATF report etc.
#     :param execID:
#     :param output_directory:
#     :return:
#     """
#     count = 0
#     for file in os.listdir(output_directory):
#         ext = os.path.splitext(file)
#         print(f"Found file: {file}, extension: {ext[1]}")
#         if ext[1] in ('.txt', '.html', '.xml', '.png', '.log'):
#             with open(os.path.join(output_directory, file), "rb") as logs:
#                 files = {"file": logs}
#                 upload_case_files_url = path + "FileSave/UploadCaseFile"
#                 params = {
#                     "executionId": execID,
#                     "caseId": 1,
#                     "leftID": count,
#                     "fileName": ext[0]
#                 }
#                 print(f"Uploading {file} to {upload_case_files_url} with params {params}")
#                 session.post(upload_case_files_url, files=files, timeout=60, params=params, verify=False)
#             count += 2


def end_execution_loop(execID):
    """
    End execution in loop.
    :return:
    """
    end_execution_loop_url = path + "ExecutionLoop/EndExecutionLoop"
    end_execution_loop_json = {
        "executionId": execID,
        "loopIndex": 1
    }
    session.post(end_execution_loop_url, json=end_execution_loop_json, timeout=60, verify=False)


def end_execution(execID):
    """
    Stop the execution with execution id.
    :return:
    """
    end_execution_url = path + "CommonExecution/EndExecution/" + str(execID)
    session.post(end_execution_url, timeout=60, verify=False)


def get_case_hierarchy(execID):
    url = path + "ExecEngineHierarchy/Get_CasesHierarchy/" + str(execID)
    # print(u)
    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(url, verify=False)
    # print(response)
    # print(response.content)

    resp = session.get(url, verify=False)
    print(resp)
    print(resp.content)
    return resp.content


def start_cleanup(execID, cleanup_id, cleanup_name):
    start_cleanup_url = path + "ExecEngineCleanup/start_cleanup"
    start_cleanup_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": 1,
        "cleanUpNumber": 0,
        "cleanUpId": cleanup_id,
        "cleanUpName": cleanup_name
    }
    session.put(start_cleanup_url, json=start_cleanup_json, timeout=60, verify=False)


def end_cleanup(execID, exec_time):
    end_cleanup_url = path + "ExecEngineCleanup/EndCleanup"
    end_cleanup_json = {
        "executionId": execID,
        "loopIndex": 1,
        "leftID": 1,
        "cleanUpNumber": 0,
        "executionTime": exec_time
    }
    session.put(end_cleanup_url, json=end_cleanup_json, timeout=60, verify=False)


def initialize_cases_hierarchy(execID, casenames):
    initialize_cases_hierarchy_url = path + "AEMSCaseHierarchy/Initialize_CasesHierarchy"
    initialize_cases_hierarchy_json = {
        "executionID": execID,
        "delim1": "|",
        "delim2": ",",
        "table": casenames
    }
    session.put(initialize_cases_hierarchy_url, json=initialize_cases_hierarchy_json, timeout=60, verify=False)


def initializecaseshirarchy(execID, case_id, left_id, case_name):
    initialize_cases_hierarchy_url = path + "ExecEngineHierarchy/InitializeCasesHierarchy"
    initialize_cases_hierarchy_json = {
        "executionID": execID,
        "delim": ",",
        "caseIDs": case_id,
        "leftIDs": left_id,
        "rightIDs": "string",
        "depths": "string",
        "caseNames": case_name
    }
    session.put(initialize_cases_hierarchy_url, json=initialize_cases_hierarchy_json, timeout=60)


def insert_step(execID, left_id, ordinal_number, set_up_number, step_name, result, exec_time):
    insert_step_url = path + "ExecEngineStep/Insert_Step"
    insert_step_json = {
        "executionID": execID,
        "loopIndex": 1,
        "leftID": left_id,
        "type": "string",
        "setupNumber": "0",
        "ordinalNumber": ordinal_number,
        "stepID": set_up_number,
        "stepTypeName": "",
        "stepName": step_name,
        "result": result,
        "executionTime": exec_time,
        "duttime": 0
    }

    session.put(insert_step_url, json=insert_step_json, timeout=60, verify=False)


def insert_stepAttributes(execID, set_up_number, text):
    insert_step_url = path + "ExecEngineStep/Insert_StepAttributes"
    insert_step_att_json = {
        "executionID": execID,
        "loopIndex": 1,
        "leftID": 1,
        "type": "string",
        "setupNumber": set_up_number,
        "attributeText": text
    }

    session.put(insert_step_url, json=insert_step_att_json, timeout=60)


def execution_status(execID, exec_status="Executed", reporttext=""):
    execution_status_url = path + "ExecutionStatus"
    execution_status_json = {
        "executionID": execID,
        "execStatus": exec_status,
        "reportText": reporttext
    }

    session.put(execution_status_url, json=execution_status_json, timeout=60, verify=False)


def result_testcaseproject(execID, platform_id, submittal, test_result, comments, test_username):
    """
    Submit test results.
    :param execID:
    :param platform_id: ID of the platform
    :param submittal: Submittal information
    :param test_result: Test result (e.g., "Passed", "Failed")
    :param comments: Additional comments or notes
    :param test_username: Username of the tester
    :return: Response from the API
    """
    insert_step_url = path + "ExecEngineStep/Insert_StepDetails"
    insert_step_json = {
        "testcaseProjectId": execID,
        "platformId": platform_id,
        "submittal": submittal,
        "testResult": test_result,
        "comments": comments,
        "testUsername": test_username
    }

    session.post(insert_step_url, json=insert_step_json, timeout=60, verify=False)


def insert_stepDetails(execID, left_id, ordinal_number, report_text, error_msg):
    insert_step_url = path + "ExecEngineStep/Insert_StepDetails"
    insert_step_json = {
        "executionID": execID,
        "loopIndex": 1,
        "leftID": left_id,
        "type": "string",
        "setupNumber": 0,
        "ordinalNumber": ordinal_number,
        "reportText": report_text,
        "errorMessage": error_msg
    }

    session.put(insert_step_url, json=insert_step_json, timeout=60, verify=False)
