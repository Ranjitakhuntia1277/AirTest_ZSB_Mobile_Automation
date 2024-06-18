"""
Sphere result integration with ATF
"""
import os

import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

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
        "testDataSource": "ZSB Mobile Automation",
        "resultsSchema": "INProgress"
    }
    api_response = session.post(new_execution_url, json=new_execution_json, timeout=60)
    exec_id = api_response.json()
    print("this is the execution ID:", exec_id)

    return exec_id


def deviceDetails(execID, hardwarename="", firmwarename="Testing"):
    device_details_url = path + 'ExecEngineDevice/Insert_Device'
    data = {
        "executionId": execID,
        "version": "1",
        "hardwareID": 0,
        "firmwareID": 0,
        "hardwareName": hardwarename,
        "firmwareName": firmwarename,
        "serialNumber": "",
        "communicationDetails": "Network - NW: 172.30.3.3:9100",
        "project": "ZSB Mobile Automation",
        "timings": "",
        "dependencies": "",
        "learnMode": "",
        "basePath": ""
    }
    session.put(device_details_url, json=data, timeout=60,verify=False)


def insert_tool_version(execid, version):
    """
    Insert the tool and version.
    :return:
    """
    insert_tool_version_url = path + "CommonExecution/InsertToolVersion"
    insert_tool_version_json = {
        "executionId": execid,
        "appName": "Airtest",
        "version": version
    }
    session.put(insert_tool_version_url, json=insert_tool_version_json, timeout=60,verify=False)


def start_set_up(exec_id, setup_id, setup_name):
    start_set_up_url = path + "ExecEngineSetup/start_set_up"
    data = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftID": 1,
        "setupNumber": 0,
        "setupID": setup_id,
        "setupName": setup_name
    }
    session.put(start_set_up_url, json=data, timeout=60)


def end_set_up(exec_id, exec_time):
    end_set_up_url = path + "ExecEngineSetup/EndSetup"
    data = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftID": 1,
        "setupNumber": 0,
        "executionTime": exec_time
    }
    session.put(end_set_up_url, json=data, timeout=60)



def start_main(exec_id,leftId):
    start_main_loop_url = path + "ExecEngineMain/StartMain"
    start_main_json = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftId": leftId
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60,verify=False)


def end_main(exec_id,leftId,exec_time):
    start_main_loop_url = path + "ExecEngineMain/EndMain"
    start_main_json = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftId": leftId,
        "executionTime": exec_time
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60,verify=False)


def insert_device(exec_id, version, hardware_name, firmware_name, serial_number, communication_details):
    """
    Insert the information of printer, station etc.
    :param hardware_name:
    :param firmware_name:
    :param serial_number:
    :param communication_details:
    :return:
    """
    insert_device_url = path + "ExecEngineDevice/Insert_Device"
    insert_device_json = {
        "executionId": exec_id,
        "version": version,
        "hardwareID": 0,
        "firmwareID": 0,
        "hardwareName": hardware_name,
        "firmwareName": firmware_name,
        "serialNumber": serial_number,
        "communicationDetails": communication_details,
        "project": "ZSB Automation",
        "timings": "",
        "dependencies": "",
        "learnMode": "",
        "basePath": ""
    }
    session.put(insert_device_url, json=insert_device_json, timeout=60)


def start_execution_loop(exec_id):
    """
    Start the execution in loop.
    :return:
    """
    start_execution_loop_url = path + "ExecutionLoop/StartExecutionLoop"
    start_execution_loop_json = {
        "executionId": exec_id,
        "loopIndex": 1
    }
    session.put(start_execution_loop_url, json=start_execution_loop_json, timeout=60,verify=False)


def insert_case_details(execid, report_text, errmsg):
    insert_case_details_url = path + "ExecEngineCase/Insert_CaseDetails"

    insert_case_details_json = {
        "executionId": execid,
        "loopIndex": 0,
        "leftID": 0,
        "reportText": report_text,
        "errorMessage": errmsg
    }
    session.post(insert_case_details_url, json=insert_case_details_json, timeout=60)


def insert_case_results(execid, loopindex, leftId, result, exec_time, reportext, errormsg):
    """
    Update the execution result for each case.
    :param total_suite_result_list:
    :return:
    """
    insert_case_results_url = path + "ExecEngineCase/Insert_CaseResult"

    insert_case_results_loop_json = {
        "executionId": execid,
        "loopIndex": loopindex,
        "leftID": leftId,
        "result": result,
        "executionTime": exec_time,
        "reportText": reportext,
        "errorMessage": errormsg

    }

    session.post(insert_case_results_url, json=insert_case_results_loop_json, timeout=60)


def upload_case_files(execid, output_directory):
    """
    Upload the files in local, like selenium report, ATF report etc.
    :param output_directory:
    :return:
    """
    count = 0
    for file in os.listdir(output_directory):
        ext = os.path.splitext(file)
        if ext[1] in ('.log', '.html', '.xml'):
            with open(os.path.join(output_directory, file), "rb") as logs:
                files = {"file": logs}
                upload_case_files_url = f"{path}FileSave/UploadCaseFile"
                params = {
                    "executionId": execid,
                    "caseId": 1,
                    "leftID": count,
                    "fileName": ext[0]
                }
                session.post(upload_case_files_url, files=files, timeout=60, params=params)
            count += 2


def end_execution_loop(execid):
    """
    End execution in loop.
    :return:
    """
    end_execution_loop_url = path + "ExecutionLoop/EndExecutionLoop"
    end_execution_loop_json = {
        "executionId": execid,
        "loopIndex": 1
    }
    session.post(end_execution_loop_url, json=end_execution_loop_json, timeout=60,verify=False)


def end_execution(exec_id):
    """
    Stop the execution with execution id.
    :return:
    """
    end_execution_url = path + "CommonExecution/EndExecution/" + str(exec_id)
    session.post(end_execution_url, timeout=60)


def get_test_case(exec_id):
    url = path + "ExecEngineHierarchy/Get_CasesHierarchy/" + str(exec_id)
    # print(u)
    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(url,verify=False)
    # print(response)
    # print(response.content)

    resp = session.get(url, verify=False)
    return resp


# get_test_case(912240)


def start_cleanup(exec_id, cleanup_id, cleanup_name):
    start_cleanup_url = path + "ExecEngineCleanup/start_cleanup"
    data = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftID": 1,
        "cleanUpNumber": 0,
        "cleanUpId": cleanup_id,
        "cleanUpName": cleanup_name
    }
    session.put(start_cleanup_url, json=data, timeout=60)


def end_cleanup(exec_id, exec_time):
    end_cleanup_url = path + "ExecEngineCleanup/EndCleanup"
    data = {
        "executionId": exec_id,
        "loopIndex": 1,
        "leftID": 1,
        "cleanUpNumber": 0,
        "executionTime": exec_time
    }
    session.put(end_cleanup_url, json=data, timeout=60)


def initialize_cases_hierarchy(exec_id, casenames):
    initialize_cases_hierarchy_url = path + "AEMSCaseHierarchy/Initialize_CasesHierarchy"
    initialize_cases_hierarchy_json = {
        "executionID": exec_id,
        "delim1": "|",
        "delim2": ",",
        "table": casenames
    }
    session.put(initialize_cases_hierarchy_url, json=initialize_cases_hierarchy_json, timeout=60,verify=False)



def initializecaseshirarchy(exec_id, case_id, left_id, case_name):
    initialize_cases_hierarchy_url = path + "ExecEngineHierarchy/InitializeCasesHierarchy"
    initialize_cases_hierarchy_json = {
        "executionID": exec_id,
        "delim": ",",
        "caseIDs": case_id,
        "leftIDs": left_id,
        "rightIDs": "string",
        "depths": "string",
        "caseNames": case_name
    }
    session.put(initialize_cases_hierarchy_url, json=initialize_cases_hierarchy_json, timeout=60)


def insert_step(exec_id,left_id, ordinal_number, set_up_number, step_name, result, exec_time):
    insert_step_url = path + "ExecEngineStep/Insert_Step"
    insert_step_json = {
        "executionID": exec_id,
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

    session.put(insert_step_url, json=insert_step_json, timeout=60,verify=False)


def insert_stepAttributes(exec_id, set_up_number, text):
    insert_step_url = path + "ExecEngineStep/Insert_StepAttributes"
    insert_step_att_json = {
        "executionID": exec_id,
        "loopIndex": 1,
        "leftID": 1,
        "type": "string",
        "setupNumber": set_up_number,
        "attributeText": text
    }

    session.put(insert_step_url, json=insert_step_att_json, timeout=60)


def insert_stepDetails(exec_id, left_id, ordinal_number, report_text, error_msg):
    insert_step_url = path + "ExecEngineStep/Insert_StepDetails"
    insert_step_json = {
        "executionID": exec_id,
        "loopIndex": 1,
        "leftID": left_id,
        "type": "string",
        "setupNumber": "0",
        "ordinalNumber": ordinal_number,
        "reportText": report_text,
        "errorMessage": error_msg
    }

    session.put(insert_step_url, json=insert_step_json, timeout=60)

#
# deviceDetails(execID,"Pixel 7 Pro","14.0.11")
# insert_tool_version(execID,"2")
#
initialize_cases_hierarchy(execID, "0,47972,Verify the Label Alignment Demo feature|47972,47973,Verify the Printer Demo feature|0,45678,sample1|45678,45789,sample2|0,46897,outer sample")
#
# start_execution_loop(execID)
#
# start_main(execID,2)
#
# stepID = 0
# stepName = "On a mobile device, from the menu click Printer Settings."
# ordinalNum = 1
#
# insert_step(execID, 2,ordinalNum, stepID, stepName, "Fail", 0)
# insert_stepDetails(execID,2,1,"did not match as expected","did not match")
#
# #





















